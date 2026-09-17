# Presentation validation — classic Beamer revision

- 26 slides in English, 16:9: 20 paper/exercise slides followed by exactly 6 Lean slides.
- Madrid theme, 12pt base text, light background, navy titles, teal blocks, and restrained gold emphasis. Headlines, footlines, navigation icons, and footer notes are disabled.
- Compiled with `make slides LATEX=/Library/TeX/texbin/pdflatex`; two passes, exit 0. No undefined references, missing files, or overfull/underfull boxes.
- Automated layout audit: no warnings. All 26 rendered slides and the contact sheet were individually visually inspected.
- Audit artifacts: `.tmp/hand-final/audit_report.md`, `.tmp/hand-final/contact_sheet.png`, and `.tmp/hand-final/pages/` (local ignored previews).
- The audit parser filters invalid XML control characters from pdftotext while preserving bounding-box geometry.
- Six Lean slides cover translation, the full finite-threshold statement and proof, proof explanation, the source wage identity, a checked counterexample, and honest build/coverage status.
- Lean excerpts are directly included from the unchanged original files. SHA-256 checks confirm all 34 original generated files remain unchanged.
- Existing Lean results remain unchanged: support build/fast check PASS; semantic preflight stopped; 0/6 full continuum propositions proved.
- Full speaking details and source page references are in analysis/presentation-notes.md rather than slide footers. Timing totals exactly 20 minutes.
- No animations or paper screenshots. Repository link is on the title slide.
- Both genuine photographs are preserved in hand/. Slides 18–19 display readable selected regions alongside typeset calculations and a verdict. The gap in the handwritten output inference is explicitly repaired by resource-allocation calculations.

Raw prompts.md preserves the actual user text and is excluded from whitespace cleanup.

- Added the economic opportunity-cost mechanism and primal–dual certification slides. Expanded the derivation and Lean tactic explanations without changing formalization claims.

- Rechecked P5/P6 against the pinned local source. Added explicit winner sets, neighborhood quantifiers, occupational clauses, strictness conditions, and the two distinct capability thresholds.
- The source wage slide now includes the original mathematical equation, exact Spec, proof fragment, symbol mapping, proof-step explanation, build result, and translation boundary.
