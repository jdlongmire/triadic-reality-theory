# Content-Role Preservation Audit

**WP:** WP-TRT-LRT-ONTO-0001
**Date:** 2026-09-23
**Status:** bounded formal audit v0.1
**Target:** define expressive actuality E without presupposing Mind
**Controls:** TASR, ADF, ESR, no-smuggling

## 1. Burden

The expressive-actuality track requires a distinction between:

X(c): some state/token associated with c occurs;

and:

E(c): c is actual as content.

If E is defined by "a mind means/understands c," the Source-Mind conclusion is circular.

The task is to determine whether content-role preservation can be specified in pre-mental terms.

## 2. Neutral representation

Let c be a content-specification in representational domain D.

Let CR(c) be the constitutive role-structure of c.

CR(c) may include:
- identity conditions;
- distinction from alternatives;
- inferential/consequence relations;
- truth-condition constraints where applicable;
- reference constraints where applicable;
- structural/dependency relations.

No subject is included by definition.

## 3. Token occurrence

Let Tok(t) mean an actual token/state t occurs.

Bare token occurrence does not establish expression:

Tok(t) -/-> E(c).

A mark, state, or event can occur without the relations constitutive of c being preserved.

## 4. Role realization

Define:

Realizes(t,CR(c))

iff t participates in an actual relational structure that instantiates the constitutive role-structure CR(c).

This is stronger than resemblance or external labeling.

Candidate:

E_0(c,t) := Tok(t) AND Realizes(t,CR(c)).

E_0 is **structural expressive actuality**.

It does not yet entail intrinsic semantics or intentionality.

## 5. External interpretation control

Suppose observer o assigns c to arbitrary token t.

AssignedBy(o,t,c)

does not imply:

Realizes(t,CR(c)).

Thus:

external interpretation alone -/-> E_0.

This prevents content from being created merely by observer labeling.

## 6. Truth-aptness

For propositional c, let TC(c) specify truth-condition structure.

If t realizes c as propositional content, its role must preserve the distinction between satisfaction and non-satisfaction of TC(c).

Candidate:

PropE_0(c,t)
->
Realizes(t,TC(c)).

This does not require that t "knows" whether c is true.

Truth-aptness is treated as structural eligibility for truth/falsity, not as a mental attitude.

## 7. Inferential role

If c has consequence relations:

c |- d,

then role preservation requires corresponding constraint relations in the realized content structure.

But inferential-role preservation alone is insufficient for full semantics because multiple interpretations may share formal inferential structure.

Therefore:

InferentialRole(c) is a component of CR(c), not the whole of content.

## 8. Reference constraint

Where c is about/referential, a stronger relation is required.

Let RefConstraint(c,o) mean that the constitutive specification of c constrains o as its target/referent.

The hard question is whether:

Realizes(t,RefConstraint(c,o))

can be defined without a subject or interpreter.

Pure covariance, causation, or mapping may underdetermine reference.

Therefore referential expressive actuality remains OPEN.

## 9. Two grades of E

The audit supports a typed distinction.

### E0: structural expressive actuality

E0(c,t) iff an actual token/state realizes the constitutive role-structure CR(c).

This can be defined without Mind.

### E1: intrinsic semantic expressive actuality

E1(c,t) iff E0 obtains and c has determinate intrinsic semantic/reference content not merely assigned by an external interpreter.

E1 -> E0.

But:

E0 -/-> E1.

The E1 bridge remains open.

## 10. Consequence for the Mind argument

The prior E category was too broad if it silently included full intrinsic semantics.

Use:

X -> generic actuality.

E0 -> structurally content-role-preserving actuality.

E1 -> intrinsically semantic expressive actuality.

Then:

X
contains E0
contains? E1

as typed specializations, with E1's existence/definition requiring further proof.

The Source-Mind argument is stronger if E1 is independently established.

It must not derive Mind from E0 by calling structural role realization "meaning."

## 11. Can E0 support sourcehood?

Yes, conditionally.

If E0 occurs, there is actual realization of a content-role structure. The act/source analysis can ask what grounds that realization.

But E0 alone may still be compatible with an impersonal structural actualizer.

Therefore:

E0 -> source burden

does not entail:

E0 -> Mind.

## 12. Can E1 support Mind?

Potentially.

Intrinsic semantic content raises:
- determinate reference;
- misrepresentation;
- truth/falsity;
- aspectual content;
- reasons-as-reasons.

These may generate subjecthood pressure.

But E1 cannot be defined as "content for a subject" and then used to prove a subject.

Neutral target:

IntrinsicSem(c,t) :=
c has determinate semantic/reference role in t that is not constituted merely by external interpretation.

Question:

IntrinsicSem(c,t) ?=> exists m Subject(m,c,t).

OPEN.

## 13. No-smuggling audit

No physical system is used as a first-principles premise.

No equation:
- token = content;
- correlation = information;
- inferential role = full semantics;
- reference = causal covariance;
- truth-aptness = knowledge;
- E0 = E1;
- E1 = Mind.

**Audit:** PASS.

## 14. Result

A non-circular content-role notion is available at the structural level.

Define:

E0(c,t) := Tok(t) AND Realizes(t,CR(c)).

This gives the expressive track a legitimate independent explanandum without presupposing Mind.

However, full semantic expression requires a second bridge:

E0 ?=> E1.

That bridge is not established.

Therefore revise the expressive-source architecture:

Generic:
X -> <L,I,A>.

Structural expressive:
E0 -> <D,L,I,A,U,SRC,...> as applicable.

Semantic expressive:
E1 -> E0 + IntrinsicSem.

Mind bridge:
E1 + unified source/reflexivity ?=> MindLike.

## 15. Bounded next target

Do not enumerate semantic examples.

Test one class-level question:

> Can intrinsic semantic reference be reduced to structural role plus constitutive informational relations without an interpreter?

This is the next load-bearing bridge.

If YES, E1 may remain pre-mental and Mind requires further work.

If NO, identify exactly what additional relation is required and whether that relation is subject-involving by definition or by independent argument.
