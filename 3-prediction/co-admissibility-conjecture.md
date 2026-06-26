# The Co-Admissibility Conjecture (Task 1.1 / §13.1)

> **Tier:** 3-prediction (Popperian severe test). **Lakatos role:** the discriminating, falsifiable descendant — the point at which TRT attempts to say something a successful *interpretation* of QM does not already say, and therefore the point at which it can be wrong. **Provenance:** the §13 half of the working file `TRT-LRM-conjecture.md` (the §6.6 formalization half is the belt task at [`../2-theory/02-variational/born-rule.md`](../2-theory/02-variational/born-rule.md)).
>
> **Depends on:** Task 0.1, co-admissibility formalization ([`../2-theory/00-foundational/co-admissibility-formalization.md`](../2-theory/00-foundational/co-admissibility-formalization.md)). Until that exists this is a **conjecture, not a prediction.** *Confidence: LOW; one component UNCERTAIN.*

---

## 13.1 The Co-Admissibility Conjecture

A foundational ontology earns the status of physics when it generates a claim that could be false and that distinguishes it from its rivals. TRT's first-stage account of measurement (the [LRM first stage](../2-theory/02-variational/born-rule.md)), taken alone, does not meet this bar, since it agrees with decoherence on the cases decoherence settles. The discriminating claim must appear where decoherence is itself unsettled.

Such a place exists. When a system couples to two or more incompatible decoherence channels — non-commuting environmental couplings that select complementary observables — the preferred basis is not fixed by decoherence alone. The selection of pointer states in this regime is an open optimization problem, solved numerically against a chosen entanglement witness, and the answer depends in general on which witness is chosen. A representative case is a cavity field coupled simultaneously to a number-basis channel and a coherent-state-basis channel, where the einselected states interpolate between Fock and coherent states as the relative coupling varies, with Fock states remaining optimal up to a critical coupling obtainable analytically (Feller, Coeuret Cauquil and Roussel, 2020).

The analytic critical coupling (Feller et al., Eqs. 39–40) is the value at which the Fock state `|n₀⟩` ceases to be a local maximum of the purity-variation and becomes a saddle:

> `(κ_n/κ_a)_crit = n₀ + ½ + √(n₀(n₀+1))   ( ≈ 2n₀ + 1 )`,

an **energy-dependent** threshold (it scales with the photon number `n₀`). This exact value is the target any co-admissibility criterion must reproduce or contradict; the [formalization work](../2-theory/00-foundational/co-admissibility-formalization.md) (Attempt 3) finds that the purity-rate criterion `γ̇` reproduces it — but does so by *adopting* the purity witness, which raises the re-description question (§13.2 falsifier (a)).

This regime is the natural test of the co-admissibility criterion, because here TRT's criterion and standard einselection are not guaranteed to agree, and the standard answer is measure-dependent where TRT's is meant to be measure-independent.

> **Co-Admissibility Conjecture.** In the presence of incompatible decoherence channels, the set of co-admissible structures selected by the logical-compatibility criterion of LRM is determined by the constraint structure of the channels alone, without reference to a chosen entanglement witness, and coincides with the einselected set in the regimes where einselection is witness-independent while differing from it, in a specified and computable way, in the regimes where einselection is witness-dependent.

The conjecture is discriminating because it makes a definite claim about a case the standard theory leaves open, and because it can fail.

## 13.2 Status and Falsification Conditions

The conjecture is unproven. Its confidence is **LOW**, and one component — whether the formalized criterion yields a unique and correct prediction rather than reproducing the standard optimization — is **UNCERTAIN** pending the formalization.

Two pieces of work stand between the conjecture and a result:

1. **Formalization** (Task 0.1): make co-admissibility a criterion that computes a definite set of structures from a given collection of channel constraints, with no free measure. Until this exists, the conjecture cannot be evaluated, and it is possible that the criterion, made precise, reduces to the einselection optimization and predicts nothing new.
2. **Computation** (Task 1.1, contingent on 1): compute the criterion's prediction for the cavity-field case with two incompatible channels and compare against the known critical coupling.

**`falsifies` (Popperian):** the conjecture fails if the co-admissibility criterion, once formalized, either —
- reproduces the witness-dependence it was meant to eliminate; or
- yields a co-admissible set that contradicts the experimentally accessible pointer structure in the cavity-field regime, including the analytically known critical coupling at which Fock-state optimality ends; or
- cannot produce a definite prediction at all — which would show the proposal to be interpretation rather than physics.

A prediction that matches the analytic critical coupling is a confirmation. A prediction that contradicts it falsifies the criterion. **Either outcome, recorded, is a successful contribution** (progressive resolution); only the third — no definite prediction — is degenerating.

Computational work for this test belongs in `./code/` (created when Task 0.1 lands).

---

## Reference

Feller, A., Coeuret Cauquil, G. and Roussel, B. (2020) 'Einselection from incompatible decoherence channels', *arXiv:2001.10851* [quant-ph].

Zurek, W.H. (2003) 'Decoherence, einselection, and the quantum origins of the classical', *Reviews of Modern Physics*, 75(3), pp. 715-775.
