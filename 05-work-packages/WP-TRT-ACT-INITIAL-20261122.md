# WP-TRT-ACT-INITIAL-20261122: Initial actualization and subsequent transitions

**Status:** Proposed; awaiting formal and adversarial review.  
**Tier:** 2-theory / protective belt.  
**Authority:** Owner's 2026-11-22 direction to investigate a common primitive operator for initial and subsequent actuality. This proposal does not supersede WP-TRT-CORE-0001 or the 2026-11-12 and 2026-11-16 charter rulings.

## Problem

The established hard core defines A as non-temporal primitive state transition/change and explicitly prohibits defining A as actualization. The proposed refinement treats primitive Action as irreducible determination of actuality, with state-change a manifestation within an established order. These are not automatically equivalent. A direct canonical rewrite would conflict with the normalization and reconciliation records.

The initial case poses a specific challenge: a relation A(s_i,s_j) appears to require a prior state, while initial physical actualization must not presuppose prior physical actuality or physical time.

## Typed preliminary model

Let R be the representable domain; C ⊆ R its L3-coherent members; D ⊆ C the actualizable domain, with further conditions unspecified; and X the actualized event structure. Neither C=D nor D=X is assumed.

Define a *candidate* event relation T ⊆ (B ⊔ D) × D, where B is a typed **boundary-condition carrier**, not a pre-existing physical state. The disjoint union prevents conflating a boundary specification with an actualized state. A candidate event is (u,v) ∈ T, with u∈B or u∈D and v∈D. Define a separate obtaining predicate O(v,e), rather than building obtaining into T by definition.

- **Initial candidate:** u∈B; no prior physical X-element is required. This is not a proof that such an event obtains.
- **Subsequent candidate:** u∈D; a realized predecessor relation in X must be separately established.
- **Single-operator hypothesis:** Both candidates instantiate one typed relation T. Whether this relation is identical to canonical A, or only a protective-belt extension, remains open.
- **Temporal neutrality:** An event ordering may induce relational time; the definition of T must not contain a physical time parameter.

This B-carrier proposal is a modeling device, not a fourth co-primitive or an assertion of a prephysical substance. Whether it can be eliminated in favor of a nullary/boundary constructor is an explicit open obligation.

## Competing formulations to test

**H0 (canonical-preserving):** A is primitive non-temporal transition; initial actuality is a separate initial condition. Subsequent A-events and the initial condition jointly define Obtains, as in the 2026-11-16 ruling.

**H1 (typed unification):** One event relation admits both boundary-origin and ordinary transition cases without a prior physical state; obtaining remains a separate predicate. Must prove conservative compatibility with the hard core or request a governed amendment.

**H2 (determination primitive):** A is redefined as irreducible determination of actuality; physical transitions are derived. This is a substantive hard-core revision, **not adopted**, requiring explicit reconciliation and owner approval.

## Proof and countermodel obligations

1. Provide a signature and semantics for R, C, D, B, X, T, O, with no physical time or prior actuality smuggled into primitive definitions.
2. Prove or refute that H1 conservatively extends the existing A(s_i,s_j) and initial-condition formulation.
3. Demonstrate that O is not trivially equivalent to T by stipulation; identify the independent condition that distinguishes a candidate event from an obtaining event.
4. Establish whether a boundary carrier is dispensable, and whether its inclusion introduces an unacknowledged fourth primitive.
5. Construct countermodels for circularity, regress, empty actuality, self-transition, cycles, and multiple incompatible outcomes.
6. Respect the charter's actualized A-event typing, partial-order, discrete covariance, and locally finite commitments, and distinguish hard-core neutrality from charter-specific single-outcome growth.
7. Preserve L3 necessity without asserting L3 sufficiency for D.
8. Distinguish primitive A from the physics action functional S.
9. Identify any genuinely new derivation, restriction, or falsifiable prediction. Merely redescribing the initial condition is insufficient.

## Acceptance gates

- Adversarial comparison of H0/H1/H2 with explicit dispositions.
- Lean or equivalent typed formalization and countermodels, where executable.
- Traceability updates only after semantic reconciliation.
- Repository lint, traceability and formalization checks pass.
- Any canonical change requires a separate governed decision and review.

## Initial disposition

**Provisional recommendation:** Investigate H1 first, retain H0 as the governing baseline, and defer H2. No theorem or empirical result is claimed.
