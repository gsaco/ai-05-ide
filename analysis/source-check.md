# Source check and claims ledger

Read versions: course PDF, May 20, 2025; pinned arXiv v11, title date February 25, 2025. The latter's submission stamp is February 24. All page numbers below are printed PDF pages. The course document is v12, so calling v11 the latest available version would be inaccurate; v11 is the assignment's formalization pin.

| Claim used in the presentation | Source location | What is and is not established here |
|---|---|---|
| n(z)=1/[h(1−z)] | v11 §3.1, p.10; course §3.1, p.11 | Derived from solver time; domain excludes a worker with z=1 |
| Two-layer profit is n(z)[s−w(z)]−w(s) | v11 p.12; course p.12 | Used to derive finite-model no-entry and zero-profit equations |
| Competitive equilibrium includes measurable occupational sets and matching resource constraint | v11 p.13; course p.13 | The finite LP replaces these by three resource constraints; this is a changed domain |
| Sufficient compute abundance bound | v11 p.13 fn.14; course corresponding §3.1 | Applied separately to the selected finite capabilities, not asserted for all a approaching 1 with μ=2 |
| h<h₀ imposed after pre-AI characterization | v11 p.18; course p.19 | Not assigned a continuum h₀ value for the discrete population |
| Autonomous rental r=a and wages by active role | Proposition 2, v11 pp.18–19; course pp.19–20 | Rental has an independent-production outside-option justification; finite examples verify leftover compute |
| Bottom winners iff a>ā, with ā in int W; top winners for every a<1 | Proposition 5, v11 p.24; course p.25 | Reported as the paper's result; not proved by finite computations or an algebraic Lean lemma |
| Humans exactly matching AI knowledge lose | v11 §5.2 p.24; course p.25 | Uses baseline w(a)>a and post-AI wᴬ(a)=a; a finite grid need not contain such a human type |
| Top gains depend on h<h₀ and a<1 | v11 p.25 and fn.19; course pp.26–27 fn.19 | Conditions are shown explicitly; perfect AI is excluded |
| Non-autonomous adoption requires a>w(0) | Proposition 6, v11 p.27; course p.28 | Distinct from ā; weak versus strict claims retained |
| Bottom/top neighborhood wage comparisons, existence of losses, strict total output comparison | Same Proposition 6 | Full quantifiers appear on an appendix slide; output and labor income kept separate |

The unchanged Proposition 5 and 6 statements were checked against both PDFs. The two versions differ in surrounding material and pagination; no assertion that their entire contents are identical is made.

## Claims rejected or qualified

1. **“Distribution is driven by autonomy, not capability.”** Rejected as an exhaustive account. Both propositions contain strict capability thresholds relevant to bottom gains or adoption.
2. **“Basic autonomous AI always hurts the bottom.”** Rejected. Since ā lies inside the pre-AI worker region, capabilities in that region above ā generate bottom winners too. The more precise proposition governs the interpretation of broad introductory prose.
3. **“Co-pilots always strictly help the bottom.”** Rejected. If a≤w(0), the source says no adoption and unchanged wages. The relevant endpoint comparison is then weak.
4. **“All top humans strictly prefer autonomy, including z=1.”** Qualified. Proposition 6 guarantees a neighborhood inequality and strictness away from z=1; it does not assert strictness at that endpoint.
5. **“An LP verifies Proposition 5.”** Rejected. It checks selected finite equilibria, while the source theorem concerns a continuum with a positive continuous density.
6. **“A Lean proof of a wage rearrangement verifies equilibrium.”** Rejected. Zero profit and the rental premise must still be justified; market clearing, existence, uniqueness, and sorting are separate obligations.
7. **“Strict output superiority follows by putting idle AI to work even at a=0.”** Rejected as a proof. Independent output aδ vanishes there; AI workers helped by knowledgeable humans supply the remaining mechanism.

These are checks of claims, not invented quotations from a prior model conversation. The original user prompt contains the suggested autonomy-only gloss. The actual exchange is retained in `prompts.md`.
