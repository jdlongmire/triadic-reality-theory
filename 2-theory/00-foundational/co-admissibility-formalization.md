# Co-Admissibility Formalization (Task 0.1)

> **Tier:** 2-theory (protective belt). **Lakatos role:** the gating belt-construction — the single highest-leverage task. Nothing discriminating is reachable without it (it is the root of the [dependency graph](../../0-program-methods/ROADMAP.md)). **Status:** OPEN. **Confidence a formalization exists:** UNCERTAIN — this is the make-or-break task.

## Target

Define co-admissibility as a criterion that takes a collection of physical constraints (channel structure, conserved quantities, coupling data) and computes a definite set of admissible structures, with **no free entanglement measure**.

> A criterion `C(constraints) → admissible set` that is well-defined, computable, and measure-independent.

## Prerequisite

None. This is the root.

## Failure condition (`risk_if_false`)

If no formalization can avoid reintroducing a free measure, or if every formalization reduces to the existing einselection optimization, the co-admissibility program collapses to re-description and **both physics conjectures lose their discriminating content** — the [decoherence conjecture](../../3-prediction/co-admissibility-conjecture.md) and the [gravity conjecture](../../3-prediction/gravity-linearity-test.md). Recording that negative result is itself a progressive resolution, not a failure of the program.

## Notes

The finite-graph attack on the gravity side ([`../03-gravity/relational-graph-test.md`](../03-gravity/relational-graph-test.md)) is part of formalizing the measure, and it reduced the question to the keystone: does *A* register obstruction (linear) or best-fit project (quadratic)? See [`actualization-resolution.md`](actualization-resolution.md). Co-admissibility may be more naturally a numerical/computational object than a Lean proof object; that is itself open (see [`../../formalization/README.md`](../../formalization/README.md)).

## Attempt 1 — the kernel/invariance criterion C₀ (2026-06-26, agent roster)

*Produced by Formalization-Agent, attacked by Red-Team-Reviewer, calibrated by Peer-Review-Agent. **Status after the pass: OPEN** (proof_status advanced to `prose_only`; epistemic stays `open`).*

**Candidate (C₀).** Take the constraint data to be the open-system generator — a Lindbladian `𝓛(ρ) = -i[H,ρ] + Σₖ γₖ(LₖρLₖ† − ½{Lₖ†Lₖ,ρ})` with the incompatible channels as jump operators (cavity case: a number-basis channel `L_n` and a coherent-state channel `L_α`). The only **measure-free, definite, set-valued** map from `{Lₖ, γₖ, H}` alone is the joint-invariance / kernel object

> `C₀({Lₖ,γₖ,H}) = { ρ : 𝓛(ρ) = 0 }` — the common fixed-point/kernel of all constraints at once.

This is the **dissipative port of the program's own result** "joint *L₃*-satisfiability = flatness = kernel of the holonomy obstruction" (relational-graph §1): co-admissible = jointly invariant under every constraint, computed from the operator algebra with no inner product. It is Lean-definable as vocabulary and computable as a joint-kernel over the truncated Fock space.

**Why it does not yet close the task (Red-Team, converged with Peer-Review):**

1. **Failure and "escape hatch" are one theorem.** `C₀` is rich (a *family*) iff the Lindblad fixed-point set is nontrivial iff the commutant `{Lₖ,Lₖ†,H}'` is nontrivial (Spohn 1977; Frigerio 1978; Evans). In the **incompatible regime** (`[L_n,L_α]≠0`) the kernel generically degenerates to a *single* steady state. The proposed rescue (a nontrivial decoherence-free subsystem) is the exact logical negation of the failure, not an independent lifeline — so the whole question reduces to **one open algebraic fact**: is the commutant nontrivial at/across the critical coupling?
2. **Even a nontrivial commutant likely targets the wrong subspace.** A DFS is the *protected* (non-decohering) sector; the einselected Fock-vs-coherent pointer family (with its analytic critical coupling) lives in the *decohering* complement. Measure-free survival of the DFS would then be disjoint-by-construction from the object the conjecture must reproduce.
3. **A weaker, more L₃-faithful criterion was not tested.** TRT defines non-contradiction *pairwise* ("no state forced to two values in the same respect"), which maps to **mutually commuting dissipators** `{ρ : [𝓓_k,𝓓_α](ρ)=0 ∀k,α}`, not to a global kernel. This is measure-free, strictly weaker than `C₀`, and untested — the collapse of "non-contradiction" into "joint invariance" was unjustified.

**Decisive next artifact (supersedes the one-part check):** a computation over the actual Feller–Coeuret Cauquil–Roussel two-channel cavity model that returns **both** (i) whether the commutant `{L_n,L_α,L_n†,L_α†,H}'` is nontrivial across the critical coupling, **and** (ii) whether the analytic einselected pointer states lie *inside* that commutant or in its orthogonal complement. Plus a test of the pairwise-commuting-dissipator criterion (3). This three-way numerical result moves OPN-001 from open to a definite outcome.

**Honest status:** `C₀` is a measure-free *re-description* that unifies with the flatness=kernel result and is impotent in the discriminating regime; whether co-admissibility can be made measure-free *and* discriminating reduces to the commutant computation above. This is a **progressive theoretical step** (sharper falsifier + a written construction), not a resolution. OPN-001 stays **open**.
