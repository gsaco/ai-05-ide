# Presentation validation

- Source compiled successfully with `make slides LATEX=/Library/TeX/texbin/pdflatex` (two passes, exit 0).
- 20 PDF pages: 17 timed main slides and 3 reference slides.
- All pages rendered and visually inspected; no clipping, overlapping text, or unreadable code found after repairs.
- Final log: no LaTeX errors, overfull boxes, undefined references, or undefined citations.
- The first compile exposed a newer local hyperref / older LaTeX metadata-command mismatch. A guarded compatibility definition fixes it without changing the user's TeX installation.
- The required Lean slide includes the original firm equation, a directly included excerpt from the frozen Lean file, a proof-step explanation, and the actual build result. A second slide states the translation boundary and partial coverage.
- No animation commands or paper screenshots are used.
- The actual handwritten photograph remains missing. Slide 16 explicitly says so and automatically includes `hand/derivation.jpg` when provided and recompiled.
- The printed repository link is on the title slide; version dates and page differences are documented.

Raw `prompts.md` intentionally retains the user's trailing space and message boundaries; it is excluded from whitespace cleanup to preserve the requested raw transcript.
