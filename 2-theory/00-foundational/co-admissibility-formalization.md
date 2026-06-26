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

**Honest status:** `C₀` is a measure-free *re-description* that unifies with the flatness=kernel result and is impotent in the discriminating regime; whether **these** measure-free objects discriminate reduces to the commutant computation above (it does **not** decide the whole measure-free design space — see Attempt 2's scope). This is a **progressive theoretical step** (sharper falsifier + a written construction), not a resolution. OPN-001 stays **open**.

## Attempt 2 — the decisive computation (2026-06-26, agent roster, computational)

*Produced inline as Formalization-Agent (computational), attacked by an independent Red-Team-Reviewer subagent (ran the code, re-derived the algebra three ways, pushed N to 64, added a falsifiability control), label-calibrated as Peer-Review. **Status after the pass: OPEN** — a recorded computational **negative** for the tested criteria; epistemic stays `open`.*

**Artifact.** [`../../3-prediction/co-admissibility-conjecture/code/coadmissibility_commutant.py`](../../3-prediction/co-admissibility-conjecture/code/coadmissibility_commutant.py) (+ `results.json`). Pure numpy/scipy, deterministic, no fitted parameters. Built on the **verified primary-source model** — Feller, Coeuret Cauquil & Roussel (2020), arXiv:2001.10851, Eqs. (3)–(4): `H = ω_c N`, `L_α = √κ_α a` (coherent-state channel), `L_n = √κ_n a†a` (number-basis dephasing); pointer states maximize variation of the **purity** witness `γ = tr ρ²`.

**Result (each leg confirmed, reproduces; cross-checked by independent re-derivation):**

1. **Commutant `{a, a†, N, H}' = ℂ·Id` — trivial.** Numerically dim = 1 across N = 8…64; the identity is an exact machine-zero singular value, the next sv is a truncation-boundary mode (~N^{-1/2}) that never collapses. Analytic backbone: `{a,a†}` act irreducibly on Fock space (Stone–von Neumann), so the commutant is `ℂ·Id`. **The `C₀` joint-invariance / decoherence-free-subsystem object is trivial — no DFS. The "escape hatch" is closed.**
2. **Pointer states lie wholly in the complement.** Fock `|n⟩⟨n|` residual = `√(2n+1)` (analytic, N-independent), coherent `|α⟩⟨α|` residual ≈ 2.83 — all clearly > 0. The measure-free object is **disjoint-by-construction** from the family the conjecture must reproduce (Attempt-1 attack #2, now rigorous).
3. **Pairwise-commuting-dissipator set = the whole state space.** `[𝓓_n, 𝓓_α] = 0` to machine precision (~1e-12) at every N, with **no** truncation defect (`L_n = N` is exactly diagonal). Independent analytic proof: `𝓓_n` multiplies each coherence band `ρ_{mn}` by the scalar `−½(m−n)²` while `𝓓_α` preserves coherence-order, so they commute exactly — **reproducing the paper's own Eq. (17)** (the two channels commute). The criterion is therefore satisfied by **every** state: measure-free but **non-discriminating**.

**Structural diagnosis (the genuinely informative part, via Red-Team).** All three tested objects are **algebraic / rate-independent**, whereas the pointer family is **rate-governed** (the Fock↔coherent transition sits at `κ_n/κ_α ≈ 1`). *A rate-independent object cannot, in principle, track a rate-dependent transition.* This is not just "these fail" but *where a surviving criterion would have to live*: rate-dependent and generator-derived.

**Scope (deliberately bounded).** This is a recorded **negative for the three tested measure-free criteria** — the `risk_if_false` outcome for OPN-001 — **not** a proof that no measure-free criterion can discriminate. The design space is not exhausted: the Red-Team checked the natural rate-*dependent* candidate (the Liouvillian slow modes) and it **also** fails (its slow eigenmode is a `k=±1` coherence band, not a pointer projector), which raises but does not max out confidence in the negative. **Open sub-question stands:** does any rate-dependent, generator-derived measure-free object reproduce the pointer interpolation?

**Honest status.** The *rate-independent* measure-free objects are **well-defined and computable but non-discriminating** on the real model. This is one horn of the dichotomy completed in Attempt 3; it materially pressures [PRD-001](../../3-prediction/co-admissibility-conjecture.md) but is **not** the whole story — see Attempt 3, which corrects the earlier (over-reached) "no measure-free criterion discriminates" reading.

## Attempt 3 — the rate-dependent door, and the dichotomy (2026-06-26, computational)

*Pursuing JD's directed sub-question: does any **rate-dependent**, generator-derived measure-free object reproduce the pointer structure? First version concluded "NO". **An independent Red-Team pass refuted that conclusion** — it found the first version tested the wrong comparison and missed an object that reproduces the analytic critical coupling. This entry records the corrected result.*

**Artifact.** [`../../3-prediction/co-admissibility-conjecture/code/coadmissibility_ratedep.py`](../../3-prediction/co-admissibility-conjecture/code/coadmissibility_ratedep.py) (+ `results_ratedep.json`). The **analytic critical coupling**, extracted from the primary-source PDF (Feller et al. Eqs. 39–40) and previously missing from our docs, is

> `g* = κ_n/κ_α = n₀ + ½ + √(n₀(n₀+1))  ( ≈ 2n₀ + 1 )`,

the coupling at which the Fock state `|n₀⟩` stops being a local maximum of the purity-variation (it becomes a saddle along the `(|n₀-1⟩,|n₀+1⟩)` plane).

**Result — a clean dichotomy across the measure-free objects:**

- **Witness-free → non-discriminating.** The genuinely witness-free objects (Attempt 2's commutant / kernel / pairwise-commuting set; and here the **Liouvillian generator spectrum** — all non-stationary eigenmodes are *traceless* by trace conservation, and the steady state is the *vacuum* at every `g`) make **no pointer-state prediction**.
- **Witness-fixed (purity) → re-description.** The initial purity-rate `γ̇ = −2[κ_n Var(N) + κ_α(⟨N⟩−|⟨a⟩|²)]`, applied via Feller's **own** energy-shell Fock-stability criterion, **reproduces the analytic `g*` to <0.2%** (independently re-derived and verified, n₀=2…6). It matches standard einselection *because `γ̇` **is** the (linear-entropy) predictability sieve* — it adopts the purity witness rather than eliminating it.

**Correction recorded (Red-Team caught a producer error).** The first version of the artifact compared `γ̇` for a Fock state vs a full coherent state (→ `g*=1`, energy-independent) and wrongly concluded no rate-dependent measure-free object discriminates. Feller's criterion is Fock-state stability *within a fixed-energy shell*, not Fock-vs-coherent. With the right criterion the object reproduces `g*`. The earlier "no prediction / sharp negative" reading was over-reached; the live threat is **re-description**, not absence of prediction. (Roster meta: the adversarial critic overturned the producer's central conclusion — the discipline working as designed.)

**What this means for the conjecture.** [PRD-001](../../3-prediction/co-admissibility-conjecture.md) claims a **witness-independent** criterion with content **beyond** einselection. The dichotomy shows there is no middle ground delivering that: witness-free is empty, witness-fixed is einselection re-described. The relevant falsifier now in play is PRD-001's **(a)** ("reproduces the witness-dependence it was meant to eliminate / predicts nothing new"), *not* (b)/(c).

**New open sub-question (the only door still ajar).** Does `γ̇` differ from standard einselection in the regime where einselection is itself **witness-dependent**? If it agrees everywhere → co-admissibility (in this form) predicts nothing new (re-description confirmed). If it differs computably → that difference is the first genuinely novel content. This is the next decisive test.

**Honest status.** **OPN-001 stays `open`** (proof_status `prose_only`). A move to `refuted` is **declined** — the result is not "no discrimination" but "discrimination only by re-description," and the re-description horn is not yet closed (the new sub-question). Labels are JD's call. Per [METHODOLOGY](../../0-program-methods/METHODOLOGY.md)/[CONTRIBUTING](../../CONTRIBUTING.md) the corrected result is a **progressive** step (a sharper, primary-source-anchored framing of exactly where the conjecture is endangered).

## Attempt 4 — the re-description test: the door closes (2026-06-26, computational)

*The decisive test of Attempt 3's open sub-question (JD: "run the test"): does `γ̇` differ from standard einselection where einselection is witness-dependent? Formalization-Agent (computational) → independent Red-Team (3rd pass, root-node). **Answer: no — re-description.***

**Artifact.** [`../../3-prediction/co-admissibility-conjecture/code/coadmissibility_redescription.py`](../../3-prediction/co-admissibility-conjecture/code/coadmissibility_redescription.py) (+ `results_redescription.json`). Deterministic, no fitted parameters.

**Result (two exact pieces):**

1. **The short-time sieve is witness-INDEPENDENT and equals `γ̇`.** For a pure state, `d/dt tr ρ^α|₀ = (α/2)·γ̇` for every Rényi index `α` (proven; verified numerically incl. non-integer α). So all Rényi-α witnesses rank pure states *identically* at `t=0` — there is no witness ambiguity at the initial-rate level, and that level *is* the `γ̇` sieve.
2. **`γ̇` reproduces standard einselection there, and is silent where einselection is witness-dependent.** The `γ̇` energy-shell critical coupling matches the analytic standard-einselection value `g* = n₀+½+√(n₀(n₀+1))` to <0.06% (n₀=2,3,4). The witness/timescale dependence Feller documents lives at **finite** observation time; the finite-`T` critical coupling drifts (real, Red-Team-confirmed) and converges *monotonically* to `γ̇`'s value as `T→0` (5.18 @ T=0.4 → 4.97 @ T=0.01 → 4.95). So `γ̇` is the exact `T→0` boundary limit — it makes no differing prediction in the witness-dependent regime; it simply does not operate there.

**Which limb of PRD-001 falsifier (a) fires (Red-Team precision).** (a) = "reproduces the witness-dependence it was meant to eliminate / **predicts nothing new**." `γ̇` is witness-*independent*, so the **first limb does not apply**. (a) fires via the **second limb**: witness-independence is bought at the cost of all novel content. The conjecture's *required* behaviour (coincide with einselection where einselection is witness-independent) is met; its *discriminating* promise (a specified, computable **difference** where einselection is witness-dependent) is **unmet** — `γ̇` is silent exactly there.

**The strongest pro-TRT counter, and why it fails.** One could say "co-admissibility = the witness-independent short-time sieve = `γ̇`" — satisfying the conjecture's witness-independent clause. But `γ̇` at `T→0` *is* standard short-time einselection (Zurek's predictability sieve at leading order = the purity-decay rate); there is zero daylight for novel content anywhere. The counter buys witness-independence by relocating co-admissibility to exactly the regime where einselection is *already* witness-independent and *already* equals `γ̇`. **`γ̇` never differs from standard einselection with added content, anywhere.**

**Status & consequence.** This **closes Attempt 3's "only door ajar"** for the `γ̇` form: the decoherence/co-admissibility descendant resolves to **re-description** — it predicts nothing beyond standard einselection on the Feller model. Recommend **PRD-001 → refuted-by-re-description** (epistemic enum lacks the value; pending JD + a possible schema addition). **OPN-001 stays `open`/`prose_only`** at the root, annotated that its *decoherence instantiation* is re-description; its surviving discriminating value rests on the **gravity** side ([PRD-002](../03-gravity/relational-graph-test.md) / keystone OPN-002). Per the methodology a recorded negative is a **progressive** resolution. **Scope:** this concerns the `γ̇`/purity criterion (the only measure-free form that discriminates at all, per Attempts 2–3); it is a primary-source-anchored re-description finding, not an impossibility proof over all conceivable criteria.
