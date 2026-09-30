# CORE-0001 Reconciliation

**WP:** WP-TRT-QSA-0001  
**Date:** 2026-09-30  
**Status:** reconciliation decision v1  
**Target:** WP-TRT-CORE-0001 and canonical R → D → X architecture

## Question

Does specification-relative determinacy require superseding the normalized hard-core architecture:

$$R\xrightarrow{L_3\;\mathrm{necessary\ filter}}D\xrightarrow{A}X(\chi)?$$

## Decision

**No supersession is required, provided L3-admissibility is read as logical admissibility of the represented state/claim at its proper specification, not as a global pre-assignment of definite classical values to every observable.**

The CORE-0001 architecture survives with a typing clarification.

## 1. What the L3 filter means

For any represented candidate x at the specification under which x is being proposed:

$$x\in D\Rightarrow \operatorname{Adm}_{L_3}(x).$$

This means an actualizable candidate cannot require a genuine logical contradiction in the claim that constitutes that candidate.

It does **not** mean:

- every observable associated with x already has a definite value;
- every amplitude is assigned True/False;
- every possible measurement question is already specified;
- all representable predicates are jointly co-selected;
- quantum contextuality is ignored.

## 2. Quantum state as candidate x

Let x be the quantum state ψ under state specification q_ψ.

Then ψ can be L3-admissible as ψ:

- Identity: ψ is ψ.
- Non-Contradiction: the state claim does not require ψ and not-ψ as the same state.
- Excluded Middle: under fixed q_ψ, the system is in ψ or it is not.

Thus:

$$\psi\in D$$

is compatible with q-relative under-determinacy for another observable claim q.

The L3 filter applies to the candidate actually under consideration. It does not distribute definite values over all predicates representable within or about that candidate.

## 3. R remains broader than D

Representability still outruns logical admissibility.

Contradiction-encoding informational content may be representable in R without being L3-admissible as a candidate actuality.

Therefore the CORE-0001 distinction remains meaningful:

$$R\supsetneq \operatorname{Adm}_{L_3}.$$

QSA does not collapse R into D or X.

## 4. D remains stronger than L3-admissibility

CORE-0001 already refuses:

$$\operatorname{Adm}_{L_3}(x)\Rightarrow x\in D.$$

QSA preserves that refusal.

A logically coherent represented state may still fail other physical/metaphysical actualizability conditions.

Thus the necessary-filter language remains valid.

## 5. A remains primitive

QSA does not alter CORE-0001's definition of A as fundamental non-temporal state transition/change.

Specification and settlement are downstream roles of action occurrences:

$$\alpha:\mathbf{Act}.$$

They do not alter the primitive triad.

## 6. X and χ

CORE-0001's X remains the actual domain.

Bare χ remains the compact Level 0 result in:

$$\chi\equiv\mathcal A(I\mid L).$$

QSA adds indexed χ_q only where a bounded determinate claim must be distinguished from the total/domain-level actuality notation.

This is a typing clarification, not a new output primitive.

## 7. Required canonical clarification

The phrase:

> “L3 constrains what may determinately obtain”

should be retained.

Add, where QSA is integrated:

> **L3-admissibility is specification-relative. It constrains the represented state or claim actually under consideration. It does not assign pre-existing definite values to every observable or represented alternative associated with that state.**

This sentence is sufficient to block the quantum misreading without changing the hard core.

## 8. LEM clarification

Excluded Middle is applied to a bounded proposition.

For q_ψ:

> the system is in ψ or it is not.

For a settled observable q:

> P or not-P under q.

QSA does not require a q-level value before q is specified/settled merely because the state ψ is L3-admissible.

Therefore LEM does not entail global definite-value realism.

## 9. Non-Contradiction clarification

Non-Contradiction applies under the same specification.

A superposition written as a linear combination of basis vectors is not thereby the proposition:

> P and not-P are both settled facts under one q.

Thus superposition is not excluded by the L3 filter merely because a chosen basis representation contains alternatives.

## 10. Identity clarification

Identity applies at every typed level where a candidate state/claim is determinate enough to be the subject of predication.

This includes ψ as state and χ_q as bounded fact.

QSA therefore does not place pre-outcome physics “outside logic.”

## 11. Formalization impact

Current Lean:

\`L3Admissible : Representable → Prop\`

can remain at the hard-core abstraction level.

However, QSA integration should document that the predicate is evaluated relative to the represented candidate/specification and does not encode a global valuation over every observable.

A future richer formalization may introduce q-indexed propositions without changing the existing necessary direction:

\`Actualizable r → L3Admissible r\`.

No immediate hard-core theorem deletion is required.

## 12. Reconciliation result

| CORE-0001 commitment | QSA effect |
|---|---|
| L3 is co-primitive constraint | preserved |
| I∞ is unbounded representability | preserved |
| A is primitive action | preserved |
| R → L3 necessary filter → D | preserved with specification-relative clarification |
| L3 sufficiency for D is open | preserved |
| X/χ is what obtains | preserved at Level 0; typed at Level 1 |
| representability ≠ actualizability | strengthened |
| measurement interpretation outside hard core | preserved |

## 13. Failure check

No contradiction remains between CORE-0001 and QSA if “L3-admissible” is not misread as “globally bivalently valued.”

If future formalization proves that CORE-0001 necessarily encoded global noncontextual value assignment, this reconciliation fails and supersession would be required. The current Lean core does not encode such a valuation.

## Verdict

**RECONCILED. CORE-0001 survives.**

QSA is a typed clarification beneath the existing hard core, not a replacement of it.

## Next gate

Sharpen q and the identity criterion for “same specification,” then decide the exact χ_q formal type before modifying Lean or canonical prose.
