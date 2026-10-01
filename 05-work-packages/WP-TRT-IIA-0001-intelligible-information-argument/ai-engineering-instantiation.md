# Artificial Intelligence as an IIA Engineering Instantiation

Status: ACTIVE RESEARCH NOTE
Date: 2026-10-01
Work package: WP-TRT-IIA-0001

## Thesis

Artificial intelligence provides a concrete engineering instantiation of several
phenomena that constitute the explanandum of the Intelligible Information Argument
(IIA). It does not independently prove IIA's rational-ground hypothesis.

AI systems function only because their input domains contain sufficiently stable,
recoverable structure for learning systems to exploit. Their successes and failures
also operationally expose distinctions among statistical information,
representation, semantic grounding, truth, and knowledge.

## Engineering chain

```text
structured source domain
        |
        v
observations / encoded data
        |
        v
recoverable statistical structure
        |
        v
learned representation
        |
        v
inference / generated representation
        |
        +--> externally validated correspondence
        |          |
        |          v
        |     truth-constrained use
        |
        +--> statistically coherent mismatch
                   |
                   v
              hallucination / error
```

The chain must not be read as asserting that every stage entails the next.

## IIA correspondence

| IIA element | AI engineering analogue | What AI establishes |
|---|---|---|
| Mind-independent/source structure | language, images, code, sensor states, physical or human-produced domains | Learning requires exploitable regularity in represented data |
| Shannon/statistical information | token, feature, pixel, state and other statistical dependencies | Systems can extract and exploit statistical dependence |
| Receiver adequacy | architecture, training process, learned parameters | A receiver must be constituted so that relevant structure can affect its states |
| Representation | latent and explicit model states / generated outputs | Statistical learning can construct useful representations |
| Semantic evaluation | grounding, task interpretation, human/system use | Meaning is not guaranteed merely by statistical coherence |
| Truth relation | external validation against the represented domain | Correctness requires a criterion beyond generation probability |
| Error/hallucination | coherent output failing external truth conditions | Statistical success and truth are non-identical |

## Hallucination as a boundary case

Generative AI can produce outputs that are syntactically fluent, contextually
plausible, and statistically well supported while being false with respect to the
external domain.

Therefore:

```text
statistical coherence != semantic truth
```

This is an operationally important instance of the IIA typing rule:

```text
I_S != C_R != T != K
```

where:
- I_S = Shannon/statistical information;
- C_R = representational/semantic content;
- T = truth relation;
- K = knowledge.

The inequalities denote non-identity, not causal independence.

## Artificial intelligence and causal provenance

Existing artificial intelligence cannot serve straightforwardly as an example of
intelligence arising without antecedent intelligence. Its engineering provenance
includes human-developed mathematics, architectures, hardware, software, objective
functions, training procedures, data-selection practices, evaluation criteria, and
semantic uses.

This observation does not establish that intelligence cannot arise naturally from
non-intelligent physical processes. It establishes only that contemporary AI is not
an independent empirical instance of such an origin.

## Receiver-side experiment

AI provides a useful experimental platform for asking what receiver adequacy
requires.

A receiver can possess:
- high statistical sensitivity;
- compression/generalization capacity;
- predictive performance;
- sophisticated internal representations;

while still producing representations that fail external truth conditions.

This permits empirical investigation of which capabilities are sufficient for
prediction, grounding, truth tracking, semantic stability, and rational evaluation.

## Strong defensible claim

Artificial intelligence could not function as artificial intelligence unless at
least the following were available:

1. sufficiently stable structure in its source/data domains;
2. recoverable statistical relationships;
3. receiver architectures capable of exploiting those relationships;
4. representation mechanisms;
5. criteria distinguishing at least some successful outputs from errors.

These are components of the IIA explanandum.

## Claims not established

AI does not by itself establish:
- that Shannon information entails semantics;
- that semantics is necessarily immaterial;
- that machines cannot understand;
- that consciousness is required for all semantic processing;
- that emergence is impossible;
- that intelligence requires an antecedent personal mind;
- that God exists.

Those remain separate philosophical questions.

## Research consequence

AI should be treated within IIA as an ENGINEERING INSTANTIATION and TEST DOMAIN,
not as a proof of the rational-ground hypothesis.

It is particularly valuable because engineered receivers allow controlled
interventions unavailable in ordinary human cognition: architecture changes,
training-data changes, objective-function changes, grounding interventions,
retrieval augmentation, verifier insertion, and systematic measurement of error.

IIA can therefore generate an empirical research programme around the transition
from recoverability to representation and from representation to truth-constrained
use.
