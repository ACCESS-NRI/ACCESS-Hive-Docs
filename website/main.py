"""mkdocs-macros hook. Structured data lives in /data so editors change YAML, not HTML:
  data/people/<team-page-slug>.yml  - members of one team (replaces the WordPress 'person' post type)
  data/partners.yml                 - partner logos (used by the footer and the partners page)"""
import os
import re
import yaml
from urllib.parse import quote


ICONS = {
    "email": "M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z",
    "linkedin": "M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.32 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.79M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z",
    "github": "M12 2A10 10 0 0 0 2 12c0 4.42 2.87 8.17 6.84 9.5.5.08.66-.23.66-.5v-1.69c-2.77.6-3.36-1.34-3.36-1.34-.46-1.16-1.11-1.47-1.11-1.47-.91-.62.07-.6.07-.6 1 .07 1.53 1.03 1.53 1.03.87 1.52 2.34 1.07 2.91.83.09-.65.35-1.09.63-1.34-2.22-.25-4.55-1.11-4.55-4.92 0-1.11.38-2 1.03-2.71-.1-.25-.45-1.29.1-2.64 0 0 .84-.27 2.75 1.02.79-.22 1.65-.33 2.5-.33.85 0 1.71.11 2.5.33 1.91-1.29 2.75-1.02 2.75-1.02.55 1.35.2 2.39.1 2.64.65.71 1.03 1.6 1.03 2.71 0 3.82-2.34 4.66-4.57 4.91.36.31.69.92.69 1.85V21c0 .27.16.59.69.5C19.14 20.16 22 16.42 22 12A10 10 0 0 0 12 2z",
    "twitter": "M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z",
    "bluesky": "M12 10.8c-1.087-2.114-4.046-6.053-6.798-7.995C2.566.944 1.561 1.266.902 1.565.139 1.908 0 3.08 0 3.768c0 .69.378 5.65.624 6.479.815 2.736 3.713 3.66 6.383 3.364.136-.02.275-.039.415-.056-.138.022-.276.04-.415.056-3.912.58-7.387 2.005-2.83 7.078 5.013 5.19 6.87-1.113 7.823-4.308.953 3.195 2.05 9.271 7.733 4.308 4.267-4.308 1.172-6.498-2.74-7.078a8.741 8.741 0 0 1-.415-.056c.14.017.279.036.415.056 2.67.297 5.568-.628 6.383-3.364.246-.829.624-5.789.624-6.479 0-.688-.139-1.86-.902-2.203-.659-.299-1.664-.621-4.3 1.24-2.752 1.942-5.711 5.881-6.798 7.995z",
}
ICONS = {k: f'<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path fill="currentColor" d="{v}"/></svg>' for k, v in ICONS.items()}

def define_env(env):
    data_dir = os.path.join(env.project_dir, "data")

    def load(*parts):
        path = os.path.join(data_dir, *parts)
        if not os.path.exists(path):
            return []
        with open(path, encoding="utf-8") as fh:
            return yaml.safe_load(fh) or []

    partners = load("partners.yml")
    env.variables["partners"] = partners
    env.conf["extra"]["partners"] = partners  # footer.html reads config.extra.partners

    ext_profiles = {}
    pr = os.path.join(env.project_dir, "stage", "person-redirects.json")
    if os.path.exists(pr):
        import json
        for u, status, loc in json.load(open(pr)):
            if status != 200 and loc:
                ext_profiles[u.rstrip("/").rsplit("/", 1)[-1]] = loc

    def rel_root():
        page = getattr(env, "page", None)
        return "../" * (page.url.count("/") if page and page.url else 0)

    def local(path):
        """root-relative media path (wp-content/...) -> path relative to the page being rendered"""
        if not path or path.startswith(("http://", "https://", "/")):
            return path
        return rel_root() + quote(path)

    def profile_href(p):
        slug = p.get("slug") or ""
        if slug in ext_profiles:
            return ext_profiles[slug]
        if slug and os.path.exists(os.path.join(env.project_dir, "docs", "person", f"{slug}.md")):
            dirurls = env.conf.get("use_directory_urls", True)
            return rel_root() + (f"person/{slug}/" if dirurls else f"person/{slug}.html")
        return p.get("profile") or f"https://www.access-nri.org.au/person/{slug}/"

    @env.macro
    def pagelink(p):
        """live path (e.g. 'about/aims') -> URL relative to the current page; for raw HTML links in Markdown"""
        p = p.strip("/")
        if not p:
            return rel_root() or "./"
        dirurls = env.conf.get("use_directory_urls", True)
        if dirurls:
            return rel_root() + p + "/"
        has_index = os.path.exists(os.path.join(env.project_dir, "docs", p, "index.md"))
        return rel_root() + (f"{p}/index.html" if has_index else f"{p}.html")

    @env.macro
    def media(p):
        return local(p)

    @env.macro
    def team_cards(team):
        out = ['<div class="team-grid" markdown="0">']
        for p in load("people", f"{team}.yml"):
            links = ""
            if p.get("email"):
                links += f'<a href="mailto:{p["email"]}" title="Email {p["name"]}" aria-label="Email">{ICONS["email"]}</a>'
            for key, label in (("linkedin", "LinkedIn"), ("twitter", "X"), ("bluesky", "Bluesky"), ("github", "GitHub")):
                if p.get(key):
                    links += f'<a href="{p[key]}" title="{label}: {p["name"]}" aria-label="{label}">{ICONS[key]}</a>'
            profile = profile_href(p)
            phone = f'<p class="role">{p["phone"]}</p>' if p.get("phone") else ""
            out.append(
                f'<div class="person-card"><img src="{local(p.get("photo", "") or "wp-content/themes/accessnri/images/no-person-photo.png")}" alt="{p["name"]}" loading="lazy">'
                f'<h3>{p["name"]}</h3><p class="role">{p.get("role", "")}</p>{phone}'
                f'<a class="btn-sm" href="{profile}">View Profile</a>'
                f'<p class="social">{links}</p></div>'
            )
        out.append("</div>")
        return "\n".join(out)

    @env.macro
    def partner_logos():
        items = "".join(
            f'<a href="{p["url"]}" title="{p["name"]}"><img src="{local(p["logo"])}" alt="{p["name"]}" loading="lazy"></a>'
            for p in partners
        )
        return f'<div class="partner-logos" markdown="0">{items}</div>'
