# Nonactualization as an Operational Target

> **Tier:** 2-theory (protective belt). **Status:** first-pass instrument-semantics audit,
> corrected by the Stage-2 [`global FLL closure witness`](fll-closure-witness.md). **Claim:**
> `OPN-009`. **Provenance:** disposition of
> [`WP-TRT-LCC-0001`](../../05-work-packages/WP-TRT-LCC-0001-logical-constraint-closure/package.yaml).

## The question

TRT reserves *outcome-actual* for a determinate measurement result and leaves the final
selection from the admissible set to one outcome as the unresolved action of *A*. A proposed
test asked whether a completed measurement could instead yield genuine nonactualization:

$$
C_L = 1 \land \chi = \varnothing.
$$

The proposal is valuable because it forces an operational question that TRT had not isolated:
what observation could distinguish the absence of an actual outcome from an anomalous actual
state, a failed record, or an unclassified record?

## Outcome-space audit

Let `Y` be the space of all retained raw records and apparatus diagnostics for a trial. Any
experimental decision rule is a function from `Y` to declared labels. For the submitted
protocol the labels are, in substance,

$$
d:Y\rightarrow\{0,1,\mathrm{anomaly},\mathrm{invalid},\mathrm{unclassified}\}.
$$

There is no separate observable supplied for $\varnothing$ **in the submitted protocol**.

- A raw record supporting `0` or `1` is a binary outcome.
- A record supporting leakage, relaxation, excitation, loss, corruption, or another state is
  an anomalous physical outcome or an invalid trial.
- No record is a no-click, acquisition, or apparatus event, all explicitly excluded.
- A residual record is an unclassified physical record. Relabelling that residual
  `nonactualization` adds an ontological interpretation but no new observable.

The problem is not that a rare event would be difficult to detect. The proposed event lacks an
observation rule independent of the exclusions used to define it. A confidence interval on its
rate therefore cannot repair the missing event definition.

## Closure dilemma

The closure vector contains redundant recording, $C_R$. In the environment-as-witness sense,
redundancy means information about pointer observables is independently accessible from
multiple environmental fragments. This creates a dilemma:

1. If $C_R$ means redundant **outcome information**, then $C_R=1$ conflicts with the candidate
   criteria that no channel supports `0`, `1`, or another physical state. The proposed
   falsifying conjunction has an empty operational extension.
2. If $C_R$ means only redundant evidence that an interaction or measurement cycle occurred,
   it does not show that the outcome alternatives were irreducibly exhausted. The bridge
   $C_L\Rightarrow I_{\mathrm{irr}}$ fails.

The other closure components establish decoherence, distinguishability, stability, and protocol
completion. They can establish a robust measurement architecture. They do not by themselves
select a unique global outcome, a limitation already acknowledged by the submitted protocol and
by TRT's Logical Resolution Model.

## Independence audit

Declaring closure before assigning `0` or `1` is temporal ordering, not statistical or logical
independence. If $C_P$ and $C_R$ are computed from the same analog records later used for outcome
classification, the antecedent and consequent share data. An adequate design would require at
least:

- disjoint preregistered data partitions or genuinely independent instruments for closure and
  outcome classification;
- a closure classifier that does not use outcome-validity thresholds, directly or indirectly;
- a positive observation rule for the alleged null event; and
- a rival model assigning a different probability to that same observable.

The first two can reduce circularity. They cannot supply the missing positive observation rule.

## Relation to complete quantum measurement

A finite POVM is an exhaustive experimental outcome model: effects $E_i$ sum to the identity and
$p_i=\mathrm{tr}(\rho E_i)$. If an observed residual class exists, the calibrated measurement
model must include an effect for it; it then has a nonzero probability and is another physical
outcome. If no such effect exists after the original effects already sum to the identity, its
effect is zero. This is measurement-model normalization, not an empirical consequence distinctive
to TRT.

Real dispersive readout also has finite efficiency, continuous noisy records, leakage, and
measurement-induced transitions. Those are reasons to enlarge or refine the outcome and
diagnostic model, not evidence of literal nonactuality.

## Result

The submitted protocol is **not promoted to tier 3 as written**. It cannot expose TRT to a
measurement outcome forbidden by standard quantum theory:

- under the strong reading of redundancy, its candidate event is operationally inconsistent;
- under the weak reading, closure does not imply irreducibility;
- under either reading, `nonactualization` is not positively observable; and
- the complete-POVM argument makes the zero probability true by model exhaustiveness rather than
  by a novel physical law.

The surviving contribution is this tier-2 operationalization problem:

> Specify a positive, instrument-level event that distinguishes failure of outcome actualization
> from every physical outcome and every record failure, while remaining possible under a
> well-defined rival model.

### Stage-2 correction

The terminal inference “therefore no positive observable can exist” was too strong. A pair of
affirmative reports about $P$ and $\neg P$ can yield actual meta-records `00` (gap) and `11`
(glut); redundant correlated instances can witness failure of bivalent outcome valuation without
requiring nonactualization itself to become an ordinary third outcome. The derived inequality and
its assumptions are in [`fll-closure-witness.md`](fll-closure-witness.md).

Thus this document's critique remains dispositive against the **submitted classifier**, not against
the possibility of an FLL discriminator.

## Primary sources

- P. Busch, “Quantum states and generalized observables: a simple proof of Gleason's theorem,”
  *Physical Review Letters* 91, 120403 (2003), arXiv:quant-ph/9909073.
- H. Ollivier, D. Poulin, and W. H. Zurek, “Environment as a witness,” *Physical Review A* 72,
  042113 (2005), DOI 10.1103/PhysRevA.72.042113.
- G. de Lange et al., “Reversing Quantum Trajectories with Analog Feedback,” *Physical Review
  Letters* 112, 080501 (2014), DOI 10.1103/PhysRevLett.112.080501.
- K. N. Nesterov and I. V. Pechenezhskiy, “Measurement-induced state transitions in dispersive
  qubit-readout schemes,” *Physical Review Applied* 22, 064038 (2024), DOI
  10.1103/PhysRevApplied.22.064038.
