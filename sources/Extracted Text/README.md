# Extracted UNO Rules

Ten UTF-8 Markdown files, one for each source PDF in the parent directory. Each filename matches its PDF with `.md` replacing `.pdf`. These files contain the English gameplay text, not just summaries. Markdown can be read directly by AI tools, search systems, text editors, and document-ingestion pipelines.

## File index

| Game or pack | Extracted text | Source PDF | Method |
| --- | --- | --- | --- |
| UNO Base Game | [uno-base-game-rules-en.md](uno-base-game-rules-en.md) | [PDF](../uno-base-game-rules-en.pdf) | Text layer + visual review |
| UNO Dare (accepted Adults Only substitute) | [uno-dare-rules-en.md](uno-dare-rules-en.md) | [PDF](../uno-dare-rules-en.pdf) | Text layer + visual review |
| UNO FLIP | [uno-flip-rules-en.md](uno-flip-rules-en.md) | [PDF](../uno-flip-rules-en.pdf) | Text layer + visual review |
| UNO Reverse Pack | [uno-reverse-pack-rules-en.md](uno-reverse-pack-rules-en.md) | [PDF](../uno-reverse-pack-rules-en.pdf) | Text layer + visual review |
| UNO Show 'em No Mercy Expansion Pack | [uno-show-em-no-mercy-expansion-pack-rules-en.md](uno-show-em-no-mercy-expansion-pack-rules-en.md) | [PDF](../uno-show-em-no-mercy-expansion-pack-rules-en.pdf) | Text layer + visual review |
| UNO Show 'em No Mercy | [uno-show-em-no-mercy-rules-en.md](uno-show-em-no-mercy-rules-en.md) | [PDF](../uno-show-em-no-mercy-rules-en.pdf) | Text layer + visual review |
| UNO Speed Pack | [uno-speed-pack-rules-en.md](uno-speed-pack-rules-en.md) | [PDF](../uno-speed-pack-rules-en.pdf) | Text layer + visual review |
| UNO Stack Pack | [uno-stack-pack-rules-en.md](uno-stack-pack-rules-en.md) | [PDF](../uno-stack-pack-rules-en.pdf) | Text layer + visual review |
| UNO Swap Pack | [uno-swap-pack-rules-en.md](uno-swap-pack-rules-en.md) | [PDF](../uno-swap-pack-rules-en.pdf) | Text layer + visual review |
| Liar's UNO | [liars-uno-rules-en.md](liars-uno-rules-en.md) | [PDF](../liars-uno-rules-en.pdf) | OCR + manual visual correction |

## What is preserved

- Contents, objectives, setup, turn sequence, action effects, examples, penalties, timing conditions, end-of-round rules, and optional scoring, wherever present in the source.
- Card names, numeric thresholds, requirements for expansions, and color-symbol legends.
- Source PDF page references, product codes, original source URLs, and SHA-256 hashes in YAML front matter.
- Rules and effects communicated by graphics are expressed in words in the separately labeled visual notes.

## Normalization and scope

English panels only. Repeated foreign-language panels, printing specifications, folding diagrams, decorative branding, and repeated card-art glyphs are omitted. Paragraph wrapping and multi-column reading order are repaired. Scoring mappings use Markdown tables. Publisher notice/contact text in the nine text-layer PDFs is retained; Liar's UNO retains publisher identification but omits its dense international contact block. This is a gameplay transcription, not a complete archival transcription of every mark on every production sheet.

Source-page sections follow the PDF page from which the English text was extracted. Some production PDFs display a larger multilingual sheet with repeated/overlaid artwork; the English rule sequence is presented once. The original PDFs remain authoritative.

## Notes for AI and other consuming systems

1. Treat the source transcription as evidence. Sections labeled “editorial” contain extraction notes, visual descriptions, or explicitly identified interpretation; they are not additional official rules.
2. Follow each file's `requires` field. The four classic add-ons require the base game; No Mercy Expansion requires No Mercy. Standalone editions have their own rules. Do not merge them automatically.
3. The Dare file is standard CDY11, accepted as a substitute for HRL30. It is not an Adults Only transcription. Its separate Dare List cards are not contained in the source PDF.
4. Retain source inconsistencies: FLIP's Light Side Flip paragraph repeats the Dark-to-Light direction; the overview establishes alternating sides. No Mercy's “25 or more” differs from the expansion Mercy coin's “more than 25.” Dare's 108-card heading also lists four reference cards. Relevant files explain these without silently changing the source.
5. An unmentioned interaction is unspecified in this source. Do not insert house rules or assume another edition's rule applies.

## Validation performed

All ten Markdown files were reopened and checked against source metadata and critical game-specific conditions. Native-text coverage was compared with the normalized text for all nine text-layer PDFs; differences were confined to documented layout artifacts, reordering, and formatting. Liar's UNO's English gameplay panel was checked visually after OCR, including the line OCR missed in Wild Liar's Challenge. Source PDF hashes were rechecked after extraction.
