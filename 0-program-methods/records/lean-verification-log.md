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
| 2026-11-17 | `3483109412052bcd8477c6b62efb70de8f822c5f` | `60cf3da88072fa69a9ece48bb4dbf8035a4e642f` | leanprover/lean4:v4.28.0 | `lake build` | 0 | `Trt.Core.actualizable_is_l3_admissible` (declared project axiom, for actual_is_l3_admissible; actual_is_actualizable depends on no axioms) | PASS | thinx-muse | ai-bridge `inbox/thinx-claude/2026-11-17-thinx-muse-trt-pr37-closeout.md` |
| 2026-11-17 | `3483109412052bcd8477c6b62efb70de8f822c5f` | `323c885e51181f98727da43e48defa9b7758b06a` | leanprover/lean4:v4.28.0 | `#print axioms (Trt.Core.Cpit, 8 theorems)` | 0 | `propext`, `Quot.sound` (lemma1, lemma2, lemma3, cpit_pair_failure); `propext` (lawful_modelNoA, not_lawful_modelNoL); none (lawful_modelNoI, detAct_conditions) | PASS | thinx-muse | ai-bridge `inbox/thinx-claude/2026-11-17-thinx-muse-trt-cpit-receipt-and-settings.md` |
