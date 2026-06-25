# TRT Gravity: Derivation Skeleton (Path A)

**Working document. Task 0.1 / 3.1 of the research program.**

**Status:** This is not a derivation. It is a derivation *schema*: an explicit statement of what global co-admissibility would have to be formalized as, what bridge premises a gravity result requires, and what would follow if those premises held. Its purpose is to make the gaps precise and falsifiable, in the Jacobson (1995) style where every assumption is on the table. Confidence labels are attached to each step. Any step marked ASSUMED is a premise the program still owes, not a result it has earned.

---

## 0. The Honesty Constraint

The entropic-gravity literature contains derivations that secretly assume their conclusion. The standard route to "deriving" the Einstein equations feeds in (i) a horizon temperature, (ii) an entropy proportional to area, and (iii) the Clausius relation δQ = T dS, and then recovers the field equations. This is legitimate only when those three inputs are stated as premises rather than smuggled. Jacobson's 1995 derivation is honest precisely because it declares its inputs.

This skeleton holds to the same standard. Every move is tagged:

- **GIVEN**: established physics or mathematics, not in question.
- **TRT**: a claim internal to TRT's ontology, with its paper-section confidence.
- **ASSUMED**: a bridge premise the program has not yet earned. These are the debts.
- **DERIVED**: follows from the items above it by stated inference.

The skeleton succeeds as a skeleton if the ASSUMED items are few, explicit, and individually testable. It would succeed as a *derivation* only if each ASSUMED item were later discharged by Task 0.1's formalization. It fails if the ASSUMED items turn out to encode the conclusion (the area law or the field equations) in disguise.

---

## 1. What Must Be Defined: Global Co-Admissibility

The gravity conjecture says gravity is the actualization of global co-admissibility on the relational structure of χ. Before any derivation, "global co-admissibility" must be a definite object. Here is the candidate, stated as precisely as the current framework allows, with its gaps marked.

**Candidate definition (TRT, to be formalized — this is Task 0.1).**
Let the actualized domain χ consist of actualized states standing in relations. Represent the relational structure as a set of states {sᵢ} together with relations Rᵢⱼ among them. A *local* admissibility condition requires each state and each relation to satisfy L₃ individually: no sᵢ is both F and not-F in the same respect, no Rᵢⱼ asserts and denies the same relation.

*Global* co-admissibility is the stronger requirement that the relations be *jointly* satisfiable under L₃ across the entire structure at once: there exists no subset of relations whose conjunction violates L₃ even though each member is locally admissible.

**The gap (UNCERTAIN).** This is still informal in one decisive respect: it does not yet specify a *measure* of how far a candidate global structure is from co-admissibility, nor a dynamics that drives structures toward co-admissibility. Without one or both, there is no quantity to extremize and no equation to derive. Supplying this is the heart of Task 0.1. Two routes are available, and the choice determines everything downstream:

- *Route 1 (constraint-satisfaction):* co-admissibility is binary (a structure either is or is not globally co-admissible), and gravity is the constraint that projects onto the co-admissible subspace. This yields *constraint equations*, not dynamics.
- *Route 2 (variational):* co-admissibility comes in degrees, measured by some functional D[χ] that vanishes exactly when the structure is globally co-admissible, and gravity is the gradient flow or stationary condition of D. This yields *dynamics*.

Route 2 is the one that could produce field equations. It requires defining D[χ], a measure of global logical "tension" in the relational structure. **This functional D[χ] is the single most important undefined object in the entire TRT gravity program.** Everything below is conditional on it.

---

## 2. The Bridge Premises

To connect the (still-undefined) D[χ] to gravity, the skeleton needs bridge premises linking TRT's primitives to geometric and thermodynamic quantities. Here they are, each tagged.

**Bridge 1 — Geometry from relations (TRT, §6.3, MEDIUM).**
The relational structure of χ has an emergent metric geometry: gμν ~ Geom(Rel(χ)). The relations among actualized states induce a notion of distance, adjacency, and curvature.
*Status:* internal TRT claim, already in the paper at moderate confidence. Not free, but not new debt.

**Bridge 2 — Actualization-rate as a scalar field (ASSUMED, Task 0.2).**
There exists a covariant scalar α(x) measuring the local rate or density of actualization across the relational structure.
*Status:* this is Task 0.2 of the program, currently undefined. DEBT.

**Bridge 3 — Co-admissibility tension relates to curvature (ASSUMED).**
The global co-admissibility functional D[χ], when localized, relates to the curvature of the emergent metric: regions of higher unresolved logical tension correspond to regions of higher curvature.
*Status:* this is the central conjectural bridge. It is the formal content of "curvature is an actualization gradient" (§10.1.3). DEBT, and the riskiest one.

**Bridge 4 — Boundary information scales with area (GIVEN/TRT).**
The information content of a region's relational structure is fixed at its boundary, and for the emergent geometry this boundary information scales with area.
*Status:* this is partly GIVEN (holographic results: Bekenstein-Hawking, Ryu-Takayanagi) and partly the TRT informational-leg claim (§10.1.1). Note carefully: **invoking area-scaling here is exactly the kind of premise that can smuggle the conclusion.** If the area law is assumed at Bridge 4, then "deriving" the area law downstream is circular. This bridge must be used only to motivate, not to derive, the area law. Flagged RED.

---

## 3. What Would Follow: The Conditional Chain

Given the bridges, here is what the skeleton can and cannot reach. Each target is tagged with what it depends on.

### 3.1 Conservation (the strongest link, nearly GIVEN)

If gravity is the actualization of global co-admissibility (TRT), and global co-admissibility is a self-consistency condition on the entire relational structure (TRT §1 above), then the geometric object expressing that consistency must be self-consistent in the sense of having vanishing divergence. The contracted Bianchi identity, ∇μ Gμν = 0 (GIVEN, pure differential geometry), is exactly such a self-consistency identity. Identifying the co-admissibility condition with the Bianchi-satisfying object gives covariant conservation, ∇μ Tμν = 0, once the field equation links geometry to stress-energy.

*Assessment (MEDIUM).* This link is real and is the strongest part of the gravity claim, because the Bianchi identity is genuine geometry, not an assumption. **But it does not single out gravity:** as the paper concedes (§10.1.2), the Bianchi identity is general differential geometry and appears in gauge theories. What this gives is: *if* the global co-admissibility object is geometric and divergence-free, conservation follows. It does not yet give *which* geometric object, i.e. it does not give the Einstein tensor specifically. That requires §3.2.

### 3.2 The Einstein tensor specifically (the hard gap, UNCERTAIN)

To get gravity rather than some-theory-with-constraints, the skeleton must show that global co-admissibility forces the *specific* form Gμν = Rμν − ½ R gμν, not merely some divergence-free tensor.

*Status:* **this is the gap that decides whether TRT derives gravity or merely interprets it.** There is a known theorem that helps and a precise statement of what the theorem demands.

- *Helps (GIVEN, Lovelock 1971):* in four dimensions, any symmetric, divergence-free tensor built from the metric and its first two derivatives (linear in the second derivatives) is necessarily *aGμν + bgμν*, the Einstein tensor plus a cosmological term. The uniqueness is genuine and proven. So *if* TRT can establish that global co-admissibility requires such a tensor, Lovelock forces the Einstein tensor uniquely, and the field-equation form follows.

- *The precise debt (UNCERTAIN).* Lovelock's uniqueness holds under exactly five conditions: (1) the equations of motion are second-order, (2) no extra fields beyond the metric, (3) general covariance, (4) locality, and (5) four spacetime dimensions. Each known modified-gravity theory works by violating one of these. Therefore the TRT gravity derivation does not owe a single hand-wave; it owes **five specific demonstrations** that the co-admissibility measure D[χ], when localized, satisfies each Lovelock condition:

  - **L1 (second order):** D[χ] localizes to a tensor depending on the metric through at most second derivatives. *This is the hardest and least obvious.* It is not clear why global logical co-admissibility should care about derivative order at all. If it does not constrain derivative order, co-admissibility is compatible with higher-derivative (f(R), Gauss-Bonnet) gravities and does not single out Einstein.
  - **L2 (no extra fields):** the localization introduces no degrees of freedom beyond the emergent metric. If co-admissibility carries an auxiliary field, the result is scalar-tensor gravity, not GR.
  - **L3 (covariance):** the measure is generally covariant, depending on no prior geometry. Plausible for TRT, since the relational structure is background-free by construction (§6.3).
  - **L4 (locality):** the localization is local. TRT's de-actualization and boundary claims (§10.1.4) flirt with nonlocality, so this needs care.
  - **L5 (four dimensions):** the emergent geometry is four-dimensional. TRT does not currently predict dimensionality; this would have to be assumed or separately derived.

  *The sharpest statement of the whole gravity gap:* discharge L1 through L5 from co-admissibility, and Lovelock delivers Einstein gravity with no further work. The conjecture's failure condition (paper §13.4) is now precise: it fails at whichever of L1–L5 cannot be derived, and L1 (derivative order) is the prime suspect. This is progress, because a five-part precisely-stated debt is a research program; a single vague hope is not.

### 3.3 The area law (do NOT claim from this skeleton)

Given Bridge 4's RED flag, the area law cannot be honestly derived here, because area-scaling was used as an input premise. The most this skeleton can say: the area law is *consistent with* and *motivated by* the boundary-relational structure of co-admissibility. Deriving S = A/4 with its coefficient requires getting the coefficient from the co-admissibility measure independently of assuming area-scaling, which is not currently possible.

*Assessment (LOW/UNCERTAIN).* The coefficient 1/4 is the real prize and is out of reach until D[χ] is defined and shown to count boundary degrees of freedom independently. Claiming the area law from the current skeleton would be the circular move §0 forbids.

---

## 4. The Skeleton in One Diagram

```
Task 0.1: define D[χ]          ASSUMED, the root debt
(global co-admissibility         │
 measure)                        │
                                 ▼
        ┌── localizes to a geometric tension ──┐
        │   (Bridge 3, DEBT)                    │
        ▼                                       ▼
must be symmetric,              relates to curvature
2nd-order, divergence-free      (Bridge 1+2, MEDIUM/DEBT)
        │                                       │
        ▼                                       │
  Lovelock 1971 (GIVEN)                         │
        │ forces uniquely                       │
        ▼                                       ▼
  Einstein tensor Gμν  ◄───────────── + field equation
        │                                       │
        ▼                                       ▼
  Bianchi ∇μGμν=0 (GIVEN) ──► conservation ∇μTμν=0  (MEDIUM)
        │
        ▼
  area law S=A/4   ◄── NOT derivable here (Bridge 4 circular)
                       coefficient out of reach until D[χ] counts
                       boundary DOF independently (LOW/UNCERTAIN)
```

---

## 5. What This Skeleton Establishes

Three honest conclusions.

First, the gravity derivation **reduces to a precise five-part debt**: derive Lovelock conditions L1 through L5 from the global co-admissibility measure D[χ]. If all five are discharged, Lovelock's theorem forces the Einstein tensor uniquely, and conservation follows from Bianchi. The program is not vague; it is blocked at five named, individually checkable points, of which L1 (why second-order rather than higher-derivative) is the prime suspect. A five-part precise debt is a research program; a single vague hope is not.

Second, the conservation link is **already strong** (MEDIUM), because it rests on the Bianchi identity, which is real geometry. But it is not gravity-specific, so it cannot stand alone.

Third, the area law and its coefficient are **not reachable** from the current skeleton without circularity, and any claim to derive them now would violate the honesty constraint of §0. They wait on a D[χ] that counts boundary degrees of freedom independently of assuming area-scaling.

A note on what would falsify the gravity conjecture outright: if it can be shown that global co-admissibility is *compatible with* a violation of any of L1–L5 (for instance, that it permits higher-derivative dependence), then co-admissibility does not single out GR, and the gravity claim is permanently interpretive. That is a real and reachable negative result, and it should be pursued as seriously as the positive program.

---

## 6. The Next Concrete Step (Path B entry point)

The skeleton identifies the single tractable next move: attempt to define D[χ], the global co-admissibility measure, and check whether *any* natural definition localizes to a second-order symmetric divergence-free tensor.

The most promising candidate to try, given the literature, is a *relative-entropy-type functional*, since Bianconi (2025) shows that a quantum relative entropy between the spacetime metric and a matter-induced metric yields modified Einstein equations. The TRT-specific question is whether global co-admissibility can be expressed as such a relative-entropy quantity, where the "distance" being measured is logical tension (distance from joint L₃-satisfiability) rather than a generic information distance.

*Failure condition for the next step:* if no co-admissibility measure localizes to second order, or if every candidate requires assuming area-scaling, then the gravity conjecture remains permanently interpretive (paper §13.4 failure condition met), and that should be recorded as a negative result, not hidden.

This is where Path B begins: not "derive gravity," but "define D[χ] and test whether it localizes to satisfy Lovelock conditions L1–L5." That is a bounded, checkable task with a clear failure condition, and it is the honest center of the gravity program.

---

## References for this document

Jacobson, T. (1995) 'Thermodynamics of spacetime: The Einstein equation of state', *Physical Review Letters*, 75(7), pp. 1260-1263.

Lovelock, D. (1971) 'The Einstein tensor and its generalizations', *Journal of Mathematical Physics*, 12(3), pp. 498-501. (Verify exact pages against primary before citing in the paper.)

Bianconi, G. (2025) 'Gravity from entropy', *Physical Review D*, 111(6), 066001.
