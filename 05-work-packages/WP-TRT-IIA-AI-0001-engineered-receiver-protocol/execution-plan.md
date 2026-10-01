# Execution Plan — Protocol 001

Status: READY FOR IMPLEMENTATION
Date: 2026-10-01

## Phase A — deterministic pilot

Build a small reproducible pilot emphasizing machine-verifiable truth:
- arithmetic and formal logic;
- executable code behavior;
- closed-corpus factual extraction;
- unanswerable closed-corpus questions.

Purpose: validate harness, schema, evaluators, and condition isolation before using
open-domain factual tasks.

## Phase B — source-grounded factual pilot

Use a frozen authoritative corpus and construct answerable, distractor-rich, and
unanswerable questions. Compare C0-C5.

## Phase C — claim-level evaluation

Decompose generated answers into factual claims and classify support/truth separately.
Citation presence is not counted as support unless entailment is verified.

## Phase D — adversarial controls

Test:
- irrelevant but plausible evidence;
- conflicting evidence with declared authority hierarchy;
- fluent false premises in prompts;
- evidence omission;
- verifier disagreement.

## Phase E — analysis

Report paired deltas between conditions and preserve per-task results. Avoid
interpreting statistically significant differences as semantic or metaphysical
identity claims.

## Gate to broader experiment

Do not scale until:
- task generation is reproducible;
- validators pass unit tests;
- condition prompts differ only by declared intervention;
- data schema is complete;
- pilot failures can be traced from aggregate result to raw output.
