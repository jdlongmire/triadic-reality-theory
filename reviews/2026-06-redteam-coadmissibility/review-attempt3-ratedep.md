# Red-Team Review — Co-Admissibility Attempt 3 (the rate-dependent door)

**Date:** 2026-06-26
**Target:** `3-prediction/co-admissibility-conjecture/code/coadmissibility_ratedep.py` — the claimed answer to JD's directed sub-question (a): *does any rate-dependent, generator-derived measure-free object reproduce the Feller pointer structure?*
**Reviewer:** Red-Team-Reviewer (independent subagent; ran the code, extracted Feller's analytic critical coupling from the PDF, computed alternative candidates).
**Outcome: the first version's conclusion ("NO, comprehensively non-discriminating") was REFUTED.** This is the headline — the adversarial critic overturned the producer's central claim. The corrected result (a dichotomy) is recorded in `co-admissibility-formalization.md` Attempt 3.

## What the Red-Team found

**1. The artifact omitted the primary-source critical coupling.** Feller et al. Eqs. 39–40 give it explicitly:

> `κ_n/κ_a = n₀ + ½ + √(n₀(n₀+1))  ≈ 2n₀ + 1`  (energy-dependent).

The first artifact discussed "the analytic critical coupling" without ever stating the value, and compared no candidate against it — a research-grade gap (now fixed in both the artifact and `co-admissibility-conjecture.md`).

**2. The artifact tested the wrong comparison (the refutation).** Feller's criterion is whether the Fock state `|n₀⟩` is a **local maximum of the purity-variation γ̇ within the fixed-energy shell** (it transitions max→saddle in the `(|n₀-1⟩,|n₀+1⟩)` plane). It is **not** a Fock-vs-coherent two-family comparison. The first artifact computed γ̇(Fock) vs γ̇(coherent) → g*=1, and concluded (wrongly) that the only discriminating measure-free functional gives a timescale-degenerate answer.

**3. The correct application reproduces the analytic critical coupling.** The **same** initial purity-rate γ̇ (generator-derived, rate-dependent, witness = purity, no observation window), applied via Feller's energy-shell Fock-stability criterion, matches Eq. 40 to <1%, N-converged (independently re-derived and re-verified by the operator: rel. err <0.2%, n₀=2…6):

| n₀ | analytic g* | γ̇ stability-flip g* |
|---|---|---|
| 2 | 4.949 | 4.95 |
| 4 | 8.972 | 8.98 |
| 6 | 12.981 | 13.00 |

So a rate-dependent measure-free object **does** reproduce the Feller pointer structure.

**4. Coverage points (do not move the verdict).** All non-stationary Liouvillian eigenmodes are traceless by trace conservation (a theorem, not a numerical accident of the slowest mode); the steady state is the vacuum at every g (no finite-energy content) — so the witness-free generator spectrum is genuinely non-discriminating. A steady-state-relative observation window makes the Fock-vs-coherent crossover window-invariant (~1.1–1.2) but still energy-dependent and ≠ Feller — reinforcing that Fock-vs-coherent is the wrong object.

## Verdicts

- **CORRECTNESS of the narrow claim — survives.** The three objects *as the first artifact defined them* do not yield Feller's g*; the code was correct for the comparison it made. Confidence HIGH.
- **SCOPE / conclusion — REFUTED.** "Sub-question (a): NO" and "comprehensively non-discriminating" are false. A measure-free, rate-dependent, generator-derived functional (purity-rate γ̇ via energy-shell stability) reproduces the analytic critical coupling. Confidence HIGH (matches primary-source Eq. 40 to <1%, N-converged).

## The real result and the live threat

This is **not** a clean win for TRT. γ̇ reproduces Feller *exactly because it is the purity predictability sieve* — it adopts the witness rather than eliminating it. The honest picture is a **dichotomy**: witness-free measure-free objects are non-discriminating; witness-fixed (purity) ones are standard einselection re-described. The conjecture's actual target — a **witness-independent** criterion with content **beyond** einselection — is delivered by neither. The live falsifier is therefore PRD-001 **(a)** ("reproduces the witness-dependence it was meant to eliminate / predicts nothing new"), i.e. **re-description**, a different and more dangerous finding than the artifact's claimed "no prediction".

## Recommendations (actioned)

1. **Do not move OPN-001 to `refuted`** — that would record a false negative. The state is "discrimination only by re-description," and the re-description horn is not yet closed. **Done** (labels held; JD's call).
2. **Correct the artifact** — candidate must use Feller's energy-shell stability, not Fock-vs-coherent. **Done** (Attempt 3 rewrite).
3. **Add the primary-source critical coupling** (Eq. 40) to the artifact and the conjecture doc. **Done.**
4. **Drop "comprehensively non-discriminating"** → the dichotomy framing; the live threat is re-description. **Done.**

## Disposition

A genuinely progressive step — but its value is the *correction*: the right rate-dependent measure-free object exists and matches the primary source, and the threat to TRT's discriminating content is re-description (falsifier a). New decisive sub-question recorded: does γ̇ differ from standard einselection in the regime where einselection is itself witness-dependent?
