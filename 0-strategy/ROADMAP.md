# Triadic Reality Theory: Research Program and Repository Plan

**Companion to** *Triadic Reality Theory: Finite Logic, Infinite Information, and Actualizing Action as the Foundation of Physical Reality* (v0.9)

**JD Longmire**
Independent Researcher
ORCID: 0009-0009-1383-7698
Correspondence: jdlongmire@outlook.com

**Document status:** Living planning document. Version 0.2.

---

## Purpose

The position paper establishes Triadic Reality Theory as a coherent foundational ontology with two physics-facing conjectures. It does not establish TRT as a formal theory. The paper itself names this gap repeatedly and treats it as the defining feature of the work ahead.

This document converts that gap into a structured program. It states what would have to be true for TRT to advance from ontology to formalized theory, orders the work by tractability and dependency, specifies the repository that will hold it, and sets the terms on which others can contribute. It is deliberately honest about what is conjecture, what is open, and what would count as failure, because the credibility of the program depends on those distinctions being maintained rather than blurred as the work proceeds.

A single principle governs the whole program. Conceptual elaboration is no longer the bottleneck. Three independent reviews of the position paper converged on the same conclusion: additional philosophical exposition adds weight without rigor. The priority is formalization, and the measure of progress is whether a named conjecture becomes either a theorem or a recorded failure.

---

## 1. Current Status

TRT v0.9 is a position paper. Its load-bearing assets are the following.

The four-tier distinction (representable, admissible, actual, outcome-actual) is the central engine. It carries the treatment of dialetheism, quantum superposition, the Pusey-Barrett-Rudolph theorem, measurement, black holes, and mathematical foundations. It is conceptually stable and does real work.

Two physics-facing conjectures exist, both honestly labeled as unproven:

- The **co-admissibility conjecture** (paper §13.1), concerning pointer-state selection under incompatible decoherence channels. Confidence LOW; one component UNCERTAIN pending formalization.
- The **gravity co-admissibility conjecture** (paper §13.4, developed in §10.1), concerning whether global co-admissibility forces the constraint structure of general relativity. Confidence LOW; UNCERTAIN pending formalization.

One retrodiction is offered at moderate confidence: the effectiveness of mathematics (paper §9.5), with a weaker companion retrodiction concerning the discipline of foundational mathematics (§3.4.2, MEDIUM).

The variational apparatus (paper §5) is explicitly a desideratum, not a derivation. No Lagrangian form, no equations of motion.

What TRT does not yet have: a single formalized criterion that computes a definite result, a recovered piece of known physics, or a discriminating prediction that has survived contact with data. The program below is organized around producing the first of these, because the second and third depend on it.

---

## 2. Research Roadmap

The roadmap is ordered by dependency and tractability. Earlier items gate later ones. Each item states its target, its prerequisite, its failure condition, and its current confidence. The discipline of stating failure conditions is carried over from the paper and is not optional: an item without a failure condition is not a research task but a hope.

### Tier 0: Foundational Formalization (prerequisite for everything downstream)

**0.1 Formalize co-admissibility.**
The single highest-leverage task. Define co-admissibility as a criterion that takes a collection of physical constraints (channel structure, conserved quantities, coupling data) and computes a definite set of admissible structures, with no free entanglement measure.
- *Target:* a criterion *C(constraints) → admissible set* that is well-defined, computable, and measure-independent.
- *Prerequisite:* none. This is the root.
- *Failure condition:* if no formalization can avoid reintroducing a free measure, or if every formalization reduces to the existing einselection optimization, the co-admissibility program collapses to re-description and both physics conjectures lose their discriminating content.
- *Confidence that a formalization exists:* UNCERTAIN. This is the make-or-break task.

**0.2 Define a covariant measure of actualization rate or density.**
Required by the dynamic leg of the gravity treatment (paper §10.1.3) and by the energy-as-action-rate identification (§6.2).
- *Target:* a covariant scalar quantifying actualization rate or density across relational structure.
- *Prerequisite:* none, but informed by 0.1.
- *Failure condition:* if no covariant measure can be defined, the curvature-as-actualization-gradient claim remains permanently schematic and the gravity dynamic leg cannot be developed.
- *Confidence:* LOW.

### Tier 1: First Discriminating Result (depends on 0.1)

**1.1 Compute co-admissibility for the incompatible-channel case.**
Apply the formalized criterion from 0.1 to the cavity-field system with two incompatible decoherence channels (number-basis and coherent-state-basis), the Feller-Coeuret Cauquil-Roussel (2020) setup.
- *Target:* a definite predicted pointer set, comparable against the analytically known critical coupling at which Fock-state optimality ends.
- *Prerequisite:* 0.1.
- *Failure condition:* if the prediction contradicts the known critical coupling, the criterion is falsified. If it merely reproduces the einselection optimization, the criterion is not discriminating.
- *Confidence:* gated entirely by 0.1.

This is the first point at which TRT could produce a result that is either a confirmation or a falsification rather than an interpretation. It is the program's first genuine physics milestone.

### Tier 2: Variational Structure (depends on 0.1, 0.2)

**2.1 Specify the Lagrangian density over χ.**
Give *L(χ, ∂χ, L₃)* a definite form, replacing the schematic expression of paper §5.
- *Target:* a Lagrangian from which equations of motion follow.
- *Prerequisite:* 0.1, 0.2.
- *Failure condition:* if no form recovers any known equation of motion in any limit, the variational claim is empty.
- *Confidence:* LOW.

**2.2 Derive or recover the Born rule.**
Attempt to derive the Born measure from constraints on actualizing action across the admissible-to-actual boundary, rather than assuming it (paper §6.6.2, §12).
- *Target:* the Born measure as a consequence, not a postulate.
- *Prerequisite:* 0.1, 2.1.
- *Failure condition:* if the measure cannot be derived and must be assumed, TRT inherits the measurement problem's hard core unchanged, as the paper already concedes.
- *Confidence:* LOW. This is a problem on which many programs have stalled; TRT claims only to have relocated it precisely, not to have a solution in hand.

### Tier 3: Gravity (depends on 0.1, 0.2, 2.1)

The gravity conjecture (paper §13.4) has been substantially refined through three working documents (`03-gravity/`): the derivation skeleton, the D[χ] attempt, and the linearity crux. The conjecture is no longer a single open question. It has been reduced through a chain of sharpenings to one combinatorial problem. The chain is recorded here because each link is a genuine narrowing and the final link is decidable.

**The reduction chain (established in the working documents):**

1. *Lovelock reduction.* By Lovelock's theorem (1971), in 4D any symmetric, divergence-free, second-order metric tensor is the Einstein tensor plus a cosmological term. Divergence-free comes free from general covariance via the Noether identity. So deriving GR reduces to showing the co-admissibility measure D[χ] localizes to a second-order (L1), metric-only (L2), local (L4), 4D (L5) object. L1 is the crux.

2. *Holonomy identification.* Local *L₃* carries no derivatives; geometry enters only through consistency of relational transport around closed loops, which is curvature holonomy, automatically second-order via area-scaling. (HEURISTIC: that joint satisfiability reduces to loop consistency is motivated by minimality, not proven.)

3. *Linearity crux.* Loop holonomy is the full Riemann tensor; a measure built from it generically gives higher-curvature modified gravity (the Bianconi 2025 outcome), not GR. Regge calculus is the existence proof that a measure *linear in the holonomy deficit* gives exactly the Einstein-Hilbert action and hence GR. The unique scalar linear in curvature is the Ricci scalar, so linearity automatically selects Einstein-Hilbert. The entire gravity question reduces to: **is the co-admissibility measure linear or quadratic in the holonomy deficit?**

4. *The argument for linearity.* Quadratic measures (relative entropy, Fisher information) carry an imposed metric on configuration space. *L₃* supplies no such metric, only a raw deficit registering the magnitude of contradiction. Raw deficits are linear. So TRT's own commitments favor the linear measure, hence GR. (HEURISTIC, and the prime remaining debt.)

**3.1 Resolve the linearity crux on a finite relational graph.**
- *Target:* define joint *L₃*-satisfiability on a finite relational graph with explicit group-valued edge transformations, and determine whether the natural measure of cycle-closure failure is linear or quadratic in the deficit.
- *Prerequisite:* 0.1 (the measure definition is part of formalizing co-admissibility).
- *Success condition:* the natural measure is linear, with linearity following from the structure of *L₃* rather than imposed. Then (with the shared discrete-gravity assumptions on group structure and continuum limit) TRT has a credible route to deriving GR exactly, and the conjecture moves from LOW to defensible MEDIUM.
- *Failure condition:* the natural measure is quadratic or higher with no logical motivation for linearity. Then TRT gives Bianconi-class modified gravity, not GR; the conjecture is downgraded to "derivation of a GR-limiting modified gravity"; and the §4 linearity argument is refuted. To be recorded as plainly as a success.
- *Confidence:* that TRT *can* recover GR exactly, conditional on linearity, is now MEDIUM (Regge is a rigorous existence proof). That linearity actually holds is UNCERTAIN but framed as a decidable combinatorial question.

**3.2 Discharge the shared discrete-gravity assumptions.** That the relational holonomy carries the appropriate frame-group structure (so its deficit is gravitational curvature), and that the continuum limit is 4D Lorentzian. These are shared with all discrete-gravity programs and are not special TRT burdens.

**Discriminating consequence (feeds Tier 4).** Linear co-admissibility predicts exact GR with no higher-curvature corrections from this mechanism; quadratic predicts Bianconi-class corrections at high curvature. These differ observationally near black holes and in the early universe. The linearity crux therefore carries observational content, not merely formal content.

### Tier 4: Recovery and Prediction (depends on all above)

**4.1 Recover known physics in limits.** Hilbert space, probability, gauge structure, relativistic spacetime, conservation laws, as the paper's §12 second challenge requires.

**4.2 Produce a novel discriminating prediction.** The final bar for the program to count as physics rather than foundational ontology. The linearity crux (3.1) already points at one candidate discriminating prediction: presence or absence of higher-curvature corrections to GR, tied to whether co-admissibility is linear or quadratic. Until an item here is reached, TRT remains, by its own standard, a research program.

---

## 3. Dependency Graph

```
0.1 Formalize co-admissibility ──┬──> 1.1 Incompatible-channel test ──> (first physics milestone)
                                 │
                                 ├──> 2.1 Lagrangian form ──> 2.2 Born rule derivation
                                 │
                                 ├──> 3.1 Linearity crux (finite graph) ──> linear?  ──> GR (Regge+Lovelock)
                                 │         │                                quadratic? ─> modified gravity
0.2 Actualization measure ───────┴────────┴──> 3.2 Frame-group + continuum ──┐
                                                                             v
                                                            4.1 Recover known physics
                                                            4.2 Novel prediction
                                                            (incl. GR vs modified-gravity test
                                                             from the linearity crux)
```

Note that the gravity path now branches at 3.1 rather than running through a single undifferentiated node. The linearity crux is reachable directly from 0.1 (it is part of defining the measure) and does not strictly require 2.1, which is why it is among the nearer-term tractable problems despite gravity being conceptually the most ambitious tier.

The graph is acyclic, consistent with the circularity discipline of the paper. Node 0.1 is the root: nothing discriminating is reachable without it. This is why the formalization of co-admissibility is the program's first and gating task.

---

## 4. Repository Structure

Proposed layout for the GitHub repository. The structure separates the stable position paper from the volatile research work, and keeps formal artifacts (code, proofs) apart from prose.

```
triadic-reality-theory/
├── README.md                      # Overview, status, how to navigate, citation
├── LICENSE                        # See §6 below
├── CITATION.cff                   # Machine-readable citation metadata
├── CONTRIBUTING.md                # Contribution terms (see §5)
├── ROADMAP.md                     # This document's §2, kept live
│
├── paper/
│   ├── TRT-v0.9.md                # The position paper, master of record
│   ├── TRT-v0.9.pdf               # Rendered version (generated)
│   └── changelog.md               # Version history, what changed between versions
│
├── program/
│   ├── 00-foundational/
│   │   ├── co-admissibility-formalization.md   # Task 0.1 working notes
│   │   └── actualization-measure.md            # Task 0.2 working notes
│   ├── 01-decoherence/
│   │   ├── incompatible-channel-test.md        # Task 1.1 plan and results
│   │   └── code/                               # Computational work for 1.1
│   ├── 02-variational/
│   │   ├── lagrangian.md                        # Task 2.1
│   │   └── born-rule.md                         # Task 2.2
│   ├── 03-gravity/
│   │   ├── derivation-skeleton.md              # Path A: five Lovelock conditions
│   │   ├── Dchi-attempt.md                     # Path B: trace vs full-tensor fork
│   │   ├── linearity-crux.md                   # Path B: linear vs quadratic, the crux
│   │   └── relational-graph-test.md            # Task 3.1: the combinatorial computation
│   └── open-problems.md                         # Consolidated, mirrors paper §12
│
├── formal/
│   ├── lean/                       # Formal verification, if pursued (see note)
│   └── notebooks/                  # Computational experiments, Jupyter/Python
│
├── reviews/
│   └── ...                         # Critical reviews received, with responses
│
└── references/
    ├── bibliography.bib            # Master BibTeX
    └── verification-status.md      # Which references are primary-verified (see §7)
```

Notes on the structure:

The `paper/` directory holds the settled artifact and changes rarely. The `program/` directory holds the volatile work and changes constantly. This separation is deliberate: readers must be able to find the stable claim without wading through speculative working notes, and contributors must be able to work on open problems without destabilizing the paper.

The `formal/lean/` directory anticipates possible Lean 4 formalization of the logical core, consistent with prior work in the author's broader research program. Whether the co-admissibility criterion is amenable to Lean formalization is itself an open question (it may be more naturally a numerical/computational object than a proof object); the directory is provisional.

The `references/verification-status.md` file is not optional. The paper carries references not yet checked against primaries. The repository must track verification status explicitly so that no downstream work builds on an unverified citation.

---

## 5. Contribution Guide (CONTRIBUTING.md content)

The program welcomes contribution under terms that preserve its intellectual discipline. The following is the proposed substance of CONTRIBUTING.md.

### What this project is

TRT is a foundational-ontology research program with a defined path toward physics-level results. It is led by an independent researcher and is genuinely open to falsification. The project's credibility rests on maintaining honest confidence labels and stated failure conditions. Contributions are evaluated first against whether they preserve that discipline.

### How to contribute

Contributions are most valuable in the following forms, roughly in order of current need:

1. **Formalization of co-admissibility (Task 0.1).** The gating problem. Mathematical contributions that make the criterion definite and computable are the highest priority. A contribution that demonstrates co-admissibility *cannot* be formalized without a free measure is equally valuable, because it would settle the matter in the negative and is a recorded result, not a failure of the project.

2. **Computational tests (Task 1.1).** Once 0.1 exists, code that computes the prediction for the incompatible-channel case and compares it against the known critical coupling.

3. **Critical review.** Adversarial reading that finds errors, circularities, or overclaims. Reviews are archived in `reviews/` with responses. A review that forces a confidence label downward or a claim to be retracted is a successful contribution.

4. **Reference verification.** Checking cited references against primaries and updating `verification-status.md`.

5. **Recovery proofs (Tier 4).** Demonstrations that TRT structures recover known physics in appropriate limits.

### Standards every contribution must meet

- **State confidence.** Every claim carries a confidence label (HIGH, MEDIUM, LOW, UNCERTAIN) matching the paper's conventions.
- **State failure conditions.** Every proposed result specifies what would falsify it.
- **No circularity.** Derivations and proofs include a dependency-graph check; the graph must be acyclic. Parametric, definitional, and validation circularity are all disqualifying (see paper §3.4, §9.2 for the standard).
- **Primary sources.** Cite primaries, not secondary characterizations. Use "as cited in" when primary access is unavailable, and flag for verification.
- **Distinguish interpretation from derivation.** A re-description of known physics in TRT's terms is interpretation, not result. Contributions must not present the former as the latter.

### What will be declined

Contributions that inflate confidence, remove failure conditions, present interpretation as derivation, or treat the metaphysical commitments as established physics will be declined regardless of technical quality. The discipline is the asset.

---

## 6. Licensing

Two separate concerns, two separate choices.

**The paper and prose** (`paper/`, `program/` notes, `ROADMAP.md`): a Creative Commons license is appropriate. CC BY 4.0 permits sharing and adaptation with attribution, which suits an open research program. If the author wishes to prevent commercial enclosure of the writing, CC BY-NC 4.0 is the alternative, at the cost of some reuse friction.

**Code and formal artifacts** (`formal/`, `program/*/code/`): a permissive software license, MIT or Apache 2.0. Apache 2.0 is preferable if patent considerations ever arise, since it includes an explicit patent grant; MIT is simpler if they do not.

The recommendation is CC BY 4.0 for prose and Apache 2.0 for code, stated clearly in `LICENSE` and `README.md`. The author should confirm, since licensing is a commitment that is awkward to reverse.

---

## 7. Reference Verification Status

The following must be resolved before any circulation draft. This list seeds `references/verification-status.md`.

**Verified this session (primary or authoritative source consulted):**
- Pusey, Barrett & Rudolph (2012), *Nature Physics* 8(6), 475-478.
- Feller, Coeuret Cauquil & Roussel (2020), arXiv:2001.10851.
- Bianconi (2025), *Physical Review D* 111(6), 066001.
- Zurek (2003), *Reviews of Modern Physics* 75(3), 715-775.

**Asserted from standard knowledge, not yet primary-verified:**
- Jacobson (1995), *Physical Review Letters* 75(7), 1260-1263. (Content confirmed by review; page numbers to verify.)
- Ryu & Takayanagi (2006), *Physical Review Letters* 96(18), 181602. (Content confirmed; article number to verify.)
- Bekenstein (1973), *Physical Review D* 7(8), 2333-2346. (Standard; verify.)
- Wigner (1960), *Communications on Pure and Applied Mathematics* 13(1), 1-14. (Standard; verify.)
- Aristotle, *Metaphysics* Book Γ. (Edition/translation citation to finalize.)
- Russell (1908), *American Journal of Mathematics* 30(3), 222-262. (Verify.)

**Carried forward from the original draft, not verified this session:**
- Deutsch & Marletto (2015), *Proceedings of the Royal Society A* 471(2174), 20140540.
- Feynman (1948), *Reviews of Modern Physics* 20(2), 367-387.
- Shannon (1948), *The Bell System Technical Journal* 27, 379-423, 623-656.
- Wheeler (1989), in Zurek (ed.), *Complexity, Entropy, and the Physics of Information*.

The carried-forward four are the priority, since they have had the least scrutiny.

---

## 8. Immediate Next Actions

In order, the concrete steps to stand up the program:

1. Create the repository with the structure of §4.
2. Place TRT v0.9 in `paper/`, strip the working-draft status note from a public-facing copy while retaining it in the working master, and render the PDF.
3. Seed `ROADMAP.md` from §2 of this document and `verification-status.md` from §7.
4. Verify the four carried-forward references first, then the standard-knowledge ones.
5. Open Task 0.1 (co-admissibility formalization) as the first working file and the first issue. This is where the real research begins.

The program now has **two** tractable near-term research targets, both reachable from Task 0.1, and both well-posed:

- **Task 1.1**, the incompatible-channel pointer-state test, the program's first potential physics milestone.
- **Task 3.1**, the linearity crux on a finite relational graph, a self-contained combinatorial question whose answer determines whether TRT's gravity is exact GR or a GR-limiting modified gravity, and which carries observational content either way.

Both depend on formalizing the co-admissibility measure (Task 0.1), which remains the honest center of the work. The notable outcome of the gravity working sessions is that the most ambitious tier of the program (gravity) has been reduced to a combinatorial question that is, in principle, decidable now, rather than remaining an open-ended aspiration. That reduction is itself the kind of progress the program should aim for: not premature claims of derivation, but the conversion of large vague questions into small sharp ones with stated success and failure conditions.

**Document version: 0.2** (updated to fold in the gravity reduction chain: Lovelock reduction, holonomy identification, linearity crux, and the relational-graph test as Task 3.1).
