# Non-Bivalent Rival Model Attempt

> **Tier:** 2-theory negative construction result. **Status:** no contrastive physical rival yet.
> **Claim:** `OPN-009`. **Scope:** strongest minimal extension of a quantum measurement instrument
> with gap and glut labels; not a no-go theorem for every future non-bivalent theory.
> **Governing boundary:** this construction serves the
> [`TRT-FLL Physical Model`](../../0-program-methods/TRT-FLL-PHYSICAL-MODEL.md). The
> representation problem is an instrument for sharpening falsification, not the research objective.

## Question

Can a physically articulated rival assign a nonzero coherent-gap or coherent-glut likelihood to
the [Global Bivalent Closure Witness under FLL](global-bivalent-closure-witness-under-fll.md), while
recovering ordinary quantum measurement when its non-bivalent parameters vanish?

A qualifying model must specify at least:

1. states and their dynamics before the measurement;
2. an instrument coupling states to actual records;
3. normalized probabilities for those records;
4. composition rules sufficient to exclude signalling or contextual relabelling artifacts; and
5. a standard-quantum limit.

Merely assigning semantic values `both` or `neither` does not meet these requirements.

## Strongest minimal construction: a four-valued actualization instrument

Let the target proposition have four candidate valuation labels

$$
\Omega_4=\{T,F,B,N\},
$$

where $B$ denotes both true and false and $N$ denotes neither. Associate each label with a
completely positive, trace-nonincreasing map $\mathcal I_x$. For input state $\rho$,

$$
p_x(\rho)=\mathrm{Tr}[\mathcal I_x(\rho)].
$$

Physical completion requires

$$
\sum_{x\in\Omega_4}\mathcal I_x
\quad\text{to be trace preserving},
\qquad
\sum_{x\in\Omega_4}p_x(\rho)=1.
$$

The record coupling may map $T,F,B,N$ respectively to the meta-records `10`, `01`, `11`, and `00`.
A family with $\mathcal I_B,\mathcal I_N\rightarrow0$ recovers the ordinary binary quantum
instrument, so this is the strongest minimal candidate with a standard-quantum limit and directly
computable witness likelihoods.

## Instrument-completion dichotomy

The construction is mathematically consistent, but it does not yet realize the intended rival.

### Horn 1 — retain normalization

If the four maps form a complete instrument, $B$ and $N$ are members of an exhaustive physical
outcome space. A trial producing `11` or `00` has actualized the outcome $B$ or $N$. The model is an
ordinary four-outcome quantum instrument with suggestive labels. Its probabilities may differ from
a two-outcome instrument, but that difference tests omitted outcomes or instrument physics, not a
failure of bivalent valuation for a completed binary proposition.

This is not changed by calling $B$ a joint truth or $N$ a nonactualization. Operationally, each is
an actual record event. A semantic bridge saying that one actual outcome nevertheless means “both”
or “neither” is additional structure and currently has no independently testable consequence.

### Horn 2 — refuse completion

Suppose a gap is instead represented by trace deficit,

$$
p_T(\rho)+p_F(\rho)<1.
$$

The residual probability is experimentally the probability that neither named binary outcome was
recorded. Completing the apparatus model adds a failure, leakage, loss, or environment outcome with
that residual weight, returning to Horn 1. If no completion is permitted, the rival supplies no
normalized likelihood over complete trials and therefore cannot be compared with the calibrated
witness.

A glut represented by overlapping exclusive effects has the dual problem. If the joint event is
assigned a normalized record label, it is an ordinary refined outcome. If its weights are simply
added to both exclusive alternatives, the proposed alternatives no longer form a probability
measure until a new event algebra and normalization/composition rule are supplied.

## Result

Within completely positive quantum instruments, the candidate has a conditional no-go:

> A gap/glut extension is either a normalized expanded outcome model, in which `00` and `11` are
> actual physical outcomes, or it lacks the complete probability law needed to predict the
> witness. Quantum-instrument mechanics alone cannot make the same event both an actual record and
> an irreducibly non-bivalent valuation of an otherwise completed binary proposition.

This does **not** prove that non-bivalent physics is impossible. It identifies what a genuine rival
must change: not just outcome labels, but the operational event algebra or the link between physical
records and truth-bearing propositions. A generalized probabilistic theory can in principle change
those structures, but it must still define normalized tests and composition. Once `gap` and `glut`
are included as test outcomes, the semantic-bridge problem recurs unless the theory derives a new,
independently measurable consequence.

## Assessment of existing paraconsistent quantum proposals

The examined paraconsistent-superposition programme formalizes contradictory powers in a potential
realm while retaining ordinary quantum predictions for actual measurements. It provides a serious
logical and interpretive rival, but no altered post-closure record distribution for this witness.
It therefore supplies logical possibility, not $P(00^R\mid H_{\mathrm{rival}})$ or
$P(11^R\mid H_{\mathrm{rival}})$.

## Change-the-verdict conditions

`OPN-009` can advance beyond this negative result if a rival supplies all of:

1. a state space and time-evolution law;
2. a non-bivalent event algebra with normalized complete tests;
3. a composition rule and causal constraints;
4. a derivation linking one valuation event to independently affirmative proposition-dual records;
5. a quantitative excess distribution not reducible to leakage, loss, an expanded outcome, or
   ordinary quantum error; and
6. the standard quantum result as a controlled limit or a separately testable deviation.

Until then the witness remains an experimentally intelligible severe-test form without a
TRT-specific or rival-specific physics prediction.

## Primary sources

- M. Ozawa, “Quantum measuring processes of continuous observables,” *Journal of Mathematical
  Physics* 25, 79--87 (1984), DOI 10.1063/1.526000.
- G. Chiribella, G. M. D'Ariano, and P. Perinotti, “Probabilistic theories with purification,”
  *Physical Review A* 81, 062348 (2010), arXiv:0908.1583,
  DOI 10.1103/PhysRevA.81.062348.
- N. C. A. da Costa and C. de Ronde, “The Paraconsistent Logic of Quantum Superpositions,”
  arXiv:1306.3121 (2013).
- N. C. A. da Costa and C. de Ronde, “The Paraconsistent Approach to Quantum Superpositions
  Reloaded,” arXiv:1507.02706 (2015).
