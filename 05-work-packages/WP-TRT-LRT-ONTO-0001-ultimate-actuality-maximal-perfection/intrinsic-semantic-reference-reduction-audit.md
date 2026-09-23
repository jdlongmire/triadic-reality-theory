# Intrinsic Semantic Reference Reduction Audit

**WP:** WP-TRT-LRT-ONTO-0001
**Date:** 2026-09-23
**Status:** bounded class-level audit v0.1
**Target:** E0 ->? E1 without interpreter
**Controls:** TASR, ADF, ESR, no-smuggling

## 1. Question

Can intrinsic semantic reference be reduced to structural role plus constitutive informational relations without an interpreter?

Let:

E0(c,t) := Tok(t) AND Realizes(t,CR(c)).

Let:

E1(c,t) := E0(c,t) AND IntrinsicSem(c,t).

The target is:

E0 + constitutive relations ?=> IntrinsicSem.

No physical implementation is permitted as a first-principles premise.

## 2. What must be explained

A successful reduction of intrinsic semantics must account for at least:

1. **Reference:** why c is about o rather than some alternative o'.
2. **Truth conditions:** what makes c eligible to be true or false of its target.
3. **Misrepresentation:** how c can retain its content when its target condition does not obtain.
4. **Content identity:** why c remains the same content across differing actual conditions.
5. **Non-derivativeness from interpreter assignment:** semantic status cannot be created merely by an external observer's labeling.

These are class-level constraints, not an invitation to enumerate examples.

## 3. Pure structural-role reduction

Candidate:

IntrinsicSem(c,t) := Realizes(t,CR(c)).

This collapses E1 into E0.

Problem:

Formal/structural role fixes relations among positions in a system but does not by itself determine which extra-structural object or state is the referent where multiple interpretations preserve the same structure.

Therefore:

StructuralRole(c) -/-> DeterminateReference(c,o)

without an additional reference-fixing relation.

**Disposition:** INSUFFICIENT for E1.

## 4. Causal/covariational reduction

Candidate:

c refers to o iff c stands in the appropriate causal/covariational relation to o.

At first-principles level this can be represented abstractly as a dependency relation without invoking physical causation.

Problem:

A dependency chain can relate c to:
- immediate source;
- distal source;
- class of sources;
- background condition;
- effect;
- correlated state.

The relation alone does not identify which node is the semantic target.

Misrepresentation also pressures simple covariance: c may retain content when o is absent.

**Disposition:** CONSTRAINS reference; does not yet determine semantics.

## 5. Functional/teleological reduction

Candidate:

c refers to o because c has the function of indicating/representing o.

This can explain misrepresentation if function is independently available.

But "function" must be defined without:
- purpose assigned by a mind;
- correctness already understood semantically;
- selected-for content imported from an already-actual physical process.

If function is merely a structural role, the account returns to section 3.

If function includes "supposed to represent," semantic normativity has been assumed.

**Disposition:** OPEN but currently risks circularity.

## 6. Inferential-role reduction

Candidate:

content is fixed by its inferential relations to other contents.

This can constrain conceptual role and truth-preserving relations.

But inferential-role is hyperintensionally and referentially underdetermined: distinct interpretations can preserve a formal network.

It also presupposes a domain of contents rather than explaining how content acquires extra-structural aboutness.

**Disposition:** INSUFFICIENT alone.

## 7. Primitive reference relation

Candidate:

Ref(c,o)

is an irreducible relation.

This secures determinate reference by stipulation if Ref is primitive.

But it introduces an additional primitive beyond thin L/I/A unless Ref can be grounded in I or another established role.

It also leaves open whether a subject is required.

**Disposition:** COHERENT RIVAL; explanatory cost added.

## 8. Constitutive informational reference

Candidate:

the informational identity of c intrinsically includes its target relation.

Spec_c(c) contains:

REF(c,o)

as constitutive information.

Then:

change the referent -> change the content.

This preserves content identity and determinate reference.

But a critical question remains:

What makes REF a semantic/aboutness relation rather than merely another ordered pair in the constitutive graph?

If the answer is "because REF means reference," the account is circular.

If REF is reduced to structural/dependency relations, underdetermination reappears.

**Disposition:** DOES NOT YET CLOSE THE GAP.

## 9. Semantic normativity

Misrepresentation exposes the strongest pressure.

For c to misrepresent o, c must preserve a standard of correctness while the represented condition fails.

Thus:

Content(c)
AND not Satisfies(o,c)
AND SameContent(c)

must be coherent.

A purely actual covariance relation tends to disappear or change when the correlated condition fails.

The content's correctness condition therefore appears to outrun current-state structural correlation.

This introduces a normative relation:

CorrectFor(c,o).

But:

CorrectFor != mere occurrence.

The source of this normativity remains open.

## 10. Subject hypothesis

A subject-based account proposes:

About_m(c,o)

where the same source/locus:
- contains c;
- distinguishes o;
- holds c under an aspect;
- preserves c's correctness condition;
- can express c whether c is satisfied or not.

This naturally unifies reference, truth-aptness, and misrepresentation.

However, this is model fit, not yet deduction.

The argument must not say:

"aboutness means being about something for a subject; therefore a subject exists."

Use the neutral semantic constraints first, then compare ontologies.

## 11. Strongest current result

No tested impersonal reduction derives determinate intrinsic reference from E0 alone without either:

1. leaving reference underdetermined;
2. importing semantic/normative vocabulary;
3. adding primitive Ref/CorrectFor relations;
4. appealing to function/purpose that itself requires grounding.

Therefore:

E0 -/-> E1

remains established as a non-entailment.

The stronger claim:

E1 -> Subject

is not yet deductively established.

## 12. Consilience update

The semantic constraint set is now:

K_sem := <Reference, TruthAptness, Misrepresentation, ContentIdentity, CorrectnessNorm>.

The Source-Mind hypothesis gains consilient pressure if one unified source can intrinsically satisfy:

K_E + K_sem

without adding independent semantic primitives.

The impersonal rival remains live but must specify how it grounds K_sem.

## 13. Primitive-semantic rival

A serious rival is:

H_PS: semantic/reference/normative relations are primitive impersonal facts.

This is coherent unless independently defeated.

Its explanatory cost is that it adds primitive semantic relations to the ground ontology.

The Source-Mind consilience cannot reject H_PS merely because it is primitive. It must compare unity and explanatory remainder.

## 14. No-smuggling audit

No physical system, brain, organism, computer, language user, or GenAI system is used as a premise.

No equation:
- covariance = reference;
- function = meaning;
- inference = aboutness;
- correctness = physical success;
- E0 = E1;
- E1 = Subject;
- Subject = person.

**Audit:** PASS.

## 15. Disposition

Pure structural role -> intrinsic semantics: FAILED.

Causal/dependency relation -> determinate reference: NOT ESTABLISHED.

Inferential role -> intrinsic semantics: INSUFFICIENT.

Functional/teleological reduction: OPEN / circularity risk.

Primitive Ref/semantic normativity: LIVE IMPERSONAL RIVAL with added primitive burden.

Constitutive informational reference without semantic primitive: NOT YET ESTABLISHED.

Subject-based source: STRONG CONSILIENT FIT, not theorem.

E1 -> Subject: OPEN.

## 16. Next bounded target

Do not continue enumerating semantic theories.

The next load-bearing question is:

> Does the unified-source ontology already derived for E0 provide a non-ad-hoc locus for K_sem such that semantic relations become intrinsic aspects of one source rather than additional primitives?

Formally:

G_E0 + K_sem
?=> SubjectLikeSource.

This is a consilience/unification test, not a new attempt to deduce Subject from one semantic property.

If the answer is positive, the programme can promote a minimal Subject-Mind hypothesis with its abductive status explicit. If negative, H_PS remains an equally live primitive-semantic rival.
