"""Three-type knowledge economy: primal allocations and dual competitive prices.

Activities are normalized per worker, not per solver. No continuum discretization
or numerical differentiation is used. Run: python3 analysis/discrete_model.py
"""
from pathlib import Path
import csv
import json
import numpy as np
from scipy.optimize import linprog

ROOT = Path(__file__).resolve().parents[1]
Z = np.array([0., .5, 1.])
MASS = np.array([.55, .30, .15])
H, MU = .5, 2.

def economy(a, regime):
    names, columns, outputs = [], [], []
    def add(name, resources, output):
        names.append(name); columns.append(resources); outputs.append(output)
    for i, z in enumerate(Z):
        col = np.zeros(4); col[i] = 1
        add(f"independent_{i}", col, z)
    for i, z in enumerate(Z):
        for j, s in enumerate(Z):
            if z < s:
                col = np.zeros(4); col[i] = 1; col[j] = H*(1-z)
                add(f"human_{i}_to_{j}", col, s)
    if regime != "none":
        for i, z in enumerate(Z):
            if z < a:
                col = np.zeros(4); col[i] = 1; col[3] = H*(1-z)
                add(f"AI_solver_for_{i}", col, a)
            if regime == "autonomous" and a < z:
                col = np.zeros(4); col[i] = H*(1-a); col[3] = 1
                add(f"AI_worker_for_{i}", col, z)
        if regime == "autonomous":
            add("AI_independent", np.array([0.,0.,0.,1.]), a)
    A = np.array(columns).T
    q = np.array(outputs)
    b = np.append(MASS, MU if regime != "none" else 0.)
    primal = linprog(-q, A_ub=A, b_ub=b, bounds=(0,None), method="highs")
    assert primal.success, primal.message
    prices = -primal.ineqlin.marginals
    dual = linprog(b, A_ub=-A.T, b_ub=-q, bounds=(0,None), method="highs")
    assert dual.success, dual.message
    output = -primal.fun
    assert abs(output-dual.fun) < 1e-8
    assert np.min(A.T @ prices-q) >= -1e-8
    assert np.max(A @ primal.x-b) < 1e-8
    assert np.max(np.abs(primal.x*(A.T@prices-q))) < 1e-8
    # Compute the entire optimal dual wage interval, avoiding arbitrary LP prices.
    wage_ranges = []
    for i in range(3):
        direction = np.eye(4)[i]
        common = dict(A_ub=-A.T,b_ub=-q,A_eq=b[None,:],b_eq=[output],bounds=(0,None),method="highs")
        lo = linprog(direction, **common)
        hi = linprog(-direction, **common)
        assert lo.success and hi.success
        wage_ranges.append([lo.fun, -hi.fun])
    return dict(regime=regime, capability=a, wages=prices[:3].tolist(),
                wage_ranges=wage_ranges, rent=float(prices[3]), output=output,
                labor_income=float(MASS@prices[:3]),
                capital_income=float(b[3]*prices[3]),
                compute_used=float((A@primal.x)[3]),
                activities={n:float(x) for n,x in zip(names,primal.x) if x>1e-8})

def main():
    results=[economy(0,"none")]
    for a in [.2,.4,.8]:
        for regime in ["autonomous","nonautonomous"]:
            results.append(economy(a,regime))
    expected=[[.2,.6,1.6],[.125,.75,2],[.2,.6,1.6],
              [.25,.5,2],[.4,.7,1.2],[.4,.6,2],[.8,.8,1]]
    for r,w in zip(results,expected):
        assert np.allclose(r["wages"],w), (r,w)
        assert all(abs(lo-hi)<1e-7 for lo,hi in r["wage_ranges"]), r
        assert abs(r["output"]-r["labor_income"]-r["capital_income"])<1e-8
    # Exact hand-derived bottom threshold applies on this branch only.
    for a in [.05,.2,2/7,.3,.31]:
        r=economy(a,"autonomous")
        assert abs(r["wages"][0]-a/(2*(1-a)))<1e-8
    endpoint=economy(0,"autonomous")
    assert np.allclose(endpoint["wages"],[0,1,2])
    assert abs(endpoint["output"]-.6)<1e-8
    (ROOT/"analysis/results.json").write_text(json.dumps(results,indent=2)+"\n")
    with (ROOT/"analysis/results.csv").open("w") as f:
        writer=csv.writer(f, lineterminator="\n")
        writer.writerow(["regime","capability","w_low","w_middle","w_high","rent","labor_income","capital_income","output"])
        for r in results:
            writer.writerow([r["regime"],r["capability"],*r["wages"],r["rent"],r["labor_income"],r["capital_income"],r["output"]])
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size":12,"axes.spines.top":False,"axes.spines.right":False})
    fig,axes=plt.subplots(1,3,figsize=(12,3.6),sharey=True)
    for k,(ax,a) in enumerate(zip(axes,[.2,.4,.8])):
        for r,label,color,marker in [(results[0],"No AI","#7b8490","o"),
           (results[1+2*k],"Autonomous","#006d77","s"),
           (results[2+2*k],"Co-pilot only","#bc5b24","^")]:
            ax.plot(Z,r["wages"],color=color,marker=marker,label=label,lw=2)
        ax.set_title(f"AI capability a = {a}")
        ax.set_xticks(Z,["Low (0)","Middle (½)","High (1)"])
        ax.set_ylim(-.03,2.12)
        ax.grid(axis="y",alpha=.15)
    axes[0].set_ylabel("Competitive wage")
    axes[1].legend(loc="upper center",bbox_to_anchor=(.5,-.15),ncol=3,frameon=False)
    fig.tight_layout()
    fig.savefig(ROOT/"figures/discrete_wages.pdf",bbox_inches="tight")
    fig.savefig(ROOT/"figures/discrete_wages.png",dpi=180,bbox_inches="tight")
    print("PASS: primal feasibility, no positive profit, complementary slackness,")
    print("strong duality, income accounting, unique wage ranges, and hand formulas.")
    for r in results:
        print(r["regime"],r["capability"],r["wages"],r["output"])

if __name__=="__main__":
    main()
