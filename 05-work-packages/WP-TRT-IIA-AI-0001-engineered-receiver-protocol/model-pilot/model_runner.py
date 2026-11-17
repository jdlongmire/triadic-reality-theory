#!/usr/bin/env python3
"""Protocol 001 model-dependent runner. No provider SDK and no network dependency.
A receiver command reads one JSON request per line from stdin and returns one JSON
object per line with at least {"answer": "...", "confidence": 0..1}.
"""
from __future__ import annotations
import argparse,csv,hashlib,json,subprocess,time
from pathlib import Path
CONDS=("C0","C1","C2","C3","C4","C5")
def h(s): return hashlib.sha256(s.encode()).hexdigest()
def norm(s): return " ".join(str(s).strip().lower().split())
def instruction(c):
 return {
 "C0":"Answer from your existing state only. Give a concise answer and confidence 0..1.",
 "C1":"Use the supplied bounded evidence when relevant. Give a concise answer and confidence 0..1.",
 "C2":"Use only supplied evidence for factual claims. If evidence is insufficient, answer ABSTAIN. Give confidence 0..1.",
 "C3":"Use only supplied evidence. Verify your proposed answer against it, correct if needed, and answer ABSTAIN if unresolved. Give confidence 0..1.",
 "C4":"Use the supplied authoritative observation/validator result when present and reconcile your answer to it. Give confidence 0..1.",
 "C5":"Answer from your existing state only. Spend additional effort improving explanation and presentation, but do not use external evidence. Give confidence 0..1."}[c]
def request(t,c):
 evidence=t.get("corpus","") if c in ("C1","C2","C3","C4") else ""
 return {"task_id":t["task_id"],"condition":c,"instruction":instruction(c),"question":t["question"],"evidence":evidence}
def call(cmd,req):
 p=subprocess.run(cmd,input=json.dumps(req)+"\n",text=True,capture_output=True,check=True)
 lines=[x for x in p.stdout.splitlines() if x.strip()]
 if len(lines)!=1: raise RuntimeError("receiver must emit exactly one JSON object")
 o=json.loads(lines[0]); assert "answer" in o
 return o
def correctness(t,a):
 if not t["answerable"]: return int(norm(a)=="abstain")
 return int(norm(t["ground_truth"]) in norm(a))
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--tasks",required=True); ap.add_argument("--receiver",nargs="+",required=True); ap.add_argument("--model-id",required=True); ap.add_argument("--model-version",default="unspecified"); ap.add_argument("--out",required=True); a=ap.parse_args()
 tasks=json.loads(Path(a.tasks).read_text()); out=Path(a.out); (out/"raw").mkdir(parents=True,exist_ok=True); rows=[]
 for t in tasks:
  for c in CONDS:
   req=request(t,c); t0=time.perf_counter(); o=call(a.receiver,req); ans=str(o["answer"]); raw=json.dumps(o,ensure_ascii=False,indent=2)
   rp=f"raw/{t['task_id']}-{c}.json"; (out/rp).write_text(raw+"\n")
   abst=norm(ans)=="abstain"; ev=req["evidence"]; ok=correctness(t,ans)
   rows.append({"experiment_id":"TRT-IIA-P001-MODEL-001","task_id":t["task_id"],"task_family":t["task_family"],"condition":c,"model_id":a.model_id,"model_version":a.model_version,"prompt_hash":h(json.dumps(req,sort_keys=True)),"evidence_packet_id":h(ev) if ev else "","ground_truth_id":h(t["task_id"]+"|"+t["ground_truth"]),"sampling_config":o.get("sampling_config","receiver-declared"),"raw_output_path":rp,"answer_normalized":norm(ans),"correctness":ok,"unsupported_claim_count":"","contradicted_claim_count":0 if ok or abst else 1,"citation_count":"","citation_entailed_count":"","abstained":int(abst),"should_abstain":int(not t["answerable"]),"confidence_reported":o.get("confidence",""),"verifier_action":o.get("verifier_action",""),"corrected":o.get("corrected",""),"latency_ms":int((time.perf_counter()-t0)*1000),"input_tokens":o.get("input_tokens",""),"output_tokens":o.get("output_tokens",""),"notes":"claim-level support scoring pending"})
 with (out/"runs.csv").open("w",newline="") as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
 (out/"run-manifest.json").write_text(json.dumps({"experiment_id":"TRT-IIA-P001-MODEL-001","model_id":a.model_id,"model_version":a.model_version,"receiver_command":a.receiver,"task_manifest_sha256":h(Path(a.tasks).read_text()),"conditions":list(CONDS),"metaphysical_inference":"none"},indent=2)+"\n")
 print(f"wrote {len(rows)} rows to {out}")
if __name__=="__main__": main()
