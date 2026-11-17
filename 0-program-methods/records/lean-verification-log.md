# Lean verification log

Receipts for full Lean builds of `formalization/`. Rules: [research-records.md](../research-records.md), section 5.

**Verifier.** Lean verification is performed by thinx-muse, which holds the pinned Lean toolchain and the Mathlib cache. Other collaborators request it through the bridge, naming the pull request.

**When a receipt is required.** A pull request that changes anything under `formalization/` cannot merge until this table holds a PASS receipt for the formalization tree it would merge. CI enforces this (job *Research records*).

**How to record a receipt.**

1. Update the pull request branch from `main`, so the branch tree is the tree that will merge.
2. Compute the tree hash: `git rev-parse HEAD:formalization`. It changes only when `formalization/` changes, so adding a row to this file outside that directory leaves it intact.
3. Run the full build, `lake build` from `formalization/`, and `#print axioms` for every theorem a claim's `formal_artifacts` marks `proven`.
4. Append one row. A PASS row records 0 `sorry`. List the axioms reported, or `none`. Evidence is a link to the build log, CI run, or bridge message.
5. Commit the row to the same pull request.

A FAIL row is kept: it is the record that a build was attempted and failed.

| Date | Formalization tree | Commit | Toolchain | Command | Sorry | Axioms | Result | Verifier | Evidence |
|---|---|---|---|---|---|---|---|---|---|
