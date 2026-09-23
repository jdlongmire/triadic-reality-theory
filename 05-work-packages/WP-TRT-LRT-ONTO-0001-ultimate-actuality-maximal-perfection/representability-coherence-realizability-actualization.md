# Representability, Coherence, Conditional Realizability, and Actualization

**WP:** WP-TRT-LRT-ONTO-0001  
**Date:** 2026-09-23  
**Status:** working formalization v0.1  
**Type:** modal/category refinement; research artifact

## Purpose

Refine the existing TRT/LRT modal backbone by distinguishing four questions that must not be collapsed:

1. Is a content representable?
2. Is that content internally coherent?
3. Is that coherent content realizable under a specified condition set?
4. Is that realizable content actualized?

This artifact extends, but does not supersede, `trt-modal-semantics.md` and the Absolute Nothingness Non-Actualizability Lemma. It preserves the existing hard-core distinction:

[
R \nRightarrow D \nRightarrow X
]

while making explicit that conditional compatibility is indexed to a condition set and therefore cannot be modeled as a simple untyped subset chain.

## 1. Definitions

Let:

[
G := \text{God}
]

[
L := \text{logical order}
]

[
I_{\mathrm{rep}}(x) := \text{informational representation of }x
]

[
Y := \{y_1,\ldots,y_n\}
]

where (Y) is a specified condition set.

Let:

[
\operatorname{Rep}(x)
]

mean that (x) is informationally representable.

Let:

[
\operatorname{Coh}(x)
]

mean that the content represented by (x) is internally non-contradictory under (L).

Let:

[
\operatorname{Compat}(x,Y)
]

mean that (x) is jointly coherent with the specified condition set (Y).

Let:

[
\operatorname{Real}(x\mid Y)
]

mean that (x) is conditionally realizable given (Y).

Let:

[
X(x)
]

mean that (x) is actualized.

Let:

[
\mathcal A_G
]

denote divine actualizing action where the theological bridge is explicitly in scope.

## 2. Grounding claim

Within the theological extension under investigation, representable information is not an autonomous Platonic domain. God is proposed as the ultimate source or ground of representable information and logical order.

The dependency claim is ontological rather than temporal:

[
G \to \{L,I_{\mathrm{rep}}\}.
]

This must not be read as:

- logic existing prior to God;
- God arbitrarily inventing logic;
- an informational substrate existing independently of God.

The stronger identification of (L) and (I_{\mathrm{rep}}) with divine attributes remains a separate proof obligation. This artifact does not promote that identification to the TRT/LRT hard core.

## 3. Representability

Representability is the weakest category.

[
\operatorname{Rep}(x)
]

asserts that sufficiently determinate informational content exists to identify what is being proposed.

It does not establish coherence:

[
\boxed{\operatorname{Rep}(x)\nRightarrow\operatorname{Coh}(x)}.
]

Example: the content "four-sided Euclidean triangle" is representable as a proposed conjunction even though its constitutive predicates cannot be jointly satisfied.

Thus semantic or informational determination must not be smuggled into metaphysical possibility.

## 4. Coherence

Define:

[
\operatorname{Coh}(x) \iff \neg(x\vdash_L\bot).
]

Coherence is intrinsic to the represented content under the governing logical constraints.

Where coherence is assessable, representation is presupposed:

[
\operatorname{Coh}(x)\to\operatorname{Rep}(x).
]

The reverse does not hold.

This refines the current TRT modal semantics without yet proving the stronger biconditional:

[
\Diamond x \iff \operatorname{Coh}(x).
]

No such equivalence is claimed here.

## 5. Conditional compatibility and realizability

Conditional realizability is relational rather than intrinsic.

A coherent (x) may fail to be compatible with a particular condition set (Y):

[
\operatorname{Coh}(x)\nRightarrow\operatorname{Compat}(x,Y).
]

Compatibility requires:

[
\operatorname{Coh}(x\land Y).
]

Candidate definition:

[
\operatorname{Compat}(x,Y)
\iff
\operatorname{Coh}(x\land Y).
]

Conditional realizability then requires at minimum compatibility:

[
\operatorname{Real}(x\mid Y)
\to
\operatorname{Compat}(x,Y).
]

Whether compatibility is sufficient for metaphysical realizability remains OPEN:

[
\operatorname{Compat}(x,Y)
\stackrel{?}{\to}
\operatorname{Real}(x\mid Y).
]

This is the same sufficiency burden already identified in the existing TRT modal semantics: logical admissibility is clearly necessary for actualizability, but its sufficiency for metaphysical possibility has not been demonstrated.

## 6. Typed correction to the four-level hierarchy

The provisional subset expression

[
\text{Actuality}\subseteq\text{Conditional Realizability}\subseteq\text{Coherence}\subseteq\text{Representability}
]

is rejected as formally imprecise.

The predicates are differently typed:

[
\operatorname{Rep}:\mathcal I\to\{0,1\},
]

[
\operatorname{Coh}:\mathcal I\to\{0,1\},
]

[
\operatorname{Compat}:\mathcal I\times\mathcal Y\to\{0,1\},
]

[
\operatorname{Real}:\mathcal I\times\mathcal Y\to\{0,1\},
]

[
X:\mathcal I\to\{0,1\}.
]

The defensible dependency structure is therefore:

[
X(x)
\to
\operatorname{Real}(x\mid Y_{\mathrm{actual}})
\to
\operatorname{Compat}(x,Y_{\mathrm{actual}})
\to
\operatorname{Coh}(x)
\to
\operatorname{Rep}(x),
]

where (Y_{\mathrm{actual}}) denotes the relevant actual condition set.

The reverse implications are denied in general.

In particular:

[
\operatorname{Rep}(x)\nRightarrow\operatorname{Coh}(x),
]

[
\operatorname{Coh}(x)\nRightarrow\operatorname{Compat}(x,Y),
]

[
\operatorname{Compat}(x,Y)\nRightarrow\operatorname{Real}(x\mid Y)
]

until sufficiency is proven, and

[
\operatorname{Real}(x\mid Y)\nRightarrow X(x).
]

## 7. Counterfactual representation

A counterfactual can be represented as:

[
Y \Box\!\to x.
]

The present framework does not assume that every representable counterfactual has a true consequent relation.

God can know:

- the representation of (x);
- the representation of (Y);
- every logical relation between (x) and (Y);
- whether (x\land Y) is coherent;
- whether (x) is realizable given (Y);
- whether (x) is actual.

Therefore divine knowledge of the represented IF does not entail actuality:

[
K_G[\operatorname{Rep}(x,Y)]\nRightarrow X(x).
]

Nor does representation entail compatibility:

[
K_G[\operatorname{Rep}(x,Y)]\nRightarrow\operatorname{Compat}(x,Y).
]

God may know exactly what a counterfactual proposes while also knowing that its antecedent-condition set logically excludes its consequent.

Thus:

[
\boxed{\text{representation of an IF}\neq\text{possibility of an IS}}.
]

## 8. IF, WOULD, and IS

Three categories must be distinguished.

**IF:** represented conditional content.

**WOULD:** a determinate counterfactual relation asserting what obtains under the antecedent.

**IS:** actualized reality.

The framework requires knowledge of the IF and of its logical status. It does not automatically supply a determinate creaturely WOULD.

Therefore:

[
\boxed{\text{Representable IF}\neq\text{determinate creaturely WOULD}}.
]

This is the principal boundary between the present account and Molinist middle knowledge.

Molinism requires an additional thesis concerning true counterfactuals of libertarian creaturely freedom prior to the divine creative decree. This artifact does not adopt that thesis.

## 9. Actualization

Within the theological extension, divine knowledge of representable content does not itself constitute creation.

Actuality requires actualizing action:

[
\mathcal A_G(I_x\mid L)\Rightarrow X(x).
]

Accordingly:

[
I_{\mathrm{rep}}(x)\nRightarrow X(x).
]

This preserves the LRT/TRT action primitive as the discriminator between admissible informational content and actuality.

The formulation:

[
\text{IF}\xrightarrow{\mathcal A_G}\text{IS}
]

is therefore permitted only when the represented state is realizable and God actualizes it. It must not imply that every represented IF is an available object awaiting selection.

## 10. Creatio ex nihilo

The framework supports the following theological formulation:

> God actualizes created reality without dependence upon antecedent created being.

Absolute nothingness supplies no:

- information;
- logical order;
- causal capacity;
- disposition;
- action;
- substrate.

Therefore:

[
\varnothing\nrightarrow R.
]

Within the proposed theological bridge:

[
G:I_R\xrightarrow{\mathcal A_G}R.
]

"Nothing became something" is rejected as an ontologically misleading formulation. Nothingness is not a source term.

## 11. Absolute nothingness

This artifact preserves ANNAL:

[
R(N)\land\neg D(N)\land\neg X(N).
]

The represented content "absolute nothingness" is informationally accessible, while its intended content cannot be actualized as a determinate state without contradiction.

No null-world object, zero-state object, or boundary-condition object may be introduced as a substitute for absolute nothingness.

Thus:

[
\operatorname{Rep}(N)\nRightarrow\operatorname{Exists}(N).
]

## 12. No-smuggling / no-free-lunch controls

The following substitutions are prohibited without independent proof:

- representable = coherent;
- coherent = metaphysically possible;
- coherent-with-(Y) = metaphysically realizable under (Y);
- realizable = actual;
- represented counterfactual = true counterfactual;
- IF = WOULD;
- divine knowledge = divine decree;
- divine knowledge = actualization;
- informational content = independently existing Platonic object;
- logical constraint = external constraint upon God;
- semantic description of nothingness = ontological nothingness object.

No ontological status may be inferred merely from representation:

[
\boxed{\operatorname{Rep}(x)\nRightarrow\operatorname{Exists}(x)}.
]

No modal status may be inferred merely from representation:

[
\boxed{\operatorname{Rep}(x)\nRightarrow\Diamond x}.
]

## 13. Current disposition

**Established or inherited within the current TRT/LRT framework:**

- representability and actualizability are distinct;
- contradiction-encoding content may be representable;
- actuality does not follow from admissibility;
- action remains required for actuality under TRT;
- absolute nothingness is representable as content but non-actualizable.

**Refinement introduced here:**

- coherence is explicitly separated from bare representability;
- compatibility is explicitly indexed to a condition set (Y);
- conditional realizability is typed as a relation rather than an intrinsic property;
- the earlier simple subset hierarchy is rejected;
- IF, WOULD, and IS are explicitly distinguished.

**Open proof obligations:**

1. Is (L_3)-admissibility equivalent to coherence as defined here?
2. Is coherence sufficient for unrestricted metaphysical possibility?
3. Is compatibility with (Y) sufficient for conditional realizability?
4. What additional resources, if any, distinguish realizability from logical compatibility?
5. Can the divine grounding of representable information be derived from the pure TRT/LRT track, or does it belong to the theological convergence track?
6. What account of counterfactual truth is required without importing Molinist middle knowledge?
7. How should divine knowledge of counterfactuals be stated without importing libertarian WOULD claims?

## 14. Preliminary thesis

> God is proposed as the ultimate ground of logical order and representable information. Divine knowledge comprehends every representable state and every logical relation among represented states, including counterfactual representations. Representability does not entail coherence; coherence does not entail compatibility with an arbitrary condition set; compatibility does not yet entail metaphysical realizability without further proof; and realizability does not entail actuality. Actuality requires act. Therefore God may know the complete representation of an IF, including whether its conditions permit or exclude its consequent, without the represented state becoming an IS and without committing the framework to Molinist middle knowledge.

Compactly:

[
\boxed{
\operatorname{Rep}(x)
\nRightarrow
\operatorname{Coh}(x)
\nRightarrow
\operatorname{Compat}(x,Y)
\nRightarrow
\operatorname{Real}(x\mid Y)
\nRightarrow
X(x)
}
]

with the caution that each non-entailment has a distinct type and proof burden.

## 15. Promotion rule

This artifact is exploratory within WP-TRT-LRT-ONTO-0001.

No change to the TRT/LRT hard core is authorized until:

- the typed predicates are reconciled with canonical (R/D/X);
- the (L_3)-admissibility/coherence relation is proved or explicitly bounded;
- conditional realizability is defined without modal circularity;
- the counterfactual semantics are red-teamed against Molinist, Thomist, Reformed, modal-realist, and nominalist alternatives;
- the no-smuggling/no-free-lunch audit passes.


## 16. Reconciliation with canonical R/D/X

The canonical TRT backbone remains:

[
R \xrightarrow{L_3} D \xrightarrow{A} X.
]

The refined predicates map onto that backbone as follows.

### R: representable domain

[
x\in R \iff \operatorname{Rep}(x).
]

This is the cleanest correspondence and is adopted provisionally.

### D: admissible / actualizable domain

The earlier shorthand

[
x\in D \iff x\text{ survives }L_3
]

must be decomposed.

Define logical admissibility:

[
\operatorname{Adm}_{L_3}(x)
:=
\operatorname{Rep}(x)\land\operatorname{Coh}_{L_3}(x).
]

Then:

[
x\in D \to \operatorname{Adm}_{L_3}(x).
]

The converse remains unproved:

[
\operatorname{Adm}_{L_3}(x)\stackrel{?}{\to}x\in D.
]

Accordingly, (D) must not yet be identified simpliciter with bare coherence.

A safer provisional reading is:

[
D := \{x\in R\mid \operatorname{Adm}_{L_3}(x)\land M(x)\},
]

where (M(x)) denotes any additional metaphysical admissibility condition required beyond logical coherence.

At present:

[
M(x)=\top
]

is a hypothesis, not a theorem.

This exposes the exact open burden rather than concealing it in the word "actualizable."

### X: actualized domain

[
x\in X \to x\in D.
]

Under TRT:

[
A:D\to X.
]

For the actual condition set (Y_a):

[
x\in X
\to
\operatorname{Real}(x\mid Y_a)
\to
\operatorname{Compat}(x,Y_a).
]

The reverse implications do not hold merely from category membership.

## 17. L3/coherence result

The present analysis supports the following bounded result:

[
\boxed{
\operatorname{Coh}_{L_3}(x)
\iff
x\text{ contains no contradiction detectable under the current }L_3\text{ constraints}
}
]

This is a logical result only.

It does not establish:

[
\operatorname{Coh}_{L_3}(x)
\iff
\Diamond x.
]

Nor does it establish:

[
\operatorname{Coh}_{L_3}(x)
\iff
x\in D.
]

Therefore the canonical phrase "L3 filters representable structure into admissible/actualizable structure" should be read operationally as a necessary filtering stage, not as a completed proof that (L_3) alone exhausts metaphysical actualizability.

### Disposition

**HIGH:** (x\in D\to\operatorname{Coh}_{L_3}(x)).

**MEDIUM:** (x\in R\iff\operatorname{Rep}(x)), subject to final vocabulary normalization.

**UNCERTAIN:** (operatorname{Coh}_{L_3}(x)\to x\in D).

**UNCERTAIN:** (x\in D\iff\Diamond x).

This resolves the immediate reconciliation without strengthening the hard core.

## 18. Conditional realizability without circularity

To avoid defining realizability by the modal operator it is intended to explain, introduce a structural relation first.

Let:

[
\operatorname{JointAdm}(x,Y)
:=
\operatorname{Adm}_{L_3}(x\land Y)\land M(x\land Y).
]

Then define conditional realizability provisionally as:

[
\operatorname{Real}(x\mid Y)
:=
\operatorname{JointAdm}(x,Y).
]

This is acceptable only if (M) can be specified independently of (Diamond).

If (M) is defined as "metaphysically possible," the definition becomes circular and must be rejected.

The research target is therefore:

> Identify whether any constraints beyond (L_3) are required for actualizability, and if so state them extensionally or structurally without invoking the modal notion being analyzed.

Until that is done, (operatorname{Real}) remains a typed research predicate rather than a canonical primitive.

## 19. Counterfactual truth boundary

The framework now distinguishes four propositions:

[
\operatorname{Rep}(Y\Box\!\to x)
]

the counterfactual is representable;

[
\operatorname{Coh}(Y\land x)
]

antecedent and consequent are jointly coherent;

[
\operatorname{Real}(x\mid Y)
]

the consequent is realizable under the antecedent conditions;

[
\operatorname{TrueCF}(Y\Box\!\to x)
]

the counterfactual itself is true.

No equivalence among these is assumed.

In particular:

[
\operatorname{Real}(x\mid Y)
\nRightarrow
\operatorname{TrueCF}(Y\Box\!\to x).
]

Realizability says that (x) can obtain under (Y). A true counterfactual of the form "if (Y), then (x) would obtain" says substantially more.

This is the point at which Molinist middle knowledge would require an additional grounding account for creaturely WOULD claims.

The current framework stops before that move.

## 20. Revised canonical candidate

The strongest formulation presently licensed is:

[
\boxed{
R
\xrightarrow{L_3\text{ necessary filter}}
D
\xrightarrow{A}
X
}
]

with:

[
x\in R\iff\operatorname{Rep}(x),
]

[
x\in D\to\operatorname{Coh}_{L_3}(x),
]

[
x\in X\to x\in D,
]

and:

[
\operatorname{Coh}_{L_3}(x)
\nRightarrow
x\in D
]

until the metaphysical sufficiency burden is discharged.

For conditional analysis:

[
X(x)
\to
\operatorname{Real}(x\mid Y_a)
\to
\operatorname{Compat}(x,Y_a)
\to
\operatorname{Coh}(x)
\to
\operatorname{Rep}(x).
]

For counterfactual analysis:

[
\boxed{
\text{IF}
\neq
\text{CAN}
\neq
\text{WOULD}
\neq
\text{IS}
}
]

where:

- **IF** = representable conditional;
- **CAN** = conditionally realizable;
- **WOULD** = true determinate counterfactual relation;
- **IS** = actualized state.

This four-way distinction is recommended for subsequent red-team work.
