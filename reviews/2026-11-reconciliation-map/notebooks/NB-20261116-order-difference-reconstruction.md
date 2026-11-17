---
id: NB-20261116-order-difference-reconstruction
title: Does the gravitational order-difference selection criterion survive known interference data?
status: resolved_negative
opened: 2026-11-16
owners:
  - {name: thinx-claude, kind: ai}
  - {name: JD Longmire, kind: human}
provenance: reconstruction
claims: []
work_package: >
  Charter obligation (b), selection rule. The charter's former working-notes section 4.5,
  repointed to section 7.1 of reviews/2026-11-reconciliation-map/reconciliation-map.md.
hypothesis: >
  A-actualization occurs when the Planck-density element-count difference between the branches
  of a mass superposition exceeds its Poisson noise, and this criterion is consistent with the
  observed coherence of electron and large-molecule superpositions.
failure_condition: >
  For a well-documented interference experiment, the criterion predicts collapse in less time than
  the coherence actually observed, for every physically reasonable branch separation R.
preregistered_commit: retroactive
retroactive_reason: >
  The calculation was done in the session of 2026-11-16, before this standard existed, to reconstruct
  the programme lead's working notes, which are absent from the repository. The failure condition
  above was written after the result was known.
method: >
  Sprinkle at Planck density rho = l_P^-4. A mass m perturbs the metric by h(r) ~ Gm/(r c^2); over a
  region of radius R and duration T the 4-volume shift is (Gm/c^2)(2 pi R^2)(cT), against
  V = (4/3) pi R^3 cT. Signal-to-noise is rho dV / sqrt(rho V); actualize at SNR = 1. Choices made by
  the reconstructor: the geometric prefactor, the identification of branch separation with R, and the
  coherence times used for comparison (electron flight time about 1e-8 s is an estimate).
sources:
  - {ref: "Tonomura, A. et al. (1989) Demonstration of single-electron buildup of an interference pattern. American Journal of Physics 57, 117-120.", verification: primary_abstract}
  - {ref: "Fein, Y.Y. et al. (2019) Quantum superposition of molecules beyond 25 kDa. Nature Physics 15, 1242.", verification: primary_abstract}
computations: [CMP-006]
circularity_check: >
  No parameter is fitted to the outcome. G cancels analytically (sqrt(rho) = c^3/(hbar G) and dV is
  proportional to G) and numerically (SNR unchanged to seven figures under G varied by ten orders of
  magnitude), so the conclusion does not depend on a gravitational coupling chosen to fail. The
  conclusion is robust over R from 10 nm to 100 micrometres. The prefactor and R are the
  reconstructor's choices and are the points a red-team pass should press.
result: >
  The criterion fails. SNR = sqrt(3 pi) (mc/hbar) sqrt(R c T), independent of G; collapse time
  T = lambda_C^2 / (3 pi R c). Predicted collapse for an electron at R = 1 micrometre is 5.3e-29 s
  against about 1e-8 s observed (20.3 orders too fast); at R = 10 nm, 18.3 orders; for a 25 kDa
  molecule at R = 266 nm, 40.9 orders. This matches the two features the charter reports
  (G-cancellation, about nineteen orders). Fidelity to the programme lead's original calculation is
  not established: the original notes are lost.
confidence: MEDIUM
red_team: requested 2026-11-17
---

# NB-20261116-order-difference-reconstruction

## Log

### 2026-11-16

Reconstruction computed in session at JD's direction ("reconstruct from context and inference"), as section 7.1 of the reconciliation map, with `code/order_difference_reconstruction.py`. Reported to JD with confidence MEDIUM that it matches the original calculation and HIGH that the criterion is falsified.

JD accepted the map's recommendations the same night. The charter amendment of 2026-11-16 repoints the charter's working-notes citations to section 7 of the map, so this calculation is now load-bearing.

### 2026-11-17

Recorded under the research-records standard. Two consequences of that standard, stated plainly:

- The confidence on the falsification is recorded as MEDIUM. The 2026-11-16 report said HIGH, but the failure condition here was fixed after the result, and a retroactive record may not carry HIGH. The physics is unchanged; the label now reflects the record.
- The computation is registered as CMP-006, and its output is re-checked in CI from now on. Its reference transcript is a baseline captured by its author.

Red-team pass requested: an independent check of the prefactor, of the choice of R, of the coherence-time inputs, and of whether a different counting of the order difference could rescue the criterion.
