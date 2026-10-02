# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This repository hosts the source code for the **ACCESS-Hive Docs** website: a MkDocs (Material theme) static site hosted on Read the Docs, published at https://docs.access-hive.org.au/. The site hosts ACCESS-NRI documentation for ACCESS climate/earth-system model users (e.g., getting started, running models, model evaluation, tutorials, community resources, etc.).

There is no application code to compile — this is a documentation site. "Development" means writing/editing Markdown content, adjusting MkDocs config/navigation, or working on the small amount of supporting CSS/JS/Python hooks.

## Common commands

```bash
# Install dependencies (prefer a venv or a conda/micromamba env)
pip install -r requirements.txt

# Serve the site locally with live-reload at http://127.0.0.1:8000
mkdocs serve

# Build the static site (output in site/)
mkdocs build
```

There is no test suite, linter, or build step beyond `mkdocs build`/`serve`. Link validity is checked in CI (see below), not locally via a script in this repo.

## Architecture / structure

- **`mkdocs.yml`** is the single source of truth for site navigation (`nav:`), theme config, plugins, and which CSS/JS files are loaded (`extra_css` / `extra_javascript`). Any new page must be added to `nav:` here to appear in the sidebar.
- **`docs/`** contains all page content as Markdown, organized into top-level sections that mirror the nav structure: `getting_started/`, `models/`, `model_evaluation/`, `tutorials/`, `community_resources/`, `about/`. Each section typically has an `index.md` landing page.
- **`drafts/`** holds content not yet wired into `nav:`/published — work in progress that isn't part of the live site yet.
- **`docs/hooks/copyright_year.py`** is an MkDocs build hook (registered under `hooks:` in `mkdocs.yml`) that stamps the current year into the footer copyright string at build time.
- **`docs/js/custom-tags.js`** defines custom HTML tags used across the docs (e.g. `<custom-not-supported/>`, `<custom-references>`, `<custom-simulated-terminal-info/>`) — see README for the full list and usage.
- **`docs/js/miscellaneous.js`** holds smaller page-behavior scripts (TOC handling, tabs, external links, citation links, permalinks, etc.) run on each page via `main()`.
- **`docs/css/access-nri.css`** and **`docs/css/responsiveness.css`** hold site-wide custom styling, referenced via `attr_list` syntax or `markdown`-in-HTML blocks in content (see README styling guidelines).
- **`overrides/`** contains Material theme template overrides (`main.html`, `home.html`, and partials for header/footer/toc/social/copyright) — edit these only for structural/theme-level changes, not content.
- **`abbreviations.md`** + `pymdownx.snippets` auto-appends glossary/abbreviation definitions to every page.
- **`references.bib`** is the BibTeX source used by `mkdocs-bibtex` for citations/references across pages.
- **`.readthedocs.yaml`** configures the Read the Docs build (Python 3.13, `requirements.txt`, runs `mkdocs.yml`).

## Branching / release model

- `main` is the default working branch where PRs land.
- `production` is deployed; a scheduled workflow (`.github/workflows/automatic_merge.yml`) auto-merges `main` into `production` daily.
- PRs automatically get a Read the Docs preview link commented by `.github/workflows/pr_preview_comment.yml`.
- All content changes require review from `@ACCESS-NRI/hivedocsteam` (enforced via `.github/CODEOWNERS`).

## Content/style conventions (see README.md for full detail)

- Prefer Markdown over raw HTML where possible.
- Prefer **absolute** links (starting with `/`, e.g. `/models/configurations/access-cm`, `/assets/...`) for all internal links and asset paths.
- Titles/subtitles must not contain code spans, bold, italic, or links.
- Use code spans/blocks for commands, file paths, and file names; italics for proper nouns (e.g. _Gadi_, _payu_); bold sparingly for emphasis.
- Admonitions (`note`, `info`, `warning`, `tip`, etc.) and tabs follow the Material-for-MkDocs conventions  but use their own rendering
- Content tabs behaviour is recreated in miscellaneous.js and documented in the README's HTML/Markdown cheatsheet — use the HTML forms shown there, not markup, since they render and work differently on this site.
- Terminal animations are provided by [animated-terminal.js](https://github.com/atteggiani/animated-terminal.js)
