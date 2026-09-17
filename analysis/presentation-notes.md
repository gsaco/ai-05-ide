# Rehearsal: classic Beamer, 20 minutes

22 slides in English: 16 on the paper and finite exercise, then exactly 6 on Lean. No notes or references are printed in the slide footers. These speaking notes remain separate from the deck.

| Slide | Topic | Time | Cumulative |
|---|---|---:|---:|
| 1 | Title | 0:15 | 0:15 |
| 2 | Question and source | 0:30 | 0:45 |
| 3 | Autonomy and capability are different dimensions | 0:40 | 1:25 |
| 4 | The agent's problem: organize knowledge and time | 1:00 | 2:25 |
| 5 | Conditions: people, problems, and firms | 0:35 | 3:00 |
| 6 | Conditions: scarce time and abundant compute | 0:45 | 3:45 |
| 7 | Proposition 5: capability determines bottom gains | 1:05 | 4:50 |
| 8 | Proposition 6: adoption still requires capability | 0:55 | 5:45 |
| 9 | Proposition 6: bottom, top, and total output | 0:55 | 6:40 |
| 10 | A three-type economy we can solve directly | 1:05 | 7:45 |
| 11 | Autonomous AI: solve one equilibrium branch | 1:10 | 8:55 |
| 12 | Same autonomy, different bottom outcomes | 1:00 | 9:55 |
| 13 | Numerical results separate the two dimensions | 0:40 | 10:35 |
| 14 | More output does not imply more labor income | 0:50 | 11:25 |
| 15 | The claim I would not accept without checking | 0:50 | 12:15 |
| 16 | What the paper and the example teach us | 0:25 | 12:40 |
| 17 | Lean 1/6: from economics to a precise statement | 0:50 | 13:30 |
| 18 | Lean 2/6: the bottom-gain threshold | 1:30 | 15:00 |
| 19 | Lean 3/6: why the inequality proof works | 1:15 | 16:15 |
| 20 | Lean 4/6: zero profit implies a wage identity | 1:30 | 17:45 |
| 21 | Lean 5/6: a missing assumption changes the claim | 1:10 | 18:55 |
| 22 | Lean 6/6: what passed and what remains open | 1:05 | 20:00 |

## Oral detail and source references

**Slides 2–6.** Read Ide and Talamàs (2025), course PDF May 20, 39 pages; the Lean run pins arXiv v11, February 25, 35 pages. Explain that knowledge determines which problems can be solved; autonomy determines permitted production roles. Helping consumes time even when unsuccessful. The population has continuous positive density in the paper. The finite example changes that domain. The assumptions h<h₀, a<1, opportunity abundance, and compute abundance are substantive.

**Slides 7–9.** Proposition 5 is v11 p.24 / course p.25; Proposition 6 is v11 p.27 / course p.28. Define B={z≤a:wᴬ(z)>w(z)} and T={z≥a:wᴬ(z)>w(z)} within [0,1]. The autonomous threshold is inside the pre-AI worker set. State the iff and strict inequality aloud. Under co-pilot adoption, AI-assisted workers, human-assisted workers, and human solvers are nonempty; independent humans may be absent. AI-assisted workers occupy the lowest positions. There exists ε>0 such that the bottom comparison holds for every z∈[0,ε); a possibly different ε gives the top comparison on (1−ε,1]. The top comparison is strict except at z=1. There is some z∈(0,1] with wᴺ(z)≤w(z), strict under adoption. Efficiency and labor-income maximization are within the co-pilot technology, not across technologies.

**Slides 10–12.** Subtract the first two baseline zero-profit equations to get t−v=1; the third then gives v=.6, t=1.6, u=.2. Baseline worker masses for L→M, L→H, M→H are .32,.23,.14. In the autonomous branch .55 low workers use .275 middle solvers; the remaining .025 middle humans supervise AI and pin their wage. AI-worker compute demand 7/[20(1−a)]<2 leaves spare compute. All no-entry inequalities are checked in analysis/derivation.md. At a=2/7 there is equality, not a strict gain. This is not the numerical value of the continuum threshold.

**Slides 13–14.** The lines join only three discrete types. Compare across panels to isolate capability and within panels to isolate autonomy. At a=.4, co-pilot wages are (.4,.7,1.2), autonomous wages (.25,.5,2). Output includes compute-owner income. Autonomous production contains the co-pilot feasible set. If a>0 and compute is idle, independent AI adds strictly positive output; a=0 needs the separate human-assisted AI-worker mechanism. Numerical checks certify the finite examples, not the continuum theorem.

**Slides 15–16.** Do the derivation yourself and add the real photo as hand/derivation.jpg before presenting. The typeset placeholder is not the required handwritten evidence. Explain the verdict in your own words: capability changes bottom gains even when autonomy is held fixed.

**Slide 17.** A Spec is a proposition. Lean checks a term of that type. The source-to-Spec translation is a separate audit, and a familiar theorem name is not evidence of source fidelity.

**Slides 18–19.** The displayed statement and proof are directly included from lean/DiscreteCalculations.lean. Real a is quantified, with 0<a<1/3. bottomWage is the candidate formula a/[2(1−a)], not a proven equilibrium object. hden proves positivity, which preserves the direction when clearing the fraction. constructor splits the equivalence; linarith checks each linear implication. The proof builds, but Proposition 5 remains unproved.

**Slide 20.** FirmAlgebra.zeroProfitWage quantifies real h,z,a,w,r with 0<h<1 and 0≤z<1, and explicitly assumes zero profit. The displayed proof obtains both nonzero factors, unfolds span and profit, clears denominators, and finishes with nlinarith. Bounds h<1 and z≥0 remain in the statement although unused by the algebra. Arbitrary real a,w,r are an algebraic generalization. Active roles, market clearing, and equilibrium rent values are not established. The source equation is on v11 pp.10/12. The original run first failed to clear a remaining factor denominator when given only a product's nonzero proof; supplying both factors repaired that tactic step.

**Slide 21.** Distinguish a failed tactic from an invalid mathematical generalization. The counterexample at z=1 uses Lean's total real division. It is outside the worker domain and refutes only the unrestricted algebraic claim. analysis/BoundaryCheck.lean compiled with exit 0; its result is recorded separately in checks/presentation-boundary-check.json. The original lean/ snapshot is unchanged.

**Slide 22.** The required fast check passed, as did the full root build. The semantic preflight stopped with exit 2 because paper_statement_map.json was missing. Four inspected proof endpoints had no sorryAx; that does not supply missing proofs. Zero of six complete continuum propositions are formalized. Measurable matching, equilibrium, sorting, complete source Specs, and semantic audits remain open. End on the value of stating exactly what has been checked.

## Questions worth rehearsing

- Why is output n(z)s, not n(z)(s−z)? The latter omits worker successes.
- Is 2/7 the paper's threshold? No; it belongs to this finite branch.
- Does h=.5 establish h<h₀ for the finite population? No; the finite benchmark is checked directly.
- Does Lean prove that AI rent equals a? No; that substitution is conditional here.
- Why not drop unused h<1 and z≥0? They retain the economic domain; the algebra alone needs less.
- Why does a green fast check coexist with 0/6 coverage? Compilation checks available declarations, not missing source claims.
- Why is the new counterexample outside `lean/`? The assignment requires preserving the original generated folder exactly.
