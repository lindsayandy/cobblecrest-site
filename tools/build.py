#!/usr/bin/env python3
"""Build the Cobblecrest Chronicles website.

Reads the shared layout (src/layout.html) and each page (src/pages/*.html),
copies src/static/ as it is, and writes the finished site to site/.
Cloudflare (Workers static assets) publishes the site/ folder. Run this after any change:

    python3 tools/build.py

No packages are needed beyond Python 3.
"""
import hashlib
import html
import re
import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
OUT = ROOT / "site"

# The main menu, in order. Each entry is (key, label, path).
NAV = [
    ("home", "Home", "/"),
    ("play", "Play", "/play/"),
    ("hire", "Hire Andy", "/hire/"),
    ("world", "The World", "/world/"),
    ("tools", "Tools", "/tools/"),
    ("contact", "Contact", "/contact/"),
]

META_RE = re.compile(r"^\s*<!--(.*?)-->\s*", re.S)


def read_page(path):
    text = path.read_text(encoding="utf-8")
    m = META_RE.match(text)
    if not m:
        sys.exit(f"{path.name}: missing the metadata comment at the top")
    meta = {}
    for line in m.group(1).strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    for key in ("title", "description", "path"):
        if key not in meta:
            sys.exit(f"{path.name}: metadata needs '{key}'")
    return meta, text[m.end():]


def nav_html(current, indent):
    rows = []
    for key, label, href in NAV:
        cur = ' aria-current="page"' if key == current else ""
        rows.append(f'{indent}<a href="{href}"{cur}>{label}</a>')
    return "\n".join(rows)


def footnav_html(indent):
    return "\n".join(f'{indent}<li><a href="{href}">{label}</a></li>' for _, label, href in NAV)


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(SRC / "static", OUT)

    # A short fingerprint of the stylesheets, so browsers fetch new CSS after a change.
    h = hashlib.sha1()
    for css in sorted((SRC / "static" / "css").glob("*.css")):
        h.update(css.read_bytes())
    version = h.hexdigest()[:8]

    layout = (SRC / "layout.html").read_text(encoding="utf-8")
    pages = sorted((SRC / "pages").glob("*.html"))
    paths = []
    for page in pages:
        meta, body = read_page(page)
        title = meta["title"]
        full = "Cobblecrest Chronicles" if title == "Home" else f"{title} | Cobblecrest Chronicles"
        out = (layout
               .replace("{{title_full}}", html.escape(full, quote=True))
               .replace("{{description}}", html.escape(meta["description"], quote=True))
               .replace("{{path}}", meta["path"])
               .replace("{{version}}", version)
               .replace("{{year}}", str(date.today().year))
               .replace("{{nav}}", nav_html(meta.get("nav", ""), "      "))
               .replace("{{footnav}}", footnav_html("        "))
               .replace("{{content}}", body.strip("\n")))
        leftover = re.findall(r"\{\{[a-z_]+\}\}", out)
        if leftover:
            sys.exit(f"{page.name}: unfilled placeholders {leftover}")
        p = meta["path"]
        if p == "/404":
            dest = OUT / "404.html"
        else:
            dest = OUT / p.strip("/") / "index.html" if p != "/" else OUT / "index.html"
            paths.append(p)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(out, encoding="utf-8")
        print(f"built {dest.relative_to(ROOT)}")

    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sitemap += [f"  <url><loc>https://cobblecrestchronicles.com{p}</loc></url>" for p in sorted(paths)]
    sitemap.append("</urlset>")
    (OUT / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8")
    print(f"done: {len(pages)} pages, css version {version}")


if __name__ == "__main__":
    main()
