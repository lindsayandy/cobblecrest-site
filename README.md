# Cobblecrest Chronicles website

Source files for cobblecrestchronicles.com. Claude edits these files when Andy asks for a change, and Cloudflare publishes every saved change on its own.

## How the site is built

- `src/pages/` holds one file per page. Each file starts with a short comment that gives the page's title, description, web address and menu item.
- `src/layout.html` holds the header, menu and footer that every page shares.
- `src/static/` holds the stylesheets, logo files, icons, and the Cloudflare settings files `_redirects` and `_headers`.
- `tools/build.py` puts the pages into the layout and writes the finished site to `site/`. Run `python3 tools/build.py` after any change. It needs only Python 3.
- `site/` is what Cloudflare publishes. It is rebuilt by the script, so edit `src/`, never `site/`.

## Cloudflare settings

The site runs as a Cloudflare Worker named `cobblecrest-site`, the same kind of project as the Cobblecrest Archive. It serves the `site/` folder as plain files and has no server code. `wrangler.toml` holds the settings.

| Setting (Worker, then Settings, then Builds) | Value |
| --- | --- |
| Git repository | `lindsayandy/cobblecrest-site` |
| Production branch | `main` |
| Build command | leave empty |
| Deploy command | `npx wrangler deploy` |
| Root directory | `/` |

The built `site/` folder is saved in the repository, so Cloudflare does not need to build anything. It only uploads the folder. Cloudflare reads `_redirects` and `_headers` from the folder, and unknown addresses get `404.html`.

Live at https://cobblecrestchronicles.com since October 22, 2026. The Worker serves the bare address and www. A Cloudflare redirect rule sends www to the bare address with a 301, and "Always Use HTTPS" (SSL/TLS, Edge Certificates) sends plain http addresses to https. The domain's DNS is on Cloudflare (free plan); the registration stays at Squarespace. Cloudflare Web Analytics counts visits (automatic setup, no code in the pages). The test address https://cobblecrest-site.cobblecrest.workers.dev still works.

Why a Worker and not Cloudflare Pages: in October 2026 Cloudflare's guidance says to use Workers for new projects, and new features go to Workers. Pages still works. Using a Worker keeps the site and the Archive on one system.

## Undoing a change

GitHub keeps every version of every file. Any change can be undone by restoring the earlier version, and Cloudflare then republishes the site.

## Credits

- Look and feel: the Cobblecrest Design System (made in Claude Design, October 2026). `src/static/css/tokens.css` is copied from it unchanged.
- Icons: [Lucide](https://lucide.dev) 0.414.0, ISC license (see `src/static/assets/icons/LICENSE-lucide.txt`).
- Fonts: Cinzel, EB Garamond, Alegreya Sans, Alegreya Sans SC and Courier Prime, loaded from Google Fonts.

## Parked ideas

- **Public Feat Forge (looked at October 22, 2026, parked by Andy).** The table version (claude.ai artifact "Cobblecrest Feat Forge") can't be linked. Its open feat grants and players' submissions show character names to anyone who opens it, and it needs a Claude sign-in. Its "Describe it" mode works only in the Google version, which uses an AI model. The plan if Andy picks it up again: a separate practice-only page on the Tools page, with the menu builder, point budget, scoring and D&D Beyond entry card, and with no grants, submissions, DM desk, sign-in or AI. Drafts would save in the visitor's browser. Check the rules text first: keep SRD wording with credit, and summarize or drop feats from paid books.
