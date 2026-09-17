# Selected Lean scope: the discrete teaching model

The user explicitly chose to retain the discrete Lean component and stop the full-continuum extension. This is a scope decision, not an upgrade of the proof status.

## What is checked

The preserved `lean/DiscreteCalculations.lean` proves the candidate bottom-wage threshold, two zero-profit identities, a comparison with free co-pilot advice, the middle-wage loss threshold, and a labor-income identity. Its main contract is:

$$0<a<1/3 \quad\Longrightarrow\quad \left(1/5<a/[2(1-a)]\iff 2/7<a\right).$$

`lean/FirmAlgebra.lean` supplies related real-scalar wage algebra. The presentation explains these assumptions and proof steps.

## What is not claimed

The Lean code does not prove existence, market clearing, or uniqueness of the full discrete equilibrium. Those properties are supported separately by the hand-solvable derivation and numerical checks. None of the six complete continuum propositions is Lean-proved. The recorded semantic-preflight failure remains disclosed.

## Preservation and organization

- `lean/` remains byte-for-byte identical to the original copied agent-run folder; no generated files were removed, renamed, or rewritten.
- New continuum experiments remain outside this weekly repository in the AppliedModelingLib clone. They are not imported or submitted as verified results.
- The separate `analysis/BoundaryCheck.lean` remains a presentation-only check outside the preserved snapshot.
- The existing check results describe the original run. No new complete-formalization result or successful semantic closeout is asserted.
- Two genuine handwritten photographs are included in hand/ and discussed on slides 18–19.
