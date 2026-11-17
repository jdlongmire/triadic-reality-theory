# Session note, 2026-11-12: next-steps plan adopted; four work packages filed

## Occasion

The 2026-11-12 arc (Pages audit fix, external review and response, charter and hard-core reconciliation, LOG-001 conformance, Pages EM-scope conformance, CPIT Lean formalization, ONT-002 and ONT-004 proof status; PRs #26 to #32) closed the programme's consistency work. JD directed that next steps be planned and captured, with appropriate work packages put in place. A next-steps plan was drafted (inventory of the 14 existing packages in 05-work-packages/, dispositions for six candidate items), and JD approved the plan and the filing of its four new packages on 2026-11-12. This note records the adoption. The filing is made by pull request for JD's word.

## The four new packages

- WP-TRT-CORE-0002, "Test whether primitive A can be eliminated without explanatory loss" (status: proposed). Successor to WP-TRT-CORE-0001, which closed complete with the A reduction as an open challenge. Runs the elimination test: the representation/efficacy distinction made rigorous, the strongest elimination of A constructed, and a loss audit. Gates any move of ONT-002 and ONT-004 epistemic status beyond argued.
- WP-TRT-GRAV-0001, "Resolve the linearity crux for the co-admissibility measure on a finite relational graph" (status: proposed). ROADMAP Task 3.1, the gravity arm of Task 0.1 (OPN-001, OPN-002). The question was fully posed in the corpus but owned by no package. Highest-leverage physics-facing item per the external review filed 2026-11-12 (move 1); the re-description audit is built in as an action, on the decoherence arm's precedent.
- WP-TRT-FORM-0001, "Make every proposed bridge in the formalization either a theorem or a marked open assumption" (status: proposed). Executable form of the external review's move 4: a bridge inventory, a Lean assumptions module, a published axiom-dependency audit, and a sufficiency register for D. Supports CORE-0002 and GRAV-0001; gates nothing.
- WP-TRT-BORN-0001, "Derive the Born measure from constraints on A, or record precisely why it must be postulated" (status: proposed, gated). ROADMAP Tier 2.2, OPN-004. The package carries a gate field: it opens only on WP-TRT-GRAV-0001's keystone disposition on OPN-002 (in particular the stage-2 question, whether projective Born selection is fundamental to A or a stage-2 overlay), and only on the programme lead's ruling. Filing this package does not open it.

## Dispositions for items already covered

- FLL operationalization: already covered by WP-TRT-FLL-0002 (status ready); no new package. Execution next action is the package's own first decision, whether TRT-FLL entails Absoluteness of Observed Events or bivalence indexed to a defined actualization context, then selection of one apparatus-level proposition and completion of all preregistered fields. Independent lane; registry link OPN-009.
- Recovery tier beyond the Born package (Einstein-Hilbert recovery; general recovery in limits, OPN-003; the variational tier, OPN-005): deliberately not packaged. Their prerequisites are unmet; the plan records trigger conditions instead (the linearity disposition for the Einstein-Hilbert item, whose shape depends on the horn; a defined actualization-rate scalar for the rest).
- Housekeeping leftovers from the Pages audit (item D3: the Struver review apparatus says 273 lines where the filed paper.md has 272; item D4: docs/architecture-decision.md is published but orphaned, with no inbound links and its route excluded by the sitemap template's filter): specified in detail and ready to execute as one small PR under WP-TRT-PAGES-0001, pending JD's word. Not part of this filing.
- TRT-working-notes.md: a dependency on JD, not executable programme work. The charter cites it in four places (file header; obligation (b); obligation (d-prime); failure condition 2), via its section 4.5, which carries the falsification record for the gravitational order-difference criterion. The file is absent from the repository. JD is to supply it, or to rule on how the four citations should be handled if it will not be filed.
- The programme response to the external review (reviews/2026-11-external-critical-review/response.md) remains marked DRAFT pending the programme lead's approval. That approval is separate from this plan and is not affected by this filing.

## Recommended sequence, as adopted

1. Housekeeping PR (audit items D3 and D4) whenever JD gives the word.
2. Open WP-TRT-CORE-0002 and WP-TRT-GRAV-0001 in parallel: the irreducibility arc's continuation and the highest-leverage physics-facing item. They share no machinery; neither waits on the other.
3. Execute WP-TRT-FLL-0002 in parallel: already written and ready; its first action is a decision, not drafting.
4. Open WP-TRT-FORM-0001 alongside, or immediately after the first phase of step 2.
5. Hold WP-TRT-BORN-0001 until WP-TRT-GRAV-0001 returns the keystone disposition, then open it on JD's ruling.
6. Draft the Einstein-Hilbert recovery and general recovery packages only when their stated triggers fire.

## Carry to next

- JD's word on this filing (PR for the four packages and this note).
- Opening actions for WP-TRT-CORE-0002 and WP-TRT-GRAV-0001; the WP-TRT-FLL-0002 first decision.
- Housekeeping PR on JD's word; TRT-working-notes.md from JD.

Human-Curated, AI-Enabled (HCAE)
