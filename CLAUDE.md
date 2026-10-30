# Working on the Cobblecrest Chronicles website

Andy asks for changes in plain language. Make the change, rebuild, check it, and save it to GitHub. Andy does not want to settle small details: decide them by the rules below and tell him what you did in a sentence or two.

## Every change

1. Edit files in `src/`, never in `site/`.
2. Run `python3 tools/build.py`.
3. Look at the changed page at desktop (1366 wide) and phone (375 wide) sizes before saving. Check for sideways scrolling and broken links.
4. Commit with a short plain message and push to `main`. Cloudflare publishes within a few minutes.
5. After publishing, load the live page to confirm the change.

## Rules that always apply

- **Fan Content notice.** Every page carries the Wizards of the Coast Fan Content notice. It lives in `src/layout.html`. Never remove it.
- **No Wizards trademarks in names.** "D&D", "Dungeons & Dragons", "Forgotten Realms" and "Dungeon Master" may describe things in body text, but never appear in the name of the site, a product, a page title or a brand.
- **Nothing paid that uses Wizards lore.** Everything on this site is free. Anything that is ever sold must be Cobblecrest-original or SRD with attribution.
- **Kids.** Never name, describe or picture a homeschool student, and never name the homeschool organization.
- **Player secrets.** Session plans are posted about three weeks after they run, with live secrets removed.
- **Player data.** Link only tools that hold no player data. Loot Claims and Feat Forge show player and character names, so they stay off the public site.
- **Facts.** Prices, times, policies and addresses come from Andy or his records. Never invent one. If a fact is unknown, leave it out and ask.
- **Guide updates.** Whenever the Player's Guide or Eddred's Regional Guide changes, refresh both copies in the same session, without being asked. One copy is the PDF on this site (steps under "Links worth knowing"). The other is the Cobblecrest Archive (`lindsayandy/cobblecrest-archive`, README section "When the Player's Guide or Regional Guide changes"). Then tell Andy both are done.

## Writing

- Plain American English at about an eighth-grade level. One idea per sentence.
- No exclamation marks, emoji, hype words, rhetorical questions, or "not just X, it's Y" lines.
- Voice from the design system: plain, concrete, slightly dry, like a game master who has run the thing twice.

## Look

The look comes from the Cobblecrest Design System (artifact "Cobblecrest Design System" in Andy's Claude account). `src/static/css/tokens.css` is copied from it unchanged; style pages in `src/static/css/site.css` using its semantic tokens.

- Square corners (5px at most), flat color, no gradients, no textures.
- One rust (ember) accent per view, usually the main button.
- The only ornament is the divider: two hairlines with a small diamond between them (`<div class="rule"><i></i></div>`).
- The logo is the original black badge on white (`badge-*.jpg` in `src/static/assets/`), shown as a round seal with `border-radius: 50%` on light and dark backgrounds alike. Never redraw or recolor it. No empty picture placeholders.
- Icons come from Lucide 0.414.0 and are copied into `src/static/assets/icons/`. Add a new one by copying its SVG from the same version.

## Links worth knowing

- Lore app (public): https://cobblecrest-archive.cobblecrest.workers.dev/ (also `/archive` on this site)
- Merch shop (Fourthwall): https://cobblecrest-chronicles-llc-shop.fourthwall.com/ (also `/shop` on this site). The Merch page shows eight products with photos copied into `src/static/assets/merch/` (360 by 480). Prices are left off the page because they change in the shop. If a product is renamed or removed in the shop, update or drop its card. Keep the shop at a product count other than 13.
- State of Comics sign-up list: https://stateofcomics.com/pages/d-d-registration
- Guides: the site serves PDF copies from `src/static/guides/` (the Player's Guide and Eddred's Regional Guide). Andy's working Google Docs stay private, so never link them. Each PDF has a Fan Content notice page right after its cover. When Andy updates a guide, export its newest version to PDF, run `python3 tools/add_notice.py <source.pdf> "<Guide title>" <output.pdf> <scratch.pdf>`, replace the file in `src/static/guides/`, and update the page count on the World page.
- Player's Guide working doc (private): https://docs.google.com/document/d/1va5MrvD87q2X3s9EhSouN9FIPFhzDNDuEx2mEbWJsRA/edit
- Regional Guide source PDF (1498 DR, in Drive): https://drive.google.com/file/d/1tcalCuIXdRtSmLXGf3leVbOt2jZSEEU9/view
- Old Google Sites addresses redirect to the new pages through `src/static/_redirects`.
