# Triadic Reality Theory: Research Programme Roadmap

> **Canonical semantic invariant (2026-09-29):** WP-TRT-CORE-0001 governs active TRT terminology. L₃, I∞, and A are the three irreducible co-primitives. L₃ is necessary ontological constraint; I∞ is unbounded representability/informational differentiation; A is fundamental non-temporal state transition/change. Representability, L₃-admissibility, actualizability, and actuality must remain typed distinctions. No protective-belt result may silently assume that L₃-coherence is sufficient for actualizability or redefine A as “actuality by definition.”

**Companion to** the programme charter ([`TRT-charter.md`](TRT-charter.md), filed 2026-11-09, amended 2026-11-12 and 2026-11-16) and the position paper *Triadic Reality Theory* (v0.10).

**JD Longmire**
Senior Technical Fellow, Aerospace and Defense Sector
ORCID: 0009-0009-1383-7698
Correspondence: jdlongmire@outlook.com

**Document status:** Living planning document. Version 0.3 (2026-11-17), rebased on the charter.

---

## Purpose

This document orders the programme's work. It governs nothing. Where it and a governing text differ, the governing text stands:

- the hard core, [`1-hypothesis/hard-core.md`](../1-hypothesis/hard-core.md);
- the charter and objective, [`TRT-charter.md`](TRT-charter.md) and [`TRT-objective.md`](TRT-objective.md), with their amendment records;
- the rulings records under [`sessions/`](sessions/), most recently [`2026-11-16-reconciliation-rulings.md`](sessions/2026-11-16-reconciliation-rulings.md);
- the methodology, [`METHODOLOGY.md`](METHODOLOGY.md) and [`research-practices.md`](research-practices.md).

The measure of progress is unchanged from v0.2: a named conjecture becomes a theorem, a testable result, or a recorded failure. A recorded failure is progress, and is written down as plainly as a success.

Version 0.2 was a companion to paper v0.9. It made the formalization of co-admissibility the root of the programme and the FLL hypothesis its governing empirical objective. The charter supersedes both. The tested forms of co-admissibility returned a recorded negative in June 2026, the charter now governs over the FLL objective and carries its falsifier as failure condition 4, and spacetime is now recovered from the order of A-events. Section 4 records where each v0.2 task went.

---

## 1. Current status

The standing claim-by-claim status is the generated [programme baseline](../traceability/generated/baseline.md), built from the claim registry, the computation registry, and the research notebooks. This section summarises it at 2026-11-17 and is not maintained between versions; the baseline is.

**Machine-checked.** The pair-failure half of the Co-Primitive Irreducibility Theorem is proved in Lean (`Core/Irreducibility.lean`), relative to its stated constitutive conditions, using Lean's standard axioms only (ONT-002, ONT-004). In the core, `actual_is_l3_admissible` is proved only from the project axiom `actualizable_is_l3_admissible`, which restates the hard core's necessity direction (ACT-001). Every registered computation reproduces in CI.

**Recorded negatives.**

- The decoherence form of the Co-Admissibility Conjecture re-describes einselection (PRD-001, `refuted_by_redescription` for the tested forms). OPN-001 stays open at the root.
- The gravitational order-difference channel cannot leave interference intact. It predicts collapse of electron superpositions about twenty orders of magnitude too fast, with G cancelling exactly. Recorded at MEDIUM confidence because its failure condition was fixed after the result; an independent red-team pass confirms it (review record in PR #40).

**Axiomatized in prose only.** The condition of actualization (ACT-002), the source commitment (INT-001), the logical closure of preclusion (LOG-003), and discreteness and local finiteness of the A-order (PHY-001) are stated as axioms without Lean declarations.

**Not yet attempted or open.** Strong positivity from the triad (QM-001), the selection rule's record threshold (ACT-003, PRD-004), the gravity measure on the A-order (PRD-002), the Born measure (OPN-004), recovery of known physics (OPN-003), and cosmological dynamics (OPN-008).

TRT does not yet have a discriminating prediction that has met data, or a recovered piece of known physics. The roadmap below is organised around the three points at which the charter's objective is decided.

---

## 2. Research roadmap

Items are ordered by dependency. Each states its target, prerequisites, failure condition, and current confidence, and names the charter obligation and registry claims it serves. An item without a failure condition is a hope, not a task.

### Tier 0: Formal foundations of the A-order

**0.1 Condition of actualization (charter obligation (e); ACT-002).**
- *Target:* declare EPA (no A-event is among the conditions of its own obtaining) and TC (conditioning is transitive) in Lean over typed A-events, and prove that the condition-of-actualization relation is a strict partial order.
- *Prerequisites:* the A-event typing of the 2026-11-16 rulings (an A-event is a pair (d, d′) with A(d, d′) and Obtains(d′)).
- *Failure condition:* TC cannot be motivated independently of an order already assumed, so the order is primitive and the acyclicity "derivation" is a restatement. To be recorded as such.
- *Confidence:* that the proof goes through given EPA and TC, HIGH (it is short). That TC is independently motivated, MEDIUM.

**0.2 Persistence of Zero from L₃ and A (obligation (d′); QM-002, LOG-003).**
- *Target:* state Persistence of Zero in the form used in quantum measure theory, verified against its primary source, and derive it from L₃, the A-order, and the logical closure of preclusion.
- *Prerequisites:* 0.1; full-text verification of the Persistence of Zero statement (Sorkin, 2019 talk, and any written form).
- *Failure condition:* the primary statement is stronger than what LCP yields, or LCP itself admits a counterexample within quantum measure theory.
- *Confidence:* that (d′) reduces to LCP, MEDIUM. That LCP is defensible as a TRT principle, LOW to MEDIUM.

**0.3 Local finiteness (PHY-001).**
- *Target:* either an argument for local finiteness from the co-primitives, or a ruling that it is an accepted posit with its own failure condition (for example, evidence of Lorentz-violating discreteness effects the causal-set substrate excludes).
- *Prerequisites:* none.
- *Failure condition:* the posit carries the physics recovery while resting on nothing the programme states. That is the present state, and it is the place a critic presses first.
- *Confidence:* that it can be derived, LOW.

### Tier 1: Decision point 1, strong positivity from the triad (obligations (a), (d); QM-001; failure condition 3)

**1.1 An independent argument for strong positivity.**
This is where the charter's distinctive claim is decided. If strong positivity follows from the triad by an argument that does not pass through Hilbert-space structure, TRT derives what the histories programme postulates, and the Tsirelson bound follows by the known route.
- *Target:* an argument from L₃, I∞, the A-order, and LCP to strong positivity of the quantal measure.
- *Prerequisites:* 0.1, 0.2.
- *Circularity constraint:* the dependency must run triad → strong positivity → Hilbert structure and Tsirelson, never Hilbert structure → strong positivity → Tsirelson. The definitions in 0.1 are fixed before this item begins and may not be tuned toward strong positivity; strong positivity is known in advance to deliver Tsirelson, so a definition tuned to produce it is fitted to its outcome.
- *Failure condition:* no independent argument exists. Then obligation (a) is discharged only by identifying Hilbert structure as contingent specification carried by D, the Tsirelson bound is inherited from that specification, and failure condition 3 applies: a fourth principle is needed, or the derivational ambition reduces to constraint.
- *Confidence:* UNCERTAIN. This is the programme's make-or-break item.

### Tier 2: Decision point 2, the selection rule (obligation (b); ACT-003, PRD-004, OPN-009; failure conditions 1, 2, 4)

**2.1 The record threshold.**
The working channel actualizes a distinction once it is redundantly recorded. Redundancy at threshold two is already excluded by spacelike-separated GHZ experiments, so the threshold must sit in the record itself.
- *Target:* derive, or bound from the co-primitives, a record scale N* above which redundantly recorded distinctions cannot be recohered.
- *Prerequisites:* none formally; informed by Tier 1.
- *Failure condition:* N* cannot be derived or bounded, so it is a fitted parameter; or every N* consistent with GHZ and interferometry data is excluded by collapse-model bounds.
- *Confidence:* that the conjecture is well posed, MEDIUM. That it is true, UNCERTAIN.

**2.2 The discriminating test (PRD-004 with the FLL frontier of WP-TRT-FLL-0002).**
- *Target:* a preregistered extended Wigner's-friend protocol in which TRT predicts Local Friendliness violations below N* and their absence above it, with the rival readings stated.
- *Prerequisites:* 2.1 for the value of N*; the protocol can be specified in parametric form before it.
- *Failure condition:* a friend above a declared N* is recohered (failure condition 1), or a reproducible irreducibly non-bivalent actualization is observed (failure condition 4).
- *Confidence:* that such a protocol can be stated, MEDIUM.

### Tier 3: Decision point 3, gravity on the A-order (obligation (c); PRD-002)

**3.1 The L₃-natural measure on the A-order.**
The A-order is the substrate of record. The question v0.2 posed on a finite relational graph is reposed on it.
- *Target:* define the natural measure of L₃-consistency on a causal set and determine whether its continuum limit is the Benincasa-Dowker action (Einstein-Hilbert plus boundary terms) or carries higher-curvature terms.
- *Prerequisites:* 0.1, 0.3. Full-text verification of the Benincasa-Dowker construction and its continuum-limit results.
- *Failure condition:* the natural measure is quadratic or higher in curvature with no L₃ motivation for the linear form, so TRT gives a modified gravity; or no measure is natural, so the choice is imposed.
- *Confidence:* LOW to MEDIUM.

**3.2 Bridge or retire the finite-graph computation (WP-TRT-GRAV-0001).**
- *Target:* state how GRAV-0001's group-valued graph relates to the A-order, or label it a toy model.
- *Failure condition:* none; this is bookkeeping owed by the 2026-11-16 rulings.

### Tier 4: Measure, recovery, and cosmology (depend on the tiers above)

**4.1 The Born measure (OPN-004).** Reposed as the quantal measure on histories, with the variational desideratum carried by amplitudes in D. Depends on 1.1. *Failure condition:* the measure must be assumed, and TRT inherits the measurement problem's hard core unchanged.

**4.2 Recovery of known physics (OPN-003).** Hilbert space and probability from Tier 1; spacetime from the A-order (obligation (c)); gauge structure and conservation laws are not yet scoped.

**4.3 Cosmological dynamics (OPN-008, ADCE).** A justified growth law with a quantitative scale, discriminated against existing causal-set and dark-energy models. Depends on 0.3 and 3.1.

### Cross-cutting work

- **Formal proof audit.** Every proven theorem carries its axiom audit and proof basis (done 2026-11-17). Next: Lean declarations for the axioms stated in prose only (ACT-002, INT-001, LOG-003, PHY-001), so that what is assumed is machine-visible.
- **Records.** Every attempt from 2026-11-17 is a notebook under [`research-records.md`](research-records.md), with its hypothesis and failure condition committed before its result.
- **Reference verification.** Full-text verification of the external results the charter now depends on: the causal-set and quantum-measure-theory literature (Rideout and Sorkin 2000; Brightwell et al. 2003; Sorkin 1997; Craig et al. 2007; Benincasa and Dowker 2010), and the experimental inputs (Erven et al. 2014; Bong et al. 2020; Donadi et al. 2021). State is tracked in [`references/verification-status.md`](../references/verification-status.md).
- **Publication readiness.** Conform paper v0.10 sections 6.5, 6.6, 7, and 9 to the 2026-09-29 normalization and the charter (they still carry the v0.9 sufficiency reading of `I_L3` and cite sections that no longer exist), then pursue the first DOI-bearing artifact (issue #3).

---

## 3. Dependency graph

```text
0.1 Condition of actualization ──┬──> 0.2 Persistence of Zero ──┐
                                 │                               v
                                 │                    1.1 Strong positivity ──> 4.1 Born measure
                                 │                    (decision point 1)    ──> 4.2 Recovery
                                 │
0.3 Local finiteness ────────────┴──> 3.1 Measure on the A-order ──> 4.3 Cosmology
                                      (decision point 3)
                                      3.2 GRAV-0001 bridge

2.1 Record threshold N* ──> 2.2 Wigner's-friend test (decision point 2)
```

The graph is acyclic. Tier 2 does not formally depend on Tier 1 and can proceed in parallel; a result in 1.1 informs which record structures the measure permits.

---

## 4. Where the v0.2 tasks went

| v0.2 task | Disposition |
|---|---|
| 0.1 Formalize co-admissibility (root) | Tested forms returned a recorded negative, 2026-06-26 (PRD-001). OPN-001 open at the root. No longer the root: discriminating content moved to the selection rule (Tier 2). |
| 0.2 Covariant actualization measure | Reposed as the measure on the A-order (3.1). |
| 1.1 Incompatible-channel test | Executed; the result is PRD-001's recorded negative. |
| 2.1 Lagrangian over χ | The variational desideratum is reposed as amplitudes in D carried to X by the quantal measure (4.1). |
| 2.2 Born rule | 4.1, now dependent on strong positivity (1.1). |
| 3.1 Linearity crux on a finite graph | Reposed on the A-order (3.1); the graph computation is a toy model owing a bridge (3.2). The Lovelock and Regge reduction chain of v0.2 remains the motivation for asking about linearity. |
| 3.2 Frame group and continuum limit | Absorbed into 3.1 and obligation (c). |
| 4.1, 4.2 Recovery and prediction | 4.2 and Tier 2. |
| FLL as governing empirical objective | The charter governs; the FLL falsifier is charter failure condition 4 (2.2). |

The repository plan, contribution terms, licensing, and reference list in v0.2 sections 4 to 7 were founding-era proposals and are now carried by the repository itself: the [README](../README.md) for layout, [CONTRIBUTING.md](../CONTRIBUTING.md) and [github-workflow.md](github-workflow.md) for contribution and branch rules, the two licence files at the repository root, and `references/verification-status.md` for references.

---

## 5. Immediate next actions

1. **0.1 in Lean.** Declare EPA and TC and prove the strict partial order. Open a notebook first, with the failure condition above committed before the attempt. Lean verification by thinx-muse.
2. **1.1 opened as a notebook.** State what an independent argument for strong positivity would have to show, and the circularity constraint, before any attempt.
3. **Verify the primaries** the charter depends on, beginning with the Persistence of Zero statement and Craig et al. (2007).
4. **Re-scope the open-problem issues.** Issues #5 (co-admissibility formalization) and #6 (linearity crux on a finite graph) track v0.2 tasks; re-scope them to 1.1 and 3.1 or close them with a pointer to this section.
5. **Conform paper v0.10** sections 6.5, 6.6, 7, and 9 ahead of the DOI artifact.

**Document version: 0.3** (2026-11-17: rebased on the charter of 2026-11-09 and the rulings of 2026-11-16; organised around the three decision points of the reconciliation map; v0.2 dispositions recorded in section 4).
