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

Adopted 2026-11-17, after the 2026-11-16 consolidation found branches up to five months old, branches with no pull request, a pull request used as a parking marker, merged branches left standing, and pre-charter branches drifting from the governing texts. Each rule below answers one of those failures.

### Rules

1. **Main is protected.** Changes reach `main` only through a pull request whose required checks pass (traceability, Lean core typecheck, math lint) and whose branch is up to date with `main`. No force push to `main`, and `main` cannot be deleted.
2. **Merged branches are deleted.** The repository deletes head branches automatically on merge.
3. **One branch, one pull request, opened at first push.** A draft is fine. A branch without a pull request is a finding.
4. **Fourteen days without a commit ends a branch's free run.** It is then merged, closed with an archive tag (rule 8), or renewed by a line in the pull request body: `Renewed until: YYYY-MM-DD; reason: ...`, at most 30 days ahead. A renewal can be repeated; each one needs a fresh date and reason.
5. **Parked ideas live in issues.** Record a parked idea as an issue labelled `parked`. An open pull request is never a parking marker.
6. **Names follow `<type>/<topic>`.** The topic is lowercase letters, digits, `.`, `_`, `-`. Allowed types:

   | Type | Use |
   |---|---|
   | `feat` | belt work, formalization, computation |
   | `fix` | corrections to existing material |
   | `paper` | position-paper and manuscript edits |
   | `wp` | filing or updating work packages |
   | `review` | reviews and audits |
   | `rulings` | executing the programme lead's rulings |
   | `traceability` | claim registry changes |
   | `formal` | Lean-only changes |
   | `docs` | the Pages site and other documentation |
   | `ops` | operations scripts and repository process |
   | `ci` | workflow changes |

7. **Branches conform before merge.** When the hard core, charter, objective, methodology, FLL model, claim schema, Lean primitives, or a rulings or reconciliation record changes on `main`, every open branch based before that change is updated from `main` and conformed, or carries a reconciliation note, before it merges.
8. **Unmerged work is tagged before deletion.** To retire a branch whose commits are not on `main`: create the tag `archive/<branch>` at its tip, comment on its pull request with the tag and the reason, close the pull request, then delete the branch. Nothing unmerged is deleted without its tag.

### Enforcement

- **Repository settings** carry rules 1 and 2. They are set by the repository owner or the operations collaborator.
- **The branch hygiene audit** ([`ops/branch_hygiene.py`](ops/branch_hygiene.py), workflow [`branch-hygiene.yml`](../.github/workflows/branch-hygiene.yml)) checks rules 3 to 7 every Monday and on demand. It maintains one rolling issue labelled `branch-hygiene`, opened or updated while findings exist and closed when the audit is clean. It reports and never fails CI, so a stale branch cannot block unrelated work on `main`.
- **The session wrap** (`research-wrap.py`) fails while any branch lacks an open pull request or survives its merge, and warns on the other findings.
- **The pull request template** ([`.github/pull_request_template.md`](../.github/pull_request_template.md)) asks for owner, next action, the methodology checks, and the conformance check.

Run the audit locally with `python3 0-program-methods/ops/branch_hygiene.py`. Its rule tests run offline with `python3 0-program-methods/ops/test_branch_hygiene.py`.

## Session lifecycle

A research session is bracketed by two scripts (mirrors thinx's session-start/wrap), so transitions carry repo housekeeping and hygiene rather than leaving loose ends:

- **`python3 0-program-methods/ops/research-start.py`** — read-only orientation briefing: VCS state, CI status, traceability health (claims / verified / acyclic), the active PI and its open issues, the open-problem registry + active subset, the appraisal verdict, figure/reference residuals, and the last session journal's carry-forward. Run it first thing.
- **`python3 0-program-methods/ops/research-wrap.py`** — end-of-session **gate** (nonzero exit on any FAIL): working tree clean, every branch has an open PR and no merged branch survives, traceability passes + generated reports fresh, Lean core typechecks, GitHub-safe LaTeX (no `\operatorname`), no build artifacts tracked; surfaces figure/reference residuals and reminds to append a session journal. **Don't claim a session done while it FAILs.**

After a green wrap: append a [session journal](sessions/) entry and update memory / the [appraisal](../3-prediction/appraisal.md) as needed.
