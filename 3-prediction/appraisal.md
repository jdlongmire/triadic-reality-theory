# Programme Appraisal (Progressive vs Degenerating)

> The Lakatosian self-audit. A research programme is **progressive** if it predicts novel facts and some corroborate; **degenerating** if it only accommodates facts post hoc with ad hoc adjustments. This file is the standing answer to: *which is TRT, right now?*

## Current verdict (TRT v0.9)

**Unappraised.** TRT is a research programme in the literal Lakatosian sense — an articulated hard core, an articulated positive heuristic (the [ROADMAP](../0-program-methods/ROADMAP.md)), and *named* potential novel facts — but **no corroborated novel fact yet.** By the programme's own standard it is not yet doing physics; it is positioned to.

This is not a deficiency to hide. It is the honest status, and naming it correctly is the discipline that the [methodology](../0-program-methods/METHODOLOGY.md) exists to protect.

## What would move the needle to *progressive*

A corroborated novel fact from one of the discriminating descendants:

| Candidate novel fact | Source | Gate |
|---|---|---|
| Measure-independent pointer selection matching the cavity-field critical coupling | [co-admissibility conjecture](co-admissibility-conjecture.md) | Task 0.1 formalization |
| Presence/absence of higher-curvature corrections, tied to linear-vs-quadratic | [gravity linearity test](gravity-linearity-test.md) | Task 0.1 + keystone |

A *theoretically* progressive step (a formalized criterion that predicts a novel fact) precedes an *empirically* progressive one (the fact corroborates). The retrodiction of the [effectiveness of mathematics](effectiveness-of-mathematics.md) is supporting weight, not a novel-fact corroboration.

## What would mark *degeneration* (to be recorded as plainly as success)

- The co-admissibility criterion, once formalized, reduces to the einselection optimization and predicts nothing new.
- The gravity measure is quadratic with no logical motivation for linearity, and the program quietly re-labels rather than recording the downgrade.
- Any confidence label inflated, or any failure condition removed, to preserve a claim — the [contribution criterion](../CONTRIBUTING.md) declines exactly this.

## Log

| Date | Event | Effect on appraisal |
|---|---|---|
| 2026-06 | v0.9 position paper + program stood up; two conjectures named, neither formalized | Unappraised (baseline) |
| 2026-06-26 | External review (GPT) — [`reviews/2026-06-gpt/`](../reviews/2026-06-gpt/). Confirms unappraised status; co-admissibility is the gating root; decoherence test is the better near-term credibility path | No change (confirming, not refuting) |
| 2026-06-26 | Agent-roster pass on Task 0.1 ([`reviews/2026-06-redteam-coadmissibility/`](../reviews/2026-06-redteam-coadmissibility/)). Measure-free criterion C0 (= Lindbladian kernel) constructed but degenerates in the discriminating regime; reduces to one open commutant computation; OPN-001 → prose_only, stays open | Progressive *theoretical* step (sharper falsifier). Still **Unappraised** — no corroborated novel fact |
| 2026-06-26 | **Decisive computation** on Task 0.1 ([code](co-admissibility-conjecture/code/coadmissibility_commutant.py); [Attempt 2](../2-theory/00-foundational/co-admissibility-formalization.md)). On the verified Feller model all three tested measure-free criteria are NON-discriminating: commutant trivial (no DFS), pointers in the complement, pairwise-commuting set = whole space (reproduces Feller Eq.17). Recorded **negative** for the tested criteria; diagnosis = the tested objects are rate-independent but the target is rate-governed. Scope bounded (design space not exhausted; one rate-dependent candidate also failed) | Progressive *theoretical* step (a recorded negative, honestly labeled, with a where-to-look-next diagnosis) — but it **pressures the decoherence route toward the degeneration watch**: PRD-001 loses discriminating content for the forms tried. Still **Unappraised** — a negative on candidates is not a corroborated novel fact |
