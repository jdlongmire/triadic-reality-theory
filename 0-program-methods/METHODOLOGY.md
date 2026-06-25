# Methodology — Popper, Lakatos, and the Falsifiability Ladder

This repository is structured as a **Lakatosian research programme** and governed by a **Popperian** standard of demarcation. The directory layout is not filing; it is the methodology made structural. This file states the apparatus and how each tier realizes it.

---

## The two standards

**Popper** (*The Logic of Scientific Discovery*, 1959; *Conjectures and Refutations*, 1963). Demarcation by **falsifiability**: a claim is scientific iff it *forbids* something — exposes itself to a risky test that could refute it. Progress is bold conjecture met by severe attempted refutation. There is no verification, only corroboration (surviving tests) and falsification. Ad hoc moves that *reduce* falsifiability are illegitimate (the "conventionalist twist").

**Lakatos** (*The Methodology of Scientific Research Programmes*, 1970). The unit of appraisal is not a lone theory but a **programme** with three parts:
- a **hard core** of fundamental commitments, held immune from refutation by the *negative heuristic* (do not aim modus tollens at the core);
- a **protective belt** of auxiliary hypotheses that surround the core and take the brunt of refutation — they get adjusted;
- a **positive heuristic**: an articulated plan for developing the refutable variants.

A programme is **progressive** if it predicts *novel facts* and some corroborate; **degenerating** if it only accommodates facts post hoc. Lakatos is the friendly amendment to Popper: Popper supplies the severe-test standard, Lakatos rehabilitates a *principled, limited* immunity for the core while keeping falsificationism at the belt.

---

## The tier mapping

The baselines form a **falsifiability gradient** — each tier is more exposed to refutation than the one above. The programme's job is to push claims *down* the ladder toward falsifiability.

| Tier | Lakatos/Popper role | Holds |
|---|---|---|
| **[0-program-methods](.)** | The frame that *governs* the ladder (not on it) | VSOK (vision/strategy/OKRs), this methodology, the ROADMAP (= the **positive heuristic**) |
| **[1-hypothesis](../1-hypothesis/)** | **Hard core** + negative heuristic | The ontology, primitives, four-tier engine, χ≡A(I∞\|L₃), the position paper |
| **[2-theory](../2-theory/)** | **Protective belt** + execution of the positive heuristic | The adjustable formal work: co-admissibility criterion, Born-rule derivation, gravity reduction |
| **[3-prediction](../3-prediction/)** | **Popperian severe test** + progressive/degenerating appraisal | The risky claims that *forbid* something; their test protocols; the [appraisal log](../3-prediction/appraisal.md) |

The two transitions name the program's two governing tasks:
- **1 → 2** ("formalization is the bottleneck"): move a hard-core commitment into a testable belt theory.
- **2 → 3** ("earn the status of physics"): produce a progressive, novel-fact prediction.

---

## The hard core is immune *by necessity*, not merely by convention

This is where TRT claims more than a standard programme. Orthodox Lakatos fixes the hard core by methodological *decision* — a core could in principle have been chosen otherwise. TRT's logical constituent *L₃* is fixed by **transcendental necessity**: its denial is self-refuting, because the denial deploys identity and non-contradiction to be stated at all (paper §7.1, after Aristotle's *Metaphysics* Γ). This answers Popper's standing distrust of immunized cores: the immunity here is *earned by necessity*, not asserted by convention.

We state this divergence from orthodox Lakatos openly rather than glossing it. The remainder of the core (the co-requirement structure, the synthetic necessity of the triad) rests on one explicit metaphysical posit — *actuality is a genuine status distinct from possibility* (paper §9.3) — which is adopted in the open, not buried.

---

## The change-legitimacy criterion (governs contributions)

Every change to the programme is judged by the progressive/degenerating standard, which is the principled justification for the [contribution rules](../CONTRIBUTING.md):

- **Progressive (accept):** adds novel content, sharpens a test, formalizes a previously prose-only claim, or *records a refutation* (a decided conjecture — success **or** failure — is a progressive resolution).
- **Degenerating (decline):** ad hoc accommodation that reduces falsifiability; inflating a confidence label; removing a failure condition; presenting *interpretation* (re-description of known physics in TRT's terms) as *derivation*.

The interpretation-vs-derivation line is the demarcation self-test: a contribution that only re-describes known physics is interpretation; one that forbids something new is a candidate progressive step.

---

## The machine-checkable form

The [`traceability/`](../traceability/) layer is this methodology rendered auditable. Every claim carries a `role` (hard-core / belt / prediction / imported / open), a `proof_status`, an `epistemic_status` (the confidence label), a `depends_on` graph (kept acyclic — the circularity discipline), a `risk_if_false` (the failure condition), and — for predictions — a `falsifies` field (the Popperian refutation condition). The generated coverage and risk reports are the programme's standing self-appraisal.

Confidence labels throughout the repository use the convention: **HIGH · MEDIUM · LOW · UNCERTAIN** (and, in traceability, the schema enum `established / argued / conjectured / open`).
