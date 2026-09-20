# RFC: Research Program Operations Console

> **Status: PROPOSED — parked.** This RFC is captured as an open PR, not merged. The open PR *is* the marker that the idea is recorded but not yet acted on, pending the gating decision in §7. Internal-ops, generalized: it describes an operator surface for *any* research programme run under this methodology; TRT is the reference instance where it is first captured.

## 1. Problem

A research programme run under the [Popper/Lakatos methodology](../METHODOLOGY.md) generates operational state that is currently scattered: the roadmap (positive heuristic), the traceability coverage/risk reports, the appraisal verdict, open issues/conjectures, and the *history of how claims evolved* (the problemshift record). There is no single operator surface to view this across one programme — and none at all across *multiple* programmes once LRT folds in and others follow.

Two distinct needs hide inside "a console":
1. **Observe** — an at-a-glance dashboard over a programme's live state (coverage, risk, roadmap, appraisal).
2. **Drive + record** — actively run the research (spawn agents to attempt formalizations, compute tests) and record each working session as durable development history.

These have very different infrastructure cost, and conflating them is the main risk this RFC guards against.

## 2. Separation of concerns (the load-bearing seam)

- **Program repos** (`triadic-reality-theory`, future LRT-folded, others) hold the **research content** — self-contained and publicly citeable.
- **The console** is the **operator surface** that *consumes* the program repos (reads/aggregates via the GitHub API and git, drives agents, records sessions).

**Invariant: research content never lives in the console.** The console is a reader and a driver, not a store. This keeps each programme citeable and the console disposable/rebuildable. Session records are the one thing the console *writes*, and they are written back *into the program repo* (see §5), not held in the console.

## 3. Constraints

- **Peak Solutions shared infrastructure (hard constraint).** Any hosted component runs on the PeakAI box, which also runs Peak's production. It must stay strictly in the **Ologos lane**: its own container, the 18xxx port block, its own Cloudflare Tunnel hostname for `research.thinxai.net`. **Never** touch host DNS, firewall, the docker daemon, or any non-Ologos service. Anything host-level is a **petition to Jay**, not a thinx change. (See thinx `morals.md` Peak Solutions constraint.)
- **Standing surface rule.** JD's standing rule is that surfaces live on **GitHub Pages**. A *static dashboard* (§4 Phase 1) honors this directly. A *dynamic, agent-driving console* (Phase 2) genuinely cannot run on Pages (Pages serves no agents), so it is a deliberate, named exception justified only by the drive+record need.
- **Foundation maturity.** Phase 2 is intended to build on thinx / thinx-console / the aide-meta-orchestrator. The meta-orchestrator is itself in-flight (transportability recently proven, first adoption PR open). Building a console on a foundation still proving itself is a moving-target risk; Phase 2 should not start until that structure has stabilized.

## 4. Proposed phasing

### Phase 1 — now, no new infrastructure
- **In-repo session journal** (`0-program-methods/sessions/`): one dated file per working session, capturing what was attempted, what confirmed, what was *recorded as a refutation*, and which claims/issues moved. This is the problemshift history — the Lakatosian narrative the [appraisal log](../../3-prediction/appraisal.md) summarizes. Captures the development-history value immediately, independent of any console.
- **GitHub Pages dashboard**: a static render of `traceability/generated/` (coverage, dependency graph, risk) + ROADMAP + appraisal. Cheap, leverages GitHub tooling, honors the surface rule, gives the at-a-glance view today.

### Phase 2 — when warranted (see §7 gate)
- **`jdlongmire/research-console`** on PeakAI at `research.thinxai.net`: the multi-programme operator surface that drives agents and records live sessions, built on thinx / thinx-console / meta-orchestrator. Reads all program repos via the GitHub API; writes session records back into each program repo per §5.

## 5. Session recording

A session record is the durable trace of one working session. Schema (proposed): timestamp, programme, roadmap task(s) touched, agents invoked, claims/issues changed, outcome (confirmed / refuted / no-change), and a short narrative. Records are committed **into the program repo** (`0-program-methods/sessions/`) so the development history travels with the content and survives the console. In Phase 1 these are written by hand / by the working agent; in Phase 2 the console writes them automatically.

## 6. Alternatives considered

- **Build the hosted console now.** Rejected for now: TRT is at day zero (scaffold, 12 seed claims, zero research done); the gating need is Task 0.1, not operator tooling. Standing up infrastructure ahead of demonstrated need, on shared infra, against an unstable foundation, is premature.
- **Everything on GitHub Pages, no hosted console ever.** Insufficient if the genuine need is *driving* agents and recording live sessions — Pages cannot run agents.
- **Console as a content store.** Rejected: violates the §2 invariant and breaks citeability.

## 7. Open decision (gates Phase 2)

**Is the console a dashboard over output, or the workbench the research is driven from?**

- *Dashboard over output* → Phase 1 (Pages + in-repo journal) is sufficient for now; Phase 2 deferred until multi-programme volume justifies it.
- *The actual workbench* (spawn agents to attempt formalizations, record each attempt live) → Phase 2 is **not** ahead-of-need; a minimal hosted version is justified sooner, still gated on meta-orchestrator stability and the Peak-lane constraints.

Until this is answered, the recommendation is **Phase 1 only**. This PR stays open as the captured proposal.
