# Session — 2026-06-26 — Task 0.1 decisive computation (the commutant result)

> Programme: TRT. Continuation of the agent-roster work on the critical-path root, OPN-001 (co-admissibility). Last session sharpened Task 0.1 to a concrete computation; this session ran it. Executor: thinx-Claude as Formalization-Agent (inline, computational) → independent Red-Team-Reviewer subagent → Peer-Review calibration (inline). Authority: agents recommend; operator records; JD final on labels.

## What happened

1. **Verified the model against the primary source.** Fetched Feller, Coeuret Cauquil & Roussel (2020), arXiv:2001.10851; extracted Eqs. (3)–(4): `H = ω_c N`, `L_α = √κ_α a` (coherent-state channel), `L_n = √κ_n a†a` (number dephasing); pointer states maximize variation of the **purity** witness `γ = tr ρ²`. Crucially also Eq. (17): the paper proves the two quantum channels **commute**.
2. **Built + ran the decisive computation** — `3-prediction/co-admissibility-conjecture/code/coadmissibility_commutant.py` (numpy/scipy, deterministic, no fitted params, N=8..20 + rate check). Result, all three tested measure-free criteria **non-discriminating**:
   - (i) commutant `{a,a†,N,H}' = ℂ·Id` (dim 1) — no DFS, escape hatch closed;
   - (ii) Fock/coherent pointer states lie in the complement (residual `√(2n+1)`);
   - (iii) `[𝒟_n,𝒟_α] = 0` to machine precision — pairwise-commuting set = whole space, **reproducing the paper's Eq. (17)**.
3. **Caught + corrected my own divergence.** My first print narrative claimed the (iii) commutator was a truncation-boundary artifact ("edge fraction = 1"); the actual numbers showed the total norm already at machine precision everywhere. Corrected the narrative to the simpler, stronger truth (no truncation defect; `N` is exactly diagonal) and removed the dead edge-localisation scaffolding.
4. **Independent Red-Team subagent** ran the code, re-derived the algebra three ways (row-stacking, direct matrix-action, an analytic coherence-band argument), pushed N to 64, and added a falsifiability control (quadrature channel → commutator norm ≈ 585, proving the machine-zero is real, not a degenerate routine). Verdict: **correctness SURVIVES (HIGH); scope SURVIVES WITH QUALIFICATION (MEDIUM-HIGH).**
5. **Acted on the three Red-Team findings:** scoped the overreaching "Honest status" wording to the *tested* criteria; added the **structural diagnosis** (the tested objects are rate-independent, the pointer family is rate-governed at `κ_n/κ_α≈1`, so they cannot track it) as the genuinely informative content; relabeled the printed singular value (it's the 2nd sv / boundary mode; the identity is the exact zero below it).

## Outcome (recorded)

- `2-theory/00-foundational/co-admissibility-formalization.md` — **Attempt 2** (the decisive computation): result, structural diagnosis, bounded scope.
- `traceability/claims/OPN-001.yaml` — `formal_artifacts.computation` wired (status `reproduces`); notes record the negative; labels held (`proof_status: prose_only`, `epistemic: open`); positive move declined. `PRD-001.yaml` — handle (d) now computed (both horns fired); epistemic held `conjectured`.
- `3-prediction/appraisal.md` — progressive theoretical step logged; pressures the decoherence route toward the degeneration watch; still **Unappraised**.
- `reviews/2026-06-redteam-coadmissibility/review-attempt2-computation.md` — full red-team pass archived.
- `build.py`: validation OK, dependency graph ACYCLIC, reports fresh. Exit 0.

## Roster verdict (meta)

The chain delivered again: the producer caught its own narrative error mid-stream (check-actions-against-intent), and the independent Red-Team upgraded a bare "these fail" into a *structural* result (rate-independent objects can't track a rate-governed transition) plus a falsifiability control — turning a negative into an informative, where-to-look-next contribution. No label was inflated; the negative is honestly scoped.

## The result, in one line

On the real incompatible-channel model, **every measure-free co-admissibility criterion tried is well-defined but non-discriminating** — the `risk_if_false` outcome for OPN-001, recorded as a progressive negative, materially pressuring PRD-001's discriminating content without claiming the measure-free design space is closed.

## Carry to next

- **Decision for JD:** how hard to read the negative. Options: (a) keep OPN-001 `open` with the recorded negative and pursue the one open sub-question — *does any rate-dependent, generator-derived measure-free object discriminate?* (the only door the result leaves open); (b) treat the decoherence route as degenerating and **pivot the discriminating effort to the gravity linearity test** (Task 3.1 / PRD-002), which the shared L²-residual ties to; (c) consider a `proof_status` enum value for "recorded computational negative" (methods change — current enum has no clean slot).
- Still open from before: O1b (v1.0 refs/figures → DOI), O2b (Core→LRT import), figure SVGs.
- A surviving criterion, if it exists, must be **rate-dependent and generator-derived** — that is the search constraint the computation hands forward.
