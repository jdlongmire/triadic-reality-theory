# TRT Lean 4 Formalization

Lean 4 formalization of Triadic Reality Theory. The module namespaces mirror the [falsifiability tiers](../0-program-methods/METHODOLOGY.md): `Core ⇄ 1-hypothesis`, `Belt ⇄ 2-theory`, `Prediction ⇄ 3-prediction`.

## Status (2026-06)

| Metric | Value |
|--------|-------|
| **Core/Primitives.lean** | ✅ typechecks (Mathlib-free, standalone) |
| **Belt / Prediction** | scaffold only — derivations pending |
| **LRT sub-project** | planned import (see [`lrt/`](lrt/)) |
| **Toolchain** | `leanprover/lean4:v4.28.0` (matched to LRT for interop) |
| **Sorries** | 0 |

## Structure

```
formalization/
├── TrtFormalization/
│   ├── Core/Primitives.lean    # ⇄ 1-hypothesis: Representable, L3Admissible, Admissible,
│   │                           #   Actual, Chi, OutcomeActual — the four-tier engine
│   ├── Belt/                    # ⇄ 2-theory: co-admissibility, Born rule, gravity reduction
│   └── Prediction/             # ⇄ 3-prediction: formal conjecture statements (where proof-shaped)
├── lrt/                        # vendored LRT formal core (sub-project) — see lrt/README.md
├── scripts/ { build.sh · clean.sh · update-mathlib.sh }
├── lakefile.toml · lean-toolchain
```

## Building

The `Core/` primitives are Mathlib-free and typecheck without a build:

```bash
source ~/.elan/env && lean TrtFormalization/Core/Primitives.lean
```

The full project (once belt derivations + the LRT core land) needs the Mathlib cache:

```bash
cd formalization && ./scripts/build.sh    # lake exe cache get && lake build
```

## Filesystem note

This repository lives on **ext4** (Macro-Drive-1TB), so — unlike the LRT origin repo on NTFS — **no `.lake` symlink to another mount is required.** `.lake/` stays in-repo and is gitignored.

## Derivation chain (planned)

```
L₃ + I∞  →  Admissible (I∞|L₃)  →  A: Admissible → Actual  →  χ
                                          ↓
        co-admissibility criterion (Belt)  →  Born rule (Belt)  →  predictions (Prediction)
                                          ↓
        gravity reduction (Belt): holonomy deficit → linear? → GR  /  quadratic? → modified gravity
```

The imported [LRT core](lrt/) supplies the verified formalization of the *L₃* constituent (LRT's X → Schrödinger chain), which TRT's `Core` and `Belt` import as needed.

## Traceability

Every Lean symbol that discharges a claim is linked from [`../traceability/`](../traceability/) via the claim's `formal_artifacts.lean` field (`file` + `symbol` + `status`).
