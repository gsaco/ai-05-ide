# Own-run report — partial formalization

**0 of the 6 continuum propositions are proved.** This run proves algebraic support only. The generated source-facing interface remains empty, the named source claims remain pending, and no semantic acceptance or full-closeout receipt exists.

## Source and workflow

The governing source is arXiv:2312.05481v11, whose 35-page PDF is dated February 25, 2025. The arXiv submission metadata says February 24 UTC. The later journal publication was located at DOI 10.1086/737233, but the homework's explicit v11 pin governs this run. Source hashes and exact workflow commit are in `audit/source_provenance.json`; local PDF and extraction bytes are ignored.

The run used AppliedModelingLib commit `2db7d108cd3a2cb10148974bb2a77856e7d87428`, its current `skills/econcs-formalizer/SKILL.md` (the successor to the requested paper-formalization skill), `econcs-prover`, the stage references, and validated protocol `formalization-audit-protocol-2026-09-01`. The contributor facade generated the paper folder and registered its target. All generated scaffold and audit files are preserved, including incomplete ledgers/configuration.

An independent source-only reviewer read the whole pinned main paper and inventoried six propositions and the Competitive Equilibrium definition. Its report is `SOURCE_ONLY_INTAKE.md`. The 35-page main paper explicitly sends formal proofs to an Online Appendix that is not included in this artifact. No other version's proof was silently substituted.

## What Lean checked

`FirmAlgebra.lean` proves the exact algebraic implication

\[
 n(z)=\frac{1}{h(1-z)},\quad n(z)(a-w)-r=0
 \quad\Longrightarrow\quad w=a-h(1-z)r,
\]

for real variables with \(0<h<1\) and \(0\le z<1\). Specializing the rent to \(r=a\) gives \(w=a[1-h(1-z)]\); specializing to \(r=0\) gives \(w=a\). Positive \(a,h,1-z\) makes the opportunity-cost gap strictly positive. The source supplies these firm equations in Section 3.1 (printed pp. 10 and 12); Proposition 2 lists the autonomous wage formula on printed p. 19. **Lean has not proved that the firm is active or that equilibrium rents take the substituted values.** Zero profit and the rent value are explicit conditional inputs.

The algebraic helper quantifies over arbitrary real AI knowledge, wage and rent; unlike the source, it does not impose their nonnegative/economic bounds. This is a valid algebraic generalization, not a larger equilibrium theorem. The source-relevant helping-cost and worker-knowledge restrictions remain explicit.

The nonzero-denominator step matters: real division is total in Lean, so silently clearing a zero denominator would not justify the intended derivation. The proof first derives \(h\ne0\) and \(1-z\ne0\), then `field_simp` clears denominators and `nlinarith` verifies the polynomial implication. An initial attempt supplying only the product's nonzero proof left a factor denominator uncleared and failed; the final proof supplies both factors explicitly.

`DiscreteCalculations.lean` is a **supplementary three-type teaching example**, with \(h=1/2\), knowledge \((0,1/2,1)\), masses \((11/20,3/10,3/20)\), and a candidate autonomous branch \(0<a<1/3\). Lean checks:

- \(1/5<a/[2(1-a)]\) iff \(a>2/7\);
- two candidate zero-profit identities;
- the candidate free-co-pilot bottom wage is higher;
- the candidate middle wage is below \(3/5\) iff \(a>2/7\);
- the exact weighted candidate-wage identity \((24-25a)/[40(1-a)]\).

These theorems do **not** prove candidate equilibrium, market clearing, global firm optimality, aggregate output maximization, or the continuum Proposition 5 threshold. The atomless positive-density source population is replaced by three types in this supplementary calculation. The real-valued source algebra in `FirmAlgebra.lean` does not make this population replacement.

## Actual validation

The required command `python3 scripts/paper_contribution.py check IT25KnowledgeEconomy --fast` returned **exit 0**. Full stdout, stderr, environment overrides, timestamps and working directory are in `checks/paper_contribution_fast.*`. It built the paper interface and its support dependencies and checked whitespace. It is **not a source-fidelity or theorem-coverage certificate**; an empty source interface can pass this fast build.

The forced support-module build returned success with clean diagnostics. The complete paper-root build is recorded separately in `checks/paper_root_build.*`. Lean's axiom inspection of the central proved endpoints reported only the standard foundations `propext`, `Classical.choice`, `Quot.sound`, with no `sorryAx`.

Draft semantic preflight returned **exit 2**: `draft semantic preflight cannot read paper_statement_map.json`. Exact observed output is preserved in `checks/draft_semantic_preflight.txt`. No full semantic closeout was attempted or claimed after this refusal.

## Precise remaining blockers

1. The continuum competitive-equilibrium model has not been represented: measurable occupational partitions, all measurable-set resource constraints, feasible firm choices, no positive-profit deviations, clearing, and the pointwise wage/matching domains remain to be encoded.
2. Consequently the six complete proposition Specs and their source routes/claim atoms are not yet written. The source inventory is discovery evidence, not a completed machine source map. Neither P5's cutoff existence/iff/top-winner result nor any P6 equilibrium, adoption, output or neighborhood comparison is proved.
3. The source map, expanded-target preflight, independent semantic judgments, graph-backed proof correspondence, and final adversarial closeout have not been issued. Empty generated ledgers must not be read as accepted judgments.
4. The independently checked algebra does not remove any of these model-level obligations. The homework permits submission of this partial own-run folder; it does not convert a partial result into a completed formalization.

## Setup failures retained as run history

The first facade invocation failed because its child script could not import `scripts`; setting `PYTHONPATH=.` fixed the invocation without changing repository code. The next invocation timed out at its 120-second Lean scaffold check while downloading dependencies and atomically removed the unfinished scaffold. Dependencies were then initialized outside that bounded check; an interrupted Mathlib checkout was preserved locally and replaced by a shallow checkout at the exact pinned tag/commit. The same facade then succeeded. No audit gate, theorem premise, or source requirement was weakened to make setup pass.

No public push or visibility change was performed. The whole paper folder is to be copied as generated by this run, with its `.gitignore` respected. A paper-local `source.txt` ignore rule carries the parent repository's source-extraction privacy rule into that standalone copy.
