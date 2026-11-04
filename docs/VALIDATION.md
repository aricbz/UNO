# Rebuild verification

## Automated checks

- Static build completes using Python 3, without package installation or a runtime server dependency.
- Eight Node state tests pass: cross-game pack rejection, active pack filtering, both FLIP sides, shared configurations below `/UNO/`, shared settings overriding saved preferences for a visit, house victory dependencies, malformed saved settings, and Liar’s challenge/victory exceptions.
- Catalog checks validate 69 card/marker references, 75 artwork derivatives, all ten source PDF hashes, edition-specific expansion requirements, and entry page references.
- HTTP checks return 200 for all 99 preview pages, runtime files, PDFs, images, and historical filename aliases.
- JavaScript syntax and Git whitespace checks pass.

## Browser review

Safari desktop collection, 390 × 844 phone layout, and 820 × 1180 tablet layout were inspected visually. Verified:

- Artwork and game logos load, and all four reference destinations stay visible on a phone.
- Changing Stack Pack and house victory updates the active table, victory explanation, and snapshot URL.
- Settings persist when opening the edition again without snapshot parameters.
- Card dialogs open from the grid and direct links; full source conditions expand; Escape closes the dialog and returns keyboard focus to the card.
- Historical `UNO Show Em No Mercy.html` redirects while retaining the query and card fragment.
- Disabled expansion card links show a warning. Explicitly enabling the expansion refreshes its card list and active configuration.
- The historical FLIP `#side-dark` fragment selects its six dark-side references.

Reduced-motion CSS was reviewed; a real mobile device and other browser engines have not been exercised. Native share sheets, clipboard permission variants, and the new manual-copy fallback still need broader device verification. The fallback retains the complete card/configuration URL.

## Source and deployment limits

See README for the accepted standard Dare substitute, missing modern classic Wild effects, FLIP wording inconsistency, Mercy coin threshold discrepancy, and unresolved combined-pack interactions. The No Mercy last-standing house victory intentionally leaves unspecified empty-hand handling to the table.

The site works as static root files or a `dist/` artifact. Both layouts contain `.nojekyll` to preserve Markdown transcriptions unchanged. Actual GitHub Pages deployment-source settings and physical NFC tags have not been tested. No production deployment or default-branch change was performed.
