# Logical Constraint Closure and the Minimal Actualization Experiment

## A Falsifiable Experimental Protocol for Quantum Actualization

**Status:** Research hypothesis / experimental protocol draft\
**Date:** 28 August 2026

## Abstract

This protocol tests the hypothesis that a quantum measurement cannot
remain non-actualized once physically relevant informational
alternatives reach irreducible closure under global logical constraint.
The frozen notation is:

-   (L): Logic, the global constraint on admissibility.
-   (I): Information, reducible until (I\_{`\mathrm{irr}`{=tex}}).
-   (`\mathcal `{=tex}A): Primitive Action, the irreducible active
    primitive.
-   (`\chi`{=tex}): Actualization, the outcome.

The central relation is

\[ `\boxed{\chi\equiv\mathcal A(I\mid L)}`{=tex} \]

and at irreducible closure,

\[ `\boxed{\chi\equiv\mathcal A(I_{\mathrm{irr}}\mid L)}`{=tex}. \]

The experiment is Popperian. A validated case in which independently
certified closure occurs while no physical outcome obtains would falsify
the unrestricted law.

## 1. Minimal Quantum System

Use a superconducting transmon qubit prepared in the maximally symmetric
state

\[ \|+`\rangle`{=tex}=`\frac{|0\rangle+|1\rangle}{\sqrt2}`{=tex} \]

and perform a binary (Z)-basis measurement. The Born rule predicts

\[ P(0)=P(1)=`\frac12`{=tex}. \]

The nominal actualization space is

\[ `\Omega`{=tex}={`\chi`{=tex}\_0,`\chi`{=tex}\_1}. \]

Introduce the proposed counterexample

\[
`\chi`{=tex}\_`\varnothing`{=tex}=`\text{genuine nonactualization}`{=tex}.
\]

For a completed binary measurement the LCC prediction is

\[ `\chi`{=tex}`\in`{=tex}{0,1}. \]

## 2. Meaning of Nonactualization

(`\chi`{=tex}\_`\varnothing`{=tex}) cannot mean detector no-click,
photon loss, qubit relaxation, leakage, apparatus failure, corrupted
data, inconclusive readout, a recognizable coherent state, absorption
elsewhere, or any other identifiable physical condition. Each of those
is itself an actuality.

The counterexample is stronger:

\[ `\boxed{\chi_\varnothing:
\text{the independently certified measurement context closes, yet no definite physical outcome obtains}.}`{=tex}
\]

An unexplained event is not automatically a nonactualization event.

## 3. Hypotheses

The foundational prediction is

\[ `\boxed{H_{\mathrm{LCC}}:
P(\chi_\varnothing\mid I_{\mathrm{irr}},L)=0.}`{=tex} \]

Equivalently,

\[
P(`\chi`{=tex}\_0`\lor`{=tex}`\chi`{=tex}*1`\mid `{=tex}I*{`\mathrm{irr}`{=tex}},L)=1.
\]

The falsification proposition is

\[ `\boxed{H_F:
\exists I_{\mathrm{irr}}\text{ such that }
P(\chi_\varnothing\mid I_{\mathrm{irr}},L)>0.}`{=tex} \]

Finite experiments cannot demonstrate an exact zero probability, so
preregister a sensitivity threshold (`\epsilon`{=tex}):

\[
H_0\^{`\mathrm{exp}`{=tex}}:p\_`\varnothing`{=tex}`\ge`{=tex}`\epsilon`{=tex}
\]

versus

\[ H_1\^{`\mathrm{exp}`{=tex}}:p\_`\varnothing`{=tex}\<`\epsilon`{=tex}.
\]

The theoretical universal remains (p\_`\varnothing=0`{=tex}).

## 4. Popperian Falsifier

Let (C_L) be an independently specified operational closure condition.
The proposed law is

\[ `\boxed{C_L\Rightarrow\chi.}`{=tex} \]

The forbidden observation is

\[ `\boxed{C_L=1\land\chi=\varnothing.}`{=tex} \]

Closure cannot be defined as "the point at which an outcome occurred,"
because that would make the hypothesis circular.

## 5. Operational Closure

Define

\[ `\boxed{C_L=(C_D,C_P,C_R,C_S,C_X)}`{=tex} \]

and declare closure only when

\[ `\boxed{C_L=1
\iff C_D\land C_P\land C_R\land C_S\land C_X.}`{=tex} \]

### (C_D): Decoherence

Residual coherence in the measurement basis falls below a preregistered
threshold:

\[ \|`\rho`{=tex}\_{01}(t_c)\|\<`\epsilon`{=tex}\_D. \]

### (C_P): Pointer distinguishability

Calibrated pointer states are distinguishable:

\[
D\_{`\mathrm{tr}`{=tex}}(`\rho`{=tex}*{M0},`\rho`{=tex}*{M1})\>1-`\epsilon`{=tex}\_P.
\]

### (C_R): Redundant recording

Multiple sufficiently independent record channels contain the
measurement information:

\[ R\_`\delta`{=tex}`\ge `{=tex}R\^\*. \]

The redundancy metric must be preregistered.

### (C_S): Stability

The record architecture is stable against experimentally accessible
recoherence for a specified interval (`\tau`{=tex}):

\[
P(`\text{recoherence during }`{=tex}`\tau`{=tex})\<`\epsilon`{=tex}\_S.
\]

### (C_X): Context completion

All operations capable of coherently reopening or changing the relevant
measurement context have terminated:

\[ C_X=1. \]

Define closure time as

\[ `\boxed{t_c=\inf\{t:C_L(t)=1\}.}`{=tex} \]

Closure classification must precede outcome classification.

## 6. Experimental Platform

Use a transmon qubit dispersively coupled to a microwave readout
resonator. This platform provides a controlled two-state system, routine
preparation of (\|+`\rangle`{=tex}), high-rate repeated measurement, raw
analog measurement records, and tunable measurement strength.

The readout should be as quantum-nondemolition as practical.
Measurement-induced transitions, relaxation, leakage, and amplifier
errors must be independently characterized.

## 7. Redundant Record Architecture

A single detector channel is insufficient because detector inefficiency
could mimic nonactualization. Use multiple independently digitized
record paths:

\[ \|+`\rangle`{=tex} `\rightarrow`{=tex}
`\text{dispersive measurement}`{=tex} `\rightarrow`{=tex}
`\text{amplification}`{=tex} `\rightarrow`{=tex}
{R_1,R_2,R_3,`\ldots`{=tex}}. \]

Retain raw analog records. Do not classify them as (0) or (1) until
after the closure flag has been determined.

## 8. Experimental Sequence

For each trial:

1.  Initialize the qubit in (\|0`\rangle`{=tex}).
2.  Apply (R_y(`\pi`{=tex}/2)) to prepare (\|+`\rangle`{=tex}).
3.  Initiate calibrated dispersive (Z)-measurement.
4.  Evaluate (C_D(t),C_P(t),C_R(t),C_S(t),C_X(t)).
5.  Determine whether (C_L=1) and record (t_c).
6.  Only after closure classification, analyze the independent raw
    record channels.
7.  Assign the trial to (`\chi`{=tex}*0), (`\chi`{=tex}*1),
    (`\chi`{=tex}*{`\mathrm{anomaly}`{=tex}}), or
    (`\chi`{=tex}*`\varnothing`{=tex}).

Known physical anomalies remain actual outcomes and are reported
separately.

## 9. Candidate (`\chi`{=tex}\_`\varnothing`{=tex}) Criteria

A trial may be called a candidate nonactualization only if:

1.  (C_L=1) was independently certified.
2.  State-preparation diagnostics passed.
3.  Apparatus-health diagnostics passed.
4.  No known leakage state explains the event.
5.  No calibrated relaxation or excitation event explains it.
6.  No photon-loss or readout-chain failure explains it.
7.  No channel supports a valid (0) record.
8.  No channel supports a valid (1) record.
9.  No alternative physical state identifiable from the raw data
    explains it.
10. The event survives preregistered independent reanalysis.

## 10. Mandatory Negative Control

Deliberately stop or reverse the measurement before closure:

\[ C_L=0. \]

Then perform an interference-sensitive operation. Recoverable coherence
should exceed a preregistered visibility threshold:

\[ `\boxed{C_L=0\Rightarrow V_{\mathrm{interference}}>V^*.}`{=tex} \]

This demonstrates that the closure criterion distinguishes an
operationally unresolved quantum state from a closed measurement
architecture.

## 11. Born-Rule Control

Among valid binary actualizations verify

\[ P(`\chi`{=tex}\_0)=P(`\chi`{=tex}\_1)=`\frac12`{=tex}. \]

For counts (N_0,N_1,N\_`\varnothing`{=tex}),

\[ N=N_0+N_1+N\_`\varnothing`{=tex}. \]

Test

\[ `\frac{N_0}{N_0+N_1}`{=tex}`\approx`{=tex}`\frac12`{=tex} \]

independently of the LCC prediction

\[ `\boxed{\frac{N_\varnothing}{N}=0.}`{=tex} \]

It is logically possible to preserve Born statistics among actualized
trials while violating LCC:

\[
P(0`\mid`{=tex}`\chi`{=tex}`\neq`{=tex}`\varnothing`{=tex})=P(1`\mid`{=tex}`\chi`{=tex}`\neq`{=tex}`\varnothing`{=tex})=`\frac12`{=tex}
\]

while

\[ P(`\chi`{=tex}\_`\varnothing`{=tex})\>0. \]

## 12. Statistical Design

Let (N) be the number of valid independently certified closure trials
after preregistered exclusions.

With zero validated nonactualization events, the exact one-sided 95%
upper confidence bound is

\[ `\boxed{p_\varnothing<1-0.05^{1/N}.}`{=tex} \]

For large (N),

\[ p\_`\varnothing`{=tex}`\lesssim`{=tex}`\frac`{=tex}3N. \]

Thus approximately:

-   (N=10\^4):
    (p\_`\varnothing`{=tex}`\lesssim3`{=tex}`\times10`{=tex}\^{-4})
-   (N=10\^6):
    (p\_`\varnothing`{=tex}`\lesssim3`{=tex}`\times10`{=tex}\^{-6})
-   (N=10\^8):
    (p\_`\varnothing`{=tex}`\lesssim3`{=tex}`\times10`{=tex}\^{-8})

The relevant (N) is valid closure events, not raw shots.

## 13. Falsification Rule

A **candidate falsification** occurs when

\[ `\boxed{C_L=1\land\chi=\varnothing}`{=tex} \]

and all preregistered anomaly and equipment explanations fail.

A **confirmed falsification** requires independent replication,
preferably on a second device or readout architecture. Replication is
experimental prudence. Logically, one genuine counterexample falsifies
the unrestricted universal.

## 14. Relation to Complete Quantum Measurement

For a complete POVM,

\[
{E_i},`\qquad `{=tex}E_i`\ge0`{=tex},`\qquad`{=tex}`\sum`{=tex}\_iE_i=I,
\]

the Born probabilities satisfy

\[ P(i)=`\operatorname{Tr}`{=tex}(`\rho `{=tex}E_i) \]

and

\[ `\sum`{=tex}\_iP(i)=1. \]

If a nonactualization effect (E\_`\varnothing`{=tex}) is added while the
original outcome set is already exhaustive,

\[ E\_`\varnothing`{=tex}=I-`\sum`{=tex}\_iE_i=0 \]

and therefore

\[ P(`\varnothing`{=tex})=0. \]

If (E\_`\varnothing`{=tex}\>0), the original measurement was incomplete
and (`\varnothing`{=tex}) has become another physical outcome rather
than literal absence of actuality.

Thus standard complete quantum measurement is formally compatible with
the LCC prediction (p\_`\varnothing=0`{=tex}), although this does not by
itself establish the proposed ontology.

## 15. Operational Versus Foundational Closure

The measurable vector (C_L) must not be equated without argument with
(I\_{`\mathrm{irr}`{=tex}}).

The foundational proposal is

\[ `\boxed{
I_{\mathrm{irr}}
=
\text{the informational condition after all physically relevant alternatives have been irreducibly exhausted under }L.
}`{=tex} \]

The experimental vector (C_L) is a proxy for that condition.

The central theoretical vulnerability is therefore:

\[
`\boxed{\text{Does }C_L=1\text{ validly imply that }I_{\mathrm{irr}}\text{ has been reached?}}`{=tex}
\]

Improving or deriving that implication is a primary research objective.

## 16. Current Evidential Status

**HIGH:** Complete quantum measurements normalize the specified outcome
space to total probability one.

**HIGH:** Standard unitary measurement dynamics can generate decoherence
and stable record structures without, by itself, selecting one unique
global branch.

**HIGH:** Bell-type results exclude the relevant class of purely local,
context-independent hidden-variable closures.

**HIGH:** The protocol states an in-principle falsifier that is
logically distinct from Born-rule testing.

**MEDIUM:** Decoherence, pointer distinguishability, redundancy,
stability, and context completion jointly provide a useful operational
proxy for irreducible informational closure.

**UNCERTAIN:** Whether this operational proxy is sufficient to establish
(I\_{`\mathrm{irr}`{=tex}}). This is the principal theoretical issue to
resolve before claiming that a laboratory implementation directly tests
the foundational law.

## 17. Core Research Statement

The programme can be reduced to four lines:

\[ `\boxed{\chi\equiv\mathcal A(I\mid L)}`{=tex} \]

\[ `\boxed{\chi\equiv\mathcal A(I_{\mathrm{irr}}\mid L)}`{=tex} \]

\[
`\boxed{H_{\mathrm{LCC}}:P(\chi=\varnothing\mid I_{\mathrm{irr}},L)=0}`{=tex}
\]

\[ `\boxed{\text{Falsifier: }C_L=1\land\chi=\varnothing.}`{=tex} \]

The experiment therefore does not ask which Born-allowed outcome occurs.
It asks the more primitive question:

> Once the informational alternatives have irreducibly closed under
> global logical constraint, can physical reality fail to actualize at
> all?

The hypothesis answers **no**. The experimental programme is designed to
give nature an independently specified opportunity to answer otherwise.
