# Experiment Data Schema

Status: ACTIVE
Date: 2026-10-01

## Unit of analysis

One row per task x condition x run.

Required fields:

```text
experiment_id
task_id
task_family
condition
model_id
model_version
prompt_hash
evidence_packet_id
ground_truth_id
sampling_config
raw_output_path
answer_normalized
correctness
unsupported_claim_count
contradicted_claim_count
citation_count
citation_entailed_count
abstained
should_abstain
confidence_reported
verifier_action
corrected
latency_ms
input_tokens
output_tokens
notes
```

## Claim-level child table

```text
experiment_id
task_id
condition
run_id
claim_id
claim_text
claim_type
support_status
truth_status
citation_id
citation_entailment
adjudication_method
```

## Metric definitions

factual_accuracy = correct tasks / answerable tasks

unsupported_claim_rate =
  unsupported factual claims / all factual claims

citation_entailment_rate =
  entailed citations / citations evaluated

abstention_precision =
  correct abstentions / all abstentions

abstention_recall =
  correct abstentions / tasks requiring abstention

correction_gain =
  post-verification accuracy - pre-verification accuracy

Calibration should use a declared proper scoring/calibration method rather than a
single informal confidence correlation.

## Provenance

Every run manifest must record model identifier/version, date/time, system prompt,
task-set commit, evaluator version, evidence corpus version, and code commit.
