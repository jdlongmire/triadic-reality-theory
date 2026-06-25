# TRT Gravity: Attempting the Co-Admissibility Measure D[χ] (Path B)

**Working document. Task 0.1 (the root debt) and Task 3.1 (L1 test).**

**Status:** This is a genuine derivation attempt, not a derivation. It constructs a candidate for the global co-admissibility measure D[χ] and tests it against Lovelock condition L1 (second-order). It reaches a definite and honest conclusion, but that conclusion is *not* "TRT derives gravity." Every step is tagged EARNED (follows rigorously from stated inputs), HEURISTIC (plausible motivating argument, not proof), or ASSUMED (premise still owed). The value of the document is that it locates precisely where the attempt succeeds and where it stalls.

---

## 1. The Target, Restated

From the skeleton (Path A), the gravity derivation reduces to: define D[χ], the global co-admissibility measure, such that its variation with respect to the emergent metric yields a tensor satisfying Lovelock's five conditions. Of these, divergence-free comes free from general covariance (L3) via the Noether identity, so the live conditions are L1 (second order), L2 (metric only), L4 (local), L5 (4D). L1 is the crux. This document attempts L1.

The question for this document, stated sharply:

> Can a measure of global logical co-admissibility, defined on the relational structure of χ, localize to a tensor that is second-order in the emergent metric, rather than higher-order?

If yes, Lovelock plus covariance forces (close to) the Einstein tensor. If the natural answer is "no, it is higher-order," then TRT gives a modified gravity, not GR, and L1 fails.

---

## 2. What "Logical Co-Admissibility" Must Mean Geometrically

To test L1, co-admissibility has to be connected to geometry concretely enough to count derivatives. Here is the chain, tagged.

**Step 2.1 (TRT, §6.3, MEDIUM).** The relational structure of χ is a set of actualized states with relations among them, and this structure carries an emergent metric *g*. Relations define adjacency and comparison; the metric is the continuum encoding of those relations.

**Step 2.2 (HEURISTIC).** Local *L₃*-admissibility is a pointwise condition: each state is self-identical (identity), not self-contradictory (non-contradiction), determinate (excluded middle). Pointwise admissibility imposes no constraint relating a state to its neighbors, so it carries *zero* derivatives of the relational structure. It cannot produce geometry. Geometry must come from how admissibility constrains *relations between* states, not states themselves.

**Step 2.3 (HEURISTIC, and this is the key move).** Global co-admissibility is the requirement that relations be *jointly* satisfiable. The minimal nontrivial joint-satisfiability condition is *consistency around a closed path*: if one transports a relational comparison from a state back to itself around a loop in the structure, joint co-admissibility requires the result to be consistent with the starting point. Inconsistency of transport around a closed loop is therefore the elementary unit of global logical tension.

This is the load-bearing identification, and it is where the geometry enters. In differential geometry, the failure of consistency of parallel transport around an infinitesimal closed loop *is* the Riemann curvature, and it scales with the area of the loop. This is the standard geometric meaning of curvature (holonomy). So:

> Elementary global logical tension (loop-inconsistency of relational transport) is identified with curvature holonomy.

*Status: HEURISTIC.* The identification is motivated and structurally natural, but it is not proven that logical co-admissibility *must* be checked loop-wise rather than by some other global criterion. A critic can ask why joint satisfiability reduces to loop consistency. The honest answer: it is the minimal nontrivial closed condition, but minimality is a plausibility argument, not a theorem. This is the first place a referee will push, and the push is fair.

**Consequence of 2.3, if granted (EARNED given 2.3).** Because loop-holonomy scales with loop area, the leading logical tension is *quadratic* in the loop size, hence *second-order* in the relational/metric structure. This is the first encouraging result: *if* co-admissibility is loop-checked, its leading term is automatically second-order, which is exactly what L1 needs. The area-scaling of holonomy delivers second-order for free.

But "second-order in loop size" is not yet "second-order in metric derivatives in the Lovelock sense," and conflating them would be the trap flagged in the skeleton §0. The next section confronts this directly.

---

## 3. The Decisive Fork: Full Riemann vs Trace

Here the attempt meets its real test. Loop-holonomy is the *full Riemann tensor*. The Riemann tensor governs both the *volume* distortion and the *shape* (shear) distortion of a small region. Lovelock's theorem yields the Einstein tensor only from a functional that is second-order and produces the *right* second-order object; a functional built from the full Riemann tensor generically produces *higher-curvature* equations of motion (Riemann-squared terms, Gauss-Bonnet, f(Riemann)), which violate L1 and give modified gravity, not GR.

This is exactly the outcome Bianconi's 2025 entropic-gravity program exhibits: its action depends explicitly on the Riemann tensor and yields *modified* Einstein equations that reduce to GR only in a low-curvature limit. So a generic relative-entropy or holonomy functional gives modified gravity. **By default, the natural construction fails L1.** This must be stated plainly: the default answer to this document's question is "higher-order, so modified gravity, not GR."

To get GR exactly, the measure must depend not on the full Riemann holonomy but on its *trace* only. The relevant fact (EARNED, standard differential geometry, verified):

> The Ricci tensor is the trace of Riemann and is precisely the second-order coefficient of *volume* deviation of geodesic balls: √det g(exp_x(tv)) = 1 − (1/6) Ric(v,v) t² + O(t³). The traceless part of Riemann (the Weyl tensor) governs *shape* distortion at fixed volume.

So the fork is sharp and geometrically meaningful:

- If co-admissibility cares about **volume** (how many distinct admissible states a region can contain, the *counting* of relational capacity), the measure depends on Ricci, the trace. A functional built from Ricci and the scalar curvature is exactly the class that yields the Einstein-Hilbert action and, by Lovelock, the Einstein tensor. **L1 satisfied, GR recovered.**
- If co-admissibility cares about **shape** (the full relational pattern, including shear), the measure depends on the full Riemann/Weyl, and yields modified, higher-curvature gravity. **L1 violated, modified gravity.**

So L1 reduces to a single, sharply stated question:

> **Does global logical co-admissibility constrain the volume of relational capacity (trace/Ricci) only, or the full relational shape (Weyl included)?**

---

## 4. The Argument That It Is Volume Only (and Why It Is Not Yet Conclusive)

There is a genuine TRT-internal argument that co-admissibility is volume-only, which would give GR. There is also an honest reason it does not yet close.

**The argument (HEURISTIC, but substantive).** Co-admissibility is about *joint satisfiability*: whether the relations in a region can all hold at once without violating *L₃*. What this constrains is the *number of mutually admissible configurations* a region can support, the count of states that can be jointly actualized. That is a *capacity* or *volume* notion: how much admissible structure fits. It is not obviously a *shape* notion. Logical consistency does not, on its face, care about the shear of a region, only about whether the region's contents can coexist, which is a count. Counting is volume. Volume deviation is Ricci. Therefore co-admissibility plausibly depends on Ricci, not Weyl, and L1 is satisfied.

This connects to the informational leg (§10.1.1, paper) and to the entropy programs: black-hole entropy counts admissible microstates and scales with area, a capacity/volume-boundary notion, not a shape notion. The consistent thread across TRT is that the logical-informational content is a *count*, and counts are volumetric. That is a real and coherent argument.

**Why it does not yet close (the honest gap).** The argument trades on an intuitive identification of "joint satisfiability" with "count of configurations" with "volume." Each link is plausible and none is proven. Specifically:

1. That joint satisfiability is fully captured by a *count* (rather than also by relational pattern) is asserted, not derived. *L₃* applied to a structured set of relations might well be sensitive to the pattern of relations (which relation conflicts with which), not merely how many coexist. If pattern matters, Weyl re-enters and L1 fails.
2. The loop-holonomy identification of §2.3 gives the *full* Riemann as the elementary tension. Projecting onto the trace requires an additional principle ("co-admissibility reads only the trace of holonomy") that has not been justified. Without it, the default full-Riemann result of §3 stands and L1 fails.

So the situation is precise. There is a coherent route to L1 (co-admissibility is volumetric → Ricci → Einstein-Hilbert → Lovelock → GR), but it depends on an unproven projection principle: that logical co-admissibility reads only the trace (volume) and not the shear (shape) of the relational holonomy. Call this the **Trace Principle**.

---

## 5. The Result of the Attempt

The attempt does not derive gravity. It produces something more useful than a false success: it isolates the entire L1 question into one unproven principle.

> **The Trace Principle (the single remaining debt for L1):** Global logical co-admissibility depends only on the trace of the relational holonomy (the volume/capacity of jointly admissible structure), not on its traceless part (the shape/shear of the relational pattern).

Conditional results, cleanly stated:

- **If the Trace Principle holds:** co-admissibility localizes to a Ricci-based functional, which is the Einstein-Hilbert class; by Lovelock (L1–L5, with divergence-free from covariance) this forces the Einstein tensor; GR is recovered, and the conservation law follows from Bianchi. *Confidence conditional on the Principle: the chain is EARNED.*
- **If the Trace Principle fails:** co-admissibility retains full-Riemann (Weyl) dependence, yielding modified higher-curvature gravity reducing to GR only in a limit, as in Bianconi (2025). *This is the §13.4 failure condition: TRT then gives modified gravity, not GR, and the "derivation of gravity" claim is downgraded to "derivation of a GR-limiting modified gravity."*

Either way, this is a real outcome. The gravity conjecture is no longer open-ended. It has been reduced to a single, sharply stated, and in-principle-decidable proposition about whether logical co-admissibility is volumetric or shape-sensitive. That proposition is the Trace Principle, and proving or refuting it is now the whole game.

---

## 6. Confidence and Honest Assessment

**Confidence that TRT derives GR exactly: LOW, and lower than before this attempt in one respect.** The attempt surfaced that the *default* behavior of any holonomy- or relative-entropy-based measure is full-Riemann dependence, i.e. modified gravity (the Bianconi precedent confirms this). Getting exact GR requires the Trace Principle, which is an additional, unproven, and non-obvious constraint. So the honest update is: exact GR from TRT is *harder* than the skeleton suggested, because the natural constructions give modified gravity by default.

**Confidence that TRT derives a GR-limiting modified gravity: MEDIUM.** This is the Bianconi-class outcome, and it is what a relative-entropy co-admissibility measure would most naturally produce. If TRT is content to predict "GR as a low-curvature limit, with higher-curvature corrections," that is reachable and consistent with an active 2025 research program. But note the cost: it is then no longer a unique derivation of GR, and the higher-curvature corrections would need to be either matched to Bianconi's or shown to be observationally viable.

**The genuine contribution of this attempt:** it converts "can TRT derive gravity?" into "is logical co-admissibility volumetric (Trace Principle) or shape-sensitive?" That is a sharper, smaller, and potentially decidable question. It also predicts, honestly, that the most likely outcome is modified gravity rather than exact GR, which is a falsifiable stance: if TRT's co-admissibility measure is ever formalized and turns out to read only the trace, that would be a surprising and strong result; the default expectation is that it reads the full tensor.

---

## 7. Next Step

The Trace Principle is now the target, replacing the vaguer Task 3.1. The concrete next move is to attempt a formal definition of joint *L₃*-satisfiability on a relational structure and compute whether its leading geometric obstruction is the trace (Ricci) or the full holonomy (Riemann). This is a problem in the logic of relational structures, not yet a problem in physics, and it may be tractable in a discrete/combinatorial setting (e.g. on a relational graph, where "joint satisfiability around cycles" can be made exact) before any continuum limit.

*Failure condition:* if the discrete computation shows the leading obstruction is generically the full holonomy with no natural trace projection, the Trace Principle fails, and TRT's gravity is modified gravity, not GR. That result should be recorded plainly.

---

## References for this document

Lovelock, D. (1971) 'The Einstein tensor and its generalizations', *Journal of Mathematical Physics*, 12(3), pp. 498-501.

Bianconi, G. (2025) 'Gravity from entropy', *Physical Review D*, 111(6), 066001.

(Volume-deviation expansion and the Ricci/Weyl volume/shape split are standard differential geometry; see any text treating the asymptotic expansion of the Riemannian volume element, e.g. the relation √det g = 1 − (1/6)Ric(v,v)t² + O(t³).)
