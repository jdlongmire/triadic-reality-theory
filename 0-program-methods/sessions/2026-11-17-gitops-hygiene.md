# Session note, 2026-11-17: branch discipline adopted and enforced

## Occasion

After the 2026-11-16 consolidation brought the repository from ten branches and six open pull requests to `main` alone, JD directed that the repository be handled with proper GitOps hygiene from this point on, so that it cannot return to that state, and that the AI collaborator do as much of the work as possible.

## What the consolidation found

Branches up to five months old; pull requests six weeks to five months open with stale CI failures; branches with no pull request whose content had reached `main` by another route; a pull request kept open as a parking marker; merged branches left standing; pre-charter branches drifting from the governing texts; six different branch prefixes.

## What this change adds

- **Rules.** `github-workflow.md`, section Branch discipline, replaces the former two-line section with eight rules: protected `main`, automatic deletion on merge, one branch and one pull request opened at first push, a fourteen-day inactivity limit with dated renewal, parked ideas in issues, `<type>/<topic>` naming, conformance before merge, and archive tags before deletion.
- **Audit.** `ops/branch_hygiene.py` with offline tests, run every Monday and on demand by `.github/workflows/branch-hygiene.yml`. It maintains one rolling issue labelled `branch-hygiene` and never fails CI. One test reconstructs the 2026-11-16 state and confirms that every problem found that night is reported.
- **Session wrap.** `research-wrap.py` now fails while any branch lacks an open pull request or survives its merge.
- **Pull request template.** Owner, next action, methodology checks, conformance check, branch hygiene checks.
- **CONTRIBUTING.md** points to the rules.

## Defaults chosen

The inactivity limit is fourteen days, renewals at most thirty days ahead. The audit reports through an issue, so a stale branch cannot block unrelated work on `main`.

## Not done from the session

Rules 1 and 2 are repository settings. Settings writes are refused in the collaborator's session (HTTP 403), so branch protection on `main` and automatic deletion of merged branches are handed to thinx-muse through the bridge.

## Records

- Rules: `0-program-methods/github-workflow.md`, Branch discipline (PR #36).
- Audit: `0-program-methods/ops/branch_hygiene.py`, `test_branch_hygiene.py`, `.github/workflows/branch-hygiene.yml` (PR #36).
- Research-records standard, computation registry, Lean verification log, and the first notebook: see the follow-up pull request recorded in this note's Carry to next.
- No claims, labels, or proof statuses changed.

## Carry to next

- Confirmation from thinx-muse that the settings are applied, verified against the live repository.
- The first scheduled audit run.
- Research records and verification (follow-up PR, same day): `research-records.md`, `records/`, `ops/research_records.py`, `ops/reproduce.py`; Lean baseline receipt from thinx-muse.

Human-Curated, AI-Enabled (HCAE)
