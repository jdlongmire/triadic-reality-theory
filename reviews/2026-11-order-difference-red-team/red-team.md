# Red-team pass: the order-difference reconstruction (NB-20261116)

- Target notebook: `reviews/2026-11-reconciliation-map/notebooks/NB-20261116-order-difference-reconstruction.md`
- Target computation: CMP-006, `reviews/2026-11-reconciliation-map/code/order_difference_reconstruction.py`
- Target text: `reviews/2026-11-reconciliation-map/reconciliation-map.md`, section 7.1
- Reviewer: thinx-muse, acting as red team under the peer-review profile (`0-program-methods/agents/peer-review-agent.md`). The reconstruction is thinx-claude's work; this pass is independent of its author.
- Requested by: thinx-claude (bridge, 2026-11-17). Authorized by: JD Longmire, 2026-11-17 05:11 CT.
- Date: 2026-11-17
- Disposition: confirming. No label change recommended (section 6).

## Verdict

Conclusion stands. The reconstruction's arithmetic is exact, its geometric prefactor is
correct, and its conclusion survives every alternative counting, noise model, and input
variation I could construct. The strongest rescue attempt found, counting elements in
causal (Alexandrov) intervals instead of spatial balls, softens the electron shortfall
from 20.3 to 13.1 orders of magnitude and the molecule shortfall from 40.9 to 26.6
orders. Nothing comes within twelve orders of rescuing the criterion for the molecule,
and nothing rescues the electron at the branch separation its apparatus imposes. The
G-cancellation is exact and structural: it follows from signal linear in the metric
perturbation combined with Poisson counting at Planck density, and it reappears in
every counting variant.

## 0. Independent reproduction

I recomputed CMP-006 from the stated setup with independent code (the 4-volume shift
obtained by numerical quadrature of h(r) = Gm/(r c^2) over the ball, not from the
closed form). Every headline number in the registered reference output reproduces:

- dV by quadrature vs closed form (2 pi prefactor): ratio 1.00000000 in both test cases.
- SNR for the electron at R = 1 um, T = 1e-8 s: 1.376510e10, matching CMP-006 to all
  printed figures, and invariant under G varied by ten orders of magnitude.
- Collapse times and shortfalls: electron 5.28e-29 s (20.3 orders) at R = 1 um,
  5.28e-27 s (18.3) at R = 10 nm, 5.28e-31 s (22.3) at R = 100 um; molecule 9.55e-44 s
  (40.9) at R = 266 nm, 2.54e-42 s (39.5) at R = 10 nm.
- The Diosi-Penrose contrast values also reproduce (1.90e30 s electron, 2.44e14 s
  molecule), which cross-validates the setup: a self-energy criterion retains G and
  behaves completely differently, so the cancellation is a property of the
  count-difference criterion, not of the arithmetic.

Confidence: HIGH. Falsifier: none applicable; this is a recomputation, and it matched.

## 1. Signal model: can a different counting rescue the criterion?

The reconstruction counts sprinkled elements in a spatial ball of radius R over a
duration T: signal dN = rho dV with dV the metric-perturbation integral, noise
sqrt(rho V), SNR = sqrt(3 pi) (mc/hbar) sqrt(R c T). I pressed on the counting, the
noise, the density, and the threshold, one at a time and in combination.

**1a. Branch-difference (dipole) counting.** The honest two-branch signal is the
difference of the two branches' perturbations, |h_A - h_B|, integrated over a common
region of radius L around both branches (separation R_sep = 1 um, electron, T = 1e-8 s,
numerical quadrature). SNR = 7.7e9 at L = 1 um, 6.7e9 at L = 3 um, 4.1e9 at L = 10 um,
giving collapse times 1.7e-28 to 5.8e-28 s, i.e. shortfalls of 19.2 to 19.8 orders.
Enlarging the region dilutes the SNR (the dipole signal grows like L, the noise like
L^(3/2)), so the reconstruction's single ball is close to the SNR-optimal region
choice: the reconstruction is generous to the hypothesis here, not unfair to it.

**1b. Causal-interval counting (strongest rescue found).** Count elements in an
Alexandrov interval (causal diamond) of proper time tau centred on the mass, the
counting causal-set practice itself uses to estimate volumes. The dimensionless
integrals are A = pi/24 (interval volume) and B = pi/6 (integral of 1/r over the
interval), so SNR = (B/sqrt(A)) (mc^2/hbar) tau with B/sqrt(A) = 1.447, and the
collapse time is 0.69 reduced Compton times, independent of R: electron 8.9e-22 s
(13.1 orders short of 1e-8 s), molecule 2.0e-29 s (26.6 orders short of 7.5e-3 s).
G cancels identically, because the same sqrt(rho) proportional to 1/G multiplies a
signal proportional to G. This variant is the one genuine softening the pass found:
for the electron it removes about seven orders of shortfall. It rescues nothing.

**1c. Link counting.** Counting links (covering relations) instead of elements gives
the same parametric form with coefficient sqrt(4 pi kappa/3), where kappa is the mean
number of links per element. For kappa from 0.5 to 50, far wider than any sprinkling
estimate, the electron collapse time at R = 1 um runs from 2.4e-28 s to 2.4e-30 s,
bracketing the ball result (5.3e-29 s) within a factor of about 100 at the extremes.
G cancels. No rescue.

**1d. Noise model.** Poisson noise is not a modelling choice on top of the sprinkling;
it is what a sprinkling is. The numbers show why no noise discussion can save the
criterion anyway: in the electron ball over 1e-8 s there are N = 1.8e122 elements and
the signal is dN = 1.9e71 elements. Even a unit noise floor (a single element) leaves
SNR = 1.9e71. The only noise model that suppresses the signal is fully correlated
noise (fluctuation of order N), which gives SNR = dV/V = mean h = 1.0e-51; that
contradicts the definition of a Poisson sprinkling, and it does not make the criterion
consistent with observation, it makes it vacuous: it would never fire for anything.

**1e. Density.** The hypothesis specifies Planck density. Since SNR scales as
sqrt(rho), rescuing the electron would require a sprinkling density 5.3e-21 of Planck
density, and the molecule 1.3e-41: that is abandoning the premise by 20 to 41 orders,
not reinterpreting it.

**1f. Threshold.** The hypothesis states actualization when the count difference
exceeds its Poisson noise, i.e. SNR = 1. Rescuing the electron requires a threshold of
1.4e10 and the molecule 2.8e20. No single threshold below 2.8e20 rescues both, and
any such threshold is a fitted parameter foreign to the stated criterion (the
notebook's circularity check already excludes fitted parameters).

**1g. Motion.** The electron at 50 kV has Lorentz factor 1.098; working in the
comoving frame changes the estimate at the ten-percent level. The molecule is
nonrelativistic. Not a lever.

Combined variations do not help either: the variants that soften the result (1a, 1b)
soften it by at most about seven orders (electron) against a shortfall of twenty, and
the molecule's shortfall exceeds forty orders under the ball counting and twenty-six
under the softest counting.

Confidence: HIGH. Falsifier: a counting within Poisson sprinkling at Planck density
whose signal is not linear in h, or whose fluctuations exceed sqrt(N) by ten or more
orders for the electron (twenty for the molecule). None is known to me, and 1d shows
the second would have to overcome a signal count of 1e71 elements.

## 2. Geometric prefactor

The prefactor is correct. Integrating h(r) = Gm/(r c^2) over a ball gives
int_0^R (1/r) 4 pi r^2 dr = 2 pi R^2 exactly, and my quadrature reproduces the
reconstruction's dV to eight figures. Under other defensible conventions (taking the
perturbation as 2Gm/(r c^2), or the volume-density perturbation with coefficient 1/2
or 2), the SNR moves by a factor of at most 2 and the collapse time by a factor of at
most 4, i.e. 0.6 orders. One honest caveat: the "4-volume shift" is slicing-dependent
at order-unity level (in Schwarzschild coordinates sqrt(-g) is exactly the flat
density), so the prefactor should be read as an order-unity quantity, which is all
the reconstruction claims. Nothing at the twenty-to-forty-order scale turns on it.

Confidence: HIGH. Falsifier: an error in the elementary integral; there is none.

## 3. Branch separation identified with R

I recomputed the collapse time across and beyond the claimed robustness range.
Electron shortfall (orders): 18.3 at R = 10 nm, 19.3 at 100 nm, 20.3 at 1 um, 21.3 at
10 um, 22.3 at 100 um. Molecule: 39.5 at 10 nm, 40.5 at 100 nm, 40.9 at 266 nm, 41.5
at 1 um, 43.5 at 100 um. The claimed robustness over 10 nm to 100 um is verified
exactly; the trend is monotone (smaller R, longer collapse time, as T proportional
to 1/R), so the scan's low end is the hypothesis's best case.

Extended scan, to locate what R would have to be. The electron is rescued only at
R = 5.3e-27 m or below; the molecule only at R = 3.4e-48 m, which is below the Planck
length (1.6e-35 m), and even at R equal to the Planck length the molecule still fails
by 12.7 orders. For the electron, the small-R escape is closed by the apparatus
itself: in Tonomura's interferometer the two branches pass on either side of the
biprism filament, which Hitachi's description gives as thinner than 1 um, so the
branch separation is of order 1 um by construction and cannot be 5.3e-27 m; the scan's
low end (10 nm) is already two orders below the smallest separation that apparatus
realizes. For Fein's interferometer, the interfering components are separated by
integer multiples of the grating period, so one period (266 nm) is the most
conservative defensible separation, and the notebook's own R = 10 nm case (39.5
orders) covers even a molecule-diameter reading of the separation.

Judgment: identifying R with the branch separation is the physically correct reading
of the hypothesis ("element-count difference between the branches"), and the values
used are the ones the two experiments impose.

Confidence: HIGH. Falsifier: documentary evidence that either experiment realizes
branch separations orders of magnitude below its grating period or filament diameter.
For the molecule, even that would not suffice short of sub-Planckian separations.

## 4. Coherence inputs against the primaries

**Tonomura et al. 1989.** Verified against the paper and the Hitachi laboratory's own
account: accelerating voltage 50 kV (paper, section III); electron speed about 0.41 c
(1.24e8 m/s); source-to-detector distance 1.5 m (paper). The flight time follows:
1.5 m at 1.24e8 m/s is 1.2e-8 s, and Hitachi's description states the transit through
the roughly one-metre microscope takes 1/100,000,000 of a second. The notebook's
"about 1e-8 s", flagged in the map as the reconstructor's estimate, is confirmed to
about twenty percent. It is not a soft input: halving the path would move the electron
shortfall by 0.4 of its 20.3 orders.

**Fein et al. 2019.** Verified against the paper's text: masses beyond 25,000 Da in a
library of molecules of up to 2,000 atoms (abstract); SiN gratings G1 and G3 of
266 nm period (full text; the optical grating G2 has the same 266 nm period); grating
spacing L = 0.98 m in a 2 m interferometer (full text). The notebook's 266 nm is
therefore a full-text value, better than the abstract-level verification its sources
field claims. The 7 ms coherence time I could not find as a printed number in the
paper. It is, however, pinned by the paper's own quantities: the de Broglie wavelength
down to 53 fm at 25 kDa implies a beam velocity near 300 m/s, so the G1-to-G3 transit
(1.96 m) takes about 6.5 ms, and slower velocity classes (150 m/s) give about 13 ms;
the Vienna group's public statement is that the molecules remained in a superposition
for more than 7 ms. The notebook's 7 ms (map text) and CMP-006's 7.5 ms both sit in
that band, and the shortfall is 40.9 orders at either value. Also in the
hypothesis's favour: CMP-006 uses exactly 25,000 amu, the bottom of "beyond 25 kDa";
the library ran heavier, which only shortens the predicted collapse.

Could not verify from the primaries: a printed "7 ms" sentence in Fein et al. itself
(verified instead by derivation from the paper's numbers plus the group's statement),
and the exact biprism filament diameter in Tonomura et al. (Hitachi's "thinner than
1 um" is all the argument needs).

Confidence: HIGH for Tonomura; MEDIUM-HIGH for the Fein coherence time (derived and
corroborated, not read). Falsifier: a primary-source coherence or transit time for
either experiment outside the bands above by an order of magnitude or more; no
plausible correction of that size exists in either apparatus.

## 5. Does the failure condition fairly test the hypothesis?

Yes, with two qualifications that do not rescue the criterion. The condition applies
the hypothesis exactly as stated (Planck-density count difference against its Poisson
noise, threshold at the noise) to two well-documented experiments, at the branch
separations those experiments realize, and asks whether the predicted collapse beats
the observed coherence. Sections 1 and 3 show the failure is not an artefact of the
reconstructor's region or R choices: the region is near-optimal for the hypothesis,
and the softest alternative counting still fails by 13.1 (electron) and 26.6
(molecule) orders.

Qualification 1: the words "for every physically reasonable branch separation R" do
real work for the electron, whose criterion is evaded below R = 5.3e-27 m. What makes
that evasion unreasonable is the apparatus geometry (section 3), which the record
should state as part of the test, as this pass now does. The molecule case needs no
such qualifier: it fails at every R down to the Planck length.

Qualification 2: the failure condition was written after the result was known. That
is disclosed in the notebook, and the research-records standard already prices it in
by capping a retroactive record at MEDIUM. A post hoc failure condition is a real
methodological cost in general; here it is mitigated by the fact that the condition
is the hypothesis's own consistency claim restated, and by the margin (thirteen
orders under the softest counting) being far larger than any plausible
condition-shopping could manufacture.

Confidence: HIGH. Falsifier: a formulation of the criterion, faithful to the
hypothesis's text, under which either experiment is consistent; sections 1 and 3 are
the search for exactly that and found none.

## 6. Bearing on the notebook's confidence and the charter's wording

On the charter: nothing found requires any change. Both features the charter reports
reproduce under independent recomputation and under hostile variation: G cancels
exactly, and the electron shortfall exceeds nineteen orders (20.3 at the
apparatus-imposed separation of about 1 um), so the charter's "more than nineteen
orders" is, if anything, understated. The charter's reliance on section 7.1 of the
reconciliation map is sound.

On the notebook's MEDIUM confidence: I recommend no change, and the reason matters.
The MEDIUM prices two things this pass cannot touch: the failure condition was fixed
retroactively, and the fidelity of the reconstruction to the programme lead's lost
original is unestablishable. Neither is a physics weakness. On the physics alone, this
pass found the falsification as robust as any order-of-magnitude argument in the
programme: exact arithmetic, a correct prefactor, hostile countings failing by
thirteen to forty-one orders, and inputs confirmed against the primaries. If the
programme ever separates "confidence in the falsification" from "confidence in the
record", the falsification itself would merit HIGH. Under the standard as written,
MEDIUM stands, and this record is the red-team evidence the notebook requested.

## 7. Immaterial notes (no number in the notebook or CMP-006 changes)

- The map's section 7.1 text says the molecule coherence is about 7 ms while CMP-006
  computes with 7.5 ms. The shortfall is 40.9 orders at both values (40.86 vs 40.89).
  A future log entry by the notebook's owners could align the text to the code value.
- The notebook's sources field labels Fein et al. as primary_abstract; the 266 nm
  grating period is in fact stated in the paper's full text. The verification label
  could honestly be raised for that input by the owners; I have not changed it.

## Recommendations

- Label move: none. Notebook confidence stays MEDIUM for the recorded procedural
  reasons; result and failure condition untouched by this pass.
- Charter wording: no change indicated.
- The two notes in section 7 are for the notebook's owners to pick up in a future log
  entry if they wish; neither affects any conclusion.

Reviewer: thinx-muse (red team). Attribution: Human-Curated, AI-Enabled (HCAE).
