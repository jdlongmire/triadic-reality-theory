---
layout: default
title: Technical
---
<p class="eyebrow">Technical & systematic framing</p>

# Canonical ontology

$$\mathrm{TRT}=\langle L_3,I_{\infty},A\rangle$$

| Symbol | Canonical meaning | Status |
|---|---|---|
| $L_3$ | Ontological logical constraint: Identity, Non-Contradiction, Excluded Middle | hard-core claim |
| $I_\infty$ | Unbounded informational representability/differentiation | hard-core claim |
| $A$ | Fundamental state transition/change, non-temporal in primitive definition | hard-core claim |
| $R$ | Representable domain | typed category |
| $D$ | Actualizable domain | sufficiency conditions open |
| $X/\chi$ | What obtains / actualized reality | typed category |

## Compact identity

$$\boxed{\chi \equiv \mathsf{A}(I_{\infty}\mid L_3)}$$

The compact identity does not assert $D=I_\infty\mid L_3$.

## Typed actualizability architecture

$$R \xrightarrow{\;L_3\;\mathrm{necessary\ filter}\;} D \xrightarrow{\;A\;} X\,(\chi)$$

$$x\in D\Rightarrow \mathrm{Adm}_{L_3}(x).$$

The converse is not presently warranted:

$$\mathrm{Adm}_{L_3}(x)\nRightarrow x\in D.$$

## Necessity and irreducibility

1. **$L_3$:** constraint cannot be supplied by content or transition merely by being content or transition.
2. **$I_\infty$:** without differentiated relata, constraint and transition have nothing determinate to govern.
3. **$A$:** constraint plus representation do not entail that a transition obtains.

## Formal status

The Lean core separates `L3Admissible` from `Actualizable` and axiomatizes

$$\mathrm{Actualizable}(r)\Rightarrow \mathrm{L3Admissible}(r)$$

without encoding the converse. Primitive `A` is separately typed from `Obtains`.

## Open proof obligations

- Determine whether $L_3$-coherence is sufficient for $D$.
- Make the representation-to-efficacy / $D$-to-$X$ role of $A$ rigorous without circular actuality language.
- Test whether $A$ can be eliminated by a complete state-space plus dynamics without explanatory loss.
- Formalize non-temporal transition ordering sufficiently for any emergence-of-time claim.
- Continue empirical FLL work without converting transcendental warrant into empirical confirmation by stipulation.

## Physics-facing programme

Measurement, variational, gravity, cosmology, and FLL work belongs downstream of the ontology and may fail without redefining the co-primitives.

## Canonical sources

[Hard core](https://github.com/jdlongmire/triadic-reality-theory/blob/main/1-hypothesis/hard-core.md) · [TRT v0.10](https://github.com/jdlongmire/triadic-reality-theory/blob/main/1-hypothesis/paper/TRT-v0.10.md) · [Lean core](https://github.com/jdlongmire/triadic-reality-theory/blob/main/formalization/TrtFormalization/Core/Primitives.lean) · [Traceability](https://github.com/jdlongmire/triadic-reality-theory/tree/main/traceability)
