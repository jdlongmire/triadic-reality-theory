#!/usr/bin/env python3
"""CHSH scenario: logical realism, counterfactual definiteness, and joint quantal measures.

Notebook: 2-theory/01-quantum/notebooks/NB-20261117-chsh-logical-realism-pr-box.md
Registered as CMP-007 (0-program-methods/records/computations.yaml).

Settings x, y in {0,1}; outcomes a, b in {0,1}. A counterfactual history is
alpha = (a0, a1, b0, b1), sixteen in all. The measured event for setting (x, y) and
outcome (a, b) is the cell E(ab|xy) = {alpha : a_x = a, b_y = b}; the four cells for one
setting partition the sixteen histories.

A joint quantal measure is a real symmetric (Hermitian) decoherence functional D on the
histories, with mu(E) = sum over alpha, beta in E of D[alpha, beta]. Each measured
partition is required to be decoherent (cross-cell block sums vanish), so its cell
measures are probabilities summing to one. D is strongly positive when it is positive
semidefinite.

Checks:
  1. PR box under per-run logical realism (LR1 to LR3) and no-signaling.
  2. Global counterfactual definiteness: maximum S over deterministic assignments.
  3. A decoherence functional reproducing the PR box: exists? positive semidefinite?
  4. Strongly positive functionals: an explicit quantum construction reaching 2 sqrt(2).
  5. Strongly positive functionals: constrained search for S above 2 sqrt(2).

Deterministic: no fitted parameters, fixed seeds. Printed values are rounded so that the
reference transcript is stable across platforms.
"""
from __future__ import annotations

import itertools
import math

import numpy as np
from scipy.optimize import minimize

HIST = list(itertools.product((0, 1), repeat=4))  # (a0, a1, b0, b1)
SETTINGS = [(x, y) for x in (0, 1) for y in (0, 1)]
OUTCOMES = [(a, b) for a in (0, 1) for b in (0, 1)]
TSIRELSON = 2 * math.sqrt(2)


def cell(x: int, y: int, a: int, b: int) -> np.ndarray:
    """Indicator vector of E(ab|xy) over the sixteen histories."""
    return np.array([1.0 if (h[x] == a and h[2 + y] == b) else 0.0 for h in HIST])


CELLS = {(x, y, a, b): cell(x, y, a, b) for (x, y) in SETTINGS for (a, b) in OUTCOMES}


def chsh(p: dict) -> float:
    """S = E00 + E01 + E10 - E11 from p[(x, y, a, b)]."""
    s = 0.0
    for x, y in SETTINGS:
        e = sum((-1) ** (a ^ b) * p[(x, y, a, b)] for a, b in OUTCOMES)
        s += (-1) ** (x * y) * e
    return s


def pr_box() -> dict:
    return {(x, y, a, b): (0.5 if (a ^ b) == (x * y) else 0.0) for (x, y) in SETTINGS for (a, b) in OUTCOMES}


def probs_from_D(D: np.ndarray) -> dict:
    return {k: float(v @ D @ v) for k, v in CELLS.items()}


def decoherence_residual(D: np.ndarray) -> float:
    worst = 0.0
    for x, y in SETTINGS:
        for (a, b), (a2, b2) in itertools.combinations(OUTCOMES, 2):
            worst = max(worst, abs(CELLS[(x, y, a, b)] @ D @ CELLS[(x, y, a2, b2)]))
    return worst


def fmt(v: float, nd: int = 6) -> str:
    r = round(v, nd)
    return f"{0.0 if r == 0 else r:.{nd}f}"


# --------------------------------------------------------------------------- check 1

def check_pr_box_logical_realism() -> None:
    p = pr_box()
    print("1. PR box under per-run logical realism (LR1-LR3) and no-signaling")
    # LR1: every actualized record is a bivalent value; LR2: each run's two records form one
    # consistent pair. Under the PR box each run yields a definite (a, b) with a XOR b = xy.
    runs_ok = all(p[(x, y, a, b)] in (0.0, 0.5) for (x, y) in SETTINGS for (a, b) in OUTCOMES)
    norm_ok = all(abs(sum(p[(x, y, a, b)] for a, b in OUTCOMES) - 1) < 1e-12 for x, y in SETTINGS)
    # no-signaling: Alice's marginal independent of y, Bob's independent of x
    ns = max(
        max(abs(sum(p[(x, 0, a, b)] for b in (0, 1)) - sum(p[(x, 1, a, b)] for b in (0, 1)))
            for x in (0, 1) for a in (0, 1)),
        max(abs(sum(p[(0, y, a, b)] for a in (0, 1)) - sum(p[(1, y, a, b)] for a in (0, 1)))
            for y in (0, 1) for b in (0, 1)),
    )
    print(f"   each run yields one definite bivalent record pair: {runs_ok}; normalized: {norm_ok}")
    print(f"   no-signaling violation: {fmt(ns)}")
    print(f"   S = {fmt(chsh(p))}  (Bell-local 2, Tsirelson {fmt(TSIRELSON)}, no-signaling max 4)")


# --------------------------------------------------------------------------- check 2

def check_counterfactual_definiteness() -> None:
    best = -9.0
    for h in HIST:
        p = {(x, y, a, b): 1.0 if (h[x] == a and h[2 + y] == b) else 0.0
             for (x, y) in SETTINGS for (a, b) in OUTCOMES}
        best = max(best, chsh(p))
    print("2. Global counterfactual definiteness (one assignment to all four settings per run)")
    print(f"   maximum S over the 16 deterministic assignments = {fmt(best)}; mixtures cannot exceed it")


# --------------------------------------------------------------------------- check 3

def symmetric_basis():
    idx = [(i, j) for i in range(16) for j in range(i, 16)]
    return idx


def check_pr_box_quantal_measure() -> None:
    idx = symmetric_basis()
    rows, rhs = [], []

    def bilinear_row(u, v):
        # coefficient of D[i,j] (i <= j) in u^T D v for symmetric D
        r = np.zeros(len(idx))
        for k, (i, j) in enumerate(idx):
            r[k] = u[i] * v[j] + (u[j] * v[i] if i != j else 0.0)
        return r

    target = pr_box()
    for x, y in SETTINGS:
        for a, b in OUTCOMES:
            rows.append(bilinear_row(CELLS[(x, y, a, b)], CELLS[(x, y, a, b)]))
            rhs.append(target[(x, y, a, b)])
        for (a, b), (a2, b2) in itertools.combinations(OUTCOMES, 2):
            rows.append(bilinear_row(CELLS[(x, y, a, b)], CELLS[(x, y, a2, b2)]))
            rhs.append(0.0)
    A, bvec = np.array(rows), np.array(rhs)
    sol, *_ = np.linalg.lstsq(A, bvec, rcond=None)
    D = np.zeros((16, 16))
    for k, (i, j) in enumerate(idx):
        D[i, j] = D[j, i] = sol[k]
    resid = float(np.max(np.abs(A @ sol - bvec)))
    p = probs_from_D(D)
    eig = np.linalg.eigvalsh(D)
    rank = int(np.linalg.matrix_rank(A))
    print("3. A decoherence functional reproducing the PR box (real symmetric D, decoherent partitions)")
    print(f"   constraints {A.shape[0]}, unknowns {A.shape[1]}, constraint rank {rank}; "
          f"solution residual {fmt(resid)}")
    print(f"   reproduces the PR box: S = {fmt(chsh(p))}; decoherence residual {fmt(decoherence_residual(D))}")
    print(f"   minimum eigenvalue of the minimum-norm solution = {fmt(float(eig[0]))} "
          f"(negative: not strongly positive)")


# --------------------------------------------------------------------------- check 4

def projector(theta: float, outcome: int) -> np.ndarray:
    """Projector onto outcome of the spin observable cos(theta) Z + sin(theta) X (real)."""
    v = np.array([math.cos(theta / 2), math.sin(theta / 2)])
    if outcome == 1:
        v = np.array([-math.sin(theta / 2), math.cos(theta / 2)])
    return np.outer(v, v)


def check_quantum_construction() -> None:
    alice, bob = (0.0, math.pi / 2), (math.pi / 4, -math.pi / 4)
    psi = np.array([1.0, 0.0, 0.0, 1.0]) / math.sqrt(2)  # (|00> + |11>)/sqrt 2
    rho = np.outer(psi, psi)
    # class operator for a counterfactual history: ordered product of the projectors of both
    # settings on each wing; summing over the unmeasured setting's outcome collapses it.
    C = []
    for a0, a1, b0, b1 in HIST:
        CA = projector(alice[0], a0) @ projector(alice[1], a1)
        CB = projector(bob[0], b0) @ projector(bob[1], b1)
        C.append(np.kron(CA, CB))
    D = np.array([[float(np.trace(C[i] @ rho @ C[j].T)) for j in range(16)] for i in range(16)])
    p = probs_from_D(D)
    eig = np.linalg.eigvalsh((D + D.T) / 2)
    print("4. Strongly positive joint quantal measure from a Bell state (explicit construction)")
    print(f"   D = Tr(C_alpha rho C_beta^T): symmetry error {fmt(float(np.max(np.abs(D - D.T))))}, "
          f"minimum eigenvalue {fmt(float(eig[0]))} (non-negative: strongly positive)")
    print(f"   decoherence residual {fmt(decoherence_residual(D))}; S = {fmt(chsh(p))} = 2 sqrt(2)")


# --------------------------------------------------------------------------- check 5

def check_strongly_positive_search(seeds=range(8)) -> None:
    pairs = [(CELLS[(x, y, a, b)], CELLS[(x, y, a2, b2)]) for (x, y) in SETTINGS
             for (a, b), (a2, b2) in itertools.combinations(OUTCOMES, 2)]
    ones = np.ones(16)

    def unpack(z):
        G = z.reshape(16, 16)
        return G @ G.T

    def neg_s(z):
        return -chsh(probs_from_D(unpack(z)))

    cons = [{"type": "eq", "fun": (lambda z, u=u, v=v: u @ unpack(z) @ v)} for u, v in pairs]
    cons.append({"type": "eq", "fun": lambda z: ones @ unpack(z) @ ones - 1.0})
    best, best_dec = -9.0, None
    for s in seeds:
        rng = np.random.default_rng(s)
        z0 = rng.normal(size=256) / 16
        r = minimize(neg_s, z0, method="SLSQP", constraints=cons,
                     options={"maxiter": 2000, "ftol": 1e-12})
        D = unpack(r.x)
        if decoherence_residual(D) < 1e-7 and abs(ones @ D @ ones - 1) < 1e-7:
            val = -r.fun
            if val > best:
                best, best_dec = val, decoherence_residual(D)
    print("5. Strongly positive joint quantal measures: constrained search for S above 2 sqrt(2)")
    print(f"   D = G G^T (positive semidefinite by construction), {len(list(seeds))} seeds, SLSQP")
    print(f"   largest feasible S found = {fmt(best, 4)} (Tsirelson {fmt(TSIRELSON, 4)}); "
          f"exceeds Tsirelson + 1e-6: {best > TSIRELSON + 1e-6}")


def main() -> None:
    check_pr_box_logical_realism()
    check_counterfactual_definiteness()
    check_pr_box_quantal_measure()
    check_quantum_construction()
    check_strongly_positive_search()


if __name__ == "__main__":
    main()
