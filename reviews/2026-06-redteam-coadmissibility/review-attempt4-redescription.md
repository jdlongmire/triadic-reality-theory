# Red-Team Review — Co-Admissibility Attempt 4 (the re-description test, root-node)

**Date:** 2026-06-26
**Target:** `3-prediction/co-admissibility-conjecture/code/coadmissibility_redescription.py` (+ `results_redescription.json`) — the decisive test of whether the purity-rate `γ̇` criterion predicts anything beyond standard einselection.
**Reviewer:** Red-Team-Reviewer (independent subagent, 3rd / root-node pass; ran the code, re-derived the algebra, refined grids).

## Verdicts

| Axis | Verdict | Confidence |
|---|---|---|
| **Correctness** (Test 1 α/2 law; Test 2a analytic match; Test 2b drift-real; determinism) | **SURVIVES** — code correct; two claims *strengthened* | **HIGH** |
| **Scope / label** ("re-description; falsifier (a) fires; pivot to gravity") | **SURVIVES with wording corrections (applied)** | **MEDIUM-HIGH** |

## Findings

- **Test 1 (α/2 law) — correct and stronger than stated.** Analytically exact (ρ projector ⇒ `d/dt tr ρ^α|₀ = α tr(ρρ̇) = (α/2)γ̇`); confirmed numerically for **non-integer** α too (α=1.5,2.5,5 match α/2 to <0.3%). So *every* Rényi witness ranks pure states identically at t=0 → the short-time sieve is witness-independent and equals `γ̇`.
- **Test 2a — confirmed.** `γ̇` energy-shell critical coupling matches Feller's analytic `g*=n₀+½+√(n₀(n₀+1))` to rel.err 3–5×10⁻⁴ (fine grid, no fitted params).
- **Test 2b — drift is REAL, not a grid artifact** (the original step-0.2 grid made it look quantized). Refined to step 0.01 + integration steps 14→120 (converged): the finite-T critical coupling converges **monotonically** to `γ̇`'s value as T→0 (5.18 @ T=0.4 → 4.97 @ T=0.01 → 4.95). So `γ̇` is the **exact T→0 boundary limit** of the witness/time-dependent family — silent on the T>0 drift, not merely coarse there.
- **Strongest pro-TRT counter (steelman) collapses.** "Co-admissibility = the witness-independent short-time sieve = `γ̇`" satisfies the conjecture's witness-independent clause — but `γ̇` at T→0 *is* standard short-time einselection (predictability sieve at leading order = purity-decay rate), so there is zero daylight for novel content. The counter buys witness-independence by relocating co-admissibility to exactly where einselection is already witness-independent and already equals `γ̇`. `γ̇` never differs from standard einselection with added content, anywhere.
- **Which limb of falsifier (a) fires.** (a) = "reproduces the witness-dependence it was meant to eliminate / predicts nothing new." `γ̇` is witness-*independent*, so the **first limb does not apply**; (a) fires via the **"predicts nothing new"** limb. (The original verdict conflated the two — corrected.)

## Recommendations (all actioned)

1. Verdict text: cite the "predicts nothing new" limb specifically; note `γ̇` is witness-independent so the other limb doesn't apply. **Done.**
2. Record the T→0 boundary-limit finding; de-round the Test-2b grid. **Done.**
3. PRD-001 → recommend `refuted-by-re-description` (epistemic enum lacks the value → JD + possible schema addition; held `conjectured` pending). **Recorded in PRD-001 notes.**
4. OPN-001 stays `open`/`prose_only` at root; annotate the *decoherence instantiation* as re-description; surviving discriminating value rests on gravity (OPN-002). **Done.**
5. "Pivot to gravity": keep, but drop "not reached through this witness" — PRD-002 shares OPN-001 + the free-measure hazard, so this *lowers* its prior rather than compartmentalising. **Done.**

## Disposition

A clean, honest, correctly-bounded recorded **negative** — the decoherence descendant resolves to re-description. The root-node question for the decoherence route is settled (for the `γ̇`/purity form): no novel content. Genuine contribution; the discipline caught a labeling imprecision but not a substantive error. Discriminating hope passes to the gravity descendant (PRD-002), with a lowered prior.
