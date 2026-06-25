# Co-Admissibility Formalization (Task 0.1)

> **Tier:** 2-theory (protective belt). **Lakatos role:** the gating belt-construction — the single highest-leverage task. Nothing discriminating is reachable without it (it is the root of the [dependency graph](../../0-program-methods/ROADMAP.md)). **Status:** OPEN. **Confidence a formalization exists:** UNCERTAIN — this is the make-or-break task.

## Target

Define co-admissibility as a criterion that takes a collection of physical constraints (channel structure, conserved quantities, coupling data) and computes a definite set of admissible structures, with **no free entanglement measure**.

> A criterion `C(constraints) → admissible set` that is well-defined, computable, and measure-independent.

## Prerequisite

None. This is the root.

## Failure condition (`risk_if_false`)

If no formalization can avoid reintroducing a free measure, or if every formalization reduces to the existing einselection optimization, the co-admissibility program collapses to re-description and **both physics conjectures lose their discriminating content** — the [decoherence conjecture](../../3-prediction/co-admissibility-conjecture.md) and the [gravity conjecture](../../3-prediction/gravity-linearity-test.md). Recording that negative result is itself a progressive resolution, not a failure of the program.

## Notes

The finite-graph attack on the gravity side ([`../03-gravity/relational-graph-test.md`](../03-gravity/relational-graph-test.md)) is part of formalizing the measure, and it reduced the question to the keystone: does *A* register obstruction (linear) or best-fit project (quadratic)? See [`actualization-resolution.md`](actualization-resolution.md). Co-admissibility may be more naturally a numerical/computational object than a Lean proof object; that is itself open (see [`../../formalization/README.md`](../../formalization/README.md)).
