#!/usr/bin/env python3
"""Turn raw page dumps in stage/*.txt (=====PATH ... markers, produced by the browser extractor) into docs/.
Re-run any time: python tools/build_stage.py. Restores URL tokens, rewrites internal links to relative .md links,
moves team-member blocks into data/people/<page>.yml + a {{ team_cards() }} call, and writes nav.generated.yml."""
import re, pathlib, yaml, json, os
ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS, STAGE = ROOT / "docs", ROOT / "stage"
LIVE = "https://www.access-nri.org.au/"
UP = LIVE + "wp-content/uploads/"

def unt(s):
    return (s.replace("{U}", UP).replace("{B}", LIVE).replace("{EQ}", "=").replace("{Q}", "?")
             .replace("c{OK}", "cookie").replace("C{OK}", "Cookie"))

pages = {}   # live path -> dict
for f in sorted(STAGE.glob("*.txt")):
    parts = re.split(r"^=====PATH ", f.read_text(encoding="utf-8"), flags=re.M)[1:]
    for p in parts:
        head, _, body = p.partition("\n")
        m = re.match(r"(\S+) \| TITLE (.*?) \| DESC (.*?) \| DATE ?(.*)$", head)
        path, title, desc, date = m.groups()
        pages[path.rstrip("/") + "/" if path != "/" else "/"] = dict(
            title=unt(title).strip(), desc=unt(desc).strip(), date=date.strip(), body=unt(body).strip())

def target(path):
    base = path.strip("/")
    has_child = any(q != path and q.startswith(path) for q in pages)
    return f"{base}/index.md" if has_child else f"{base}.md"

TARGET = {p: target(p) for p in pages}

def rel(src, dst):
    return os.path.relpath(dst, os.path.dirname(src) or ".").replace(os.sep, "/")

def fix_links(body, src):
    def sub(m):
        txt, url, frag = m.group(1), m.group(2), m.group(3) or ""
        path = url[len(LIVE) - 1:]
        key = path if path.endswith("/") else path + "/"
        if key in TARGET:
            return f"[{txt}]({rel(src, TARGET[key])}{frag})"
        return m.group(0)
    return re.sub(r"\[([^\]]*)\]\((https://www\.access-nri\.org\.au/[^)#\s]*)(#[^)\s]*)?\)", sub, body)

PERSON = re.compile(
    r"!\[(?P<alt>[^\]]*)\]\((?P<img>[^)]*)\)\n\n### (?P<name>[^\n]+)\n\n(?P<role>[^\n]*)\n\n\[View Profile\]\((?P<prof>[^)]*)\)(?:\n\n(?P<phone>[0-9()+ ]{8,}))?"
    r"(?P<soc>(?:\n\n- \[[^\]]*\]\([^)]*\)(?:\n- \[[^\]]*\]\([^)]*\))*)?)")

def people_split(body, slug):
    people = []
    def sub(m):
        p = dict(name=m["name"].strip(), role=m["role"].strip(), photo=m["img"], profile=m["prof"])
        sl = re.search(r"/person/([^/]+)/", m["prof"])
        if m["phone"]: p["phone"] = m["phone"].strip()
        p["slug"] = sl.group(1) if sl else re.sub(r"[^a-z0-9]+", "-", m["name"].lower()).strip("-")
        for u in re.findall(r"\]\(([^)]*)\)", m["soc"]):
            if "linkedin" in u: p["linkedin"] = u
            elif "twitter.com" in u or "//x.com" in u: p["twitter"] = u
            elif "bsky" in u: p["bluesky"] = u
            elif "github.com" in u: p["github"] = u
            elif u.startswith("mailto:"): p["email"] = u[7:]
        people.append(p)
        return "\x00PERSON\x00"
    body = PERSON.sub(sub, body)
    if not people:
        return body
    (ROOT / "data" / "people").mkdir(parents=True, exist_ok=True)
    (ROOT / "data" / "people" / f"{slug}.yml").write_text(yaml.safe_dump(people, sort_keys=False, allow_unicode=True), encoding="utf-8")
    body = re.sub(r"(?:\x00PERSON\x00\s*)+", f'{{{{ team_cards("{slug}") }}}}\n\n', body, count=1)
    return body.replace("\x00PERSON\x00", "")

def teams_prepass():
    key = "/teams/all-access-nri-teams/"
    if key not in pages: return
    by_title = {v["title"]: k for k, v in pages.items() if k.startswith("/teams/") and k not in ("/teams/", key)}
    parts = re.split(r"^## (.+)$", pages[key]["body"], flags=re.M)
    out = parts[0]
    for i in range(1, len(parts), 2):
        title, sec = parts[i].strip(), parts[i + 1]
        tp = by_title.get(title)
        if not tp:
            out += f"## {title}\n{sec}"; continue
        slug = tp.strip("/").split("/")[-1]
        out += f"## [{title}]({LIVE}{tp.strip('/')}/)\n\n" + people_split(sec.strip(), slug) + "\n\n"
    pages[key]["body"] = out

teams_prepass()
for path, pg in pages.items():
    dst = TARGET[path]
    slug = path.strip("/").split("/")[-1]
    body = people_split(pg["body"].replace("§PEOPLE§", f'{{{{ team_cards("{slug}") }}}}'), slug)
    body = fix_links(body, dst)
    fm = {"title": pg["title"]}
    if pg["desc"]: fm["description"] = pg["desc"][:300]
    if "/news/posts/" in dst or pg["date"]:
        if pg["date"]: fm["date"] = pg["date"][:10]
    out = DOCS / dst
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True) + "---\n\n# " + pg["title"] + "\n\n" + body + "\n", encoding="utf-8")
# ---- news archive + "in conversation" listing -------------------------------------------------
def news_pages():
    rows = [l.rstrip("\n").split("|", 2) for l in (STAGE / "news-index.tsv").read_text(encoding="utf-8").splitlines() if l.strip()]
    def link(slug, title):
        local = DOCS / "news" / f"{slug}.md"
        return f"[{title}]({slug}.md)" if local.exists() else f"[{title}]({LIVE}{slug}/)"
    def write(path, title, intro, items):
        out, year = [f"---\ntitle: {title}\n---\n\n# {title}\n\n{intro}\n"], None
        for d, slug, t in items:
            if d[:4] != year:
                year = d[:4]; out.append(f"\n## {year}\n")
            out.append(f"- {d} — {link(slug, t)}")
        (DOCS / path).parent.mkdir(parents=True, exist_ok=True)
        (DOCS / path).write_text("\n".join(out) + "\n", encoding="utf-8")
    write("news/index.md", "Latest news", "All ACCESS-NRI news, newest first. Articles not yet imported into this repository link to the live site; "
          "run `python tools/migrate_wp.py --posts` to import them (see the README).", rows)
    write("news/in-conversation-with.md", "In conversation with", "Profiles of the people behind ACCESS-NRI.",
          [r for r in rows if r[2].startswith("In conversation with")])
news_pages()

# ---- nav --------------------------------------------------------------------------------------
def build_nav():
    items = []
    for l in (STAGE / "menu.txt").read_text(encoding="utf-8").splitlines():
        d, path, title = l.split("|", 2)
        items.append((int(d), path, title))
    def tgt(path):
        if path.startswith("http"): return path
        if path.rstrip("/") + "/" in TARGET: return TARGET[path.rstrip("/") + "/"]
        if path == "/news-and-events/latest-news/": return "news/index.md"
        if path == "/category/in-conversation-with/": return "news/in-conversation-with.md"
        return None
    tree = []
    for d, path, title in items:
        node = {"title": title, "path": tgt(path), "kids": []}
        if d == 0: tree.append(node)
        elif d == 1: tree[-1]["kids"].append(node)
        else: tree[-1]["kids"][-1]["kids"].append(node)
    def conv(n, top=False):
        if not n["kids"]: return {n["title"]: n["path"]}
        kids = [conv(k) for k in n["kids"]]
        if n["path"] and n["path"] != (n["kids"][0]["path"]):
            kids.insert(0, {"Overview": n["path"]})
        return {n["title"]: kids}
    return [conv(n, True) for n in tree if n["path"] or n["kids"]]
nav = build_nav()
cfg = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
head = cfg.split("\nnav:")[0].rstrip("\n")
(ROOT / "mkdocs.yml").write_text(head + "\n\n" + yaml.safe_dump({"nav": nav}, sort_keys=False, allow_unicode=True, width=1000), encoding="utf-8")

json.dump(TARGET, open(ROOT / "stage" / "targets.json", "w"), indent=1)
print(len(pages), "pages written")
