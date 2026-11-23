# L–I–A Necessity: Formal Status and Adversarial Audit

**Date:** 2026-11-22  
**Tier:** research work package / formalization scoping; no promotion to established theorem  
**Status:** proposed, proof obligations open  
**Authority:** owner direction to investigate the claim “There is no reality without the three”; read with `1-hypothesis/hard-core.md`, `0-program-methods/TRT-charter.md`, and WP-TRT-CORE-0001.

## 1. Claim and scope

For **determinate actuality in the constituted order**, propose:

```text
N-LIA: Necessarily, if χ obtains, then L₃, I∞, and A are jointly required.
        □(χ → (L₃ ∧ I∞ ∧ A))
```

This is a **candidate metaphysical necessity claim**. It is not an independently established theorem. The modal operator requires a declared semantics and a domain of possible worlds or admissible models. L₃ means Identity, Non-Contradiction, and Excluded Middle scoped to propositions over actualized states. I∞ denotes the unbounded representable domain, **not** a claim that any actual event carries infinite information. A denotes fundamental non-temporal state transition/change, **not** “actualization” by definition.

**Boundary:** The charter distinguishes the Logos, the common source, from the triad constituted in the created order. Divine being is not an A-event and divine agency is related analogically to A. Therefore the universal phrase “no reality without the three” must be typed carefully: it cannot silently quantify over divine being as though the Logos depends upon created state transitions. A separate Logos-grounding thesis may say the divine nature, intellect, and will are eternally inseparable without equating them literally with the created-order co-primitives.

## 2. Three distinct claims

1. **Necessity:** χ entails each of L₃, I∞, A, with scope fixed as above.
2. **Irreducibility:** no one co-primitive is definable or derivable solely from the other two under a noncircular interpretation.
3. **Sufficiency:** the three together entail determinate actuality (or determine D). **Not established**. The repository expressly keeps R, L₃-admissibility, D, and X distinct; L₃ alone does not exhaust D.

The converse `(L₃ ∧ I∞ ∧ A) → χ` is not authorized by the necessity thesis.

## 3. Conditional derivation ledger

| ID | Candidate result | Additional premise | Status |
| --- | --- | --- | --- |
| N1 | χ → L₃ | Determinate obtaining requires identity and consistent predication; excluded middle applies only over actualized-state propositions | Argued, not proven |
| N2 | χ → I∞ | Actuality requires distinguishable informational content; justify why *unbounded representability* rather than minimal differentiation follows | **Gap** |
| N3 | χ → A | Obtaining must be linked to an A-event or a typed initial condition; test static/eternal actualities and avoid defining A as obtaining | **Gap** |
| N4 | χ → (L₃ ∧ I∞ ∧ A) | N1, N2, N3 | Derivable propositionally *if* premises hold |
| N5 | □(χ → triad) | Modal necessity of N1–N3 in all relevant admissible models | **Gap** |
| IR1–IR3 | Pairwise irreducibility | Independent noncircular semantics and countermodel exclusions | Argued, open |
| S1 | Triad → χ | Complete D specification and actualization conditions | Not established |

A proof assistant can verify the implication N4 from N1–N3; that is a **conditional theorem**, not a proof of the metaphysical premises.

## 4. Adversarial tests

- **Static-world countermodel:** Can a timeless, changeless, determinate created reality obtain without A? If excluded, state and defend the exclusion independently.
- **Initial-state countermodel:** Does the charter's initial condition allow an obtaining state not targeted by an A-event? If so, revise N3 or type χ as event actuality.
- **Finite-content countermodel:** Does a single actual distinction require I∞ or only some I? Distinguish global domain presupposition from event-level information.
- **Logic scope:** Does the claim about excluded middle cover only propositions over actualized states? Avoid assigning definite values to unactualized properties.
- **Modal strength:** What makes the claim necessary in every admissible model rather than true by stipulative model restriction?
- **Reduction test:** Can L, I, and A be collapsed into one primitive with three predicates? Define a non-question-begging criterion for irreducibility.
- **Logos typing:** Ensure no derivation makes divine being contingent upon an A-event or equates divine willing with temporal change.
- **Naturalism comparison:** Distinguish explanatory gaps, brute-fact commitments, and proven contradictions. No conclusion of naturalism's logical impossibility follows from N-LIA alone.

## 5. Planned verification

1. Define typed signatures for `Representable`, `AdmissibleL3`, `Actualizable`, `Obtains`, `TransitionA`, and `InitialCondition`.
2. Specify modal semantics and quantifier domains; show a conditional Lean proof of N4 without presenting assumptions as discoveries.
3. Build and document countermodels for N2, N3, and N5; state exact strengthening axioms needed to exclude them.
4. Check consistency against the current charter's 2026-11-12 and 2026-11-16 amendments and the hard core.
5. Submit adversarial review before any promotion of theorem, necessity, or empirical status.

## 6. Acceptance criteria

A successful work package produces a reproducible typed model, an assumption ledger, conditional derivations, explicit countermodels or exclusions, and a documented disposition for each gap. Failure to establish any necessity claim is recorded as a substantive result. No changes to the canonical hard core, claim registry, or theorem status occur without separate evidence and review.

## 7. Source provenance

Primary project sources reviewed directly in GitHub: `README.md`; `1-hypothesis/hard-core.md`; `0-program-methods/METHODOLOGY.md`; `0-program-methods/TRT-charter.md`; `05-work-packages/WP-TRT-CORE-0001-co-primitive-normalization/package.yaml`. Operational bootstrap: `jdlongmire/ai-bridge/bootstrap/EBCC-001.md` v1.0. No external philosophical or scientific citations are asserted here.
