# Traceability

Full claim ↔ proof ↔ prose traceability — a first-class goal of the programme. This layer is the [Popper/Lakatos methodology](../0-strategy/METHODOLOGY.md) rendered machine-checkable.

## How it works

- **`claims/*.yaml`** — one file per claim, the source of truth. Each conforms to [`schemas/claim.schema.yaml`](schemas/claim.schema.yaml) and carries: `tier` (falsifiability ladder), `role` (Lakatos: primitive/bridge/derived/imported/prediction/open), `proof_status`, `epistemic_status` (confidence), a `depends_on` graph (kept **acyclic** — the circularity discipline), `risk_if_false` (failure condition), and — for predictions — `falsifies` (Popperian refutation condition). Lean and computational artifacts are linked via `formal_artifacts`.
- **`scripts/build.py`** — validates every claim, checks the dependency graph is acyclic, verifies linked Lean files exist, and regenerates the reports. Exits nonzero on failure (CI-ready).
- **`generated/`** — built artifacts (do not edit): `claims.json`, `coverage-report.md`, `dependency-graph.{mmd,json}`, `risk-report.md`.

## Rebuild

```bash
python3 traceability/scripts/build.py
```

## Claim id prefixes

`ONT` ontology · `LOG` logic · `ACT` actualization · `QM` quantum · `PHY` dynamics/gravity · `INT` interpretive · `PRD` prediction · `OPN` open · `EXT` imported.

Adapted from the LRT traceability schema; extended with a `tier` binding and a `computation` artifact type (TRT predictions are partly numerical, not only proof-theoretic).
