#!/usr/bin/env python3
"""reproduce: re-run every registered computation and compare it with its reference.

The registry is 0-program-methods/records/computations.yaml. Each computation's
script directory is copied to a temporary directory and run there, so a script
that writes its results beside itself never modifies the working tree. Outputs
are compared with their references numerically: numbers within a relative or
absolute tolerance, all other text exactly.

Usage:
  python3 0-program-methods/ops/reproduce.py [--only CMP-001,CMP-002] [--update-stdout-references]

Exit status is nonzero if any computation fails to run or to reproduce.
--update-stdout-references rewrites stdout references from a fresh run; use it
only when a change to a script is intended, and record the change in the
owning notebook.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "0-program-methods/records/computations.yaml"
NUM = re.compile(r"[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?")
DEFAULT_REL, DEFAULT_ABS = 1e-9, 1e-12


def close(a: float, b: float, rel: float, abs_: float) -> bool:
    if math.isnan(a) and math.isnan(b):
        return True
    return math.isclose(a, b, rel_tol=rel, abs_tol=abs_)


def compare_json(got, ref, rel, abs_, path="$") -> list[str]:
    if isinstance(ref, bool) or isinstance(got, bool):
        return [] if got is ref else [f"{path}: {got!r} != {ref!r}"]
    if isinstance(ref, (int, float)) and isinstance(got, (int, float)):
        return [] if close(float(got), float(ref), rel, abs_) else [f"{path}: {got!r} != {ref!r}"]
    if isinstance(ref, dict) and isinstance(got, dict):
        out = [f"{path}: keys differ: {sorted(set(got) ^ set(ref))}"] if set(got) != set(ref) else []
        for k in sorted(set(got) & set(ref)):
            out += compare_json(got[k], ref[k], rel, abs_, f"{path}.{k}")
        return out
    if isinstance(ref, list) and isinstance(got, list):
        if len(got) != len(ref):
            return [f"{path}: length {len(got)} != {len(ref)}"]
        out = []
        for i, (g, r) in enumerate(zip(got, ref)):
            out += compare_json(g, r, rel, abs_, f"{path}[{i}]")
        return out
    return [] if got == ref else [f"{path}: {got!r} != {ref!r}"]


def split_text(s: str) -> tuple[list[str], list[float]]:
    words = [" ".join(w.split()) for w in NUM.split(s)]
    return words, [float(x) for x in NUM.findall(s)]


def compare_text(got: str, ref: str, rel, abs_) -> list[str]:
    gw, gn = split_text(got)
    rw, rn = split_text(ref)
    if gw != rw:
        for i, (a, b) in enumerate(zip(gw, rw)):
            if a != b:
                return [f"text differs near segment {i}: {a[:60]!r} != {b[:60]!r}"]
        return [f"text differs in length ({len(gw)} vs {len(rw)} segments)"]
    bad = [f"number {i}: {a!r} != {b!r}" for i, (a, b) in enumerate(zip(gn, rn)) if not close(a, b, rel, abs_)]
    return bad[:10]


def load_registry() -> list[dict]:
    import yaml
    return yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))["computations"]


def run_one(c: dict, update_stdout: bool) -> list[str]:
    script = ROOT / c["script"]
    rel, abs_ = c.get("rel_tol", DEFAULT_REL), c.get("abs_tol", DEFAULT_ABS)
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp) / "code"
        shutil.copytree(script.parent, work)
        r = subprocess.run([sys.executable, "-I", str(work / script.name), *map(str, c.get("args", []))],
                           cwd=work, capture_output=True, text=True, timeout=c.get("timeout_s", 600))
        if r.returncode != 0:
            return [f"exit {r.returncode}: {(r.stderr or r.stdout).strip().splitlines()[-1:]}"]
        problems = []
        for cmp_ in c["compare"]:
            ref_path = ROOT / cmp_["reference"]
            if cmp_["kind"] == "json":
                got = json.loads((work / cmp_["produced"]).read_text(encoding="utf-8"))
                ref = json.loads(ref_path.read_text(encoding="utf-8"))
                problems += [f"{cmp_['produced']}: {p}" for p in compare_json(got, ref, rel, abs_)]
            elif cmp_["kind"] == "stdout":
                if update_stdout:
                    ref_path.write_text(r.stdout, encoding="utf-8")
                    continue
                problems += [f"stdout: {p}" for p in compare_text(r.stdout, ref_path.read_text(encoding="utf-8"), rel, abs_)]
            else:
                problems.append(f"unknown comparison kind {cmp_['kind']!r}")
        return problems


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--only", help="comma-separated computation ids")
    ap.add_argument("--update-stdout-references", action="store_true")
    a = ap.parse_args(argv)
    comps = load_registry()
    if a.only:
        wanted = set(a.only.split(","))
        comps = [c for c in comps if c["id"] in wanted]
    failed = 0
    for c in comps:
        try:
            problems = run_one(c, a.update_stdout_references)
        except Exception as e:  # noqa: BLE001
            problems = [f"{type(e).__name__}: {e}"]
        if problems:
            failed += 1
            print(f"FAIL {c['id']} {c['script']}")
            for p in problems[:10]:
                print(f"     {p}")
        else:
            print(f"OK   {c['id']} {c['script']}")
    print(f"reproduced {len(comps) - failed}/{len(comps)}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
