# ADCE Targets 3 and 5: A-SAT Dissolution and the Bridge-Law Scan

**Status:** working report (belt-level, physics-facing) · **Claim:** [OPN-008](../../traceability/claims/OPN-008.yaml) · **Parent:** [adce.md](adce.md) (v3.1) · **Code:** [code/adce_bridge_scan.py](code/adce_bridge_scan.py) · **Prior review:** [2026-07 red-team](../../reviews/2026-07-redteam-adce/review.md)

This report executes the two items promoted at the close of the v3.1 cycle: **Target 3** (capacity bound and saturation axiom) and the FLRW-level portion of **Target 5** (the growth-law toy model, run against the red-team's severe test). The discrete CSG benchmark against Ahmed and Rideout (2010) remains open; §7 states what this report's results imply for how it should be scoped.

Summary of findings, stated up front:

1. **Target 3 closes negatively: A-SAT dissolves under the declared two-level structure.** At the substrate level it is an identity that cannot force expansion; at the record level it is empirically false by ~100 orders of magnitude. The capacity-forcing route is closed *for the two declared levels* — not universally: a mesoscopic, Jacobson-type horizon-thermodynamic level (entropy saturated on causal horizons *and* geometry-sensitive) is not covered by the dichotomy, remains a standing route, and is — this must be said plainly — the same territory the report's surviving branch trades on (§2).
2. **The mandatory deliverable (a) is achieved at background-morphology level only**: a growth law with a deceleration-to-acceleration transition exists in the natural grid — self-feedback rate with diluted-stock bridge — and v2's boxed relation $H = \lambda/3$ is recovered as a genuine *attractor*, not an assumption (§4.2). Its costs: the rate constant $\lambda \approx 3H_0$ is hand-set (the coincidence problem relocated; two tuned dials, $\mu$ and $\lambda$ — the same parameter count as CPL itself); it sits in the freezing-quintessence quadrant ($w_0 > -1$, $w_a > 0$), which DESI DR2 disfavors; and it carries a **permanent ~14% dust-like tracker through recombination** whose early-universe viability is unestablished (§4.2 — post-review disclosure).
3. **The severe test fails across the natural grid — every cell, including the horizon cell.** No {source} × {bridge} cell reproduces the DESI-preferred shape (sign-stable, late-peaking $\rho_A$, crossing at $z \approx 0.35$–$0.50$). The nearest morphological match locks its peak to cosmic noon ($z \approx 2.1$), a factor ~5 too early; the horizon cell fails the same interior-peak criterion and under-accelerates. The honest ranking is: no cell passes; the horizon cell fails least, and in the observed direction (§4.3–4.4).
4. **One probe (not three) selects horizon coupling as the least-dead branch.** The scan and the inverse problem are the same B1-conditional computation run forward and backward against the same DESI history, and the magnitude table's horizon row is a consistency identity, not evidence (§6). What that single probe establishes: under diluted-stock bookkeeping, the DESI history requires a source *rising* into the late era; no matter-processing source does that; horizon area does (§5, §7). (This summary supersedes the pre-review "three independent probes converge" framing — red-team vector 7, accepted.)

## 1. Setup inherited from v3.1

The two-level structure of adce.md §9.4 is taken as given: the substrate count $N_P$ (one element per Planck 4-volume; CST kinematics; inert) and the record count $N_R$ (physical record-forming events; the only level where dynamics can live). The v3.1 reformulated hypothesis makes expansion the registration of *accelerating* actualization; the open question is whether any natural record-sector growth law, mapped to stress-energy by some bridge law, produces the observed expansion history.

Observational anchors (verified against primaries this cycle): DESI DR2 w0waCDM fits span $w_0 = -0.42$ to $-0.84$, $w_a = -1.75$ to $-0.62$ across SN combinations (2.8–4.2σ over ΛCDM; arXiv:2503.14738); the phantom crossing sits at $z_c \approx 0.35$–$0.50$ (DESI's own statement: $z_c \simeq 0.45$; arXiv:2503.14743), and $\rho_{DE}$ peaks *at the crossing* (an identity of $w_0w_a$CDM: $d\ln\rho_{DE}/d\ln a = -3(1+w(a))$), only 7–40% above today's value — the required non-monotonicity is mild. Reference values used below: the DESY5 combination $w_0 = -0.752$, $w_a = -0.86$, giving peak/crossing $z^* = 0.405$.

## 2. Target 3: the capacity bound dissolves rather than closes

v3.1 left A-SAT ("actualization proceeds at the maximal rate the capacity bound admits; $\rho_A \to \rho_{A,\max}$") as a named, load-bearing, underived axiom, with the red-team's direction-of-explanation fork recorded against it. Executing Target 3 under the two-level split resolves the fork by *dissolving the axiom*:

**At the substrate level ($N_P$), saturation is an identity and cannot force anything.** CST discreteness is not the claim that element density *approaches* a bound; it is the claim that spacetime *is* a causal set whose elements realize 4-volume at fixed Poisson density $\rho_4 = \rho_{Planck}$ (Bombelli–Lee–Meyer–Sorkin 1987). There is no dynamical achievement in "$\rho_4$ at its bound" — that is the content of the number–volume correspondence itself. And because the bound is 4-volume-referenced, it is *geometry-neutral*: any spacetime, static ones included, accumulates 4-volume and hence elements at exactly $\rho_{Planck}$. This is the static-universe refutation of the red-team pass, restated as a structural fact about where the bound lives. A capacity bound can only force spatial expansion if it binds against a quantity that *fails to grow in a static geometry* — and the substrate bound does not.

**At the record level ($N_R$), saturation is empirically false.** The realized record density sits at least ~100 orders of magnitude below Planckian or holographic capacity (adce.md §9.4). No bound is being approached; no saturation dynamics can be invoked. A-SAT at this level does no work because it is simply not true.

**Conclusion — scoped.** For capacity-based forcing, one needs a level where the bound both *binds* and is *geometry-sensitive*. The substrate level gives binding without geometry-sensitivity; the record level gives neither. Within the declared two-level structure, no level gives both, so the forcing route through capacity is closed *for that structure* and A-SAT is retired from the framework. **What the closure does not cover (post-review):** the argument surveys the two declared levels; it proves no dichotomy lemma that every possible level is either identity-bound or unbound. A concrete third-level candidate exists in the published literature — Jacobson-type horizon thermodynamics, where entropy *saturated* on local causal horizons ($\delta Q = T\delta S$ with $S = A/4$) is geometry-sensitive enough to yield the Einstein equations. A mesoscopic horizon-screen level could in principle bind and respond. That route is not closed; it is also, without coincidence, the same territory as the horizon-coupled branch this report ends up selecting (§7) — meaning the extremal-principle escape and the surviving branch have effectively merged into one open problem: a horizon-thermodynamic derivation of the bridge law. What survives of Target 3 is a redistribution of load: the entire dynamical content of ADCE now lives in the **bridge law** $B$: the map from the record sector to effective stress-energy,

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
| S4(λ=3H₀)×B1 (feedback, diluted) | ✗ (0.18; see §4.2) | −0.53 | 0.47 | none | none | (−1.05, +0.97)* | **deliverable (a)** at background level: de Sitter attractor $H^* = \lambda/3$; permanent ~14% early tracker |
| S4×B2 | ✓ | −1.2…−1.9 | ~0.5 | none | none | deep phantom | super-accelerating; excluded |
| S5×B1 (horizon, diluted) | ✓ | −0.11 | 0.53 | (z≈15, artifact) | none | (−0.58, −0.28) | **only DESI-quadrant cell**; acceleration too weak |

*\*CPL fit over $a \in [0.5,1]$; for S4×B1 the fit exaggerates $w_a$ because $w_A(a)$ is strongly non-linear near the attractor; the pointwise values are $w(0) = -1.00$, $w(0.5) = -0.74$.*

### 4.1 Analytic structure confirmed numerically

The two exact relations of §3 hold in the numerics to grid precision (B1 cells cross $w=-1$ exactly at their $\rho_A$ peak; B2 cells never cross). The B1/B3 degeneracy under S4 ($\dot N \propto N$ makes rate and stock proportional) is exact in the output — a consistency check, not a finding.

### 4.2 Mandatory deliverable (a): the feedback attractor

S4×B1 — records with fixed energy $\mu$ diluting as $a^{-3}$, formed at rate $\dot N_R = \lambda N_R$ — has a genuine de Sitter attractor: if $H > \lambda/3$ the stock dilutes faster than it grows and $\rho_A$ falls; if $H < \lambda/3$ it is phantom and $\rho_A$ rises; the fixed point $H^* = \lambda/3$ is approached from either side. **v2's boxed toy-model relation $H = \tfrac13 \dot N/N$ is thereby recovered as an attractor of a specific bridge law rather than as a kinematic assumption** — the strongest positive result of the scan. With $\lambda = 3H_0$: matter era intact ($\rho_A/\rho_m \approx 0.18$ at $z=5$), acceleration onset $z_{acc} \approx 0.47$, $w$ today $= -1.00$.

Costs, stated plainly: (i) $\lambda$ is a free parameter, and the observed acceleration requires $\lambda \approx 3H_0$ — *why is the channel-opening rate the present Hubble rate?* This is the coincidence problem relocated, not solved; exactly the disease of generic quintessence. With $\mu$ also tuned, deliverable (a) is achieved with **two dials — the same parameter count as CPL itself** (red-team vector 3, accepted). (ii) The approach to the attractor is from $w > -1$ with $w$ *decreasing* over time — the freezing-quintessence quadrant ($w_a > 0$ in CPL terms), which is the opposite of DESI DR2's preferred quadrant. Not excluded (ΛCDM itself sits within DESI's 2.8–4.2σ), but disfavored by the current best data. (iii) **The early-universe tracker (post-review disclosure; red-team vector 4, reproduced and accepted).** Because $\rho_A \propto e^{\lambda t}/a^3$ and $e^{\lambda t} \to 1$ at early times, the cell carries a *constant* dust-like fraction of the matter budget deep into the early universe: $\rho_A/\rho_m = 0.180$ at $z=5$, asymptoting to $0.144$ — verified through $z = 9000$, with $w_A = 0.000$ at recombination. "Matter era intact," as this report's first draft put it, was wrong: 0.18 at $z=5$ fails the scan's own $<0.1$ criterion, and a permanent ~14% smooth addition to the matter budget through recombination is either relabeled dark matter (if it clusters — criterion-12 disease at the matter end) or in immediate tension with Planck's percent-level $\Omega_m h^2$ and growth constraints (if it does not). No perturbation-level treatment exists. Deliverable (a) is therefore claimed at **background-morphology level only; early-universe viability unestablished.**

### 4.3 The severe test fails on the natural grid

No cell passes. The instructive failure is S1×B1: it produces exactly the demanded *morphology* — sign-stable, non-monotone $\rho_A$ with an interior peak, phantom crossing at the peak, in the correct direction (phantom in the past, $w > -1$ after) — but the peak sits at $z \approx 2.11$ (resolution-stable), locked to cosmic noon, because under B1 the peak occurs where $d\ln N_R/d\ln a = 3$, and for any source tracking astrophysical processing that threshold is crossed shortly after the SFH begins its post-noon decline. The observed peak is $z^* \approx 0.35$–$0.50$. A factor ~5 in epoch separates the natural astrophysical-record model from the data, and by $z=0$ its $w \approx -0.11$: essentially dust, no acceleration today.

### 4.4 The horizon cell

S5×B1 ($N_R \propto H^{-2}$, i.e. record stock tracking apparent-horizon area) is the only natural cell that is **both in the DESI quadrant and accelerating**: $(w_0, w_a)^{fit} = (-0.58, -0.28)$, sign-stable. (Stated precisely, post-review: S1×B1 and S2×B1 also land in the $w_0 > -1$, $w_a < 0$ quadrant by CPL fit — but with $q_0 > 0$; the quadrant claim without the acceleration qualifier was false as first worded. And by the composite shape criterion used to kill S1×B1 — interior peak at $0.1 < z < 1$ — **S5 fails too**: its $\rho_A$ maximum is a real but nearly flat radiation-era feature at $z \approx 15.5$ (9.6% variation over $z \in [3,30]$; "artifact" was the wrong word in the first draft). The criterion is now applied symmetrically: *no cell passes the severe test; S5 fails least, and in the observed direction.*) During matter domination $\rho_A \propto H^{-2}a^{-3} = $ const — $w = -1$ exactly, by the same algebra that makes Hubble-cutoff holographic dark energy Λ-like in that era. But self-consistently it cannot complete the job: as $\rho_A$ dominates, $H \to$ const forces $\rho_A \propto a^{-3}$, i.e. $w \to 0$; the acceleration self-limits ($q_0 = -0.11$ vs. observed $\approx -0.55$). This is the known pathology of Hubble-scale holographic dark energy (Hsu 2004); the cure in that literature — a future-event-horizon cutoff (Li 2004) — has a well-known acausality cost. The cell fails as it stands, but it is the *only* natural cell pointing in the observed direction.

## 5. The inverse problem: what source would DESI require?

Under B1, invert the DESY5-combination history exactly: $N_R^{req} = a^3 \rho_{DE}(a)$, $\sigma^{req} = dN_R^{req}/dt$. Results (resolution-stable):

- $\sigma^{req}(z)$ is **non-negative everywhere** (no record destruction needed — sign-stability is achievable; robust across all four DR2 dataset combinations), and **rises steeply from $z \geq 1$ into the acceleration era**: for the DESY5 combination it peaks at $z = 0$, at 2.8× its $z=1$ value and ~25× its $z=4$ value. (Combination dependence, post-review: the peak sits at $z = 0$ for DESY5 and Pantheon+, $z = 0.06$ for Union3, $z = 0.29$ for DESI+CMB alone — "rises into the late era" is the combination-robust statement; "monotone to $z=0$ exactly" is not.)
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

The astrophysical rows all yield *unexplained* scales (why 8 eV? why 13 GeV?) — and each fails the shape requirement independently (CMB photon count is comoving-constant: $d\ln N/d\ln a = 0$ gives $w = 0$ under B1). The horizon row sits within a factor ~1.4–1.7 (volume-convention-dependent) of $k_B T_{dS} = \hbar H_0/2\pi = 3.7 \times 10^{-53}$ J, the de Sitter temperature. **This row is a consistency identity, not a probe (post-review correction; red-team vector 6, reproduced and accepted).** The ratio has the closed form $\mu / k_B T_{dS} = \Omega_\Lambda \cdot (c/H_0 R_{CEH})^2$ (Hubble-volume convention; $= 0.59$, verified) — it is *fully* determined by $\Omega_\Lambda$ and a kinematic radius ratio, contains no information about records or actualization, and could not have failed to land near $\hbar H_0$ for any horizon-referenced inventory, by dimensional analysis. The first draft's "partially guaranteed" understated this; "fully guaranteed given the inputs" is correct. What survives is strictly comparative and weak: the astrophysical rows' scales are unrecognized numbers; the horizon row's is a recognized one — because it was built from one.

## 7. Synthesis and program consequences

**One probe, one direction (restated post-review; supersedes the first draft's "three probes converge").** The red-team correctly refused the triangulation framing: the scan (§4) and the inverse problem (§5) are one B1-conditional computation run forward and backward against the same DESI history, and the magnitude table's horizon row is an identity (§6). What the *single* probe establishes is nonetheless real and directional: under diluted-stock bookkeeping, the DESI history requires a record source **rising into the late era**; every matter-processing history falls there; horizon area rises there. *If* the mean-growth mechanism describes dark energy, actualization must be **horizon-coupled** — supported by one probe and one identity-grade consistency check, not three independent lines. The record-sector-as-astrophysics reading of ADCE is under direct pressure from its own severe test: its natural cells fail to accelerate, sit in the disfavored quadrant, or peak at cosmic noon instead of $z \approx 0.4$.

**Falsification-criteria adjudication for this cycle (obligation carried from v3.1's degeneration clause, flagged by red-team vector 10):** Criterion 4 — *fired and absorbed*: A-SAT can indeed not be derived or independently motivated (that is the content of §2); the v3.1 reformulation plus the bridge-law re-posing is the required substantial revision, registered here. Criterion 15 — **partially fired at the FLRW level**: the only transition-producing cell needs a hand-set $\lambda \approx 3H_0$ and delivers $z_{acc} \approx 0.47$; a CSG-natural derivation of $\lambda$ is the named repair, and absent one this criterion completes. Criterion 5 — *standing watch*: both surviving branches currently fit its description (couplings chosen to reproduce the observed scale). Criterion 12 — *acute on the horizon branch*, as stated throughout.

**The criterion-12 risk is now acute and must be named.** A horizon-coupled ADCE is structurally adjacent to holographic dark energy (Li 2004) and to horizon-thermodynamic approaches (Padmanabhan; and Sorkin's everpresent Λ is horizon-adjacent via $V_4$). For the branch to be ADCE rather than a relabel, it must supply what those programs lack: an *ontology of the horizon as actualization locus* (horizon crossings as irreversible causal facts — a record-formation reading of horizon-area growth) **and** at least one prediction that separates it from generic HDE. Absent both, criterion 12 fires and the honest disposition is absorption.

**The CSG microdynamics claim, restated as the conjecture it is (post-review; red-team vector 8, accepted).** The first draft asserted "CSG natively selects the feedback branch." That inference commits a level slip the program's own §9.4 architecture forbids: the percolation and cosmic-renormalization results — transitive percolation $t_n = t^n$ as the unique fixed-point family (Martin–O'Connor–Rideout–Sorkin gr-qc/0009063), the exponentially-expanding de Sitter-like post-bounce phase Ahmed–Rideout fit — are statements about **substrate element birth ($N_P$)**, the level at which ADCE "inherits CST unchanged and adds nothing dynamical." No CSG result constrains the record-sector source $\sigma$ or the bridge law $B$ (confirmed literature gap in both directions: neither a horizon-referenced nor a record-sector feedback law has been derived from any covariant $t_n$ family). And at the substrate level, "exponential $N$ growth in proper time" is, by the dictionary this program's §6 warns about, de Sitter geometry restated — a kinematic identity cannot side with a bridge law. The defensible statement is a named conjecture: **Inheritance conjecture (open):** *record formation tracks the substrate's growth morphology* — under which, and only under which, generic CSG dynamics motivates the feedback branch. Additionally, any future CSG benchmark can only certify a coarse-observable correspondence: Glaser–Surya (arXiv:1309.3403) showed Ahmed–Rideout's own parameter cases fail the interval-abundance manifoldlikeness test, and CSG continuum limits are semiorders with no spatial structure (Brightwell–Georgiou, via Surya 2019) — the de Sitter phase is real in the volume-vs-proper-time observable at finite $n$ between posts, and only there.

**Revised target queue** (supersedes the v3.1 §15 ordering for the affected items):

1. ~~Target 3 (capacity bound + A-SAT)~~ — **closed negative** this report (§2): A-SAT dissolved; capacity-forcing route closed in principle; extremal-principle escape (Krishna–Mathew shape) remains the only reopening.
2. **Target 4′ (re-posed): derive the bridge law** — now specifically: derive a horizon-coupled bridge from the actualization ontology, with the freezing-quintessence attractor (S4×B1, §4.2) as the fallback branch if the DESI preference weakens toward ΛCDM in DR3+.
3. **Target 5 (CSG benchmark, still open — scoped by the inheritance conjecture)**: the substrate-level literature answer (percolation fixed point, exponential growth) transfers to the record sector only under the inheritance conjecture above. The discrete work is therefore two problems: (i) test whether any covariant $t_n$ family yields a horizon-referenced effective law (none known; confirmed gap); (ii) give the inheritance conjecture content or refute it — both bounded to coarse observables by the Glaser–Surya manifoldlikeness ceiling.
4. **Falsification watch (the program's sharpest structure)**: the attractor branch and the DESI-preferred quadrant are *mutually exclusive* ($w_a$ of opposite sign); the CSG microdynamics motivates the attractor branch *conditionally on the inheritance conjecture*. DESI DR3 / Euclid tightening of $(w_0, w_a)$ adjudicates for free: if the phantom-crossing preference strengthens, the feedback branch dies (and with it the conjecture's relevance) and ADCE survives only as horizon-coupled actualization with no microdynamical derivation and an acute criterion-12 risk; if the preference dissolves toward ΛCDM, the horizon branch loses its motivation and the surviving object is the freezing attractor — with a relocated coincidence problem, an unestablished early-universe tracker (§4.2), and criteria 5/15 one unfixed parameter from completing. Neither outcome is comfortable; both are informative, and the discomfort is quantifiable in advance.

**What did NOT survive this cycle:** A-SAT (dissolved); the astrophysical-record reading of the source (all its cells dead on shape or epoch); any remaining hope that the severe test could be passed without horizon reference.

**What survives:** the reformulated (v3.1) hypothesis, now with exactly two damaged-but-live realizations — the feedback attractor (deliverable (a) at background level; disfavored quadrant; relocated coincidence; unestablished ~14% early tracker; criteria 5/15 partially fired) and horizon-coupled actualization (in-quadrant and accelerating but failing the shape test itself; no complete model; acute criterion-12 risk; now merged with the Jacobson-type extremal route as one open problem). In the red-team's summary sentence, accepted as this cycle's honest close: **one probe, two damaged branches, one scheduled execution date.** Per the programme methodology, the narrowings are recorded negatives, and the mutual-exclusivity of the surviving branches is the most decision-useful structure ADCE has yet produced.

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
