# Validation guide

| Record | What it establishes |
|---|---|
| [lean-scope.md](lean-scope.md) | User-selected discrete scope and explicit proof limits. |
| [lean-check.md](lean-check.md) | Original required fast check, full build, and unresolved semantic check. |
| [lean-copy-manifest.json](lean-copy-manifest.json) | Original generated-folder hashes and ignore status. |
| [computation.txt](computation.txt) | Numerical feasibility, optimality, wages, and accounting checks. |
| [computation-environment.json](computation-environment.json) | Numerical runtime information. |
| [presentation-check.md](presentation-check.md) | Compilation and visual review of the classic deck. |
| [presentation-requirements.md](presentation-requirements.md) | Assignment requirements mapped to slide numbers, including the missing photo. |
| [presentation-build.txt](presentation-build.txt) | Actual LaTeX build output. |
| [presentation-boundary-check.json](presentation-boundary-check.json) | Separate Lean counterexample command and exit status. |

A successful build checks existing declarations. It does not establish missing source propositions or full model formalization. Original run artifacts remain inside [../lean/docs/](../lean/docs/).
