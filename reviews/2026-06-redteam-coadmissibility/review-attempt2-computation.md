# Red-Team Review — Co-Admissibility Attempt 2 (the decisive computation)

**Date:** 2026-06-26
**Target:** `3-prediction/co-admissibility-conjecture/code/coadmissibility_commutant.py` (+ `results.json`) — the claimed computational NEGATIVE resolution of OPN-001 (Task 0.1).
**Reviewer:** Red-Team-Reviewer (independent subagent; ran the code, re-derived the algebra by three routes, pushed N to 64, added a falsifiability control).
**Producer:** Formalization-Agent (inline), on the verified primary-source model — Feller, Coeuret Cauquil & Roussel (2020), arXiv:2001.10851, Eqs. (3)–(4).

## Verdicts

- **Computation correctness: SURVIVES — confidence HIGH.**
- **Scope of the stated conclusion: SURVIVES WITH QUALIFICATION — confidence MEDIUM-HIGH.**

## Per attack vector

**1. Truncation artifacts — does not land.** Independent harness to N=64: exactly one true machine-zero singular value at every N (= the identity); `dim=1` robust even at tolerance 0.1. The value the script printed as "smallest nonzero sv" is the *second* sv, a truncation-boundary mode ~N^{-1/2} — shrinking but never approaching the identity's exact zero, and no second mode collapses. `‖[𝒟_n,𝒟_a]‖` stays at machine precision; the mild growth with N is float accumulation, confirmed by a direct matrix-action build (no kron) at N=24.

**2. Analytic backbone — does not land (backbone correct).** Vectorization verified two independent ways (row-stacking rebuild; direct matrix-action). Structural derivation: `𝒟_n` multiplies coherence band `ρ_{mn}` by scalar `g(m−n)=−½(m−n)²`; `𝒟_a` preserves coherence-order, so `[𝒟_n,𝒟_a]=0` exactly and analytically — consistent with paper Eq.(17). `{a,a†}'=ℂ·Id` correctly justified (Fock-space irreducibility). Pointer residuals analytically `√(2n+1)`, N-independent, unambiguously > 0.

**3. Mis-formalization / strawman — partially lands (the real weakness).** `{ρ:[𝒟_n,𝒟_a]ρ=0}` is a defensible reading of "pairwise non-contradiction," not a strawman. But all three tested objects share a feature: they are **algebraic / rate-independent**, while the pointer family is **rate-governed** (critical coupling ~1). A rate-independent object cannot in principle track a rate-dependent transition — so the three tests were structurally pre-destined to be non-discriminating. The reviewer tested the most natural untested rate-*dependent* object — the Liouvillian slow modes: there is genuine rate-dependent structure (a slow-mode level-crossing near `κ_n/κ_a≈1`), but its eigenvector is a `k=±1`/`k=0` coherence band, not a pointer projector — so it also fails. Net: the verdict survives, but the methodology only licenses "the **tested** objects fail," and the measure-free design space is not exhausted.

**4. Scope overreach — lands as a wording issue.** Fixed: Attempt-1 "Honest status" and the code/results verdict were tightened to scope the negative to the tested criteria.

**5. Smuggled assumptions / circularity — does not land.** No fitted parameters (ω_c=κ_a=κ_n=1 declared; rate-independence cross-checked at ratio 5). Falsifiability control: swapping the dephasing channel for a quadrature channel `D[a+a†]` gives commutator norm ≈ 585 — proving the machine-zero is a real property of *this* model, not a routine that returns 0 for everything.

## What would change the verdict

A measure-free, generator-derived, **rate-dependent** object that reproduces the Fock↔coherent pointer interpolation would overturn the negative (turn it into a confirmation). The natural such candidate (Liouvillian slow modes) was checked and fails, raising confidence in the negative — but the space is not exhausted, so scope stays MEDIUM-HIGH, not certain.

## Recommendations (actioned this session)

1. Tighten the overreaching "Honest status" wording → scoped to the tested criteria. **Done** (Attempt 2 + code/results verdict).
2. State the rate-independence point as a *structural diagnosis*, not just a check (tells future formalizers where to look). **Done.**
3. OPN-001 stays `open` (proof_status `prose_only`); the computation wired as `formal_artifacts.computation`. Positive label move declined. **Done** — final label call is JD's.
4. Relabel the printed "(i)" singular value as the *second* sv (boundary mode); identity is the exact machine-zero below it. **Done.**

## Disposition

A genuine, progressive **negative** for the tested measure-free criteria. Correct, reproducible, honestly scoped. Pressures PRD-001's discriminating content for the forms tried; does **not** close the measure-free design space. Open sub-question recorded: does any rate-dependent measure-free object discriminate?
