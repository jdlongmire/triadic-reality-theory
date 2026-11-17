# Causal Burden Conservation: A Symmetric Framework for Historical Causal Inference

**Status:** Working paper scaffold  
**Work package:** WP-TRT-CBCP-0001

## Abstract

Historical explanations commonly contain causal transitions that cannot be directly observed. This creates a recurrent epistemic danger: evidential support for one part of a reconstruction can be allowed to migrate into an adjacent but independently unresolved causal transition. The Causal Burden Conservation Principle (CBCP) proposes a symmetric rule for controlling that inference. Every material causal transition asserted by an explanatory model carries its own evidential burden, and that burden cannot be discharged merely by evidence for an adjacent transition, elapsed time, an explanatory label, or the failure of a competing account. CBCP distinguishes generative capacity from historical attribution, operational causation from provenance, and component possibility from integrated causal adequacy. The framework is compatible with Bayesian model comparison but requires explicit causal and dependency structure before likelihoods are assigned. Intelligent agency, undirected physical processes, emergence, chance, and designed initialization are thereby subjected to the same burden architecture.

## 1. The problem

Consider a reconstructed sequence:

```text
S0 -> S1 -> S2 -> ... -> E
```

Evidence that strongly establishes one transition does not automatically establish the others. Yet historical explanations often compress unresolved transitions into terms such as "emergence," "chance," "evolution," "design," "initialization," or "sufficient time."

CBCP begins with a simple constraint:

> **Every material causal transition asserted by an explanatory model carries its own evidential burden. Evidence for adjacent transitions, elapsed time, explanatory labels, and deficiencies in competing explanations cannot by themselves discharge that burden.**

## 2. Formal seed

Let an explanatory history be a directed causal graph:

```text
G = (V, E)
```

where each vertex represents an evidentially relevant state and each material edge

```text
e_ij = (v_i -> v_j)
```

asserts a causal transition.

Associate with each edge an evidential burden `B(e_ij)`. Support for `e_kl` does not discharge `B(e_ij)` when the edges are distinct unless an explicit dependency, derivation, or independently warranted bridge licenses the transfer.

In TRT-compatible notation:

```text
chi_0 --A_1--> chi_1 --A_2--> ... --A_n--> chi_n
```

The ontological claim that action is required for transition is distinct from the epistemic claim that a particular `A_i` has been identified and historically warranted. CBCP governs the latter.

## 3. Causal adequacy

A historical explanation must do more than show that component events are individually possible.

```text
component possibility
< pathway plausibility
< integrated causal adequacy
< discriminating historical attribution
```

Causal adequacy asks whether the specified causal resources, operating under independently warranted initial and boundary conditions, can generate the explanandum through a reachable pathway.

## 4. Generative pathways

A causal category supported by independently observed generative capacity is a legitimate candidate when the explanandum belongs to the relevant class of effects.

Mind provides an important example:

```text
mind
-> intention
-> specification
-> selection
-> action
-> instantiated functional state
```

This is positive causal knowledge. It does not entail that every specified functional state was historically produced by mind. Generative capacity establishes candidacy; discriminating evidence is required for attribution.

Likewise, lawful physical systems demonstrably generate emergent outcomes:

```text
laws + initial state + boundary conditions + dynamics + time
-> emergent outcome
```

That evidence establishes the operational generative capacity of the specified regime. It does not without further argument establish an undirected provenance for the laws, conditions, or generative architecture presupposed by the regime.

## 5. No Gap Substitution

The following forms are methodologically parallel when the named category substitutes for an unresolved transition:

```text
unresolved pathway -> therefore divine action
unresolved pathway -> therefore sufficient time
unresolved pathway -> therefore chance
unresolved pathway -> therefore emergence
unresolved pathway -> therefore design
unresolved pathway -> therefore initialization
```

The error is not the use of any of these causal categories. The error is treating the category name as if it supplied the missing generative pathway.

> **Naming the gap is not crossing it.**

## 6. Time and emergence

Time is not by itself a generative mechanism. It may increase opportunities available to an independently specified process. More time has explanatory force only when the model establishes a reachable state space, transition structure, and opportunity or probability model under which additional duration changes the likelihood of the explanandum.

Emergence can be a genuine causal description, but its evidential content is conditional on the lower-level dynamics and constraints that generate the higher-level state. Evidence for emergence within a lawful regime must not be silently converted into evidence for the provenance of that regime.

## 7. Symmetry and independent burdens

Failure of one candidate explanation does not discharge another candidate's burden. This rule blocks both God-of-the-gaps and naturalism-of-the-gaps reasoning.

For competing hypotheses:

```text
H1: specified pathway P1 -> E
H2: specified pathway P2 -> E
```

each pathway must expose its own causal resources, conditions, dependencies, and unresolved transitions. A deficit on one ledger is not automatically a credit on the other.

## 8. Bayesian interface

CBCP is compatible with Bayesian model comparison:

```text
Posterior odds(H1:H2 | E)
=
Prior odds(H1:H2)
x
Bayes factor(E | H1:H2)
```

But a likelihood such as `P(E|H)` is only as meaningful as the generative model represented by `H`. Unmodeled causal transitions may not be hidden inside an omnibus hypothesis label and then treated as evidentially solved.

The Bayesian ledger should expose:

- causal graph and unresolved edges;
- initial and boundary conditions;
- dependencies among evidence streams;
- auxiliary hypotheses;
- fitted versus independently specified parameters;
- opportunity/probability structure;
- post-hoc accommodation;
- discriminating predictions;
- uncertainty in likelihood assignments.

Where numerical likelihoods are not defensible, ordinal comparison is preferable to false precision.

## 9. Adversarial test cases

The framework should be tested against cases that cut in different directions:

- Hoyle/Fowler and the carbon-12 resonance;
- Oklo natural nuclear reactors;
- abiogenesis simulation experiments;
- ordinary emergent physical systems;
- archaeology and forensic inference;
- DFM initialization;
- conventional deep-time historical reconstruction.

The purpose is not to guarantee a preferred conclusion. It is to determine whether CBCP applies symmetrically.

## 10. Relation to TRT

TRT supplies an ontological distinction among logical constraint, informational differentiation, action, and determinate actuality. CBCP does not add a fourth primitive. It is an epistemic governance rule for claims about which action or pathway connects evidentially relevant states.

In compact form:

```text
ontology:   chi requires action
epistemology: identifying the relevant action carries a burden
history:    attributing the action requires discriminating evidence
```

## 11. Research questions

1. Can burden assignment be formalized without pretending that epistemic warrant is numerically conserved?
2. What constitutes a material edge rather than a harmless explanatory decomposition?
3. When can evidence legitimately support multiple edges through a common causal model?
4. How should auxiliary cost and model flexibility enter comparative likelihoods?
5. What evidential threshold distinguishes demonstrated generative capacity from historical attribution?
6. How should interventions in simulation experiments be represented in the causal graph?
7. Can CBCP improve historical inference without privileging either design or non-design explanations?

## 12. Provisional thesis

> **Every material causal transition asserted by an explanatory model carries its own evidential burden. Evidence establishing one transition cannot automatically be borrowed to establish another. A candidate explanation gains causal standing through demonstrated generative adequacy and gains historical attribution only through evidence that discriminates it from causally adequate alternatives.**
