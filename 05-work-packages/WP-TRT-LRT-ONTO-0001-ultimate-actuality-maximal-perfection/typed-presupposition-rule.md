# Typed Presupposition Rule (TPR)

**WP:** WP-TRT-LRT-ONTO-0001
**Date:** 2026-09-19
**Status:** canonical methodological rule v0.1

## Purpose

Prevent category errors between:
- transcendental/ontic presuppositions;
- hypotheses within an already well-posed domain;
- derived results;
- bridge hypotheses concerning the ultimate ground.

The distinction is type-theoretic, not a difference in confidence.

## 1. Presupposition versus hypothesis

### Ontic/transcendental presupposition

Y is ontically presupposed by X when no determinate X is possible unless Y obtains as a constitutive condition.

[
Presupposes_{ont}(X,Y)
]

means:

> no determinate X unless Y.

If Y is withdrawn, the attempted withdrawal cannot remain a determinate instance of the same subject matter without using Y.

A presupposition is therefore not merely a claim awaiting ordinary empirical evidence inside the domain it constitutes.

### Hypothesis

A hypothesis phi is proposed within an already well-posed space.

[
Hypothesizes(T,arphi)
]

means T proposes phi as holdable-or-not within the constitutive domain.

If phi fails, the domain remains available for stating, testing, and explaining the failure.

A hypothesis can be false without making the act of stating its falsity ill-posed.

## 2. Withdrawal diagnostic

**Hypothesis diagnostic:**

If withdrawing phi leaves one able to determinately state that phi has been withdrawn, phi is hypothesis-eligible.

[
Withdraw(arphi)
land
CanDeterminatelyAssert[Withdraw(arphi)]
Rightarrow
HypothesisEligible(arphi).
]

**Presupposition diagnostic:**

If withdrawing Y removes the constitutive conditions required to state a determinate withdrawal of Y, Y is functioning as a transcendental presupposition.

[
Withdraw(Y)
ightarrow

eg CanDeterminatelyAssert_Y[Withdraw(Y)].
]

The subscript indicates that the determinate assertion cannot be made while genuinely withholding the constitutive role under test.

## 3. TRT type system

### Type P: Transcendental Presupposition

[
mathbf P
]

Current TRT hard-core roles:

[
mathcal L,mathcal I,mathcal A:mathbf P
]

relative to determinate actuality D.

Canonical claim:

[
Dightarrow(mathcal Llandmathcal Ilandmathcal A).
]

This is transcendental/constitutive, not an empirical physical conjecture.

### Type D: Derived Result

[
mathbf D
]

Examples:
- CPIT pair-failure result;
- CPN;
- minimal selection/differentiation S0, where properly derived;
- anti-circularity consequences such as LEE/DEE/AEE under their premises.

Derived results inherit their warrant from the typed premises and proof.

### Type H: Intra-domain Hypothesis

[
mathbf H
]

Examples:
- physical laws/models;
- specific Hamiltonian governing a device;
- detector outcome claims;
- decoherence sufficiency claims;
- TRM physics-facing proposals;
- gravity-as-global-co-admissibility;
- empirical FLL hypotheses.

These operate within D and may be falsified, revised, assigned confidence, or removed without withdrawing the constitutive domain.

### Type B: Ground/Bridge Hypothesis

[
mathbf B
]

Examples when proposed as ultimate grounds:
- OSR/primitive structural ground;
- Platonism/abstracta;
- powers ontology;
- nonmental necessary ground;
- Infinite Transcendent Mind.

Bridge hypotheses do not constitute D merely by being proposed. They attempt to account for why the Type-P package obtains/unifies.

Thus:

[
Ground(M_infty^T,mathcal G):mathbf B
]

not:

[
M_infty^T:mathbf P.
]

This firewall is mandatory.

## 4. Typed evaluation rules

### Type P evaluation
Use:
- transcendental analysis;
- elenctic/self-defeat testing;
- constitutive dependence;
- pair-failure/irreducibility;
- formal scope review.

Do not treat P as an ordinary empirical belt hypothesis.

### Type H evaluation
Use:
- falsification;
- severe empirical tests;
- model comparison;
- measurement;
- confidence labels;
- revision/abandonment.

### Type B evaluation
Use:
- Functional Adequacy Argument;
- Anti-Smuggling Rule;
- explanatory-cost ledger;
- non-circularity;
- co-unity burden;
- rival-ground comparison;
- convergence.

### Type D evaluation
Use:
- proof validity;
- dependency traceability;
- premise-type integrity;
- scope control.

## 5. Typed Anti-Smuggling Rule

The Anti-Smuggling Rule applies to an ultimate-ground move, not to every hypothesis that uses constitutive conditions.

**TASR:**

If X ontically presupposes Y in order to be a determinate X, then X cannot be promoted without further non-circular argument to the ontologically prior ultimate ground of Y.

[
Presupposes_{ont}(X,Y)
land
ProposedUltimateGround(X,Y)
ightarrow
GroundingCircularity(X,Y)
]

unless an independent level distinction breaks the dependency.

This does not invalidate ordinary intra-domain explanations.

A Hamiltonian may presuppose logic/information/actuality and still explain physical evolution within D.

It becomes type-invalid only if the Hamiltonian, or physicality as such, is promoted to the ultimate ground of the constitutive conditions it already requires.

## 6. Example: classical logic

The claim:

"Perhaps L3 fails at the level of determinate actuality"

is not automatically an ordinary Type-H hypothesis inside TRT.

To state a determinate failure one must identify:
- what failed;
- what it is contrasted with;
- in what respect;
- whether the failure obtains.

Those operations invoke the determinacy roles under test.

By contrast:

"This specified formal/experimental context exhibits a valuation gap under protocol Q"

can be a Type-H claim. It is a determinate claim inside the constitutive domain and may be tested without withdrawing determinate actuality itself.

Thus nonclassical formalisms/empirical protocols are not banned; their claims must be typed correctly.

## 7. Example: Mind

Mind must not cross the type boundary.

Wrong:

[
Dightarrow M_infty^T
]

merely because D presupposes L/I/A.

Correct programme:

[
Dightarrowmathcal G
]

then:

[
Ground(M_infty^T,mathcal G):mathbf B
]

and compare M against rival Type-B grounds under FAA/TASR/CUB.

Mind may eventually be established by a successful bridge argument. It is not a presupposition of D merely by being the preferred candidate ground.

## 8. Confidence-label rule

Confidence labels attach naturally to:
- Type H claims;
- Type B comparative conclusions;
- formalization maturity;
- historical/source claims;
- empirical conjectures.

They must not imply that a Type-P role is merely a probabilistic belt hypothesis.

Therefore replace formulations such as:

"DAT is MEDIUM-HIGH, perhaps actuality is not logically determinate"

with typed formulations such as:

- **Ontological status in TRT:** Type P / hard-core constitutive role.
- **Formalization maturity:** under adversarial review.
- **Scope maturity:** exact-condition/LEM treatment under review.

The review concerns our articulation and proof scope, not whether the hard core is casually parked in the protective belt.

## 9. Lakatosian architecture

TRT research programme:

### Hard core
Type P:
[
mathcal L,mathcal I,mathcal A
]

plus the canonical R/D/X distinctions and irreducibility claims once formally admitted to the hard core.

### Protective belt
Type H:
physics-facing mechanisms, TRM models, FLL tests, cosmological/quantum applications, and other revisable empirical conjectures.

### Bridge programme
Type B:
candidate metaphysical grounds of the hard core, including H_S and H_MinfT.

### Derived theorem layer
Type D:
results formally obtained from P/H/B premises with explicit provenance.

No layer may silently trade places with another.

## 10. Fundamental distinction

A hypothesis is content inside a well-posed space.

A presupposition is a constitutive condition of the space being well-posed.

A bridge hypothesis is a proposed explanation of why the presupposed package has the ground/unity it does.

A derived result is what follows from typed premises.

This four-way distinction is canonical for the WP.
