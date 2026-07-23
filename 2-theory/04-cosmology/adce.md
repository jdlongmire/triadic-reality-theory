# Actualization-Driven Cosmological Expansion (ADCE) — v3.2

**Working document. Belt-level research note; tracks [OPN-008](../../traceability/claims/OPN-008.yaml) and issue [#9](https://github.com/jdlongmire/triadic-reality-theory/issues/9).**

**Status:** Pre-theoretical research program, confidence **LOW/CONJECTURED** throughout except where labeled. v3 is the repositioning revision of the 2026-07 note: it adds the related-work placement (§2), makes the saturation axiom explicit (§9), resolves the capacity-scaling fork toward 4-volume counting (§9), states the rivalry with fluctuation-driven everpresent Λ (§11), and anchors the observational targets to DESI DR2 (§14). The v2 primitive shift is retained: the primitive is **irreversible actualization**, not emitted information; emitters are derived physical instances of the process.

**v3.1** absorbs the red-team pass ([reviews/2026-07-redteam-adce/](../../reviews/2026-07-redteam-adce/review.md)): the central hypothesis is **reformulated** after the static-universe result (§8; falsification criterion 3 fired against the v2-form statement under 4-volume counting and the firing is registered, §16); the two-level reading of $N$ is made explicit (§9.4); A-SAT's repair claim is softened (§9.1); the monotonicity claim is defined precisely and the DESI tension stated (§11, §14); the mean-coupled magnitude default is stated plainly (§11).

**v3.2** executes Targets 3 and 5 (FLRW level) — results in the companion report [adce-t3t5-report.md](adce-t3t5-report.md): **Target 3 closes negatively** (A-SAT dissolves under the two-level split — identity-and-inert at the substrate level, false at the record level; the capacity-forcing route is closed in principle, §9.1 note); the mandatory deliverable (a) is achieved by the feedback attractor ($H^* = \lambda/3$ recovered as an attractor of the diluted-stock bridge, not an assumption); the severe test **fails across the natural bridge-law grid**; three independent probes (natural-grid scan, inverse problem, magnitude table) converge on horizon coupling as the only data-viable branch, while the CSG literature (cosmic renormalization) natively selects the feedback branch — the two surviving branches are mutually exclusive in $w_a$ sign and DESI DR3/Euclid adjudicates between them.

**Author:** James D. Longmire (ORCID 0009-0009-1383-7698). v3 drafted with thinx-Claude research assistance; prior-art and observational claims verified against primary sources per the programme's source protocol (HCAE).

---

## Abstract

The accelerated expansion of the universe is conventionally represented by a cosmological constant, a dynamical dark-energy field, or a modification of gravitational theory. These approaches model the observed expansion history; the physical ontology underlying cosmic acceleration remains unresolved.

This note develops a speculative alternative grounded in the triadic (Logic-Information-Action) framework. Representable information specifies possible physical states. Logic constrains which states are admissible. Action renders admissible states determinate within realized physical history. Each irreversible actualization event adds a physically instantiated event, relation, or record to the realized causal structure of the universe.

The central hypothesis (reformulated in v3.1): cosmic expansion is the geometric registration of an **accelerating** actualization rate, and what is described phenomenologically as dark energy is the effective gravitational signature of the higher-order structure of that growth. Continued actualization alone does *not* force expansion (a static universe accumulates realized history at constant rate; §8); the dynamical question is why the actualization rate accelerates. The kinematic substrate of the proposal (a number-volume correspondence for causal events) is not new: it is causal set theory's founding postulate. What the proposal adds is (a) an ontological account of what the birth of a causal element *is*, supplied by the triadic primitives, and (b) a sharp dynamical question posed inside that shared kinematics: whether the dark-energy signal is driven by the *mean growth structure* of realized causal history, in contrast to the established causal-set mechanism in which it is driven by *Poisson fluctuations* in the causal-element count.

The proposal remains pre-theoretical. Its viability depends on a covariant actualization current, a derived (not postulated) growth law that produces matter-era deceleration followed by late acceleration, a natural magnitude compatible with the observed dark-energy scale, and observational predictions distinguishable from both the cosmological constant and the fluctuation-driven alternative.

---

## 1. The Cosmological Problem

The large-scale universe is expanding, and observations of distant Type Ia supernovae indicate the expansion has entered an accelerating regime (Riess et al., 1998; Perlmutter et al., 1999).

In the standard model the acceleration is represented by a cosmological constant Λ or an equivalent dark-energy density. In a homogeneous and isotropic spacetime, acceleration requires a component with

$$\rho + \frac{3p}{c^2} < 0,$$

and a cosmological constant satisfies $p_\Lambda = -\rho_\Lambda c^2$, so

$$w_\Lambda = \frac{p_\Lambda}{\rho_\Lambda c^2} = -1.$$

The representation is mathematically economical and empirically successful. It does not establish what dark energy *is*. The unresolved question is ontological: what physical or geometric condition gives rise to the effective negative pressure associated with accelerated expansion?

The present proposal considers whether cosmic expansion arises from the continued enlargement of realized physical history through irreversible actualization.

---

## 2. Related Work and Positioning

This section is new in v3 and is load-bearing. The proposal's kinematic substrate has forty years of prior art, and its novelty claim must be stated against that record or it has none.

### 2.1 Causal set theory owns the kinematics

The correspondence between causal-element count and spacetime volume is the founding postulate of causal set theory (CST): "Order + Number = Geometry," one element per Planck 4-volume (Bombelli, Lee, Meyer and Sorkin, 1987). The correspondence is implemented by Poisson sprinkling, whose random form is forced by Lorentz invariance; a region of 4-volume $V_4$ contains $\langle N \rangle = \rho_c V_4$ elements with fluctuation $\delta N \sim \sqrt{N}$ (Surya, 2019). **Any argument of the form "bounded event density therefore $V \propto N$" re-derives this dictionary; it is not a result of the present proposal.** [HIGH]

CST also supplies the growth dynamics: classical sequential growth (CSG), in which a causal set grows one element at a time subject to discrete general covariance and Bell causality (Rideout and Sorkin, 2000). CSG is an explicit counterexample to the claim that relativity forces a block universe: becoming is real but *asynchronous*, with birth order pure gauge (Sorkin, 2007; Dowker, 2014). The covariant-becoming problem this proposal faces at Targets 2 and 4 (§15) therefore has a worked answer to adopt, not a gap to fill from scratch. [HIGH]

CSG dynamics have already been shown to produce de Sitter-like early expansion in a large class of models (Ahmed and Rideout, 2010). Any discrete toy model built here must be benchmarked against that result. [HIGH]

### 2.2 The established causal-set dark-energy mechanism is fluctuation-driven

Sorkin predicted, in print before the 1998 supernova discovery, a fluctuating cosmological "constant" of magnitude

$$\Lambda \sim \pm \frac{\hbar}{\sqrt{V_4}} \sim 10^{-120} \ \text{(natural units, today)},$$

from unimodular gravity (Λ conjugate to 4-volume) plus the Poisson fluctuation $\delta N \sim \sqrt N$ of the CST dictionary (Sorkin, 1997). The phenomenological realization is "everpresent Λ" (Ahmed, Dodelson, Greene and Sorkin, 2004): Λ fluctuates about zero with magnitude tracking the ambient energy density at every epoch, which dissolves the coincidence problem by construction. Cosmological fits perform as well as ΛCDM and relieve some low-redshift tensions (Zwane, Afshordi and Sorkin, 2018), with implementation-dependence and typicality concerns subsequently flagged (Das, Nasiri and Yazdi, 2023). [HIGH]

### 2.3 Count-driven volume growth has a structural precedent

Padmanabhan (2012) derives the full Friedmann dynamics from a postulated law of emergent space,

$$\frac{dV}{dt} = L_P^2 \left( N_{\mathrm{surf}} - N_{\mathrm{bulk}} \right),$$

with de Sitter as the *equilibrium* state (holographic equipartition, $N_{\mathrm{surf}} = N_{\mathrm{bulk}}$). The companion CosMIn proposal fixes the numerical value of Λ from a conserved information count (Padmanabhan and Padmanabhan, 2013). Two lessons carry over. First, count-driven $dV/dt$ laws can reproduce exact FRW dynamics. Second, the program's standing criticisms (teleological justification, ad hoc sign conventions, foliation dependence) show what happens when the growth law is postulated to fit rather than derived. Note the inversion relative to ADCE: for Padmanabhan de Sitter is the equilibrium of vanishing count difference; here de Sitter would be the signature of proportional (exponential) growth. [HIGH]

Holographic dark energy (Li, 2004) and Verlinde's emergent gravity (Verlinde, 2011; 2017) are adjacent programs; the former remains observationally live, the latter is disfavored at galactic scales. [MEDIUM]

### 2.4 Disavowed path: energy-per-bit

Two informational dark-sector programs assign a standing energy or mass to stored bits by misreading Landauer's erasure cost as a state property: information-energy cosmology (Gough, 2008; 2022) and mass-energy-information equivalence (Vopson, 2019). Both have near-zero mainstream uptake and formal rebuttals. **ADCE explicitly does not travel this path**: no energy cost is assigned to abstract bits, information is not a fluid, and no radiation pressure mechanically pushes galaxies apart. The actualization sector's stress-energy, if any, must emerge from a variational principle over realized causal structure (§12), not from a per-bit conversion. [MEDIUM]

### 2.5 What is actually new here

Given §2.1 to §2.4, the novelty claim is confined to two items, and the program stands or falls with them:

1. **The ontological grounding.** CST is deliberately silent on what the "birth of an element" is. The triadic framework supplies an ontology: an element-birth is an irreversible actualization, $\Pi : \mathcal{I}_{\mathrm{adm}} \to \mathcal{H}_{\mathrm{R}}$, the transition of an admissible possibility into realized determinate history (§3). This grounds the growth dynamics in the programme's hard core ($\chi \equiv \mathsf{A}(I_\infty \mid L_3)$) rather than leaving it a formal postulate.
2. **The mean-growth question.** Inside the shared CST kinematics, the established dark-energy mechanism is fluctuation-driven ($\delta N \sim \sqrt N$, §2.2). ADCE poses the rival question: **can the *mean* growth rate $\dot N$ drive the late-time acceleration?** This is a well-posed dynamical rivalry (§11), not a re-description, and it has different failure conditions.

---

## 3. Foundational Framework

The proposal begins from the triadic primitives: $\mathcal{I}$ (representable information), $\mathcal{L}$ (logical constraint), $\mathcal{A}$ (actualizing action). Representable information includes possible distinctions, states, relations, and histories. Logic constrains which combinations are coherent and physically admissible. Action renders an admissible possibility determinate within realized physical history.

Let $\mathcal{I}_{\mathrm{adm}} = \mathcal{L}(\mathcal{I})$ denote the admissible state space, and let $\Pi$ denote the actualization operator:

$$\Pi : \mathcal{I}_{\mathrm{adm}} \rightarrow \mathcal{H}_{\mathrm{R}},$$

where $\mathcal{H}_{\mathrm{R}}$ is realized physical history. The essential distinction is between $\mathcal{I}_{\mathrm{adm}}$ as the domain of admissible possibilities and $\mathcal{H}_{\mathrm{R}}$ as the domain of physically actualized events and relations. Information is not treated as an independently acting substance; action is the transition from admissibility to realized determinacy.

---

## 4. Irreversible Actualization

An actualization event occurs when a physically admissible state becomes determinate within realized history. Represent an event as $a_i : \sigma_i^{-} \rightarrow \sigma_i^{+}$. The event is irreversibly actualized when it establishes a persistent causal distinction, which may be instantiated through an emitted quantum, a particle interaction, a radioactive decay, a molecular transition, a decohered environmental record, a gravitational-wave event, a black-hole horizon transition, a thermodynamically irreversible process, or a stable computational or biological record.

**Working definition.** An irreversible actualization event is a physical transition that establishes at least one new persistent causal relation or record within the realized history of the universe: $\Delta \mathcal{R}_i > 0$, where $\mathcal{R}_i$ is the set of realized causal relations associated with $a_i$.

The theory concerns growth in realized causal structure, not abstract information production.

**Emitters are derived.** An emitter is any system whose actualization event propagates a new physical distinction beyond its immediately prior state. Ordinary emitted radiation has $w_{\mathrm{rad}} = 1/3$ and decelerates expansion in the standard Friedmann equations; the proposal does not identify dark energy with radiation, and an emitter does not generate expansion by exerting pressure. Emitter activity is *evidence* of ongoing actualization; the proposed cosmological effect arises from the geometric consequences of actualization itself.

---

## 5. Realized Causal Structure

Represent realized history as a directed causal structure $\mathcal{G}_{\mathrm{R}} = (V, E)$: $V$ the set of realized events, $E$ the realized causal relations. Each irreversible actualization adds at least one event and ordinarily one or more relations, so the realized structure is dynamically increasing. Global counts and a global time are schematic only; a relativistic formulation must replace them with local densities and currents (§7), and the CSG precedent (§2.1) shows how growth and covariance coexist.

---

## 6. The Kinematic Identity (a caution before the physics)

Under the CST dictionary the count and the volume are proportional by *definition*. It follows that any relation of the form

$$H = \frac{1}{3}\frac{\dot N}{N} \quad (\text{3-volume counting}), \qquad H = \frac{1}{3}\frac{\ddot N}{\dot N} \quad (\text{4-volume counting, §9})$$

is a **kinematic identity, not a dynamical result**: it holds for every FRW history, decelerating or accelerating, because $N$ tracks volume by construction. All physical content of ADCE lives in the growth law

$$\dot N = \Gamma(N, t)$$

and in whatever microphysics determines it. v2 half-stated this; v3 states it outright, because mistaking the identity for a derivation is the proposal's nearest failure mode (falsification criterion 4, §16).

---

## 7. The Actualization Current

Introduce an actualization current $A^\mu$ with divergence

$$\nabla_\mu A^\mu = \Sigma_A \geq 0,$$

where $\Sigma_A$ is the local source density of irreversible actualization. Candidate measures: realized events per unit 4-volume, stable causal distinctions per unit 4-volume, record-forming transitions per unit 4-volume, decohered outcome density, growth in causal-set cardinality. The correct definition must be invariant, operationally meaningful, and compatible with quantum field theory in curved spacetime. The definition should not be selected for convenience (Target 2, §15).

---

## 8. The Central Geometric Hypothesis (reformulated in v3.1)

The v2-form hypothesis read: *continued irreversible actualization necessarily changes the geometry of realized spacetime.* Under the 4-volume counting adopted in §9, that statement is **false by the paper's own equations**, and the red-team pass caught the failure (review, vector 1). With $N = \rho_4 V_4$ and $V_4 = V_c \int_0^t a^3\, dt'$:

$$\dot N = \rho_4 V_c\, a^3 > 0 \quad \text{for any } a(t) > 0.$$

A static universe ($a$ constant) accumulates 4-volume, hence realized history, linearly and forever at saturated density with zero metric evolution; a contracting universe likewise sustains $\dot N > 0$. Constant-rate actualization corresponds *exactly* to a static universe. The capacity bound plus continued actualization therefore constrain $a(t)$ not at all. **Falsification criterion 3 (§16) fired against the v2-form statement, and the firing is registered rather than papered over.**

**Reformulated hypothesis (v3.1).** Under the 4-volume dictionary, expansion is the geometric registration of an *accelerating* actualization rate ($H = \tfrac{1}{3}\ddot N / \dot N$), and cosmic acceleration corresponds to a jerk condition on the count ($3\dot N \dddot N > 2\ddot N^2$, §9.3). The central dynamical claim becomes:

> The actualization rate accelerates, for reasons grounded in the growth dynamics of realized causal structure (candidate grounds in §10), and dark energy is the effective gravitational signature of that acceleration.

$$\mathcal{I}_{\mathrm{adm}} \rightarrow \Pi \rightarrow \ddot N > 0 \rightarrow \Delta g_{\mu\nu}.$$

This is a strictly weaker and honestly harder claim than v2's: nothing *forces* it, and the burden is entirely on deriving the growth law (Target 5). One alternative escape remains open and unexecuted: a back-reaction argument that a static geometry cannot *sustain* actualization (that admissible-state supply or record formation dies without expansion), which would restore a forcing form. Until such an argument exists, the forcing language is retired.

---

## 9. The Capacity Fork and the Saturation Axiom

v2 argued: if every finite region has an upper bound on realizable distinctions, then continued actualization under the bound forces geometric enlargement. v3 makes the two hidden commitments explicit.

### 9.1 The saturation axiom (named, not smuggled)

A capacity bound alone yields an inequality, $V \geq N / \rho_{\max}$: growth of $N$ forces growth of $V$ only *at* the bound. Obtaining the proportionality $V \propto N$ requires an additional principle:

> **A-SAT (Saturation Axiom, ASSUMED).** Actualization proceeds at the maximal rate the capacity bound admits, and the realized-event density sits at (or tends to) its bound: $\rho_A \to \rho_{A,\max}$.

Naming the axiom is progress in honesty, **not a repair** (red-team, vector 2). A-SAT faces a direction-of-explanation fork: if geometry determines $\dot N$ through the dictionary, the growth-law question is answered trivially by geometry and ADCE is re-labeled kinematics (criteria 11-12); if a microphysical $\dot N$ determines geometry, then A-SAT quietly asserts that geometry *responds* so as to hold $\rho_4$ at its bound, which is precisely the ungrounded growth-to-geometry content of Target 4. The axiom presupposes the theorem it was introduced to enable. The only exit is a derivation of A-SAT from an extremal principle *that also derives the geometric response* (Targets 3 and 4 jointly; compare Krishna and Mathew, 2017, for the analogous grounding of Padmanabhan's law). Until then it is an axiom, it is labeled as one, and it is known to be load-bearing beyond what an axiom should carry.

> **v3.2 closure.** Target 3 was executed and the axiom **dissolved**: at the substrate level ($N_P$) saturation is an identity of the number–volume correspondence — geometry-neutral, unable to force expansion (the static-universe result restated structurally); at the record level ($N_R$) saturation is false by ~100 orders of magnitude. No level exists where the bound both binds and is geometry-sensitive, so the capacity-forcing route is closed in principle, and A-SAT is retired. The extremal-principle exit above remains open but is weaker than this section hoped: Krishna–Mathew prove *law ⇒ entropy maximization*, not the converse. Full argument: [adce-t3t5-report.md](adce-t3t5-report.md) §2. All dynamical load now sits on the bridge law (§9.4).

### 9.2 Area, 3-volume, or 4-volume?

The Bousso covariant entropy bound makes fundamental capacity scale with boundary **area**, not volume: $S \leq A/4$ on light-sheets, with spacelike volume-scaling bounds admitting known FRW counterexamples (Bousso, 1999; 2002). If realized causal events carry entropy in the Bousso sense, a bounded density per unit *3-volume* eventually violates holography for large regions. [HIGH]

Two escape routes exist. Either argue that actualization events are not Bousso entropy (which surrenders the natural justification for the bound), or count per unit **4-volume**. v3 adopts the second:

> **Resolution (adopted).** Actualization events are events *in history*: they dwell in 4-volume, not in space at an instant. The capacity bound is a bound on realized-event density per unit 4-volume, $\rho_4 \leq \rho_{4,\max}$, and A-SAT pins $\rho_4$ at the Planckian sprinkling density. This is simultaneously the triadically consistent choice (actualization adds to realized *history*) and CST's own choice, which sidesteps the holographic objection rather than fighting it.

### 9.3 Kinematics under 4-volume counting

For a comoving domain with $V_4(t) = V_c \int_0^t a^3(t')\, dt'$ and $N = \rho_4 V_4$:

$$\dot N = \rho_4 V_c\, a^3 \quad\Longrightarrow\quad a \propto \dot N^{1/3}, \qquad H = \frac{1}{3}\frac{\ddot N}{\dot N}.$$

Differentiating, the acceleration condition becomes

$$\frac{\ddot a}{a} = \frac{1}{3}\frac{\dddot N}{\dot N} - \frac{2}{9}\left(\frac{\ddot N}{\dot N}\right)^2 > 0 \quad\Longleftrightarrow\quad 3\, \dot N\, \dddot N > 2\, \ddot N^2.$$

Reference cases (all verified symbolically):

* Power-law count $N \propto t^m$: $a \propto t^{(m-1)/3}$; acceleration requires $m > 4$ (3-volume counting required $m > 3$).
* Proportional growth of the *rate*, $\ddot N = \lambda \dot N$: $\dot N \propto e^{\lambda t}$, hence $a \propto e^{\lambda t / 3}$, exact de Sitter with $H = \lambda/3$.

The structure of the 3-volume case (v2 §§10-12) carries over with one derivative shifted; the fork changes quantitative thresholds, not the qualitative program. Everything in §6's caution still applies: these are dictionary identities, and the physics is the growth law.

### 9.4 Two levels of N (equivocation resolved by declaration)

The red-team pass (vector 3) caught an equivocation v3 committed: the Bousso escape and A-SAT's "Planckian sprinkling density" require $N$ to be the **substrate element count** ($N_P$, one per Planck 4-volume, $\sim 10^{147}$ per m³ per second), while §4's working definition and §13's microphysics count **physical record-forming events** ($N_R$: decays, decohered records, transitions), whose 4-density is at least $\sim 100$ orders of magnitude below Planckian. These cannot be the same quantity, and v3's safety claims borrowed one reading while its novelty claims borrowed the other.

v3.1 declares the two-level structure explicitly:

* **$N_P$ (substrate count)** carries the kinematics: the CST dictionary, A-SAT, the Bousso escape, and every identity in §9.3 are statements about $N_P$. At this level ADCE inherits CST unchanged and adds nothing dynamical.
* **$N_R$ (record count)** carries the ontology: §4's actualization events, §13's decoherence microphysics, and Target 1's invariance criterion are statements about $N_R$. $N_R \lll N_P$ and $N_R$ is *not* density-saturated.
* **The bridge is the open problem.** ADCE's mechanism requires a stated bridge law relating $N_R$-dynamics (the physics of record formation) to $N_P$-growth (the geometry). $\Sigma_A$ (§7) is the natural carrier of that bridge. Absent a bridge law, the "ontological grounding" of §2.5 is an interpretive gloss on unchanged kinematics, which is this programme's canonical degenerating move. The bridge is therefore added to Target 1's deliverables, and its absence is a standing threat, not a footnote.

---

## 10. Growth Laws and the Coincidence Problem

The primary dynamical question: **what determines the cosmic growth law of realized causal events?**

Candidate phenomenological laws (v2 §20, restated for 4-volume counting): linear rate growth (deceleration), proportional rate growth (de Sitter), saturating growth (acceleration weakens toward a maximum), matter-coupled growth (effect follows matter density), horizon-coupled growth (rate tied to horizon area). Candidate physical grounds for proportional growth: each realized event opens new admissible interaction channels; branching of irreversible records; decoherence across an enlarging environment; recursive interaction between geometry and actualization. None is derived; deriving one is Target 5.

**The coincidence problem (named, unsolved).** Pure proportional growth gives de Sitter *always*: no matter-dominated deceleration era, contradicting the observed expansion history (deceleration until $z \approx 0.7$, acceleration after). None of the listed growth laws obviously produces the observed transition. The fluctuation-driven rival (§11) dissolves this problem by construction, since everpresent Λ tracks the ambient density at every epoch. **A growth law that yields matter-era deceleration followed by late acceleration is therefore a mandatory deliverable of the toy model, not an optional refinement.** Absent it, ADCE is not competitive. [Open]

---

## 11. The Rivalry: Mean Growth versus Fluctuation

Both ADCE and everpresent Λ live on the same kinematic substrate ($N$ tracks 4-volume at Planckian density). They divide cleanly on the source of the dark-energy signal:

* **Everpresent Λ (established rival):** the signal is the Poisson fluctuation, $\delta N \sim \sqrt N$; Λ fluctuates about zero with magnitude $\sim \hbar / \sqrt{V_4} \sim H^2$, delivering the observed order of magnitude for free and dissolving the coincidence problem, at the cost of a sign-fluctuating Λ (roughly every Hubble time) and known typicality concerns (Das, Nasiri and Yazdi, 2023).
* **ADCE (this proposal):** the signal is the mean growth structure of $N$ (the acceleration and jerk of the count, §8-§9). Its magnitude and its onset epoch are *not* delivered for free and constitute the program's two hardest open problems (§10, criterion 14 in §16).

**"Monotone" defined precisely (v3.1, after red-team vector 5).** Two readings must not be conflated. *Sign-stability*: the effective dark-energy contribution does not fluctuate in sign; ADCE plausibly has this property and everpresent Λ does not (its Λ changes sign roughly every Hubble time). *Magnitude-monotonicity*: $\rho_A$ never decreases; ADCE has **no earned claim** to this either way, because the map from growth law to $\rho_A(z)$ is entirely underived, and asserting it would repeat the identity-as-result sin of §6. Only the sign-stability reading is claimed, and weakly.

**The DESI history is pressure, not comfort.** In the DESI-preferred quadrant ($w_0 > -1$, $w_a < 0$, crossing present), the dark-energy density $\rho_{DE}(a)$ *rose to a maximum at the crossing* ($a_* = 1 + (1 + w_0)/w_a \approx 0.71$, $z_* \approx 0.4$ for central fits) *and has been declining since* (from $d\ln\rho/d\ln a = -3(1+w)$; verified symbolically). A mechanism whose effective density were magnitude-monotone could not produce this history at all, and any mean-growth mechanism must explain why the geometric signature of *growing* realized structure is a density that peaked at $z \approx 0.4$. Prima facie, DESI DR2 favors the non-monotone over the naive-growth shape; §14 states the resulting test.

**Magnitude default (v3.1, after red-team vector 6).** The rival's smallness is free: its signal is the fluctuation, suppressed by $1/\sqrt{N} \sim 10^{-60}$. A mechanism coupled to the *mean* has natural scale $\rho_{4,\max}$, i.e. Planckian: the original cosmological-constant problem, roughly 120 orders too large. Absent a derived suppression mechanism, criterion 14's failure mode is ADCE's *default outcome*, not a remote risk. The table reflects this.

| Question | Everpresent Λ | ADCE (current state) |
|---|---|---|
| Magnitude of the effect | Derived, order $10^{-120}$ | Open; default is Planckian (120 orders wrong) absent derived suppression |
| Coincidence problem | Dissolved by construction | Open (§10) |
| Sign behavior of Λ_eff | Fluctuates (pressure point) | Sign-stable plausibly; magnitude behavior underived; DESI's non-monotone ρ_DE is prima facie pressure |
| Covariance of the mechanism | CSG-grounded | To adopt from CSG (Target 2/4) |
| Distinct near-term prediction | Fluctuation statistics in $w(z)$ | Growth-law-dependent $w(z)$ (§14) |

If ADCE cannot at least match the first two rows, the fluctuation mechanism wins on the shared substrate and ADCE reduces to re-labeled CST kinematics (failure criteria 11 and 12, §16). Sign-stability is the one axis on which ADCE may be structurally better positioned, and it is observationally live (§14); it is a narrower advantage than v3 claimed.

---

## 12. Covariant Program (action, stress-energy, conservation, homogeneity)

Condensed from v2 §§13-17; unchanged in substance, held to the same discipline.

**Action principle.** $S = S_{\mathrm{EH}} + S_{\mathrm{m}} + S_{\mathrm{A}} + S_{\mathrm{int}}$. A scalar-field representation ($A^\mu = \nabla^\mu \phi_A$ with canonical kinetic term and potential) is mathematically available but conceptually dangerous: it risks reducing the proposal to relabeled quintessence (criterion 12). A constraint formulation with a Lagrange multiplier enforcing $\Sigma_A = \Gamma[g_{\mu\nu}]$ better reflects the intended structure. The actualization sector must be *derived from* causal growth or record formation, not introduced to reproduce acceleration. Note also §14: the observationally preferred expansion history involves a phantom crossing, which a single minimally coupled scalar field cannot produce; if taken literally, the placeholder scalar formulation is already ruled out, which reinforces rather than embarrasses the intent of criterion 12.

**Effective stress-energy.** $T^{(A)}_{\mu\nu}$ from metric variation; in FRW form, acceleration requires $w_A < -1/3$; the theory must derive $w_A$ from growth dynamics, never assume $p_A = -\rho_A c^2$.

**Emergent negative pressure.** With effective energy $E_A(V, N)$ and $p_A = -\left(\partial E_A / \partial V\right)_N$, a dependence $E_A \propto V^n$ gives $w_A = -n$; the cosmological-constant case $n = 1$ means fixed energy per unit realized volume, which is Λ by another name unless the coefficient is derived. The feedback loop (volume up, admissible actualization up, realization up, volume up) requires demonstration of existence and stability.

**Conservation.** $\nabla^\mu (T^{(m)}_{\mu\nu} + T^{(A)}_{\mu\nu}) = 0$; either sector-separate conservation or an exchange current $Q_\nu$, the latter tightly constrained by laboratory, stellar, and galactic bounds on local conservation.

**Homogeneity.** Local actualization is clustered; the acceleration is smooth. Candidate reconciliations: microscopic ubiquity of actualization (source smoother than luminous matter), large-scale averaging, or geometric integration through a causal response kernel $\delta g_{\mu\nu}(x) = \int K_{\mu\nu}(x, x')\, \Sigma_A(x') \sqrt{-g(x')}\, d^4x'$ with support restricted to the causal past. Any genuinely acausal nonlocality disqualifies the model (criterion 9).

---

## 13. Microphysics: Decoherence, Records, Entropy

**Decoherence** provides the candidate microscopic context: system-environment correlation suppresses interference in the reduced state and stabilizes environmental records. A candidate source is the rate of stable record formation per unit 4-volume, $\Sigma_A \propto dR_{\mathrm{stable}} / dV_4$. Decoherence alone does not select a unique outcome, so the theory must state whether actualization is identified with decoherence, is an objective collapse process, is a deeper ontological commitment, or realizes all branches; these give different meanings to $N$ and $\Sigma_A$. The framework presently assumes objective realized determinacy, a commitment requiring explicit defense. **Quantum Darwinism** (redundant environmental records as the criterion of objectivity; Zurek, 2009) is the natural candidate for an observer-independent record criterion and should anchor Target 1.

**Entropy** is related but not identical: $\Delta S_{\mathrm{th}} > 0$ does not specify *which* event became determinate. Any bridging relation (v2 §19) is phenomenological until a microscopic derivation exists.

---

## 14. Observational Status and Targets (2025-26 anchor)

DESI DR2 BAO combined with CMB prefers evolving dark energy over ΛCDM at 3.1σ (DESI+CMB alone) and at 2.8σ to 4.2σ when supernova compilations are added, in the quadrant $w_0 > -1$, $w_a < 0$, with a phantom crossing at $z \approx 0.4$ to $0.5$ that is robust to parameterization choice (DESI Collaboration, 2025a; 2025b). [HIGH] Caveats: the significance is supernova-compilation-dependent and prior-dependent (Efstathiou, 2025); the preferred region *worsens* the $H_0$ tension, so no late-time expansion-history mechanism should claim a Hubble fix. [MEDIUM-HIGH]

Consequences for ADCE:

1. **A derived $w_A(z) \neq -1$ has a live observational target** for the first time since 1998.
2. **Phantom crossing is a severe test, not an advertised advantage (reframed in v3.1).** The DESI-preferred history has $\rho_{DE}$ peaking at $z \approx 0.4$ and declining since (§11): prima facie pressure against mean-growth mechanisms. The test: exhibit a *natural* growth law whose effective $\rho_A(z)$ is sign-stable yet non-monotone in magnitude with a late peak. If none exists in the CSG family, that is evidence toward criterion 15/16 territory. (A single minimally coupled scalar cannot cross $w = -1$, so the placeholder scalar formulation of §12 is independently unable to fit this history; the actualization sector, if viable at all, must not be one.)
3. **Background fits are insufficient.** Perturbations ($c_{s,A}^2$, anisotropic stress $\pi_A$, clustering) discriminate where $H(z)$ does not; first meaningful sound-speed constraints on dynamical dark energy now exist and must eventually be confronted.

The reconstruction dictionary is standard: given $N(a)$, $w_A(a) = -1 - \tfrac{1}{3}\, d\ln\rho_A / d\ln a$, with predictions required for $H(z)$, distances, growth $f\sigma_8(z)$, and the scalar potentials.

---

## 15. Derivation Targets (reordered in v3)

The v2 target list stands, but the order of attack changes: positioning and the capacity fork precede model-building, and the toy model inherits CSG rather than inventing a growth rule.

1. **Target 0 (new): positioning discipline.** Every subsequent artifact cites and distinguishes the CST substrate (§2.1), the fluctuation rival (§2.2), and the count-driven precedent (§2.3). Done in v3; maintained thereafter.
2. ~~**Target 3 (promoted): capacity bound and saturation.**~~ **Closed negative in v3.2** ([adce-t3t5-report.md](adce-t3t5-report.md) §2): A-SAT dissolved, capacity-forcing route closed in principle; extremal-principle derivation remains the only conjectural reopening.
3. **Target 1: invariant actualization criterion, plus the bridge law (extended in v3.1).** Separate actualized records from reversible evolution, transient correlation, gauge redundancy, coarse-graining artifacts, and observer-relative description; anchor: quantum Darwinism redundancy (§13). Then state the bridge law relating the record count $N_R$ to the substrate count $N_P$ (§9.4), without which the ontological grounding does not connect to the kinematics.
4. **Target 2: covariant current.** Define $A^\mu$, $\Sigma_A$ field-theoretically; adopt CSG's discrete general covariance for the discrete regime.
5. **Target 4: growth-to-geometry theorem.** Show $\Sigma_A > 0$ under the bound implies specific metric evolution (via A-SAT, this is where the theorem must do real work beyond the dictionary identity of §6).
6. **Target 5: the growth law, on CSG dynamics.** *Partially executed in v3.2 at the FLRW level* ([adce-t3t5-report.md](adce-t3t5-report.md) §§3–5): deliverable (a) achieved by the feedback attractor; deliverable (b) computed for the full natural grid — severe test failed; surviving branches are the feedback attractor (CSG-natural, DESI-disfavored quadrant) and horizon coupling (DESI-quadrant, no microdynamical derivation, acute criterion-12 risk). Remaining discrete work: whether any covariant $t_n$ family yields a horizon-referenced effective law (confirmed literature gap), bounded by the Glaser–Surya coarse-observable ceiling.
7. **Targets 6-9: stress-energy, equation of state, perturbations, data confrontation.** As in v2, gated behind the above. Include the **magnitude confrontation**: recover or beat the fluctuation mechanism's derived $10^{-120}$ (§11).

---

## 16. Falsification Criteria

The proposal should be rejected or substantially revised if any of the following holds. Criteria 1-14 are carried from v2; 15-17 are added in v3. Criteria 1-3 are worded as non-existence claims that cannot be conclusively established; they function as **abandonment heuristics** (sustained failure of serious attempts), not decidable tests, and are so labeled (v3.1, after red-team vector 9).

1. Irreversible actualization cannot be defined independently of observer-relative description. *(Heuristic.)*
2. No covariant actualization current can be constructed. *(Heuristic.)*
3. Realized causal growth does not imply any necessary metric evolution. *(Heuristic — and **partially fired, adjudicated in v3.1**: under 4-volume counting, continued growth demonstrably implies no metric evolution (§8, static-universe result). The v2-form central hypothesis was falsified and has been reformulated as an acceleration hypothesis; the criterion now reads against the reformulated claim: if no grounds can be found for accelerating actualization, the reformulated hypothesis fails too.)*
4. Metric expansion follows only after assuming volume-count proportionality (equivalently: A-SAT can neither be derived nor independently motivated, §9.1).
5. The theory requires an arbitrary coupling chosen solely to reproduce the observed value of Λ.
6. The derived equation of state satisfies $w_A \geq -1/3$.
7. The model predicts excessive clustering in the actualization sector.
8. It violates tested local conservation laws.
9. It requires acausal nonlocality.
10. Its predicted expansion history conflicts with precision cosmology.
11. It reproduces ΛCDM exactly while yielding no distinct observable prediction.
12. The actualization field reduces to ordinary quintessence without independent ontological or predictive content.
13. The model depends on ambiguous event counting that changes under coordinate transformation or coarse-graining.
14. The predicted magnitude differs radically from the observed dark-energy scale without a natural suppression mechanism.
15. **(v3)** No growth law on the CSG substrate produces matter-era deceleration followed by acceleration onset at $z \approx 0.7$ without hand-tuning (§10): the coincidence problem proves unsolvable for the mean-growth mechanism.
16. **(v3)** The mean-growth mechanism cannot match the fluctuation mechanism's derived magnitude (§11) after Targets 3 and 5 are complete: the rivalry resolves in favor of everpresent Λ on the shared substrate.
17. **(v3)** The 4-volume capacity bound (§9.2) proves incompatible with holographic entropy accounting even in light-sheet form, and no 3-volume or area formulation survives Bousso counterexamples.

A theory of actualization must remain open to failure; these conditions are the program's asset, not its liability.

**Degeneration clause (v3.1).** The criteria must be *re-run against each revision of this document*, not only against future derivations; v3 failed to do this and criterion 3's firing went unregistered until the red-team pass. Additionally: a future version that rescues the central hypothesis by adding an unmotivated postulate (for example, a back-reaction assumption introduced solely to restore the forcing form of §8 with no independent support) is the conventionalist twist and should be recognized as degenerating, per the programme methodology.

---

## 17. Present Status

Pre-theoretical. v3 established: honest positioning against forty years of adjacent work (§2); the kinematic-identity caution (§6); an explicit saturation axiom (§9.1); a resolved capacity fork with revised 4-volume kinematics (§9.2-9.3); the named coincidence problem (§10); the mean-growth-versus-fluctuation rivalry with its competitive bar (§11); DESI-anchored observational targets (§14); and a reordered derivation program (§15).

v3.1 absorbed a partial refutation at the belt (red-team, 2026-07-22): the v2-form central hypothesis was falsified by the paper's own 4-volume equations and reformulated as an acceleration hypothesis (§8); the two-level reading of $N$ with its required bridge law was declared (§9.4); A-SAT's limits were stated (§9.1); the monotonicity and magnitude claims were corrected against the DESI history (§11, §14). Per the programme methodology, the recorded negative is itself progress; the surviving question is narrower and harder than v3 stated it.

v3.2 executed Targets 3 and 5 (FLRW level) — [adce-t3t5-report.md](adce-t3t5-report.md). Established: A-SAT dissolved and Target 3 closed negative (§9.1 note); deliverable (a) achieved (feedback attractor, $H^* = \lambda/3$ as fixed point); severe test failed across the natural bridge-law grid; three-probe convergence on horizon coupling as the only data-viable branch, against the CSG-natural feedback branch — mutually exclusive in $w_a$ sign, adjudicated by DESI DR3/Euclid. The program now has exactly two live realizations and an externally scheduled kill condition for at least one of them.

Not yet established: everything on the target list, now including the $N_R \to N_P$ bridge law. The decisive chain remains

$$\Sigma_A \rightarrow \ddot N(t) \rightarrow g_{\mu\nu} \rightarrow T^{(A)}_{\mu\nu} \rightarrow w_A(z),$$

derived without inserting accelerated expansion into the assumptions. The program succeeds only if that chain is completed; it is abandoned or absorbed into the fluctuation mechanism if criteria 15 or 16 fire.

---

## References

Ahmed, M., Dodelson, S., Greene, P.B. and Sorkin, R.D. (2004) 'Everpresent Λ', *Physical Review D*, 69, 103523. arXiv:astro-ph/0209274.

Ahmed, M. and Rideout, D. (2010) 'Indications of de Sitter spacetime from classical sequential growth dynamics of causal sets', *Physical Review D*, 81, 083528. arXiv:0909.4771.

Bombelli, L., Lee, J., Meyer, D. and Sorkin, R.D. (1987) 'Space-time as a causal set', *Physical Review Letters*, 59(5), pp. 521-524.

Bousso, R. (1999) 'A covariant entropy conjecture', *Journal of High Energy Physics*, 1999(07), 004. arXiv:hep-th/9905177.

Bousso, R. (2002) 'The holographic principle', *Reviews of Modern Physics*, 74(3), pp. 825-874. arXiv:hep-th/0203101.

Cortês, M. and Smolin, L. (2014) 'The universe as a process of unique events', *Physical Review D*, 90, 084007. arXiv:1307.6167.

Das, S., Nasiri, A. and Yazdi, Y.K. (2023) 'Aspects of everpresent Λ (I): a fluctuating cosmological constant from spacetime discreteness', *Journal of Cosmology and Astroparticle Physics*, 2023(10), 047. arXiv:2304.03819.

DESI Collaboration (2025a) 'DESI DR2 results II: measurements of baryon acoustic oscillations and cosmological constraints', *Physical Review D*, 112, 083515. arXiv:2503.14738.

DESI Collaboration (2025b) 'Extended dark energy analysis using DESI DR2 BAO measurements'. arXiv:2503.14743.

Dowker, F. (2014) 'The birth of spacetime atoms as the passage of time', *Annals of the New York Academy of Sciences*, 1326, pp. 18-25. arXiv:1405.3492.

Efstathiou, G. (2025) 'Evolving dark energy or supernovae systematics?', *Monthly Notices of the Royal Astronomical Society*, 538, pp. 875-882. arXiv:2408.07175.

Frieman, J.A., Turner, M.S. and Huterer, D. (2008) 'Dark energy and the accelerating universe', *Annual Review of Astronomy and Astrophysics*, 46, pp. 385-432.

Gough, M.P. (2008) 'Information equation of state', *Entropy*, 10(3), pp. 150-159.

Gough, M.P. (2022) 'Information dark energy can resolve the Hubble tension and is falsifiable by experiment', *Entropy*, 24(3), 385.

Krishna, P.B. and Mathew, T.K. (2017) 'Holographic equipartition and the maximization of entropy', *Physical Review D*, 96, 063513. arXiv:1702.02787.

Li, M. (2004) 'A model of holographic dark energy', *Physics Letters B*, 603(1-2), pp. 1-5. arXiv:hep-th/0403127.

Padmanabhan, T. (2012) 'Emergence and expansion of cosmic space as due to the quest for holographic equipartition'. arXiv:1206.4916.

Padmanabhan, H. and Padmanabhan, T. (2013) 'CosMIn: the solution to the cosmological constant problem', *International Journal of Modern Physics D*, 22(12), 1342001. arXiv:1302.3226.

Perlmutter, S. et al. (1999) 'Measurements of Ω and Λ from 42 high-redshift supernovae', *The Astrophysical Journal*, 517(2), pp. 565-586.

Riess, A.G. et al. (1998) 'Observational evidence from supernovae for an accelerating universe and a cosmological constant', *The Astronomical Journal*, 116(3), pp. 1009-1038.

Rideout, D.P. and Sorkin, R.D. (2000) 'A classical sequential growth dynamics for causal sets', *Physical Review D*, 61, 024002. arXiv:gr-qc/9904062.

Sorkin, R.D. (1997) 'Forks in the road, on the way to quantum gravity', *International Journal of Theoretical Physics*, 36(12), pp. 2759-2781. arXiv:gr-qc/9706002.

Sorkin, R.D. (2007) 'Relativity theory does not imply that the future already exists: a counterexample', in Petkov, V. (ed.) *Relativity and the Dimensionality of the World*. Dordrecht: Springer. arXiv:gr-qc/0703098.

Surya, S. (2019) 'The causal set approach to quantum gravity', *Living Reviews in Relativity*, 22, 5. arXiv:1903.11544.

Verlinde, E. (2011) 'On the origin of gravity and the laws of Newton', *Journal of High Energy Physics*, 2011(4), 29. arXiv:1001.0785.

Verlinde, E. (2017) 'Emergent gravity and the dark universe', *SciPost Physics*, 2(3), 016. arXiv:1611.02269.

Vopson, M.M. (2019) 'The mass-energy-information equivalence principle', *AIP Advances*, 9, 095206.

Zurek, W.H. (2009) 'Quantum Darwinism', *Nature Physics*, 5, pp. 181-188. arXiv:0903.5082.

Zwane, N., Afshordi, N. and Sorkin, R.D. (2018) 'Cosmological tests of everpresent Λ', *Classical and Quantum Gravity*, 35(19), 194002. arXiv:1703.06265.
