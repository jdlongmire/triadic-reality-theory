# Research Practices

Best-practice disciplines the programme commits to, beyond the [Popper/Lakatos methodology](METHODOLOGY.md). These are the *how-we-work* norms that keep the programme honest as it scales.

## 1. Preregistration of predictions

State the prediction *and its failure condition* **before** computing it. The [co-admissibility](../3-prediction/co-admissibility-conjecture.md) and [gravity](../3-prediction/gravity-linearity-test.md) conjectures already carry their `falsifies` conditions; no result is reported without the refutation condition having been fixed in advance. This forecloses the post-hoc accommodation that marks a degenerating programme.

## 2. Interpretation vs derivation — the standing demarcation

A re-description of known physics in TRT's terms is **interpretation**; a claim that forbids something new is a candidate **derivation/prediction**. Every result is tagged as one or the other. Presenting interpretation as derivation is the canonical degenerating move and is rejected in review.

## 3. Confidence labelling

Every claim carries a label — **HIGH · MEDIUM · LOW · UNCERTAIN** in prose; the traceability enum `established / argued / conjectured / open`. Labels move *down* freely on evidence and *up* only on earned grounds. A label inflated without grounding is a review-blocking defect.

## 4. Primary-source discipline

Cite primaries, not secondary characterisations. Use "as cited in" when primary access is unavailable, and flag for verification. Verification state is tracked per reference in [`../references/verification-status.md`](../references/verification-status.md); no downstream work builds on an unverified citation.

## 5. Reproducibility

Computational results ship with their code (`3-prediction/<test>/code/`) and a stated environment; formal results ship as Lean that builds green under the pinned toolchain. A result that cannot be reproduced is not yet a result. The traceability `formal_artifacts` field links each claim to its Lean symbol or computational notebook with a status (`proven`/`reproduces`/`pending`).

## 6. Circularity audit

Mandatory for proofs, derivations, and any parameter claimed as "derived". Trace the dependency graph (must be acyclic — enforced by CI), audit definitions for self-reference, confirm no "derived" value was fitted to the outcome it explains. The standard is paper §3.4 and §9.2.

## 7. Adversarial review is a contribution

A review that forces a confidence label down, exposes a circularity, or compels a retraction is *successful* and is archived in [`../reviews/`](../reviews/) with a response. The programme's credibility is the discipline, not the optimism.

## 8. Honest status at all times

The [appraisal log](../3-prediction/appraisal.md) records, standingly, whether the programme is progressive, degenerating, or (currently) unappraised. The status is never rounded up.

## 9. GitHub-safe LaTeX

Math must render on the publishing surface (GitHub) and in strict KaTeX viewers, not only in a local engine. Rules:

- **Operator names:** use `\mathrm{Name}`, not `\operatorname{Name}` — the latter is rejected by GitHub/strict-KaTeX math ("macros are not allowed: operatorname"); `\mathrm` renders identically and is universal. (See [issue #7](https://github.com/jdlongmire/triadic-reality-theory/issues/7).)
- **Absolute values / norms in inline math inside tables:** use `\lvert … \rvert`, not bare `|` — kramdown reads `|` as a table delimiter. (Bare `|` is fine in `$$` display blocks, e.g. kets `|\psi\rangle`.)
- **No definition macros** (`\def`, `\newcommand`, `\gdef`, `\let`), `\href`, `\label`, or `\tag` in committed math — GitHub's renderer blocks them.
- Sanity check: `grep -rn '\\operatorname' --include="*.md" .` should return nothing.
