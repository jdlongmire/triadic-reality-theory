# Triadic Reality Theory (TRT)

A foundational-ontology research program proposing that physical reality is **constrained information in action**: the convergence of finite logical constraint (*L₃*), infinite informational potential (*I∞*), and actualizing action (*A*), yielding actualized reality (*χ*).

$$\chi \equiv \mathsf{A}(I_\infty \mid L_3), \qquad \delta\mathcal{S}[\chi] = 0$$

**Status: TRT v0.9 — a coherent position paper, not yet a formalized theory.** It is genuinely open to falsification. Its discipline is the maintenance of honest confidence labels and stated failure conditions; that discipline is the asset.

---

## How this repository is structured

The layout is a **[Lakatosian research programme](0-strategy/METHODOLOGY.md)** governed by a **Popperian** standard. The tiers form a *falsifiability gradient* — each more exposed to refutation than the one above — and the programme's work is to push claims *down* the ladder toward falsifiability.

| Tier | Role | Contents |
|---|---|---|
| **[0-strategy/](0-strategy/)** | Strategy + methodology (governs the ladder) | [VSOK](0-strategy/vsok.md) · [METHODOLOGY](0-strategy/METHODOLOGY.md) (Popper/Lakatos) · [ROADMAP](0-strategy/ROADMAP.md) (the positive heuristic) |
| **[1-hypothesis/](1-hypothesis/)** | **Hard core** — immune by necessity | [hard-core.md](1-hypothesis/hard-core.md) · [the position paper](1-hypothesis/paper/TRT-v0.9.md) |
| **[2-theory/](2-theory/)** | **Protective belt** — formalization work | co-admissibility · Born rule · gravity reduction · [open problems](2-theory/open-problems.md) |
| **[3-prediction/](3-prediction/)** | **Severe tests** — falsifiable claims | [co-admissibility conjecture](3-prediction/co-admissibility-conjecture.md) · [gravity test](3-prediction/gravity-linearity-test.md) · [appraisal](3-prediction/appraisal.md) |

Supporting: **[formalization/](formalization/)** (Lean 4 + Mathlib, with the [LRT formal core](formalization/lrt/) as a sub-project), **[traceability/](traceability/)** (claim ↔ proof ↔ prose audit), **[references/](references/)**, **[reviews/](reviews/)**.

## The central thesis

Physical reality is neither brute material substance, nor abstract law, nor information alone. The finite laws of logic provide the conditions of coherent admissibility; infinite informational potential provides the domain of possible distinction; actualizing action brings logically admissible possibility into determinate actuality. Their convergence is reality.

## What is and is not claimed

TRT is a candidate foundational ontology and research program, not a completed physical theory. It has two physics-facing conjectures (co-admissibility in decoherence; gravity as global co-admissibility), both currently **LOW/UNCERTAIN**. It offers one **MEDIUM**-confidence retrodiction (the effectiveness of mathematics). The variational and gravitational machinery are targets, not derivations. See the paper's §12–§13 and the [ROADMAP](0-strategy/ROADMAP.md).

## Current frontier

The gravity conjecture has been reduced to a single sharp question about the nature of actualizing action *A*: does it resolve unsatisfiable relational structure by direct **obstruction-registration** (→ General Relativity) or by **best-fit projection** (→ modified gravity)? The same question appears to govern quantum measurement resolution. See [`2-theory/00-foundational/actualization-resolution.md`](2-theory/00-foundational/actualization-resolution.md).

## Traceability

Full claim-to-proof traceability is a first-class goal. Every claim is tracked with its role, proof status, epistemic status, dependency graph, failure condition, and (for predictions) its Popperian refutation condition. See [`traceability/`](traceability/).

## Relation to Logic Realism Theory (LRT)

TRT is the broader ontology within which LRT is situated: **TRT → LRT → LRM → predictions**. LRT formalizes TRT's *L₃* constituent. Its verified Lean formal core is imported here as a sub-project at [`formalization/lrt/`](formalization/lrt/).

## Citation

See [`CITATION.cff`](CITATION.cff).

## License

Prose and documents: **CC BY 4.0**. Code and formal artifacts: **Apache 2.0**.
