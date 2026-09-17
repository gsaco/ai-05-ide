# Independent source-only intake

Source: `source.txt`, complete 35-page main paper, arXiv:2312.05481v11 (24 February 2025), title-page date 25 February 2025. Source text read in full, including references. No Lean files or source maps consulted. This is discovery and scope classification, **not semantic acceptance**. Locators below use physical text line numbers (as `nl -ba` reports) and printed PDF pages. PDF pages 19 and 27 were visually inspected against the extraction.

## Named inventory (`material_named_claim`)

No numbered/named lemmas, corollaries, or separately stated theorems occur. There are six propositions and one named definition. “First Welfare Theorem” (lines 734–743) is an invocation in explanatory prose, not a newly stated named theorem. All formal mathematical proofs are relegated to an Online Appendix (line 282, p. 7), which is **not contained in this canonical 35-page source**. Consequently there are no formal proof-local labeled claims to invent or recover from another version.

| Source label | Exact locator | Statement coverage |
|---|---|---|
| Definition (Competitive Equilibrium) | 557–562, p. 13 | Nonnegative compute allocations; measurable occupation sets; matching satisfying (1); nonnegative wage schedule/rental rate; optimal zero-profit firm structure; compute clearing; occupation cover with pairwise measure-zero overlap. Governing definitions at 499–555, pp. 12–13 are attached context, not separate results. |
| Proposition 1 | 715–731, p. 16 | Pre-AI unique efficient equilibrium; occupational stratification; strict positive assortative matching; nonempty workers and solvers; independent producers iff h>h0∈(0,1); continuity, strict increase and convexity of wages (strict on W∪S); all three wage formulas and solver integration constant; strict wage dominance outside cl I and everywhere when h<h0. |
| Proposition 2 | 828–858, pp. 18–19 | Autonomous-AI unique efficient equilibrium; occupational order; W*⪯{zAI}⪯S*; human matching and Wa*⪯Wp*, Sp*⪯Sa*; AI independent production; conditional necessary worker/solver use; r*=zAI; wage regularity; all five occupation-specific wage formulas; integration constant and all three boundary identities. |
| Proposition 3 | 987–989, p. 22 | Basic AI zAI∈int W: W*⊂W, S*⊃S; advanced AI zAI∈int S: W*⊃W, S*⊂S. Preserve strict set-inclusion claims. |
| Proposition 4 | 1006–1013, p. 22 | Basic AI: retained workers' productivity strictly falls; retained solvers' span strictly rises if e(z)<zAI, strictly falls if e(z)>zAI. Advanced AI: retained workers' productivity strictly rises for z<e(zAI), strictly falls for z>e(zAI); retained solvers' span strictly rises. Adjacent definitions at 998–1004 identify productivity as expected output per unit time / solver knowledge and span as worker count. Equality cases are not asserted. |
| Proposition 5 | 1091–1092, p. 24 | B nonempty iff zAI>bar zAI, with bar zAI∈int W; T nonempty for every zAI∈[0,1). B/T definitions and relevant assumptions are detailed below. |
| Proposition 6 | 1217–1232, p. 27 | Non-autonomous unique efficient equilibrium maximizing labor income; r⋆=0; both adoption regimes and occupation nonemptiness; strictly greater autonomous output; existence of weak/strict losers; local least-knowledgeable wage comparison to BOTH pre-AI and autonomous AI; local most-knowledgeable comparison and its stated strictness exception. See full conditions below. |

## Governing context attached to named claims

- Model primitives: lines 393–421, pp. 9–10. Unit human mass, unit time, z∈[0,1], continuous strictly positive density g, perfectly observable knowledge, competitive identical firms, no fixed cost and at most two layers; independent uniform problem difficulty, unit output on success; h∈(0,1); n(z) satisfies h n(z)(1−z)=1 for z<1. These specify the meaning of all propositions and the equilibrium definition, not a second headline result.
- Autonomous technology and feasible configurations: 451–467, p. 11. Common exogenous zAI∈[0,1), unit compute per agent, perfect human substitute, universally available AI, exogenous µ; production opportunities exceed combined human/AI capacity. Footnote 11 at 492–493 excludes zAI=1 due to discontinuity.
- Wages, normalization and profits: 500–523, p. 12. Risk neutrality and income maximization, compute to highest bidder, unit output price; Π1 and all three Π2 formulas with z≤zAI, zAI≤s, z≤s restrictions. Compute allocations and measurable sets: 525–540; matching and resource equality (1): 546–555, pp. 12–13. Resource equality is for **every measurable Y⊆Wp**.
- Abundant compute: 576–597, p. 13. More AI agents than can be matched with humans, so some independent AI production. Footnote 14 gives sufficient bound ∫₀^{zAI} n(z)⁻¹dG(z)+n(zAI)(1−G(zAI))<µ and claims a finite µ can satisfy it for all zAI∈[0,1), for any G and h∈(0,1). Attach abundance as hypothesis; retain the finite-uniform-bound assertion as a deep-audit observation.
- Notation: 601–610, p. 14. W=Wa∪Wp, S=Sa∪Sp; e is inverse matching function; int and cl; B⪯B′ means sup B≤inf B′.
- Pre-AI: 709–713, p. 16; µ=0, Wa=Sa=∅. The restriction **h<h0** is introduced at 814–816, p. 18, and governs ensuing baseline comparisons (P2–P6); it is not an extra premise of the full P1 characterization.
- Star distinction: 824–826, p. 18, and 1201–1202, p. 26. Plain symbols pre-AI, * autonomous, ⋆ non-autonomous. Do not collapse the two stars.
- Basic versus advanced: 944–947, p. 21. Interior W versus interior S; knife-edge W∩S referred to Online Appendix.

## Proposition 5: complete contextual conditions

P5 concerns autonomous AI under the Section 3.1 model, abundant compute, at most two layers, zAI∈[0,1), and h<h0. Pre-AI W and S are from P1. Lines 1084–1089, p. 24 define

- B={z∈[0,zAI]:w*(z)>w(z)};
- T={z∈[zAI,1]:w*(z)>w(z)}.

Benefits mean **strict wage increases**, not weak gains or productivity gains. The adjacent prose states w*(zAI)<w(zAI), B=[0,zb), T=(zt,1], zb≥0, zt≤1. The threshold belongs to **int W**, and the iff uses a **strict** zAI>bar zAI; equality does not produce B winners. “Always” for top winners is expressly restricted to zAI∈[0,1). Lines 1143–1151, p. 25 explain the h<h0 dependence; footnote 19 (1160–1162) explicitly says both h<h0 and zAI<1 matter, and reports that at zAI=1 the most knowledgeable humans necessarily lose. Do not extend P5 to h≥h0 or superintelligent AI. The adjacent interval-shape result is not itself a numbered P5 clause: classify it deep_audit_material while attaching its definitions to P5.

## Proposition 6: complete contextual conditions

Lines 1192–1202, p. 26 explicitly keep the Section 3.1 model, modifying only that AI cannot pursue production opportunities. Single-layer automated and bottom-automated firms produce no output; Sa=∅ and µw=0; µi now denotes **idle compute**. Firms have at most two layers, and autonomous/non-autonomous comparisons use **identical compute availability, abundant relative to human time**. Baseline h<h0 and zAI∈[0,1) persist. Plain w is the **pre-AI wage schedule** (1215), so adoption threshold w(0) is endogenous to the benchmark, not zero or zAI.

Full clause checklist:

1. Unique equilibrium, efficient, maximizes labor income, r⋆=0.
2. If zAI≤w(0): Wa⋆=∅, and human occupations AND wages coincide with pre-AI.
3. If zAI>w(0): Wa⋆⪯(Wp⋆∪I⋆∪Sp⋆); Wa⋆, Wp⋆, Sp⋆ are all nonempty, I⋆ possibly empty.
4. In either regime: autonomous total output is **strictly** higher than non-autonomous.
5. ∃z∈(0,1] with w⋆(z)≤w(z), strict when zAI>w(0). The existential excludes z=0.
6. ∃ϵ>0, ∀z∈[0,ϵ): w⋆(z)≥max{w(z),w*(z)}, strict if zAI>w(0). Both comparisons and the neighborhood quantifiers matter.
7. ∃ϵ>0, ∀z∈(1−ϵ,1]: w⋆(z)≤w*(z), **strict if z≠1**. This exception is printed in the PDF, not an extraction error. Do not replace it with strictness conditioned on AI adoption or silently strengthen the endpoint.

## Additional mathematical presentations (`deep_audit_material`)

These unnumbered observations, derivations, example calculations, and extension assertions are source-discovery candidates, not additional accepted named results. Context already attached above is not double-counted as an independent result.

| Locator | Presentation / audit candidate |
|---|---|
| 569–574, p. 13 | Five-component total-output integral; aggregate wage integral; µr capital income; zero profit gives output=total labor+capital income. |
| 585–591, p. 13, footnote 13 | Interval approximation underlying pointwise matching and solver-time balance. |
| 593–597, p. 13, footnote 14 | Sufficient compute bound plus finite µ uniform in zAI assertion. |
| 676–694, pp. 15–16 | Multiple-AI extension: only most advanced technology used with similar compute requirements; potential coexistence when less advanced AI needs substantially less compute. |
| 696–706, p. 16 | No-unemployment argument from scarce resources/abundant opportunities; extension with excess compute makes all humans below AI knowledge unemployed while hierarchy survives. |
| 734–757, pp. 16–17 | Welfare theorem/marginal-product interpretation, occupational comparative advantage, complementarity and matching argument, low-h two-layer adoption argument. Explanatory support to P1 rather than new named theorem. |
| 736–737, p. 16, footnote 17 | µ=0 differs from µ>0,zAI=0: ignorant AI can pursue opportunities and expand frontier. |
| 782–785, p. 17 | Figure 3 uniform G(z)=z example, h0=3/4, h=1/2 and 0.8125. |
| 791–813 and 831–834, p. 18 | Marginal knowledge value <1 for workers, =1 independent, >1 solvers; firm maximization display; FOC w′(m(z))=n(z), wage integral derivation; footnote 18 marginal solver-time/output calculation. Informal proof-local derivations supporting P1. |
| 867–881, 913–934, pp. 19–21 | Informal P2 proof: scalability plus sorting, AI must interact with humans, contradiction w*(zAI)=w(zAI)>zAI, market-clearing contradiction if wrong occupation; r*=zAI and both automation zero-profit wage equations; continuity and independent-production boundary argument. |
| 905–910, p. 20; 974–977, p. 21 | Uniform-distribution equilibrium examples with h=1/2 and zAI=0.425 or 0.85; different AI roles. |
| 991–997, 1020–1024, 1051–1056, pp. 22–23 | Comparative-static mechanisms for P3/P4, including changing pool of solvers and retained-solvers' matches. |
| 1045–1048, p. 23 | Figure 6 explicit parameter example for P4. |
| 1071–1078, pp. 23–24 | Total labor income increases with autonomous AI; contradiction from aggregate profits of old firms; output increase from labor+capital income. Unnumbered observation, **not** extra numbered proposition. |
| 1084–1089, p. 24 | Strict loss at zAI and interval shapes of B,T. Definitions govern P5; shape assertion remains deep. |
| 1098–1115, 1143–1151, pp. 24–25 | Endpoint reduction for winners; opposing match/share effects; basic threshold and advanced least-knowledgeable gains; h restriction for top gains. |
| 1160–1162, p. 25, footnote 19 | Superintelligent zAI=1 exception: top humans lose. |
| 1207–1211, p. 26 | Idle compute gives r⋆=0; w⋆(zAI)≠r⋆ because non-autonomous AI is no perfect human substitute. |
| 1234–1252, p. 27 | Adoption threshold and binding autonomy constraint/output explanation; distributional mechanism supporting P6. |
| 1287–1300 and 1310, pp. 28–29 | Two-layer one-escalation implicit cost; humans just below AI prefer human help; arbitrary layers/no asking cost extension shifts all z<zAI toward zAI; endpoint preference claim persists. |
| 1303–1306, p. 28, footnote 21 | Equilibrium continuity in compute; results persist for small positive compute price; qualified limited-compute extension. |
| 1343–1347, p. 29, footnote 22 | More-than-two-layer advanced AI may amplify top expertise, but top humans still prefer autonomous AI. |
| 1323–1325, p. 29 | Co-pilot/co-worker emergence conditions summarized. |
| 1372–1383, p. 30 | Homogeneous scalable AI differs from offshoring/immigration; formal extension referenced but not supplied. |
| 1385–1408, pp. 30–31 | Partial adoption from autonomous opportunity cost and non-autonomous useless advice for knowledgeable workers. |
| 1410–1419 and 1438–1442, p. 31 | Better communication/more knowledgeable population raises pre-AI solver cutoff; reducing h displaces humans from solving into routine work. |
| 1421–1427, p. 31 | Policy interpretation: autonomy increases output and exacerbates labor-income inequality. Unnumbered broad inequality assertion, not an extra P6 clause. |

## Extraction cautions and scope limits

- P6 item 4 strictness “if z ≠ 1” visually verified on PDF p. 27; preserve exactly.
- P2 boundary line 858 visually verified on PDF p. 19: w*(sup W*)=sup Wp*, w*(zAI)=zAI, w*(inf S*)=inf Sp*. The right-hand subscripts p are real; do not silently normalize them away. Empty-set/boundary conventions merit semantic audit rather than extraction repair.
- Integrals appear as `R` with bounds on adjacent lines, especially lines 727–728, 853–855, and 593–595. P2 lower bound is inf Sp*, with C*=inf Sp* (visually verified). Formula line wrapping is not missing hypotheses.
- PDF mathematical stars * and ⋆ distinguish economies; subscript/superscript placement and overbar on bar zAI must be retained. `intW`, `clI`, and `z∈ / clI` are extraction formatting, not new symbols.
- Figures contain poorly extracted embedded labels (e.g. Figure 1's `/(1)`), and Figure 8 extraction includes configurations visually crossed out. Do not infer extra feasible non-autonomous firms from raw figure text; adjacent prose at 1192–1196 is explicit.
- P1 uses strict convexity “when z∈W∪S”; precise piecewise/boundary interpretation is a later semantic issue. No discovery claim resolves endpoint ownership, measure-zero overlap, empty-set ordering, or the mathematical meaning of uniqueness.
- No appendix proof claims or claims from arXiv v6/v10 were imported. References to these extensions are recorded as unresolved deep-audit presentations only.
