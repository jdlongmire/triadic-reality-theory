#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,json,re,time
from pathlib import Path
CONDITIONS=("C0","C1","C2","C3","C4","C5"); EXPERIMENT_ID="TRT-IIA-P001-PILOT-001"
def sha256_text(s): return hashlib.sha256(s.encode()).hexdigest()
def normalize(s): return " ".join(s.strip().lower().split())
def evidence_for(t,c): return t.get("corpus","") if c in ("C1","C2","C3","C4") else ""
def receiver(t,c):
    f=t["task_family"]; e=evidence_for(t,c)
    if f=="arithmetic":
        x=t["question"].removeprefix("What is ").rstrip("?")
        if not re.fullmatch(r"[0-9+\-*/(). ]+",x): return "ABSTAIN"
        v=eval(x,{"__builtins__":{}},{})
        return str(int(v) if v==int(v) else v)
    if f=="logic": return t["ground_truth"]
    if f in ("closed_corpus","unanswerable_closed_corpus"):
        if not e or not t["answerable"]: return "ABSTAIN"
        return t["ground_truth"] if normalize(t["ground_truth"]) in normalize(e) else "ABSTAIN"
    return "ABSTAIN"
def correct(t,a): return int(normalize(a)==("abstain" if not t["answerable"] else normalize(t["ground_truth"])))
def prompt(t,c):
    i={"C0":"internal state only","C1":"bounded evidence","C2":"evidence; withhold unsupported claims","C3":"evidence; verify and correct","C4":"deterministic observation/validator","C5":"extra presentation budget; no evidence"}[c]
    return i+"\nQUESTION: "+t["question"]+"\nEVIDENCE: "+evidence_for(t,c)
def run(tasks):
    rows=[]; claims=[]
    for t in tasks:
      for c in CONDITIONS:
        p=prompt(t,c); e=evidence_for(t,c); t0=time.perf_counter_ns(); a=receiver(t,c); ok=correct(t,a)
        abst=normalize(a)=="abstain"; cite=int(bool(e) and not abst); ent=int(bool(cite) and normalize(t["ground_truth"]) in normalize(e))
        rows.append({"experiment_id":EXPERIMENT_ID,"task_id":t["task_id"],"task_family":t["task_family"],"condition":c,
        "model_id":"deterministic-fixture-receiver","model_version":"1.0","prompt_hash":sha256_text(p),
        "evidence_packet_id":sha256_text(e) if e else "","ground_truth_id":sha256_text(t["task_id"]+"|"+t["ground_truth"]),
        "sampling_config":"deterministic","raw_output_path":f"raw/{t['task_id']}-{c}.txt","answer_normalized":normalize(a),
        "correctness":ok,"unsupported_claim_count":0,"contradicted_claim_count":0 if ok or abst else 1,
        "citation_count":cite,"citation_entailed_count":ent,"abstained":int(abst),"should_abstain":int(not t["answerable"]),
        "confidence_reported":"","verifier_action":("accept" if ok else "flag") if c=="C3" else "none","corrected":0,
        "latency_ms":(time.perf_counter_ns()-t0)//1000000,"input_tokens":"","output_tokens":"","notes":"deterministic harness pilot"})
        if not abst: claims.append({"experiment_id":EXPERIMENT_ID,"task_id":t["task_id"],"condition":c,"run_id":"001","claim_id":"1",
        "claim_text":a,"claim_type":"answer","support_status":"supported" if ent else ("validator" if t["task_family"] in ("arithmetic","logic") else "unresolved"),
        "truth_status":"true" if ok else "false","citation_id":"1" if cite else "","citation_entailment":ent if cite else "","adjudication_method":"deterministic"})
    return rows,claims
def write_csv(path,rows):
    with path.open("w",newline="",encoding="utf-8") as f:
      w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
def aggregate(rows):
    o={}
    for c in CONDITIONS:
      rs=[r for r in rows if r["condition"]==c]; ans=[r for r in rs if not r["should_abstain"]]; ar=[r for r in rs if r["should_abstain"]]
      o[c]={"n":len(rs),"factual_accuracy":sum(r["correctness"] for r in ans)/len(ans),"overall_correctness":sum(r["correctness"] for r in rs)/len(rs),
      "abstention_recall":sum(r["abstained"] and r["should_abstain"] for r in rs)/len(ar),
      "citation_entailment_rate":sum(r["citation_entailed_count"] for r in rs)/sum(r["citation_count"] for r in rs) if sum(r["citation_count"] for r in rs) else None,
      "contradicted_claims":sum(r["contradicted_claim_count"] for r in rs)}
    return o
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--tasks",default="tasks.json"); ap.add_argument("--out",default="results"); a=ap.parse_args()
    tp=Path(a.tasks); tasks=json.loads(tp.read_text()); out=Path(a.out); (out/"raw").mkdir(parents=True,exist_ok=True)
    rows,claims=run(tasks)
    for r in rows: (out/r["raw_output_path"]).write_text(r["answer_normalized"]+"\n")
    write_csv(out/"runs.csv",rows); write_csv(out/"claims.csv",claims); (out/"aggregate.json").write_text(json.dumps(aggregate(rows),indent=2)+"\n")
    (out/"run-manifest.json").write_text(json.dumps({"experiment_id":EXPERIMENT_ID,"receiver":"deterministic-fixture-receiver/1.0","conditions":list(CONDITIONS),
    "task_count":len(tasks),"task_manifest_sha256":sha256_text(tp.read_text()),"purpose":"Harness/schema/validator validation before model-dependent execution","metaphysical_inference":"none"},indent=2)+"\n")
    print(json.dumps(aggregate(rows),indent=2))
if __name__=="__main__": main()
