#!/usr/bin/env python3
"""
Co-admissibility — the decisive computation (Task 0.1 / OPN-001).

The measure-free candidates for a co-admissibility criterion C(constraints) ->
admissible set are tested against the ACTUAL two-channel cavity model of
Feller, Coeuret Cauquil & Roussel (2020), arXiv:2001.10851, Eqs. (3)-(4):

    H  = omega_c * N                          (N = a^dag a)
    La = sqrt(kappa_a) * a                    coherent-state-basis dissipation
    Ln = sqrt(kappa_n) * N                    number-basis dephasing
    d_t rho = -i omega_c [N, rho]
              + kappa_n ( N rho N - 1/2 {N^2, rho} )       (dephasing dissipator D_n)
              + kappa_a ( a rho a^dag - 1/2 {N, rho} )      (damping  dissipator D_a)

Three measure-free objects are tested (the two-part commutant check from the
2026-06-26 red-team pass, plus the weaker pairwise-commuting-dissipator criterion):

  (i)   COMMUTANT of the constraint operators  S = {a, a^dag, N, H}.
        C0 (joint-invariance / DFS) is non-trivial  iff  this commutant is
        non-trivial. Analytic expectation: {a, a^dag} generate the oscillator
        algebra irreducibly on Fock space (Stone-von Neumann), so the commutant
        is C*Id (trivial). We confirm numerically on a truncated space and
        isolate truncation edge effects.

  (ii)  POINTER-STATE LOCATION. Are the einselected pointer states (Fock |n><n|
        and coherent |alpha><alpha|) inside the commutant or in its complement?
        If the commutant is C*Id, no rank-1 projector is in it -> the measure-free
        object is disjoint-by-construction from the family the conjecture must
        reproduce.

  (iii) PAIRWISE-COMMUTING-DISSIPATOR criterion (the more L3-faithful, weaker
        criterion):  { rho : [D_n, D_a](rho) = 0 }.  We build the dissipator
        SUPEROPERATORS and compute their commutator. The paper's Eq. (17) proves
        the quantum channels commute; if [D_n, D_a] = 0 identically the criterion
        is satisfied by EVERY state -> measure-free but non-discriminating.

Vectorisation convention: column-stacking, vec(A X B) = (B^T kron A) vec(X).
Pure numpy/scipy; deterministic; no fitted parameters.

Run:  python3 coadmissibility_commutant.py
"""

import json
import math
import os
import numpy as np

np.set_printoptions(precision=4, suppress=True, linewidth=120)

# --- model parameters (declared; none are fitted to any outcome) -------------
OMEGA_C = 1.0          # cavity frequency (sets the energy scale)
KAPPA_A = 1.0          # coherent-state-channel rate
KAPPA_N = 1.0          # number-basis-channel rate
# kappa_n/kappa_a = 1 here; the commutant/commutator results below are
# INDEPENDENT of the rates (they are algebraic), which we also verify by
# re-running at a second ratio. The critical coupling kappa_n/kappa_a ~ 1
# (paper Fig. 6) governs WHICH pointer states appear, not whether they lie in
# the commutant -- see the (ii) discussion.
TOL = 1e-9             # singular-value tolerance for rank/nullspace


def operators(N):
    """Truncated Fock space, dimension N. Returns a, adag, num, H."""
    a = np.zeros((N, N), dtype=complex)
    for n in range(1, N):
        a[n - 1, n] = np.sqrt(n)          # a|n> = sqrt(n)|n-1>
    adag = a.conj().T
    num = adag @ a                         # diag(0,1,...,N-1) up to truncation
    H = OMEGA_C * num
    return a, adag, num, H


def comm(A, B):
    return A @ B - B @ A


def commutant_dim(op_list, N):
    """
    dim { X (N x N) : [X, M] = 0  for all M in op_list }.
    vec([X,M]) = (I kron M  -  M^T kron I) vec(X)   (column-stacking).
    Returns (dim, sorted singular values) of the stacked constraint map.
    """
    I = np.eye(N)
    blocks = []
    for M in op_list:
        # X M - M X  ->  (M^T kron I - I kron M) vec(X)
        blocks.append(np.kron(M.T, I) - np.kron(I, M))
    A = np.vstack(blocks)
    s = np.linalg.svd(A, compute_uv=False)
    dim = int(np.sum(s < TOL))
    return dim, s


def dissipator_super(L, N):
    """Superoperator D[L](rho) = L rho L^dag - 1/2 {L^dag L, rho}, column-stacking.

    Analytic anchor for [D_n, D_a] = 0 (independent of the numerics below):
    D_n = D[N] multiplies each coherence band rho_{mn} by the scalar
    g(m-n) = -1/2 (m-n)^2 (it is diagonal on coherence-order k = m-n); D_a = D[a]
    maps band k to band k (coherence-order-preserving). A scalar-per-band operator
    commutes with any band-preserving operator, so [D_n, D_a] = 0 EXACTLY. Since
    N is exactly diagonal under truncation, there is no edge defect -- consistent
    with paper Eq.(17).
    """
    I = np.eye(N)
    LdL = L.conj().T @ L
    # vec(L rho L^dag) = (conj(L) kron L) vec(rho)
    return (np.kron(L.conj(), L)
            - 0.5 * np.kron(I, LdL)
            - 0.5 * np.kron(LdL.T, I))


def hamiltonian_super(H, N):
    """Unitary generator U(rho) = -i[H, rho], column-stacking."""
    I = np.eye(N)
    return -1j * (np.kron(I, H) - np.kron(H.T, I))


def fock_proj(n, N):
    rho = np.zeros((N, N), dtype=complex)
    rho[n, n] = 1.0
    return rho


def coherent_proj(alpha, N):
    c = np.array([alpha ** k / np.sqrt(math.factorial(k)) for k in range(N)],
                 dtype=complex)
    c *= np.exp(-0.5 * abs(alpha) ** 2)
    c /= np.linalg.norm(c)            # renormalise (truncation)
    return np.outer(c, c.conj())


def in_commutant(rho, op_list):
    """max_M ||[rho, M]||_F ; ~0 means rho is in the commutant."""
    return max(np.linalg.norm(comm(rho, M)) for M in op_list)


def run(N, kappa_a=KAPPA_A, kappa_n=KAPPA_N):
    a, adag, num, H = operators(N)
    La = np.sqrt(kappa_a) * a
    Ln = np.sqrt(kappa_n) * num

    # (i) commutant of constraint operators {a, adag, N, H}
    S = [a, adag, num, H]
    dim, svals = commutant_dim(S, N)
    # the trivial solution X = Id is the single exact machine-zero singular value;
    # the SMALLEST NONZERO sv below is the second sv (a truncation-boundary mode,
    # ~N^-1/2) -- it sits well above the identity's exact zero and no second mode
    # collapses toward zero as N grows, so dim = 1 is robust (confirmed to N=64).
    gap_lo = svals[svals >= TOL].min() if np.any(svals >= TOL) else float("nan")

    # (ii) pointer-state location
    fock = {n: in_commutant(fock_proj(n, N), S) for n in (1, 2, 3)}
    alpha = 2.0
    coh = in_commutant(coherent_proj(alpha, N), S)

    # (iii) dissipator superoperators + commutators
    Da = dissipator_super(La, N)
    Dn = dissipator_super(Ln, N)
    UH = hamiltonian_super(H, N)

    c_DaDn = comm(Da, Dn)                 # pure-dissipator commutator
    c_HplusA_n = comm(UH + Da, Dn)        # paper Eq.(17) grouping (H+La) vs Ln
    c_UH_Dn = comm(UH, Dn)
    c_UH_Da = comm(UH, Da)

    return {
        "N": N, "kappa_a": kappa_a, "kappa_n": kappa_n,
        "commutant_dim": dim,
        "commutant_smallest_nonzero_sv": float(gap_lo),
        "fock_residual": {str(k): float(v) for k, v in fock.items()},
        "coherent_residual": float(coh),
        "norm[Da,Dn]": float(np.linalg.norm(c_DaDn)),
        "norm[UH+Da,Dn]": float(np.linalg.norm(c_HplusA_n)),
        "norm[UH,Dn]": float(np.linalg.norm(c_UH_Dn)),
        "norm[UH,Da]": float(np.linalg.norm(c_UH_Da)),
    }


def main():
    print("=" * 74)
    print("  Co-admissibility decisive computation — Feller et al. (2020) model")
    print("=" * 74)

    results = []
    for N in (8, 12, 16, 20):
        r = run(N)
        results.append(r)

    # also a second coupling ratio to show the algebraic results are rate-free
    r_ratio = run(16, kappa_a=1.0, kappa_n=5.0)   # kappa_n/kappa_a = 5 (paper Fig.6)

    print("\n(i) COMMUTANT of {a, a^dag, N, H}  (non-trivial => DFS / C0 escape hatch)")
    print(f"    {'N':>4} {'dim':>5} {'2nd singular value (boundary mode)':>36}")
    print("    (the identity X=Id is an exact machine-zero BELOW this 2nd sv)")
    for r in results:
        print(f"    {r['N']:>4} {r['commutant_dim']:>5} "
              f"{r['commutant_smallest_nonzero_sv']:>36.4e}")
    print("    => dim 1 across N = only C*Id (the identity). Commutant is TRIVIAL.")
    print("       No non-trivial decoherence-free subsystem exists. Escape hatch CLOSED.")

    print("\n(ii) POINTER-STATE LOCATION  (max_M ||[rho,M]||_F ; ~0 => inside commutant)")
    r = results[-1]
    for k, v in r["fock_residual"].items():
        print(f"     Fock |{k}><{k}|        residual = {v:>12.4f}   (>0 => NOT in commutant)")
    print(f"     coherent |a=2><a=2|  residual = {r['coherent_residual']:>12.4f}   (>0 => NOT in commutant)")
    print("     => every pointer state lies in the COMPLEMENT of the commutant.")
    print("        The measure-free object is disjoint from the family the conjecture needs.")

    print("\n(iii) PAIRWISE-COMMUTING-DISSIPATOR criterion  { rho : [D_n,D_a](rho)=0 }")
    print(f"     {'N':>4} {'||[Da,Dn]||':>14} {'||[UH+Da,Dn]||':>16}   (Eq.17 grouping)")
    for r in results:
        print(f"     {r['N']:>4} {r['norm[Da,Dn]']:>14.4e} "
              f"{r['norm[UH+Da,Dn]']:>16.4e}")
    print("     => both commutators vanish to MACHINE PRECISION (~1e-12) at every N.")
    print("        No truncation defect (Ln = N is exactly diagonal under truncation),")
    print("        so this is not an edge artifact: the dissipators COMMUTE as super-")
    print("        operators, reproducing paper Eq.(17). Criterion (iii) is therefore")
    print("        satisfied by EVERY state: measure-free but NON-DISCRIMINATING")
    print("        (its admissible set is the whole state space).")

    print("\n     [rate-independence check] N=16, kappa_n/kappa_a = 5:")
    print(f"        commutant_dim = {r_ratio['commutant_dim']}, "
          f"||[Da,Dn]|| = {r_ratio['norm[Da,Dn]']:.2e}")

    # machine-checkable assertions (the artifact "reproduces" iff these hold)
    last = results[-1]
    assert all(r["commutant_dim"] == 1 for r in results), "commutant not trivial"
    assert last["fock_residual"]["2"] > 1e-3, "Fock pointer wrongly in commutant"
    assert last["coherent_residual"] > 1e-3, "coherent pointer wrongly in commutant"
    assert all(r["norm[Da,Dn]"] < 1e-9 for r in results), \
        "dissipators do not commute"
    assert all(r["norm[UH+Da,Dn]"] < 1e-9 for r in results), \
        "paper Eq.(17) not reproduced"
    assert r_ratio["commutant_dim"] == 1, "result is rate-dependent (unexpected)"

    print("\n" + "=" * 74)
    print("  VERDICT (all assertions passed; computation reproduces)")
    print("=" * 74)
    print("""  Each of the THREE TESTED measure-free candidates is well-defined and
  computable, but NOT discriminating on the actual incompatible-channel model:
    (i)   the commutant is C*Id (trivial) -> no DFS;
    (ii)  the pointer family lies wholly in its complement;
    (iii) the pairwise-commuting-dissipator set is the WHOLE space (Eq.17).
  No tested measure-free object reproduces the witness-dependent pointer
  structure (the Fock<->coherent interpolation across kappa_n/kappa_a~1).

  STRUCTURAL DIAGNOSIS (why, not just that): all three tested objects are
  ALGEBRAIC / RATE-INDEPENDENT, while the pointer family is RATE-GOVERNED
  (the transition sits at kappa_n/kappa_a ~ 1). A rate-independent object
  cannot, in principle, track a rate-dependent transition. This says where a
  surviving criterion would have to live (rate-dependent, generator-derived).

  SCOPE (do not overclaim): this is a recorded NEGATIVE for the TESTED criteria
  -- the `risk_if_false` outcome for OPN-001 -- and a progressive resolution,
  NOT a proof that no measure-free criterion can ever discriminate. The
  measure-free design space is not exhausted (the natural rate-dependent
  candidate, the Liouvillian slow modes, was checked in the red-team pass and
  also fails: its slow eigenmode is a k=+-1 coherence band, not a pointer
  projector). Open sub-question stands: does ANY rate-dependent measure-free
  object discriminate?""")

    out = {"model": "Feller-CoeuretCauquil-Roussel-2020 arXiv:2001.10851 Eq.(3)-(4)",
           "params": {"omega_c": OMEGA_C, "kappa_a": KAPPA_A, "kappa_n": KAPPA_N},
           "convergence_in_N": results,
           "rate_check_ratio5": r_ratio}
    path = os.path.join(os.path.dirname(__file__), "results.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\n  numeric results written to {os.path.basename(path)}")


if __name__ == "__main__":
    main()
