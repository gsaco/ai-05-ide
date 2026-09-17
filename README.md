<p align="center">
  <img src="assets/banner.svg" alt="AI in the knowledge economy — autonomy, capability, and proof" width="100%">
</p>

<p align="center">
  <a href="https://arxiv.org/abs/2312.05481v11"><img src="assets/badge-source.svg" alt="Source: arXiv v11"></a>
  <a href="checks/lean-check.md"><img src="assets/badge-lean-check.svg" alt="Lean fast check: PASS, recorded run"></a>
  <a href="checks/lean-scope.md"><img src="assets/badge-coverage.svg" alt="Lean scope: discrete model"></a>
  <a href="presentation.pdf"><img src="assets/badge-deck.svg" alt="Presentation: 20 minutes"></a>
</p>

<p align="center">
  <a href="presentation.pdf"><strong>Read the slides</strong></a> ·
  <a href="analysis/derivation.md">Follow the derivation</a> ·
  <a href="lean/DiscreteCalculations.lean">Inspect the discrete proof</a> ·
  <a href="lean/docs/RUN_REPORT.md">See the honest status</a>
</p>

**Ide & Talamàs (2025), _Artificial Intelligence in the Knowledge Economy_.** Reading: course PDF, May 20, 2025, 39 pages. Lean pin: arXiv v11, February 25, 2025, 35 pages.

### The question and the agent’s problem

Who benefits when AI enters an economy organized around knowledge? Workers solve familiar problems and ask specialists for help. Specialists know more but have limited time. Humans choose the best-paying role; firms choose profitable teams. Competition and resource availability determine wages and compute rents. **Capability** determines which problems AI solves; **autonomy** determines whether it can produce independently or only advise humans.

### Main results—and their conditions

**Proposition 5:** with autonomous AI, some people at the bottom gain **if and only if capability exceeds a threshold inside the pre-AI worker range**. Some people at the top gain at every permitted capability. A person with exactly AI’s knowledge loses. Autonomy alone does not explain these results.

**Proposition 6:** co-pilot AI is adopted only when capability exceeds the least knowledgeable human’s pre-AI wage, measured in output. Otherwise wages and occupations stay unchanged. Near the bottom, co-pilots pay at least as much as autonomous AI and no AI; both comparisons become strict with adoption. Near the top, autonomous AI pays at least as much, strictly except at maximum knowledge. Some human weakly loses relative to no AI, strictly with adoption. At the same capability and compute supply, **autonomous AI produces strictly more total output**.

These claims require positive, sufficiently low helping costs so everyone initially works in teams; imperfect AI; abundant production opportunities; and compute supply exceeding potential human–AI team demand. Humans have equal working time and observable knowledge with a positive continuous density. Problem difficulty is independent and uniform. Agents are risk neutral, firms competitive with full information and no fixed costs, and teams have at most two layers. Endpoint comparisons concern neighborhoods, not every worker. Co-pilot equilibrium is unique, efficient, and maximizes labor income within its restricted technology; with adoption, AI-assisted workers, human-assisted workers, and human solvers coexist, while independent humans may be absent.

### Our derivation and Lean results

The [genuine handwritten pages](hand/README.md) solve a three-type example. They show how capability changes bottom gains while autonomy stays fixed. We checked wages, resource clearing, entry incentives, and output numerically. The second page’s output conclusion needs an additional allocation calculation, supplied in the hand guide and slides.

**Lean proves the finite bottom-gain threshold, two zero-profit identities, a middle-wage loss threshold, a free-advice comparison, and a labor-income identity.** Supporting proofs derive a wage formula from zero profit with explicit denominator restrictions. The recorded build and required fast check passed. These are conditional algebraic results: neither full discrete equilibrium nor the six complete continuum propositions is proved. Semantic verification stopped because the source statement map was missing.

The original generated `lean/` folder is preserved unchanged. The [20-minute deck](presentation.pdf) includes six Lean slides explaining mathematics, code, proof steps, and limits. [Raw prompts](prompts.md), [analysis](analysis/README.md), and [checks](checks/README.md) preserve the evidence. Badges describe recorded results. The [submission audit](checks/submission-audit.md) records the requirement review and outstanding submission steps.
