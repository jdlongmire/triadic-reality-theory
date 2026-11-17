"""Reconstruction (Claude, 2026-11-16) of the order-difference estimate the TRT charter
attributes to working-notes section 4.5. Not JD's calculation; an independent rebuild.

Setup: causal set at Planck density rho = l_P^-4. A mass m perturbs the metric by
h(r) ~ G m / (r c^2). Over a spacetime region of spatial radius R and duration T the
4-volume shift is dV ~ integral of h, so the element-count shift is dN = rho*dV against
Poisson noise sqrt(rho*V). Two branches of a superposition separated by ~R differ in
count by order dN. Criterion: actualize when SNR >= 1.
"""
import math
G=6.67430e-11; hbar=1.054571817e-34; c=2.99792458e8
lP=math.sqrt(hbar*G/c**3); rho=lP**-4
amu=1.66053906660e-27; me=9.1093837015e-31

def snr(m,R,T,Gval=G):
    lp=math.sqrt(hbar*Gval/c**3); rho=lp**-4
    dV=(Gval*m/c**2)*(2*math.pi*R**2)*(c*T)      # integral of h over ball x duration
    V=(4/3)*math.pi*R**3*(c*T)
    return rho*dV/math.sqrt(rho*V)

def t_collapse(m,R):
    # closed form: SNR = sqrt(3*pi) * (m c/hbar) * sqrt(R c T)  ->  T = lam^2/(3 pi R c)
    lam=hbar/(m*c)
    return lam**2/(3*math.pi*R*c)

print("Planck length", lP)
# G-cancellation check: vary G by 10 orders, SNR unchanged
for g in (G, G*1e5, G*1e-5):
    print("G=%.3e  SNR(electron,R=1um,T=1e-8s)=%.6e"%(g, snr(me,1e-6,1e-8,g)))
print("closed-form coefficient check:", snr(me,1e-6,1e-8)/((me*c/hbar)*math.sqrt(1e-6*c*1e-8)), "vs sqrt(3pi)=",math.sqrt(3*math.pi))

cases=[("electron, R=1 um, coherence 1e-8 s", me, 1e-6, 1e-8),
       ("electron, R=100 um, coherence 1e-8 s", me, 1e-4, 1e-8),
       ("electron, R=10 nm, coherence 1e-8 s", me, 1e-8, 1e-8),
       ("molecule 25 kDa, R=266 nm, coherence 7.5e-3 s", 25000*amu, 266e-9, 7.5e-3),
       ("molecule 25 kDa, R=10 nm, coherence 7.5e-3 s", 25000*amu, 1e-8, 7.5e-3)]
for name,m,R,Tobs in cases:
    T=t_collapse(m,R)
    print(f"{name}: T_collapse={T:.2e} s, observed/predicted={Tobs/T:.2e}, orders={math.log10(Tobs/T):.1f}")
# contrast with Diosi-Penrose scale tau ~ hbar*R/(G m^2), where G does not cancel
for name,m,R in (("electron",me,1e-6),("25 kDa",25000*amu,266e-9)):
    print(name,"Diosi-Penrose-type tau ~ %.2e s"%(hbar*R/(G*m*m)))
