# Session — 2026-06-26 (cont.) — Task 0.1: the re-description test closes the decoherence door

> Same session, final leg. JD: "run the test" — the decisive sub-question Attempt 3 left open: does the purity-rate `γ̇` (the only measure-free form that discriminates) differ from standard einselection where einselection is witness-dependent? Formalization-Agent (computational) → independent root-node Red-Team (3rd pass) → operator verification.

## What happened

1. **Reasoned the structure, then computed it** (didn't trust the analytics alone — the Attempt-3 burn was fresh). Two exact pieces:
   - **Test 1:** for a pure state `d/dt tr ρ^α|₀ = (α/2)·γ̇` for every Rényi-α (proven + verified, incl. non-integer α). So all witnesses rank pure states identically at t=0 → the short-time sieve is **witness-independent** and equals `γ̇`.
   - **Test 2:** `γ̇`'s energy-shell critical coupling = the analytic standard-einselection `g* = n₀+½+√(n₀(n₀+1))` to <0.06%. The witness-dependence Feller documents is a **finite-observation-time** phenomenon; `γ̇` is the exact `T→0` boundary limit and is silent there.
2. **Verdict: RE-DESCRIPTION.** `γ̇` coincides with einselection where einselection is unambiguous and is silent where it is ambiguous — it predicts nothing new. PRD-001 falsifier (a) fires.
3. **Root-node Red-Team** ran the code, re-derived the α/2 law (strengthened: non-integer α too), refined the Test-2b grid (drift is REAL — finite-T converges monotonically to `γ̇` as T→0: 5.18→4.97→4.95), and attacked the strongest pro-TRT counter ("γ̇ *is* the witness-independent criterion") — it collapses because `γ̇` at T→0 *is* standard einselection. **Correctness HIGH; scope SURVIVES with wording fixes.**
4. **Applied the Red-Team's three corrections:** (a) falsifier (a) fires via the *"predicts nothing new"* limb only — `γ̇` is witness-*independent*, so the "reproduces witness-dependence" limb does NOT apply; (b) recorded the `T→0` boundary-limit finding + de-rounded the grid; (c) the gravity pivot lowers PRD-002's prior (shared OPN-001 + free-measure hazard), not compartmentalized.

## Outcome (recorded)

- `3-prediction/co-admissibility-conjecture/code/coadmissibility_redescription.py` (+ `results_redescription.json`) — reproduces, assertions pass.
- `2-theory/00-foundational/co-admissibility-formalization.md` — **Attempt 4** (the door closes).
- `traceability/claims/OPN-001.yaml` (third computation artifact + decoherence-instantiation annotation) + `PRD-001.yaml` (re-description confirmed; recommend refuted-by-re-description, pending JD/schema). `build.py` acyclic + fresh.
- `3-prediction/appraisal.md` — decoherence descendant resolved (recorded negative); one of two discriminating routes closed; still **Unappraised**.
- `reviews/2026-06-redteam-coadmissibility/review-attempt4-redescription.md`.

## The bottom line (root node, decoherence route)

The co-admissibility criterion, in the only measure-free form that discriminates (`γ̇`/purity), **reproduces standard einselection and predicts nothing new** on the Feller model. The decoherence descendant (PRD-001) is a recorded **negative** (re-description). This is a *progressive* resolution — the conjecture's own falsifier, decisively triggered and anchored to the primary source — but it means TRT's first discriminating route does not deliver a novel fact.

## Roster verdict (meta)

Four-attempt arc on the root node, each adversarially checked. The roster caught a wrong producer conclusion (Attempt 3) and tightened a labeling imprecision (Attempt 4) without ever inflating a result. Net: the decoherence route is honestly closed, the primary-source critical coupling is now on record, and the discriminating effort has a clear next home.

## Carry to next

- **Programmatic call for JD:** pivot the discriminating effort to the **gravity linearity test** (PRD-002 / Task 3.1, keystone OPN-002) — the remaining discriminating descendant — with the caveat that this decoherence negative *lowers its prior* (same free-measure hazard). Alternative: accept the decoherence negative as sufficient and consolidate (DOI / write-up) before opening gravity.
- **Label decision for JD:** PRD-001 → refuted-by-re-description (needs an epistemic enum value or annotation); OPN-001 root stays open with the decoherence instantiation annotated.
- Lower-risk carryover unchanged: O1b (v1.0 refs/figures → DOI), O2b (Core→LRT import), figure SVGs.
