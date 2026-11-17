# TRT Reconciliation Map: Hard Core, Prior Art, and the Charter Objective

**Status:** Draft for the programme lead's ruling. Nothing here is filed, and no claim, label, or governing text has been changed.
**Date:** 2026-11-16
**Prepared by:** Claude (AI collaborator), at JD Longmire's direction.
**Repository state read:** `jdlongmire/triadic-reality-theory` at 23befa9 (merge of PR #33).

---

## 1. Purpose

The programme currently has two layers. The paper (v0.10), the ROADMAP (v0.2), and most of the belt carry the June to September line: co-admissibility, the Logical Resolution Model, holonomy gravity. The charter and objective filed 2026-11-09 carry a newer line: discrete A-events, causal-set recovery of spacetime, order and redundancy selection, the Tsirelson bound, Persistence of Zero, and the source commitment. The hard core is consistent with both.

This document places every prior item under the charter, states what each becomes, and identifies where the objective is met or lost. It also reconstructs the content of `TRT-working-notes.md`, which the charter cites and the repository does not contain.

## 2. Provenance and confidence

Three kinds of statement appear below, and they are kept apart.

- **Repository fact.** Read directly from the files named. Confidence HIGH.
- **Verified external.** Checked this session against the primary abstract or text. Marked [V]. Confidence HIGH on what the abstract states, MEDIUM on details beyond it.
- **Reconstruction or proposal.** My inference or my construction. Marked [R]. These are not JD's notes and must not be cited as such. Confidence stated case by case.

Items resting on general knowledge that I did not verify this session are marked [U].

## 3. The reconciling thesis

Three sentences carry the reconciliation.

1. **Everything unitary lives in D.** The charter states that unitary evolution is internal structure of D and no instance of A. Decoherence, einselection, pointer states, and the quantum state itself therefore belong to D.
2. **Everything discriminating lives at D → X.** A criterion defined over D alone can only re-describe the physics of D. Novel content must come from the rule by which A fixes the actualized event algebra, which is charter obligation (b).
3. **Everything geometric lives in X.** Time and geometry are recovered from the order and number of A-events. Gravity questions must be posed on that order.

The June negative on co-admissibility is what sentence 1 predicts. That observation is legitimate only if sentence 2 is honoured with a new, exposed falsifier. Without one it is post hoc accommodation, which METHODOLOGY classes as degenerating. Sections 6 and 9 supply the candidate.

## 4. Typing before placement

A typing gap has to be closed first, because the two layers use "A" at different types.

- **Lean core** (`Core/Primitives.lean`): `A : ActualizableState → ActualizableState → Prop`. A is a relation on D. `Obtains` is a separate predicate.
- **Charter:** A-events are individuated elements that form a partial order and constitute X.
- **Paper §6.5:** A "crosses the boundary" from admissible to actual.

These agree once an A-event is typed as an occurrence. Proposal [R]:

> An **A-event** is a pair e = (d, d′) with A(d, d′) and Obtains(d′). X is the set of A-events. The order on X is supplied by the condition-of-actualization relation defined in §7.2.

On this typing A stays a transition relation as the 2026-11-12 ruling requires, actualization stays a role, and the charter's event language becomes well formed. The quantum state is a structure in D, which matches the paper's ontic-admissible reading.

One open typing question is flagged for ruling. WP-TRT-QSA-0001 allows that a physically instantiated quantum state "can itself be actual" (`Inst(σ)`). The charter places the state in D. Either `Inst` is a status inside D, or the QSA package and the charter disagree.

## 5. Placement map

| Prior item | Source | Placement under the charter | Resulting status |
|---|---|---|---|
| Co-primitives, R → D → X, irreducibility | hard core, ONT-001 to 004 | Unchanged. Charter obligation 1. | Stands |
| Scoped Excluded Middle | 11-12 ruling, LOG-001 | Identical to the charter's "scoped definiteness". | Stands; paper §6.5.3 wording to conform |
| Quantum state as admissible structure, PBR reading | paper §6.5 | Structure of D. | Stands; `I_L3` notation retired |
| LRM stage 1 (co-admissible set = pointer set) | paper §6.6.1, OPN-001 | Physics of D. Imported decoherence. | Reclassified as interpretation, per the 06-26 negative |
| Co-Admissibility Conjecture (decoherence form) | paper §13.1, PRD-001 | Tested on D alone. | Recorded negative for tested forms; status call pending since June |
| LRM stage 2 (one outcome actualizes) | paper §6.6.2, OPN-002, OPN-004 | Charter obligation (b): the selection rule. | The live discriminating front |
| Born measure | OPN-004, WP-BORN-0001 | Quantal measure on histories; strong positivity is the key property. | Open; see §8 on circularity |
| Variational desideratum δS[χ] = 0 | paper §5, OPN-005 | Amplitudes and action functional belong to D; the measure on histories carries them to X. | Open; reposed |
| FLL bivalence hypothesis | TRT-FLL model, OPN-009 | Empirical form of the charter's logical-realism commitment. | Should be a charter failure condition |
| "Where does L act?" | TRT-FLL model §3 | On the actualized event algebra of X (the fourth listed option). | Answered by the charter, MEDIUM |
| FLL-0002 first decision (AOE or context-indexed bivalence) | WP-TRT-FLL-0002 | The charter's logical realism entails absoluteness of actualized events. TRT gives up locality at A's selection. | Answered by the charter, MEDIUM |
| Gravity positioning (§10.1) | paper | Interpretive, as the paper already says. | Stands |
| Linearity crux, Regge route | ROADMAP 3.1, PRD-002, WP-GRAV-0001 | Must name its substrate. See §6.3. | Open; substrate ruling needed |
| ADCE cosmology | OPN-008, EXT-002 | Already on the causal-set substrate. | Unchanged |
| Dynamic Stability Principle | 10-25 assessment | The charter puts continuous grounding in the source's will-relation, which "is not an instance of A". That is the assessment's option 3. | Resolved toward option 3, MEDIUM |
| Effectiveness of mathematics | PRD-003 | Unchanged. | Stands (retrodiction) |
| Great Selector, grounding modes | charter | Hard-core adjacent commitment with a secular presentation rule. | Needs a claim entry and a tier |

Charter commitments with no registry entry at all: discreteness, local finiteness, order selection, redundancy selection, the Tsirelson obligation, Persistence of Zero, and the source commitment. METHODOLOGY requires each to carry a role, dependencies, and a failure condition.

## 6. Prior art the charter imports

The charter's physics vocabulary comes from two established programmes. Stating the import openly is what keeps TRT's own contribution visible.

### 6.1 Causal set theory and the histories programme

- Spacetime as a locally finite partial order, with geometry from order and number: Bombelli, Lee, Meyer and Sorkin (1987). Already in the registry as EXT-002.
- Classical sequential growth: Rideout and Sorkin (2000) derive a family of stochastic growth dynamics from discrete general covariance and Bell causality [V]. The charter's obligation (c) replaces Bell causality with Persistence of Zero plus strong positivity.
- Stem events: for generalized percolation models, the stem sets generate the covariant measurable sets up to measure zero (Brightwell et al. 2003) [V]. This is the source of the charter's "order-invariant (stem) events".
- Quantum measure and preclusion: Sorkin (1997) treats the quantal measure as a propensity and gives a criterion under which measure zero implies preclusion [V].
- Strong positivity and Tsirelson: Craig et al. (2007) obtain a Tsirelson-type inequality from a joint quantal measure; their proof uses the fact that every strongly positive quantal measure admits an associated Hilbert space [V].
- Persistence of Zero: proposed by Sorkin (2019 Perimeter talk) as a causality condition for quantum causal sets [V for existence and purpose; the precise statement is U].

### 6.2 Redundancy

The charter's working channel, a distinction recorded in at least two disjoint and causally independent regions, is the redundancy idea of quantum Darwinism. Riedel, Zurek and Zwolak (2016) define redundancy of a history through orthogonal records on subsystems and propose it to reduce the set-selection problem [V].

### 6.3 The gravity substrate

WP-TRT-GRAV-0001 works on a finite relational graph with group-valued edges and reaches Einstein-Hilbert through Regge calculus if the measure is linear in the deficit. The charter makes the actual a causal set, which carries order and number only.

Causal set theory has its own route to curvature. Benincasa and Dowker (2010) construct a scalar-curvature analogue and an action whose continuum limit is Einstein-Hilbert, and they note the natural suppression of curvature-squared and higher terms [V]. Later work supports Einstein-Hilbert plus a boundary term (Machet and Wang 2020; Dowker 2021) [V].

Consequence [R], confidence LOW to MEDIUM: the linear-versus-quadratic question can be reposed on the A-order as "is the L₃-natural measure on a causal set one whose continuum limit is the Benincasa-Dowker action?" That keeps the fork and its observational content while removing the unexplained second substrate. GRAV-0001 as written remains a valid finite computation; it needs a stated bridge from its graph to the A-order, or an explicit statement that it is a toy model.

## 7. Reconstruction of the missing working notes

All of §7 is [R].

### 7.1 The order-difference falsification (charter's "§4.5")

The charter reports that the gravitational order-difference criterion fails because G cancels from the signal-to-noise ratio at Planck density, and that it predicts collapse of electron and molecular superpositions more than nineteen orders of magnitude too fast. The following independent rebuild reproduces both statements.

Setup. Sprinkle at Planck density ρ = l_P⁻⁴. A mass m perturbs the metric by h(r) ≈ Gm/(rc²). Over a region of spatial radius R and duration T, the 4-volume shift is δV ≈ (Gm/c²)(2πR²)(cT), against V = (4/3)πR³cT. Two branches of a superposition separated by about R differ in element count by about ρδV, against Poisson noise √(ρV).

Result.

SNR = ρδV / √(ρV) = √(3π) · (mc/ħ) · √(RcT)

G cancels identically, because √ρ = c³/(ħG) and δV ∝ G. Varying G by ten orders of magnitude leaves the computed SNR unchanged to seven figures. The sensitivity is set by the Compton wavelength, where a Diósi-Penrose estimate is set by gravitational self-energy and retains G.

Setting SNR = 1 gives a collapse time T = λ̄_C² / (3πRc), with λ̄_C = ħ/(mc).

| Case | Predicted collapse time | Observed coherence | Shortfall |
|---|---|---|---|
| Electron, R = 1 µm | 5.3 × 10⁻²⁹ s | ~10⁻⁸ s | 20.3 orders |
| Electron, R = 10 nm | 5.3 × 10⁻²⁷ s | ~10⁻⁸ s | 18.3 orders |
| 25 kDa molecule, R = 266 nm | 9.6 × 10⁻⁴⁴ s | ~7 × 10⁻³ s | 40.9 orders |

Inputs: electrons at 50 kV in a biprism interferometer (Tonomura et al. 1989) [V for voltage; the 10⁻⁸ s flight time is my estimate, U]. Molecules beyond 25 kDa in a 2 m interferometer with 7 ms coherence (Fein et al. 2019) [V; the 266 nm grating period is U].

Assessment. The rebuild matches the charter's two reported features: exact G-cancellation and a shortfall of about twenty orders for electrons at micron scale. Confidence that this is the calculation the notes contained: MEDIUM. Confidence in the conclusion that the criterion is falsified: HIGH, since no plausible choice of R rescues it. The geometric prefactor and the choice of R are mine. Code: `code/order_difference_reconstruction.py`, reproducible, no fitted parameters.

### 7.2 A candidate for obligation (e): condition of actualization

Definitions.

- For an A-event e, let Cond(e) be the set of A-events whose obtaining is required for e to obtain.
- Write f ≺ e when f ∈ Cond(e).

Two axioms.

- **EPA (exclusion of prior actuality).** e ∉ Cond(e). An event's obtaining is never among the conditions of its own obtaining. This is the event-level form of the charter's phrase, and it is where Non-Contradiction enters: if e ∈ Cond(e), then e must obtain as a condition and must fail to obtain independently of the transition that yields it, in the same respect.
- **TC (transitivity of conditioning).** If g ∈ Cond(f) and f ∈ Cond(e), then g ∈ Cond(e).

Proposition. ≺ is a strict partial order, hence acyclic.
Proof. Irreflexive by EPA, transitive by TC. A cycle e ≺ f ≺ e gives e ≺ e by TC, contradicting EPA. ∎

Audit of what this does and does not deliver.

- Irreflexivity is argued from L₃. Acyclicity follows only with TC. TC is a claim about what "condition" means and is the real premise. It is plausible and it is separate from the conclusion, so the derivation is non-circular but modest.
- Individuation of events follows from L₃ Identity, as the charter says.
- **Local finiteness is not derived.** It remains a posit about A, as the charter states. It is also the property on which the whole causal-set recovery depends.
- The hard core's definition of A does not contain "exclusion of prior actuality"; only the charter's definition does. EPA should be entered as an explicit axiom with its own registry claim.

### 7.3 A sketch for obligation (d′): Persistence of Zero from L₃ and A

Target, informally [U on exact form]: if an event E has measure zero, then E ∩ B has measure zero for every event B to its future.

Step 1. By the preclusion rule, μ(E) = 0 implies E does not obtain.
Step 2. Scoped Excluded Middle makes "E does not obtain" a determinate actualized proposition. By EPA and acyclicity, no later A-event is a condition of an earlier one, so later events cannot alter it.
Step 3. By Non-Contradiction, if E does not obtain then no refinement E ∩ B obtains.

Steps 1 to 3 show that E ∩ B does not *obtain*. Persistence of Zero requires that E ∩ B has *measure zero*. The step from "does not obtain as a matter of law" to "has measure zero" is not supplied by L₃ or A. It needs a bridge:

> **Logical Closure of Preclusion (LCP).** If the preclusion of E entails, by L₃ alone, the preclusion of F, then μ(F) = 0.

With LCP, Persistence of Zero follows. LCP says the measure is the complete law of what cannot occur. It is a natural TRT principle and it is motivated independently of any quantum bound. It is also a new premise, so the honest statement is: (d′) reduces to LCP. Confidence that this matches JD's sketch: LOW. Confidence in the reduction: MEDIUM.

## 8. Circularity audit of the charter's distinctive claim

The charter claims that scoped definiteness, Persistence of Zero, and strong positivity are consequences of the triad, and that the Tsirelson bound is to be derived via strong positivity.

Finding. The charter also says, in obligation (a), that Hilbert-space structure may be contingent specification carried by D. Craig et al. (2007) tie strong positivity to the existence of an associated Hilbert space [V], and ordinary Hilbert-space quantum theory yields a strongly positive decoherence functional [U, standard]. Then:

- If Hilbert structure is contingent specification, strong positivity is inherited from that specification, and so is the Tsirelson bound.
- That outcome is the second horn of the charter's own failure condition 3: quantum structure is contingent specification and the derivational ambition reduces to constraint.

So obligation (a) and the distinctive claim cannot both be discharged by the same route. The dependency graph must run:

triad → (independent argument) → strong positivity → Hilbert structure and Tsirelson

and never Hilbert structure → strong positivity → Tsirelson.

A second hazard is parametric. Strong positivity is known in advance to deliver Tsirelson. Any definition in obligation (e) that is tuned to produce strong positivity is fitted to its outcome. The definitions in §7.2 were fixed without reference to the measure, which is why they are modest. That ordering should be preserved.

Status of each component:

| Component | From the triad? | Basis |
|---|---|---|
| Scoped definiteness | Yes, by the 11-12 ruling | L₃ with typed R, D, X |
| Acyclicity | Yes, given EPA and TC | §7.2 |
| Persistence of Zero | Reduces to LCP | §7.3 |
| Strong positivity | No argument yet | Open; this is where the objective is decided |
| Local finiteness | Posit | Charter |

## 9. Where the objective is met or lost

### 9.1 The selection rule and a constraint it already faces

The charter's working channel actualizes a distinction once it is recorded in at least two disjoint, causally independent regions.

Constraint [R], confidence MEDIUM to HIGH. A three-photon GHZ state records one photon's basis value in two other photons. Erven et al. (2014) distributed such states to spacelike-separated stations hundreds of metres apart and violated Mermin's inequality [V]. That violation requires coherence between the branches. If A had actualized one branch at redundancy two, the correlations would not appear.

Consequences.

- The unrefined rule is refuted by existing data. The charter's open items (record length scale, recoverability) are therefore mandatory, and the next two points bound them.
- A minimum-separation scale cannot be the fix, since the records were already far apart. The threshold has to sit in the record itself: its size, its count, or its irrecoverability.
- Once such a threshold is declared, the rule is a collapse-type model with a parameter. It is then exposed to the charter's failure condition 2 and to collapse-model bounds such as Donadi et al. (2021), which ruled out the parameter-free Diósi-Penrose model [V].

### 9.2 A candidate replacement for failure condition 1

The same structure yields the exposed falsifier that §3 requires.

> **Record-Threshold Conjecture (candidate).** There is a record scale N* such that distinctions redundantly recorded above N* cannot be recohered, while below N* unitary predictions hold exactly. In an extended Wigner's-friend experiment, Local Friendliness violations persist for friends below N* and cease above it.

Bong et al. (2020) prove that if quantum evolution is controllable at the scale of an observer, one of No-Superdeterminism, Locality, or Absoluteness of Observed Events fails, and they violate the inequalities with a photon path as the friend [V]. TRT keeps Absoluteness for actualized events and surrenders locality at A's selection. It additionally denies controllability above N*. That is a claim unitary quantum theory does not make, it is the kind decoherence alone cannot re-describe, and it is where WP-TRT-FLL-0002's named frontier and obligation (b) meet.

Failure conditions for the conjecture: N* cannot be derived or bounded; any N* consistent with GHZ and interferometry data is excluded by collapse bounds; or a friend above a declared N* is recohered. Confidence that the conjecture is well posed: MEDIUM. Confidence that it is true: UNCERTAIN.

### 9.3 The three decision points

1. **Strong positivity from the triad.** If an independent argument exists, TRT derives what the histories programme postulates, and the Tsirelson obligation is met. If none exists, failure condition 3 applies.
2. **A record threshold that survives.** If N* can be derived or declared within existing bounds, TRT has a discriminating prediction. If every value is excluded, obligation (b) fails on its current channel.
3. **The measure on the A-order.** If the L₃-natural measure has the Benincasa-Dowker continuum limit, the gravity route yields general relativity on the charter's own substrate.

Meeting the objective requires the first. The second and third determine whether the programme becomes progressive in the Lakatosian sense.

## 10. Rulings requested

1. **PRD-001 status.** Adopt a status for the decoherence form (recorded negative for tested forms) and add the schema value it needs.
2. **Charter failure condition 1.** Either cite the 06-26 negative and keep the condition as PRD-001, or replace it with a D → X conjecture such as §9.2 under a new claim.
3. **Precedence.** State how the FLL governing objective (2026-08-29) and the charter (2026-11-09) relate. Recommended: add the FLL falsifier to the charter's failure conditions.
4. **A-event typing.** Accept, amend, or reject §4.
5. **EPA and TC.** Accept as explicit axioms toward obligation (e), or supply the intended definition.
6. **LCP.** Accept as the bridge for (d′), or supply the intended sketch.
7. **Gravity substrate.** Rule whether GRAV-0001's graph is the A-order, a toy model, or a second substrate to be justified.
8. **Registry.** Authorize claim entries for the charter commitments listed in §5.
9. **QSA typing.** Rule whether `Inst(σ)` is a status inside D.
10. **Working notes.** Rule whether §7 may stand in for the missing file as a labelled reconstruction, with the charter's four citations repointed.

## 11. What this document does not establish

- Whether the objective is met remains open. The document locates the three points at which that is decided.
- It does not derive strong positivity, the Born measure, or local finiteness.
- The reconstruction in §7 is mine. Agreement with the charter's summary is evidence of fidelity, with no guarantee.
- External results marked [V] were checked at abstract level this session. Full-text verification is still owed before publication, and items marked [U] need primary checks.

## References

Verification status follows each entry.

- Benincasa, D.M.T. and Dowker, F. (2010) 'The scalar curvature of a causal set', *Physical Review Letters*, 104, 181301. arXiv:1001.2725. [V, abstract via arXiv; journal reference U]
- Bombelli, L., Lee, J., Meyer, D.A. and Sorkin, R.D. (1987) 'Space-time as a causal set', *Physical Review Letters*, 59, pp. 521-524. [as verified in the repository's objective file]
- Bong, K.-W. et al. (2020) 'A strong no-go theorem on the Wigner's friend paradox', *Nature Physics*, 16, pp. 1199-1205. arXiv:1907.05607. [V, abstract]
- Brightwell, G., Dowker, F., García, R.S., Henson, J. and Sorkin, R.D. (2003) '"Observables" in causal set cosmology', *Physical Review D*, 67, 084031. arXiv:gr-qc/0210061. [V, abstract]
- Craig, D., Dowker, F., Henson, J., Major, S., Rideout, D. and Sorkin, R.D. (2007) 'A Bell inequality analog in quantum measure theory', *Journal of Physics A*, 40, pp. 501-523. arXiv:quant-ph/0605008. [V, abstract]
- Donadi, S. et al. (2021) 'Underground test of gravity-related wave function collapse', *Nature Physics*, 17, pp. 74-78. [V, abstract; page range U]
- Dowker, F. (2021) 'Boundary contributions in the causal set action', *Classical and Quantum Gravity*. doi:10.1088/1361-6382/abc2fd. arXiv:2007.13206. [V, abstract; volume U]
- Erven, C. et al. (2014) 'Experimental three-photon quantum nonlocality under strict locality conditions', *Nature Photonics*, 8, pp. 292-296. arXiv:1309.1379. [V, abstract; page range U]
- Fein, Y.Y. et al. (2019) 'Quantum superposition of molecules beyond 25 kDa', *Nature Physics*, 15, p. 1242. [V, abstract; end page U]
- Machet, L. and Wang, J. (2020) 'On the continuum limit of Benincasa-Dowker-Glaser causal set action'. arXiv:2007.13192. [V, abstract]
- Rideout, D.P. and Sorkin, R.D. (2000) 'A classical sequential growth dynamics for causal sets', *Physical Review D*, 61, 024002. arXiv:gr-qc/9904062. [V, abstract]
- Riedel, C.J., Zurek, W.H. and Zwolak, M. (2016) 'Objective past of a quantum universe: redundant records of consistent histories', *Physical Review A*, 93, 032126. arXiv:1312.0331. [V, abstract]
- Sorkin, R.D. (1997) 'Quantum measure theory and its interpretation'. arXiv:gr-qc/9507057. [V, abstract]
- Sorkin, R.D. (2019) 'A possible causality-condition for causal sets: persistence of zero', Perimeter Institute talk, PIRSA:19110093. [V, title and abstract fragment only; precise statement requires verification before publication]
- Tonomura, A., Endo, J., Matsuda, T., Kawasaki, T. and Ezawa, H. (1989) 'Demonstration of single-electron buildup of an interference pattern', *American Journal of Physics*, 57, pp. 117-120. [V, citation and 50 kV]

Human-Curated, AI-Enabled (HCAE)

---

## Addendum A (2026-11-16): unmerged branches

Four branches were read after the map above was drafted. All predate the charter. Nothing in them is merged, and nothing here changes them.

### A.1 What was read

| Branch | PR | Content | Effect on the map |
|---|---|---|---|
| `wp-trt-fd-0001-flexible-determinism` | #15 | Package plus three gate notes (2026-10-03) | Changes §4 and adds rulings |
| `work/wp-trt-paper-0001-metaphysical-foundations` | #19 draft | 2,800-word manuscript, countermodel CM-01, adversarial review (2026-10-30) | Sharpens §7.2 and adds a ruling |
| `work/wp-trt-found-0002-dynamic-stability` | #16 draft | Package and five notebook scaffolds (2026-10-11) | No placement change; corroborates §8 |
| `feat/godel-modal-discriminator` | none | Theory note and package | Superseded: both files are identical on main; one docs line differs |

### A.2 Finding: the actuality-gap argument defends `Obtains`, and A is typed otherwise

Repository facts.

- FD-0001's Actuality Gap gate concludes that representability and admissibility do not constitute actuality, and it recasts A as the **instantiation / obtaining** role. It adds that A is better defined that way than as temporal transition.
- The 2026-09-29 normalization and the 2026-11-12 ruling define A as **state transition/change** and state that a state's obtaining is a distinct notion from A.
- The Lean core carries both: `A` as a relation on D, and `Obtains` as a separate opaque predicate.
- PAPER-0001's review item ADV-11 makes the same point from the other side: that actuality differs from possibility does not entail change.

Consequence [R], confidence HIGH on the logic. The programme's best-developed necessity argument supports the obtaining role. Under the governing definitions that role belongs to `Obtains`. The necessity of A as transition then rests on a separate argument that the repository has not completed (PAPER-0001 leaves its premise P3 open). Read strictly, the formal core holds four notions: L₃, I∞, A, and Obtains. The charter's obligation 1 guards against collapse to one primitive; the live risk here is expansion to four.

This turns the typing proposal of §4 into a fork that needs a ruling:

- **Occurrent reading.** A(d, d′) holds only where the transition occurs. Then `Obtains(d′)` is definable as "d′ is the target of some A-event" (plus an initial condition), the count returns to three, and the Actuality Gap argument supports A again. Cost: this sits close to defining A as actualization, which the 11-12 ruling forbids as a definition while allowing it as a role. The wording must hold that line.
- **Modal reading.** A(d, d′) says the transition is available. Then `Obtains` does independent work and must be either reduced or admitted.

The charter's growth picture favours the occurrent reading, since an A-event there is a birth. I recommend it, at MEDIUM confidence, and it requires a matching change to how the Lean core documents `Obtains`.

### A.3 Finding: single outcome and growth are charter commitments that earlier gates advised against fixing

- FD-0001 recommends removing the unique-outcome clause from the hard core and keeping A neutral between single-outcome and Everett-type readings. The hard core as it stands is neutral. The charter commits to one actualized branch and one globally consistent actualization.
- FD-0001 and CM-01 both advise against committing TRT to temporal becoming. The charter commits to sequential growth, in which events are born.

These are compatible if the levels are stated: the hard core stays neutral, and the charter adds single-outcome and growth as programme commitments with their own failure exposure. In that case the rejection of many-worlds rests on the logical-realism commitment and on parsimony, and has no support from the hard core alone. On growth, the causal-set literature's answer is that the order of births carries no physical meaning beyond the partial order (Rideout and Sorkin's discrete general covariance [V]), which gives becoming without a global time. That answer should be stated in the charter if it is the intended one.

### A.4 Placement of flexible determinism

FD-0001 separates stochastic-law randomness (a lawful non-degenerate measure) from ontological randomness (no further determinant of the individual outcome), affirms the first, and declines to infer the second. Its Gate 1 recommends the name **constrained actualization**.

Under the charter this is the source commitment in secular form: the measure is fixed by the specification of D, and each actualization is grounded in the will-relation. Placement: programme commitment adjacent to the hard core, with no empirical content of its own. FD-0001's Gate 3 reaches the same verdict, finding no quantum-interpretive discriminator.

### A.5 Corroborations of the map

- FD-0001 Gate 3 names objective-collapse models as the nearest structural competitor to A construed as stochastic selection. This agrees with §9.1: a redundancy rule with a declared threshold is a collapse-type model.
- FOUND-0002 lists the imported status of complex phase, Hilbert space, and the Born rule as an open challenge (its ADV-06), and lists GHZ states among its test cases. This agrees with §8 and §9.1.
- PAPER-0001's ADV-05 asks for an atemporal relation from which order arises as a theorem, or an admission of primitive order. §7.2 is an attempt at the first. In fairness to that objection, EPA and TC make conditioning a primitive relation, so §7.2 answers ADV-05 only if conditioning is accepted as non-temporal.
- PAPER-0001's ADV-04 (unboundedness of I∞ is not entailed by differentiation) is untouched by the charter and remains open.

### A.6 Additional rulings requested

11. **A and Obtains.** Choose the occurrent or the modal reading of A (A.2), and state how the count stays at three.
12. **Levels.** Confirm that single-outcome and growth are charter-level commitments while the hard core stays neutral (A.3).
13. **Name.** Adopt "constrained actualization" as the technical term, per FD-0001 Gate 1, or retain "flexible determinism".
14. **Branch hygiene.** PRs #15, #16, and #19 use pre-charter wording and are 29 to 44 commits behind main. Decide whether each is rebased and conformed, merged as historical record, or closed. The Gödel branch can be deleted.
