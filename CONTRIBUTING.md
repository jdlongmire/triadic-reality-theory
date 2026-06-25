# Contributing

TRT is a foundational-ontology research programme with a defined path toward physics-level results. It is led by an independent researcher and is genuinely open to falsification. **The project's credibility rests on maintaining honest confidence labels and stated failure conditions. Contributions are evaluated first against whether they preserve that discipline.**

The governing standard is the [Popper/Lakatos methodology](0-program-methods/METHODOLOGY.md): a contribution is accepted if it is a **progressive problemshift** and declined if it is a **degenerating** one.

## What counts as progressive (welcome)

In rough order of current need:

1. **Formalization of co-admissibility (Task 0.1)** — the gating problem. Mathematical contributions that make the criterion definite, computable, and measure-free are the highest priority. A contribution that demonstrates co-admissibility *cannot* be formalized without a free measure is **equally valuable** — it settles the matter in the negative and is a recorded result.
2. **Computational tests (Task 1.1)** — once 0.1 exists, code computing the prediction for the incompatible-channel case against the known critical coupling.
3. **Critical review** — adversarial reading that finds errors, circularities, or overclaims. Archived in [`reviews/`](reviews/) with responses. A review that forces a confidence label downward or compels a retraction is a *successful* contribution.
4. **Reference verification** — checking citations against primaries and updating [`references/verification-status.md`](references/verification-status.md).
5. **Recovery proofs (Tier 4)** — demonstrations that TRT structures recover known physics in appropriate limits.
6. **Lean formalization** — extending [`formalization/`](formalization/) and wiring claims through [`traceability/`](traceability/).

## Standards every contribution must meet

- **State confidence.** Every claim carries a label: HIGH / MEDIUM / LOW / UNCERTAIN (traceability enum: `established` / `argued` / `conjectured` / `open`).
- **State failure conditions.** Every proposed result specifies what would falsify it (`risk_if_false`; for predictions, `falsifies`).
- **No circularity.** Derivations include a dependency-graph check; the graph must be acyclic. Parametric, definitional, and validation circularity are disqualifying (paper §3.4, §9.2).
- **Primary sources.** Cite primaries, not secondary characterizations. Use "as cited in" when primary access is unavailable, and flag for verification.
- **Distinguish interpretation from derivation.** A re-description of known physics in TRT's terms is *interpretation*, not result. Do not present the former as the latter — that is the canonical degenerating move.
- **Traceability.** New claims get a `traceability/claims/` entry conforming to the [schema](traceability/schemas/claim.schema.yaml).

## What will be declined (degenerating)

Contributions that inflate confidence, remove failure conditions, present interpretation as derivation, or treat the metaphysical commitments as established physics will be declined **regardless of technical quality**. The discipline is the asset.

## License of contributions

By contributing you agree that prose is licensed CC BY 4.0 and code/formal artifacts Apache 2.0, consistent with the repository [license](README.md#license).
