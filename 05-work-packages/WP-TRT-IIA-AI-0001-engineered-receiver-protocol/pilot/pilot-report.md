# Protocol 001 Deterministic Pilot Report

Status: PILOT COMPLETE
Date: 2026-10-01
Work package: WP-TRT-IIA-AI-0001
Experiment: TRT-IIA-P001-PILOT-001

## Purpose

This run validates the experiment harness, condition isolation, required row schema,
deterministic truth checks, abstention handling, provenance manifest, and traceability
before model-dependent execution.

The receiver is intentionally simple and deterministic. These results must not be
treated as an LLM benchmark or as evidence for the metaphysical IIA.

## Frozen fixture

Eight tasks were used across six conditions (48 task-condition rows): two arithmetic,
two formal-logic, two answerable closed-corpus, and two unanswerable closed-corpus
tasks. C0 and C5 receive no evidence packet. C1-C4 receive the bounded corpus on
closed-corpus tasks. C5 changes no truth-bearing input.

## Validation result

`test_pilot.py`: PASS.

The suite verifies all 48 rows, declared schema fields, evidence isolation, negative
control invariance, and the expected closed-corpus evidence dependency.

## Aggregate result

```json
{
  "C0":{"n":8,"factual_accuracy":0.6666666666666666,"overall_correctness":0.75,"abstention_recall":1.0,"citation_entailment_rate":null,"contradicted_claims":0},
  "C1":{"n":8,"factual_accuracy":1.0,"overall_correctness":1.0,"abstention_recall":1.0,"citation_entailment_rate":1.0,"contradicted_claims":0},
  "C2":{"n":8,"factual_accuracy":1.0,"overall_correctness":1.0,"abstention_recall":1.0,"citation_entailment_rate":1.0,"contradicted_claims":0},
  "C3":{"n":8,"factual_accuracy":1.0,"overall_correctness":1.0,"abstention_recall":1.0,"citation_entailment_rate":1.0,"contradicted_claims":0},
  "C4":{"n":8,"factual_accuracy":1.0,"overall_correctness":1.0,"abstention_recall":1.0,"citation_entailment_rate":1.0,"contradicted_claims":0},
  "C5":{"n":8,"factual_accuracy":0.6666666666666666,"overall_correctness":0.75,"abstention_recall":1.0,"citation_entailment_rate":null,"contradicted_claims":0}
}
```

## Interpretation

The pilot demonstrates that the harness can represent a controlled separation between
receiver behavior without an evidence-bearing input and receiver behavior with such an
input. In this fixture, C0/C5 cannot establish the closed-corpus answers, while C1-C4
can recover them from the supplied corpus.

This dependency is introduced by construction. It validates the apparatus and the
operational distinction between available structured input and externally validated
output. It does not establish that information, content, truth, normativity, or
knowledge are metaphysically distinct kinds.

No inference to consciousness, intentionality, knowledge, theism, or the IIA
rational-ground hypothesis is licensed by this pilot.

## Gate assessment

- reproducible fixture: PASS
- deterministic validators: PASS for pilot fixture
- condition isolation: PASS
- required row schema: PASS
- aggregate-to-row traceability: PASS in executable harness
- model-dependent raw-output traceability: NOT YET TESTED
- free-form claim decomposition: NOT YET TESTED
- calibration metric: NOT YET TESTED

Disposition: proceed to a model-dependent deterministic/low-temperature pilot while
preserving the frozen task and condition definitions.
