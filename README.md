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

**Based on Enrique Ide and Eduard Talamàs (2025), _Artificial Intelligence in the Knowledge Economy_.** Course reading: May 20, 2025, 39 pages. Lean source: arXiv v11, February 25, 2025, 35 pages. [Source details](paper/README.md).

> **The key lesson:** giving AI more independence and making it more capable are different changes. Both affect who gains, who loses, and how much the economy produces.

### What is the economic problem?

Workers handle routine problems and ask more knowledgeable specialists for help when they get stuck. Specialists have valuable knowledge but limited time. Firms choose who should work, who should advise, and whether to use AI. Humans seek the highest income; firms seek the most profitable teams. Competition and the availability of people and compute determine wages and AI rental prices.

AI changes this organization in two ways. **Capability** determines which problems it can solve. **Autonomy** determines whether it can perform production work itself or only advise a human.

### Who gains? The conditions matter

| Result | Intuition and condition |
|:--|:--|
| **Bottom earners — Proposition 5** | With autonomous AI, some less knowledgeable humans gain **if and only if AI capability exceeds a threshold**. That threshold lies within the range of pre-AI workers, so even some relatively basic AI can benefit the bottom. Autonomy alone does not determine the outcome. |
| **Top earners — Proposition 5** | Some highly knowledgeable humans gain at every permitted AI capability: they can supervise AI workers and apply their expertise more widely. This requires the assumptions below, including imperfect AI and sufficiently low helping costs. A human with exactly AI's knowledge loses. |
| **Co-pilot adoption — Proposition 6** | Advice is used only when AI's problem-solving capability exceeds the least knowledgeable human's pre-AI wage, measured in units of output. Otherwise, wages and occupations stay unchanged. With adoption, the bottom gains strictly, but some other humans lose. This threshold differs from the autonomous-AI threshold. |
| **Autonomy versus co-pilots — Proposition 6** | Near the bottom, co-pilots deliver wages at least as high as either autonomous AI or no AI; adoption makes both comparisons strict. Near the top, autonomous AI pays at least as much, strictly so except at the highest knowledge level. **Autonomous AI produces more total output.** |

**These results describe a specific economy.** Everyone has equal working time; knowledge is observable and continuously distributed with a positive, continuous density. Problems have independent, uniformly distributed difficulty. People are risk neutral; firms have full information, no fixed costs, and at most two layers. Output is the unit of account. Helping costs are positive and low enough that everyone works in teams before AI. AI cannot solve every problem. Production opportunities are plentiful, and compute exceeds what human–AI teams can use. The autonomy comparison holds capability and compute supply fixed.

The co-pilot equilibrium is unique and efficient, and maximizes labor income **within that restricted technology**. With adoption, AI-assisted workers, human-assisted workers, and human solvers all remain present; independent producers need not. The endpoint wage comparisons are local, not rankings of every worker.

### What we checked ourselves

A **three-type example** replaces the paper's continuous population with low-, middle-, and high-knowledge humans. Solving the team equations shows how greater capability can turn bottom losses into gains while autonomy stays fixed. Numerical checks verify resource use, profitable-entry conditions, wage uniqueness, and income accounting for the selected examples. More output can coexist with less total human wage income because compute owners also receive income.

[Read the derivation](analysis/derivation.md) · [Inspect the numerical checks](checks/computation.txt)

### What Lean verifies

Lean checks whether a mathematical conclusion follows from its stated assumptions. Our selected scope is **the discrete example's algebra and supporting wage calculations**.

| Checked result | What the proof establishes |
|:--|:--|
| **Bottom-gain threshold** | Within the analyzed range, the proposed bottom wage improves on its pre-AI level exactly when capability crosses the derived threshold. Equality is not a strict gain. |
| **Team wages and profits** | The proposed wages exhaust the output of two specified team configurations, leaving zero profit. |
| **Distribution and accounting** | The code checks a middle-wage loss threshold, a comparison with free co-pilot advice, and the formula for total human wage income. |
| **Supporting wage identity** | Given zero profit and explicit restrictions on helping costs and worker knowledge, the wage follows from productivity and the cost of AI advice. |

**The recorded Lean build and required fast check passed.** This verifies the implemented proofs; it does not prove that the proposed teams form an equilibrium. The full discrete equilibrium and the paper's six complete continuum propositions are **not Lean-proved**. The separate source-verification check stopped because the source statement map was missing. Those limits remain visible in the original run records.

[Discrete proofs](lean/DiscreteCalculations.lean) · [Check results](checks/lean-check.md) · [Scope and limitations](checks/lean-scope.md)

### Explore the repository

The [presentation](presentation.pdf) has six dedicated Lean slides; the [rehearsal guide](analysis/presentation-notes.md) allocates 20 minutes. The [analysis guide](analysis/README.md) and [validation guide](checks/README.md) locate the supporting materials. [Raw prompts](prompts.md) preserve the exchange.

The complete generated `lean/` folder remains unchanged, including its audits and partial status. Badges describe the recorded run, not live automated checks. **The genuine handwritten derivation photograph is still pending**; see [hand/](hand/README.md).
