#!/usr/bin/env python3
"""ADCE bridge-law scan (Target 5 toy model, FLRW level).

Two-level framework (adce.md v3.1 SS9.4): the record-sector count N_R is the
dynamical driver; a bridge law B maps the record sector to an effective
energy density rho_A entering the Friedmann equation. This script scans
{source history} x {bridge law} cells for the red-team's severe test:

  (i)   matter-era deceleration preserved (rho_A subdominant at z >~ 5)
  (ii)  late-time acceleration (q0 < 0)
  (iii) sign-stability of rho_A
  (iv)  shape of rho_A(z): monotone vs late-peaking (DESI DR2 prefers a
        peak at z ~ 0.3-0.5 with phantom crossing at the peak)
  (v)   effective (w0, wa) vs the DESI quadrant (w0 > -1, wa < 0)

Sources (comoving record-formation rate density sigma(a), arbitrary units):
  S1 sfh        : Madau-Dickinson 2014 cosmic star-formation history
  S2 per-baryon : constant comoving rate (fixed rate per conserved baryon)
  S3 collisional: sigma ~ a^-3 (two-body interaction rate per comoving vol)
  S4 feedback   : sigma = lam * N_R (each record opens new channels)

Bridges (mu tuned per cell so Omega_A(a=1) = 1 - Om - Or):
  B1 diluted-stock : rho_A = mu * N_R / a^3   (fixed energy per record;
                     w_A = -(1/3) dlnN_R/dlna exactly)
  B2 comoving-stock: rho_A = mu * N_R         (undiluted; Lambda-limit if
                     N_R saturates; w_A = -1 - (1/3) dlnN_R/dlna)
  B3 rate          : rho_A = mu * (dN_R/dt) / a^3  (proper rate density)

Self-consistency: H^2 = H0^2 [Or a^-4 + Om a^-3 + rho_A/rho_c0], with
N_R(a) = int sigma dt and t(a) from the same H. Solved by fixed-point
iteration starting from LCDM.
"""

import numpy as np

# --- cosmology constants (DESI DR2 / Planck baseline) ---
OM, OR = 0.31, 9.0e-5
OA = 1.0 - OM - OR
H0 = 1.0                      # internal units: H0 = 1; t in 1/H0
AI, NPTS = 1e-4, 4000
X = np.linspace(np.log(AI), 0.0, NPTS)   # x = ln a
A = np.exp(X)
Z = 1.0 / A - 1.0


def mdickinson(z):
    """Madau-Dickinson 2014 SFH fitting function (arbitrary normalization)."""
    return (1 + z) ** 2.7 / (1 + ((1 + z) / 2.9) ** 5.6)


def cumtrapz0(y, x):
    out = np.zeros_like(y)
    out[1:] = np.cumsum(0.5 * (y[1:] + y[:-1]) * np.diff(x))
    return out


def dlog(y, x):
    """d ln y / d x, guarded."""
    ly = np.log(np.clip(y, 1e-300, None))
    return np.gradient(ly, x)


def solve_cell(source, bridge, lam=None, iters=60, tol=1e-8):
    """Fixed-point solve; returns dict of curves or None on failure."""
    E2 = OR * A**-4 + OM * A**-3 + OA          # LCDM seed for E^2 = (H/H0)^2
    mu_hist = []
    for it in range(iters):
        E = np.sqrt(E2)
        # t(a): dt = dx / H
        t = cumtrapz0(1.0 / E, X)
        # record accumulation
        if source == "S4":
            # dN/dt = lam*N  -> N = N0 exp(lam t); N0 arbitrary (mu absorbs)
            NR = np.exp(lam * t)
        else:
            if source == "S1":
                sig = mdickinson(Z)
            elif source == "S2":
                sig = np.ones_like(A)
            elif source == "S3":
                sig = A**-3
            # dN/dx = sigma / H ; seed avoids log(0)
            NR = cumtrapz0(sig / E, X) + 1e-12
        # bridge -> unnormalized shape f(a)
        if bridge == "B1":
            f = NR / A**3
        elif bridge == "B2":
            f = NR.copy()
        elif bridge == "B3":
            if source == "S4":
                dNdt = lam * NR
            else:
                dNdt = sig
            f = dNdt / A**3
        mu = OA / f[-1]
        rhoA = mu * f
        E2_new = OR * A**-4 + OM * A**-3 + rhoA
        err = np.max(np.abs(E2_new - E2) / E2)
        E2 = E2_new
        mu_hist.append(mu)
        if err < tol:
            break
    E = np.sqrt(E2)
    rhoA = np.clip(rhoA, 1e-300, None)
    # effective EoS: w = -1 - (1/3) dln rhoA / dln a
    w = -1.0 - dlog(rhoA, X) / 3.0
    # deceleration q = -1 - dlnH/dlna
    q = -1.0 - dlog(E, X)
    return dict(E=E, t=cumtrapz0(1.0 / E, X), NR=NR, rhoA=rhoA, w=w, q=q,
                converged=err < tol, iters=it + 1)


def diagnostics(r):
    d = {}
    rhoA, w, q = r["rhoA"], r["w"], r["q"]
    # matter era intact: rho_A / rho_m at z=5 and z=99
    for zc, key in [(5, "ratio_z5"), (99, "ratio_z99")]:
        i = np.argmin(np.abs(Z - zc))
        d[key] = rhoA[i] / (OM * A[i] ** -3)
    d["q0"] = q[-1]
    # acceleration onset
    zlim = Z <= 10
    qq, zz = q[zlim], Z[zlim]
    sgn = np.where(np.diff(np.sign(qq)))[0]
    d["z_acc"] = zz[sgn[-1]] if len(sgn) else None
    # rho_A peak (search z < 20)
    m = Z < 20
    ip = np.argmax(rhoA[m])
    zpk = Z[m][ip]
    interior = 0 < ip < m.sum() - 1
    d["z_peak"] = zpk if interior else None
    # w at benchmarks
    for zc, key in [(0, "w0z"), (0.5, "w_z05"), (1.0, "w_z1")]:
        i = np.argmin(np.abs(Z - zc))
        d[key] = w[i]
    # crossing of w=-1 for z<6
    m2 = Z < 6
    ww, zz2 = w[m2], Z[m2]
    cr = np.where(np.diff(np.sign(ww + 1)))[0]
    d["z_cross"] = zz2[cr[-1]] if len(cr) else None
    # CPL fit over a in [0.5, 1]
    mfit = A >= 0.5
    x1 = 1 - A[mfit]
    coef = np.polyfit(x1, w[mfit], 1)
    d["w0_fit"], d["wa_fit"] = coef[1], coef[0]
    d["sign_stable"] = bool(np.all(rhoA >= 0))
    return d


def solve_horizon_cell():
    """S5 x B1: N_R = cumulative apparent-horizon area ~ E^-2 (units absorbed);
    rho_A = mu * E^-2 / a^3. Fixed-point solve."""
    E2 = OR * A**-4 + OM * A**-3 + OA
    for it in range(200):
        NR = 1.0 / E2
        f = NR / A**3
        mu = OA / f[-1]
        rhoA = mu * f
        E2_new = OR * A**-4 + OM * A**-3 + rhoA
        err = np.max(np.abs(E2_new - E2) / E2)
        E2 = 0.5 * E2 + 0.5 * E2_new          # damped: quadratic self-coupling
        if err < 1e-10:
            break
    E = np.sqrt(E2)
    w = -1.0 - dlog(rhoA, X) / 3.0
    q = -1.0 - dlog(E, X)
    return dict(E=E, t=cumtrapz0(1.0 / E, X), NR=NR, rhoA=rhoA, w=w, q=q,
                converged=err < 1e-10, iters=it + 1)


def inverse_problem():
    """Under B1, what comoving source history sigma_req(z) reproduces the
    DESI DR2 w0waCDM rho_DE(a) exactly? N_R = a^3 rho_A / mu, sigma = dN/dt."""
    w0, wa = -0.752, -0.86
    rhoA = OA * A ** (-3 * (1 + w0 + wa)) * np.exp(-3 * wa * (1 - A))
    E = np.sqrt(OR * A**-4 + OM * A**-3 + rhoA)
    NR = A**3 * rhoA
    # sigma = dN/dt = (dN/dx) * H
    sigma = np.gradient(NR, X) * E
    m = (Z < 6) & (sigma > 0)
    ipk = np.argmax(sigma[m])
    print(f"\n[inverse problem, B1] sigma_req(z) peaks at z = {Z[m][ipk]:.2f}; "
          f"sigma_req(0)/sigma_req(peak) = {sigma[-1]/sigma[m][ipk]:.2f}")
    # where does sigma_req go negative (record destruction required)?
    neg = np.where(sigma[Z < 6] < 0)[0]
    zneg = Z[Z < 6][neg]
    if len(neg):
        print(f"  sigma_req < 0 (record DESTRUCTION required) for z in "
              f"[{zneg.min():.2f}, {zneg.max():.2f}]")
    else:
        print("  sigma_req >= 0 everywhere (no record destruction needed)")
    # compare shapes at a few z against candidates
    print("  shape sigma_req vs SFH (both normalized at z=1):")
    isfh = mdickinson(Z)
    i1 = np.argmin(np.abs(Z - 1))
    for zc in [0.0, 0.5, 1.0, 2.0, 4.0]:
        i = np.argmin(np.abs(Z - zc))
        print(f"    z={zc:3.1f}: sigma_req={sigma[i]/sigma[i1]:8.3f}   "
              f"SFH={isfh[i]/isfh[i1]:6.3f}")
    # required record-stock growth exponent today for w0=-0.752 under B1
    print(f"  required dlnN_R/dlna today (w0={w0}): {-3*w0:.2f}")


def main():
    cells = []
    for src in ["S1", "S2", "S3", "S4"]:
        for br in ["B1", "B2", "B3"]:
            if src == "S4":
                # feedback rate lam is a free parameter; scan a few
                for lam in [1.0, 2.0, 3.0, 4.0]:
                    r = solve_cell(src, br, lam=lam)
                    cells.append((f"{src}(lam={lam:g}H0)x{br}", r))
            else:
                r = solve_cell(src, br)
                cells.append((f"{src}x{br}", r))

    hdr = (f"{'cell':<22} {'conv':<5} {'rA/rm@z5':>9} {'q0':>6} {'z_acc':>6} "
           f"{'z_peak':>7} {'z_cross':>8} {'w(0)':>6} {'w(0.5)':>7} "
           f"{'w0fit':>6} {'wafit':>6} {'DESI?':>6}")
    print(hdr)
    print("-" * len(hdr))
    for name, r in cells:
        d = diagnostics(r)
        desi = (d["w0_fit"] > -1 and d["wa_fit"] < 0 and d["z_peak"] is not None
                and 0.1 < d["z_peak"] < 1.0 and d["q0"] < 0
                and d["ratio_z5"] < 0.1)
        fmt = lambda v, p=3: ("  none" if v is None else f"{v:>6.{p}f}")
        print(f"{name:<22} {str(r['converged']):<5} {d['ratio_z5']:>9.2e} "
              f"{d['q0']:>6.2f} {fmt(d['z_acc'],2):>6} {fmt(d['z_peak'],2):>7} "
              f"{fmt(d['z_cross'],2):>8} {d['w0z']:>6.2f} {d['w_z05']:>7.2f} "
              f"{d['w0_fit']:>6.2f} {d['wa_fit']:>6.2f} {str(desi):>6}")

    # S5 x B1 horizon cell
    r = solve_horizon_cell()
    d = diagnostics(r)
    fmt = lambda v, p=2: ("  none" if v is None else f"{v:>6.{p}f}")
    print(f"{'S5(horizon)xB1':<22} {str(r['converged']):<5} {d['ratio_z5']:>9.2e} "
          f"{d['q0']:>6.2f} {fmt(d['z_acc']):>6} {fmt(d['z_peak']):>7} "
          f"{fmt(d['z_cross']):>8} {d['w0z']:>6.2f} {d['w_z05']:>7.2f} "
          f"{d['w0_fit']:>6.2f} {d['wa_fit']:>6.2f}")

    inverse_problem()

    # reference: DESI DR2 w0waCDM shape
    w0, wa = -0.752, -0.86
    rho = A ** (-3 * (1 + w0 + wa)) * np.exp(-3 * wa * (1 - A))
    m = Z < 20
    ipk = np.argmax(rho[m])
    astar = 1 + (1 + w0) / wa
    print(f"\n[DESI DR2 ref] rho_DE peak z = {Z[m][ipk]:.2f}; "
          f"w=-1 crossing z = {1/astar - 1:.2f} (analytic)")


if __name__ == "__main__":
    main()
