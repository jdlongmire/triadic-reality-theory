# Session note: reconciliation map rulings (2026-11-16)

**Programme lead:** JD Longmire (owner rulings)
**Source document:** `reviews/2026-11-reconciliation-map/reconciliation-map.md` (filed this date; originally PR #34, archived at tag `archive/review/reconciliation-map-2026-11-16` during the 2026-11-16 branch consolidation, and filed on main with these rulings)
**Disposition:** On 2026-11-16 the programme lead accepted the recommended disposition for every ruling the map requested (its sections 10 and A.6). Ruling 14 (branch hygiene) was resolved by the branch consolidation itself. This note is the record; the conforming changes are listed in section 3.

## 1. The rulings as adopted

1. **PRD-001 status.** The decoherence form of the Co-Admissibility Conjecture carries the status "recorded negative for tested forms." Executed in the registry as `epistemic_status: refuted_by_redescription`, the schema value the claim's own 2026-06-26 Attempt 4 note requested; the schema and the build ordering were extended to carry it.
2. **Failure condition 1.** Replaced. The charter's first failure condition now points at the Record-Threshold Conjecture (new claim PRD-004), an exposed falsifier at D to X, with the June negative cited as PRD-001's recorded result. PRD-004 is entered at conjectural status with "N* underived" on its face.
3. **Precedence.** The charter (2026-11-09) governs over the FLL governing objective (2026-08-29). The FLL falsifier (an irreducibly non-bivalent physical informational actualization, per `0-program-methods/TRT-FLL-PHYSICAL-MODEL.md` section 5) is added to the charter's failure conditions as condition 4.
4. **A-event typing.** The map's section 4 typing is accepted as working typing: an A-event is a pair (d, d') with A(d, d') and Obtains(d'); X is the set of A-events; the order on X is supplied by the condition-of-actualization relation. Entered dependent on rulings 5 and 11.
5. **EPA and TC.** Exclusion of Prior Actuality and Transitivity of Conditioning are accepted as explicit axioms toward obligation (e), each recorded in claim ACT-002 and labelled as axioms, not derivations. TC is named as the operative premise of the acyclicity result. Local finiteness remains a posit (claim PHY-001).
6. **LCP.** Logical Closure of Preclusion is accepted as the bridge principle for obligation (d'), recorded as a new premise in claim LOG-003. Persistence of Zero (claim QM-002) is recorded as reducing to LCP; it is not claimed to follow from L3 and A alone.
7. **Gravity substrate.** The A-order is the substrate of record. WP-TRT-GRAV-0001's finite graph stands as a toy computation that owes an explicit bridge to the A-order, and the linearity crux is reposed as whether the L3-natural measure on a causal set has the Benincasa-Dowker continuum limit. See the substrate ruling note in the GRAV-0001 package.
8. **Registry.** Claim entries are authorized and created for the charter commitments the map's section 5 listed as unregistered: discreteness and local finiteness (PHY-001), order selection (ACT-002), redundancy selection (ACT-003), the Tsirelson obligation (QM-001), Persistence of Zero (QM-002), and the source commitment (INT-001).
9. **QSA typing.** `Inst(sigma)` is a status inside D. Any actuality language in WP-TRT-QSA-0001 routes through A-events. See the typing ruling note in the QSA-0001 package.
10. **Working notes.** Section 7 of the reconciliation map stands in for the absent `TRT-working-notes.md` as a labelled reconstruction. The charter's working-notes references are repointed to it by the charter amendment record of this date. The reconstruction is never cited as the owner's notes.
11. **A and Obtains.** The occurrent reading is adopted, under the wording discipline of the 2026-11-12 ruling: A's definition is unchanged (fundamental non-temporal state transition/change, not defined as actualization); in the actualized algebra, A(d, d') holds where the transition occurs, and Obtains(d') is definable as being the target of an A-event, together with an initial condition. The primitive count stays at three.
12. **Levels.** Confirmed: single-outcome and growth are charter-level commitments; the hard core stays neutral, per FD-0001 and CM-01. The charter amendment records the discrete general covariance note: birth order carries no physical meaning beyond the partial order.
13. **Name.** "Constrained actualization" is adopted as the technical term, per FD-0001 Gate 1, placed as a programme commitment adjacent to the hard core with no empirical content claimed for it. "Flexible determinism" is retained only as the historical name of WP-TRT-FD-0001.
14. **Branch hygiene.** Resolved by the 2026-11-16 consolidation: PRs #15 and #19 merged as historical record, PR #16 closed as superseded, the Godel branch archived and deleted. No further action.

## 2. What these rulings do not do

- No hard-core text, definition, confidence label, or proof status is changed except as listed in section 3. The charter's filed text above its amendment records is untouched.
- Strong positivity has no argument from the triad yet (map section 8). No ruling here supplies one, and the circular route through contingent Hilbert structure remains barred by failure condition 3.
- PRD-004's threshold N* is underived. The rulings expose the conjecture; they do not establish it.

## 3. Execution map

| Ruling | Where executed |
|---|---|
| 1 | `traceability/claims/PRD-001.yaml`; `traceability/schemas/claim.schema.yaml`; `traceability/scripts/build.py` |
| 2, 3, 10, 11, 12 | Charter amendment record (2026-11-16) in `0-program-methods/TRT-charter.md` |
| 4, 11 | Charter amendment record; conforming note in `1-hypothesis/hard-core.md`; claims ACT-002, PHY-001 |
| 5 | Claim ACT-002 |
| 6 | Claims LOG-003, QM-002 |
| 7 | `05-work-packages/WP-TRT-GRAV-0001-linearity-crux/substrate-ruling-2026-11-16.md`; claim PHY-001 |
| 8 | Claims PHY-001, ACT-002, ACT-003, QM-001, QM-002, INT-001 |
| 9 | `05-work-packages/WP-TRT-QSA-0001-quantum-state-selection-determinate-actuality/inst-typing-ruling-2026-11-16.md` |
| 13 | Charter amendment record; this note |
| All | Generated traceability reports regenerated by `traceability/scripts/build.py` |

Human-Curated, AI-Enabled (HCAE)
