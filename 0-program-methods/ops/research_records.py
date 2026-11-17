#!/usr/bin/env python3
"""research_records: validate the programme's research records.

Rules: 0-program-methods/research-records.md. Checks:

  notebooks      every **/notebooks/NB-*.md has complete front matter, consistent status,
                 and a preregistration provable from git history
  computations   0-program-methods/records/computations.yaml is well formed
  lean log       0-program-methods/records/lean-verification-log.md rows are well formed
  lean receipt   with --pr-base SHA: a pull request that changes formalization/ needs a PASS
                 receipt for the formalization tree it would merge
  sessions       session notes dated 2026-11-17 or later carry a "## Records" section

Errors exit nonzero. Warnings are printed and do not fail.

Usage:
  python3 0-program-methods/ops/research_records.py [--pr-base SHA]
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = "0-program-methods/records/computations.yaml"
LEAN_LOG = "0-program-methods/records/lean-verification-log.md"
SESSIONS = "0-program-methods/sessions"
STANDARD_FROM = dt.date(2026, 11, 17)

STATUSES = {"open", "resolved_positive", "resolved_negative", "inconclusive", "abandoned"}
CLOSED = STATUSES - {"open"}
CONFIDENCE = {"HIGH", "MEDIUM", "LOW", "UNCERTAIN"}
OWNER_KINDS = {"human", "ai"}
SOURCE_LEVELS = {"primary_fulltext", "primary_abstract", "secondary", "unverified"}
PROVENANCE = {"original", "reconstruction"}
REQUIRED = ("id", "title", "status", "opened", "owners", "provenance", "claims", "work_package",
            "hypothesis", "failure_condition", "preregistered_commit", "method", "sources",
            "computations", "circularity_check", "result", "confidence", "red_team")
HEX = re.compile(r"^[0-9a-f]{7,40}$")
FULL_HEX = re.compile(r"^[0-9a-f]{40}$")


def git(*args: str, root: Path = ROOT) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)


def front_matter(text: str) -> dict | None:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    data = yaml.safe_load(m.group(1))
    return data if isinstance(data, dict) else None


def blank(v) -> bool:
    return v is None or (isinstance(v, str) and not v.strip()) or v == []


# --------------------------------------------------------------------------- notebooks

def check_notebook(rel: str, text: str, claims: set[str], cmp_ids: set[str], root: Path = ROOT,
                   ) -> tuple[list[str], list[str]]:
    err, warn = [], []
    fm = front_matter(text)
    if fm is None:
        return [f"{rel}: missing or unparsable YAML front matter"], []
    for k in REQUIRED:
        if k not in fm:
            err.append(f"{rel}: missing field `{k}`")
    if err:
        return err, warn

    stem = Path(rel).stem
    if fm["id"] != stem:
        err.append(f"{rel}: id `{fm['id']}` does not match file name `{stem}`")
    status = fm["status"]
    if status not in STATUSES:
        err.append(f"{rel}: status `{status}` not in {sorted(STATUSES)}")
    if fm["provenance"] not in PROVENANCE:
        err.append(f"{rel}: provenance `{fm['provenance']}` not in {sorted(PROVENANCE)}")
    try:
        dt.date.fromisoformat(str(fm["opened"]))
    except ValueError:
        err.append(f"{rel}: opened `{fm['opened']}` is not an ISO date")

    owners = fm["owners"] if isinstance(fm["owners"], list) else []
    if not owners or any(not isinstance(o, dict) or blank(o.get("name")) or o.get("kind") not in OWNER_KINDS
                         for o in owners):
        err.append(f"{rel}: owners must be a non-empty list of {{name, kind: human|ai}}")
    if fm["provenance"] == "reconstruction" and not any(o.get("kind") == "ai" for o in owners if isinstance(o, dict)):
        warn.append(f"{rel}: reconstruction with no AI owner listed; confirm who reconstructed it")

    for c in fm["claims"] or []:
        if c not in claims:
            err.append(f"{rel}: claim `{c}` is not in traceability/claims")
    for c in fm["computations"] or []:
        if c not in cmp_ids:
            err.append(f"{rel}: computation `{c}` is not registered in {REGISTRY}")
    for s in fm["sources"] or []:
        if not isinstance(s, dict) or blank(s.get("ref")) or s.get("verification") not in SOURCE_LEVELS:
            err.append(f"{rel}: each source needs {{ref, verification: {'|'.join(sorted(SOURCE_LEVELS))}}}")
            break

    for k in ("hypothesis", "failure_condition", "method"):
        if blank(fm[k]):
            err.append(f"{rel}: `{k}` is empty")

    closed = status in CLOSED
    if closed and blank(fm["result"]):
        err.append(f"{rel}: status `{status}` requires a result")
    if status == "open" and not blank(fm["result"]):
        err.append(f"{rel}: an open notebook carries a result; close it or move the result into the log")
    if closed and status != "abandoned":
        if fm["confidence"] not in CONFIDENCE:
            err.append(f"{rel}: closed notebook needs confidence in {sorted(CONFIDENCE)}")
        if blank(fm["circularity_check"]):
            err.append(f"{rel}: closed notebook needs a circularity_check")

    # Preregistration
    pre = str(fm["preregistered_commit"]).strip()
    if pre == "retroactive":
        if blank(fm.get("retroactive_reason")):
            err.append(f"{rel}: retroactive preregistration needs `retroactive_reason`")
        if fm["confidence"] == "HIGH":
            err.append(f"{rel}: a retroactive record may not carry HIGH confidence")
    elif pre == "pending":
        if closed:
            err.append(f"{rel}: preregistered_commit is still `pending` on a closed notebook")
    elif HEX.match(pre):
        err += check_preregistration(rel, fm, pre, root)
    else:
        err.append(f"{rel}: preregistered_commit must be a commit hash, `pending`, or `retroactive`")

    # Red team
    rt = str(fm["red_team"]).strip()
    rt_ok = (rt == "not_required" or rt.startswith("waived:") or re.match(r"^requested \d{4}-\d{2}-\d{2}$", rt)
             or (root / rt).exists())
    if not rt_ok:
        err.append(f"{rel}: red_team must be `not_required`, `requested YYYY-MM-DD`, `waived: <reason>`, or an existing path")
    if closed and fm["confidence"] in {"HIGH", "MEDIUM"} and rt == "not_required":
        err.append(f"{rel}: a closed notebook at {fm['confidence']} confidence needs a red-team record or a stated waiver")
    if rt.startswith("requested"):
        warn.append(f"{rel}: red-team pass {rt}, not yet done")
    return err, warn


def check_preregistration(rel: str, fm: dict, sha: str, root: Path) -> list[str]:
    if git("cat-file", "-e", f"{sha}^{{commit}}", root=root).returncode != 0:
        return [f"{rel}: preregistered_commit {sha} is not in this repository's history (shallow clone?)"]
    if git("merge-base", "--is-ancestor", sha, "HEAD", root=root).returncode != 0:
        return [f"{rel}: preregistered_commit {sha} is not an ancestor of HEAD"]
    shown = git("show", f"{sha}:{rel}", root=root)
    if shown.returncode != 0:
        return [f"{rel}: the notebook does not exist at preregistered_commit {sha}"]
    then = front_matter(shown.stdout) or {}
    out = []
    for k in ("hypothesis", "failure_condition"):
        if blank(then.get(k)):
            out.append(f"{rel}: `{k}` was empty at preregistered_commit {sha}")
        elif str(then.get(k)).strip() != str(fm[k]).strip():
            out.append(f"{rel}: `{k}` changed after preregistration at {sha}; open a new notebook or re-preregister")
    if not blank(then.get("result")):
        out.append(f"{rel}: a result was already present at preregistered_commit {sha}")
    return out


# --------------------------------------------------------------------------- registries

def check_registry(claims: set[str], root: Path = ROOT) -> tuple[list[str], set[str]]:
    err, ids = [], set()
    path = root / REGISTRY
    if not path.exists():
        return [f"{REGISTRY}: missing"], ids
    comps = (yaml.safe_load(path.read_text(encoding="utf-8")) or {}).get("computations") or []
    for c in comps:
        cid = c.get("id", "?")
        if not re.match(r"^CMP-\d{3}$", cid):
            err.append(f"{REGISTRY}: bad id `{cid}`")
        if cid in ids:
            err.append(f"{REGISTRY}: duplicate id `{cid}`")
        ids.add(cid)
        if not (root / str(c.get("script", ""))).is_file():
            err.append(f"{REGISTRY}: {cid}: script `{c.get('script')}` not found")
        for cl in c.get("claims") or []:
            if cl not in claims:
                err.append(f"{REGISTRY}: {cid}: claim `{cl}` not in traceability/claims")
        if blank(c.get("reference_provenance")):
            err.append(f"{REGISTRY}: {cid}: reference_provenance is required")
        if not c.get("compare"):
            err.append(f"{REGISTRY}: {cid}: at least one comparison is required")
        for cmp_ in c.get("compare") or []:
            if cmp_.get("kind") not in {"json", "stdout"}:
                err.append(f"{REGISTRY}: {cid}: comparison kind must be json or stdout")
            if not (root / str(cmp_.get("reference", ""))).is_file():
                err.append(f"{REGISTRY}: {cid}: reference `{cmp_.get('reference')}` not found")
        nb = c.get("notebook")
        if nb and not (root / nb).is_file():
            err.append(f"{REGISTRY}: {cid}: notebook `{nb}` not found")
    return err, ids


def lean_receipts(root: Path = ROOT) -> tuple[list[dict], list[str]]:
    path = root / LEAN_LOG
    if not path.exists():
        return [], [f"{LEAN_LOG}: missing"]
    rows, err = [], []
    in_table = False
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.startswith("| Date |"):
            in_table = True
            continue
        if not in_table or not line.startswith("|") or set(line) <= set("|- "):
            continue
        cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
        if len(cells) != 10:
            err.append(f"{LEAN_LOG}:{n}: expected 10 columns, found {len(cells)}")
            continue
        date, tree, commit, toolchain, command, sorry, axioms, result, verifier, evidence = cells
        try:
            dt.date.fromisoformat(date)
        except ValueError:
            err.append(f"{LEAN_LOG}:{n}: bad date `{date}`")
        if not FULL_HEX.match(tree):
            err.append(f"{LEAN_LOG}:{n}: tree must be a full 40-character hash")
        if not HEX.match(commit):
            err.append(f"{LEAN_LOG}:{n}: bad commit `{commit}`")
        if result not in {"PASS", "FAIL"}:
            err.append(f"{LEAN_LOG}:{n}: result must be PASS or FAIL")
        if result == "PASS" and sorry != "0":
            err.append(f"{LEAN_LOG}:{n}: a PASS receipt must record 0 sorry")
        if blank(verifier) or blank(toolchain) or blank(command) or blank(axioms):
            err.append(f"{LEAN_LOG}:{n}: toolchain, command, axioms, and verifier are required")
        rows.append({"tree": tree, "result": result, "line": n, "text": f"{command} {axioms}"})
    return rows, err


def formalization_tree(rev: str = "HEAD", root: Path = ROOT) -> str | None:
    r = git("rev-parse", f"{rev}:formalization", root=root)
    return r.stdout.strip() if r.returncode == 0 else None


def check_lean_receipt(pr_base: str | None, rows: list[dict], root: Path = ROOT) -> tuple[list[str], list[str]]:
    err, warn = [], []
    tree = formalization_tree("HEAD", root)
    passed = {r["tree"] for r in rows if r["result"] == "PASS"}
    if pr_base:
        if git("cat-file", "-e", f"{pr_base}^{{commit}}", root=root).returncode != 0:
            return [f"--pr-base {pr_base}: commit not available (checkout needs fetch-depth: 0)"], warn
        changed = git("diff", "--quiet", pr_base, "HEAD", "--", "formalization", root=root).returncode != 0
        if changed and tree not in passed:
            err.append(f"this pull request changes formalization/ and no PASS receipt exists for tree {tree}; "
                       f"request Lean verification from thinx-muse ({LEAN_LOG})")
    if tree and tree not in passed:
        warn.append(f"no PASS Lean receipt for the current formalization tree {tree}")
    return err, warn


def check_receipt_coverage(rows: list[dict], root: Path = ROOT) -> list[str]:
    """Each Lean theorem a claim marks proven should be named, in full, in a PASS receipt
    for the current formalization tree. Reported as a warning: receipts are free text."""
    import yaml
    tree = formalization_tree("HEAD", root)
    texts = [r["text"] for r in rows if r["result"] == "PASS" and r["tree"] == tree]
    warn = []
    for p in sorted((root / "traceability/claims").glob("*.yaml")):
        c = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        for a in (c.get("formal_artifacts") or {}).get("lean", []):
            sym = a.get("symbol", "")
            if a.get("status") == "proven" and not any(re.search(rf"(?<![\w.]){re.escape(sym)}(?!\w)", t) for t in texts):
                warn.append(f"{p.stem}: proven theorem `{sym}` is not named in full in a PASS receipt for the current "
                            f"formalization tree ({LEAN_LOG})")
    return warn


def check_sessions(root: Path = ROOT) -> list[str]:
    err = []
    for p in sorted((root / SESSIONS).glob("*.md")):
        m = re.match(r"^(\d{4}-\d{2}-\d{2})", p.name)
        if not m or dt.date.fromisoformat(m.group(1)) < STANDARD_FROM:
            continue
        if not re.search(r"^## Records\b", p.read_text(encoding="utf-8"), re.M):
            err.append(f"{SESSIONS}/{p.name}: session notes from {STANDARD_FROM} carry a `## Records` section")
    return err


# --------------------------------------------------------------------------- entry

def run(pr_base: str | None = None, root: Path = ROOT) -> tuple[list[str], list[str]]:
    claims = {p.stem for p in (root / "traceability/claims").glob("*.yaml")}
    err, warn = [], []
    reg_err, cmp_ids = check_registry(claims, root)
    err += reg_err
    notebooks = sorted(p for p in root.rglob("notebooks/NB-*.md") if ".git" not in p.parts)
    for p in notebooks:
        e, w = check_notebook(str(p.relative_to(root)), p.read_text(encoding="utf-8"), claims, cmp_ids, root)
        err += e
        warn += w
    rows, log_err = lean_receipts(root)
    err += log_err
    e, w = check_lean_receipt(pr_base, rows, root)
    err += e
    warn += w
    if tree_receipted := any(r["result"] == "PASS" and r["tree"] == formalization_tree("HEAD", root) for r in rows):
        warn += check_receipt_coverage(rows, root)
    err += check_sessions(root)
    run.summary = (f"research records: {len(notebooks)} notebook(s), {len(cmp_ids)} registered computation(s), "
                   f"{len(rows)} Lean receipt(s)")
    return err, warn


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--pr-base", help="base commit of a pull request, to apply the Lean receipt gate")
    a = ap.parse_args(argv)
    err, warn = run(a.pr_base or None)
    print(run.summary)
    for w in warn:
        print(f"WARN  {w}")
    for e in err:
        print(f"ERROR {e}")
    print("OK" if not err else f"{len(err)} error(s)")
    return 1 if err else 0


if __name__ == "__main__":
    raise SystemExit(main())
