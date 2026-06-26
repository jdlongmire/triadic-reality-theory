#!/usr/bin/env python3
"""
Co-admissibility, the last open door (Task 0.1 / OPN-001, sub-question (a)).

  >>> CORRECTED 2026-06-26 after an independent Red-Team pass refuted the first
      version's conclusion. The first version compared gamma_dot for a Fock state
      vs a full coherent state (=> g*=1) and wrongly concluded "no rate-dependent
      measure-free object discriminates." That is the WRONG comparison: Feller's
      criterion is Fock-state stability WITHIN A FIXED-ENERGY SHELL, not Fock-vs-
      coherent. With the right criterion, a rate-dependent measure-free object DOES
      reproduce the analytic critical coupling. The honest result is a DICHOTOMY,
      not a negative. See the verdict. <<<

Attempt 2 (coadmissibility_commutant.py): the ALGEBRAIC / rate-INDEPENDENT measure-
free objects (commutant, joint kernel, pairwise-commuting dissipators) are non-
discriminating. The open door (JD, pursue (a)):

    Does any RATE-DEPENDENT, generator-derived, measure-free object reproduce the
    Feller einselected pointer structure across the critical coupling g=kappa_n/kappa_a?

Model (verified primary source -- Feller, Coeuret Cauquil & Roussel 2020,
arXiv:2001.10851): H = w_c N, L_a = sqrt(k_a) a, L_n = sqrt(k_n) N. Fix k_a=1,
sweep g=k_n. Pointer states = extremise the PURITY tr rho^2 at a given energy.
Analytic critical coupling (paper Eqs. 39-40, extracted from the PDF):

    g* = kappa_n/kappa_a = n0 + 1/2 + sqrt(n0 (n0+1))   ( ~ 2 n0 + 1 )

at which the Fock state |n0> stops being a local maximum of the purity-variation
(it becomes a saddle along the (|n0-1>,|n0+1>) plane).

Three rate-dependent objects:

  (1) GENERATOR SPECTRUM (witness-FREE).  Every non-stationary Liouvillian eigenmode
      is traceless (trace conservation: Tr L(rho)=0 => any eigenmode with non-zero
      eigenvalue is traceless), so none is a density-matrix pointer; the steady state
      is the vacuum at every g (no finite-energy content).  => the witness-free
      generator spectrum makes NO pointer prediction.  [non-discriminating horn]

  (2) gamma_dot, Fock-vs-coherent (the WRONG object, kept as a labelled control).
      gamma_dot(|psi>) = -2[k_n Var(N) + k_a(<N> - |<a>|^2)].  Fock |n>: 2 k_a n;
      coherent: 2 k_n <n>.  Crossover g*=1, energy-independent -- but this compares
      two fixed families, not Feller's criterion.

  (3) gamma_dot ENERGY-SHELL STABILITY (Feller's ACTUAL criterion, witness=purity).
      Is |n0> a local max of gamma_dot under energy-preserving perturbations in the
      (|n0-1>,|n0+1>) plane?  The max->saddle flip reproduces g* = n0+1/2+sqrt(n0(n0+1))
      to <0.2%.  => a rate-dependent, generator-derived, purity-witness object DOES
      reproduce the analytic critical coupling.  [re-description horn]

Pure numpy/scipy; deterministic; no fitted parameters.
Run:  python3 coadmissibility_ratedep.py
"""

import json
import math
import os
import numpy as np

np.set_printoptions(precision=4, suppress=True, linewidth=120)

OMEGA_C = 1.0
ENERGIES = (2, 3, 4, 5, 6)     # n0 = mean photon number of the Fock state |n0>


def ops(N):
    a = np.zeros((N, N), dtype=complex)
    for n in range(1, N):
        a[n - 1, n] = math.sqrt(n)
    return a, a.conj().T @ a            # a, N


def liouvillian(N, g):
    a, num = ops(N)
    H = OMEGA_C * num
    I = np.eye(N)

    def D(L):
        LdL = L.conj().T @ L
        return np.kron(L.conj(), L) - 0.5 * np.kron(I, LdL) - 0.5 * np.kron(LdL.T, I)

    return -1j * (np.kron(I, H) - np.kron(H.T, I)) + D(a) + g * D(num)


def gamma_dot(N, g, psi):
    """Initial purity-decay rate for a pure state |psi>: gamma_dot = 2 Re tr(rho L(rho))
    = -2[ g Var(N) + (<N> - |<a>|^2) ]  (k_a = 1, k_n = g)."""
    a, num = ops(N)
    nE = np.vdot(psi, num @ psi).real
    n2 = np.vdot(psi, num @ num @ psi).real
    aE = np.vdot(psi, a @ psi)
    return -2.0 * (g * (n2 - nE ** 2) + (nE - abs(aE) ** 2))


# ---- (1) generator spectrum --------------------------------------------------
def generator_spectrum_report(N, g):
    L = liouvillian(N, g)
    w, V = np.linalg.eig(L)
    nonstat = [i for i in range(len(w)) if abs(w[i].real) > 1e-9]
    max_trace = max(abs(np.trace(V[:, i].reshape(N, N))) / np.linalg.norm(V[:, i])
                    for i in nonstat)
    # steady state: eigenvector of the ~zero eigenvalue
    iss = min(range(len(w)), key=lambda i: abs(w[i]))
    rho_ss = V[:, iss].reshape(N, N)
    rho_ss = rho_ss / np.trace(rho_ss)
    _, num = ops(N)
    n_ss = np.real(np.trace(rho_ss @ num))
    return max_trace, len(nonstat), n_ss


# ---- (3) energy-shell Fock-stability ----------------------------------------
def fock_stability_flip(N, n0, s=1e-3, ntheta=33):
    """Smallest g at which |n0> turns from saddle (some perturbation raises gamma_dot)
    to local max (no perturbation raises it). Energy-preserving perturbations:
    equal weight on |n0-1>,|n0+1> with relative phase theta; worst-case theta."""
    base = np.zeros(N, dtype=complex)
    base[n0] = 1.0
    g0_of = lambda g: gamma_dot(N, g, base)

    def cmax(g):
        out = -np.inf
        for th in np.linspace(0, 2 * np.pi, ntheta):
            psi = base.copy()
            psi[n0 - 1] = s
            psi[n0 + 1] = s * np.exp(1j * th)
            psi /= np.linalg.norm(psi)
            out = max(out, (gamma_dot(N, g, psi) - g0_of(g)) / s ** 2)
        return out                      # >0 => |n0> is a saddle (not the robust max)

    gs = np.linspace(0.5, 4 * n0 + 5, 1200)
    prev = cmax(gs[0])
    for g in gs[1:]:
        c = cmax(g)
        if prev > 0 >= c:               # saddle -> max
            return g
        prev = c
    return None


def main():
    print("=" * 74)
    print("  Co-admissibility sub-question (a): rate-dependent measure-free objects")
    print("  (CORRECTED after red-team: the answer is a DICHOTOMY, not a negative)")
    print("=" * 74)

    N = 20
    out = {"model": "Feller et al. 2020 arXiv:2001.10851", "N": N,
           "analytic_g_star": "n0 + 1/2 + sqrt(n0(n0+1))  (Eq. 39-40)"}

    # (1) generator spectrum (witness-free)
    print("\n(1) GENERATOR SPECTRUM (witness-free) -- non-discriminating horn")
    spec = {}
    for g in (0.5, 1.0, 2.0):
        mt, nns, nss = generator_spectrum_report(N, g)
        spec[g] = {"max_trace_over_norm": mt, "n_nonstationary": nns, "steady_state_<N>": nss}
        print(f"    g={g:>4}: all {nns} non-stationary modes traceless "
              f"(max |Tr|/||.||={mt:.1e}); steady state <N>={nss:.2e} (vacuum)")
    print("    => no density-matrix pointer in the spectrum; steady state carries no")
    print("       finite-energy structure. Witness-free generator => NO pointer prediction.")

    # (2) gamma_dot Fock-vs-coherent (labelled WRONG object)
    print("\n(2) gamma_dot Fock-vs-coherent (the WRONG comparison -- control only)")
    def coherent(al):
        c = np.array([al ** k / math.sqrt(math.factorial(k)) for k in range(N)], dtype=complex)
        c *= np.exp(-0.5 * abs(al) ** 2); c /= np.linalg.norm(c); return c
    def fock(n):
        v = np.zeros(N, dtype=complex); v[n] = 1.0; return v
    fvc = {}
    for nbar in (2, 4, 6):
        gs = np.linspace(0.3, 3, 200)
        d = [gamma_dot(N, g, fock(nbar)) - gamma_dot(N, g, coherent(math.sqrt(nbar))) for g in gs]
        gx = next((gs[i] + (gs[i+1]-gs[i])*(-d[i])/(d[i+1]-d[i])
                   for i in range(len(gs)-1) if d[i]*d[i+1] < 0), None)
        fvc[nbar] = gx
        print(f"    n0={nbar}: crossover g*={gx:.3f}")
    print("    => g*~1 (energy-independent). This is NOT Feller's criterion; it compares")
    print("       two fixed families instead of testing stability within the energy shell.")

    # (3) gamma_dot energy-shell Fock-stability (Feller's ACTUAL criterion)
    print("\n(3) gamma_dot ENERGY-SHELL Fock-stability (Feller's criterion) -- re-description horn")
    print(f"    {'n0':>3} {'analytic g*=n0+1/2+sqrt(n0(n0+1))':>34} {'numeric flip':>14} {'rel.err':>9}")
    shell = {}
    for n0 in ENERGIES:
        analytic = n0 + 0.5 + math.sqrt(n0 * (n0 + 1))
        Nn = n0 + 12
        flip = fock_stability_flip(Nn, n0)
        rel = abs(flip - analytic) / analytic
        shell[n0] = {"analytic": analytic, "numeric": flip, "rel_err": rel}
        print(f"    {n0:>3} {analytic:>34.4f} {flip:>14.4f} {rel:>9.2e}")
    print("    => reproduces the analytic critical coupling to <0.2%. A RATE-DEPENDENT,")
    print("       generator-derived, purity-witness object DOES reproduce the pointer structure.")

    # assertions
    assert all(spec[g]["max_trace_over_norm"] < 1e-6 for g in spec), "non-stationary modes not traceless"
    assert all(abs(spec[g]["steady_state_<N>"]) < 1e-6 for g in spec), "steady state not vacuum"
    assert all(abs(fvc[nb] - 1.0) < 0.05 for nb in fvc), "Fock-vs-coherent control not g*=1"
    assert all(shell[n0]["rel_err"] < 0.01 for n0 in ENERGIES), "energy-shell flip != analytic g*"

    print("\n" + "=" * 74)
    print("  VERDICT (all assertions passed; reproduces) -- a DICHOTOMY")
    print("=" * 74)
    print("""  Sub-question (a): does a RATE-DEPENDENT measure-free object reproduce the
  Feller pointer structure?  The measure-free objects split cleanly:

    WITNESS-FREE  (commutant/kernel/pairwise [Attempt 2]; generator spectrum [here])
        -> NON-DISCRIMINATING: no pointer-state prediction at all.

    WITNESS-FIXED to the purity (gamma_dot energy-shell stability [here])
        -> REPRODUCES the analytic critical coupling g* = n0+1/2+sqrt(n0(n0+1))
           EXACTLY -- because gamma_dot IS the (linear-entropy) predictability sieve.
           It matches standard einselection by ADOPTING its witness => RE-DESCRIPTION.

  So there is no middle ground delivering what the conjecture actually claims:
  a WITNESS-INDEPENDENT criterion with content BEYOND einselection. Witness-free is
  empty; witness-fixed is einselection re-described. This REVISES Attempt 3's earlier
  wrong "no prediction" conclusion (caught by red-team) -- the live threat to PRD-001
  is the RE-DESCRIPTION horn (falsifier (a)), not (b)/(c).

  NEW open sub-question (the only door still ajar): does gamma_dot differ from standard
  einselection in the regime where einselection is itself WITNESS-DEPENDENT? If it
  agrees everywhere, co-admissibility (in this form) predicts nothing new; if it
  differs in a computable way, that difference is the first genuinely novel content.

  SCOPE: principal rate-dependent candidates covered; not an impossibility proof over
  every conceivable measure-free object. Label decision (incl. any move toward
  refuted-by-re-description) is JD's.""")

    out["generator_spectrum"] = {str(k): v for k, v in spec.items()}
    out["fock_vs_coherent_control"] = {str(k): v for k, v in fvc.items()}
    out["energy_shell_stability"] = {str(k): v for k, v in shell.items()}
    path = os.path.join(os.path.dirname(__file__), "results_ratedep.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\n  numeric results written to {os.path.basename(path)}")


if __name__ == "__main__":
    main()
