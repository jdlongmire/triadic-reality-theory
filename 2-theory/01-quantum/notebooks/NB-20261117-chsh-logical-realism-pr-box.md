---
id: NB-20261117-chsh-logical-realism-pr-box
title: Does logical realism, operationalized on a finite CHSH scenario, exclude superquantum (PR-box) correlations?
status: open
opened: 2026-11-17
owners:
  - {name: thinx-claude, kind: ai}
  - {name: thinx-gpt, kind: ai}
  - {name: JD Longmire, kind: human}
provenance: original
claims: [QM-001, OPN-009]
work_package: >
  ROADMAP v0.3 item 1.1 (strong positivity from the triad; issue #5) and the charter's
  logical-realism commitment. Handed off by thinx-gpt at JD's request, 2026-11-17
  ("logically real, not Bell-local").
hypothesis: >
  On the CHSH scenario (settings x, y in {0,1}; outcomes a, b in {0,1}), take logical
  realism as: (LR1) every actualized record is a determinate bivalent value, with Excluded
  Middle scoped to actualized propositions; (LR2) in each run the actualized records of both
  wings form one jointly consistent history, including across spacelike separation;
  (LR3) unperformed measurements carry no context-independent value; plus no-signaling.
  Then: (H1) the PR box (S = 4) satisfies LR1 to LR3 and no-signaling, so logical realism so
  operationalized excludes no no-signaling correlation; (H2) replacing LR3 with global
  counterfactual definiteness (one consistent assignment to all four settings per run)
  restricts to S at most 2, which experiment excludes; (H3) a joint quantal measure on the
  sixteen counterfactual histories, with each measured partition decoherent, reproduces the
  PR box only if it is not strongly positive; (H4) strongly positive such measures do not
  exceed S = 2 sqrt(2). Neither operationalization of logical realism yields the Tsirelson
  bound; the restriction comes from strong positivity.
failure_condition: >
  Any of: (a) LR1 to LR3 with no-signaling, as operationalized, exclude the PR box or impose a
  bound strictly between 2 and 4, so that L3 does nontrivial work toward the quantum bound and
  thinx-gpt's guardrail fails for this operationalization; (b) a strongly positive joint quantal
  measure with decoherent measured partitions is found with S above 2 sqrt(2) + 1e-6,
  contradicting Craig et al. (2007) or exposing an error in this setup; (c) no Hermitian joint
  quantal measure with decoherent measured partitions reproduces the PR box, so that strong
  positivity is not what excludes PR boxes in this framework.
preregistered_commit: 516e754e179168b3fe90a95e7947235c15bc5bbc
method: >
  (1) Check H1 directly: the PR box p(ab|xy) = 1/2 when a XOR b = xy, else 0; verify each
  run's record is a consistent bivalent pair and that marginals are uniform. (2) H2: enumerate
  the sixteen deterministic assignments (a0, a1, b0, b1) and take the maximum of S; mixtures
  cannot exceed it. (3) H3: solve the linear system for a real symmetric 16 x 16 decoherence
  functional D whose diagonal block sums give the PR box on each measured partition and whose
  off-diagonal block sums within each partition vanish; report the minimum eigenvalue of the
  minimum-norm solution and of the closest solutions found, and whether any solution is
  positive semidefinite. (4) H4: maximize S over D = G G^T (strongly positive by construction)
  subject to the same normalization and decoherence constraints, by constrained optimization
  from fixed seeds. Choices made by the investigator: the operationalization of LR1 to LR3
  (thinx-gpt's candidate principle and the charter's scoping), restricting D to real symmetric,
  imposing decoherence of each measured partition so that its probabilities sum to one, and
  using local optimization for H4, which can show attainment and fail to find violations but
  cannot prove the bound; the bound itself rests on Craig et al. (2007).
sources:
  - {ref: "Craig, D., Dowker, F., Henson, J., Major, S., Rideout, D. and Sorkin, R.D. (2007) A Bell inequality analog in quantum measure theory. Journal of Physics A 40, 501-523.", verification: primary_abstract}
  - {ref: "Popescu, S. and Rohrlich, D. (1994) Quantum nonlocality as an axiom. Foundations of Physics 24, 379-385.", verification: unverified}
  - {ref: "Fine, A. (1982) Hidden variables, joint probability, and the Bell inequalities. Physical Review Letters 48, 291-295.", verification: unverified}
computations: []
circularity_check: ""
result: ""
confidence: ""
red_team: not_required
---

# NB-20261117-chsh-logical-realism-pr-box

## Log

### 2026-11-17

Opened at JD's direction ("Yes", 06:03 CT), from thinx-gpt's handoff of the same morning. Hypothesis, failure condition, and method are committed here before any computation. Expected answers are stated as H1 to H4; (c) in the failure condition is the outcome I am least sure of.
