# Sub-route: Sheaf-Cohomological Probe of the Keystone (OPN-002)

> **Tier:** 2-theory (protective belt). **Parent:** [`actualization-resolution.md`](actualization-resolution.md) (OPN-002, the keystone). **Lakatos role:** a candidate *formal vehicle* for sub-route 1 ("define *A*'s resolution operation; if projective, determine the norm and whether it is forced or imposed"). **Confidence this resolves OPN-002:** LOW. **Confidence this is the right corner of category theory to try:** MEDIUM. The deliverable sought is a *sharper falsifier*, not a result.

## Origin

External proposal (Grok, 2026-06; triaged at [`../../reviews/2026-06-grok/`](../../reviews/2026-06-grok/)) recommended a categorical formalization of TRT — dagger symmetric monoidal category, decoherence as an idempotent monad, ZX/ZH calculus. That package is **declined** as a program (it re-skins the v0.9 hard core and its centerpiece — decoherence as a structure-preserving idempotent — is the route PRD-001 already recorded NEGATIVE as re-description). One graft was extracted: the sub-route below.

## The thesis

The keystone fork has a clean cohomological shape, and that shape distinguishes the two horns natively:

| *A*'s resolution | Cohomological reading | Metric? | Horn |
|---|---|---|---|
| **Obstruction-registering** | the relational structure admits no global section; *A* registers the **obstruction class** itself (the cohomology element) | **none** — uses only the relational/group structure | linear → GR |
| **Best-fit projective** | no global section exists; *A* selects the **nearest** approximate section by minimizing a residual | **required** — needs an inner product on the value space to define "nearest" | quadratic → modified gravity |

This is not a metaphor. "Register the obstruction to a global section" vs. "project onto the nearest global section" is a real and standard mathematical distinction (roughly: compute a cohomology class vs. solve a least-squares problem). It maps onto TRT's linear-vs-quadratic fork because the *metric-dependence* is the discriminating variable in both — exactly the variable [`actualization-resolution.md`](actualization-resolution.md) names ("requires an inner product on the value space and a minimization").

**Precedent.** Abramsky & Brandenburger (2011), *The Sheaf-Theoretic Structure of Non-Locality and Contextuality* — contextuality/non-locality as a cohomological **obstruction** to a global section of a presheaf over measurement contexts. (Confidence MEDIUM-HIGH that this is the result and framing; **verify against the primary before building on it** — see [verification-status](../../references/verification-status.md).) This is the rare corner of categorical foundations with discriminating track record: an obstruction class is a genuine invariant, not a relabeling. That is precisely why it is a candidate here and the dagger-compact/ZX toolkit is not.

## Construction (over the existing test object — no new toy)

Reuse the relational structure already in hand ([`../03-gravity/relational-graph-test.md`](../03-gravity/relational-graph-test.md); the Feller cavity setup), to keep continuity and avoid a fresh model whose result would not transfer.

1. **Presheaf.** Over the poset of sub-contexts of the relational structure, take the presheaf whose sections over a context are the locally *L₃*-admissible assignments on that context.
2. **Global section = co-admissibility.** A jointly *L₃*-admissible (co-admissible) assignment is a global section. Co-admissibility *failure* = no global section = a nonzero obstruction.
3. **The keystone question, restated.** Is the object *A* delivers the **obstruction class** of (2) — read off the relational/group structure with no norm (horn a) — or a **best-fit global section** that minimizes a residual under a chosen norm (horn b)?

## Discriminating outcomes (what each result buys)

- **(a) succeeds** — the resolution is faithfully expressed as obstruction-class registration, metric-free: formalizes horn (a), supports linear → exact GR. A *theoretically progressive* step.
- **(b) forced** — every faithful expression requires choosing a norm to define "nearest": horn (b), quadratic → modified gravity, **and** the norm is *imposed, not derived* — which fires the `risk_if_false` failure condition in [`actualization-resolution.md`](actualization-resolution.md). Recorded as a downgrade, plainly.
- **Neither expressible** — the relevant obstruction always trivializes, or cohomology is the wrong invariant for these structures: informative *negative*, pressures toward (b), bounds the design space. Still progress (a sharper falsifier).

## The principal hazard — why this can also collapse to re-description

The Abramsky-Brandenburger machinery is standardly built over **distributions** (a presheaf of probability measures), which *presupposes a measure*. Naively applied, it smuggles the quadratic/metric structure back in through the back door and the sub-route degenerates exactly as PRD-001 did. **The discipline that keeps horn (a) genuinely metric-free:** work at the **possibilistic** (support-only) layer of the sheaf — the relational/order structure of *which* assignments are admissible — not the probabilistic layer. The possibilistic obstruction is metric-free; the probabilistic one is not. If the obstruction can only be made discriminating at the probabilistic layer, that *is* a result: it means the metric is doing the work (horn b).

A second hazard, flagged by the prior cross-sector red-team ([`../../reviews/2026-06-redteam-gravity/`](../../reviews/2026-06-redteam-gravity/)): assert **shared *A***, not shared *value space*, between the quantum and gravity sectors. The presheaf construction must not quietly identify the two sectors' value spaces; doing so would repeat the smuggling the red-team already caught.

## Correction logged (ZX → sheaf)

A prior session-level suggestion to use **ZX-calculus** as the keystone probe is **withdrawn**. ZX is a dagger-compact calculus — it bakes in the inner product, so it natively expresses only the *quadratic/projective* horn and cannot neutrally represent the metric-free *linear* horn. It is the wrong corner of category theory for this fork. Sheaf cohomology (possibilistic layer) is the right one because it can carry the obstruction class without a norm. This correction is the whole reason the graft is sheaf-theoretic rather than diagrammatic-quantum.

## Status and priority

- **Priority:** BELOW the live commutant/gravity work (Task 0.1, OPN-001; the gravity descendant PRD-002). This is an *optional* formal vehicle for sub-route 1 of the keystone, not a new critical path. It does not gate, and is not gated by, the active work beyond its shared dependence on OPN-001.
- **Failure condition:** if the possibilistic obstruction is non-discriminating on the test structure (trivializes, or only discriminates once a measure is reintroduced), record NEGATIVE for the sheaf vehicle and the keystone fork stays open by other means.
- **First concrete step before any build:** verify Abramsky-Brandenburger (2011) against the primary, and confirm the possibilistic-layer obstruction is well-defined on the Feller relational structure. Cheap; do it first.
