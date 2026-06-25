# GitHub Workflow — Agile-DevOps for a Research Programme

How the programme uses GitHub's tools as its operating spine. The principle: treat the research programme like a software product under agile-devops discipline, but keep the *unit of work* epistemic (a problemshift), not a feature.

## The mapping

| GitHub tool | Programme use |
|---|---|
| **Issues** | One per open task / conjecture / review. An issue states a *target*, a *prerequisite*, and a *failure condition* — an issue without a failure condition is not a research task but a hope. Labelled by tier (`tier:0–3`), by `role` (hard-core/belt/prediction), and by status. |
| **Milestones** | The [ROADMAP](ROADMAP.md) tiers (0.1, 1.1, 2.x, 3.1, 4.x). A milestone closes when its conjecture is *resolved* — confirmation **or** recorded refutation both count. |
| **Projects (board)** | Kanban over belt work: `Backlog → Formalizing → Computing → Under review → Resolved`. The board is the live view of the positive heuristic. |
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

## Branch discipline

`main` is always green. Belt work happens on `feat/<task>` branches → PR → review against the methodology → merge. Paper edits on `paper/<topic>`. No force-push to `main`.
