# Cobblecrest Chronicles website

Source files for cobblecrestchronicles.com. Claude edits these files when Andy asks for a change, and Cloudflare Pages publishes every saved change on its own.

## How the site is built

- `src/pages/` holds one file per page. Each file starts with a short comment that gives the page's title, description, web address and menu item.
- `src/layout.html` holds the header, menu and footer that every page shares.
- `src/static/` holds the stylesheets, logo files, icons, and the Cloudflare settings files `_redirects` and `_headers`.
- `tools/build.py` puts the pages into the layout and writes the finished site to `site/`. Run `python3 tools/build.py` after any change. It needs only Python 3.
- `site/` is what Cloudflare publishes. It is rebuilt by the script, so edit `src/`, never `site/`.

## Cloudflare Pages settings

| Setting | Value |
| --- | --- |
| Production branch | `main` |
| Framework preset | None |
| Build command | leave empty |
| Build output directory | `site` |

The built `site/` folder is saved in the repository, so Cloudflare does not need to run anything.

## Undoing a change

GitHub keeps every version of every file. Any change can be undone by restoring the earlier version, and Cloudflare then republishes the site.

## Credits

- Look and feel: the Cobblecrest Design System (made in Claude Design, October 2026). `src/static/css/tokens.css` is copied from it unchanged.
- Icons: [Lucide](https://lucide.dev) 0.414.0, ISC license (see `src/static/assets/icons/LICENSE-lucide.txt`).
- Fonts: Cinzel, EB Garamond, Alegreya Sans, Alegreya Sans SC and Courier Prime, loaded from Google Fonts.
