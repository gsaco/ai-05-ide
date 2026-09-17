import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# Supplementary discrete calculations (not source Propositions 5 or 6)

This module checks algebra for a three-type teaching example with h = 1/2,
knowledge (0, 1/2, 1), and masses (11/20, 3/10, 3/20).
It does not establish competitive equilibrium, market clearing, uniqueness,
or the paper's continuum threshold. Candidate wages are explicit functions;
their equilibrium interpretation must be established separately.
-/
namespace IT25KnowledgeEconomy.Discrete

noncomputable def bottomWage (a : ℝ) : ℝ := a / (2 * (1 - a))
noncomputable def middleWage (a : ℝ) : ℝ := (1 - 2 * a) / (1 - a)

/-- Strict gain over the pre-AI bottom wage 1/5 on the candidate branch. -/
def BottomGainSpec : Prop :=
  ∀ a : ℝ, 0 < a → a < 1 / 3 →
    (1 / 5 < bottomWage a ↔ 2 / 7 < a)

theorem bottomGain : BottomGainSpec := by
  intro a ha hupper
  have hden : 0 < 2 * (1 - a) := by linarith
  unfold bottomWage
  rw [lt_div_iff₀ hden]
  constructor <;> intro h <;> linarith

/-- Zero profit of a human bottom-worker / middle-solver team. -/
theorem humanTeam_zeroProfit (a : ℝ) (ha : a < 1) :
    2 * ((1 / 2 : ℝ) - bottomWage a) - middleWage a = 0 := by
  have hne : 1 - a ≠ 0 := by linarith
  unfold bottomWage middleWage
  field_simp [hne]
  ring

/-- Zero profit of AI workers paired with the middle type. -/
theorem middleAIWorkers_zeroProfit (a : ℝ) (ha : a < 1) :
    (1 / 2 - a) / ((1 / 2) * (1 - a)) - middleWage a = 0 := by
  have hne : 1 - a ≠ 0 := by linarith
  unfold middleWage
  field_simp [hne]
  ring

/-- A free co-pilot delivers a higher candidate bottom wage than a rented one. -/
theorem freeCopilot_exceeds_candidate (a : ℝ) (ha : 0 < a) (hu : a < 1 / 3) :
    bottomWage a < a := by
  have hden : 0 < 2 * (1 - a) := by linarith
  unfold bottomWage
  rw [div_lt_iff₀ hden]
  nlinarith

/-- The branch has a losing middle type compared with its baseline wage 3/5. -/
theorem middleLoss_iff (a : ℝ) (hu : a < 1) :
    (middleWage a < 3 / 5 ↔ 2 / 7 < a) := by
  have hden : 0 < 1 - a := by linarith
  unfold middleWage
  rw [div_lt_iff₀ hden]
  constructor <;> intro h <;> linarith

/-- Wage accounting only: no equilibrium or output-maximization claim. -/
theorem laborIncome_identity (a : ℝ) (ha : a < 1) :
    (11 / 20 : ℝ) * bottomWage a + (3 / 10 : ℝ) * middleWage a +
      (3 / 20 : ℝ) * 2 = (24 - 25 * a) / (40 * (1 - a)) := by
  have hne : 1 - a ≠ 0 := by linarith
  unfold bottomWage middleWage
  field_simp [hne]
  ring

end IT25KnowledgeEconomy.Discrete
