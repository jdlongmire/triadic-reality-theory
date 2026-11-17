# Research records

**Adopted:** 2026-11-17. **Applies to:** every research attempt begun on or after that date. Records made before it are legacy: they stay as they are and are converted to this standard when next touched.

This document says what the programme records, where, and in what form, so that any result can be traced from its claim to its preregistered test, its method, its sources, its computation or proof, its review, and the session that produced it. It implements [research-practices.md](research-practices.md) sections 1 to 8; that file states the norms and this one states the records that show they were kept.

## 1. The record system

| Record | What it holds | Where | Checked by |
|---|---|---|---|
| Session journal | One entry per working session: what was done, what was recorded, what carries forward | `0-program-methods/sessions/` | `research_records.py` (Records section) |
| Research notebook | One per research attempt: preregistered hypothesis and failure condition, method, sources, result, confidence, review | `notebooks/` beside the work it serves | `research_records.py` |
| Computation registry | Every computation a claim or notebook relies on, with its reference output | `0-program-methods/records/computations.yaml` | `reproduce.py` in CI |
| Lean verification log | Receipts for full Lean builds | `0-program-methods/records/lean-verification-log.md` | `research_records.py` in CI |
| Claim registry | Claims, dependencies, statuses, failure conditions | `traceability/claims/` | `traceability/scripts/build.py` in CI |
| Source verification | Verification state of every reference | `references/verification-status.md` | review |
| Reviews | Adversarial and external reviews with responses | `reviews/` | review |
| Appraisal log | Whether the programme is progressive or degenerating | `3-prediction/appraisal.md` | review |

## 2. Research notebooks

A notebook is the record of one attempt: a derivation, a computation, a formalization, a test against data, or an adversarial probe. One question per notebook. A new question, or a changed hypothesis or failure condition, is a new notebook.

**Location and name.** `notebooks/NB-YYYYMMDD-<slug>.md` inside the folder of the work it serves: a work package, a `2-theory/` or `3-prediction/` area, or a review. The date is the day it was opened.

**Template.** [templates/notebook-template.md](templates/notebook-template.md).

**Front matter.** Every field is required.

| Field | Content |
|---|---|
| `id` | the file name without `.md` |
| `title` | the question, in one line |
| `status` | `open`, `resolved_positive` (hypothesis survived its test), `resolved_negative` (hypothesis failed its test), `inconclusive`, or `abandoned` |
| `opened` | ISO date |
| `owners` | list of `{name, kind}` with `kind` `human` or `ai`; every contributor is named |
| `provenance` | `original`, or `reconstruction` when rebuilding work whose original record is lost |
| `claims` | claim IDs the attempt bears on, or `[]` |
| `work_package` | package ID, or a short statement of the owning context |
| `hypothesis` | what is being tested |
| `failure_condition` | what result would count against it, fixed before the attempt |
| `preregistered_commit` | the commit at which `hypothesis` and `failure_condition` were first recorded; `pending` until known; `retroactive` for a record written after the work |
| `method` | how the test is carried out, including choices made by the investigator |
| `sources` | list of `{ref, verification}` with `verification` one of `primary_fulltext`, `primary_abstract`, `secondary`, `unverified` |
| `computations` | registered computation IDs, or `[]` |
| `circularity_check` | the audit of research-practices section 6: dependency graph, self-reference, fitted parameters |
| `result` | empty while open; the outcome once closed (for `abandoned`, the reason) |
| `confidence` | `HIGH`, `MEDIUM`, `LOW`, or `UNCERTAIN` once closed |
| `red_team` | `not_required`, `requested YYYY-MM-DD`, `waived: <reason>`, or the path of the red-team record |

**Preregistration is proved from git, not asserted.** Commit the notebook first with `status: open`, the hypothesis, the failure condition, an empty result, and `preregistered_commit: pending`. Then set `preregistered_commit` to that commit's hash. The validator confirms that the commit is in the history of the branch, that the notebook existed there with the same hypothesis and failure condition, and that it held no result. Changing either field afterwards fails the check: the honest course is a new notebook.

**Retroactive records.** Work done before a notebook existed is recorded with `preregistered_commit: retroactive` and a `retroactive_reason`. A retroactive record cannot carry HIGH confidence, because its failure condition was chosen after the result was known.

**Closing.** A closed notebook carries a result, a confidence label, and a circularity check. A notebook closed at MEDIUM or HIGH confidence needs a red-team record or a stated waiver; `requested` is allowed and is reported until the review is done.

**The log.** Below the front matter, the notebook keeps a dated, append-only log. Entries are added and never rewritten; an error is corrected by a new entry that says what was wrong. Negative and abandoned results are recorded with the same care as positive ones.

**AI provenance.** Work produced by an AI collaborator is marked as such in `owners` and, where it reconstructs or paraphrases the programme lead's work, in `provenance`. A reconstruction is never cited as the original.

## 3. Session journal

Each working session, human or AI, adds one entry under `0-program-methods/sessions/` per the [journal convention](sessions/README.md). From 2026-11-17 every entry carries a `## Records` section listing the notebooks, computations, receipts, claims, and reviews it created or changed, or `none`.

## 4. Computation registry

Any computation a claim, notebook, or paper relies on is registered in `records/computations.yaml` with:

- the script, its arguments, and the claims it serves;
- its reference output: a committed result file (`json`) or a reference transcript (`stdout`);
- `reference_provenance`: who produced the reference, and how far it has been independently checked.

CI re-runs every registered computation on every push and pull request, in a temporary copy so the working tree is untouched, and compares numbers within a tolerance of 1e-9 relative or 1e-12 absolute and all other text exactly. A computation that does not reproduce fails CI. A reference captured from a fresh run is labelled a baseline: it proves the computation is stable from then on, and nothing about whether it is correct. Changing a reference is a recorded event in the owning notebook.

Library versions are pinned in CI. Unregistered code may exist for exploration, but no claim or notebook may rest on it.

## 5. Lean verification

Lean verification is performed by **thinx-muse**, which holds the pinned toolchain and the Mathlib cache.

- CI typechecks the Mathlib-free core files (`Core/Primitives.lean`, `Core/Irreducibility.lean`) on every change and rejects `sorry` and `admit` anywhere in `TrtFormalization/`.
- A full `lake build`, with `#print axioms` for every theorem that a claim marks `proven`, is recorded as a receipt in the [Lean verification log](records/lean-verification-log.md).
- A pull request that changes `formalization/` cannot merge without a PASS receipt for the tree it would merge. Request one from thinx-muse through the bridge, naming the pull request.
- A claim's `proof_status: verified` rests on a receipt. The current tree's receipt status is reported on every CI run.

## 6. Running the checks

```text
python3 0-program-methods/ops/research_records.py      # notebooks, registry, Lean log, sessions
python3 0-program-methods/ops/reproduce.py             # re-run registered computations
python3 0-program-methods/ops/test_research_records.py # offline tests of both
```

Human-Curated, AI-Enabled (HCAE)
