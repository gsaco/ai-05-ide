# Rehearsal: classic Beamer, 20 minutes

26 English slides: 20 on the paper and finite exercise, followed by exactly six on Lean. All conditions and local comparison quantifiers are explicit. No footer notes.

| Slide | Topic | Time | Cumulative |
|---|---|---:|---:|
| 1 | Title | 0:15 | 0:15 |
| 2 | Question and source | 0:25 | 0:40 |
| 3 | Autonomy and capability are different dimensions | 0:35 | 1:15 |
| 4 | The agent's problem: organize knowledge and time | 0:50 | 2:05 |
| 5 | Conditions: people, problems, and firms | 0:30 | 2:35 |
| 6 | Conditions: scarce time and abundant compute | 0:40 | 3:15 |
| 7 | Proposition 5: capability determines bottom gains | 0:55 | 4:10 |
| 8 | Proposition 6: adoption still requires capability | 0:45 | 4:55 |
| 9 | Proposition 6: local comparisons, explicit quantifiers | 0:50 | 5:45 |
| 10 | Proposition 6: equilibrium, losses, and output | 0:50 | 6:35 |
| 11 | Why autonomy changes the distribution | 0:55 | 7:30 |
| 12 | A three-type economy we can solve directly | 0:55 | 8:25 |
| 13 | Autonomous AI: solve one equilibrium branch | 1:00 | 9:25 |
| 14 | Same autonomy, different bottom outcomes | 0:50 | 10:15 |
| 15 | Numerical results separate the two dimensions | 0:35 | 10:50 |
| 16 | More output does not imply more labor income | 0:40 | 11:30 |
| 17 | What the computational check establishes | 0:50 | 12:20 |
| 18 | Hand check: capability changes who gains | 0:20 | 12:40 |
| 19 | Hand check: wages are not total output | 0:20 | 13:00 |
| 20 | What the paper and the example teach us | 0:25 | 13:25 |
| 21 | Lean 1/6: from economics to a precise statement | 0:45 | 14:10 |
| 22 | Lean 2/6: the bottom-gain threshold | 1:20 | 15:30 |
| 23 | Lean 3/6: why the inequality proof works | 1:10 | 16:40 |
| 24 | Lean 4/6: paper equation, contract, and checked proof | 1:15 | 17:55 |
| 25 | Lean 5/6: a missing assumption changes the claim | 1:00 | 18:55 |
| 26 | Lean 6/6: what passed and what remains open | 1:05 | 20:00 |

## Oral detail and source references

**Slides 2–6.** Read Ide and Talamàs (2025), course PDF May 20, 39 pages; the Lean run pins arXiv v11, February 25, 35 pages. Explain that knowledge determines which problems can be solved; autonomy determines permitted production roles. Helping consumes time even when unsuccessful. The population has continuous positive density in the paper. The finite example changes that domain. The assumptions h<h₀, a<1, opportunity abundance, and compute abundance are substantive.

**Slides 7–9.** Proposition 5 is v11 p.24 / course p.25; Proposition 6 is v11 p.27 / course p.28. Define B={z≤a:wᴬ(z)>w(z)} and T={z≥a:wᴬ(z)>w(z)} within [0,1]. The autonomous threshold is inside the pre-AI worker set. State the iff and strict inequality aloud. Under co-pilot adoption, AI-assisted workers, human-assisted workers, and human solvers are nonempty; independent humans may be absent. AI-assisted workers occupy the lowest positions. There exists ε>0 such that the bottom comparison holds for every z∈[0,ε); a possibly different ε gives the top comparison on (1−ε,1]. The top comparison is strict except at z=1. There is some z∈(0,1] with wᴺ(z)≤w(z), strict under adoption. Efficiency and labor-income maximization are within the co-pilot technology, not across technologies.

**Slides 12–14.** Subtract the first two baseline zero-profit equations to get t−v=1; the third then gives v=.6, t=1.6, u=.2. Baseline worker masses for L→M, L→H, M→H are .32,.23,.14. In the autonomous branch .55 low workers use .275 middle solvers; the remaining .025 middle humans supervise AI and pin their wage. AI-worker compute demand 7/[20(1−a)]<2 leaves spare compute. All no-entry inequalities are checked in analysis/derivation.md. At a=2/7 there is equality, not a strict gain. This is not the numerical value of the continuum threshold.

**Slides 15–16.** The lines join only three discrete types. Compare across panels to isolate capability and within panels to isolate autonomy. At a=.4, co-pilot wages are (.4,.7,1.2), autonomous wages (.25,.5,2). Output includes compute-owner income. Autonomous production contains the co-pilot feasible set. If a>0 and compute is idle, independent AI adds strictly positive output; a=0 needs the separate human-assisted AI-worker mechanism. Numerical checks certify the finite examples, not the continuum theorem.

**Slides 18–20.** The genuine photos appear on slides 18–19. Point out the gap in the handwritten “Hence”: output follows from feasible production allocations, not wage rankings. The hand guide supplies the full calculation. Explain the verdict in your own words: capability changes bottom gains even when autonomy is held fixed.

**Slide 21.** A Spec is a proposition. Lean checks a term of that type. The source-to-Spec translation is a separate audit, and a familiar theorem name is not evidence of source fidelity.

**Slides 22–23.** The displayed statement and proof are directly included from lean/DiscreteCalculations.lean. Real a is quantified, with 0<a<1/3. bottomWage is the candidate formula a/[2(1−a)], not a proven equilibrium object. hden proves positivity, which preserves the direction when clearing the fraction. constructor splits the equivalence; linarith checks each linear implication. The proof builds, but Proposition 5 remains unproved.

**Slide 24.** FirmAlgebra.zeroProfitWage quantifies real h,z,a,w,r with 0<h<1 and 0≤z<1, and explicitly assumes zero profit. The displayed proof obtains both nonzero factors, unfolds span and profit, clears denominators, and finishes with nlinarith. Bounds h<1 and z≥0 remain in the statement although unused by the algebra. Arbitrary real a,w,r are an algebraic generalization. Active roles, market clearing, and equilibrium rent values are not established. The source equation is on v11 pp.10/12. The original run first failed to clear a remaining factor denominator when given only a product's nonzero proof; supplying both factors repaired that tactic step.

**Slide 25.** Distinguish a failed tactic from an invalid mathematical generalization. The counterexample at z=1 uses Lean's total real division. It is outside the worker domain and refutes only the unrestricted algebraic claim. analysis/BoundaryCheck.lean compiled with exit 0; its result is recorded separately in checks/presentation-boundary-check.json. The original lean/ snapshot is unchanged.

**Slide 26.** The required fast check passed, as did the full root build. The semantic preflight stopped with exit 2 because paper_statement_map.json was missing. Four inspected proof endpoints had no sorryAx; that does not supply missing proofs. Zero of six complete continuum propositions are formalized. Measurable matching, equilibrium, sorting, complete source Specs, and semantic audits remain open. End on the value of stating exactly what has been checked.

## Questions worth rehearsing

- Why is output n(z)s, not n(z)(s−z)? The latter omits worker successes.
- Is 2/7 the paper's threshold? No; it belongs to this finite branch.
- Does h=.5 establish h<h₀ for the finite population? No; the finite benchmark is checked directly.
- Does Lean prove that AI rent equals a? No; that substitution is conditional here.
- Why not drop unused h<1 and z≥0? They retain the economic domain; the algebra alone needs less.
- Why does a green fast check coexist with 0/6 coverage? Compilation checks available declarations, not missing source claims.
- Why is the new counterexample outside `lean/`? The assignment requires preserving the original generated folder exactly.

## Added explanations

**Slide 11.** For a fixed human–AI team, r=a reflects the compute owner's autonomous production opportunity; r=0 reflects abundant compute restricted to advising. Substituting in the same zero-profit equation isolates this opportunity-cost channel. Neither formula alone ranks all equilibrium wages, because humans may switch roles or partners. The original Lean run proves the algebraic substitutions conditionally.

**Slide 17.** A contains resource requirements for production activities, b contains human masses and compute supply, and q contains expected output. The dual vector p contains human wages and the AI rental. Feasible allocations and prices with equal objectives certify the finite optimum. Separate minimization and maximization of each wage over the optimal dual face check uniqueness. Explain these objects orally; the slide is deliberately compact.

**Slide 10.** Complete the remaining P6 clauses: occupational nonemptiness under adoption, efficiency within the technology, existence of a weak loser (strict under adoption), and strict total-output comparison at the same capability and compute. Slide 9 now displays the endpoint quantifiers explicitly.
