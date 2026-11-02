# ACCESS-NRI website prototype (MkDocs)

This folder is a prototype of www.access-nri.org.au as a MkDocs site. It is built **only** for pull-request previews of this repo (at `<preview-url>/website/`, see `.readthedocs.yaml`). It is independent of the Hive docs build.

---

# ACCESS-NRI website on MkDocs (migration prototype)

Everything on the site is Markdown/YAML in this repo: edit on GitHub, open a PR, get a preview, merge to publish.

## Run it
```bash
pip install -r requirements.txt
mkdocs serve                      # http://127.0.0.1:8000
mkdocs build --strict             # what CI runs
mkdocs build -f mkdocs-preview.yml   # static copy in site-preview/ that opens from any folder (double-click index.html)
```

## Layout
| Path | What |
|---|---|
| `docs/` | pages; file paths mirror the live WordPress URLs so links and bookmarks keep working |
| `data/people/<team>.yml` | team/board/SAC members, rendered by `{{ team_cards("<team>") }}` |
| `data/partners.yml` | partner logos (footer + Partners page) |
| `overrides/` | header, hover mega-menu (3 levels, built from `nav:`), footer incl. Mailchimp form |
| `docs/stylesheets/accessnri.css` | the live site's palette, fonts, masthead, cards |
| `stage/` + `tools/build_stage.py` | raw page dumps taken from the live site and the script that turns them into `docs/`, `data/` and `nav:` |
| `tools/migrate_wp.py` | importer for the 116 news posts (REST API) - run once on a machine with normal internet access |

## Hosting
* **Read the Docs**: import the repo; `.readthedocs.yaml` is ready. Set the project to serve at the root of a custom domain (otherwise URLs get an `/en/latest/` prefix) and enable pull-request previews.
* **GitHub Pages**: `.github/workflows/deploy.yml` builds with `--strict` and deploys on push to `main`.
* Add an `ACCESS-NRI/access-nri-website` repo, push, and point DNS (via ANU IT) once the staging URL has been reviewed.

## What is and isn't migrated
Done (58 pages): About (+Board, SAC, Code of conduct, Strategic plan, Contact), Teams (all 13 with members from the live site), Models (4), Impact (3), For users (join, EoI, working groups x7, support, merit allocation x2, user reporting, acknowledging, CWG terms of reference, how to join, SAC minutes), News & events (newsletter, workshops 2026 x4, upcoming events), Jobs, PhD internship, Resources, Reports, Glossary, home page.

Replacements for dynamic features
* Subscribe form: the same Mailchimp list as the live site, posted straight from a plain HTML form (no JavaScript, no plugin).
* User-reporting: already an external Microsoft Forms link.
* Events: a hand-edited Markdown list (`docs/upcoming-events.md`).
* News: archive index of all 116 posts (`docs/news/`); posts not yet imported link to the live site.

Not done / needs a decision
* **News post bodies (116)**: run `python tools/migrate_wp.py --posts`, review, commit. Untested against the live API from my sandbox.
* **Person profile pages** (`/person/<name>/`): "View Profile" currently links to the live site; either migrate (one short page per person) or link to staff pages elsewhere.
* **Sub-pages not in the menu**: workshop programme pages, individual job ads (`/job/...`), case-study pages (`/case-study/...`), event pages, multimedia gallery page 2.
* **Images**: still hot-linked from `wp-content/uploads` on the live site. Download them into `docs/assets/uploads/` before WordPress is switched off.
* **MkDocs 2.0**: Material for MkDocs' team warns that MkDocs 2.0 will break plugins/themes. `requirements.txt` pins `mkdocs<2`; ProperDocs (a drop-in continuation of MkDocs 1.x) is the suggested fallback.


## Verifying the migration

`tools/verify_migration.py` compares the live WordPress site with the built MkDocs site, page by page (run it where the live
site is reachable; `pip install -r requirements-verify.txt`):

    mkdocs build -f mkdocs.yml
    python tools/verify_migration.py --live https://www.access-nri.org.au --built site --visual

It reads the live `wp-sitemap.xml` and reports, per live URL: missing pages (redirects from `redirect_maps` count as present),
share of live words that survive, live paragraphs/bullets absent from the port, missing headings, images and PDF/attachment
links, plus broken internal links/anchors and remaining hot-linked images in the built site. `--visual` saves live/built
screenshot pairs in `report/visual/`. Items you decide not to migrate go in `tools/verify_expected_missing.txt`.
The same check is available as the manual/weekly GitHub Action `verify-migration`. It has been smoke-tested against a
deliberately damaged copy (it caught the deleted page, image and bullet) but **not yet against the real live site**.


## Full replication (2 Nov 2026)

`tools/crawl_convert.py` replicates every page of the live site (stages: `pages`, `listings`, `news`, `banners`, `links`, `media`):
posts, events, case studies, jobs, person profiles, workshop programme pages, plus generated tag/category listings with
thumbnails. Pages already in `docs/` (the hand-tuned ones) are never overwritten. Paths mirror the live URLs; images and
PDFs keep their live `wp-content/uploads/...` paths. Per-page banner photos are stored as `banner:` front matter.
`people-category/` and `author/` pages (WordPress archives that only show the home page) redirect via `redirect_maps`.

`tools/fetch_media.py` downloads the ~157 MB of referenced images/PDFs (it needs only `requests`). The media is not committed
(`docs/wp-content/uploads` is git-ignored) and is fetched on every build. Before WordPress is switched off, move it to Git LFS
or object storage and delete that step.

Result of `tools/verify_migration.py` against the live site: **all 479 live pages present**, mean text recall **0.98**, no
broken internal links, 1 broken anchor, 6 unmatched images. Known cosmetic differences: tile headings on hub pages (teams,
resources) are rendered as icon links, listing excerpts are truncated as on the live site, and 21 person URLs that redirect to
external profile pages stay external links.
