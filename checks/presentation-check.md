# Presentation validation — classic Beamer revision

- 22 slides in English, 16:9: 16 paper/exercise slides followed by exactly 6 Lean slides.
- Madrid theme, 12pt base text, white background, blue titles. Headlines, footlines, navigation icons, and footer notes are disabled.
- Compiled with `make slides LATEX=/Library/TeX/texbin/pdflatex`; two passes, exit 0. No undefined references, missing files, or overfull/underfull boxes.
- Automated layout audit: no warnings. All 22 rendered slides and the contact sheet were individually visually inspected.
- Audit artifacts: `.tmp/classic-final/audit_report.md`, `.tmp/classic-final/contact_sheet.png`, and `.tmp/classic-final/pages/` (local ignored previews).
- The audit parser filters invalid XML control characters from pdftotext while preserving bounding-box geometry.
- Six Lean slides cover translation, the full finite-threshold statement and proof, proof explanation, the source wage identity, a checked counterexample, and honest build/coverage status.
- Lean excerpts are directly included from the unchanged original files. SHA-256 checks confirm all 34 original generated files remain unchanged.
- Existing Lean results remain unchanged: support build/fast check PASS; semantic preflight stopped; 0/6 full continuum propositions proved.
- Full speaking details and source page references are in analysis/presentation-notes.md rather than slide footers. Timing totals exactly 20 minutes.
- No animations or paper screenshots. Repository link is on the title slide.
- Remaining requirement: genuine handwritten photograph, explicitly pending on slide 15. Supplying hand/derivation.jpg and rebuilding inserts it automatically.

Raw prompts.md preserves the actual user text and is excluded from whitespace cleanup.
