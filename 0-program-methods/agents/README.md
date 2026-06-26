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

- **QA-Agent** — repository & code-development hygiene gate.
- **Peer-Review-Agent** — adversarial scientific/philosophical review.

## Proposed (not yet built — see the program lead)

- **Formalization-Agent** — turns a prose claim into Lean/computational form and wires it through traceability (the generative counterpart to QA's checking; aimed at the critical-path Task 0.1).
- **Red-Team-Reviewer** — a peer-review specialization that *attacks the root node*: tries to show co-admissibility needs a free measure or collapses to einselection.
