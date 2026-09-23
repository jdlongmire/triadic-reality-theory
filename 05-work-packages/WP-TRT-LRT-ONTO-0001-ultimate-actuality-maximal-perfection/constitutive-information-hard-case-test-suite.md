# Constitutive Information Graph Hard-Case Test Suite

**WP:** WP-TRT-LRT-ONTO-0001
**Date:** 2026-09-23
**Status:** adversarial test suite v0.1
**Target:** G_c(x), CIP-1..4, CCAC-2

## Method

Each case is tested using provenance-tagged constitutive edges only:

- ID: identity/reference fixing
- DEF: definitional determination
- STR: structural determination
- DEP: constitutive dependency
- TYPE: kind/type determination
- EMP: empirically discovered constitutive information
- MODAL: modal premise

A case passes the no-smuggling test only if the relevant exclusion or admissibility result can be generated without a load-bearing MODAL edge.

## Case 1: Socrates / singleton Socrates

Fine's challenge: necessarily, if Socrates and singleton {Socrates} exist, Socrates belongs to the singleton. Yet membership in that set is not thereby part of what Socrates is.

Model:

G_c(Socrates):
- ID: Socrates = s
- TYPE: s is a person/human, subject to independent ontology of personhood
- no edge from s's constitutive identity to singleton membership

G_c({s}):
- DEF: singleton {s} has exactly s as member
- DEP: existence/identity of {s} depends on s under the adopted set theory

Result:

membership(s,{s}) belongs to the constitutive graph of the singleton relation, not to G_c(s) as a constitutive fact about Socrates.

PASS.

This shows why provenance and direction matter. Necessary co-truth is insufficient for constitutive membership.

## Case 2: Socrates / Eiffel Tower distinctness

The distinctness relation follows from ID facts for two independently fixed referents.

It need not be placed in G_c(Socrates) as part of what Socrates is.

Result:

Finean irrelevance is preserved.

PASS.

## Case 3: Water / H2O

Under the Kripke-Putnam framework, empirical investigation fixes that the natural-kind referent water has H2O microstructure.

Model:

- ID: "water" rigidly fixes natural-kind referent W, if rigid designation is accepted
- EMP/TYPE: W has microstructural constitution H2O
- ID/STR: H2O fixes molecular structure

Then "W is non-H2O" conflicts under closure once the empirically established identity/constitution is entered.

No MODAL edge is needed to generate the contradiction after identity is fixed.

PASS CONDITIONALLY.

Burden: TRT/LRT must distinguish empirical discovery of constitutive information from the ontological status of that information.

## Case 4: Origin essentialism

Kripkean origin essentialism claims, roughly, that this individual could not have originated from wholly different parents/material.

Attempted non-modal graph:

- ID: individual x fixed by actual referential chain
- DEP?: x's numerical identity is constitutively dependent on originating process O

Problem:

The DEP edge is exactly what is contested. It cannot be justified merely by saying x necessarily has O.

Result:

OPEN / FAILS CURRENTLY.

Origin essentialism is the first hard case where the constitutive edge itself lacks a non-modal derivation in the current framework.

This is not yet a counterexample to CCAC-2. It is a proof obligation concerning whether origin participates in identity determination.

## Case 5: Kind essentialism

Claim: x is of kind K as a constitutive feature.

If TYPE(x,K) is independently grounded by real definition, structure, genealogy, or natural-kind constitution, closure can operate without MODAL.

If TYPE is justified only by "x must be K," the edge is circular.

Result:

PASS CONDITIONALLY; ontology of kinds remains external burden.

## Case 6: Mathematical objects

For a triangle T:

- DEF: Euclidean triangle
- STR: exactly three straight sides
- STR: angle/point/line relations from the adopted geometry

"T has four sides" closes to contradiction.

For abstract mathematical objects more generally, the graph can encode axiomatic/structural identity conditions.

Problem cases arise where multiple non-equivalent foundations characterize "the same" mathematical object.

Result:

PASS for ordinary defined structures; OPEN for foundational identity questions.

## Case 7: Artifact identity

Consider Theseus's ship or a table.

Candidate graph may include:
- ID: referential history
- STR: organization
- DEP: material/history relation
- TYPE: artifact function

There is no consensus non-modal rule determining which of these fixes numerical identity through replacement.

Result:

OPEN.

This is an underdetermination of the constitutive graph, not evidence that a completed contradiction-free graph is unactualizable.

## Case 8: Personal identity

Candidate criteria include organism continuity, psychological continuity, soul/substance identity, or other accounts.

The framework cannot choose among them by stipulation.

Once an identity theory is supplied, G_c can represent its constitutive relations. But the truth of that theory is an upstream metaphysical question.

Result:

OPEN EXTERNAL ONTOLOGY.

No MODAL edge should be used to settle it.

## Case 9: Libertarian choice counterfactual

Let C be a creature, Y circumstances, and actions a and b.

Suppose:

bottom not-in Cl_L(G_c(C) union Spec(Y) union {a})

and

bottom not-in Cl_L(G_c(C) union Spec(Y) union {b}).

Then both are CAN states under Y.

Nothing in closure yields:

Y WOULD-> a

or

Y WOULD-> b.

Result:

PASS.

This strongly confirms the IF/CAN/WOULD/IS distinction and prevents CCAC from silently becoming Molinist middle knowledge.

## Case 10: God and lying

Within a theological graph, if truthful/holy nature is independently established as constitutive of God:

- TYPE/ID: G is God
- DEP/DEF: truthfulness belongs to divine nature
- proposed state: G lies

Closure yields contradiction.

If truthfulness is inserted only because "God cannot lie," the argument is modal and circular.

Result:

PASS CONDITIONALLY on independent theological grounding.

## Summary matrix

1. Socrates/singleton: PASS
2. Socrates/Eiffel Tower: PASS
3. Water/H2O: PASS CONDITIONALLY
4. Origin essentialism: OPEN, strongest pressure case
5. Kind essentialism: PASS CONDITIONALLY
6. Mathematical objects: PASS/OPEN at foundations
7. Artifact identity: OPEN
8. Personal identity: OPEN external ontology
9. Libertarian choice: PASS
10. Divine essential attribute case: PASS CONDITIONALLY

## Main finding

No case yet establishes:

Coh_c(x) AND not D(x)

for a completed, independently warranted constitutive graph.

The hard cases instead expose a prior question:

Which relations genuinely belong in G_c(x)?

That is an identity/constitution problem.

Therefore CCAC-2 has not been falsified, but its success now depends on a **Constitutive Edge Warrant Rule**.

## Candidate Constitutive Edge Warrant Rule (CEWR)

An edge e may enter G_c(x) only when there is a non-modal warrant that e participates in fixing the identity, type, structure, real definition, or constitutive dependency of x.

Prohibited warrant:

"e is constitutive because x could not exist/be x without e."

Permitted candidate warrants:

- explicit real definition;
- identity/reference establishment;
- empirical discovery of constitutive structure;
- generative/origin dependency, if independently shown identity-fixing;
- formal structural definition;
- explanatory determination of type/kind.

CEWR itself remains a research rule.

## Next burden

Origin essentialism is the best next stress test because it directly asks whether historical/generative dependence can be constitutive of numerical identity without appealing to modal intuition.

If that relation can be characterized informationally and non-modally, the graph model gains significant strength. If it cannot, origin may expose a genuinely modal primitive or an independent identity primitive that LRT must account for.
