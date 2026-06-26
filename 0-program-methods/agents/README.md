# Agent Profiles

Reusable, harness-agnostic operating briefs for any **AI-aide** working on the TRT research programme — a Claude Code subagent, GPT, OlogosAI, a contributor's assistant. Each profile is a plain-markdown system prompt **bound to this repo's methodology** (not generic role text); load it as the aide's brief for that role.

## Division of labour (load-bearing)

| Profile | Judges | Does **not** touch |
|---|---|---|
| [`qa-agent.md`](qa-agent.md) | the **machinery** — repo hygiene, code, Lean/Python build, traceability, CI, conventions | the *truth* of claims or validity of derivations |
| [`peer-review-agent.md`](peer-review-agent.md) | the **content** — claims, derivations, conjectures, the paper, against the Popper/Lakatos methodology | code/CI/build hygiene; committing changes |

They are complementary and **defer to each other**: QA never adjudicates physics; Peer-Review never fixes code. Both **recommend**; decision authority stays human (EIF §1.2).

## How to invoke (any harness)

- **Claude Code:** spawn an `Agent` with the profile file's contents as the prompt, plus the target (a diff, a claim id, a section).
- **Any chat AI:** paste the profile as the system/opening message, then the target.
- **Workflow/automation:** read the profile as the agent's system prompt.

Always give the aide: the profile + the specific target + access to the repo (or the relevant files). The profile tells it what to read next.

## Profile template

Every profile carries: **Role**, **Mandate** (one line), **Scope** (in / out), **Inputs**, **Procedure**, **Output** (format), **Methodology bindings** (which repo rules it enforces), **Boundaries** (must-not), **Authority** (recommend vs decide).

## Current profiles

- [**QA-Agent**](qa-agent.md) — repository & code-development hygiene gate (the *machinery*).
- [**Peer-Review-Agent**](peer-review-agent.md) — adversarial scientific/philosophical review (the *content*).
- [**Formalization-Agent**](formalization-agent.md) — turns a prose claim into Lean/computational form and wires it through traceability (the *generative* counterpart to QA; aimed at critical-path Task 0.1).
- [**Red-Team-Reviewer**](red-team-reviewer.md) — peer-review specialization that *attacks the root node*: tries to show co-admissibility needs a free measure or collapses to einselection.

## Invocation triggers (when to dispatch which)

An AI-aide working the programme should reach for a profile when its trigger fires — spawn a subagent loaded with that profile (or adopt it inline for a quick pass). Natural-language phrasings map to the same dispatch.

| Trigger | Profile | NL phrasings |
|---|---|---|
| Before any commit/PR of code, scripts, Lean, or traceability; at session-wrap; reviewing a diff for hygiene | **QA-Agent** | "QA this", "hygiene check", "run QA" |
| Evaluating a claim/section/conjecture's content; before accepting a contribution as progressive; on receiving an external review | **Peer-Review-Agent** | "peer-review X", "review this claim", "progressive or degenerating?" |
| Working a formalization task (Task 0.1, an `OPN-*` claim, belt/prediction Lean, a computational test) | **Formalization-Agent** | "formalize OPN-N", "Lean this claim", "work Task 0.1" |
| Before accepting any conjecture as resolved/confirmed; on Formalization-Agent output; before an appraisal moves toward *progressive* | **Red-Team-Reviewer** | "red-team the co-admissibility conjecture", "try to break this" |

**Chaining:** a formalization pass is *produced* by Formalization-Agent → checked by QA-Agent (build/hygiene) → attacked by Red-Team-Reviewer (validity) → general Peer-Review for label calibration. Nothing is accepted on a single role's say-so, and all recommend while a human decides.
