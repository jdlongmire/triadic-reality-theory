# Global FLL Closure Witness

> **Tier:** 2-theory candidate bridge. **Status:** derived witness form; physical instantiation
> and rival likelihood remain open. **Claim:** `OPN-009`. **Provenance:** Stage 2 of
> [`WP-TRT-LCC-0001`](../../05-work-packages/WP-TRT-LCC-0001-logical-constraint-closure/package.yaml).

## Correction to the first-pass disposition

The first pass required genuine nonactualization to supply an ordinary positive detector outcome.
That requirement was too strong. A meta-record can actualize while reporting that the target
proposition has no bivalent outcome. Experiments routinely infer a latent physical property from
a structured pattern of actual records; the target property need not itself be another detector
label.

The correct question is therefore not “can nothing be recorded?” It is:

> After a context has physically closed, do all independent records admit one coherent valuation
> satisfying Identity, Non-Contradiction, and Excluded Middle?

## What the three laws constrain

Fix one completed context, one event token $e$, and one well-formed outcome proposition $P(e)$.
The same-time/same-respect qualifications are part of the proposition identity.

1. **Identity:** every fragment's $P_j$ refers to the same $P(e)$ under the preregistered event and
   context map. Without this, apparent disagreement may be equivocation.
2. **Non-Contradiction:** $P(e)$ and $\neg P(e)$ are not both outcome-actual.
3. **Excluded Middle:** $P(e)$ or $\neg P(e)$ is outcome-actual.

Together the last two restrict a closed binary context to exactly one of two valuations:

| Latent valuation | $v(P)$ | $v(\neg P)$ | Classical status |
|---|---:|---:|---|
| true | 1 | 0 | admissible |
| false | 0 | 1 | admissible |
| glut | 1 | 1 | forbidden by Non-Contradiction |
| gap | 0 | 0 | forbidden by Excluded Middle |

The table makes violations imaginable without making them incoherent as experimental hypotheses.
A rival semantics can include gluts, gaps, or both.

## What existing challenges do—and do not—show

- **Paraconsistent consequence** rejects explosion; by itself it does not assert true physical
  contradictions. **Dialetheism** permits truth-value gluts and is therefore a genuine semantic
  rival to Non-Contradiction.
- **Paracomplete and intuitionistic logics** withhold unrestricted Excluded Middle, but a proof gap
  is not automatically a physical outcome gap. A physical rival must connect its semantics to
  record probabilities.
- **Paraconsistent readings of quantum superposition** show that a contradiction-tolerant
  interpretation can be formally developed. Existing proposals explicitly present themselves as
  interpretive first steps, not distinct laboratory likelihood models.
- **Kochen–Specker/contextuality inequalities** prove that quantum statistics do not admit certain
  joint, context-independent valuations over multiple measurement contexts. They do not show that
  Identity, Non-Contradiction, or Excluded Middle fails for the outcome inside one completed
  context. They supply the relevant technique—derive a correlation polytope and a separating
  inequality—not the result.

This boundary is load-bearing. “Global FLL” here means globally operative in actuality, not one
counterfactual value assigned simultaneously to every incompatible observable.

## Dual-affirmation record architecture

For each independent record fragment $j=1,\ldots,R$, implement two separately calibrated binary
reports:

$$
Y_j=(Y_j^P,Y_j^{\neg P})\in\{00,01,10,11\}.
$$

These are affirmative digitized reports, not missing data:

- `10`: fragment supports $P$ only;
- `01`: fragment supports $\neg P$ only;
- `11`: fragment reports a glut;
- `00`: fragment reports a gap.

The architecture need not use two destructive measurements of the original qubit. Each fragment
may be a separately accessed environmental or ancilla record established by the measurement
interaction. What matters is a preregistered operational equivalence between the two report families
and the propositions they claim to witness.

## Error-bounded forbidden-correlation inequality

Assume the global closed-context model has a latent bivalent value $G\in\{T,F\}$. Calibrate each
fragment's conditional probabilities $q_j(y\mid G)$ on known `0` and `1` preparations. Define the
coherent gap and glut events:

$$
E_{\mathrm{gap}}=\{Y_1=\cdots=Y_R=00\},\qquad
E_{\mathrm{glut}}=\{Y_1=\cdots=Y_R=11\}.
$$

Under conditional independence of the fragments given $G$,

$$
p_{\mathrm{gap}}
\leq
\max_{g\in\{T,F\}}\prod_{j=1}^{R}q_j(00\mid g),
$$

$$
p_{\mathrm{glut}}
\leq
\max_{g\in\{T,F\}}\prod_{j=1}^{R}q_j(11\mid g).
$$

Therefore the global-FLL closure model obeys

$$
\boxed{
p_{\mathrm{gap}}+p_{\mathrm{glut}}
\leq B_{\mathrm{FLL}}
}
$$

with

$$
B_{\mathrm{FLL}}=
\max_g\prod_j q_j(00\mid g)
+
\max_g\prod_j q_j(11\mid g).
$$

For a symmetric per-fragment bound $q_j(00\mid g),q_j(11\mid g)\leq\epsilon$,
$B_{\mathrm{FLL}}\leq2\epsilon^R$.

An observed excess over this calibrated bound is a positive, countable discriminator. It rejects
the conjunction of:

1. context identity and closure;
2. a global bivalent latent outcome;
3. the calibrated response model; and
4. the stated conditional-independence structure.

That is a legitimate severe-test shape. It is not yet uniquely a falsification of FLL because the
instrument and independence assumptions remain alternative failure points.

## Why redundancy no longer contradicts the candidate event

The first pass assumed redundancy meant several copies of `0` or `1`. Here redundancy means several
independent fragments agree on the **valuation status**. A coherent `00...00` pattern is redundant
evidence of a gap; `11...11` is redundant evidence of a glut. Thus the closure condition and the
candidate event can be jointly satisfiable at the record level.

The distinction also makes anomalies structured. Independent random failures shrink approximately
as $\epsilon^R$; a global gap/glut source produces correlated forbidden reports. Shared amplifiers,
clocks, firmware, preparation errors, and common environments defeat that scaling and must either be
physically separated or included in a calibrated joint bound.

## Candidate circuit-level instantiation

A stronger implementation than splitting one amplifier output is possible in principle. For each
fragment $j$, prepare a one-hot ancilla pair $A_j^P,A_j^{\neg P}$ and coherently map the target's
binary $Z$ alternatives as

$$
|0\rangle|00\rangle_j\mapsto|0\rangle|10\rangle_j,
\qquad
|1\rangle|00\rangle_j\mapsto|1\rangle|01\rangle_j.
$$

Repeat onto $R$ separately read ancilla pairs before digitization. Orthogonal pointer information
can be copied redundantly; this is not cloning an arbitrary unknown state. Each pair then yields an
actual two-bit meta-record. Separate resonators, amplification paths, clocks where practicable, and
blind classification reduce downstream common modes.

This architecture does not solve the problem by itself:

- target leakage can produce correlated `00` across every pair;
- a faulty common mapping pulse can produce correlated gaps or gluts;
- the ancilla interaction helps create the very closure it is intended to witness;
- testing residual coherence on the same trial is destructive, so $C_D$ needs a preregistered
  matched-cohort or nondemolition estimator; and
- standard quantum mechanics predicts one-hot results too, so the experiment still lacks a rival
  positive violation rate.

The real null bound must therefore be the maximum coherent-gap/glut probability over a calibrated
causal error model, not automatically $2\epsilon^R$. The symmetric formula remains a transparent
reference case and a negative control for the analysis code.

### Independence-free joint calibration

The fragment-independence assumption can be removed from the statistical bound. On matched control
preparations with known latent values $g\in\{T,F\}$, calibrate the **complete joint events**
$00^R$ and $11^R$ directly. Let $U_{g,\mathrm{gap}}$ and $U_{g,\mathrm{glut}}$ be simultaneous
one-sided upper confidence bounds on those four Bernoulli rates. Then

$$
B_{\mathrm{joint}}
=
\max_g U_{g,\mathrm{gap}}
+
\max_g U_{g,\mathrm{glut}}
$$

is valid without factorizing the fragment responses. The reference code implements exact one-sided
Clopper–Pearson limits with Bonferroni allocation across the four calibration rates. This incorporates
observed common-mode failures into the null instead of suppressing them artificially by
$\epsilon^R$.

The price is substantial:

- rare-event calibration requires very large control samples;
- the bound may be too loose to yield useful power;
- controls must match the measurement strength, timing, leakage population, and closure regime of
  science trials; and
- an unmodeled distribution shift between calibration and science trials remains a rival
  explanation.

The direct joint bound is the default for any real protocol. The factorized bound is admissible only
after a causal argument and intervention tests establish the claimed conditional independence.

## Current epistemic status

**Derived:** an explicit observable and inequality can be written. The claim that no discriminator
exists was wrong.

**Not derived:** that a transmon implementation can realize proposition-dual, causally independent
record fragments; that $C_L$ entails the required context identity; or that any developed rival
logic predicts a nonzero excess. Standard quantum measurement is expected to satisfy the same bound.

Accordingly this remains tier 2. Promotion to tier 3 requires a concrete instrument model, a
joint-error calibration protocol, and at least one rival physical model with a different predicted
distribution—not merely a different vocabulary for the same Born statistics.

## Primary sources

- N. C. A. da Costa and C. de Ronde, “The Paraconsistent Logic of Quantum Superpositions,”
  arXiv:1306.3121 (2013).
- R. W. Spekkens, “Contextuality for preparations, transformations, and unsharp measurements,”
  *Physical Review A* 71, 052108 (2005), DOI 10.1103/PhysRevA.71.052108.
- A. A. Klyachko et al., “Simple Test for Hidden Variables in Spin-1 Systems,” *Physical Review
  Letters* 101, 020403 (2008), DOI 10.1103/PhysRevLett.101.020403.
- M. Kleinmann et al., “Optimal inequalities for state-independent contextuality,” *Physical
  Review Letters* 109, 250402 (2012), DOI 10.1103/PhysRevLett.109.250402.
- M. D. Mazurek et al., “An experimental test of noncontextuality without unphysical
  idealizations,” *Nature Communications* 7, 11780 (2016), DOI 10.1038/ncomms11780.
