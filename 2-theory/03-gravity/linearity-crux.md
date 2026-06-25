# TRT Gravity: The Linearity Crux (Path B, continued)

**Working document. Refines Task 3.1 to a single decidable question.**

**Status:** Continuation of the D[χ] attempt. The previous document reduced the gravity derivation to the "Trace Principle" (does co-admissibility read the trace/volume or the full tensor/shape of relational holonomy). Working the discrete setting further shows that framing, while correct, sits on top of a sharper and more answerable question about the *power* to which holonomy enters the measure. This document states that sharper crux, gives the existence proof that the favorable answer is geometrically realizable, and presents an honest TRT-internal argument that bears on which answer obtains. Tags as before: EARNED, HEURISTIC, ASSUMED.

---

## 1. The Discrete Setting

To make "joint satisfiability around cycles" exact, drop to a discrete relational structure: states as nodes, relations as edges carrying a transformation (an element of some group *G*), exactly as in lattice gauge theory and Regge calculus. The holonomy around an elementary cycle (plaquette, or in 4D a hinge) is the ordered product of edge transformations. Flatness (perfect consistency) is holonomy equal to the identity. The *deficit*, the failure of the holonomy to be the identity, is the elementary unit of logical tension from the previous document's §2.3.

This is EARNED as a setup choice: it is the standard discrete encoding of "consistency of transport around loops," and it makes the holonomy exact rather than heuristic. What it does not settle by itself is the *group G* and the *functional form* of the tension measure, and those are where the physics lives.

---

## 2. The Existence Proof: Linear-in-Deficit Gives GR Exactly

The decisive fact, now verified against the Regge-calculus literature:

> **(EARNED, standard result.)** In a discrete (simplicial) structure, curvature concentrates on hinges (codimension-2 simplices) as a deficit angle. The action formed by summing, over hinges, the hinge volume times the deficit angle is *linear* in the deficit, and its continuum limit is exactly the Einstein-Hilbert action ∫√g (R − 2Λ), with R the Ricci scalar. Variation yields the Einstein field equations.

This is the existence proof the program needed. It establishes that a discrete holonomy-based consistency measure *can* yield exactly GR, with no higher-curvature corrections, provided the measure is **linear in the deficit (holonomy defect)**. Regge calculus is precisely this construction, and it is rigorous and standard.

So the favorable answer is not a fantasy. The question is whether TRT's co-admissibility measure is of the linear (Regge, → GR) type or the quadratic (relative-entropy, → modified gravity) type.

---

## 3. The Crux: Linear or Quadratic in Holonomy

This is the sharper replacement for the Trace Principle. The two outcomes:

**Linear in deficit → General Relativity.**
A measure linear in the holonomy defect gives the Einstein-Hilbert action. Note a clean supporting fact (EARNED): the *unique* scalar that is linear in the curvature tensor is the Ricci scalar R (up to a constant), because the antisymmetries of Riemann leave only one independent full contraction. So linearity *automatically* selects R, hence Einstein-Hilbert, hence (by Lovelock and covariance) the Einstein tensor. Linearity subsumes and explains the Trace Principle: a linear measure cannot help but read the double-trace. The trace question dissolves into the power question.

**Quadratic (or higher) in deficit → modified gravity.**
A measure quadratic in the holonomy, such as a relative-entropy or Fisher-information distance, produces curvature-squared terms (Riemann², Weyl², Gauss-Bonnet), i.e. higher-curvature modified gravity, reducing to GR only in a low-curvature limit. This is the Bianconi (2025) class, and it is no accident: relative entropy is intrinsically quadratic at leading order, since its second-order expansion is the Fisher metric. Any measure built as an information distance carries this quadratic structure and therefore gives modified gravity by default.

The crux, stated once:

> **Is the measure of global logical co-admissibility linear in the holonomy defect (a raw deficit), or quadratic (an information distance)?**

Linear gives GR. Quadratic gives modified gravity. This is sharper than the Trace Principle because it is a question about the *algebraic form* of the tension measure, and it has a candidate answer from the nature of logic itself.

---

## 4. The TRT-Internal Argument for Linearity

Here is a genuine argument, internal to TRT's commitments, that the measure should be linear. It is HEURISTIC, but it is substantive and it cuts in a definite direction, reversing the pessimism of the previous document.

Relative entropy is quadratic because it is a *metric distance* on a space of states: it equips the configuration space with a Fisher-Rao metric and measures squared-distance-like deviation. That quadratic structure is imposed by treating tension as a *geometric distance between distributions*.

Logical co-admissibility carries no such metric. *L₃* registers contradiction or its absence. The natural measure of the failure of joint satisfiability is the *amount of deficit*, the raw magnitude of the holonomy's departure from the identity, not the square of that magnitude. There is no logical operation that introduces a square. Squaring would require imposing a metric on the space of relational configurations, and *L₃* supplies no metric; it supplies only the binary registration of consistency and a magnitude of violation. A raw deficit is linear.

Put sharply: the quadratic structure of the entropic-gravity programs is inherited from the *information-geometric metric* they build in. TRT's logical tension has no information-geometric metric by default. It has a deficit. Deficits are linear. Therefore TRT, taken on its own terms, favors the linear measure, hence GR, not modified gravity.

**This reverses the previous document's pessimistic default.** There I noted that holonomy-based measures give full Riemann (modified gravity) by default. The refinement is: that pessimism came from implicitly assuming a quadratic (relative-entropy) measure. Once the measure's algebraic form is made the explicit question, TRT's own commitments point toward linearity, and linearity gives GR cleanly via Regge plus Lovelock.

---

## 5. Why This Is Not Yet a Derivation (the Honest Gaps)

The argument is genuinely encouraging but rests on three ASSUMED links, each now precisely stated.

**Gap 1: That logical tension is a raw deficit, not a metric distance (the linearity assumption).**
The §4 argument is plausible but not proven. One can imagine logical tension measures that combine deficits nonlinearly, for instance if multiple simultaneous contradictions compound super-additively, or if the "severity" of a contradiction is naturally squared. The claim "L₃ supplies no metric, only a deficit" is a reading of the nature of logical constraint, not a theorem. This is the new crux and the prime remaining debt. It is, however, a *philosophically tractable* question about the nature of logical violation, not an open-ended physics problem.

**Gap 2: That the relational holonomy group yields the Ricci scalar via deficit (the group-structure assumption).**
Regge calculus gives the Ricci scalar because its holonomy lives in the rotation/Lorentz group of a metric geometry. TRT must establish that the relational structure's holonomy takes values in the appropriate group so that its deficit is the gravitational curvature, not some other quantity. This requires that the emergent geometry of §6.3 be genuinely (pseudo-)Riemannian with the right frame group. ASSUMED, and tied to making §6.3 precise.

**Gap 3: That the continuum limit exists and is 4D Lorentzian (Lovelock L4, L5).**
The discrete structure must have a continuum limit that is local and four-dimensional with Lorentzian signature. TRT does not currently derive dimensionality or signature. ASSUMED.

---

## 6. Result of This Stage

The gravity derivation now reads as a clean conditional with a single principal unknown:

> **If** logical co-admissibility is measured by a raw holonomy deficit (linear), **and** the relational holonomy carries the appropriate frame-group structure, **and** the continuum limit is 4D Lorentzian, **then** the measure is the Regge / Einstein-Hilbert action, Lovelock forces the Einstein tensor, conservation follows from Bianchi, and TRT recovers General Relativity exactly, with no higher-curvature corrections.

The principal unknown is Gap 1: linear versus quadratic. And TRT's own commitments supply a real argument for linear (logic has no imposed metric, only a deficit), which is the encouraging and somewhat surprising finding of this stage. The two subsidiary gaps (2, 3) are shared with essentially all discrete-gravity programs and are not special burdens of TRT.

**Confidence update.**
- That TRT *can* recover GR exactly (conditional on linearity): raised to MEDIUM, because Regge calculus is a rigorous existence proof that linear-deficit measures give exactly GR, and TRT has a genuine internal argument for linearity.
- That the linearity assumption (Gap 1) actually holds: UNCERTAIN, but now framed as a tractable question about the nature of logical violation rather than an open physics problem.
- That TRT gives modified gravity instead: still live (MEDIUM), and it is the outcome if Gap 1 resolves toward a quadratic/metric measure.

The discriminating consequence is now concrete and potentially observable: **linear co-admissibility predicts exact GR (no higher-curvature corrections from this mechanism); quadratic predicts Bianconi-class modified gravity with corrections at high curvature.** These differ near black holes and in the early universe. The linear-versus-quadratic question is therefore not merely formal; its resolution makes an observational difference, which is exactly the kind of discriminating content the research program (paper §13) demands.

---

## 7. Next Step

Resolve Gap 1 in the discrete setting. Define joint *L₃*-satisfiability on a finite relational graph precisely, with explicit edge-transformations and an explicit measure of the failure of cycle-closure, and determine whether the natural measure of that failure is linear or quadratic in the deficit. Because the setting is finite and combinatorial, this is a well-posed mathematical question, not a continuum physics problem, and it should be decidable.

*Failure condition:* if the natural measure of joint-satisfiability failure is quadratic (or higher) in the deficit with no logical motivation for linearity, then TRT gives modified gravity, the §13.4 conjecture is downgraded to "GR-limiting modified gravity," and the linearity argument of §4 is refuted. That outcome should be recorded as plainly as a success.

*Success condition:* if the natural measure is linear, with the linearity following from the structure of *L₃* rather than imposed by hand, then combined with Gaps 2 and 3 (shared with all discrete-gravity programs) TRT has a credible route to deriving GR exactly, and the gravity conjecture moves from LOW to a defensible MEDIUM.

This is the sharpest the question has been made. It is one combinatorial problem, with a clear success and failure condition, and a real argument on each side.

---

## References for this document

Regge, T. (1961) 'General relativity without coordinates', *Il Nuovo Cimento*, 19(3), pp. 558-571. (Verify exact citation against primary.)

Lovelock, D. (1971) 'The Einstein tensor and its generalizations', *Journal of Mathematical Physics*, 12(3), pp. 498-501.

Bianconi, G. (2025) 'Gravity from entropy', *Physical Review D*, 111(6), 066001.

(The linear-deficit Regge action converging to the Einstein-Hilbert action ∫√g(R − 2Λ), and curvature concentrating on hinges as deficit angle, are standard results in the Regge-calculus and causal-dynamical-triangulations literature.)
