# Bounded Claim q and Determinate Fact Type

**WP:** WP-TRT-QSA-0001  
**Date:** 2026-09-30  
**Status:** pre-formalization type decision v1

## 1. Purpose

Freeze the identity conditions for a bounded claim q and choose the weakest adequate formal type for χ_q.

The goal is to prevent “same subject / same respect” from becoming elastic while avoiding unnecessary commitment to a particular quantum interpretation or physical ontology.

## 2. Bounded claim

Refine:

$$q=\langle x,P,c,r\rangle$$

to the typed structure:

$$q=\langle x,\mathcal P,\kappa,\rho\rangle.$$

Where:

- **x** = subject/system identifier;
- **P** = predicate, property, observable, or proposition-schema applied to x;
- **κ** = conditions/context required to evaluate P, including temporal index where relevant, measurement/basis/context data where relevant, and branch/index data only where the physical interpretation requires it;
- **ρ** = respect/semantic mode fixing what P means in this claim.

These components are fields of a specification record, not ontological primitives.

## 3. Same-q criterion

Two bounded claims q1 and q2 count as the same specification iff all four fields are extensionally the same for the evaluation at issue:

$$q_1\equiv_q q_2
\iff
x_1=x_2
\land
\mathcal P_1=\mathcal P_2
\land
\kappa_1=\kappa_2
\land
\rho_1=\rho_2.$$

No field may be changed after a contradiction test is posed.

If a proposed P/not-P pair differs in subject, predicate meaning, context/condition, branch, basis, temporal index, or respect, it is not a same-q contradiction.

## 4. Why κ and ρ are separate

κ carries physical/evaluative conditions.

ρ carries semantic respect.

Example:

- “door is physically open” and
- “facility is legally open”

may share subject and time but differ in ρ.

Likewise, incompatible quantum measurement contexts belong in κ, not in a post-hoc change to the predicate.

This separation prevents semantic equivocation from being hidden inside “context.”

## 5. State claim q_σ

For an informational/physical state σ define a state claim:

$$q_\sigma=\langle x,\operatorname{InState}(\sigma),\kappa,\rho_{\mathrm{state}}\rangle.$$

Where physical instantiation is warranted:

$$\operatorname{Inst}(\sigma)\Rightarrow\chi_{q_\sigma}.$$

This is determinate actuality of the state under the state specification.

It does not entail determinate values for every other q definable over σ.

## 6. Observable/value claim q_P

For an observable/property claim:

$$q_P=\langle x,P,\kappa,\rho_P\rangle.$$

A state may satisfy χ_{q_σ} while q_P remains unsettled.

Thus:

$$\chi_{q_\sigma}\not\Rightarrow\chi_{q_P}.$$

## 7. Branch/context indexing

Do not add branch identity as a universal fifth field.

If an interpretation requires branch-relative evaluation, branch identity belongs inside κ.

Therefore Everettian branch-relative claims differ because κ differs, not because QSA adds an Everett-specific primitive.

Likewise basis/measurement context belongs in κ when physically relevant.

## 8. Temporal discipline

Time is not a mandatory primitive field independent of κ.

Where temporal indexing is physically meaningful, it is carried inside κ.

This preserves TRT's commitment that primitive Action is non-temporal in definition.

## 9. Candidate χ_q types considered

### Option A: χ_q as proposition

Rejected as too weak.

A proposition can represent a claim without establishing that it obtains. This would collapse determinate actuality back into representation.

### Option B: χ_q as physical state

Rejected as too narrow.

Determinate facts may concern relations, records, mental acts, mathematical/structural facts within the ontology, or other non-state propositions. QSA should not define all determinate actuality as physical state.

### Option C: χ_q as truth value

Rejected.

χ_q is the determinate actuality/fact, not merely the semantic value assigned to a sentence about it.

### Option D: χ_q as indexed actuality witness / state-of-affairs

Accepted.

Define χ_q as a witness that bounded claim q obtains as determinate actuality.

At the formal level:

$$\chi_q : \operatorname{Obtains}(q).$$

This is intentionally dependent/indexed: the type of χ_q carries q.

A different q yields a different actuality-witness type.

## 10. Formal reading

Use:

$$\operatorname{Obtains}(q):\mathbf{Prop}$$

and:

$$\chi_q : \operatorname{Obtains}(q).$$

In a proof assistant, χ_q is therefore evidence/witness that q obtains, not a global object containing all reality.

This cleanly distinguishes:

- q: represented bounded claim;
- Obtains(q): actuality proposition/status;
- χ_q: witness of determinate actuality under q.

## 11. Negation

For a fixed q whose predicate is P, the contrary bounded claim must preserve x, κ, and ρ while replacing P by its defined negation.

Write:

$$\neg q=\langle x,\neg P,\kappa,\rho\rangle.$$

A same-q contradiction would require witnesses for both:

$$\chi_q:\operatorname{Obtains}(q)$$

and

$$\chi_{\neg q}:\operatorname{Obtains}(\neg q)$$

under the same x, κ, and ρ.

L3 excludes this as determinate actuality.

## 12. Excluded Middle

For a properly bounded q:

$$\operatorname{Obtains}(q)\lor\neg\operatorname{Obtains}(q).$$

This is not a claim that every possible q is already physically specified or measured.

It states the LEM form once q is a well-formed bounded proposition.

QSA must continue to distinguish:

- existence/formation of q;
- physical specification of q by an action;
- settlement/witness χ_q.

## 13. Specification relation

Retain:

$$\operatorname{Spec}(\alpha,\sigma,q).$$

The relation fixes q. It does not prove Obtains(q).

## 14. Settlement relation

Refine settlement as:

$$\operatorname{Settled}(\alpha,q,\chi_q)$$

where:

$$\chi_q:\operatorname{Obtains}(q).$$

Settlement therefore relates an action occurrence, bounded claim, and actuality witness.

This remains relational. QSA does not assume uniqueness of α or of the physical route to the same fact.

## 15. Identity of determinate facts

Two witnesses may support the same q without being numerically the same proof object or physical record.

Therefore QSA does not require:

$$\chi_q^{(1)}=\chi_q^{(2)}.$$

What matters for fact identity is that both witness the same Obtains(q).

This prevents redundant records from becoming multiple incompatible realities merely because they are distinct physical tokens.

## 16. L3 typing

L3 applies to well-formed bounded claims and their determinate actuality.

Identity:
q remains the same q under the frozen field criteria.

Non-Contradiction:
there cannot be determinate actuality witnesses for q and its genuine negation as the same fact under the same specification.

Excluded Middle:
for well-formed q, Obtains(q) or not-Obtains(q).

This does not impose a value on a different q.

## 17. Consequence for χ notation

Bare χ remains Level 0.

At Level 1:

- X / Actual = actual domain/type;
- q = bounded representable claim;
- Obtains(q) = actuality proposition/status;
- χ_q = witness of determinate actuality for q.

This is the recommended formal type.

## 18. Lean target

Candidate future Lean structure:

\`\`\`lean
structure BoundedClaim where
  subject   : Subject
  predicate : Predicate subject
  context   : Context subject predicate
  respect   : Respect subject predicate context

opaque ObtainsQ : BoundedClaim → Prop

def ChiQ (q : BoundedClaim) : Type := ObtainsQ q

opaque Spec :
  ActionOccurrence → Representable → BoundedClaim → Prop

opaque Settled :
  (a : ActionOccurrence) → (q : BoundedClaim) → ChiQ q → Prop
\`\`\`

This is a target sketch only. Exact dependent types must be tested against the existing core before commit.

## 19. Falsification discipline

A proposed violation of L3 must register q before evaluation.

Required record:

1. subject x;
2. predicate P;
3. context κ;
4. respect ρ;
5. warrant for q and neg-q being genuine negations under those same fields;
6. warrant for determinate actuality of both.

Changing any field after the result is known invalidates the test.

## Verdict

**TYPE DECISION PASS.**

q is frozen as a four-field bounded claim with extensible context κ. χ_q is best typed as an indexed actuality witness/state-of-affairs:

$$\chi_q:\operatorname{Obtains}(q).$$

This is weaker than defining χ_q as a physical state and stronger than treating it as a mere proposition or truth value.

## Next gate

Prototype this structure in Lean against the existing CORE primitives. If it typechecks without redefining L3, I∞, A, Actualizable, Obtains, or Actual, proceed to controlled canonical refactor.
