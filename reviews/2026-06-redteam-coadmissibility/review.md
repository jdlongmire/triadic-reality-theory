# Internal Red-Team Pass — Co-Admissibility (Task 0.1)

- **Date:** 2026-06-26
- **Reviewers:** TRT agent roster — Formalization-Agent (producer), Red-Team-Reviewer + Peer-Review-Agent (critics). First exercise of `0-program-methods/agents/`.
- **Target:** Task 0.1, a measure-free co-admissibility criterion `C(constraints) → admissible set`.
- **Disposition:** result is a **progressive theoretical step**, not a resolution. OPN-001 stays **open** (`proof_status` → `prose_only`). PRD-001 gains a sharper falsifier.

## Producer (Formalization-Agent)

Proposed **C₀ = {ρ : 𝓛(ρ)=0}** — the joint-invariance/kernel of the Lindblad generator from constraint data `{Lₖ,γₖ,H}` alone; the dissipative port of the program's "joint L₃-satisfiability = flatness = kernel of the holonomy obstruction." Measure-free and definite. Audit: degenerates to a single steady state in the incompatible-channel regime; re-inflating to the pointer family reintroduces a witness unless a decoherence-free subsystem exists. Verdict: achievable for the definition/agreement regime; likely needs a free measure for the discriminating prediction.

## Red-Team-Reviewer (attacks)

1. **Failure = rescue (one theorem).** Lindblad fixed-point set nontrivial ⟺ commutant `{Lₖ,Lₖ†,H}'` nontrivial (Spohn 1977; Frigerio 1978; Evans). The degeneration and the DFS escape hatch are the same condition negated — the whole question reduces to **one open algebraic fact**.
2. **Wrong subspace.** Even a nontrivial commutant yields the *protected* sector; the einselected pointer family lives in the *decohering* complement — disjoint by construction. Escape hatch leans **refuted**.
3. **Untested weaker criterion.** "Non-contradiction" is *pairwise* (`[𝓓_k,𝓓_α]=0`), not global kernel; the collapse into joint-invariance was unjustified. A weaker, more L₃-faithful measure-free criterion was never tried.
- **Verdict:** UNCERTAIN, escape hatch leaning refuted. **OPN-001 stays `open`** (not `argued`). Decisive check is **two-part**: commutant nontriviality + pointer-location, over the Feller cavity model.

## Peer-Review-Agent (calibration)

- C₀ is honestly presented as re-description for the agreement regime, unfinished for the discriminating regime — **no degenerating move**, *provided* the wording keeps the scope qualifier.
- `epistemic_status: argued` is **overclaimed** (in this programme `argued` = a *complete* argument, cf. LOG-002/ONT-004); the central claim degenerates and the repair is unverified → **stays `open`**. `proof_status: open→prose_only` accepted.
- Commutant check is a **genuine, cheaper, antecedent falsifier** → accept onto PRD-001 `falsifies` (a).
- Move is **progressive** (sharpened test + unifying construction); programme remains **Unappraised**.

## Outcome (applied)

- `2-theory/00-foundational/co-admissibility-formalization.md` — added "Attempt 1 (C₀)".
- `OPN-001` → `proof_status: prose_only`, epistemic `open`; notes + `depends_on: OPN-002`.
- `PRD-001` → `falsifies` clause (d): the commutant/pointer-location handle.
- `appraisal.md` — progressive theoretical step logged; still Unappraised.
