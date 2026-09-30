# Semantic Collision Audit

**WP:** WP-TRT-QSA-0001  
**Date:** 2026-09-30  
**Status:** Step 1 audit, initial canonical/active-surface pass  
**Rule:** preserve Level 0 canon `χ ≡ 𝒜(I | L)`; classify before refactoring.

## Executive finding

The repository contains a real semantic collision around `χ`, actuality, actualization, and quantum selection. The collision is present in active canonical and protective-belt artifacts, not only in historical work.

The compact equation remains coherent as Level 0 shorthand. The collision appears when its compressed terms are used as if they had one univocal Level 1 type.

## Classification key

- **C0 — compact-compatible:** safe at Level 0.
- **C1 — typed-compatible:** already distinguishes the needed Level 1 category.
- **O — overloaded:** one symbol/term carries multiple Level 1 types.
- **Q — quantum-specific collision:** state-instantiation, basis/context specification, or determinate outcome are conflated.
- **H — historical:** preserve provenance; annotate rather than silently rewrite.
- **R — revision candidate:** active artifact should be reconciled after notation freeze.

## Collision matrix

| Surface | Current usage | Class | Finding | Required disposition |
|---|---|---:|---|---|
| `README.md` | `X/χ` = actualized reality / what obtains; compact equation | C0/O/R | Good Level 0 entry point, but `χ` is domain-wide rather than fact-typed | Preserve compact equation; add Level 1 pointer after notation freeze |
| `1-hypothesis/hard-core.md` | Actual `X/χ` = content that obtains; `A` primitive transition; actualization is role of A | C0/C1/O/R | Correct primitive distinction; `χ` remains broad | Preserve hard core; type downstream `χ_q` without replacing Level 0 |
| `TRT-v0.10.md` | `χ` = what obtains, actual reality, actualized domain; derivative `χ_actual, χ_t, χ_phys, χ_obs, χ_adm`; quantum “outcome-actual” | O/Q/R | Highest-density active collision | Controlled revision required after notation decision |
| `Core/Primitives.lean` | `Actual` = subtype of actualizable states satisfying `Obtains`; `Chi := Actual`; `OutcomeActual : Actual → Prop` | C1/O/R | Already has a useful domain/outcome distinction, but `Chi` aliases whole Actual domain/type | Candidate foundation for `X` domain + fact predicate rather than redefining primitive |
| `state-transition-and-actualization-framework.md` | `X/χ` = what obtains; actualization distinguished from primitive A | C0/O/R | Compatible with compact canon but broad `χ` | Add typed downstream clarification |
| `actuality-actualization-disambiguation.md` | `χ` = total actual domain/result; `A` = actuality-conferring operator; alpha = actuality status | H/O | Predates CORE-0001 and conflicts with primitive-A normalization | Preserve as historical research; add supersession note, do not silently rewrite |
| `actualization-resolution.md` | A “resolves” unresolved superposition into determinate outcome | Q/R | Treats resolution as role of primitive A but lacks Spec/Settled typing | Refactor into derived action roles after notation freeze |
| `born-rule.md` | decoherence/einselection selects co-admissible set; further selection gives one `χ`; `D → χ` residual actualization event | Q/R | Conflates at least context/set selection and determinate settlement; risks making decoherence a primitive selection stage | Recast as downstream specifying action vs settling action; retain empirical claims only where independently warranted |
| `non-bivalent-physics-adversarial-background.md` | `χ` = completed physical informational actualization; bivalence asserted at `P_χ`; pre-χ may be non-bivalent | C1/Q/R | Closest existing artifact to new fact typing, but “pre-χ” can wrongly imply physically instantiated ψ is not actual | Replace pre/post actuality language with state-instantiated vs determinate-fact typing |
| `WP-TRT-CORE-0001` | `χ` = what obtains; A primitive transition/change; actualization a role/consequence of A | C0/H | Governing completed normalization; must not be silently changed | Preserve; QSA must reconcile beneath it |
| `WP-TRT-LRT-ONTO-0001` artifacts | mixed `χ` total-domain, actualized result, actuality status, selection/agency bridges | H/O | Research history contains pre-normalization alternatives | Preserve provenance; annotate only where referenced by active canon |
| `WP-TRT-QSA-0001` | Level 0 compact canon plus candidate Level 1 `α, Spec, q, Settled, χ_q` | C1 | Current reconciliation locus | Continue to notation freeze and adversarial test |

## Primary collisions

### 1. χ overload

At least four senses occur:

1. **Compact Level 0 result:** the result of `𝒜(I | L)`.
2. **Actual domain/type:** all content that obtains.
3. **Physically instantiated state:** an actual physical state such as a prepared quantum state.
4. **Determinate fact/outcome:** a settled proposition/value under a fixed respect.

The QSA proposal should not erase sense (1). It must prevent senses (2)-(4) from being treated as identical at Level 1.

### 2. A / actualization overload

CORE-0001 correctly fixes primitive A as non-temporal state transition/change. Active belt artifacts still use “A resolves,” “A actualizes,” and “actualization event” in ways that can be read as separate operators or as the primitive definition.

Candidate repair: keep primitive Action; type specification and settling as derived roles of an action occurrence `α`.

### 3. Selection overload

The corpus uses selection for at least:

- logical filtering/co-admissibility;
- decoherence/einselection or pointer-state stabilization;
- choice/specification of observable/context/respect;
- selection of one determinate outcome/value.

These are not one operation. QSA should reserve “specification” for bounding `q` and “settling” for determinate `χ_q`, while using decoherence/einselection only for the physical process established by the relevant model.

### 4. State actuality versus fact actuality

The current “pre-χ / post-χ” language is unsafe for quantum states. A prepared superposition may be physically instantiated and therefore actual as a state while no represented basis alternative is thereby a settled determinate value.

Candidate distinction:

`Inst(σ)` = physically instantiated informational state.

`χ_q` = determinate fact under bounded `q`.

In general:

`Inst(σ) ≠ χ_q`.

### 5. L₃ scope

CORE-0001 gives L₃ a broad ontological-admissibility role. QSA proposes an especially explicit role for L₃ at determinate `χ_q`. The latter must not be written as “L₃ applies only to χ_q” unless a separate argument narrows the existing hard-core claim.

## Initial notation recommendation for Step 2

Do not redefine bare `χ` yet.

Test this strategy first:

- retain bare `χ` exclusively as Level 0 compact result in exposition;
- retain `X` / `Actual` for the typed actual domain;
- use `Inst(σ)` for physical state-instantiation;
- use `α : Act` for an action occurrence;
- use `Spec(α,σ,q)` as a relation rather than a partial function until uniqueness is proved;
- use `Settled(α,q,χ_q)` as a relation until uniqueness is proved;
- use `χ_q` only for determinate fact actuality under fixed `q`.

This avoids overloading `A`, avoids prematurely assuming specification or settlement are functional, and preserves the original compact equation.

## Immediate revision queue after notation freeze

1. `1-hypothesis/paper/TRT-v0.10.md`
2. `1-hypothesis/hard-core.md`
3. `README.md`
4. `formalization/TrtFormalization/Core/Primitives.lean`
5. `2-theory/00-foundational/state-transition-and-actualization-framework.md`
6. `2-theory/00-foundational/actualization-resolution.md`
7. `2-theory/02-variational/born-rule.md`
8. `2-theory/00-foundational/non-bivalent-physics-adversarial-background.md`

Historical ONTO artifacts should receive supersession/interpretation notes only where active navigation could cause ambiguity.

## Audit conclusion

Step 1 confirms that QSA addresses a genuine type problem. No evidence from this pass requires abandoning the three co-primitives or the compact identity. The lowest-cost reconciliation is to preserve Level 0 and introduce typed Level 1 distinctions beneath it.

Next gate: freeze Level 1 notation before editing any canonical artifact.
