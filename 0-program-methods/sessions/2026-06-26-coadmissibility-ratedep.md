# Session — 2026-06-26 (cont.) — Task 0.1 sub-question (a): the rate-dependent door + the dichotomy

> Same session as the morning's decisive-computation entry; JD directed "pursue (a)" — the one open door the Attempt-2 red-team left: *does any rate-dependent, generator-derived measure-free object reproduce the Feller pointer structure?* Executor: thinx-Claude as Formalization-Agent (computational) → independent Red-Team subagent → operator verification. The headline is a **producer error caught and corrected by the red-team**.

## What happened

1. **Pinned the analytic critical coupling from the primary source.** Extracted Feller et al. Eqs. 39–40 from the PDF: `g* = κ_n/κ_a = n₀ + ½ + √(n₀(n₀+1)) ≈ 2n₀+1`, energy-dependent. (Our docs had referenced "the analytic critical coupling" without ever stating the value — a research-grade gap, now fixed.)
2. **Built a first rate-dependent artifact and reached the WRONG conclusion.** It tested generator slow modes (traceless), the initial purity-rate γ̇ Fock-vs-coherent (g*=1), and a finite-time predictability sieve (g*≈1.7–2.3, window/energy-dependent), and concluded "(a): NO — comprehensively non-discriminating." I caught and fixed one framing slip myself (witness vs timescale dependence) before review.
3. **The independent Red-Team REFUTED the conclusion.** It found the artifact tested the *wrong comparison*: Feller's criterion is Fock-state stability **within a fixed-energy shell** (max→saddle of the purity-variation in the `(|n₀-1⟩,|n₀+1⟩)` plane), not Fock-vs-coherent. Applying the **same** γ̇ via Feller's actual criterion **reproduces** `g*` to <1%.
4. **I independently verified the correction** before accepting it: re-derived the Hessian flip (`Δγ̇/s² = −2[2g − (2n₀+1+2√(n₀(n₀+1))cosθ)]`, worst at cosθ=1) and computed it numerically — reproduces `g* = n₀+½+√(n₀(n₀+1))` to <0.2% (n₀=2…6). The Red-Team is right.
5. **Rewrote the artifact to the corrected result** — a dichotomy — and propagated it through the docs/traceability/appraisal.

## The result — a dichotomy (corrected)

- **Witness-free measure-free objects** (Attempt 2's commutant/kernel/pairwise-commuting; plus the Liouvillian generator spectrum — all non-stationary modes traceless, steady state = vacuum) → **non-discriminating** (no pointer prediction).
- **Witness-fixed (purity) objects** — the initial purity-rate γ̇ via energy-shell Fock-stability → **reproduce the analytic critical coupling exactly**, because γ̇ *is* the (linear-entropy) predictability sieve. It matches standard einselection by **adopting its witness** → **re-description**.

There is no middle ground delivering the conjecture's actual claim (a *witness-independent* criterion with content *beyond* einselection). So the live falsifier flips from the earlier (b)/(c) reading to **(a) re-description**.

## Outcome (recorded)

- `3-prediction/co-admissibility-conjecture/code/coadmissibility_ratedep.py` (+ `results_ratedep.json`) — corrected; reproduces, assertions pass.
- `2-theory/00-foundational/co-admissibility-formalization.md` — **Attempt 3** (dichotomy + the recorded correction).
- `3-prediction/co-admissibility-conjecture.md` — analytic `g*` value added (§13.1).
- `traceability/claims/OPN-001.yaml` (second computation artifact) + `PRD-001.yaml` (live falsifier corrected to (a)). `build.py` acyclic + fresh.
- `3-prediction/appraisal.md` — dichotomy logged; threat sharpened to re-description; still **Unappraised**.
- `reviews/2026-06-redteam-coadmissibility/review-attempt3-ratedep.md` — the refutation pass archived.

## Roster verdict (meta)

The most important pass yet: **the adversarial critic overturned the producer's central conclusion**, anchored in the primary source (Eq. 40) and verified independently by the operator. A wrong "negative" would have been recorded as a contribution; the discipline caught it and replaced it with the true (and more dangerous) finding — re-description. EIF §3 in action: false refutation is as bad as false confirmation, and here the *producer's* false negative was the error caught.

## Carry to next

- **The single decisive test now** (the only door ajar): does γ̇ (the purity-rate criterion) **differ from standard einselection in the regime where einselection is itself witness-dependent**? If it agrees everywhere → re-description confirmed → PRD-001 falsifier (a) fires → the decoherence route is degenerating, pivot to gravity (PRD-002). If it differs computably → that difference is TRT's first genuinely novel content. This is a Formalization-Agent (computational) task → Red-Team.
- Lower-risk carryover: O1b (v1.0 refs/figures → DOI), O2b (Core→LRT import), figure SVGs.
- Decision for JD: whether to run the re-description test next, or treat re-description as the likely outcome and pivot the discriminating effort to the gravity linearity test.
