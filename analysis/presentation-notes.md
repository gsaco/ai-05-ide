# 20-minute presentation rehearsal

These are preparation notes, not a claim that the student has already carried out the hand check. Read the derivation and actual Lean report, work the algebra yourself, and replace the pending photograph before presenting.

| Slide | Topic | Minutes | Cumulative |
|---|---|---:|---:|
| 1 | Title, repository, versions | 0.50 | 0.50 |
| 2 | Autonomy and capability | 0.75 | 1.25 |
| 3 | Agent and firm problem | 1.00 | 2.25 |
| 4 | Conditions | 1.00 | 3.25 |
| 5 | Proposition 5 | 1.50 | 4.75 |
| 6 | Proposition 6 | 1.50 | 6.25 |
| 7 | Economic mechanism | 1.00 | 7.25 |
| 8 | Three-type benchmark | 1.50 | 8.75 |
| 9 | Autonomous equilibrium branch | 1.50 | 10.25 |
| 10 | Capability threshold | 1.50 | 11.75 |
| 11 | Non-autonomous calculation | 1.00 | 12.75 |
| 12 | Computational verification | 1.00 | 13.75 |
| 13 | Output and factor income | 1.00 | 14.75 |
| 14 | Mathematical claim → Lean → proof → interpretation | 1.50 | 16.25 |
| 15 | Translation boundary and check result | 1.50 | 17.75 |
| 16 | Genuine hand derivation and own verdict | 1.25 | 19.00 |
| 17 | What was learned | 1.00 | 20.00 |

Appendix slides are for questions; do not read them during the timed talk.

## What to explain aloud

**1–2.** Name the authors as Ide and Talamàs, date the paper 2025, and explicitly distinguish the course reading from the Lean source pin. Define autonomy as permitted roles, not model intelligence. Capability is the fraction of uniformly distributed problems the AI can solve. The object of interest is equilibrium income, not merely task completion in a laboratory.

**3.** Start from the time constraint, rather than memorizing the team-size formula. A worker asks for help only when its own knowledge fails. The solver spends time on each request even when unable to solve it. Explain the human's occupational choice and the firm's maximization, with zero-profit conditions as the wage equations.

**4.** Mention all conditions on screen; emphasize h<h₀ and a<1 as genuine restrictions on the top-winner result. Abundant compute is distinct from abundant production opportunities. The former pins rentals and the latter prevents the paper's technological-unemployment extension from becoming the baseline.

**5.** Define B and T, including their comparison to the no-AI wage. Read “if and only if” and the strict capability inequality aloud. The threshold lies inside the pre-AI worker set: equating basic AI with bottom losses throughout that set is incorrect. This is the strongest source-based answer to the week's trap.

**6.** Distinguish weak and strict claims. At a≤w(0) the non-autonomous technology is unused; it cannot strictly improve wages while leaving the economy unchanged. Explain that its threshold w(0) is not Proposition 5's threshold ā. Near the top is a neighborhood claim; strictness is not asserted at z=1. Efficiency and labor-income maximization are within the feasible non-autonomous technology, not a claim that it has the most output among both technologies.

**7.** Read the bottom wage equation as output minus the per-worker solver bill. Both the quality of the match and the wage paid to the solver change. At the top, AI workers spread scarce human expertise over more opportunities. A lower rental for a co-pilot follows from its idle outside option; it is not a cost assumption imposed by hand.

**8.** Solve the wage system at the board in miniature: subtract the first equation from the second to obtain t−v=1, then substitute into the third. Give the resource-clearing allocation so that the audience sees why active zero-profit equations constitute an equilibrium rather than guessed wages. A type is a mass of identical agents, which can split across roles. There is no continuum of knowledge in this example.

**9–10.** State the branch before its formulas. Human-middle capacity is .30 and serving the .55 low workers uses .275. Residual middle capacity can supervise AI, pinning v. Spare compute makes r=a consistent. When multiplying the wage inequality, identify the positive denominator. At the threshold the lowest human is indifferent, not a strict winner. Compare a=.2 and a=.3, both inside the derivation's branch; a=.4 belongs to a different branch checked separately.

**11.** Keep a=.4 and μ=2 fixed across regimes. AI advice pins the low wage at .4, while active human teams pin t and v. Check how the .15 high human mass divides its time. This example shows bottom and middle gains with top losses, but does not claim that every possible non-autonomous equilibrium harms the top relative to no AI.

**12.** Explain one primal and one dual constraint: a human team uses one worker and h(1−z) solvers; its payment must cover its output to prevent entry. The solver verifies both resource feasibility and prices, plus that every possible optimal wage vector gives the same wages in these examples. Interpolated lines on the chart are only guides between three points.

**13.** Read the income columns separately. Autonomous AI has lower labor income than non-autonomous AI in this comparison, but higher total output because compute is productive and receives rent. Feasible-set inclusion proves weak output dominance; strictly positive idle compute and a>0 strengthen it to strict dominance. At a=0 that argument is invalid and AI's use as workers must be analyzed separately.

**14–15.** Read the exact theorem in the generated Lean folder before rehearsal. Identify the scalar domain and every hypothesis, explain the proof's denominator-positivity step, and distinguish algebraic verification from the missing equilibrium-to-formula link. Report the actual focused build and required paper-check results separately. A failed audit is not a proof that the displayed algebra is false, and a successful algebra build is not a proof of the full paper.

**16.** Show your actual handwritten page. Say what you personally checked and why you accepted or rejected the AI's statement. The prepared exercise is to challenge the autonomy-only gloss and check the strict capability threshold. Do not invent a prior LLM mistake or a personal experience that did not happen.

**17.** Finish with one sentence each about the bottom, top, output, and verification boundary. Do not recite the abstract.

## Questions to rehearse

- **Why is team output n(z)s rather than n(z)(s−z)?** The latter omits problems workers solve on their own. Success is x≤s, so its probability is s.
- **Why does the highest human earn 2 in the autonomous examples?** With z=1, (1−a)/[h(1−a)]=1/h=2. This cancellation requires a<1 and an active AI-worker role.
- **Does h=.5 establish h<h₀ for the discrete economy?** No. The continuum h₀ belongs to its own distribution. The finite benchmark's positive all-team allocation is directly checked; it is not an application of the continuum proposition.
- **Is 2/7 the paper's threshold?** No. It is the threshold on the explicitly derived finite branch for these masses and h. The source threshold depends on its continuum economy.
- **Is no-AI output compared with identical compute?** The no-AI benchmark has no productive AI technology; post-AI autonomy comparisons both use μ=2. The program sets baseline productive compute to zero without giving humans additional resources.
- **Is total output a complete welfare criterion?** The model is quasilinear in the numeraire and considers output and factor incomes. Distributional preferences, ownership concentration, transition costs, and taxes are outside this exercise.
- **What has Lean not established?** Read the final partial-status report. In particular, do not claim continuum equilibrium existence, uniqueness, sorting, or Propositions 5–6 unless the actual proof/audit artifacts establish them.
