#!/usr/bin/env python3
"""Offline tests for research_records.py and reproduce.py.

Builds throwaway git repositories to test that preregistration is proved from
history. Run: python3 0-program-methods/ops/test_research_records.py
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import reproduce as rp  # noqa: E402
import research_records as rr  # noqa: E402

NB = "area/notebooks/NB-20261120-test.md"


def nb(status="open", pre="pending", hypothesis="H holds.", failure="F is observed.", result="",
       confidence="", red_team="not_required", provenance="original", extra=""):
    return f"""---
id: NB-20261120-test
title: Test
status: {status}
opened: 2026-11-20
owners:
  - {{name: tester, kind: human}}
provenance: {provenance}
claims: [ABC-001]
work_package: n/a
hypothesis: {hypothesis}
failure_condition: {failure}
preregistered_commit: {pre}
method: Compute it.
sources:
  - {{ref: "Someone (2020) Paper.", verification: primary_abstract}}
computations: []
circularity_check: "{'no fitted parameters' if status != 'open' else ''}"
result: "{result}"
confidence: "{confidence}"
red_team: {red_team}
{extra}---

## Log
"""


class Repo:
    def __init__(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.git("init", "-q", "-b", "main")
        self.write("traceability/claims/ABC-001.yaml", "id: ABC-001\n")
        self.write(rr.REGISTRY, "computations: []\n")
        self.write(rr.LEAN_LOG, "| Date | Formalization tree | Commit | Toolchain | Command | Sorry | Axioms | Result | Verifier | Evidence |\n|---|---|---|---|---|---|---|---|---|---|\n")
        self.write("formalization/A.lean", "theorem t : True := trivial\n")
        self.commit("base")

    def git(self, *a):
        r = subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *a], cwd=self.root,
                           capture_output=True, text=True)
        assert r.returncode == 0, r.stderr
        return r.stdout.strip()

    def write(self, rel, text):
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")

    def commit(self, msg):
        self.git("add", "-A")
        self.git("commit", "-q", "-m", msg)
        return self.git("rev-parse", "HEAD")

    def check(self, pr_base=None):
        return rr.run(pr_base, self.root)


def errors_matching(errs, text):
    return [e for e in errs if text in e]


def test_open_pending_notebook_is_valid():
    r = Repo()
    r.write(NB, nb())
    r.commit("open")
    err, _ = r.check()
    assert err == [], err


def test_preregistration_proved_from_history():
    r = Repo()
    r.write(NB, nb())
    sha = r.commit("preregister")
    r.write(NB, nb(status="resolved_negative", pre=sha, result="F observed.", confidence="LOW"))
    r.commit("close")
    err, _ = r.check()
    assert err == [], err


def test_failure_condition_changed_after_preregistration():
    r = Repo()
    r.write(NB, nb())
    sha = r.commit("preregister")
    r.write(NB, nb(status="resolved_positive", pre=sha, failure="Something easier.", result="ok", confidence="LOW"))
    r.commit("close with moved goalposts")
    err, _ = r.check()
    assert errors_matching(err, "`failure_condition` changed after preregistration"), err


def test_result_present_at_preregistration_is_rejected():
    r = Repo()
    r.write(NB, nb(status="resolved_positive", result="already known", confidence="LOW"))
    sha = r.commit("result first")
    r.write(NB, nb(status="resolved_positive", pre=sha, result="already known", confidence="LOW"))
    r.commit("claim preregistration")
    err, _ = r.check()
    assert errors_matching(err, "a result was already present"), err


def test_unknown_commit_and_pending_on_closed():
    r = Repo()
    r.write(NB, nb(status="resolved_positive", pre="deadbeef", result="x", confidence="LOW"))
    r.commit("bad sha")
    assert errors_matching(r.check()[0], "not in this repository's history")
    r.write(NB, nb(status="resolved_positive", pre="pending", result="x", confidence="LOW"))
    r.commit("pending closed")
    assert errors_matching(r.check()[0], "still `pending` on a closed notebook")


def test_retroactive_rules():
    r = Repo()
    r.write(NB, nb(status="resolved_negative", pre="retroactive", result="x", confidence="HIGH",
                   red_team="requested 2026-11-21", extra="retroactive_reason: done before the standard\n"))
    r.commit("retro high")
    err, warn = r.check()
    assert errors_matching(err, "retroactive record may not carry HIGH"), err
    assert any("red-team pass requested" in w for w in warn)
    r.write(NB, nb(status="resolved_negative", pre="retroactive", result="x", confidence="MEDIUM",
                   red_team="requested 2026-11-21"))
    r.commit("retro without reason")
    assert errors_matching(r.check()[0], "needs `retroactive_reason`")


def test_closed_requirements_and_red_team():
    r = Repo()
    r.write(NB, nb(status="resolved_positive", pre="retroactive", result="", confidence="",
                   extra="retroactive_reason: x\n"))
    r.commit("closed without result")
    err = r.check()[0]
    assert errors_matching(err, "requires a result") and errors_matching(err, "needs confidence")
    r.write(NB, nb(status="resolved_positive", pre="retroactive", result="ok", confidence="MEDIUM",
                   extra="retroactive_reason: x\n"))
    r.commit("medium without red team")
    assert errors_matching(r.check()[0], "needs a red-team record or a stated waiver")
    r.write(NB, nb(status="resolved_positive", pre="retroactive", result="ok", confidence="MEDIUM",
                   red_team="'waived: replication by a second method'", extra="retroactive_reason: x\n"))
    r.commit("waived")
    assert r.check()[0] == []


def test_schema_errors():
    r = Repo()
    r.write(NB, nb(status="done").replace("claims: [ABC-001]", "claims: [ZZZ-999]"))
    r.commit("bad")
    err = r.check()[0]
    assert errors_matching(err, "status `done`") and errors_matching(err, "claim `ZZZ-999`")
    r.write(NB, "no front matter\n")
    r.commit("none")
    assert errors_matching(r.check()[0], "missing or unparsable YAML front matter")


def test_open_notebook_with_result_rejected():
    r = Repo()
    r.write(NB, nb(result="premature"))
    r.commit("x")
    assert errors_matching(r.check()[0], "an open notebook carries a result")


def test_lean_receipt_gate():
    r = Repo()
    base = r.git("rev-parse", "HEAD")
    r.write("docs/x.md", "doc\n")
    r.commit("no lean change")
    err, warn = r.check(pr_base=base)
    assert err == [] and any("no PASS Lean receipt" in w for w in warn)

    r.write("formalization/A.lean", "theorem t : True := by trivial\n")
    r.commit("lean change")
    assert errors_matching(r.check(pr_base=base)[0], "changes formalization/")

    tree = r.git("rev-parse", "HEAD:formalization")
    log = (r.root / rr.LEAN_LOG).read_text()
    r.write(rr.LEAN_LOG, log + f"| 2026-11-20 | {tree} | {r.git('rev-parse', 'HEAD')[:7]} | lean4:v4.28.0 | lake build | 0 | none | PASS | thinx-muse | ci |\n")
    r.commit("receipt")
    err, warn = r.check(pr_base=base)
    assert err == [] and not any("no PASS Lean receipt" in w for w in warn), (err, warn)


def test_receipt_names_each_proven_theorem():
    r = Repo()
    r.write("formalization/A.lean", "theorem my_theorem : True := by trivial\n")
    r.write("traceability/claims/ABC-001.yaml", "id: ABC-001\nformal_artifacts:\n  lean:\n"
            "    - { file: A.lean, symbol: my_theorem, status: proven, axioms: [] }\n")
    r.commit("claim and proof")
    tree = r.git("rev-parse", "HEAD:formalization")
    head = r.git("rev-parse", "HEAD")[:7]
    log = (r.root / rr.LEAN_LOG).read_text()
    r.write(rr.LEAN_LOG, log + f"| 2026-11-20 | {tree} | {head} | lean4:v4.28.0 | lake build | 0 | none (abbrev: my) | PASS | thinx-muse | ci |\n")
    r.commit("receipt without the name")
    assert any("`my_theorem` is not named in full" in w for w in r.check()[1])
    log = (r.root / rr.LEAN_LOG).read_text()
    r.write(rr.LEAN_LOG, log + f"| 2026-11-20 | {tree} | {head} | lean4:v4.28.0 | #print axioms my_theorem | 0 | none (my_theorem) | PASS | thinx-muse | ci |\n")
    r.commit("receipt naming it")
    assert not any("not named in full" in w for w in r.check()[1])


def test_lean_log_rows_validated():
    r = Repo()
    log = (r.root / rr.LEAN_LOG).read_text()
    r.write(rr.LEAN_LOG, log + "| 2026-11-20 | abc | 1234567 | t | c | 2 | none | PASS | v | e |\n| bad row |\n")
    r.commit("bad receipts")
    err = r.check()[0]
    assert errors_matching(err, "full 40-character hash") and errors_matching(err, "must record 0 sorry")
    assert errors_matching(err, "expected 10 columns")


def test_sessions_need_records_section():
    r = Repo()
    r.write(f"{rr.SESSIONS}/2026-11-16-old.md", "# old\n")
    r.write(f"{rr.SESSIONS}/2026-11-20-new.md", "# new\n")
    r.commit("sessions")
    err = r.check()[0]
    assert errors_matching(err, "2026-11-20-new.md") and not errors_matching(err, "2026-11-16-old.md")
    r.write(f"{rr.SESSIONS}/2026-11-20-new.md", "# new\n\n## Records\n\nnone\n")
    r.commit("fixed")
    assert r.check()[0] == []


def test_registry_validation():
    r = Repo()
    r.write(rr.REGISTRY, "computations:\n  - id: CMP-1\n    script: missing.py\n    claims: [ZZZ-1]\n    compare: []\n")
    r.commit("bad registry")
    err = r.check()[0]
    for text in ("bad id", "not found", "claim `ZZZ-1`", "reference_provenance", "at least one comparison"):
        assert errors_matching(err, text), (text, err)


def test_reproduce_comparators():
    assert rp.compare_json({"a": 1.0, "b": [1, 2]}, {"a": 1.0 + 1e-12, "b": [1, 2]}, 1e-9, 1e-12) == []
    assert rp.compare_json({"a": 1.0}, {"a": 1.001}, 1e-9, 1e-12)
    assert rp.compare_json({"a": 1}, {"a": 1, "b": 2}, 1e-9, 1e-12)
    assert rp.compare_json({"a": True}, {"a": 1}, 1e-9, 1e-12)
    ref = "SNR=4.35e-02 cell S1xB1 True\n"
    assert rp.compare_text("SNR=4.3500000000001e-02 cell  S1xB1 True\n", ref, 1e-9, 1e-12) == []
    assert rp.compare_text("SNR=4.36e-02 cell S1xB1 True\n", ref, 1e-9, 1e-12)
    assert rp.compare_text("SNR=4.35e-02 cell S1xB1 False\n", ref, 1e-9, 1e-12)


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    for t in tests:
        t()
    print(f"research records tests: {len(tests)} passed")
