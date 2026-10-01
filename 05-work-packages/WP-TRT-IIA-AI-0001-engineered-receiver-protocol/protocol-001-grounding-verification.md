# Protocol 001 — Grounding, Verification, and Truth Tracking

Status: DRAFT PREREGISTRATION
Date: 2026-10-01
Work package: WP-TRT-IIA-AI-0001

## Research question

For a fixed receiver/model and fixed question set, how do grounding and verification
interventions affect external correctness relative to linguistic/statistical
coherence?

## Hypotheses

H1. Retrieval grounding will reduce unsupported factual claims relative to an
ungrounded baseline when authoritative evidence is available.

H2. Independent verification will improve external correctness beyond answer-only
generation on tasks with machine-checkable or source-checkable truth conditions.

H3. Fluency/coherence scores can remain stable or improve without proportional
improvement in factual correctness.

H4. Confidence and truth will be imperfectly coupled; calibration interventions
should improve their relationship without making them identical.

These are empirical hypotheses about engineered systems, not metaphysical claims.

## Conditions

C0 BASELINE
Model answers from its internal learned state only.

C1 RETRIEVAL
Same model and prompts, with a bounded evidence packet retrieved from an approved
corpus.

C2 SOURCE-CONSTRAINED
C1 plus instruction that factual claims must be supported by supplied evidence and
unsupported claims should be withheld.

C3 VERIFY
C2 plus an independent verification pass that classifies claims as supported,
contradicted, or unresolved and permits correction.

C4 TOOL-OBSERVED
Where applicable, the receiver may query a deterministic or authoritative external
tool/state and must reconcile the answer with that observation.

C5 NEGATIVE CONTROL
Increase generation/reasoning budget or stylistic refinement without adding new
external evidence or verification. This tests whether apparent quality can improve
without truth tracking.

## Task families

1. Closed-corpus factual QA with authoritative source text.
2. Entity/attribute questions with time-stamped ground truth.
3. Arithmetic/logical tasks with deterministic validators.
4. Code behavior questions with executable tests.
5. Deliberately underdetermined questions requiring abstention.
6. Adversarial evidence packets containing relevant and irrelevant material.

No personal or sensitive data are required.

## Primary metrics

- Exact/semantic factual accuracy against fixed ground truth.
- Unsupported factual claim rate.
- Contradicted claim rate.
- Citation entailment: whether cited evidence supports the associated claim.
- Abstention precision and recall on unanswerable items.
- Correction gain from verifier intervention.
- Calibration error between expressed confidence and correctness.

## Secondary metrics

- Answer completeness.
- Fluency/coherence, measured separately from truth.
- Evidence utilization.
- Latency and computational cost.
- Failure-mode taxonomy.

## IIA mapping

I_S proxy:
  measurable dependence on available input/evidence and predictive structure.

C proxy:
  explicit representations/claims about the target domain.

T proxy:
  external correctness under a fixed validator or authoritative evidence.

K:
  NOT directly claimed. The experiment can measure warranted-output proxies but
  cannot by itself establish philosophical knowledge or consciousness.

N proxy:
  rule-governed inference performance under explicit logical or verification tests.

## Critical controls

- Same base model across paired conditions where technically possible.
- Fixed temperature/sampling settings within paired comparisons.
- Randomized task order.
- Ground truth frozen before model output is inspected.
- Evaluator separation from generator where practical.
- Human adjudication only for predeclared ambiguous cases.
- Report negative and null results.
- Do not use model self-confidence as ground truth.

## Disconfirmation conditions

The simple intervention hypotheses are weakened if grounding and verification do
not reproducibly improve truth metrics, or if apparent gains disappear under
controlled evaluator and leakage checks.

The IIA typed distinction is weakened as an empirical research heuristic if one
operational variable robustly and interchangeably predicts all proposed layers
without residual error or explanatory need. Such a result would not by itself settle
their philosophical identity.

## Required artifacts

- task-set manifest
- ground-truth manifest
- run configuration
- raw model outputs
- claim-level evaluator output
- aggregate metrics
- error taxonomy
- reproducibility instructions
- final interpretation with metaphysical claims explicitly separated
