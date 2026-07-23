# ADCE Targets 3 and 5: A-SAT Dissolution and the Bridge-Law Scan

**Status:** working report (belt-level, physics-facing) · **Claim:** [OPN-008](../../traceability/claims/OPN-008.yaml) · **Parent:** [adce.md](adce.md) (v3.1) · **Code:** [code/adce_bridge_scan.py](code/adce_bridge_scan.py) · **Prior review:** [2026-07 red-team](../../reviews/2026-07-redteam-adce/review.md)

This report executes the two items promoted at the close of the v3.1 cycle: **Target 3** (capacity bound and saturation axiom) and the FLRW-level portion of **Target 5** (the growth-law toy model, run against the red-team's severe test). The discrete CSG benchmark against Ahmed and Rideout (2010) remains open; §7 states what this report's results imply for how it should be scoped.

Summary of findings, stated up front:

1. **Target 3 closes negatively: A-SAT dissolves under the two-level split.** At the substrate level it is an identity that cannot force expansion; at the record level it is empirically false by ~100 orders of magnitude. The capacity-forcing route to expansion is closed, confirming the red-team's vector-2 suspicion analytically (§2).
2. **The mandatory deliverable (a) is achieved**: a growth law with matter-era deceleration and late acceleration exists in the natural grid — self-feedback rate with diluted-stock bridge — and v2's boxed relation $H = \lambda/3$ is recovered as a genuine *attractor*, not an assumption (§4.2). Its cost: the rate constant $\lambda \approx 3H_0$ is hand-set (the coincidence problem relocated), and it sits in the freezing-quintessence quadrant ($w_0 > -1$, $w_a > 0$), which DESI DR2 disfavors.
3. **The severe test fails across the natural grid.** No {source} × {bridge} cell reproduces the DESI-preferred shape (sign-stable, late-peaking $\rho_A$, crossing at $z \approx 0.35$–$0.50$). The nearest morphological match locks its peak to cosmic noon ($z \approx 2.1$), a factor ~5 too early (§4.3).
4. **Three independent probes converge on horizon coupling** as the only surviving branch of the mean-growth mechanism: the inverse problem's required source history rises monotonically to $z=0$ (anti-correlated with all matter-processing histories, §5); the only natural cell in the DESI quadrant is horizon-coupled (§4.4); and the only record inventory whose energy-per-record is a *derived* scale rather than an unexplained one is the horizon-entropy inventory (§6).

## 1. Setup inherited from v3.1

The two-level structure of adce.md §9.4 is taken as given: the substrate count $N_P$ (one element per Planck 4-volume; CST kinematics; inert) and the record count $N_R$ (physical record-forming events; the only level where dynamics can live). The v3.1 reformulated hypothesis makes expansion the registration of *accelerating* actualization; the open question is whether any natural record-sector growth law, mapped to stress-energy by some bridge law, produces the observed expansion history.

Observational anchors (verified against primaries this cycle): DESI DR2 w0waCDM fits span $w_0 = -0.42$ to $-0.84$, $w_a = -1.75$ to $-0.62$ across SN combinations (2.8–4.2σ over ΛCDM; arXiv:2503.14738); the phantom crossing sits at $z_c \approx 0.35$–$0.50$ (DESI's own statement: $z_c \simeq 0.45$; arXiv:2503.14743), and $\rho_{DE}$ peaks *at the crossing* (an identity of $w_0w_a$CDM: $d\ln\rho_{DE}/d\ln a = -3(1+w(a))$), only 7–40% above today's value — the required non-monotonicity is mild. Reference values used below: the DESY5 combination $w_0 = -0.752$, $w_a = -0.86$, giving peak/crossing $z^* = 0.405$.

## 2. Target 3: the capacity bound dissolves rather than closes

v3.1 left A-SAT ("actualization proceeds at the maximal rate the capacity bound admits; $\rho_A \to \rho_{A,\max}$") as a named, load-bearing, underived axiom, with the red-team's direction-of-explanation fork recorded against it. Executing Target 3 under the two-level split resolves the fork by *dissolving the axiom*:

**At the substrate level ($N_P$), saturation is an identity and cannot force anything.** CST discreteness is not the claim that element density *approaches* a bound; it is the claim that spacetime *is* a causal set whose elements realize 4-volume at fixed Poisson density $\rho_4 = \rho_{Planck}$ (Bombelli–Lee–Meyer–Sorkin 1987). There is no dynamical achievement in "$\rho_4$ at its bound" — that is the content of the number–volume correspondence itself. And because the bound is 4-volume-referenced, it is *geometry-neutral*: any spacetime, static ones included, accumulates 4-volume and hence elements at exactly $\rho_{Planck}$. This is the static-universe refutation of the red-team pass, restated as a structural fact about where the bound lives. A capacity bound can only force spatial expansion if it binds against a quantity that *fails to grow in a static geometry* — and the substrate bound does not.

**At the record level ($N_R$), saturation is empirically false.** The realized record density sits at least ~100 orders of magnitude below Planckian or holographic capacity (adce.md §9.4). No bound is being approached; no saturation dynamics can be invoked. A-SAT at this level does no work because it is simply not true.

**Conclusion.** For capacity-based forcing, one needs a level where the bound both *binds* and is *geometry-sensitive*. The substrate level gives binding without geometry-sensitivity; the record level gives neither. No level gives both, so the forcing route through capacity is closed — not "open pending derivation" but closed in principle under the two-level structure. A-SAT is retired from the framework. What survives of Target 3 is a redistribution of load: the entire dynamical content of ADCE now lives in the **bridge law** $B$: the map from the record sector to effective stress-energy,

$$T^{(A)}_{\mu\nu} = B[N_R\text{-sector}; g_{\mu\nu}],$$

and Target 4's "growth-to-geometry theorem" is re-posed as "derive $B$." One escape from this closure remains logically open and unexecuted: an extremal principle that would derive *both* the response and the rate at once. The available template is weaker than v3.1 hoped: Krishna–Mathew (arXiv:1702.02787, checked in fulltext this cycle) prove the direction *law ⇒ entropy maximization* — Padmanabhan's expansion law drives the universe to the holographic-equipartition entropy maximum ($\dot S \geq 0$, $\ddot S < 0$ at late times, saturation exactly at the de Sitter end state) — but the converse (extremal principle ⇒ unique law) is *not* established there; the law is one realization consistent with the extremal endpoint. Using their schema as a derivation template is therefore a conjecture, not an available result. Until such a derivation exists, ADCE has no forcing form at all — only candidate bridge laws to be tested. That is what the rest of this report does.

## 3. The bridge-law scan: design

Since $B$ is underived, the honest move is to scan the natural candidate space phenomenologically and let the data kill cells. The scan ([code/adce_bridge_scan.py](code/adce_bridge_scan.py)) solves the self-consistent FLRW system $H^2 = H_0^2[\Omega_r a^{-4} + \Omega_m a^{-3} + \rho_A/\rho_{c,0}]$ with $N_R(a) = \int \sigma\, dt$ computed in the same background (fixed-point iteration from a ΛCDM seed; $\Omega_m = 0.31$, converged to $10^{-8}$; resolution-stable at 2× grid density).

**Source histories** $\sigma(a)$ (comoving record-formation rate density): **S1** astrophysical processing (Madau–Dickinson 2014 SFH, coefficients verified against the ARAA primary); **S2** constant per-baryon rate; **S3** collisional ($\propto a^{-3}$); **S4** self-feedback ($\dot N_R = \lambda N_R$: each record opens new interaction channels); **S5** horizon-area accumulation ($N_R \propto H^{-2}$).

**Bridge laws:** **B1** diluted stock ($\rho_A = \mu N_R/a^3$: fixed energy per record, records are objects in space); **B2** comoving stock ($\rho_A = \mu N_R$); **B3** proper rate density ($\rho_A = \mu \dot N_R/a^3$).

The normalization $\mu$ is tuned per cell so $\Omega_A(a{=}1) = 0.69$: the scan tests *shape only*; magnitude is treated separately (§6). Two exact relations orient the reading: under B1, $w_A = -\tfrac13\, d\ln N_R/d\ln a$ (phantom ⇔ stock growing faster than volume; the $w=-1$ crossing coincides with the $\rho_A$ peak — structurally the DESI shape); under B2, $w_A = -1 - \tfrac13\, d\ln N_R/d\ln a$ (always phantom while records form; can never cross back; monotone $\rho_A$ — structurally *not* the DESI shape).

## 4. Scan results

Condensed results (full table in the script output; "DESI shape" = sign-stable, interior $\rho_A$ peak at $0.1 < z < 1$, $w_0^{fit} > -1$, $w_a^{fit} < 0$, $q_0 < 0$, matter era intact):

| cell | matter era | $q_0$ | $z_{acc}$ | $\rho_A$ peak | crossing | $(w_0, w_a)^{fit}$ | verdict |
|---|---|---|---|---|---|---|---|
| S1×B1 (SFH, diluted) | ✓ | +0.39 | 1.48 | z≈2.11 | z≈2.11 | (−0.06, −0.58) | shape right, epoch wrong, no acceleration today |
| S1×B2 (SFH, comoving) | ✓ | −0.62 | 0.71 | none | none | (−1.03, −0.73) | accelerates; monotone ρ_A; phantom side |
| S2×B1, S3×B1, S3×B2, S2×B3, S3×B3 | — | — | — | none | none | — | degenerate or dust-like; no viable cell |
| S4(λ=3H₀)×B1 (feedback, diluted) | ✓ (0.18) | −0.53 | 0.47 | none | none | (−1.05, +0.97)* | **deliverable (a)**: de Sitter attractor $H^* = \lambda/3$ |
| S4×B2 | ✓ | −1.2…−1.9 | ~0.5 | none | none | deep phantom | super-accelerating; excluded |
| S5×B1 (horizon, diluted) | ✓ | −0.11 | 0.53 | (z≈15, artifact) | none | (−0.58, −0.28) | **only DESI-quadrant cell**; acceleration too weak |

*\*CPL fit over $a \in [0.5,1]$; for S4×B1 the fit exaggerates $w_a$ because $w_A(a)$ is strongly non-linear near the attractor; the pointwise values are $w(0) = -1.00$, $w(0.5) = -0.74$.*

### 4.1 Analytic structure confirmed numerically

The two exact relations of §3 hold in the numerics to grid precision (B1 cells cross $w=-1$ exactly at their $\rho_A$ peak; B2 cells never cross). The B1/B3 degeneracy under S4 ($\dot N \propto N$ makes rate and stock proportional) is exact in the output — a consistency check, not a finding.

### 4.2 Mandatory deliverable (a): the feedback attractor

S4×B1 — records with fixed energy $\mu$ diluting as $a^{-3}$, formed at rate $\dot N_R = \lambda N_R$ — has a genuine de Sitter attractor: if $H > \lambda/3$ the stock dilutes faster than it grows and $\rho_A$ falls; if $H < \lambda/3$ it is phantom and $\rho_A$ rises; the fixed point $H^* = \lambda/3$ is approached from either side. **v2's boxed toy-model relation $H = \tfrac13 \dot N/N$ is thereby recovered as an attractor of a specific bridge law rather than as a kinematic assumption** — the strongest positive result of the scan. With $\lambda = 3H_0$: matter era intact ($\rho_A/\rho_m \approx 0.18$ at $z=5$), acceleration onset $z_{acc} \approx 0.47$, $w$ today $= -1.00$.

Costs, stated plainly: (i) $\lambda$ is a free parameter, and the observed acceleration requires $\lambda \approx 3H_0$ — *why is the channel-opening rate the present Hubble rate?* This is the coincidence problem relocated, not solved; exactly the disease of generic quintessence. (ii) The approach to the attractor is from $w > -1$ with $w$ *decreasing* over time — the freezing-quintessence quadrant ($w_a > 0$ in CPL terms), which is the opposite of DESI DR2's preferred quadrant. Not excluded (ΛCDM itself sits within DESI's 2.8–4.2σ), but disfavored by the current best data.

### 4.3 The severe test fails on the natural grid

No cell passes. The instructive failure is S1×B1: it produces exactly the demanded *morphology* — sign-stable, non-monotone $\rho_A$ with an interior peak, phantom crossing at the peak, in the correct direction (phantom in the past, $w > -1$ after) — but the peak sits at $z \approx 2.11$ (resolution-stable), locked to cosmic noon, because under B1 the peak occurs where $d\ln N_R/d\ln a = 3$, and for any source tracking astrophysical processing that threshold is crossed shortly after the SFH begins its post-noon decline. The observed peak is $z^* \approx 0.35$–$0.50$. A factor ~5 in epoch separates the natural astrophysical-record model from the data, and by $z=0$ its $w \approx -0.11$: essentially dust, no acceleration today.

### 4.4 The horizon cell

S5×B1 ($N_R \propto H^{-2}$, i.e. record stock tracking apparent-horizon area) is the only natural cell landing in the DESI quadrant: $(w_0, w_a)^{fit} = (-0.58, -0.28)$, sign-stable. During matter domination $\rho_A \propto H^{-2}a^{-3} = $ const — $w = -1$ exactly, by the same algebra that makes Hubble-cutoff holographic dark energy Λ-like in that era. But self-consistently it cannot complete the job: as $\rho_A$ dominates, $H \to$ const forces $\rho_A \propto a^{-3}$, i.e. $w \to 0$; the acceleration self-limits ($q_0 = -0.11$ vs. observed $\approx -0.55$). This is the known pathology of Hubble-scale holographic dark energy (Hsu 2004); the cure in that literature — a future-event-horizon cutoff (Li 2004) — has a well-known acausality cost. The cell fails as it stands, but it is the *only* natural cell pointing in the observed direction.

## 5. The inverse problem: what source would DESI require?

Under B1, invert the DESY5-combination history exactly: $N_R^{req} = a^3 \rho_{DE}(a)$, $\sigma^{req} = dN_R^{req}/dt$. Results (resolution-stable):

- $\sigma^{req}(z)$ is **non-negative everywhere** (no record destruction needed — sign-stability is achievable), and **rises monotonically to the present**: it peaks at $z = 0$, at 2.8× its $z=1$ value and ~25× its $z=4$ value.
- Every matter-processing proxy runs the other way: the SFH *falls* by ~6× from $z=1$ to $z=0$. The required source is **anti-correlated with the astrophysical activity history of the universe**. Whatever forms records at the required rate, it is not star formation, not collisional processing, not anything that traces matter density.
- The required stock growth today is $d\ln N_R/d\ln a = -3w_0 \approx 2.26$ (record count doubling every ~4.3 Gyr, sustained now).
- The one geometric quantity in the inventory that *does* rise monotonically into the acceleration era is horizon area — the qualitative reason S5 is the only quadrant-correct cell.

## 6. Magnitude (criterion 14)

With $\rho_{DE} = 5.29 \times 10^{-10}$ J/m³, the energy-per-record $\mu$ required of each candidate inventory (Egan–Lineweaver arXiv:0909.3983 for the entropy budget):

| record inventory | count/density today | required $\mu$ |
|---|---|---|
| CMB photons | $4.1 \times 10^8$ m⁻³ | 8.1 eV |
| all photons ever scattered (~10×) | $4 \times 10^9$ m⁻³ | 0.8 eV |
| stellar photons emitted (EBL) | $\sim 10^7$ m⁻³ | ~330 eV |
| baryons | 0.25 m⁻³ | 13 GeV |
| **cosmic-horizon entropy** | $S_{CEH} = 2.6 \times 10^{122}\, k_B$ | $2.5 \times 10^{-53}$ J $= 1.6 \times 10^{-34}$ eV |

The astrophysical rows all yield *unexplained* scales (why 8 eV? why 13 GeV?) — and each fails the shape requirement independently (CMB photon count is comoving-constant: $d\ln N/d\ln a = 0$ gives $w = 0$ under B1). The horizon row is the only one whose $\mu$ is a **derived** scale: it sits within a factor 1.4 of $k_B T_{dS} = \hbar H_0/2\pi = 3.7 \times 10^{-53}$ J, the de Sitter temperature. **Caveat, stated before anyone else states it:** $\rho_{DE} V \sim S_{CEH} T_{dS}$ is close to a thermodynamic identity of de Sitter space, so this near-coincidence is partially guaranteed and is *not* a derivation of the magnitude. Its evidential force is comparative only: horizon-coupled bookkeeping is the unique row where the required scale is even a recognized physical quantity.

## 7. Synthesis and program consequences

**Three probes, one direction.** The natural-grid scan (§4.4), the inverse problem (§5), and the magnitude table (§6) independently select the same surviving branch: *if* the mean-growth mechanism describes dark energy, actualization must be **horizon-coupled** — the record stock that gravitates must track horizon structure, not matter processing. The record-sector-as-astrophysics reading of ADCE is now under direct pressure from its own severe test (criteria 15/16 direction): its natural cells either fail to accelerate, sit in the disfavored quadrant, or peak at cosmic noon instead of $z \approx 0.4$.

**The criterion-12 risk is now acute and must be named.** A horizon-coupled ADCE is structurally adjacent to holographic dark energy (Li 2004) and to horizon-thermodynamic approaches (Padmanabhan; and Sorkin's everpresent Λ is horizon-adjacent via $V_4$). For the branch to be ADCE rather than a relabel, it must supply what those programs lack: an *ontology of the horizon as actualization locus* (horizon crossings as irreversible causal facts — a record-formation reading of horizon-area growth) **and** at least one prediction that separates it from generic HDE. Absent both, criterion 12 fires and the honest disposition is absorption.

**The CSG microdynamics takes a side — and it is the disfavored one.** The fulltext sweep of the sequential-growth literature (this cycle) adds a fact the scan could not: classical sequential growth *generically* produces the feedback branch. Cosmic renormalization (Martin–O'Connor–Rideout–Sorkin gr-qc/0009063) has the transitive-percolation family $t_n = t^n$ as its unique fixed-point line (no other fixed points, no cycles), so late cosmic epochs generically run percolation dynamics; and percolation's post-bounce phase is exactly the exponentially-expanding, de Sitter-like regime Ahmed–Rideout fit (3+1-dimensional over ≥1.5 decades of $p$). No CSG work derives a horizon-referenced effective growth law from any covariant $t_n$ family — a confirmed literature gap, not just an unsearched corner. The theory-vs-data split is therefore clean: **CSG microdynamics natively selects the feedback/attractor branch; the current data preference (DESI phantom crossing) selects the horizon branch; and the two are mutually exclusive in $w_a$ sign.** Additionally, any future CSG benchmark can only certify a coarse-observable correspondence: Glaser–Surya (arXiv:1309.3403) showed Ahmed–Rideout's own parameter cases fail the interval-abundance manifoldlikeness test, and CSG continuum limits are semiorders with no spatial structure (Brightwell–Georgiou) — the de Sitter phase is real in the volume-vs-proper-time observable at finite $n$ between posts, and only there.

**Revised target queue** (supersedes the v3.1 §15 ordering for the affected items):

1. ~~Target 3 (capacity bound + A-SAT)~~ — **closed negative** this report (§2): A-SAT dissolved; capacity-forcing route closed in principle; extremal-principle escape (Krishna–Mathew shape) remains the only reopening.
2. **Target 4′ (re-posed): derive the bridge law** — now specifically: derive a horizon-coupled bridge from the actualization ontology, with the freezing-quintessence attractor (S4×B1, §4.2) as the fallback branch if the DESI preference weakens toward ΛCDM in DR3+.
3. **Target 5 (CSG benchmark, partially answered by the literature)**: the microdynamics question the v3.1 queue posed — which growth law does covariant sequential growth select? — is already answered generically: the feedback/exponential branch (percolation as renormalization fixed point; see above). The remaining discrete work is narrower and harder: determine whether *any* covariant $t_n$ family can produce a horizon-referenced effective law (none known; confirmed gap), understanding that any positive result is bounded to coarse observables by the Glaser–Surya manifoldlikeness ceiling.
4. **Falsification watch (now the program's sharpest structure)**: the attractor branch and the DESI-preferred quadrant are *mutually exclusive* ($w_a$ of opposite sign), and the microdynamics has already sided with the attractor. DESI DR3 / Euclid tightening of $(w_0, w_a)$ therefore adjudicates for free: if the phantom-crossing preference strengthens, the CSG-natural branch dies and ADCE survives only as horizon-coupled actualization with no microdynamical derivation and an acute criterion-12 risk; if the preference dissolves toward ΛCDM, the horizon branch loses its motivation and the surviving object is the freezing attractor with a relocated coincidence problem. Neither outcome is comfortable; both are informative, and the discomfort is quantifiable in advance.

**What did NOT survive this cycle:** A-SAT (dissolved); the astrophysical-record reading of the source (all its cells dead on shape or epoch); any remaining hope that the severe test could be passed without horizon reference.

**What survives:** the reformulated (v3.1) hypothesis, now with exactly two live realizations — the feedback attractor (achieves deliverable (a), disfavored quadrant, relocated coincidence) and horizon-coupled actualization (right quadrant, no complete model, acute criterion-12 risk). The program is narrower, again, and the next kill condition is externally scheduled (DR3+). Per the programme methodology, both narrowings are recorded negatives, and the mutual-exclusivity of the surviving branches is the most decision-useful structure ADCE has yet produced.

## References

Ahmed, M. and Rideout, D. (2010) 'Indications of de Sitter spacetime from classical sequential growth dynamics of causal sets', *Physical Review D*, 81, 083528. arXiv:0909.4771.

Bombelli, L., Lee, J., Meyer, D. and Sorkin, R.D. (1987) 'Space-time as a causal set', *Physical Review Letters*, 59(5), pp. 521–524.

DESI Collaboration (2025) 'DESI DR2 results II: measurements of baryon acoustic oscillations and model extensions'. arXiv:2503.14738. Companion: 'Extended dark energy analysis'. arXiv:2503.14743.

Egan, C.A. and Lineweaver, C.H. (2010) 'A larger estimate of the entropy of the universe', *The Astrophysical Journal*, 710(2), pp. 1825–1834. arXiv:0909.3983.

Glaser, L. and Surya, S. (2013) 'Towards a definition of locality in a manifoldlike causal set', *Physical Review D*, 88, 124026. arXiv:1309.3403.

Hsu, S.D.H. (2004) 'Entropy bounds and dark energy', *Physics Letters B*, 594(1-2), pp. 13–16. hep-th/0403052.

Martin, X., O'Connor, D., Rideout, D.P. and Sorkin, R.D. (2001) 'On the "renormalization" transformations induced by cycles of expansion and contraction in causal set cosmology', *Physical Review D*, 63, 084026. gr-qc/0009063.

Krishna, P.B. and Mathew, T.K. (2017) 'Holographic equipartition and the maximization of entropy', *Physical Review D*, 96, 063513. arXiv:1702.02787.

Li, M. (2004) 'A model of holographic dark energy', *Physics Letters B*, 603(1-2), pp. 1–5. hep-th/0403127.

Madau, P. and Dickinson, M. (2014) 'Cosmic star-formation history', *Annual Review of Astronomy and Astrophysics*, 52, pp. 415–486. arXiv:1403.0007. (Eq. 15: $\psi(z) = 0.015\,(1+z)^{2.7}/[1+((1+z)/2.9)^{5.6}]$ M☉ yr⁻¹ Mpc⁻³.)

Padmanabhan, T. (2012) 'Emergence and expansion of cosmic space as due to the quest for holographic equipartition'. arXiv:1206.4916.

Rideout, D.P. and Sorkin, R.D. (2000) 'Classical sequential growth dynamics for causal sets', *Physical Review D*, 61, 024002. gr-qc/9904062.

Sorkin, R.D. (1997) 'Forks in the road, on the way to quantum gravity'. gr-qc/9706002.

Surya, S. (2019) 'The causal set approach to quantum gravity', *Living Reviews in Relativity*, 22, 5. arXiv:1903.11544. (Source, with Brightwell–Georgiou 2010, for the semiorder continuum-limit result cited in §7.)
