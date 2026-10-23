#!/usr/bin/env python3
import json
from pathlib import Path
import pilot
tasks=json.loads(Path("tasks.json").read_text()); rows,claims=pilot.run(tasks)
assert len(rows)==len(tasks)*6
required={"experiment_id","task_id","task_family","condition","model_id","model_version","prompt_hash","evidence_packet_id","ground_truth_id","sampling_config","raw_output_path","answer_normalized","correctness","unsupported_claim_count","contradicted_claim_count","citation_count","citation_entailed_count","abstained","should_abstain","confidence_reported","verifier_action","corrected","latency_ms","input_tokens","output_tokens","notes"}
assert required==set(rows[0])
for r in rows:
  if r["task_family"] in ("closed_corpus","unanswerable_closed_corpus"):
    assert (r["evidence_packet_id"]=="") == (r["condition"] in ("C0","C5"))
for tid in {r["task_id"] for r in rows}:
  c0=next(r for r in rows if r["task_id"]==tid and r["condition"]=="C0"); c5=next(r for r in rows if r["task_id"]==tid and r["condition"]=="C5")
  assert c0["correctness"]==c5["correctness"]
for tid in ("C001","C002"):
  assert next(r for r in rows if r["task_id"]==tid and r["condition"]=="C0")["correctness"]==0
  assert next(r for r in rows if r["task_id"]==tid and r["condition"]=="C1")["correctness"]==1
print("Protocol 001 deterministic pilot tests: PASS")
