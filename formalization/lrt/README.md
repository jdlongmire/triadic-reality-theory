# LRT Formal Core (sub-project) — import plan

Logic Realism Theory (LRT) is the layer of the program that formalizes TRT's *L₃* constituent: **TRT → LRT → LRM → predictions**. Its verified Lean 4 derivation chain (X → … → Schrödinger; Born rule via Gleason, unitarity via Stone, energy/action via Noether) is the formal backbone TRT builds on.

This directory hosts a **curated import** of that core — the Lean formalization and its traceability claims only. The baggage of the standalone LRT repo (chatbot, archive, Jekyll docs, prior theory versions) is deliberately **left behind**.

## Status: PLANNED (stage 2)

Not yet vendored. The vendoring step:

1. Copy the LRT `formalization/LrtFormalization/` derivation chain into `lrt/LrtFormalization/`.
2. Wire it as a second `lean_lib` (or path `require`) in the parent [`../lakefile.toml`](../lakefile.toml); the toolchain is already matched (`v4.28.0` / Mathlib `v4.28.0`).
3. `lake exe cache get && lake build` to confirm green (the heavy Mathlib step).
4. Import the relevant LRT traceability claims (ONT/LOG/ACT/QM/PHY/EXT) into [`../../traceability/claims/`](../../traceability/claims/), tagged `role: imported`, `proof_status: verified`, with provenance to LRT.
5. TRT's `Core`/`Belt` import LRT symbols for the *L₃* constituent rather than re-proving them.

## Provenance

Origin: `jdlongmire/logic-realism-theory` — `formalization/` (Lean 4, Mathlib `v4.28.0`; at import time: 19 axioms, 3 technical sorries, build green). The standalone repo is untouched by this import; whether it is eventually deprecated in favor of this hosted core is a later decision.
