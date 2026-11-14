#!/usr/bin/env python3
"""Systematically compare the live WordPress site with the built MkDocs site.

Run it on a machine that can reach the live site (the cloud sandbox this repo was drafted in cannot):

    mkdocs build -f mkdocs.yml                      # -> site/
    python tools/verify_migration.py --live https://www.access-nri.org.au --built site

It answers, per live URL: does a page exist (or a redirect), how much of the live text/headings/images/
attachments/links survive, and then checks the built site on its own (broken internal links, missing
anchors, hot-linked images). Output goes to report/ (summary.md, pages.csv, missing-*.txt, visual/).
Live pages are cached in .verify-cache/ so reruns are quick; it is polite (1 request/0.5 s by default).

Exit status is 1 if any threshold fails, so it can run in CI (.github/workflows/verify-migration.yml).
"""
import argparse, collections, csv, hashlib, os, re, sys, time
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote

import requests, yaml
from bs4 import BeautifulSoup

UA = {"User-Agent": "access-nri-migration-verify/1.0 (+https://github.com/ACCESS-NRI)"}
WORD = re.compile(r"[a-z0-9]+")
SIZE_SUFFIX = re.compile(r"-\d+x\d+(?=\.\w+$)")
ATTACH = re.compile(r"\.(pdf|docx?|xlsx?|pptx?|csv|zip|png|jpe?g|gif|svg|webp|mp4)$", re.I)


# ---------- fetching ----------
class Fetcher:
    def __init__(self, cache, delay):
        self.cache, self.delay, self.last = Path(cache), delay, 0.0
        self.cache.mkdir(parents=True, exist_ok=True)

    def get(self, url):
        f = self.cache / (hashlib.sha1(url.encode()).hexdigest() + ".html")
        if f.exists():
            return f.read_text("utf-8", "replace")
        wait = self.delay - (time.time() - self.last)
        if wait > 0:
            time.sleep(wait)
        try:
            cur = url
            for _ in range(5):  # follow redirects only while they stay on our host
                r = requests.get(cur, headers=UA, timeout=30, allow_redirects=False)
                loc = r.headers.get("Location")
                if r.status_code in (301, 302, 303, 307, 308) and loc:
                    cur = urljoin(cur, loc)
                    if urlparse(cur).netloc.replace("www.", "") != urlparse(url).netloc.replace("www.", ""):
                        return None
                    continue
                break
        except requests.RequestException as e:
            print("fetch failed:", url, str(e)[:80], file=sys.stderr)
            return None
        finally:
            self.last = time.time()
        if r.status_code != 200:
            return None
        text = r.content.decode("utf-8", "replace")  # WordPress often omits the charset header
        f.write_text(text, "utf-8")
        return text


def live_urls(base, fetch):
    """URLs from the WordPress sitemap(s) (wp-sitemap.xml, falling back to sitemap.xml)."""
    out, seen = {}, set()

    def walk(u):
        if u in seen:
            return
        seen.add(u)
        xml = fetch.get(u)
        if not xml:
            return
        soup = BeautifulSoup(xml, "xml")
        for sm in soup.find_all("sitemap"):
            walk(sm.loc.text.strip())
        kind = re.sub(r"^.*wp-sitemap-([a-z_]+?)-\d+\.xml$", r"\1", u) if "wp-sitemap-" in u else "page"
        for url in soup.find_all("url"):
            loc = url.loc.text.strip()
            if urlparse(loc).netloc.replace("www.", "") == urlparse(base).netloc.replace("www.", ""):
                out[loc] = kind  # person entries can point at other sites; those are not ours to migrate

    for root in ("/wp-sitemap.xml", "/sitemap.xml", "/sitemap_index.xml"):
        walk(base.rstrip("/") + root)
        if out:
            break
    return out


# ---------- extraction ----------
def clean(soup, drop):
    for t in soup.select(drop):
        t.decompose()
    return soup


def live_main(html):
    soup = BeautifulSoup(html, "lxml")
    node = None
    for sel in ("main", "#main", ".entry-content", "#content", "article"):
        node = soup.select_one(sel)
        if node and len(node.get_text(strip=True)) > 50:
            break
    node = node or soup.body
    for ul in node.select("ul:has(> li.arch-month)"):  # WordPress "Archives" month list in the sidebar
        ul.decompose()
    for h in node.select("h2,h3"):
        if h.get_text(strip=True) == "News and updates" and len(h.parent.get_text(strip=True)) < 400 and h.parent is not node:
            h.parent.decompose()  # newsletter sign-up block repeated in the live footer area
            continue
        if h.get_text(strip=True) == "Archives" or re.fullmatch(r"\d{4}", h.get_text(strip=True)):
            h.decompose()
    clean(node, "script,style,noscript,nav,header,footer,.menu,.breadcrumbs,form,.cookie,.md-top,.skip-link,.screen-reader-text,.sr-only,a[href='#main'],a[href='#content'],[aria-hidden=true]")
    return node


def built_main(html):
    soup = BeautifulSoup(html, "lxml")
    node = soup.select_one("article.md-content__inner") or soup.select_one("main") or soup.body
    clean(node, "script,style,noscript,nav,.md-source-file,.headerlink,.md-content__button,.anri-preview,.anri-banner,form")
    return node


def words(node):
    return collections.Counter(WORD.findall(node.get_text(" ").lower()))


BLOCKS = "p,li,td,th,h1,h2,h3,h4,h5,h6,dd,dt,blockquote,figcaption"


def sentences(node):
    """One entry per leaf block element (paragraph, list item, table cell, heading), so a dropped bullet is visible."""
    out = []
    for el in node.select(BLOCKS):
        if el.select_one(BLOCKS):
            continue
        t = re.sub(r"\s+", " ", el.get_text(" ")).strip()
        if len(t.split()) >= 4:
            out.append(t)
    return out


def basename(u):
    return SIZE_SUFFIX.sub("", unquote(urlparse(u).path.rsplit("/", 1)[-1])).lower()


def headings(node):
    return [re.sub(r"\s+", " ", h.get_text(" ")).strip().lower() for h in node.select("h1,h2,h3,h4")]


# ---------- mapping live URL -> built file ----------
def redirects(cfg):
    try:
        c = yaml.safe_load(open(cfg)) or {}
    except Exception:
        return {}
    for p in c.get("plugins", []) or []:
        if isinstance(p, dict) and "redirects" in p:
            m = (p["redirects"] or {}).get("redirect_maps", {}) or {}
            return {k[:-3].strip("/"): v[:-3].strip("/") for k, v in m.items() if k.endswith(".md") and v.endswith(".md")}
    return {}


def built_file(site, path, redir):
    path = path.strip("/")
    for p in (path, redir.get(path, "\0")):
        for cand in ([site / "index.html"] if p == "" else [site / p / "index.html", site / f"{p}.html"]):
            if cand.exists():
                return cand, ("redirect" if p != path else "ok")
    return None, "missing"


# ---------- checks on the built site alone ----------
def check_built_site(site):
    broken, anchors, hot, ids_cache = [], [], collections.Counter(), {}

    def ids(f):
        if f not in ids_cache:
            s = BeautifulSoup(f.read_text("utf-8", "replace"), "lxml")
            ids_cache[f] = {t.get("id") for t in s.select("[id]")} | {t.get("name") for t in s.select("a[name]")}
        return ids_cache[f]

    for f in site.rglob("*.html"):
        s = BeautifulSoup(f.read_text("utf-8", "replace"), "lxml")
        main = s.select_one("article.md-content__inner") or s
        for a in main.select("a[href]"):
            h = a["href"]
            if re.match(r"^(https?:|mailto:|tel:|javascript:)", h):
                continue
            u = urlparse(h)
            tgt = f if not u.path else (f.parent / unquote(u.path)).resolve()
            if tgt.is_dir():
                tgt = tgt / "index.html"
            if not tgt.exists():
                broken.append((str(f.relative_to(site)), h))
            elif u.fragment and tgt.suffix == ".html" and u.fragment not in ids(tgt):
                anchors.append((str(f.relative_to(site)), h))
        for im in main.select("img[src]"):
            src = im["src"]
            if src.startswith("http"):
                hot[urlparse(src).netloc] += 1
            elif not src.startswith("data:") and not (f.parent / unquote(src.split("?")[0])).exists():
                broken.append((str(f.relative_to(site)), "IMG " + src))
    return broken, anchors, hot


# ---------- optional visual pairs ----------
def screenshots(pairs, out):
    from playwright.sync_api import sync_playwright
    out.mkdir(parents=True, exist_ok=True)
    rows = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1300, "height": 900})
        for i, (live, built) in enumerate(pairs):
            for tag, u in (("live", live), ("built", built)):
                try:
                    pg.goto(u, wait_until="load", timeout=45000)
                    pg.wait_for_timeout(800)
                    pg.screenshot(path=str(out / f"{i:03d}-{tag}.png"), full_page=True)
                except Exception as e:
                    print("screenshot failed", u, e)
            rows.append(f'<h3>{live}</h3><div style="display:flex;gap:8px"><img style="width:49%" src="{i:03d}-live.png"><img style="width:49%" src="{i:03d}-built.png"></div>')
        b.close()
    (out / "index.html").write_text("<meta charset=utf-8><title>Visual pairs</title>" + "\n".join(rows))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--live", default="https://www.access-nri.org.au")
    ap.add_argument("--built", default="site", help="built MkDocs output directory")
    ap.add_argument("--config", default="mkdocs.yml", help="read redirect_maps from here")
    ap.add_argument("--out", default="report")
    ap.add_argument("--cache", default=".verify-cache")
    ap.add_argument("--delay", type=float, default=0.5)
    ap.add_argument("--min-recall", type=float, default=0.93, help="per-page share of live words found in the port")
    ap.add_argument("--kinds", default="page,post", help="sitemap kinds to require (comma list; 'all' for everything)")
    ap.add_argument("--expected-missing", default="tools/verify_expected_missing.txt",
                    help="file of live paths known not to be migrated yet (one per line)")
    ap.add_argument("--ignore-prefix", default="people-category/,author/", help="live path prefixes that are redirects/WordPress artefacts (comma list)")
    ap.add_argument("--visual", action="store_true", help="also save live/built full-page screenshot pairs")
    a = ap.parse_args()

    site, out = Path(a.built).resolve(), Path(a.out)
    out.mkdir(exist_ok=True)
    fetch = Fetcher(a.cache, a.delay)
    redir = redirects(a.config)
    known_missing = set()
    if os.path.exists(a.expected_missing):
        known_missing = {l.strip().strip("/") for l in open(a.expected_missing) if l.strip() and not l.startswith("#")}

    urls = live_urls(a.live, fetch)
    if not urls:
        sys.exit("Could not read a sitemap from the live site. Is it reachable from here?")
    want = None if a.kinds == "all" else set(a.kinds.split(","))
    host = urlparse(a.live).netloc
    rows, missing, pairs = [], [], []
    low, imgs_missing, att_missing, head_missing, text_missing = [], [], [], [], []

    # sentences appearing on >=30% of live pages are boilerplate; ignore them
    docs = {}
    for u in urls:
        if want and urls[u] not in want:
            continue
        h = fetch.get(u)
        if h:
            docs[u] = live_main(h)
    freq = collections.Counter(s for d in docs.values() for s in set(sentences(d)))
    boiler = {s for s, n in freq.items() if n >= max(3, 0.3 * len(docs))}

    ignore = tuple(x for x in a.ignore_prefix.split(",") if x)
    for u, node in sorted(docs.items()):
        path = urlparse(u).path.strip("/")
        if ignore and path.startswith(ignore):
            continue
        f, status = built_file(site, path, redir)
        row = dict(url=u, kind=urls[u], status=status, recall="", missing_words="", imgs_missing=0, att_missing=0, headings_missing=0)
        if f is None:
            row["status"] = "expected-missing" if path in known_missing else "MISSING"
            if row["status"] == "MISSING":
                missing.append(u)
            rows.append(row)
            continue
        built = built_main(f.read_text("utf-8", "replace"))
        lw, bw = words(node), words(built)
        for s in boiler:
            for w in WORD.findall(s.lower()):
                if lw[w] > 0:
                    lw[w] -= 1
        total = sum(lw.values())
        hit = sum(min(n, bw[w]) for w, n in lw.items())
        row["recall"] = 1.0 if total == 0 else round(hit / total, 3)  # an empty live page cannot lose anything
        row["missing_words"] = total - hit
        if row["recall"] < a.min_recall:
            low.append((u, row["recall"]))
        # live sentences (not site-wide boilerplate) whose words are mostly absent from the port
        bset = set(bw)
        for s in sentences(node):
            if s in boiler:
                continue
            ws = WORD.findall(s.lower())
            if ws and sum(w in bset for w in ws) / len(ws) < 0.75:
                text_missing.append((u, s))
        # headings
        bh = set(headings(built))
        hm = [h for h in headings(node) if h and h not in bh]
        row["headings_missing"] = len(hm)
        head_missing += [(u, h) for h in hm]
        # images + attachments
        bimg = {basename(i["src"]) for i in built.select("img[src]")}
        im = [basename(i["src"]) for i in node.select("img[src]") if not i["src"].startswith("data:")]
        mi = sorted({x for x in im if x and x not in bimg})
        row["imgs_missing"] = len(mi)
        imgs_missing += [(u, x) for x in mi]
        batt = {basename(x["href"]) for x in built.select("a[href]")}
        la = {basename(x["href"]) for x in node.select("a[href]") if ATTACH.search(urlparse(x["href"]).path)}
        ma = sorted(la - batt)
        row["att_missing"] = len(ma)
        att_missing += [(u, x) for x in ma]
        rows.append(row)
        pairs.append((u, f.as_uri()))

    broken, anchors, hot = check_built_site(site)

    with open(out / "pages.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    for name, data in (("missing-pages", missing), ("low-recall", low), ("missing-text", text_missing), ("missing-headings", head_missing),
                       ("missing-images", imgs_missing), ("missing-attachments", att_missing), ("broken-links", broken), ("broken-anchors", anchors)):
        (out / f"{name}.txt").write_text("\n".join("\t".join(map(str, x)) if isinstance(x, tuple) else str(x) for x in data))

    ok = sum(r["status"] in ("ok", "redirect") for r in rows)
    scored = [r["recall"] for r in rows if r["recall"] != ""]
    summary = f"""# Migration verification
- Live URLs checked ({a.kinds}): {len(rows)}
- Present in port: {ok}  (via redirect: {sum(r['status']=='redirect' for r in rows)})
- Expected missing (listed in {a.expected_missing}): {sum(r['status']=='expected-missing' for r in rows)}
- **Unexpectedly missing: {len(missing)}** -> missing-pages.txt
- Mean text recall: {sum(scored)/len(scored):.3f}  |  pages under {a.min_recall}: {len(low)} -> low-recall.txt, missing-text.txt
- Headings missing: {len(head_missing)}  |  images missing: {len(imgs_missing)}  |  attachments missing: {len(att_missing)}
- Built site: broken internal links/images: {len(broken)}  |  broken anchors: {len(anchors)}
- Hot-linked images by host: {dict(hot)}
""" if scored else "No pages compared.\n"
    (out / "summary.md").write_text(summary)
    print(summary)
    if a.visual:
        screenshots(pairs[:60], out / "visual")
    sys.exit(1 if (missing or low or broken) else 0)


if __name__ == "__main__":
    main()
