# A three-type version, solved algebraically

This is an original finite-type analogue of Ide and Talamàs (2025), not a proof of their continuum Propositions 5–6. Read alongside the course PDF (May 20, 2025) and arXiv v11 (February 25, 2025). The discrete population does not satisfy the paper's continuous, strictly positive density assumption. In particular, continuum uniqueness and interval-of-winners claims cannot simply be imported.

## Technology and the agent's problem

Humans have knowledge z in {0, 1/2, 1}, with masses (11/20, 3/10, 3/20). Each has one unit of time. Difficulty is uniform on [0,1]; solving produces one unit of the numeraire. Let h=1/2 and compute supply μ=2. AI capability is a<1. Firms are competitive, have at most two layers, and choose the organization with maximal profit. Humans maximize income over their available roles; compute owners maximize rental income.

A worker of type z fails with probability 1−z. Each request costs h units of solver time, whether successful or not. Thus

    h n(z)(1−z)=1  =>  n(z)=1/[h(1−z)].

A team with solver s>z produces n(z)s, NOT n(z)(s−z). The latter counts only rescued tasks and omits workers' own successes. Equivalently, z+(1−z)(s−z)/(1−z)=s per worker.

Per worker, a human team consumes one worker plus h(1−z) solvers and yields s. Zero profit requires

    w(z)+h(1−z)w(s)=s

on active teams, with ≥ for every feasible team (no profitable entry). Independent production imposes w(z)≥z. Equal-knowledge teams are dominated by independent production and need not be enumerated.

## Pre-AI equilibrium: solve three equations

Write wages (u,v,t) for the low, middle, and high types. The three active team conditions are

    u+v/2=1/2,    u+t/2=1,    v+t/4=1.

Subtracting the first from the second gives t−v=1. Substitute in the third:

    (t−1)+t/4=1  =>  t=8/5, v=3/5, u=1/5.

These exceed each type's independent output. Let x,y,q be the masses of low workers assigned to middle solvers, low workers assigned to high solvers, and middle workers assigned to high solvers. Market clearing gives

    x+y=11/20,   x/2+q=3/10,   y/2+q/4=3/20.

Hence x=8/25, y=23/100, q=7/50, all positive. Output is

    Y0=x/2+y+q=53/100.

Wage income is (11/20)(1/5)+(3/10)(3/5)+(3/20)(8/5)=53/100.

The positive allocation and the no-positive-profit wage vector certify optimality without invoking a solver. These three independent active equalities also pin all three wages. Other mass choices can instead leave a wage interval; this is why the computational check tests dual wage ranges.

## Autonomous AI: the opportunity cost is r=a

With spare compute used in independent production, r=a. The two new no-entry inequalities are

    w(z) ≥ a − h(1−z)a          (human worker, AI solver; z<a),
    w(s) ≥ (s−a)/[h(1−a)]      (human solver, AI workers; a<s).

For 0<a<1/3, all low humans work with middle solvers, using 11/40 middle humans. The remaining 1/40 middle humans and all 3/20 high humans supervise AI workers. Therefore

    t=(1−a)/[(1−a)/2]=2,
    v=(1/2−a)/[(1−a)/2]=(1−2a)/(1−a),
    u=1/2−v/2=a/[2(1−a)].

All omitted activities have nonpositive profit: v>1/2; u>a/2; u+t/2≥1; v+t/4>1. Compute used by AI workers is (7/40)·2/(1−a)=7/[20(1−a)]<2, so r=a is consistent. The remaining compute produces independently.

Compare the lowest wage with its pre-AI value:

    u>1/5
    iff a/[2(1−a)]>1/5
    iff 5a>2(1−a)                 [because 1−a>0]
    iff a>2/7.

Equality at a=2/7 is NOT a strict gain. This is a capability threshold while autonomy stays fixed. It is an exact result on the branch 0<a<1/3. The branch is not the whole finite model and 2/7 is not the paper's continuum threshold. The three-type linear program below checks additional capabilities.

At a=1/5, wages are (1/8,3/4,2): low loses; middle and high gain. Output is

    L_A=19/32=0.59375,
    K_A=μa=2/5,
    Y_A=159/160=0.99375.

At a=2/5, middle humans remaining after helping the low type instead produce independently. Wages are (1/4,1/2,2), and Y_A=111/80=1.3875. At a=4/5, wages are (2/5,3/5,2), and Y_A=23/10=2.3. Bottom winners therefore need not imply middle winners.

## Non-autonomous AI: free advice is not infinitely capable advice

AI can only advise; unused compute has zero opportunity cost, so r_N=0. A human assisted by AI can earn a, subject to z<a. At a≤1/5, the old wages already dominate this option, so no use of AI is needed and the pre-AI equilibrium remains valid. At equality, humans can be indifferent; our reported optimum uses no AI. Do not automatically transfer the continuum's strict allocation uniqueness to a finite model.

At a=2/5 the low AI-assisted wage is u=a=2/5. The active low–high and middle–high teams imply

    u+t/2=1 => t=6/5,
    v+t/4=1 => v=7/10.

All middle humans (3/10) work with high solvers, consuming 3/40 of them. The remaining 3/40 high humans help 3/20 low workers. The other 2/5 low humans use AI solvers, consuming 1/5 compute; 9/5 compute remains idle. Output is

    Y_N=(2/5)(2/5)+(3/20)+(3/10)=61/100.

All output is labor income because r_N=0. Bottom gains from 1/5 to 2/5, while top loses from 8/5 to 6/5. Autonomous output at the SAME a and μ is 111/80>61/100.

At a=4/5, all low and middle humans use AI advice, while high humans produce independently: wages (4/5,4/5,1), output 83/100, and compute used 7/20<2.

## Output: prove weak inclusion before claiming strictness

Every non-autonomous allocation is feasible with autonomy. Therefore the maximal output with autonomy is at least as large. If a>0 and the non-autonomous optimum leaves δ>0 compute idle, assigning that same idle compute to independent AI production raises output by aδ>0. This proves strictness without assuming that the optimizing human allocation stays fixed.

At a=0 this particular proof fails: aδ=0. The paper's strict comparison at a=0 requires the separate value of AI as workers assisted by knowledgeable humans. Our finite example explicitly verifies that mechanism: autonomous wages (0,1,2), labor/output 3/5>53/100. Do not use a positive-a proof to claim the endpoint.

## Computation and its limits

`discrete_model.py` enumerates every undominated one- and two-layer activity. It maximizes output subject to the three human resource constraints and compute availability. Dual constraints are exactly the no-positive-profit inequalities above. It independently minimizes total factor payments, checks the primal–dual gap, complementary slackness, feasibility, wage uniqueness, income accounting, and the branch formulas. Results are saved in `results.json` and `results.csv`.

Lines joining the three wage points in the presentation are visual guides; the model has no intermediate human types. A few numerical equilibria do not establish the continuum theorem or a global comparative-static claim.
