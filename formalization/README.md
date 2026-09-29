# TRT Lean 4 Formalization

Lean 4 formalization of Triadic Reality Theory. The module namespaces mirror the [falsifiability tiers](../0-program-methods/METHODOLOGY.md): `Core ⇄ 1-hypothesis`, `Belt ⇄ 2-theory`, `Prediction ⇄ 3-prediction`.

## Status (2026-09-29)

| Metric | Value |
|--------|-------|
| **Core/Primitives.lean** | ✅ typechecks (Mathlib-free, standalone) |
| **Belt / Prediction** | scaffold only — derivations pending |
| **LRT sub-project** | planned import (see [`lrt/`](lrt/)) |
| **Toolchain** | `leanprover/lean4:v4.28.0` (matched to LRT for interop) |
| **Sorries** | 0 |

## Structure

\`\`\`
I∞ / R  --L₃ necessary filter-->  D / Actualizable  --A-->  X / χ
                    │
                    └── sufficiency of L₃ for D is NOT assumed

A = primitive non-temporal state transition/change.
Obtains = separate actuality predicate.
\`\`\`

Protective-belt work may refine the D-to-X bridge, co-admissibility, measurement, Born-rule, and gravity models without redefining the hard-core primitives.

The imported [LRT core](lrt/) supplies the verified formalization of the *L₃* constituent (LRT's X → Schrödinger chain), which TRT's `Core` and `Belt` import as needed.

## Traceability

Every Lean symbol that discharges a claim is linked from [`../traceability/`](../traceability/) via the claim's `formal_artifacts.lean` field (`file` + `symbol` + `status`).
