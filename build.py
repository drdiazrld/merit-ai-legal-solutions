#!/usr/bin/env python3
"""Assemble the Merit AI Legal Solutions multi-page site from partials + page bodies."""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent
PARTIALS = ROOT / "partials"
PAGES = ROOT / "pages"
OUT = ROOT  # pages land in marketing/site/*.html

NAV_KEYS = ["CAP", "ORC", "GAI", "LAI", "PRO", "TES", "SEC", "COM", "PIL"]

def build():
    head = (PARTIALS / "head.html").read_text()
    nav_tpl = (PARTIALS / "nav.html").read_text()
    footer = (PARTIALS / "footer.html").read_text()

    for src in sorted(PAGES.glob("*.html")):
        body = src.read_text()
        title = re.search(r"__TITLE__\s*(.*?)\s*$", body, re.M).group(1).strip()
        # drop the title token line from body
        body = re.sub(r"^__TITLE__\s*.*$", "", body, flags=re.M)

        nav = nav_tpl
        stem = src.stem
        active_key = {"index": None, "capabilities": "CAP", "orchestration": "ORC",
                      "vs-general-ai": "GAI", "vs-legal-ai": "LAI", "proof": "PRO",
                      "testing": "TES", "security": "SEC", "compliance": "COM", "pilot": "PIL"}.get(stem)
        # activate this page's nav link BEFORE blanking the tokens
        if active_key:
            nav = nav.replace(f'class="nav-cta __NAV_ACTIVE_{active_key}__"', 'class="nav-cta active"')
            nav = nav.replace(f'class="__NAV_ACTIVE_{active_key}__"', 'class="active"')
        for key in NAV_KEYS:
            nav = nav.replace(f'class="nav-cta __NAV_ACTIVE_{key}__"', 'class="nav-cta"')
            nav = nav.replace(f'class="__NAV_ACTIVE_{key}__"', '')

        page = head.replace("__TITLE__", title) + nav + body + footer + "\n</body>\n</html>\n"
        out = OUT / (stem + ".html")
        out.write_text(page)
        print(f"built {out.name}  ({len(page):,} chars)")

if __name__ == "__main__":
    build()
