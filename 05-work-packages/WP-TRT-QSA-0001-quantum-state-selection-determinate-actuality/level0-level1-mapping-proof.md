# Level 0 ↔ Level 1 Mapping Proof

**WP:** WP-TRT-QSA-0001  
**Date:** 2026-09-30  
**Status:** mapping proof v1  
**Question:** Is the QSA typed architecture an unpacking of the canonical compact equation, or does it add new ontology?

## 1. Canonical Level 0

TRT retains:

$$\boxed{\chi \equiv \mathcal{A}(I\mid L)}$$

with the canonical reading:

> Logic constrains. Information is the representable content. Action actualizes. χ is the determinate result.

The proof obligation is conservative extension:

> Every Level 1 symbol must be either (a) a typed specialization of L, I, A, or χ; (b) a variable ranging over one of those types; or (c) a derived relation/status among them. No Level 1 term may introduce a new irreducible ontological engine.

## 2. Mapping criterion

Let the Level 0 vocabulary be:

$$V_0=\{L,I,A,\chi\}.$$

Let the Level 1 vocabulary be:

$$V_1=\{L_3,I_\infty,\sigma,\operatorname{Inst},\alpha,q,\operatorname{Spec},
\operatorname{Settled},X,\chi_q\}.$$

QSA is a conservative typed refinement only if every member of V1 is reducible to a type, instance, status, or relation grounded in V0.

## 3. Logic mapping

### Level 0

L = constraint structure.

### Level 1

L3 is the canonical explicit logical constraint structure:

$$L_3=\{\mathrm{Identity},\mathrm{NonContradiction},\mathrm{ExcludedMiddle}\}.$$

Mapping:

$$L_3 \subseteq_{\mathrm{role}} L.$$

This notation means role-specialization, not set-theoretic containment unless a later formal model supplies the relevant carrier.

QSA uses L3 explicitly at determinate χ_q while preserving CORE-0001's broader admissibility role.

### Result

**PASS.** L3 is already canonical and introduces no new primitive.

## 4. Information mapping

### Level 0

I = representable/differentiated informational content.

### Level 1

I∞ = unbounded representability.

A particular:

$$\sigma\in I_\infty$$

is an instance/member of informational structure.

Mapping:

$$I \rightsquigarrow I_\infty,\sigma.$$

No new ontological category is added. The distinction is domain versus member.

### Result

**PASS.**

## 5. Physical instantiation mapping

\`Inst(σ)\` is a predicate asserting that informational structure σ is physically instantiated as a state.

It is not a primitive operator and does not cause instantiation.

Its content can be expanded as:

> there exists an actual physical state whose informational structure is σ.

Thus Inst is a status predicate relating I-level structure to the actual domain X.

Schematic:

$$\operatorname{Inst}(\sigma)\Rightarrow \exists x\in X\;\operatorname{Structure}(x)=\sigma.$$

The equality is schematic and must not be promoted to a formal identity without a carrier/type model.

### Result

**PASS as a derived cross-type predicate.**

### Open burden

The formalization must define the relation without reducing physical statehood to information by stipulation.

## 6. Action mapping

### Level 0

A = primitive Action/state transition/change.

### Level 1

$$\alpha:\mathbf{Act}$$

is an occurrence/token of primitive Action.

Mapping:

$$\alpha\in\operatorname{Occ}(A).$$

No new primitive is introduced. The type/token distinction merely prevents A from being overloaded as both primitive category and individual occurrence.

### Result

**PASS.**

## 7. Bounded claim q

$$q=\langle x,P,c,r\rangle$$

packages the subject, predicate/observable, conditions, and respect under which a determinate fact is evaluated.

q does not cause, constrain, represent, or actualize anything by itself. It is a typed informational specification.

Therefore:

$$q\in I$$

at the representational level, subject to coherence/admissibility constraints where applicable.

q is not a fifth ontological constituent.

### Result

**PASS as typed informational content.**

## 8. Specification mapping

\`Spec(α,σ,q)\` says that action occurrence α acquires the role of fixing q as the bounded respect in force relative to σ.

The relation contains:

- α, already typed under A;
- σ and q, already typed under I;
- applicability under L.

No independent selector S is posited.

Therefore Spec is a derived relation among A- and I-typed terms under constraint L.

Schematic expansion:

$$\operatorname{Spec}\subseteq \mathbf{Act}\times I\times I.$$

The exact admissibility conditions remain open.

### Result

**PASS as a derived role relation.**

### Failure condition

If specification requires an irreducible selector not characterizable as an action-role/relation among existing types, QSA would cease to be conservative.

No such requirement has been demonstrated.

## 9. Settlement mapping

\`Settled(α,q,χ_q)\` says that action occurrence α acquires the derived role/result relation in which bounded q obtains as determinate χ_q.

The terms map to:

- α → A;
- q → I;
- logical constraint → L;
- χ_q → χ typed to bounded determinate result.

Thus Settled is the Level 1 expansion of the **actualizes** role compressed into Level 0 A.

It is not a second actualization primitive.

### Result

**PASS as a derived role/result relation.**

### Failure condition

If settling requires an irreducible actuality-conferring entity or operator distinct from A, L, I, and χ, the compact ontology would require revision.

QSA has not established such a requirement.

## 10. Actual domain X

X denotes the typed domain of what obtains.

The existing normalized architecture already uses:

$$R\to D\to X(\chi).$$

QSA uses X to prevent bare χ from being overloaded in Level 1 reasoning.

X is therefore a type/domain notation for actuality already compressed into the result side of Level 0 χ.

### Result

**PASS; pre-existing canonical type distinction.**

## 11. Determinate χ_q

χ_q is χ typed relative to bounded q.

It does not add a new result-kind. It prevents the Level 0 result symbol from simultaneously denoting:

- the total actual domain;
- a physically instantiated state;
- a determinate bounded fact.

Mapping:

$$\chi_q\rightsquigarrow \chi\;\text{under fixed }q.$$

### Result

**PASS as subtype/indexed specialization.**

## 12. Under-determinate status U

The QSA physics split uses U(σ,q) only as a status predicate:

$$U(\sigma,q)\iff \sigma\in I\land\neg\exists\alpha,\chi_q\;\operatorname{Settled}(\alpha,q,\chi_q).$$

U therefore introduces no ontological object. It abbreviates absence of a settlement relation for q.

### Result

**PASS as definitional abbreviation.**

## 13. Full expansion

The compact expression:

$$\chi \equiv \mathcal{A}(I\mid L)$$

licenses the following Level 1 analysis for a determinate bounded fact:

1. informational structure σ is represented in I∞;
2. an action occurrence α may act upon/evolve/sustain instantiated or available σ;
3. some action occurrence may acquire the derived specification role \`Spec(α,σ,q)\`;
4. some action occurrence may acquire the derived settlement role \`Settled(α,q,χ_q)\`;
5. χ_q is a determinate result under q;
6. L3 explicitly constrains the determinate result and retains its broader canonical admissibility role.

None of steps 2–4 is required to be temporally successive by the notation alone. Distinct α occurrences may instantiate the roles, or one α may bear multiple roles, depending on the physical model.

## 14. Compression recovery

Starting from Level 1, erase the typing detail:

- erase token α to primitive A;
- erase σ/q distinction to informational content I;
- erase Spec and Settled as named derived roles and retain their parent role under A;
- erase χ_q indexing to χ;
- abstract L3 to compact constraint structure L.

The resulting expression is:

$$\boxed{\chi \equiv \mathcal{A}(I\mid L)}.$$

Therefore the compact equation is recoverable without residue.

## 15. No-residue test

A conservative refinement should leave no irreducible Level 1 term after compression.

| Level 1 term | Compression target | Residue? |
|---|---|---|
| L3 | L | No |
| I∞ | I | No |
| σ | I-instance | No |
| Inst(σ) | actuality/status relation between I and X | No new engine |
| α | A-occurrence | No |
| q | I-level bounded specification | No |
| Spec | derived A/I relation | No |
| Settled | derived A/I/χ relation under L | No |
| X | actual-domain typing of χ-result side | No |
| χ_q | indexed χ | No |
| U(σ,q) | definitional status abbreviation | No |

### Result

**NO IRREDUCIBLE RESIDUE FOUND.**

## 16. Two remaining nontrivial burdens

The mapping proof is ontological/type-theoretic, not yet physical.

### Burden A: physical criteria

QSA still owes observer-independent physical criteria for when Spec and Settled are warranted.

Failure to supply those criteria would make the Level 1 architecture explanatorily thin, but would not by itself introduce a fourth primitive.

### Burden B: Inst relation

QSA must avoid defining Inst so that “physical” simply means “informational structure in X.” That would trivialize the state-instantiation distinction.

The formal/physics layer must supply independent physical conditions for state instantiation.

## 17. Theorem-status discipline

This document establishes only:

> **Conservative-typing result:** the current QSA Level 1 vocabulary can be mapped to the existing Level 0 ontology without an identified additional co-primitive.

It does **not** prove:

- that the compact equation is metaphysically true;
- that Spec or Settled has a unique physical realization;
- that settlement occurs in every quantum interpretation;
- that χ_q is globally bivalent for all possible predicates;
- that the Born rule follows;
- that decoherence entails settlement;
- that MWI is false.

## Verdict

**PASS: Level 1 is a conservative typed expansion of Level 0, conditional on the open physical criteria for Inst, Spec, and Settled.**

The original compact equation remains canonical:

$$\boxed{\chi \equiv \mathcal{A}(I\mid L)}.$$

QSA refines its types. It does not replace its ontology.

## Next gate

Before canonical refactor, close or sharply operationalize:

1. observer-independent Spec criterion;
2. observer-independent Settled criterion;
3. independent physical Inst criterion;
4. non-quantum structural analogue of instantiated-but-q-under-determinate state.

Only then should the active canonical surfaces be revised.
