# GitHub Workflow — Agile-DevOps for a Research Programme

How the programme uses GitHub's tools as its operating spine. The principle: treat the research programme like a software product under agile-devops discipline, but keep the *unit of work* epistemic (a problemshift), not a feature.

## The mapping

| GitHub tool | Programme use |
|---|---|
| **Issues** | One per open task / conjecture / review. An issue states a *target*, a *prerequisite*, and a *failure condition* — an issue without a failure condition is not a research task but a hope. Labelled by tier (`tier:1–3`), by PI (`pi-N`), and by commitment (`committed`/`stretch`). |
| **Milestones** | **Program Increments** (the temporal box, e.g. `PI-1`). A PI closes when its objectives are *resolved* — confirmation **or** recorded refutation both count. (Tiers are *labels*, not milestones — they are structural, not temporal.) See [pi-planning/](pi-planning/). |
| **Projects (board)** | Kanban over the PI's work: `Backlog → Formalizing → Computing → Under review → Resolved`. The board is the live view of the positive heuristic. |
| **Pull requests** | Every belt change is a PR, reviewed against the [progressive-vs-degenerating criterion](METHODOLOGY.md). A PR that inflates a confidence label, removes a failure condition, or presents interpretation as derivation is declined regardless of technical quality. |
| **Discussions** | Open conceptual debate before it hardens into an issue or a claim. |
| **Actions (CI)** | The devops gate — see below. |
| **Releases / tags** | Paper versions (`v0.9`, `v1.0`) and frozen programme snapshots for citation. |

## The iteration unit

Research is not sprint-shaped, so an "iteration" here is **one problemshift attempt with a stated success/failure condition** — pick a roadmap task, state what would confirm and what would refute, attempt it, record the outcome (including a recorded failure, which is progress). Cadence is opportunistic, not calendar-locked; the discipline is the stated conditions, not a fixed sprint length.

## CI gate (`.github/workflows/`)

Every push and PR runs, and must pass:

1. **Traceability validation** — `python3 traceability/scripts/build.py` must exit 0: schema-valid claims, **acyclic dependency graph** (the circularity discipline, enforced mechanically), no dangling refs, every linked Lean file present, and every `role: prediction` carrying a `falsifies` condition.
2. **Lean core typecheck** — the Mathlib-free `Core/Primitives.lean` must typecheck with no errors and no `sorry`. (The full Mathlib build is a separate, heavier job gated on the LRT sub-project landing.)
3. **Generated reports fresh** — `traceability/generated/` must match a clean rebuild (no stale coverage/risk reports committed).

The CI gate is what makes the methodology *structural* rather than aspirational: you cannot merge a change that breaks traceability or smuggles a circularity.

## Open-problem tracking

Open problems have one source of truth and two derived surfaces:

1. **Canonical registry — `OPN-*` traceability claims** ([`../traceability/claims/`](../traceability/claims/)). Every open problem *exists* as a claim — versioned, citeable, Lean-linkable, audited. The claim's fields (`tier`, `role`, `epistemic_status`, `depends_on`, `risk_if_false`) carry the metadata.
2. **Registry view (generated)** — `build.py` emits [`../traceability/generated/open-problems.md`](../traceability/generated/open-problems.md) from the `OPN-*` claims. Never hand-edited; can't drift.
3. **Active subset (GitHub Issues)** — open an issue **only** for a problem currently being worked (e.g. in the running PI), not one-per-claim-forever. An open `open-problem` issue therefore *means* "in active play."

**Issue ↔ claim convention.** An open-problem issue body carries `Tracks: OPN-id`, and its labels **project** the claim's fields:

| Facet | Labels |
|---|---|
| Tier | `tier:1` · `tier:2` · `tier:3` |
| Kind | `open-problem` |
| Confidence | `conf:established` · `conf:argued` · `conf:conjectured` · `conf:open` |
| Salience | `gating` · `critical-path` |

Reconciliation is convention now (the `Tracks:` line); a `build.py` issue↔claim audit can be added later. Resolving a problem closes its issue and flips the claim's `proof_status`/`epistemic_status` (or adds a `verdict`), which the regenerated registry view reflects.

## Branch discipline

`main` is always green. Belt work happens on `feat/<task>` branches → PR → review against the methodology → merge. Paper edits on `paper/<topic>`. No force-push to `main`.

## Session lifecycle

A research session is bracketed by two scripts (mirrors thinx's session-start/wrap), so transitions carry repo housekeeping and hygiene rather than leaving loose ends:

- **`python3 0-program-methods/ops/research-start.py`** — read-only orientation briefing: VCS state, CI status, traceability health (claims / verified / acyclic), the active PI and its open issues, the open-problem registry + active subset, the appraisal verdict, figure/reference residuals, and the last session journal's carry-forward. Run it first thing.
- **`python3 0-program-methods/ops/research-wrap.py`** — end-of-session **gate** (nonzero exit on any FAIL): working tree clean, traceability passes + generated reports fresh, Lean core typechecks, GitHub-safe LaTeX (no `\operatorname`), no build artifacts tracked; surfaces figure/reference residuals and reminds to append a session journal. **Don't claim a session done while it FAILs.**

After a green wrap: append a [session journal](sessions/) entry and update memory / the [appraisal](../3-prediction/appraisal.md) as needed.
