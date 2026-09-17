# Genuine handwritten derivations

The two original photographs supplied by the student are preserved as `IMG_5928.HEIC` and `IMG_5929.HEIC`. The matching `derivation-1.jpg` and `derivation-2.jpg` files are format conversions with camera orientation normalized for portable viewing; no handwriting was generated or altered. Slides 18–19 display selected regions, with readable typeset equations and the verdict alongside them.

- **Page 1:** three human types, span of control, zero-profit equations, baseline wages, autonomous wages, and the bottom-gain threshold.
- **Page 2:** non-autonomous wages at capability three tenths and the comparison across regimes.

## Verification and qualifications

The handwritten wages and strict bottom-gain threshold are correct for the branch in `analysis/derivation.md`. Helping cost is one half and compute supply is two. The handwritten span expression means one divided by the entire product h(1−z). The baseline output line uses worker quantities x, y, q; their definitions and resource equations appear below. The bottom threshold applies only for capability strictly between zero and one third; at two sevenths there is equality.

The final “Hence” on page 2 is incomplete reasoning: wage rankings alone do not establish output rankings. The output conclusion is correct, with the missing calculation supplied here. The photographs are retained unchanged, including that gap.

### Resource and output calculation

Before AI, let x, y, q denote low workers helped by middle humans, low workers helped by high humans, and middle workers helped by high humans. Resource clearing gives:

$$x+y=11/20,\qquad x/2+q=3/10,\qquad y/2+q/4=3/20.$$

Thus x=8/25, y=23/100 and q=7/50, and output is x/2+y+q=53/100.

At AI capability 3/10, autonomous AI uses all 11/20 low humans as workers with middle solvers, 1/14 AI workers with the remaining middle solvers, and 3/7 AI workers with high solvers. The remaining 3/2 units of compute produce independently:

$$Y_A=\frac{11}{40}+\frac1{28}+\frac37+\frac32\frac3{10}=\frac{333}{280}.$$

With non-autonomous AI, 3/20 low workers and 3/10 middle workers use high solvers; 2/5 low workers use AI advice. They require 1/5 compute units, leaving abundant idle compute:

$$Y_N=\frac3{20}+\frac3{10}+\frac25\frac3{10}=\frac{57}{100}.$$

Therefore Y_A>Y_N>Y_0. The output comparison includes compute-owner income. A separate numerical primal–dual check at this exact capability is recorded in `checks/hand-check.json`.

These calculations illustrate the economic mechanisms of Propositions 5 and 6 in a finite economy. They do not establish the continuum propositions, and the finite threshold is not the paper's continuum threshold.

Reproduce the numerical check with `python3 analysis/verify_hand.py` using the repository requirements.
