import IT25KnowledgeEconomy.FirmAlgebra
import Mathlib.Tactic.NormNum

/-!
Presentation-only boundary check, added after the frozen paper run.
This is not a source theorem and stays outside the preserved lean/ folder.
At z=1, the unrestricted scalar zero-profit implication is false. The tuple
is outside the worker domain, not an admissible economic AI team.
-/
namespace PresentationBoundary
open IT25KnowledgeEconomy.FirmAlgebra

theorem missing_worker_bound_counterexample :
    topAutomatedProfit (1 / 2) 1 (1 / 2) 1 0 = 0 ∧
      (1 : ℝ) ≠ (1 / 2) - (1 / 2) * (1 - 1) * 0 := by
  norm_num [topAutomatedProfit, span]

end PresentationBoundary
