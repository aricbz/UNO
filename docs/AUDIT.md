# Rebuild audit and decisions

## Starting state

The supplied folder contained 70 final PNG card/coin/marker/package assets, five final PNG logos, ten original PDFs, ten normalized English transcriptions, and indexes. It had no Git repository. No local application or uncommitted Git work was overwritten.

GitHub `aricbz/UNO` had only `main`, at `973751b0c4fafe867ae133ffb8210c4046e50b73`. Its tree had six standalone HTML pages, a favicon, README, and license. Each page bundled its own content/design/behavior. The README identified GitHub Pages and NFC URLs. Player-count errors and broad claims in the old site are not treated as official rules.

This environment blocked Git initialization at the materials-folder root, so the checkout lives in `UNO/`. The exact signed original commit/tree and every original file were hash-verified through GitHub retrieval. A successful fetch subsequently recovered all 29 original commits. No rewritten original commit is used as the base.

## Implementation

Native static HTML/CSS/JS serves fast lookups and browser-local settings without a server. Real legacy filenames work below a GitHub Pages repository prefix. Python regenerates the catalog and entry pages; there is no production build dependency.

Design: neutral charcoal game table, white condensed headlines, monochrome shared navigation, faithful card fans, edition-specific accents, and limited interaction movement. Edition accents use classic yellow, No Mercy ruby/burgundy, FLIP purple, Liar’s royal blue/navy, and Dare neon white with the supplied red/white logo glow. All 75 WebP derivatives total approximately 2.9 MB; the original 103 MB of PNG artwork remains untouched in the parent folder.

The catalog separates editorial summaries from full source transcription sections. Each verified card points to a section and PDF page. Substitute and unverified references have distinct labels. PDF hashes are checked against transcription metadata. Known house victories are opt-in; No Mercy empty-hand handling remains explicitly unresolved.

## Creative tools

Higgsfield’s official API help and pricing documentation were reviewed. It supports image/video generation but requires an account, credential, payment method and prepaid balance (currently a $5 minimum top-up; model/configuration rates vary). No credits were purchased or generations requested. CSS motion meets the current need. A future decorative video could be a static file with a still/reduced-motion fallback; recognizable card art should remain supplied artwork.

References: https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api and https://open.higgsfield.ai/pricing.

## Hosting safety

No Pages settings, default branch, or public deployment changed. There were no original workflow files. This rebuild stays on its separate branch. Production files contain the new implementation only; original application code remains in Git.
