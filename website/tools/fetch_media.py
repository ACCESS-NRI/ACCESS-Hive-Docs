#!/usr/bin/env python3
"""Download every wp-content/ file the pages reference from the live site into docs/ (same paths as live).

Dependency-light (requests + stdlib) so it can run inside the Read the Docs build:
    python tools/fetch_media.py            # run from the folder that holds docs/ (website/)

The media is NOT committed to the repo (docs/wp-content/uploads is git-ignored): it is large (~160 MB) and is
fetched on every build. Before the live WordPress site is switched off, move it to the repo (Git LFS) or object
storage and delete this step.
"""
import re, sys, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import quote, unquote

import requests

LIVE = "https://www.access-nri.org.au"
PAT = re.compile(r"wp-content/(?:uploads|themes)/[^\s)\"'<>\]#?]+")
docs = Path("docs")
refs = set()
for root in (docs, Path("data"), Path("overrides")):
    for f in root.rglob("*"):
        if f.is_file() and f.suffix in (".md", ".yml", ".html", ".css", ".js"):
            refs |= {unquote(m) for m in PAT.findall(f.read_text("utf-8", "ignore"))}
todo = sorted(r for r in refs if not (docs / r).exists())
print(f"{len(refs)} media references, {len(todo)} to download")
sess = requests.Session()
failed = []


def get(rel):
    for _ in range(3):
        try:
            r = sess.get(f"{LIVE}/{quote(rel)}", timeout=60, headers={"User-Agent": "access-nri-mkdocs-build/1.0"})
            if r.status_code == 200:
                dest = docs / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(r.content)
                return
            if r.status_code == 404:
                break
        except requests.RequestException:
            time.sleep(2)
    failed.append(rel)


with ThreadPoolExecutor(6) as ex:
    list(ex.map(get, todo))
print(f"done; {len(failed)} not found:", *failed[:10], sep="\n  ")
sys.exit(0)  # a missing image must not fail the docs build
