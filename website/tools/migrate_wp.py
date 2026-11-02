#!/usr/bin/env python3
"""Bulk-migrate access-nri.org.au (WordPress) pages to Markdown. Run LOCALLY (needs normal internet access):

    pip install requests beautifulsoup4 markdownify pyyaml
    python tools/migrate_wp.py            # pages from the top menu -> docs/, writes nav.generated.yml
    python tools/migrate_wp.py --posts    # also every news post -> docs/news/posts/ (blog plugin)

Pages are fetched through the public WP REST API (/wp-json/wp/v2/...), so it gets the real content
without scraping the theme. Team members (person posts) are written to data/people/<team>.yml.
Review the diff before committing; forms, embeds and plugin widgets are left as HTML comments TODO."""
import argparse, re, sys, pathlib, html
from urllib.parse import urlparse
import requests, yaml
from bs4 import BeautifulSoup
from markdownify import markdownify as md

BASE = "https://www.access-nri.org.au"
ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
S = requests.Session()


def get(url, **kw):
    r = S.get(url, timeout=30, **kw)
    r.raise_for_status()
    return r


def menu_from_home():
    soup = BeautifulSoup(get(BASE + "/").text, "html.parser")
    ul = next(u for u in reversed(soup.find_all("ul")) if u.select_one("ul ul") and "About" in u.get_text())
    def walk(ul):
        out = []
        for li in ul.find_all("li", recursive=False):
            a = li.find("a", recursive=False)
            sub = li.find("ul", recursive=False)
            out.append({"title": a.get_text(strip=True) if a else "", "href": urlparse(a["href"]).path if a and a.get("href") else "",
                        "children": walk(sub) if sub else []})
        return out
    return walk(ul)


def slug_of(path):
    return path.strip("/").split("/")[-1]


def local_path(path):
    """live URL path -> docs-relative .md path, mirroring the live hierarchy"""
    p = path.strip("/") or "index"
    return p + ".md"


def clean(content_html):
    soup = BeautifulSoup(content_html, "html.parser")
    for t in soup(["script", "style", "noscript", "form"]):
        t.replace_with(soup.new_string(f"<!-- TODO: removed <{t.name}> (widget/form) - re-create by hand -->"))
    for t in soup.find_all("iframe"):
        t.replace_with(BeautifulSoup(f'<p><a href="{t.get("src","")}">Embedded content</a></p>', "html.parser"))
    for img in soup.find_all("img"):
        if img.get("data-src"):
            img["src"] = img["data-src"]
    return md(str(soup), heading_style="ATX", bullets="-").strip()


def rewrite_links(text, known):
    def sub(m):
        path = urlparse(m.group(2)).path
        if path in known:
            return f"[{m.group(1)}]({known[path]})"
        return m.group(0)
    return re.sub(r"\[([^\]]*)\]\((https://www\.access-nri\.org\.au[^)\s]*)\)", sub, text)


def fetch_page(path):
    slug = slug_of(path)
    r = get(f"{BASE}/wp-json/wp/v2/pages", params={"slug": slug, "_fields": "id,slug,link,title,excerpt,content,parent"}).json()
    r = [x for x in r if urlparse(x["link"]).path.rstrip("/") == path.rstrip("/")] or r
    return r[0] if r else None


def nav_yaml(items, known):
    out = []
    for it in items:
        if it["children"]:
            kids = nav_yaml(it["children"], known)
            if it["href"] in known:
                kids.insert(0, {"Overview": known[it["href"]]})
            out.append({it["title"]: kids})
        elif it["href"] in known:
            out.append({it["title"]: known[it["href"]]})
    return out


def flatten(items):
    for it in items:
        if it["href"]:
            yield it["href"]
        yield from flatten(it["children"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--posts", action="store_true")
    a = ap.parse_args()
    menu = menu_from_home()
    paths = [p for p in dict.fromkeys(flatten(menu)) if p.startswith("/") and not re.search(r"category|upcoming-events", p)]
    known = {p: local_path(p) for p in paths}
    for p in paths:
        pg = fetch_page(p)
        if not pg:
            print("skip (not a WP page):", p, file=sys.stderr)
            known.pop(p)
            continue
        body = rewrite_links(clean(pg["content"]["rendered"]), known)
        title = html.unescape(pg["title"]["rendered"])
        desc = BeautifulSoup(pg["excerpt"]["rendered"], "html.parser").get_text(" ", strip=True)
        out = DOCS / known[p]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(f"---\ntitle: {title}\ndescription: {desc[:200]!r}\n---\n\n# {title}\n\n{body}\n", encoding="utf-8")
        print("wrote", out.relative_to(ROOT))
    (ROOT / "nav.generated.yml").write_text(yaml.safe_dump({"nav": nav_yaml(menu, known)}, sort_keys=False, allow_unicode=True))
    if a.posts:
        page = 1
        while True:
            r = S.get(f"{BASE}/wp-json/wp/v2/posts", params={"per_page": 50, "page": page, "_embed": 1}, timeout=30)
            if r.status_code == 400:
                break
            for po in r.json():
                d = po["date"][:10]
                cats = [c["name"] for g in po.get("_embedded", {}).get("wp:term", []) for c in g if c["taxonomy"] == "category"]
                title = html.unescape(po["title"]["rendered"])
                fm = yaml.safe_dump({"title": title, "date": d, "categories": cats or ["News"], "slug": po["slug"]}, allow_unicode=True)
                f = DOCS / "news" / "posts" / f"{po['slug']}.md"
                f.parent.mkdir(parents=True, exist_ok=True)
                f.write_text(f"---\n{fm}---\n\n# {title}\n\n{rewrite_links(clean(po['content']['rendered']), known)}\n", encoding="utf-8")
            page += 1
            if page > int(r.headers.get("X-WP-TotalPages", 1)):
                break


if __name__ == "__main__":
    main()
