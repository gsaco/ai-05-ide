import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# Algebraic proof support for Ide and Talamàs (2025), arXiv v11

The source's two-layer top-automated profit is n(z)(a - w) - r,
with n(z) = 1 / (h(1-z)). This module checks what zero profit implies
about one worker's wage. It does not prove an equilibrium exists, that
this firm is active, or that the compute rent equals a.
Source: section 3.1, printed pp. 10 and 12; Proposition 2, printed p. 19.
-/
namespace IT25KnowledgeEconomy.FirmAlgebra

noncomputable def span (h z : ℝ) : ℝ := 1 / (h * (1 - z))
noncomputable def topAutomatedProfit (h z a w r : ℝ) : ℝ :=
  span h z * (a - w) - r

/-- Transparent contract for the zero-profit implication only, not P2/P5/P6. -/
def ZeroProfitWageSpec : Prop :=
  ∀ h z a w r : ℝ, 0 < h → h < 1 → 0 ≤ z → z < 1 →
    topAutomatedProfit h z a w r = 0 → w = a - h * (1 - z) * r

theorem zeroProfitWage : ZeroProfitWageSpec := by
  intro h z a w r hh _ _ hz hprofit
  have hhne : h ≠ 0 := ne_of_gt hh
  have hzne : 1 - z ≠ 0 := ne_of_gt (sub_pos.mpr hz)
  unfold topAutomatedProfit span at hprofit
  field_simp [hhne, hzne] at hprofit
  nlinarith

/-- Under the autonomous rent condition r=a, the source wage formula follows. -/
theorem autonomous_wage (h z a w : ℝ) (hh : 0 < h) (hh1 : h < 1)
    (hz0 : 0 ≤ z) (hz1 : z < 1)
    (hp : topAutomatedProfit h z a w a = 0) :
    w = a * (1 - h * (1 - z)) := by
  have hw := zeroProfitWage h z a w a hh hh1 hz0 hz1 hp
  calc
    w = a - h * (1 - z) * a := hw
    _ = a * (1 - h * (1 - z)) := by ring

/-- Under a zero compute rent, zero profit instead yields the full AI productivity. -/
theorem nonautonomous_wage (h z a w : ℝ) (hh : 0 < h) (hh1 : h < 1)
    (hz0 : 0 ≤ z) (hz1 : z < 1)
    (hp : topAutomatedProfit h z a w 0 = 0) : w = a := by
  simpa using zeroProfitWage h z a w 0 hh hh1 hz0 hz1 hp

/-- Holding knowledge and helping cost fixed, positive rent reduces this wage. -/
theorem opportunity_cost_gap (h z a : ℝ) (hh : 0 < h)
    (hz : z < 1) (ha : 0 < a) : a * (1 - h * (1 - z)) < a := by
  have hcost : 0 < a * (h * (1 - z)) :=
    mul_pos ha (mul_pos hh (sub_pos.mpr hz))
  nlinarith

end IT25KnowledgeEconomy.FirmAlgebra
