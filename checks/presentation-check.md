# Presentation validation

- Revised deck: 23 pages, comprising 20 timed main slides and 3 reference slides. Rehearsal notes allocate 20 minutes, including 8.6 minutes across seven Lean slides.
- Source compiled successfully in two passes. Final log contains no LaTeX errors, warnings, overfull boxes, or undefined references.
- All 23 final pages were rendered at 120 dpi and individually visually inspected: no clipping, overlap, or illegible proof excerpts found. The automated layout audit also reported no warnings.
- The audit reader required filtering invalid XML control characters emitted by pdftotext for mathematical glyphs; bounding-box geometry and all layout checks were preserved.
- The required Lean sequence shows the original equation, directly included Lean contract and proof fragment, and an interpretation. Additional slides explain denominator conditions, proof tactics, the finite threshold, a failed attempt, a checked boundary counterexample, and partial coverage.
- The new presentation-only counterexample passed Lean (exit 0); see presentation-boundary-check.json. It is outside the frozen original lean/ folder.
- SHA-256 comparison confirmed all 34 original generated Lean-folder files remain unchanged, including local ignored source bytes. No source-coverage claim was upgraded: 0/6 full continuum propositions are proved.
- README banner was visually inspected; all local SVG assets parse successfully. Status badges explicitly describe the recorded run rather than live CI.
- No animations or screenshots of the paper are used. The title slide contains the repository link; version dates and differing page numbers are explicit.
- The genuine handwritten photograph remains missing. Slide 19 states this and includes hand/derivation.jpg automatically when supplied and recompiled.

Raw prompts.md intentionally preserves user message whitespace and is excluded from whitespace cleanup.
