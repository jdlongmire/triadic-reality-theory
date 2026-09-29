# TRT Lean 4 Formalization

Lean 4 formalization of Triadic Reality Theory. Module namespaces mirror the programme tiers: `Core ⇄ 1-hypothesis`, `Belt ⇄ 2-theory`, and `Prediction ⇄ 3-prediction`.

## Status (2026-09-29)

| Metric | Value |
|---|---|
| **Core/Primitives.lean** | normalized under WP-TRT-CORE-0001 |
| **Belt / Prediction** | scaffold and active derivation work |
| **LRT sub-project** | imported at [`lrt/`](lrt/) |
| **Toolchain** | Lean 4 / Mathlib project tooling |
| **Core semantic rule** | L₃ necessity does not imply L₃ sufficiency for actualizability |

## Structure

```text
formalization/
├── TrtFormalization/
│   ├── Core/Primitives.lean
│   ├── Belt/
│   └── Prediction/
├── lrt/
├── scripts/
├── lakefile.toml
└── lean-toolchain
```

The normalized core contains:

- `Representable`: R / informational representability.
- `L3Admissible`: the necessary logical filter.
- `Actualizable`: D, intentionally independent from `L3Admissible`.
- `actualizable_is_l3_admissible`: the canonical warranted direction.
- `A`: primitive non-temporal state transition/change.
- `Obtains`: actuality predicate, deliberately distinct from A.
- `Actual` / `Chi`: X / χ.
- `OutcomeActual`: downstream measurement distinction.

## Canonical formal architecture

```text
I∞ / R  --L₃ necessary filter-->  D / Actualizable  --A-->  X / χ
```

The Lean core deliberately does **not** encode:

```text
L3Admissible r -> Actualizable r
```

because the sufficiency of L₃-coherence for metaphysical actualizability remains an open proof obligation.

Likewise, A is not defined as “whatever actualizes.” It is independently typed as a transition relation. This prevents the formalization from proving the necessity of A merely by definition.

## Building

The core is Mathlib-free and can be checked directly:

```bash
source ~/.elan/env
lean TrtFormalization/Core/Primitives.lean
```

For the project build:

```bash
cd formalization
./scripts/build.sh
```

## LRT relation

The imported [LRT core](lrt/) develops the L₃ constituent. TRT's broader formal burden is to preserve the distinctions among constraint, representability, transition, actualizability, and actuality while testing proposed bridges rather than encoding them as definitions.

## Traceability

Lean symbols that discharge or encode claims are linked from [`../traceability/`](../traceability/) through each claim's `formal_artifacts.lean` field.
