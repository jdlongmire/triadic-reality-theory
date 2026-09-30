# Physics Type Split: Under-Determinate and Determinate

**WP:** WP-TRT-QSA-0001  
**Date:** 2026-09-30  
**Status:** candidate architecture for adversarial testing  
**Depends on:** \`level-1-notation-decision.md\`

## Governing claim

Use the Level 1 type split as a physics split beneath the unchanged Level 0 canon:

$$\boxed{\chi \equiv \mathcal{A}(I\mid L)}$$

The split does not create two physical theories. It distinguishes two statuses within the same compact ontology.

- **Under-determinate physics relative to q:** physically relevant or physically instantiated informational structure for which bounded claim q is not settled. The same state may already be determinate actuality under its own state specification q_σ.
- **Determinate physics relative to q:** a settled determinate fact χ_q under fixed q.

“Under-determinate” is always indexed, explicitly or implicitly, to a bounded claim q. It does not mean vague, unreal, nonphysical, merely epistemic, or mathematically unspecified.

## 1. Why q-relativity is mandatory

A prepared quantum state ψ may be completely determinate as a quantum state while under-determinate with respect to a particular observable.

For example, Inst(ψ) can be a settled state-level claim while a z-spin value remains unsettled.

Therefore do not write:

> ψ is indeterminate.

Prefer:

> ψ is physically instantiated and under-determinate relative to q = “definite z-spin value under the specified conditions.”

This prevents state determinacy from being confused with value determinacy.

## 2. Type comparison

| | Under-determinate physics relative to q | Determinate physics relative to q |
|---|---|---|
| Type | σ ∈ I; often Inst(σ); q not settled | χ_q |
| Content | states, amplitudes, fields, dynamical structure, superpositions, entanglement, reduced states | settled fact under fixed q |
| Core question | how instantiated/representable information changes | what determinate fact obtains under q |
| LEM | no q-level bivalent fact is asserted before q is settled | for fixed q, P or not-P is the determinate fact claim |
| Example | ψ(t), Hamiltonian-governed evolution, decohered reduced state | “spin up along z at t” or a determinate pointer record |
| Ontic status | may be physically real | physically real as determinate fact |
| Completeness | need not settle q | settles q only; does not assign all observables |

## 3. Formal marks

### 3.1 Under-determinate relative to q

Use a q-relative predicate rather than treating the whole informational domain as globally indeterminate:

$$U(\sigma,q) \iff \sigma\in I \land \neg\exists\alpha,\chi_q\;\operatorname{Settled}(\alpha,q,\chi_q).$$

Where physical instantiation matters:

$$U_{\mathrm{inst}}(\sigma,q)
\iff
\operatorname{Inst}(\sigma)
\land
\neg\exists\alpha,\chi_q\;\operatorname{Settled}(\alpha,q,\chi_q).$$

This is the principal quantum-mechanical class: real as state, unsettled as a determinate fact under q.

For merely represented, non-instantiated content:

$$U_{\mathrm{rep}}(\sigma)
\iff
\sigma\in I
\land
\neg\operatorname{Inst}(\sigma).$$

Do not conflate U_rep and U_inst.

### 3.2 Determinate relative to q

Use:

$$D_q(\chi_q)
\iff
\exists\alpha\;
\operatorname{Settled}(\alpha,q,\chi_q)
\land
\operatorname{L3Admissible}(\chi_q).$$

This symbol D_q is local to QSA analysis and must not be confused with canonical D, the metaphysical actualizable domain.

A notation amendment may rename D_q before canonical refactor if collision risk remains high.

## 4. Action roles across the split

Primitive Action remains one ontology.

### Non-specifying action

An action occurrence α may produce, sustain, or evolve σ without fixing q.

This is under-determinate physics relative to any q not yet bounded/settled.

### Specifying action

If:

$$\operatorname{Spec}(\alpha,\sigma,q),$$

then q is in force. The question is bounded; its determinate value need not be settled.

This is **specified under-determinate physics** relative to q.

### Settling action

If:

$$\operatorname{Settled}(\alpha,q,\chi_q),$$

then the action occurrence has the derived settling role and χ_q is determinate physics relative to q.

These are statuses/roles of action, not additional primitives.

## 5. Dynamical discipline

The variational/dynamical formalism may govern histories of informational structure without thereby entailing a determinate χ_q.

Candidate discipline:

$$\frac{\delta S}{\delta I}=0 \;\nRightarrow\; \chi_q.$$

A lawful trajectory, unitary evolution, or stationary-action history does not by itself settle every bounded observable claim.

Do not yet canonize a new action functional such as:

$$S[I\mid L]=\int(L_I+L_{\mathrm{Spec}}+\lambda C_L)$$

until each term, measure, and constraint has independent definition. QSA records that expression as a research candidate only.

## 6. Decoherence

Decoherence belongs downstream in the physics-facing belt.

A decohering interaction may move a system, relative to q, from richly under-determinate structure toward **specified under-determinate structure** by dynamically selecting/stabilizing pointer structure and suppressing interference among relevant components.

Decoherence does not, by definition, entail a unique χ_q. This is consistent with standard foundational treatments in which decoherence identifies robust/preferred structures while the relation to unique outcomes depends on interpretation.

Therefore:

$$\mathrm{Decoherence}\;\not\equiv\;\mathrm{Settled}.$$

And only where independently warranted:

$$\mathrm{Decoherence\ interaction}\Rightarrow\operatorname{Spec}(\alpha,\sigma,q).$$

## 7. Everett / MWI test

Do not define MWI as an error in the QSA hard analysis.

Everettian approaches characteristically treat the universal quantum state as fundamental and use decoherence to identify dynamically independent or emergent branch/world structure. Some formulations take all measurement outcomes to obtain in different branches/worlds.

QSA therefore asks a discriminating question:

> Does an Everettian branch-relative determinate record satisfy χ_q only relative to a branch-indexed q, while the global state remains U_inst relative to any non-branch-indexed single-outcome q?

This is a testable typing question inside the framework. It must be answered before TRT claims that MWI “counts the under-determinate sector as χ.”

Candidate outcomes:

1. **MWI maps cleanly to branch-relative χ_q.** Then QSA does not refute MWI; it merely types its actuality claims.
2. **MWI requires globally incompatible χ_q claims under one fixed q.** Then it conflicts with QSA/L3.
3. **The question is interpretation-dependent or under-specified.** Record no verdict.

## 8. Compact status statement

Preferred:

> **Under-determinate physics:** information under Action that is physically meaningful and may be instantiated, while a specified q remains unsettled.
>
> **Determinate physics:** χ_q, the settled fact under q.

Do not say “under-determinate physics = I minus χ” without q-indexing. One σ may be determinate under one claim and under-determinate under another.

## 9. Level 0 mapping

The two statuses remain within:

$$\chi \equiv \mathcal{A}(I\mid L).$$

At Level 1:

- I carries representable content and instantiated structures.
- A supplies primitive action occurrences.
- Spec is a derived role when action bounds q.
- Settled is a derived role/result when action settles q.
- L3 constrains the determinate χ_q and retains its broader canonical admissibility role.
- χ_q is the determinate result under q.

This is refinement of the compact equation, not a second theory.

## 10. Research proposition

The physics-facing proposition to test is:

> **No known physically instantiated quantum state requires contradictory determinate facts under one fixed q. Quantum theory instead requires a distinction between physically instantiated state structure and determinate value actuality.**

This proposition is deliberately weaker than global classical bivalence and does not assume definite values for all observables prior to settlement.

## Disposition

**CANDIDATE FOR ADVERSARIAL TEST.** The type split is accepted as the working QSA physics architecture, with q-relativity mandatory. MWI remains an interpretation to type and test, not a failure condition assumed in advance.
