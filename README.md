# UNO: The Rulez

A visual game-night companion for Ari’s NFC-enabled card boxes. Five edition pages, source-backed card references, selectable expansions, and visibly separate house victory rules.

## Run locally

Python 3 and a modern browser are sufficient. Node 18+ is needed only for state tests. Generated static HTML pages and web assets are checked in; no dependency install is required to use the site.

```sh
python3 scripts/build.py
python3 -m http.server 4173 --bind 127.0.0.1 --directory dist
```

Open `http://127.0.0.1:4173`. All runtime URLs are relative, including when served below `/UNO/` on GitHub Pages.

```sh
node --test tests/state.test.mjs
python3 scripts/validate.py
```

Eight behavior tests and the content/asset checks pass. See [verification details](docs/VALIDATION.md) for browser coverage and remaining limits.

`npm run build`, `npm run test`, and `npm run dev` wrap these commands. Optional asset regeneration uses `npm install` then `npm run assets`; it requires the original `Card Assets` and `Game Logos` directories in the checkout’s parent. `SHARP_MODULE` can point to an existing Sharp module. Regeneration never modifies the originals.

## Product structure

- Collection: five decks with faithful logos and card art.
- Learn: setup, turns, victory, midgame questions, active pack reminders.
- Cards: search, FLIP side filters, source-backed dialogs, deep links.
- Table rules: edition-specific expansions and confirmed house victory choices.
- Sources: ten unchanged PDFs, transcriptions, page references, and source gaps.

Official settings are the initial default. House choices are opt-in and labeled everywhere they change victory. No Mercy’s last-standing house rule does not invent what happens when someone empties their hand; that remaining table decision is stated explicitly.

Settings persist per game in localStorage. A shared `?v=1&packs=...&house=...&continue=...` URL overrides local settings for that visit; “Remember this setup” saves it. Editing toggles also saves. Sharing is a snapshot, not synchronization. Native sharing is preferred; clipboard and selectable-link fallbacks are available.

## Content architecture

`scripts/build-content.py` holds concise learning summaries and explicit artwork/effect mappings. It reads the preserved Markdown transcriptions in `sources/Extracted Text/` and emits `content.json`. `app.mjs` renders that catalog; `state.mjs` contains pure configuration/filtering/sharing behavior. Correct a source-backed effect in one place, rebuild, and every view uses it.

There is no framework, bundler, account system, paid generation API, analytics, or runtime package dependency. Native dialogs and details provide keyboard/disclosure behavior. CSS respects reduced motion. Google Fonts have local fallback fonts.

## NFC and hosting

The original README identifies GitHub Pages at `https://aricbz.github.io/UNO/`; its original tree has static root HTML and no deployment workflow. Every current entry filename is retained, with redirects for older names found in Git history. Root publication and a static `dist/` artifact are supported. Actual Pages settings could not be verified through the connected API; confirm the deployment source before a future merge/publication.

| Existing route | New destination |
| --- | --- |
| `index.html` | Collection |
| `uno.html` | Classic + four add-on packs |
| `uno-show-em-no-mercy.html` | No Mercy + expansion |
| `uno-flip.html` | Both FLIP sides |
| `liars-uno.html` | Liar’s UNO |
| `uno-dare-adults-only.html` | Dare, with substitute-source labeling |
| `liars_uno.html` | Redirect to Liar’s UNO |
| `uno-dare.html` | Redirect to Dare Adults Only reference |
| `UNO Show Em No Mercy.html` | Redirect to No Mercy |
| `UNO Show Em No Mercy Full Rules.html` | Redirect to No Mercy |

Real `.html` files need no SPA fallback. `#learn`, `#cards`, `#table`, `#sources`, and `#card/<asset-id>` are supported. Common old panel fragments remain recognized. Historical redirects preserve queries and fragments. A disabled-pack card deep link opens its reference with an explicit opt-in to enable the pack; it never silently changes the deck.

Do not deploy or merge until Ari explicitly requests it. No deployment automation has been introduced.

## Preservation

Original exact commit: `973751b0c4fafe867ae133ffb8210c4046e50b73`.

- Local tag: `archive/original-before-rebuild`.
- Remote archival branch: `archive/original-before-rebuild`, same commit.
- Rebuild branch: `rebuild/uno-the-rulez`.
- Complete original 29-commit history is present locally.
- Original PNGs and source materials remain untouched in the parent folder.
- This `UNO/` checkout connects to the same `aricbz/UNO` remote. The supplied parent folder was a materials folder, not a checkout.

Connected GitHub tools support branches but not tag creation. HTTPS Git push has no authenticated machine credential; the tag remains local, while the remote archival branch preserves the identical commit. Once authenticated push is available:

```sh
git push origin refs/tags/archive/original-before-rebuild
```

To view the original without disturbing the rebuild:

```sh
git worktree add ../UNO-original archive/original-before-rebuild
```

## Known source limits

- Standard Dare CDY11 is the accepted substitute, not verified Adults Only HRL30 instructions. Die, Truth/reverse results, four dare levels, and actual dare lists are not invented.
- Base No Mercy eliminates at 25 or more; the expansion coin says rescue at more than 25. Rescue timing and unspecified expansion/stack interactions remain unresolved.
- FLIP’s Light Side Flip paragraph has an inconsistent direction sentence. The summary follows the overview’s alternating-side explanation and starting-Flip note; Sources flags this interpretation.
- The supplied 108-card classic leaflet does not document Shuffle Hands or Customizable Wild effects. Their artwork is marked as a source gap.
- Combined-pack edge cases remain table decisions unless specified in the sheets.

Original license: CC BY-NC-SA 4.0. UNO and its artwork belong to Mattel; this is an unofficial, noncommercial fan companion.
