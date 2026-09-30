# Operational Criteria for Instantiation, Specification, and Settlement

**WP:** WP-TRT-QSA-0001  
**Date:** 2026-09-30  
**Status:** operationalization v1  
**Purpose:** close the three physical-criterion burdens identified by the QSA mapping proof without adding new primitives.

## 1. Method rule

QSA must distinguish ontology from operational warrant.

The predicates \`Inst\`, \`Spec\`, and \`Settled\` are ontological/status claims in TRT. Physics does not warrant them merely because TRT defines them. Each needs independently observable or model-supported criteria.

The criteria below are sufficient-warrant candidates, not definitions of the underlying ontology.

## 2. Inst(σ): physical state-instantiation

### Candidate criterion

Warrant:

$$\operatorname{Inst}(\sigma)$$

when all of the following hold:

1. a physical system is prepared or evolves under independently specified dynamics;
2. σ is required by the successful physical model of that system's state;
3. interventions sensitive to σ's structure produce the predicted physical effects/statistics;
4. replacing σ with a materially different state-description changes those predictions in experimentally discriminable ways.

This treats σ as physically instantiated rather than mere bookkeeping.

### Quantum example

A coherently prepared superposition can satisfy Inst(ψ) because relative phase and coherence affect interference and subsequent measurement statistics. Physical instantiation of ψ does not entail that each basis alternative is already a determinate χ_q.

### Guardrail

Do not infer:

$$\sigma\in I_\infty\Rightarrow\operatorname{Inst}(\sigma).$$

Representability alone never establishes physical instantiation.

## 3. Spec(α,σ,q): objective specification

### Candidate criterion

Warrant:

$$\operatorname{Spec}(\alpha,\sigma,q)$$

when an action/interaction α produces a physically privileged, reproducible coupling or stability relation that fixes which bounded variable/predicate q is operationally discriminated, independent of a later observer's arbitrary relabeling.

Indicators may include:

- stable system-apparatus correlation in the q-basis;
- environment-induced pointer stability/einselection;
- a measurement interaction Hamiltonian that couples the system variable represented by q to a distinct apparatus degree of freedom;
- reproducible discrimination of q-values by the downstream physical apparatus/environment.

### Why this is observer-independent

A human need not inspect the apparatus. The physical coupling can fix q by its interaction structure.

### Guardrail

Specification does not imply a unique value has settled:

$$\operatorname{Spec}(\alpha,\sigma,q)\nRightarrow
\exists\chi_q\;\operatorname{Settled}(\alpha,q,\chi_q).$$

## 4. Settled(α,q,χ_q): determinate physical record

### Candidate criterion

Warrant:

$$\operatorname{Settled}(\alpha,q,\chi_q)$$

when the interaction yields a q-indexed physical record that is:

1. **value-discriminating:** it corresponds to one determinate q-value rather than merely retaining coherent alternatives;
2. **stable enough for re-identification:** subsequent interactions can correlate with the same record without requiring re-preparation of the original system;
3. **redundantly or independently accessible in principle:** more than one downstream physical channel can correlate with the record, or an equivalent objectivity criterion is met;
4. **L3-admissible under fixed q:** the record does not require P and not-P as the same determinate fact under the same bounded claim.

These criteria are inspired by the physics of pointer records and redundant environmental records but do not define settlement as decoherence itself.

### Important limitation

This is an operational warrant for calling a record settled. It is not yet a derivation of why one unique outcome obtains in interpretations where that is a fundamental problem.

Therefore:

$$\mathrm{record\ criterion}\neq\mathrm{solution\ to\ measurement\ problem}.$$

## 5. Decoherence relation

Decoherence/einselection can provide physical warrant for Spec because environmental interaction monitors certain observables and stabilizes pointer states.

It can also help create stable, redundantly accessible records.

But QSA preserves:

$$\mathrm{Decoherence}\nRightarrow\mathrm{Settled}$$

as a general rule.

A specific model may warrant Settled only when the additional record criteria are satisfied and the interpretation licenses the relevant determinate-fact claim.

## 6. Non-quantum structural analogue

The required analogue is a classical dynamical system whose physical state is determinate under its state specification while a different bounded future/event predicate remains unsettled.

### Example: chaotic coin/die dynamics before outcome registration

Consider a physically instantiated coin in flight.

Its instantaneous physical state is real and dynamically evolving. Let q be:

> “Which face will be stably upward after the coin has landed and come to rest relative to the table?”

During flight:

- the coin's physical state is instantiated;
- the dynamics are real;
- q is well-defined;
- no settled terminal record χ_q yet obtains.

After stable rest and record formation:

- the bounded claim q has a determinate physical value;
- a stable orientation can be independently re-observed.

This is not quantum indeterminacy. Given a sufficiently complete classical state, the outcome may be dynamically determined. The analogy concerns **type/status**, not mechanism:

> actual instantiated state ≠ already settled fact for every q about that state's trajectory.

Thus the distinction between state actuality and q-relative determinate fact actuality is not uniquely quantum.

### Stronger deterministic form

Even in a fully deterministic classical model, a present state can be actual while a future-indexed q is not yet instantiated as a present physical record.

QSA therefore does not define under-determinacy as metaphysical randomness.

## 7. Criteria summary

| Predicate | Operational warrant |
|---|---|
| \`Inst(σ)\` | σ has discriminable physical consequences in a successfully controlled/modelled system |
| \`Spec(α,σ,q)\` | interaction objectively privileges/discriminates q through physical coupling/stability |
| \`Settled(α,q,χ_q)\` | a stable, value-discriminating, physically re-identifiable/accessible q-record exists and is L3-admissible |
| \`U_inst(σ,q)\` | Inst(σ) holds while no warranted settled q-record exists |

## 8. Falsification / downgrade conditions

Downgrade QSA if:

1. Inst cannot be operationally distinguished from mere mathematical representation;
2. Spec can only be defined by a conscious observer choosing a question;
3. Settled can only be defined circularly as “whatever is χ_q”;
4. the record criterion covertly assumes the unique-outcome result it is meant to warrant;
5. the classical analogue collapses because q-relative unsettled status is shown to be purely epistemic and irrelevant to the proposed ontological typing.

## 9. Disposition

**PROVISIONAL PASS.**

- Inst has an independent physical-warrant criterion.
- Spec has an observer-independent interaction criterion.
- Settled has an observer-independent record criterion, but the criterion does not solve the unique-outcome measurement problem.
- A non-quantum type analogue exists in ordinary dynamical systems: an actual evolving state can precede a settled q-indexed terminal record.

The remaining burden is to test these criteria against the active quantum/decoherence literature and then determine whether they are strong enough for canonical refactor.
