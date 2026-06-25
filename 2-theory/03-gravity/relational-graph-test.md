# TRT Gravity: The Relational-Graph Computation (Task 3.1)

**Working document. The attempt at the linearity crux.**

**Status:** This is the genuine computation. It sets up joint *L₃*-satisfiability on a finite relational graph, works the smallest nontrivial case explicitly, and locates the linear-versus-quadratic fork in precise mathematical terms. Honest headline up front: **the computation does not decide the fork, but it sharpens it from a vague question into a recognizable mathematical dichotomy (cohomological obstruction versus least-squares residual), exhibits both sides concretely in a worked example, and identifies the exact further fact that would settle it.** Tags: EARNED (rigorous), HEURISTIC (argued, not proved), OPEN (undecided).

---

## 1. Setup (EARNED)

A finite relational structure is a graph: nodes are actualized states, edges are relations. Following the holonomy identification of the previous documents, each directed edge *e: i → j* carries a transformation *Uₑ ∈ G* for some group *G*, read as "the relation asserts that the value at *j* is *Uₑ* applied to the value at *i*."

A *value assignment* is a map from nodes to the space *V* on which *G* acts: *i ↦ vᵢ ∈ V*. The relation on edge *e: i → j* is *satisfied* by the assignment iff

  *vⱼ = Uₑ vᵢ.*

**Joint *L₃*-satisfiability (EARNED definition).** The relational structure is jointly satisfiable iff there exists a value assignment satisfying every edge relation simultaneously. This is the exact relational reading of non-contradiction: no state is forced to two different values in the same respect.

**Holonomy and the obstruction (EARNED, standard).** Transport a value around a closed cycle *γ*. The composed transformation is the holonomy *Hγ = Uₑₙ ⋯ Uₑ₁*. A consistent assignment requires *vᵢ = Hγ vᵢ* for the basepoint, so *vᵢ* must be a fixed point of *Hγ*. Generic holonomy has no nontrivial fixed point, so:

> The relational structure is jointly satisfiable (for nonzero values, globally) iff the holonomy is trivial around every independent cycle, i.e. iff the connection *{Uₑ}* is **flat**.

This is exact. Joint *L₃*-satisfiability = flatness of the relational connection. The obstruction to satisfiability is the curvature (nontrivial holonomy), and it is a cohomological object: the holonomy assigns to each cycle an element of *G*, and flatness is the vanishing of this assignment.

---

## 2. The First Honest Problem: Strict Satisfiability Is Too Strong (EARNED)

Strict joint satisfiability demands flatness everywhere. A theory of gravity cannot demand flatness, because gravity *is* curvature; a universe forced to be globally flat has no gravity at all. So strict binary *L₃*-co-admissibility, taken as an absolute requirement on χ, would forbid gravity rather than produce it.

The resolution is forced and is itself informative. Co-admissibility cannot be an absolute constraint; it must be a *quantity that actualization extremizes*. Perfect co-admissibility (flatness) is the vacuum. Matter, the informational content actualized into the region, sources deviation from flatness. The actual geometry is the one that extremizes total logical tension subject to the matter content.

This is exactly the structural form of a variational theory of gravity: empty space relaxes to flat, matter sources curvature, and the field configuration extremizes an action. The relational-graph picture has, with no further assumption, reproduced the *form* of a gravitational variational principle. (EARNED, modulo the identification of "matter" with sourced informational content, which is TRT-internal and MEDIUM.)

What it has not yet fixed is the *functional form* of the tension. That is the fork.

---

## 3. The Worked Case: A Single Triangle (EARNED)

Take the smallest cycle: three nodes, three edges, group *U(1)* (phases), so transformations add. Let the edge values be *a, b, c* (the connection). The holonomy around the triangle is the deficit

  *δ = a + b + c.*

A consistent phase assignment *φ₁, φ₂, φ₃* on the nodes would need *φ₂ − φ₁ = a*, *φ₃ − φ₂ = b*, *φ₁ − φ₃ = c*. Summing, the left side telescopes to zero, so consistency requires *δ = 0*. If *δ ≠ 0*, the triangle is not jointly satisfiable. The deficit *δ* is the exact obstruction.

Now the decisive question: how do we *measure* the magnitude of the unsatisfiability? Two measures, both legitimate, computed explicitly.

**Measure 1 — the raw obstruction (linear).**
The deficit itself, *δ = a + b + c*, or its magnitude *|δ|*. This is computed directly from the connection by composing the edge transformations around the loop. It requires nothing but the group operation. It is intrinsic to the connection and uses no structure on the value space *V*.

**Measure 2 — the least-squares residual (quadratic).**
Ask instead: what is the *best* assignment, the one that comes closest to satisfying all three relations, and how large is the leftover? Minimize

  *Σ = (φ₂ − φ₁ − a)² + (φ₃ − φ₂ − b)² + (φ₁ − φ₃ − c)².*

Let the residuals be *r₁ = φ₂ − φ₁ − a*, *r₂ = φ₃ − φ₂ − b*, *r₃ = φ₁ − φ₃ − c*. The phases cancel in the sum: *r₁ + r₂ + r₃ = −(a + b + c) = −δ*. So we minimize *r₁² + r₂² + r₃²* subject to *r₁ + r₂ + r₃ = −δ*. By symmetry the minimum is at *r₁ = r₂ = r₃ = −δ/3*, giving

  *Σ_min = 3 · (δ/3)² = δ²/3.*

The best-fit residual is *δ²/3*, **quadratic in the deficit.**

**This is the fork, made concrete and exact.** The same triangle with the same deficit *δ* has a linear measure of unsatisfiability (*|δ|*, the raw obstruction) and a quadratic one (*δ²/3*, the best-fit residual). Both are mathematically legitimate. They are different functions of the same logical tension.

---

## 4. What the Two Measures Become (EARNED)

The two measures are not arbitrary; each is the germ of a known and different physics.

**Linear (raw obstruction) → General Relativity.**
Summing the deficit over cycles, weighted by the cell volume, is exactly the Regge action *Σ (hinge volume)(deficit angle)*, whose continuum limit is the Einstein-Hilbert action *∫√g R* (EARNED, established in the prior document). Linear-in-deficit gives GR, with the Ricci scalar selected automatically because the unique scalar linear in curvature is *R*.

**Quadratic (best-fit residual) → modified / Yang-Mills-type gravity.**
Summing the squared residual is the lattice analogue of *∫|F|²*, a Yang-Mills-type or curvature-squared action. Its continuum limit carries higher-curvature terms (Riemann², etc.), giving modified gravity that reduces to GR only in a limit. This is the relative-entropy / Fisher-information / Bianconi-class outcome, and the quadratic appears for exactly the reason it appears here: a *squared norm* is minimized over best-fit assignments.

So the worked triangle confirms, concretely and correctly, the fork claimed abstractly in the previous document. Linear obstruction is GR; quadratic residual is modified gravity.

---

## 5. The Argument for the Linear (GR) Side (HEURISTIC, but sharpened)

The computation makes the argument for linearity sharper than before, because it exposes *exactly* what extra structure the quadratic measure requires.

The quadratic measure *δ²/3* arose from two ingredients absent in the linear measure:

1. A **squared norm** on the residuals, i.e. an inner product on the value space *V*. We wrote *r₁² + r₂² + r₃²*; the squaring is a choice of *L²* metric on *V*.
2. A **minimization** over assignments (best fit).

The linear measure used neither. The deficit *δ = a + b + c* is computed from the group operation alone, with no inner product on *V* and no minimization.

The TRT-internal argument is now precise. *L₃* supplies the *relations* (the connection, the group elements *Uₑ*). It does not supply an inner product on the value space *V*. Non-contradiction is the statement that a value cannot be forced to two incompatible determinations; it is registered by the failure of the loop to close, which is the deficit. It is not naturally a *squared distance*, because a squared distance requires a metric on values that logic does not provide. The squared residual is an *energy*; energies need metrics; *L₃* is not a metric.

Therefore the structure-minimal, *L₃*-faithful measure of unsatisfiability is the raw obstruction (linear), not the best-fit residual (quadratic). And linear gives GR.

This is a genuine argument and it cuts toward GR. It is not a proof.

---

## 6. The Honest Gaps, Now Precise (OPEN)

Three gaps remain, and the computation has made them sharper than they were.

**Gap A — minimization may be intrinsic to actualization.**
The quadratic measure came from *minimizing over best-fit assignments*. But actualization (A) might *be* a best-fit process: when a structure is not jointly satisfiable, A may resolve it by selecting the closest satisfiable assignment, which is exactly the least-squares projection, which is quadratic. If actualization resolves inconsistency by best-fit, the quadratic measure is the physically correct one, and TRT gives modified gravity. If actualization instead simply *registers* the obstruction without best-fitting, the linear measure holds, and TRT gives GR.

*So the fork reduces to a precise question about the nature of A:* **does actualizing action resolve unsatisfiable relational structure by best-fit projection (→ quadratic → modified gravity) or by direct obstruction-registration (→ linear → GR)?** This is the sharpest form the gravity question has reached.

**Gap B — the deficit angle still needs the frame geometry.**
Getting from the abstract group deficit to the Regge *deficit angle* (and hence the Ricci scalar) requires the holonomy group to be the frame-rotation group of a metric geometry. This is the shared discrete-gravity assumption (Gap 2 of the prior document), tied to making §6.3 of the paper precise. Not special to TRT.

**Gap C — value-space metric versus none.**
The argument of §5 rests on *L₃* supplying no inner product on *V*. A critic can argue that the value space of physical relations *does* carry a natural metric (Hilbert-space inner product, for quantum states), in which case the squared residual is natural after all and the quadratic measure returns. Whether the relevant value space is bare (no metric, → linear → GR) or Hilbert (metric, → quadratic → modified gravity) is undecided and may be the same question as Gap A in different dress.

---

## 7. An Unexpected Connection (HEURISTIC, flagged speculative)

Gap A asks how actualization resolves unsatisfiable structure: best-fit projection or obstruction-registration. This is recognizably *the same question* as the measurement problem in the quantum sector. The Logical Resolution Model (paper §6.6) asks how A resolves an unresolved quantum superposition into a determinate outcome. Best-fit projection onto a satisfiable assignment is structurally a *projection*, which is what measurement is often modeled as.

So the linear-versus-quadratic gravity fork and the nature of quantum measurement may be governed by the same unknown: *how A resolves unresolved admissible structure.* If A is a projector (best-fit), both the quantum sector and the gravity sector inherit quadratic structure. If A registers obstructions without projecting, both are linear. This is a genuine potential unification of the two open problems, and it is offered as a conjecture worth recording, not a result. Confidence: LOW, but the structural parallel is real and was not designed in; it emerged from the computation.

---

## 8. Result of the Attempt

Stated honestly.

**Not decided.** The computation does not prove TRT yields GR, and does not prove it yields modified gravity. Claiming either would be false.

**Sharpened to a recognizable dichotomy (EARNED).** The linear-versus-quadratic fork is now exhibited concretely: for a single triangle of deficit *δ*, the raw obstruction is *|δ|* (linear, → GR via Regge) and the best-fit residual is *δ²/3* (quadratic, → modified gravity via Yang-Mills-type action). Both are computed explicitly and correctly. The fork is the well-known mathematical distinction between a cohomological obstruction and a least-squares residual.

**Reduced to a question about A (the genuine advance).** Whether TRT gives GR or modified gravity reduces to whether actualizing action resolves unsatisfiable relational structure by direct obstruction-registration (linear, GR) or by best-fit projection (quadratic, modified gravity). This is a sharp, structural question about the primitive A, and it plausibly coincides with the measurement-resolution question in the quantum sector.

**Argument leans GR (HEURISTIC).** The obstruction measure uses only the relational/group structure that *L₃* supplies, while the residual measure requires an inner product on the value space and a minimization that *L₃* does not supply. On structure-minimality grounds, the *L₃*-faithful measure is the linear obstruction, hence GR. This is a real argument and it leans toward GR, but it rests on the value space carrying no imposed metric, which is precisely Gap C and is not settled.

**Confidence after the attempt.**
- TRT yields GR exactly: LOW-to-MEDIUM, conditional on A being obstruction-registering and the value space being metric-free. The argument leans this way but does not close.
- TRT yields modified gravity: LOW-to-MEDIUM, the outcome if A is best-fit/projective or the value space is Hilbert-metric. Equally live.
- That the fork is now a precise question about the nature of A, shared with the measurement problem: this is the EARNED advance, and it is the honest product of the attempt.

---

## 9. Next Step

The question is now well-posed and singular: **characterize how actualizing action A resolves unsatisfiable relational structure.** Two sub-routes:

1. *Formal.* Define A's resolution operation precisely. If it is a projection (minimizing a norm), determine what norm, and whether the norm is forced by the structure or imposed. This connects directly to Task 2.2 (Born rule) and the LRM, since the measurement-resolution operation is the same A.

2. *Comparative-observational.* Linear (GR) and quadratic (modified gravity) differ observationally at high curvature. If TRT cannot decide the fork internally, the fork becomes an empirical question: does nature show the higher-curvature corrections that the quadratic measure predicts? This is a genuine discriminating prediction (paper §13, Tier 4.2), and it is the same fork seen from the data side.

*Failure condition for the program here:* if A's resolution operation cannot be characterized, or is shown to be best-fit/projective with an imposed norm, the linear/GR route closes and TRT's gravity is modified gravity, to be recorded plainly.

This is the honest end of the attempt: not a derivation of gravity, but the reduction of "does TRT give GR" to a single sharp question about the nature of actualization, a question that the computation showed is shared with the measurement problem, and that is in principle decidable either formally or observationally.

---

## References for this document

(The triangle least-squares computation and the holonomy/flatness characterization are elementary and self-contained. External anchors, established in prior documents: Regge calculus → Einstein-Hilbert in the linear-deficit case; Lovelock 1971 for uniqueness; the quadratic *∫|F|²* structure of Yang-Mills-type actions is standard.)
