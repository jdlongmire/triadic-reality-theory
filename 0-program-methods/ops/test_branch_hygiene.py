#!/usr/bin/env python3
"""Offline tests for branch_hygiene.py. Run: python3 0-program-methods/ops/test_branch_hygiene.py"""
from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import branch_hygiene as bh  # noqa: E402

NOW = dt.datetime(2026, 11, 17, 12, 0, tzinfo=dt.timezone.utc)


def days_ago(n: int) -> str:
    return (NOW - dt.timedelta(days=n)).isoformat().replace("+00:00", "Z")


def branch(name, age=1, ahead=1, behind=0, governing=(), truncated=False):
    return {"name": name, "sha": "a" * 40, "date": days_ago(age), "ahead_by": ahead, "behind_by": behind,
            "governing_changed": list(governing), "files_truncated": truncated}


def pr(number, head, title="Work", body="", labels=(), local=True):
    return {"number": number, "title": title, "body": body, "labels": list(labels), "draft": False,
            "head_ref": head, "head_is_local": local, "url": ""}


def data(branches, prs):
    return {"repo": "o/r", "default_branch": "main", "default_sha": "b" * 40, "branches": branches, "prs": prs}


def rules(findings, subject=None):
    return sorted(f["rule"] for f in findings if subject is None or f["subject"] == subject)


def test_clean():
    d = data([branch("feat/x")], [pr(1, "feat/x")])
    assert bh.evaluate(d, NOW) == []


def test_no_pr():
    d = data([branch("feat/x")], [])
    assert rules(bh.evaluate(d, NOW)) == ["NO_PR"]


def test_fork_pr_does_not_cover_local_branch():
    d = data([branch("feat/x")], [pr(1, "feat/x", local=False)])
    assert rules(bh.evaluate(d, NOW)) == ["NO_PR"]


def test_merged_branch_reported_once():
    d = data([branch("work/old", age=90, ahead=0)], [])
    assert rules(bh.evaluate(d, NOW)) == ["MERGED"]


def test_stale_and_limit_boundary():
    assert rules(bh.evaluate(data([branch("feat/x", age=14)], [pr(1, "feat/x")]), NOW)) == []
    assert rules(bh.evaluate(data([branch("feat/x", age=15)], [pr(1, "feat/x")]), NOW)) == ["STALE"]


def test_valid_renewal_clears_stale():
    body = "Notes\nRenewed until: 2026-12-01; reason: waiting on review of the Lean bridge\n"
    assert rules(bh.evaluate(data([branch("feat/x", age=40)], [pr(1, "feat/x", body=body)]), NOW)) == []


def test_expired_or_long_renewal_does_not_clear_stale():
    expired = "Renewed until: 2026-11-01; reason: old"
    too_long = "Renewed until: 2027-03-01; reason: indefinite"
    no_reason = "Renewed until: 2026-12-01; reason: "
    for body in (expired, too_long, no_reason):
        f = bh.evaluate(data([branch("feat/x", age=40)], [pr(1, "feat/x", body=body)]), NOW)
        assert rules(f) == ["STALE"], body


def test_names():
    good = ["feat/a", "fix/pages-l3", "wp/next-steps-2026-11-12", "rulings/2026-11-16-x", "traceability/ont-002",
            "ops/branch-hygiene-guardrails", "review/struever.v2"]
    bad = ["work/wp-trt-x", "wp-trt-fd-0001-flexible-determinism", "feat/Upper", "feat/", "misc/x", "feat/a/b"]
    for n in good:
        assert bh.NAME_RE.match(n), n
    for n in bad:
        assert not bh.NAME_RE.match(n), n
    f = bh.evaluate(data([branch("work/x")], [pr(1, "work/x")]), NOW)
    assert rules(f) == ["NAME"]


def test_parked_pr_by_title_or_label():
    d = data([branch("ops/rfc")], [pr(2, "ops/rfc", title="RFC: console (parked)")])
    assert rules(bh.evaluate(d, NOW)) == ["PARKED_PR"]
    d = data([branch("ops/rfc")], [pr(2, "ops/rfc", labels=["parked"])])
    assert rules(bh.evaluate(d, NOW)) == ["PARKED_PR"]


def test_conformance():
    d = data([branch("feat/x", behind=40, governing=["0-program-methods/TRT-charter.md"])], [pr(1, "feat/x")])
    f = bh.evaluate(d, NOW)
    assert rules(f) == ["CONFORMANCE"] and "TRT-charter.md" in f[0]["detail"]
    d = data([branch("feat/x", behind=900, truncated=True)], [pr(1, "feat/x")])
    assert rules(bh.evaluate(d, NOW)) == ["CONFORMANCE"]


def test_is_governing():
    assert bh.is_governing("1-hypothesis/hard-core.md")
    assert bh.is_governing("0-program-methods/sessions/2026-11-16-reconciliation-rulings.md")
    assert bh.is_governing("0-program-methods/sessions/2026-11-12-charter-hardcore-reconciliation.md")
    assert not bh.is_governing("0-program-methods/sessions/2026-11-16-branch-consolidation.md")
    assert not bh.is_governing("docs/index.md")


def test_tonights_drift_is_caught():
    """The 2026-11-16 state, reconstructed: every problem found that night is reported."""
    d = data(
        [branch("wp-trt-fd-0001-flexible-determinism", age=44, behind=44, governing=["0-program-methods/TRT-charter.md"]),
         branch("work/wp-trt-found-0002-dynamic-stability", age=36),
         branch("feat/godel-modal-discriminator", age=45),
         branch("review/struever-line-audit-2026-11-11", age=5),
         branch("wp/next-steps-2026-11-12", age=4, ahead=0),
         branch("ops/research-console-proposal", age=144)],
        [pr(15, "wp-trt-fd-0001-flexible-determinism"),
         pr(16, "work/wp-trt-found-0002-dynamic-stability"),
         pr(2, "ops/research-console-proposal", title="RFC: Research Program Operations Console (parked)")])
    f = bh.evaluate(d, NOW)
    assert rules(f, "`wp-trt-fd-0001-flexible-determinism`") == ["CONFORMANCE", "NAME", "STALE"]
    assert rules(f, "`work/wp-trt-found-0002-dynamic-stability`") == ["NAME", "STALE"]
    assert rules(f, "`feat/godel-modal-discriminator`") == ["NO_PR", "STALE"]
    assert rules(f, "`review/struever-line-audit-2026-11-11`") == ["NO_PR"]
    assert rules(f, "`wp/next-steps-2026-11-12`") == ["MERGED"]
    assert rules(f, "`ops/research-console-proposal`") == ["STALE"]
    assert rules(f, "#2") == ["PARKED_PR"]


def test_render():
    d = data([branch("feat/x")], [])
    body = bh.render(d, bh.evaluate(d, NOW), NOW)
    assert "| NO_PR | `feat/x` |" in body
    assert bh.render(data([], []), [], NOW).rstrip().endswith("No findings.")


class FakeApi:
    def __init__(self, open_issues=(), labels=("branch-hygiene", "parked")):
        self.calls, self.open_issues, self.labels = [], list(open_issues), set(labels)

    def api(self, path, method="GET", payload=None):
        self.calls.append((method, path, payload))
        if method == "GET" and "/labels/" in path:
            if path.rsplit("/", 1)[-1] not in self.labels:
                raise RuntimeError("404")
            return {}
        if method == "POST" and path.endswith("/issues"):
            return {"number": 99}
        return {}

    def lister(self, path):
        return self.open_issues


def test_sync_opens_updates_closes():
    f = [{"rule": "NO_PR", "subject": "`feat/x`", "detail": "", "remedy": ""}]
    fake = FakeApi(labels=())
    assert bh.sync_issue("o/r", f, "body", NOW, fake.api, fake.lister) == "opened issue #99"
    assert ("POST", "repos/o/r/labels", {"name": "branch-hygiene", "color": "5319e7",
            "description": "Rolling report from the branch hygiene audit"}) in fake.calls

    fake = FakeApi(open_issues=[{"number": 7}])
    assert bh.sync_issue("o/r", f, "body", NOW, fake.api, fake.lister) == "updated issue #7"
    assert ("PATCH", "repos/o/r/issues/7", {"title": "Branch hygiene: 1 finding(s)", "body": "body"}) in fake.calls

    fake = FakeApi(open_issues=[{"number": 7}])
    assert bh.sync_issue("o/r", [], "body", NOW, fake.api, fake.lister) == "closed issue #7"
    assert ("PATCH", "repos/o/r/issues/7", {"state": "closed", "state_reason": "completed"}) in fake.calls

    fake = FakeApi()
    assert bh.sync_issue("o/r", [], "body", NOW, fake.api, fake.lister) == "no issue needed"

    fake = FakeApi(open_issues=[{"number": 5, "pull_request": {}}])
    assert bh.sync_issue("o/r", f, "body", NOW, fake.api, fake.lister) == "opened issue #99"


def test_collect_with_fake_api():
    responses = {
        "repos/o/r": {"default_branch": "main"},
        "repos/o/r/branches/main": {"commit": {"sha": "m" * 40}},
        "repos/o/r/branches/feat%2Fx": {"commit": {"sha": "x" * 40, "commit": {"committer": {"date": days_ago(3)}}}},
        "repos/o/r/compare/main...feat%2Fx": {"ahead_by": 2, "behind_by": 5, "merge_base_commit": {"sha": "base"}},
        "repos/o/r/compare/base..." + "m" * 40: {"files": [{"filename": "1-hypothesis/hard-core.md"},
                                                         {"filename": "docs/index.md"}]},
    }
    lists = {
        "repos/o/r/branches": [{"name": "main"}, {"name": "feat/x"}],
        "repos/o/r/pulls?state=open": [{"number": 3, "title": "t", "body": None, "labels": [], "draft": True,
                                        "head": {"ref": "feat/x", "repo": {"full_name": "o/r"}}, "html_url": "u"}],
    }
    d = bh.collect("o/r", api=lambda p, *a: responses[p], lister=lambda p: lists[p])
    assert d["branches"][0]["governing_changed"] == ["1-hypothesis/hard-core.md"]
    assert d["prs"][0]["head_is_local"] and d["prs"][0]["body"] == ""
    assert rules(bh.evaluate(d, NOW)) == ["CONFORMANCE"]


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    for t in tests:
        t()
    print(f"branch hygiene tests: {len(tests)} passed")
