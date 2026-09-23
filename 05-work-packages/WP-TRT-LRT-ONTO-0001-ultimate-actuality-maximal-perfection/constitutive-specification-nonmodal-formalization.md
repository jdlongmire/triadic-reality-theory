# Constitutive Specification Without Modal Smuggling

**WP:** WP-TRT-LRT-ONTO-0001
**Date:** 2026-09-23
**Status:** formalization v0.1
**Target:** define Spec_c(x) without possible/necessary/could/must vocabulary

## 1. Problem

CCAC-2 requires a constitutive informational specification Spec_c(x). The definition fails if "constitutive" is cashed out modally.

Prohibited definitions include:

- properties x necessarily has;
- properties x has in every possible world;
- properties x could not lack;
- conditions required for x to be metaphysically possible.

The target is a non-modal specification relation.

## 2. Primitive proposal: determination

Let Delta(p,x) mean:

p participates in fixing the determinate identity/content of x.

Delta is not defined as necessary predication. It is a typed determination relation between informational content p and represented item x.

Let Spec_c(x) be:

Spec_c(x) := {p | Delta(p,x)}.

The intended question is "What fixes what x is?" rather than "What must x be?"

This follows the real-definition direction associated with Fine while avoiding, at the definition stage, modal vocabulary.

## 3. Admissibility test for Delta

Delta is acceptable only if instances can be justified through non-modal relations such as:

1. identity/reference fixing;
2. explicit definition;
3. structural composition;
4. constitutive dependency;
5. type/kind determination;
6. relation-position determination;
7. mathematical construction;
8. informational invariance under redescription.

No instance may be justified merely by saying p is necessary for x.

## 4. Core subrelations

Define candidate subrelations:

IdFix(p,x): p fixes the referent/identity conditions for x.

Def(p,x): p occurs in or follows from the real/constitutive definition of x.

Struct(p,x): p specifies a constitutive structural relation of x.

Dep_c(p,x): x is constituted or determined in part by the relation expressed by p.

TypeFix(p,x): p fixes the kind/type under which x is represented.

Then:

Delta(p,x) := IdFix(p,x) OR Def(p,x) OR Struct(p,x) OR Dep_c(p,x) OR TypeFix(p,x).

This is a research schema, not a claim that the disjunction is complete.

## 5. Accidental information

Let Acc(p,x) mean p describes x without participating in fixing what x is.

Then:

Spec(x) = Spec_c(x) union Spec_a(x),

where:

Spec_a(x) := {p | Acc(p,x)}.

No modal definition of Acc is permitted.

Examples should be established by explanatory/dependency analysis, not by "x could have lacked p."

## 6. Explanatory asymmetry

A promising non-modal discriminator is explanatory priority.

If p belongs to Spec_c(x), then p helps explain why a correct representation counts as a representation of x of that type/identity.

Accidental q does not perform that identity-fixing role.

This yields candidate criterion:

Delta(p,x) -> Explain(p, IdentityContent(x)).

The converse is not yet assumed.

## 7. Finean interface

Fine's real-definition approach treats essence as connected to what an object is rather than reducing it to de re necessity. This supports the direction of the present proposal, but Fine treats essence as primitive and does not thereby supply TRT/LRT with a completed informational reduction.

Therefore:

Finean real definition != proven Spec_c reduction.

The present project asks whether real-definition structure can be represented as informational determination under logical closure.

## 8. Mackie constraint

Mackie's challenge is decisive methodologically: if real definition cannot be isolated without modal assumptions, then Spec_c has not discharged the modal burden.

Accordingly every proposed Delta instance must carry a provenance tag:

- DEF: explicit definitional determination;
- ID: identity/reference determination;
- STR: structural determination;
- DEP: constitutive dependency;
- TYPE: kind/type determination;
- MODAL: justified only by modal premise.

MODAL-tagged content may not be used to prove CCAC-2 without circularity.

## 9. Constraint closure

Define:

Cl_L(Spec_c(x))

as closure of constitutive information under logical consequence and constitutive dependency rules admitted independently of modal vocabulary.

Then:

Coh_c(x) iff bottom not-in Cl_L(Spec_c(x)).

Conditional form:

Coh_c(x,Y) iff bottom not-in Cl_L(Spec_c(x) union Spec(Y)).

Candidate:

D(x) ?<=> Coh_c(x).

The right-to-left direction remains open.

## 10. Test cases

### Euclidean triangle

Spec_c(T) includes the definitional/structural relations constituting a Euclidean triangle. "T has four sides" conflicts under closure.

Result: excluded without modal premise.

### Water/H2O

If empirical identity inquiry establishes that the referent water is H2O, that identity fact is ID-tagged in Spec_c(water). "Water is non-H2O" then conflicts under identity closure.

The fact may be discovered a posteriori while functioning constitutively once established.

### Socrates and singleton Socrates

Fine's classic pressure case distinguishes "Socrates is Socrates" from "Socrates belongs to {Socrates}" despite necessary equivalence. Spec_c should preserve this hyperintensional distinction because IdFix/Def provenance differs.

Thus logical equivalence alone does not collapse determination provenance.

### Creaturely choice

A creature C under circumstances Y may have action a and b each compatible with Spec_c(C) union Spec(Y).

This yields CAN(a|Y) and CAN(b|Y) if closure remains contradiction-free.

Nothing in Spec_c alone yields WOULD(a|Y) or WOULD(b|Y).

## 11. Hyperintensionality requirement

Spec_c cannot be modeled merely as an unstructured set of truth-valued propositions modulo logical equivalence.

It must preserve at least:

- provenance;
- direction of determination;
- dependency structure;
- identity/reference role.

Therefore represent constitutive specification as a graph:

G_c(x) = (V,E,tau),

where V contains informational items, E contains determination/dependency relations, and tau types those relations.

Constraint closure operates over the graph, not merely over a bag of propositions.

This may be the decisive refinement required by Fine's objection.

## 12. Candidate Constitutive Information Principle

**CIP-1**

For any determinately represented x, there exists a typed constitutive-information graph G_c(x) containing the non-accidental identity, definitional, structural, and constitutive-dependency information that fixes what x is.

**CIP-2**

No modal predicate is permitted as a primitive edge type in G_c(x) for purposes of deriving metaphysical actualizability.

**CIP-3**

If contradiction appears in closure over G_c(x), x is not actualizable.

Formally:

bottom in Cl_L(G_c(x)) => not D(x).

**CIP-4, conjectural**

If no contradiction appears in closure over G_c(x), x is actualizable.

bottom not-in Cl_L(G_c(x)) ?=> D(x).

CIP-4 is the remaining CCAC-2 sufficiency burden.

## 13. Result

The non-modal formulation is viable at the level of a research schema.

The key move is:

essence-language -> typed constitutive determination -> informational dependency graph -> logical closure.

This does not yet prove that all essence facts reduce to information. It provides a precise place to test that hypothesis.

No fourth primitive has yet been required.

## 14. Falsifiers

The programme fails or requires revision if any of the following is established:

1. a constitutive fact about x cannot be represented informationally even in principle;
2. the distinction between constitutive and accidental information cannot be grounded without modal vocabulary;
3. a contradiction-free closed G_c(x) is independently shown metaphysically unactualizable;
4. a required constitutive relation cannot be typed as logic, information, or dependency without adding a genuinely new primitive.

## 15. Epistemic disposition

Typed determination schema: MEDIUM.

Hyperintensional graph requirement: MEDIUM-HIGH.

CIP-3: MEDIUM-HIGH within TRT/DAT.

CIP-4: UNCERTAIN.

Reduction of Finean essence to constitutive information: UNCERTAIN.

No-smuggling status: PASS provisionally.

## 16. Next target

Build a small formal test suite of hard cases against G_c:

- Socrates / singleton Socrates;
- water / H2O;
- origin essentialism;
- kind essentialism;
- mathematical objects;
- artifact identity;
- personal identity;
- libertarian choice counterfactuals.

For each case, require explicit provenance-tagged edges and reject any edge whose only warrant is modal language.
