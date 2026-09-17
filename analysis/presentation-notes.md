# Rehearsal: 20 minutes, with 8.6 minutes on Lean

The redesigned talk has 20 main slides and three reference slides. The Lean walkthrough occupies slides 12–18. The mathematical scope of the original `lean/` folder is unchanged. A new, separate boundary check supports the discussion of domain restrictions.

| Slide | Topic | Time | Cumulative |
|---|---|---:|---:|
| 1 | Question, authors, repository and versions | 0:24 | 0:24 |
| 2 | Autonomy and capability | 0:42 | 1:06 |
| 3 | Worker–solver technology and agent's problem | 0:48 | 1:54 |
| 4 | Conditions on the paper's results | 0:36 | 2:30 |
| 5 | Proposition 5: capability threshold | 1:00 | 3:30 |
| 6 | Proposition 6: adoption and endpoint comparisons | 1:00 | 4:30 |
| 7 | Three-type baseline | 1:00 | 5:30 |
| 8 | Autonomous equilibrium branch | 1:00 | 6:30 |
| 9 | Derive the strict threshold | 1:00 | 7:30 |
| 10 | Read the numerical comparison | 0:48 | 8:18 |
| 11 | Output versus labor income | 0:48 | 9:06 |
| 12 | Translation versus proof | 0:54 | 10:00 |
| 13 | Paper equation → Spec → proof → interpretation | 1:36 | 11:36 |
| 14 | Explain each proof step | 1:18 | 12:54 |
| 15 | Rent specializations and economic meaning | 0:54 | 13:48 |
| 16 | The discrete iff proof | 1:18 | 15:06 |
| 17 | Failed attempt and missing-assumption counterexample | 1:30 | 16:36 |
| 18 | Actual checks and coverage boundary | 1:06 | 17:42 |
| 19 | Real hand derivation and personal verdict | 1:18 | 19:00 |
| 20 | Economic and verification conclusions | 1:00 | 20:00 |

## What to say, beyond the slide text

**1–4.** Name Ide and Talamàs and say 2025. Identify the course reading and the v11 Lean pin separately. AI autonomy means permitted roles, not intelligence. Capability is a fraction of problems solved. A worker's failure consumes solver time, so n(z) follows from a resource equation. The human chooses income-maximizing work and the firm chooses the organization. In the source, h<h₀ and a<1 are substantive restrictions on the top-winner claim. Abundant compute does not mean abundant production opportunities; both conditions matter separately.

**5–6.** Read “if and only if” and the strict inequality aloud. Since the autonomous threshold lies inside the pre-AI worker region, some basic autonomous AI benefits the bottom. For co-pilots, a≤w(0) means no adoption and unchanged wages. Do not turn a weak endpoint comparison into a strict gain. The top comparison is local and does not assert strictness at z=1. Refer questions about exact quantifiers and nonempty occupational sets to slide 21.

**7–9.** Subtract the first two zero-profit equations to get t−v=1 and substitute into the third. The positive market-clearing allocation validates which equations are active. In the autonomous branch, .55 low workers consume .275 middle solvers; the residual .025 middle humans supervise AI, which pins their wage. At 2/7 the bottom is indifferent. Both .2 and .3 lie in the displayed branch, unlike the separate .4 computational case. The finite model allows one type's mass to split across roles; it is not the source's continuous-knowledge economy.

**10–11.** Read across panels to change capability and within a panel to change autonomy. At .4, co-pilot advice raises the bottom wage from .2 to .4, while the top falls from 1.6 to 1.2. Autonomous AI instead yields (.25,.5,2). The output table separates human income from compute-owner income. Feasible-set inclusion proves weak output dominance; positive capability and idle compute make that argument strict. At a=0 the independent-production argument fails, requiring AI workers helped by humans.

**12.** A `Spec : Prop` is a proposition: a precise claim with domains and hypotheses. A theorem of that type is a proof of it. The source-to-Spec translation remains a separate audit question. Do not call the name `ZeroProfitWageSpec` evidence that the source was formalized correctly. The actual objects and conclusion must match.

**13.** Identify all five real scalars: helping cost h, worker knowledge z, AI capability a, worker wage w, and compute rent r. `span` is 1/[h(1−z)] and `topAutomatedProfit` is n(z)(a−w)−r. The source uses the equation for an active top-automated team. The Lean theorem assumes zero profit explicitly; it does not derive activity or existence. Its bounds are 0<h<1 and 0≤z<1. It permits arbitrary real a,w,r: a valid algebraic generalization, not a claim that those values all describe an economic team. The code is included directly from the preserved source file.

**14.** `intro` fixes arbitrary scalars and assumptions. `hh` names h>0 and `hz` names z<1. `ne_of_gt` turns positivity into nonzeroness, and `sub_pos.mpr hz` proves 1−z>0. `unfold` replaces both definitions; `field_simp` clears denominators using those facts. `nlinarith` finishes the polynomial implication. The underscores ignore h<1 and z≥0 inside the proof, although both remain in the statement. A stronger or broader algebra lemma can still preserve economically meaningful restrictions in its interface.

**15.** Substitute r=a to get a[1−h(1−z)] and r=0 to get a. With a>0 the wedge a h(1−z) is positive. This is a firm-level opportunity-cost comparison, not Proposition 6: equilibrium may change the occupation and match of the human under comparison. In the actual Lean files, `ring` checks factoring and `simpa` checks the zero-rent simplification.

**16.** `bottomWage` is a defined candidate formula, not an equilibrium object proved to exist. `hden` establishes a positive denominator, stronger than merely nonzero because an inequality direction is involved. `lt_div_iff₀` rewrites to an equivalent inequality. `constructor` splits the iff into necessity and sufficiency, and `linarith` proves both. The upper bound a<1/3 identifies the candidate equilibrium branch; the formal proof still does not establish market clearing or optimality.

**17.** The original run report records a failed factor-clearing attempt, repaired by supplying both nonzero factors. Distinguish that tactical failure from a false mathematical statement. The new presentation-only theorem verifies a counterexample to deleting the worker bound: at z=1, Lean's total real division gives span zero, allowing zero profit for a wage different from a. This tuple is outside the economic worker domain. It tests an unrestricted algebraic implication, not the paper. The new check is in `analysis/BoundaryCheck.lean`; it does not modify or upgrade the original formalization snapshot.

**18.** The required fast check returned 0, and the root build succeeded. Four inspected proof endpoints have only standard Lean foundations and no `sorryAx`. This says nothing about nonexistent proofs: all six continuum propositions remain unproved. Semantic preflight returned 2 because the source statement map was missing. Explain the required remaining work in order: continuum objects, matching and clearing, complete Specs, proofs, independent semantic audit. An empty paper-facing interface can pass a build.

**19.** This slide still requires your own real handwritten photograph. Work the derivation, explain what you checked personally, and state your own verdict. Save the photo as `hand/derivation.jpg` and rebuild. Neither the typeset exercise nor a generated image would meet the requirement.

**20.** End with the economic conclusion and the verification conclusion, not another paper summary. Autonomy and capability jointly matter. A formal proof is informative when its hypotheses and scope are visible.

## Questions worth rehearsing

- Why is output n(z)s, not n(z)(s−z)? The latter omits worker successes.
- Is 2/7 the paper's threshold? No; it belongs to this finite branch.
- Does h=.5 establish h<h₀ for the finite population? No; the finite benchmark is checked directly.
- Does Lean prove that AI rent equals a? No; that substitution is conditional here.
- Why not drop unused h<1 and z≥0? They retain the economic domain; the algebra alone needs less.
- Why does a green fast check coexist with 0/6 coverage? Compilation checks available declarations, not missing source claims.
- Why is the new counterexample outside `lean/`? The assignment requires preserving the original generated folder exactly.
