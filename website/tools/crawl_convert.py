#!/usr/bin/env python3
"""Replicate the whole live WordPress site into docs/ (Markdown) and localise its media.

    python tools/crawl_convert.py              # all stages
    python tools/crawl_convert.py --stage pages|listings|banners|links|media

Stages (all idempotent; pages already in docs/ are never overwritten):
  pages     every live URL without a docs/ page -> docs/<live path>.md  (posts, events, case studies, jobs, persons, plain pages)
  listings  tag/ and category/ pages generated from the live listings (links to the local posts)
  banners   per-page banner photo -> `banner:` front matter (every page, including hand-migrated ones)
  links     rewrite absolute live links in all of docs/ to relative links; collect wp-content/uploads references
  media     download every referenced wp-content/uploads file to docs/wp-content/uploads/... (same path as live)

Needs network access to the live site. Live HTML is cached in .verify-cache/ (shared with verify_migration.py).
"""
import argparse, json, os, re, sys, time, posixpath
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote, quote

import requests, yaml
from bs4 import BeautifulSoup, NavigableString
from markdownify import MarkdownConverter

sys.path.insert(0, os.path.dirname(__file__))
from verify_migration import Fetcher  # noqa: E402

LIVE = "https://www.access-nri.org.au"
HOSTS = {"www.access-nri.org.au", "access-nri.org.au"}
DOCS = Path("docs")
UA = {"User-Agent": "access-nri-migration/1.0"}
UPLOADS = "wp-content/uploads/"
MEDIA_FILE = Path("stage/media.json")
# pages handled elsewhere (redirect_maps, hand-built indexes) or WordPress artefacts that only redirect
SKIP_PREFIX = ("people-category/", "author/", "tag/", "category/", "page/", "wp-")
SKIP_EXACT = {"news-and-events/latest-news"}


def path_of(url):
    u = urlparse(url)
    return u.path.strip("/")


def load_urls():
    urls = json.load(open("stage/live-urls.json"))
    ext = {path_of(u): loc for u, st, loc in json.load(open("stage/person-redirects.json")) if st != 200}
    return [u for u in urls if path_of(u) not in ext], ext


def redirect_sources():
    try:
        c = yaml.safe_load(open("mkdocs.yml"))
        for p in c["plugins"]:
            if isinstance(p, dict) and "redirects" in p:
                return {k[:-3] for k in p["redirects"]["redirect_maps"]}
    except Exception:
        pass
    return set()


class Site:
    """live path -> docs file mapping, shared by every stage"""

    def __init__(self):
        self.urls, self.ext = load_urls()
        self.handled = redirect_sources() | SKIP_EXACT
        self.md = {}
        for u in self.urls:
            p = path_of(u)
            self.md[p] = self.find(p)
        self.md[""] = DOCS / "index.md"
        self.frags = set()

    def find(self, p):
        for c in (DOCS / f"{p}.md", DOCS / p / "index.md"):
            if c.exists():
                return c
        return DOCS / f"{p}.md"

    def rel(self, from_md, to):
        return posixpath.relpath(Path(to).as_posix(), Path(from_md).parent.as_posix())

    def link(self, from_md, href, base=LIVE + "/"):
        """absolute/relative live href -> relative local link (or unchanged)"""
        href = (href or "").split("<")[0].strip()  # some live hrefs carry stray markup
        if not href or href.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
            return href
        u = urlparse(urljoin(base, href.strip()))
        if u.netloc not in HOSTS:
            return href
        p = u.path.strip("/")
        frag = f"#{u.fragment}" if u.fragment else ""
        if p.startswith(UPLOADS):
            return self.media_rel(from_md, u.path) + frag
        if p in self.ext:
            return self.ext[p] + frag
        if p in self.md and (self.md[p].exists() or p in PLANNED):
            return quote(self.rel(from_md, self.md[p])) + frag
        return f"{LIVE}/{p}/{frag}" if p else f"{LIVE}/{frag}"

    def media_rel(self, from_md, path):
        rel = unquote(path).lstrip("/")
        REGISTRY.add(rel)
        return quote(self.rel(from_md, DOCS / rel))


REGISTRY = set()
PLANNED = set()


# ---------- HTML -> Markdown ----------
class MD(MarkdownConverter):
    def convert_img(self, el, text, parent_tags):
        src = el.get("src", "")
        alt = (el.get("alt") or "").replace("\n", " ").strip()
        if not src:
            return ""
        al = re.search(r"\balign(left|right|center)\b", " ".join(el.get("class") or []))
        return f"![{alt}]({src})" + (f"{{ .align-{al.group(1)} }}" if al else "")

    def convert_a(self, el, text, parent_tags):
        out = super().convert_a(el, text, parent_tags)
        cls = " ".join(el.get("class") or [])
        if out.strip() and re.search(r"\b(button|btn)\b", cls) and "](" in out and "![" not in out:
            out = out.strip() + "{ .buttononblue }"
        return out

    def convert_iframe(self, el, text, parent_tags):
        src = el.get("src", "")
        return f'\n\n<iframe src="{src}" width="100%" height="400" style="border:0" loading="lazy" allowfullscreen></iframe>\n\n' if src else ""

    def convert_hN(self, n, el, text, parent_tags):
        out = super().convert_hN(n, el, text, parent_tags)
        a = el.get("data-anchor")
        return out.rstrip("\n") + f" {{ #{a} }}\n\n" if a and out.strip() else out

    def convert_figcaption(self, el, text, parent_tags):
        return f"\n\n*{text.strip()}*\n\n" if text.strip() else ""


def to_md(node):
    md = MD(heading_style="ATX", bullets="-", strip=["script", "style"], escape_underscores=False, escape_asterisks=True).convert_soup(node)
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    return md.replace("{{", "&#123;&#123;").replace("{%", "&#123;%")


DROP = "script,style,noscript,form,.sharedaddy,.addtoany_share_save_container,.pagination,.post-navigation,.related-posts,.screen-reader-text,[hidden],p.date,p.post-categories,p.post-tags"


def parse_page(html):
    s = BeautifulSoup(html, "lxml")
    h1 = s.select_one(".page-title h1") or s.select_one("h1")
    title = h1.get_text(" ", strip=True) if h1 else ""
    pt = s.select_one(".page-title")
    banner = None
    if pt and pt.get("style"):
        m = re.search(r"url\(['\"]?([^)'\"]+)", pt["style"])
        banner = m.group(1) if m else None
    date_el = s.select_one("article p.date") or s.select_one("p.date")
    date_txt = date_el.get_text(strip=True) if date_el else ""
    pub = s.select_one('meta[property="article:published_time"]')
    desc = s.select_one('meta[name="description"]') or s.select_one('meta[property="og:description"]')
    cats = [(a.get_text(strip=True), a["href"]) for a in s.select("article p.post-categories a")]
    tags = [(a.get_text(strip=True), a["href"]) for a in s.select("article p.post-tags a")]
    body = s.select_one("article.single-post-item") or s.select_one("#main-content .body-content") or s.select_one(".body-content")
    photo = None
    for im in s.select("#main-content img"):
        if "wp-content/uploads" in (im.get("src") or "") and not (body and im in body.find_all("img")):
            photo = im["src"]
            break
    pos = s.select_one("#main-content p.position")
    return dict(s=s, photo=photo, position=pos.get_text(" ", strip=True) if pos else "", title=title, banner=banner, date=date_txt, iso=(pub["content"][:10] if pub else ""),
                desc=(desc["content"].strip() if desc and desc.get("content") else ""), cats=cats, tags=tags, body=body)


def convert_body(site, from_md, body, base):
    body = BeautifulSoup(str(body), "lxml").body
    for t in body.select(DROP):
        t.decompose()
    for t in body.select("[href]"):
        t["href"] = site.link(from_md, t["href"], base)
    for t in body.select("img"):
        src = t.get("src") or t.get("data-src") or ""
        t["src"] = site.link(from_md, src, base)
    for t in body.select("[id]"):
        i = t["id"]
        if t.name in ("h1", "h2", "h3", "h4", "h5", "h6"):
            t["data-anchor"] = i
        elif i in site.frags and t.name != "a":
            t.insert_before(NavigableString(f'<a id="{i}"></a>'))
        elif i in site.frags:
            t.insert_before(NavigableString(f'<a id="{i}"></a>'))
    for t in body.select("a[name]"):  # old-style anchors, e.g. Word footnotes
        if t["name"] in site.frags:
            t.insert_before(NavigableString(f'<a id="{t["name"]}"></a>'))
    for t in body.select("[srcset],[sizes],[class],[style],[id]"):
        for k in ("srcset", "sizes", "style", "id"):
            t.attrs.pop(k, None)
        if t.name not in ("a", "img"):
            t.attrs.pop("class", None)
    return to_md(body)


def front_matter(**kv):
    kv = {k: v for k, v in kv.items() if v not in (None, "", [])}
    return "---\n" + yaml.safe_dump(kv, allow_unicode=True, sort_keys=False, width=1000) + "---\n\n"


def collect_fragments(site, fetch):
    for u in site.urls:
        html = fetch.get(u)
        if html:
            for m in re.finditer(r'href="[^"#]*#([^"]+)"', html):
                site.frags.add(unquote(m.group(1)))


def stage_pages(site, fetch):
    collect_fragments(site, fetch)
    todo = []
    for u in site.urls:
        p = path_of(u)
        if not p or p in site.handled or p.startswith(SKIP_PREFIX):
            continue
        if site.md[p].exists():
            continue
        todo.append((p, u))
        PLANNED.add(p)
    print(f"pages to generate: {len(todo)}")
    n = fail = 0
    for p, u in todo:
        html = fetch.get(u)
        if not html:
            print("  fetch failed", u)
            fail += 1
            continue
        pg = parse_page(html)
        if pg["body"] is None:
            print("  no body", u)
            fail += 1
            continue
        out = site.md[p]
        body = convert_body(site, out, pg["body"], u)
        head = []
        if p.startswith("person/") and pg.get("photo"):
            head.append(f"![{pg['title']}]({site.link(out, pg['photo'], u)}){{ .align-right }}")
        if pg.get("position"):
            head.append(f"**{pg['position']}**")
        if pg["date"]:
            head.append(f"*{pg['date']}*")
        foot = []
        if pg["cats"]:
            foot.append("**Categories:** " + ", ".join(f"[{n_}]({site.link(out, h)})" for n_, h in pg["cats"]))
        if pg["tags"]:
            foot.append("**Tags:** " + ", ".join(f"[{n_}]({site.link(out, h)})" for n_, h in pg["tags"]))
        top = pg["title"] and f"# {pg['title']}\n\n"
        text = front_matter(title=pg["title"], date=pg["iso"] or None, description=pg["desc"][:300] or None,
                            categories=[c for c, _ in pg["cats"]], tags=[t for t, _ in pg["tags"]],
                            type=p.split("/")[0] if p.split("/")[0] in ("event", "case-study", "job", "person") else None) + (top or "")
        text += ("\n\n".join(head) + "\n\n" if head else "") + body + ("\n\n" + "\n\n".join(foot) if foot else "") + "\n"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, "utf-8")
        n += 1
    print(f"generated {n}, failed {fail}")


# ---------- tag / category listings ----------
def listing_entries(fetch, url):
    """all posts on a live listing page, following /page/N/ pagination"""
    entries, seen, page = [], set(), 1
    while True:
        u = url if page == 1 else f"{url.rstrip('/')}/page/{page}/"
        html = fetch.get(u)
        if not html:
            break
        s = BeautifulSoup(html, "lxml")
        arts = s.select("#main-content article.post-item")
        new = 0
        for a in arts:
            h = a.select_one("h2 a, h3 a, a[href]")
            if not h or h["href"] in seen:
                continue
            seen.add(h["href"])
            new += 1
            d = a.select_one("p.date")
            ex = [p.get_text(" ", strip=True) for p in a.select("p") if "date" not in (p.get("class") or [])]
            im = a.select_one("img")
            entries.append(dict(thumb=(im.get("src") if im else ""), title=(a.select_one("h2,h3") or h).get_text(" ", strip=True), href=h["href"],
                                date=d.get_text(strip=True) if d else "", excerpt=(ex[0] if ex else "")[:240]))
        if not new or not s.select(f'a[href*="/page/{page + 1}/"]'):
            break
        page += 1
    return entries


def stage_listings(site, fetch):
    items = [path_of(u) for u in site.urls if path_of(u).startswith(("tag/", "category/")) and path_of(u) not in site.handled]
    print("listing pages:", len(items))
    for p in items:
        out = DOCS / f"{p}.md"
        if site.md.get(p) and site.md[p].exists() and site.md[p] != out:
            continue
        u = f"{LIVE}/{p}/"
        html = fetch.get(u)
        if not html:
            continue
        pg = parse_page(html)
        ents = listing_entries(fetch, u)
        lines = [f"# {pg['title']}\n"]
        for e in ents:
            th = f"[![]({site.link(out, e['thumb'])}){{ .listing-thumb }}]({site.link(out, e['href'])})\n  " if e.get("thumb") else ""
            lines.append(f"- {th}**[{e['title']}]({site.link(out, e['href'])})**" + (f" — {e['date']}" if e["date"] else "") +
                         (f"  \n  {e['excerpt']}" if e["excerpt"] else ""))
        if not ents:
            lines.append("No entries.")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(front_matter(title=pg["title"], banner=None, type="listing") + "\n".join(lines) + "\n", "utf-8")


def stage_news(site, fetch):
    """news/index.md and news/in-conversation-with.md from the live category listings (real post links)"""
    for cat, out, intro in (("news", DOCS / "news/index.md", "All ACCESS-NRI news, newest first."),
                            ("in-conversation-with", DOCS / "news/in-conversation-with.md", "Profiles of the people behind ACCESS-NRI.")):
        ents = listing_entries(fetch, f"{LIVE}/category/{cat}/")
        title = "Latest news" if cat == "news" else "In conversation with"
        by_year = {}
        for e in ents:
            y = re.search(r"(\d{4})", e["date"])
            by_year.setdefault(y.group(1) if y else "Other", []).append(e)
        lines = [f"# {title}\n", intro + "\n"]
        for y in sorted(by_year, reverse=True):
            lines.append(f"\n## {y}\n")
            for e in by_year[y]:
                th = f"[![]({site.link(out, e['thumb'])}){{ .listing-thumb }}]({site.link(out, e['href'])})\n  " if e.get("thumb") else ""
                lines.append(f"- {th}**[{e['title']}]({site.link(out, e['href'])})** — {e['date']}" + (f"  \n  {e['excerpt']}" if e["excerpt"] else ""))
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(front_matter(title=title) + "\n".join(lines) + "\n", "utf-8")
        print(cat, len(ents), "entries")


# ---------- banners ----------
def set_meta(path, key, val):
    t = path.read_text("utf-8")
    if t.startswith("---\n"):
        end = t.index("\n---", 4)
        fm = yaml.safe_load(t[4:end]) or {}
        rest = t[end + 4:]
    else:
        fm, rest = {}, "\n" + t
    if fm.get(key) == val:
        return
    fm[key] = val
    path.write_text("---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=1000) + "---" + rest, "utf-8")


def stage_banners(site, fetch):
    n = 0
    for u in site.urls:
        p = path_of(u)
        md = site.md.get(p)
        if not md or not md.exists() or md.read_text("utf-8").startswith("---\n") and "banner:" in md.read_text("utf-8")[:2000]:
            continue
        html = fetch.get(u)
        if not html:
            continue
        b = parse_page(html)["banner"]
        if b and urlparse(b).netloc in HOSTS:
            rel = unquote(urlparse(b).path).lstrip("/")
            REGISTRY.add(rel)
            set_meta(md, "banner", rel)
            n += 1
    print("banners set:", n)


# ---------- link rewrite across every page ----------
ABS = re.compile(r"https?://(?:www\.)?access-nri\.org\.au/[^\s)\"'<>\]]*")


def stage_links(site):
    changed = 0
    for md in DOCS.rglob("*.md"):
        t = md.read_text("utf-8")
        def repl(m, t=t, md=md):
            raw = m.group(0)
            url = raw.rstrip(".,;")
            tail = raw[len(url):]
            if re.search(r"(href|src)=[\"']$", t[max(0, m.start() - 6):m.start()]):  # raw HTML: Markdown will not rewrite it
                u = urlparse(url)
                p = u.path.strip("/")
                if p.startswith(UPLOADS):
                    return "{{ media('" + unquote(p) + "') }}" + tail
                if p in site.md and site.md[p].exists():
                    return "{{ pagelink('" + p + "') }}" + (f"#{u.fragment}" if u.fragment else "") + tail
                return raw
            return site.link(md, url) + tail
        new = ABS.sub(repl, t)
        if new != t:
            md.write_text(new, "utf-8")
            changed += 1
    print("pages with rewritten links:", changed)


# ---------- media ----------
def stage_media():
    reg = set(REGISTRY)
    if MEDIA_FILE.exists():
        reg |= set(json.load(open(MEDIA_FILE)))
    # also anything mentioned in docs, data, overrides, css
    pat = re.compile(r"wp-content/uploads/[^\s)\"'<>\]#?]+")
    for root in (DOCS, Path("data"), Path("overrides")):
        for f in root.rglob("*"):
            if f.is_file() and f.suffix in (".md", ".yml", ".html", ".css", ".js"):
                reg |= {unquote(m) for m in pat.findall(f.read_text("utf-8", "ignore"))}
    reg = {r for r in reg if not (DOCS / r).exists() and "/" in r}
    MEDIA_FILE.parent.mkdir(exist_ok=True)
    json.dump(sorted(reg), open(MEDIA_FILE, "w"))
    print("media to download:", len(reg))
    sess = requests.Session()
    fails, total = [], 0

    def get(rel):
        dest = DOCS / rel
        for attempt in range(3):
            try:
                r = sess.get(f"{LIVE}/{quote(rel)}", headers=UA, timeout=60)
                if r.status_code == 200:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_bytes(r.content)
                    return len(r.content)
                if r.status_code == 404:
                    break
            except requests.RequestException:
                time.sleep(2)
        fails.append(rel)
        return 0

    with ThreadPoolExecutor(6) as ex:
        for i, size in enumerate(ex.map(get, sorted(reg))):
            total += size
    print(f"downloaded {len(reg) - len(fails)} files, {total / 1e6:.1f} MB; failed {len(fails)}")
    Path("stage/media-failed.txt").write_text("\n".join(fails))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", default="all")
    ap.add_argument("--delay", type=float, default=0.3)
    a = ap.parse_args()
    site = Site()
    fetch = Fetcher(".verify-cache", a.delay)
    st = a.stage
    if st in ("all", "pages"):
        stage_pages(site, fetch)
        site = Site()
    if st in ("all", "listings"):
        stage_listings(site, fetch)
        site = Site()
    if st in ("all", "news"):
        stage_news(site, fetch)
    if st in ("all", "banners"):
        stage_banners(site, fetch)
    if st in ("all", "links"):
        stage_links(site)
    if st in ("all", "media"):
        stage_media()


if __name__ == "__main__":
    main()
