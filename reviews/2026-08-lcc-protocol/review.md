# Internal Red-Team Review — Logical Constraint Closure Protocol

- **Date:** 2026-08-28
- **Target:** the preserved LCC experimental-protocol intake in `WP-TRT-LCC-0001`
- **Review posture:** strongest charitable reconstruction, then observability, circularity,
  rival-model, and severe-test attacks
- **Verdict:** **REJECT as tier-3 protocol; RECLASSIFY the surviving question as tier-2
  operationalization debt**

## Strongest reconstruction

The strongest non-circular version of the proposal is:

1. certify a measurement context as closed using criteria fixed without consulting the eventual
   outcome label;
2. inspect independent raw records after closure;
3. look for a positive record pattern licensed by a rival theory but forbidden by TRT; and
4. confirm that the pattern is neither `0`, `1`, another physical state, nor apparatus/data
   failure.

This is stronger than the submitted text because step 3 requires a positive observation pattern
and a rival likelihood. The submission supplies neither. The review does not silently credit it
with them.

## Attack 1 — the candidate event has no positive observable

The ten candidate criteria define $\chi_\varnothing$ only by excluding all recognized physical
states and failures. A recorded residual is still a physical record; absence of a record is a
no-click or acquisition event. Both are excluded. Therefore the classifier can return only a
known outcome, anomaly, invalid trial, or unclassified datum. Calling the last class
`nonactualization` is an interpretation of ignorance, not an additional observation.

**Finding:** decisive. The protocol has no event whose frequency $N_\varnothing/N$ can be counted.

## Attack 2 — redundant recording makes the falsifier inconsistent or weakens closure

$C_R$ requires multiple sufficiently independent record channels to contain the measurement
information. If that means the outcome-bearing pointer information used in quantum Darwinism,
then candidate criteria 7–9 deny what $C_R$ asserts. If it means only that a measurement pulse or
interaction occurred, it does not establish closure of the alternatives.

**Finding:** decisive dilemma. Strong $C_R$ makes the candidate set empty; weak $C_R$ breaks
$C_L\Rightarrow I_{\mathrm{irr}}$.

## Attack 3 — “classification precedes outcome classification” is not independence

$C_P$ and $C_R$ depend on pointer distinguishability and recorded measurement information. If
they are evaluated from the same retained analog channels used later to label the outcome, the
two classifiers share data. Running one first does not make it independent. Separate channels or
held-out data could repair this defect, but not Attacks 1 or 2.

**Finding:** repairable design flaw, not the central failure.

## Attack 4 — the POVM section concedes non-discrimination

For a complete outcome model, effects sum to the identity. A residual observation either receives
its own effect and becomes another physical outcome or has zero effect after an already exhaustive
set. The submission derives $p_\varnothing=0$ from completeness and then presents an experiment
whose only prediction is that same normalization. Standard quantum measurement and LCC therefore
assign no different observable likelihood.

**Finding:** decisive against tier 3. Agreement with a framework assumption is compatibility, not
a novel prediction.

## Attack 5 — the statistics test sensitivity, not the universal

The zero-count upper bound is correct for a well-defined Bernoulli event. It can constrain
$p_\varnothing$ only after such an event is operationalized. Moreover, rejecting
$p_\varnothing\ge\epsilon$ supports a sensitivity-bounded claim, not the exact universal
$p_\varnothing=0$. This limitation is acknowledged in the intake, but the event-definition
failure prevents even the bounded test.

**Finding:** mathematically acceptable conditional on an event definition; inapplicable here.

## Attack 6 — realistic transmon records expand the anomaly model

Dispersive transmon readout produces noisy continuous records with finite measurement efficiency;
measurement drive can also induce transitions into noncomputational states. Redundant digitization
does not create independent physical records if channels share the same resonator field,
amplifier, or upstream noise. These facts enlarge calibration and causal-dependence requirements.
They do not create a route to identifying literal nonactuality.

**Finding:** implementation burden reinforces, but does not cause, the conceptual failure.

## Change-the-verdict conditions

A future proposal may return only if it supplies all four:

1. a positive raw-data event definition fixed before data collection;
2. an independently measurable closure antecedent that remains satisfiable on that event;
3. a calibrated rival model assigning the event nonzero probability while TRT assigns zero; and
4. a demonstration that adding the event to the measurement outcome model does not simply turn it
   into another physical outcome.

Condition 4 may be impossible in ordinary instrument semantics. That is the open conceptual
problem, not a reason to relax it.

