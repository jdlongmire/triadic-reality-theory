---
id: NB-20261117-d-only-classification-dilemma
title: Can a classification criterion defined over D alone carry discriminating content?
status: open
opened: 2026-11-17
owners:
  - {name: thinx-claude, kind: ai}
  - {name: JD Longmire, kind: human}
provenance: original
claims: [ACT-004, OPN-001, PRD-001]
work_package: >
  OPN-001 (co-admissibility) and charter obligation (b). Reading of the June 2026
  negative on PRD-001, discussed with JD on 2026-11-17.
hypothesis: >
  Any classification criterion over D (inputs intrinsic to D: state, Hamiltonian,
  system-environment decomposition and couplings; unitary dynamics and Born
  statistics left unmodified) either selects what unitary dynamics with einselection
  already selects, or selects otherwise and is contradicted by the dynamics it leaves
  in place. Discriminating content requires a rule acting at D -> X.
failure_condition: >
  A classification criterion over D, as defined, is exhibited that yields an observable
  prediction differing from unitary quantum theory with einselection for some physical
  system, while leaving the dynamics and the Born statistics unmodified. Or the
  dilemma can be proved only with a premise beyond the charter's placement of unitary
  evolution in D, in which case it is recorded as conditional on that premise.
preregistered_commit: 33321893dcec23bdebaa661030418767a14719e5
method: >
  Formalize "classification criterion over D" as a map from D-data to a distinguished
  set of structures whose output does not enter the dynamics or the measure. Show that
  every observable consequence of the output is a function of D's dynamics, so that it
  either coincides with the einselected structure or contradicts the dynamics. Test the
  formalization against the three recorded cases (the purity-rate sieve, the
  idempotent-monad recast, the sheaf probe's probabilistic layer) and against the
  counter-class of dynamical rules (Diosi-Penrose; the order-difference channel), which
  must fall outside it. The definition of "classification" is the investigator's choice
  and is the first thing a red team should press: drawn too narrowly the dilemma is
  trivial, drawn too widely it is false.
sources:
  - {ref: "Zurek, W.H. (2003) Decoherence, einselection, and the quantum origins of the classical. Reviews of Modern Physics 75(3), 715-775.", verification: primary_fulltext}
  - {ref: "Feller, A., Coeuret Cauquil, G. and Roussel, B. (2020) arXiv:2001.10851.", verification: primary_fulltext}
computations: [CMP-001, CMP-002, CMP-003]
circularity_check: ""
result: ""
confidence: ""
red_team: not_required
---

# NB-20261117-d-only-classification-dilemma

## Log

### 2026-11-17

Opened. In discussion JD asked how to read the June 2026 negative on PRD-001. Claude proposed that the negative may be a structural no-go for criteria over D, stated first in the unrestricted form "no criterion over D discriminates". On writing it out, that form is false: dynamical rules built from D-data discriminate (Diosi-Penrose; the order-difference channel of NB-20261116). The hypothesis above is the restricted form. It is registered as ACT-004 (conjectured, proof open). Hypothesis and failure condition are committed here before any attempt at proof.

The source verification levels above are carried from the programme's reference record (ROADMAP v0.2, section 7, "verified this session"); they were not rechecked today.
