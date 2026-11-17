#!/usr/bin/env python3
"""research-wrap — end-of-session hygiene gate for the TRT research repo.

Mirrors thinx's session-wrap: a pass/fail gate run at the session transition.
Don't claim a session done if any check FAILs. Checks repo housekeeping and the
programme's specific hygiene (branch discipline, traceability acyclic + fresh,
Lean core green, GitHub-safe LaTeX, no stray build artifacts), and surfaces residuals.
The branch check fails the wrap if any branch lacks an open PR or survives its merge.

Usage:  python3 0-program-methods/ops/research-wrap.py
Exit code is nonzero if any gate check FAILs.
"""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
results = []  # (level, label, detail)


def run(cmd, shell=False):
    try:
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=120, shell=shell)
        return r.returncode, (r.stdout or "").strip(), (r.stderr or "").strip()
    except Exception as e:  # noqa: BLE001
        return 1, "", str(e)


def add(level, label, detail=""):
    results.append((level, label, detail))


def main():
    print("=" * 68)
    print("  TRT research-wrap  |  session hygiene gate")
    print("=" * 68)

    # 1. Working tree clean
    _, porc, _ = run(["git", "status", "--porcelain"])
    if porc:
        add("FAIL", "uncommitted changes", f"{len(porc.splitlines())} file(s) — commit before wrapping:\n    " +
            "\n    ".join(porc.splitlines()[:20]))
    else:
        add("PASS", "working tree clean")

    # 2. Unpushed commits
    _, ahead, _ = run(["git", "rev-list", "--count", "origin/main..HEAD"])
    if ahead.isdigit() and int(ahead):
        add("WARN", "unpushed commits", f"{ahead} commit(s) ahead of origin/main — push if intended")
    else:
        add("PASS", "synced with origin/main")

    # 2b. Branch hygiene (rules in github-workflow.md, "Branch discipline")
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import datetime as dt
        import branch_hygiene as bh
        repo = bh.detect_repo()
        findings = bh.evaluate(bh.collect(repo), dt.datetime.now(dt.timezone.utc))
        blocking = [f for f in findings if f["rule"] in ("NO_PR", "MERGED")]
        other = [f for f in findings if f["rule"] not in ("NO_PR", "MERGED")]
        fmt = lambda fs: "\n    " + "\n    ".join(f"{f['rule']}: {f['subject']}, {f['remedy']}" for f in fs)
        if blocking:
            add("FAIL", "branches without a PR, or merged and not deleted", fmt(blocking))
        if other:
            add("WARN", "branch hygiene findings", fmt(other))
        if not findings:
            add("PASS", "branch hygiene", "every branch has an open PR; nothing stale, misnamed, or parked")
    except Exception as e:  # noqa: BLE001
        add("WARN", "branch hygiene", f"audit unavailable ({str(e).splitlines()[0][:120]}); run branch_hygiene.py")

    # 3. Traceability: build passes + generated fresh
    rc, out, err = run(["python3", "traceability/scripts/build.py"])
    acyclic = "ACYCLIC" in (out + err)
    valid = "validation: OK" in (out + err)
    if rc == 0 and acyclic and valid:
        add("PASS", "traceability", "validation OK, dependency graph acyclic")
    else:
        add("FAIL", "traceability", f"build.py exit {rc}; acyclic={acyclic} valid={valid}")
    _, gen_dirty, _ = run(["git", "status", "--porcelain", "traceability/generated"])
    if gen_dirty:
        add("FAIL", "generated reports stale", "build.py changed traceability/generated — commit the refresh")
    else:
        add("PASS", "generated reports fresh")

    # 3b. Research records and reproducibility (research-records.md)
    rc, out, err = run([sys.executable, "0-program-methods/ops/research_records.py"])
    lines = [l for l in out.splitlines() if l.startswith(("ERROR", "WARN"))]
    if rc == 0:
        add("PASS", "research records valid", (out.splitlines() or [""])[0])
        warns = [l[6:] for l in lines if l.startswith("WARN")]
        if warns:
            add("WARN", "research records", "\n    " + "\n    ".join(warns[:10]))
    else:
        add("FAIL", "research records invalid", "\n    " + "\n    ".join(l for l in lines if l.startswith("ERROR"))[:2000])
    rc, out, err = run([sys.executable, "0-program-methods/ops/reproduce.py"])
    if rc == 0:
        add("PASS", "registered computations reproduce", (out.strip().splitlines() or [""])[-1])
    elif "ModuleNotFoundError" in (out + err):
        add("WARN", "reproducibility", "numpy/scipy unavailable here; CI re-runs the registry")
    else:
        add("FAIL", "a registered computation does not reproduce",
            "\n    " + "\n    ".join(l for l in out.splitlines() if l.startswith(("FAIL", "     ")))[:2000])

    # 4. Lean core typecheck (Mathlib-free)
    rc, out, err = run(". ~/.elan/env 2>/dev/null; lean formalization/TrtFormalization/Core/Primitives.lean", shell=True)
    if rc == 0:
        add("PASS", "Lean core typechecks", "Core/Primitives.lean, 0 errors")
    else:
        tail = (err or out).splitlines()[-3:]
        unavailable = "not found" in err
        add("WARN" if unavailable else "FAIL", "Lean core typecheck",
            "lean unavailable here; CI typechecks the core, and full builds are verified by thinx-muse "
            "(records/lean-verification-log.md)" if unavailable else "errors:\n    " + "\n    ".join(tail))

    # 5. GitHub-safe LaTeX (math-lint)
    rc, hits, _ = run(r"grep -rnF '\operatorname' --include='*.md' . | grep -v '/lrt/' | grep -v '`' || true", shell=True)
    if hits.strip():
        add("FAIL", "math-lint (\\operatorname)", "use \\mathrm:\n    " + "\n    ".join(hits.splitlines()[:10]))
    else:
        add("PASS", "math-lint", "no \\operatorname in committed math")

    # 6. No stray build artifacts staged/tracked
    _, lake_tracked, _ = run("git ls-files | grep -E '\\.lake/|/build/' || true", shell=True)
    if lake_tracked.strip():
        add("FAIL", "build artifacts tracked", lake_tracked.splitlines()[0] + " ... (should be gitignored)")
    else:
        add("PASS", "no build artifacts tracked")

    # --- Residuals (informational) ---
    rc, figs, _ = run(r"grep -rn --include='*.md' --exclude-dir=0-program-methods "
                      r"'^> \*\*\[FIGURE-PLACEHOLDER\]' . | wc -l", shell=True)
    nfig = int(figs) if figs.strip().isdigit() else 0
    add("INFO", "figure placeholders", f"{nfig} unresolved in papers (must be 0 before a v1.0 deposit)")
    vs = (ROOT / "references/verification-status.md")
    if vs.exists() and "Remaining" in vs.read_text():
        add("INFO", "references", "residual items remain (see verification-status.md)")

    # --- Session journal reminder ---
    sess = [s for s in (ROOT / "0-program-methods/sessions").glob("*.md") if s.name.lower() != "readme.md"]
    _, recent, _ = run("git log -1 --since='12 hours ago' --name-only --pretty=format: -- 0-program-methods/sessions || true", shell=True)
    if recent.strip():
        add("PASS", "session journal", "entry touched recently")
    else:
        add("WARN", "session journal", "append a session entry to 0-program-methods/sessions/ before wrapping")

    # --- Report ---
    print()
    icon = {"PASS": "✓", "WARN": "⚠", "FAIL": "✗", "INFO": "·"}
    for level, label, detail in results:
        print(f"  [{icon[level]}] {level:4} {label}" + (f" — {detail}" if detail else ""))

    fails = [r for r in results if r[0] == "FAIL"]
    warns = [r for r in results if r[0] == "WARN"]
    print("\n" + "=" * 68)
    if fails:
        print(f"  RESULT: FAIL — {len(fails)} blocking issue(s), {len(warns)} warning(s). Not wrapped.")
        print("=" * 68)
        return 1
    print(f"  RESULT: PASS — {len(warns)} warning(s). Safe to wrap.")
    print("  Then: append the session journal + update memory/appraisal as needed.")
    print("=" * 68)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
