# Response — GPT review (2026-06-26)

Reviewed: [`review.md`](review.md). **Disposition:** accepted as a high-quality, *confirming* review. It moves no confidence label downward — it independently corroborates the programme's own self-assessment (unappraised; co-admissibility is the gating root). Under the [methodology](../../0-program-methods/METHODOLOGY.md) it is a successful contribution: it sharpens the review-ask and prompts four concrete improvements, three of which are actioned here.

## Point-by-point

**1. "Create a Reviewer Entry Point document" — ACCEPTED, done.**
Created [`../REVIEWER-ENTRY-POINT.md`](../REVIEWER-ENTRY-POINT.md): states that TRT is not yet a physical theory, names the thesis and four-tier engine, identifies co-admissibility (Task 0.1) as the gating task, names the incompatible-channel severe test, and gives the single narrow falsification ask. This directly implements the reviewer's "force the critique onto the root node."

**2. "Move/rephrase the working-draft status note" — PARTIALLY ACCEPTED, tracked (JD's call).**
The point is fair: a prominent "prose/refs unverified" banner makes the public master read as unfinished. But *removing* the honesty note risks the opposite failure — looking like we hid the draft status. Recommended middle path: rephrase the note to a concise **stable-v0.9-preprint** version line plus a pointer to `references/verification-status.md`, rather than delete it. Note also that the [deposit gate](../../0-program-methods/ops/zenodo-publishing.md) already cuts a *stripped* `TRT-v1.0-public.md` for circulation, so this concerns only the GitHub-public v0.9 master. Because the paper is the hard-core master, the exact wording is JD's call — **tracked as an issue.**

**3. "Treat Task 0.1 as the next full project; stop expanding exposition" — ACCEPTED, already our posture.**
This is the ROADMAP's own position and PI-1's critical path (O3 = issue #5). The review independently confirming the critical path *strengthens* the case for not diluting effort into more prose. No change beyond executing O3.

**4. "Change CITATION.cff type from software" — ACCEPTED, done.**
Added a `preferred-citation` of type `article` (the position paper) so citers cite the scholarly object; kept the top-level `type: software` because CFF 1.2 restricts the top-level type to `software`/`dataset` and the repo does carry Lean + Python artifacts. This gives the correct citation without misusing the schema.

## Strategic input accepted

**"The decoherence/channel test is the better near-term credibility path than gravity."** Agreed, with independent grounding: both branches gate on Task 0.1, but once the criterion exists, the incompatible-channel test (Task 1.1) compares against an *analytically known* critical coupling — a cleaner, harder-to-dismiss credibility win than the gravity fork, which a critic can read as overreach until the finite-graph test is precise. **Effect:** within PI-1, prefer **0.1 → 1.1 (decoherence)** before pressing O4 (gravity linearity). Recorded here and in the next PI review; the appraisal's candidate novel facts already rank the cavity-field test first.

## One thing the review did not weigh (noted, not a defect)

The review assesses *physics* credibility and rightly makes it hinge on co-admissibility. It does not engage the programme's distinct *philosophical* claim — that the hard core's logical constituent is immune **by transcendental necessity**, not convention (METHODOLOGY §"hard core is immune by necessity"). That claim stands or falls independently of the physics branch and is not touched by the co-admissibility question.

## Net changes from this review

- Added `reviews/REVIEWER-ENTRY-POINT.md` (narrow review-ask).
- Fixed `CITATION.cff` (added `preferred-citation`).
- Opened an issue for the status-note rephrase decision.
- Logged the review in `3-prediction/appraisal.md` and `reviews/README.md`.
- No confidence labels changed (review is confirming, not refuting).
