---
id: NB-YYYYMMDD-slug
title: The question, in one line
status: open
opened: YYYY-MM-DD
owners:
  - {name: Name, kind: human}
provenance: original
claims: []
work_package: WP-TRT-XXXX-0000 or the owning context
hypothesis: >
  What is being tested.
failure_condition: >
  What result would count against the hypothesis. Fixed before the attempt.
preregistered_commit: pending
method: >
  How the test is carried out, including every choice the investigator makes.
sources: []
#  - {ref: "Author (Year) Title. Venue.", verification: primary_fulltext}
computations: []
circularity_check: ""
result: ""
confidence: ""
red_team: not_required
---

# NB-YYYYMMDD-slug: the question

Copy this file to `notebooks/NB-YYYYMMDD-<slug>.md` beside the work it serves. Rules: `0-program-methods/research-records.md`.

1. Fill in the front matter down to `method`. Commit.
2. Set `preregistered_commit` to the hash of that commit. Commit.
3. Do the work. Record it in the log below as it happens.
4. Close: set `status`, `result`, `confidence`, `circularity_check`, and `red_team`.

## Log

Dated entries, newest last. Add; never rewrite. Correct an error with a new entry.

### YYYY-MM-DD

Opened.
