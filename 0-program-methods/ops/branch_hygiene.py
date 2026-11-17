#!/usr/bin/env python3
"""branch_hygiene: audit branches and pull requests against the branch rules.

The rules are stated in 0-program-methods/github-workflow.md, section
"Branch discipline". This script checks the ones a machine can check:

  MERGED       a branch with no commits beyond the default branch still exists
  NO_PR        a branch has no open pull request
  STALE        a branch's tip is older than the inactivity limit, without a valid renewal
  NAME         a branch name does not follow <type>/<topic>
  PARKED_PR    an open pull request is being used as a parking marker
  CONFORMANCE  governing texts changed on the default branch after the branch's merge base

The audit is report-only. With --issue it maintains one rolling issue labelled
`branch-hygiene`: opened or updated while findings exist, closed when clean.

Usage:
  python3 0-program-methods/ops/branch_hygiene.py [--repo OWNER/NAME] [--issue] [--json]

Requires the GitHub CLI (`gh`) with read access; --issue also needs issue write access.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import urllib.parse
from typing import Callable

STALE_DAYS = 14
RENEWAL_MAX_DAYS = 30
BRANCH_TYPES = ("feat", "fix", "paper", "wp", "review", "rulings", "traceability", "formal", "docs", "ops", "ci")
NAME_RE = re.compile(r"^(" + "|".join(BRANCH_TYPES) + r")/[a-z0-9][a-z0-9._-]*$")
RENEWAL_RE = re.compile(r"^\s*Renewed until:\s*(\d{4}-\d{2}-\d{2})\s*;\s*reason:\s*(\S.*)$", re.I | re.M)
PARKED_RE = re.compile(r"\bparked\b", re.I)

# Texts whose change obliges open branches to be re-read before merge.
GOVERNING_FILES = (
    "1-hypothesis/hard-core.md",
    "0-program-methods/TRT-charter.md",
    "0-program-methods/TRT-objective.md",
    "0-program-methods/METHODOLOGY.md",
    "0-program-methods/TRT-FLL-PHYSICAL-MODEL.md",
    "traceability/schemas/claim.schema.yaml",
    "formalization/TrtFormalization/Core/Primitives.lean",
)
ISSUE_LABEL = "branch-hygiene"
PARKED_LABEL = "parked"
DOC = "0-program-methods/github-workflow.md#branch-discipline"


def is_governing(path: str) -> bool:
    if path in GOVERNING_FILES:
        return True
    if path.startswith("0-program-methods/sessions/"):
        name = path.rsplit("/", 1)[-1].lower()
        return "ruling" in name or "reconciliation" in name
    return False


# --------------------------------------------------------------------------- GitHub access

def gh_json(path: str, method: str = "GET", payload: dict | None = None):
    cmd = ["gh", "api", "-X", method, path]
    if payload is not None:
        cmd += ["--input", "-"]
    r = subprocess.run(cmd, input=json.dumps(payload) if payload is not None else None,
                       capture_output=True, text=True, timeout=90)
    if r.returncode != 0:
        raise RuntimeError(f"gh api {method} {path} failed: {(r.stderr or r.stdout).strip()}")
    return json.loads(r.stdout) if r.stdout.strip() else None


def gh_list(path: str) -> list:
    items, page = [], 1
    sep = "&" if "?" in path else "?"
    while True:
        batch = gh_json(f"{path}{sep}per_page=100&page={page}")
        items.extend(batch)
        if len(batch) < 100:
            return items
        page += 1


def q(name: str) -> str:
    return urllib.parse.quote(name, safe="")


def collect(repo: str, api: Callable = gh_json, lister: Callable = gh_list) -> dict:
    meta = api(f"repos/{repo}")
    default = meta["default_branch"]
    default_sha = api(f"repos/{repo}/branches/{q(default)}")["commit"]["sha"]
    branches = []
    for b in lister(f"repos/{repo}/branches"):
        name = b["name"]
        if name == default:
            continue
        info = api(f"repos/{repo}/branches/{q(name)}")
        cmp_ = api(f"repos/{repo}/compare/{q(default)}...{q(name)}")
        changed, truncated = [], False
        if cmp_["behind_by"] > 0:
            base = cmp_["merge_base_commit"]["sha"]
            drift = api(f"repos/{repo}/compare/{base}...{default_sha}")
            files = [f["filename"] for f in drift.get("files", [])]
            truncated = len(files) >= 300
            changed = sorted({f for f in files if is_governing(f)})
        branches.append({
            "name": name,
            "sha": info["commit"]["sha"],
            "date": info["commit"]["commit"]["committer"]["date"],
            "ahead_by": cmp_["ahead_by"],
            "behind_by": cmp_["behind_by"],
            "governing_changed": changed,
            "files_truncated": truncated,
        })
    prs = []
    for p in lister(f"repos/{repo}/pulls?state=open"):
        head_repo = (p.get("head") or {}).get("repo") or {}
        prs.append({
            "number": p["number"],
            "title": p.get("title") or "",
            "body": p.get("body") or "",
            "labels": [lb["name"] for lb in p.get("labels", [])],
            "draft": bool(p.get("draft")),
            "head_ref": p["head"]["ref"],
            "head_is_local": head_repo.get("full_name") == repo,
            "url": p.get("html_url", ""),
        })
    return {"repo": repo, "default_branch": default, "default_sha": default_sha,
            "branches": branches, "prs": prs}


# --------------------------------------------------------------------------- rules

def parse_iso(s: str) -> dt.datetime:
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))


def renewal_status(body: str, today: dt.date) -> tuple[bool, str]:
    """Return (valid, note) for a `Renewed until: YYYY-MM-DD; reason: ...` line."""
    m = RENEWAL_RE.search(body or "")
    if not m:
        return False, ""
    try:
        until = dt.date.fromisoformat(m.group(1))
    except ValueError:
        return False, "renewal date is malformed"
    if until < today:
        return False, f"renewal expired on {until}"
    if (until - today).days > RENEWAL_MAX_DAYS:
        return False, f"renewal to {until} exceeds the {RENEWAL_MAX_DAYS}-day maximum"
    return True, f"renewed until {until}"


def evaluate(data: dict, now: dt.datetime, stale_days: int = STALE_DAYS) -> list[dict]:
    today = now.date()
    findings: list[dict] = []

    def add(rule, subject, detail, remedy):
        findings.append({"rule": rule, "subject": subject, "detail": detail, "remedy": remedy})

    prs_by_head: dict[str, list[dict]] = {}
    for p in data["prs"]:
        if p["head_is_local"]:
            prs_by_head.setdefault(p["head_ref"], []).append(p)

    for b in sorted(data["branches"], key=lambda x: x["name"]):
        name = b["name"]
        subject = f"`{name}`"
        prs = prs_by_head.get(name, [])

        if b["ahead_by"] == 0:
            add("MERGED", subject, "no commits beyond the default branch",
                "delete the branch (its content is already on the default branch)")
            continue

        if not prs:
            add("NO_PR", subject, f"{b['ahead_by']} commit(s) ahead, no open pull request",
                "open a pull request (draft is fine), or tag `archive/<branch>` and delete")

        age = (now - parse_iso(b["date"])).days
        if age > stale_days:
            valid, note = False, ""
            for p in prs:
                valid, note = renewal_status(p["body"], today)
                if valid:
                    break
            if not valid:
                detail = f"last commit {age} days ago (limit {stale_days})"
                if note:
                    detail += f"; {note}"
                add("STALE", subject, detail,
                    "merge, or close with an `archive/<branch>` tag, or renew with a dated reason in the PR")

        if not NAME_RE.match(name):
            add("NAME", subject, "name does not follow `<type>/<topic>`",
                "rename to an allowed type: " + ", ".join(BRANCH_TYPES))

        if b["governing_changed"] or b["files_truncated"]:
            what = ", ".join(f"`{f}`" for f in b["governing_changed"]) or "drift too large to list"
            add("CONFORMANCE", subject, f"governing texts changed on the default branch since this branch's base: {what}",
                "update the branch from the default branch and conform or add a reconciliation note before merge")

    for p in sorted(data["prs"], key=lambda x: x["number"]):
        if PARKED_LABEL in p["labels"] or PARKED_RE.search(p["title"]):
            add("PARKED_PR", f"#{p['number']}", "open pull request used as a parking marker",
                f"move the idea to an issue labelled `{PARKED_LABEL}`, tag the branch, close the pull request")

    return findings


# --------------------------------------------------------------------------- report

def render(data: dict, findings: list[dict], now: dt.datetime) -> str:
    stamp = now.strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Branch hygiene audit",
        "",
        f"Audited `{data['repo']}` at {stamp}; default branch `{data['default_branch']}` at `{data['default_sha'][:7]}`.",
        f"Branches other than the default: {len(data['branches'])}. Open pull requests: {len(data['prs'])}.",
        f"Rules: [Branch discipline](https://github.com/{data['repo']}/blob/{data['default_branch']}/{DOC}).",
        "",
    ]
    if not findings:
        lines.append("No findings.")
        return "\n".join(lines) + "\n"
    lines += ["| Rule | Subject | Detail | Remedy |", "|---|---|---|---|"]
    for f in findings:
        cells = [f["rule"], f["subject"], f["detail"], f["remedy"]]
        lines.append("| " + " | ".join(c.replace("|", "\\|") for c in cells) + " |")
    lines += ["", "This issue is maintained by the branch hygiene workflow and closes itself when the audit is clean."]
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------- issue sync

def ensure_label(repo: str, name: str, color: str, description: str, api: Callable) -> None:
    try:
        api(f"repos/{repo}/labels/{q(name)}")
    except RuntimeError:
        api(f"repos/{repo}/labels", "POST", {"name": name, "color": color, "description": description})


def sync_issue(repo: str, findings: list[dict], body: str, now: dt.datetime,
               api: Callable = gh_json, lister: Callable = gh_list) -> str:
    ensure_label(repo, ISSUE_LABEL, "5319e7", "Rolling report from the branch hygiene audit", api)
    ensure_label(repo, PARKED_LABEL, "bfd4f2", "Idea recorded and deliberately not being worked", api)
    open_issues = [i for i in lister(f"repos/{repo}/issues?state=open&labels={ISSUE_LABEL}")
                   if "pull_request" not in i]
    current = open_issues[0] if open_issues else None
    if findings:
        title = f"Branch hygiene: {len(findings)} finding(s)"
        if current:
            api(f"repos/{repo}/issues/{current['number']}", "PATCH", {"title": title, "body": body})
            return f"updated issue #{current['number']}"
        made = api(f"repos/{repo}/issues", "POST", {"title": title, "body": body, "labels": [ISSUE_LABEL]})
        return f"opened issue #{made['number']}"
    if current:
        stamp = now.strftime("%Y-%m-%d %H:%M UTC")
        api(f"repos/{repo}/issues/{current['number']}/comments", "POST",
            {"body": f"Audit clean at {stamp}. Closing."})
        api(f"repos/{repo}/issues/{current['number']}", "PATCH", {"state": "closed", "state_reason": "completed"})
        return f"closed issue #{current['number']}"
    return "no issue needed"


# --------------------------------------------------------------------------- entry

def detect_repo() -> str:
    if os.environ.get("GITHUB_REPOSITORY"):
        return os.environ["GITHUB_REPOSITORY"]
    url = subprocess.run(["git", "remote", "get-url", "origin"], capture_output=True, text=True).stdout.strip()
    m = re.search(r"github\.com[:/]([^/]+/[^/.]+?)(?:\.git)?$", url)
    if not m:
        raise SystemExit("cannot determine repository; pass --repo OWNER/NAME")
    return m.group(1)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo", help="OWNER/NAME (default: GITHUB_REPOSITORY or the origin remote)")
    ap.add_argument("--issue", action="store_true", help="open, update, or close the rolling issue")
    ap.add_argument("--json", action="store_true", help="print findings as JSON instead of markdown")
    ap.add_argument("--stale-days", type=int, default=STALE_DAYS)
    a = ap.parse_args(argv)

    repo = a.repo or detect_repo()
    now = dt.datetime.now(dt.timezone.utc)
    data = collect(repo)
    findings = evaluate(data, now, a.stale_days)
    body = render(data, findings, now)
    print(json.dumps(findings, indent=2) if a.json else body)
    if a.issue:
        print(sync_issue(repo, findings, body, now), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
