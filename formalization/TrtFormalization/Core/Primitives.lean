/-
  Triadic Reality Theory — Core: Primitives  (Tier 1, hard core)

  Encodes the four-tier engine and the central identity χ ≡ A(I∞ | L₃).

  This file is deliberately Mathlib-free so it typechecks standalone. The heavier
  belt derivations (Born rule, gravity reduction) and the imported LRT L₃-core
  (formalization/lrt/) require Mathlib.

  Module ⇄ tier:  Core ⇄ 1-hypothesis,  Belt ⇄ 2-theory,  Prediction ⇄ 3-prediction.
-/
namespace Trt.Core

/-- Tier 1 (representable): any well-formed structure in `I∞`, including
    contradiction-encoding ones. Abstract carrier; representability requires only
    well-formedness, not logical admissibility. -/
opaque Representable : Type

/-- `L₃` admissibility — the finite logical constraint {Identity, Non-Contradiction,
    Excluded Middle} as a predicate over the representable. A structure is admissible
    iff it survives `L₃`. -/
opaque L3Admissible : Representable → Prop

/-- Tier 2 (admissible): `I_adm = I∞ | L₃` — the representable filtered by `L₃`. -/
def Admissible : Type := { r : Representable // L3Admissible r }

/-- Whether actualizing action `A` has realized an admissible structure. -/
opaque Actualized : Admissible → Prop

/-- Tier 3 (actual): the members of `χ` that `A` has realized. -/
def Actual : Type := { a : Admissible // Actualized a }

/-- `χ` — actualized reality:  χ ≡ A(I∞ | L₃). -/
abbrev Chi : Type := Actual

/-- Outcome-actuality — the determinate result of a measurement. A quantum state is
    admissible and real but not outcome-actual (the tier distinction of paper §6.5). -/
opaque OutcomeActual : Actual → Prop

/-- The gate between the representable and the actual is `L₃`: every actual structure
    is `L₃`-admissible. Holds by construction here; a model that derives it from a
    dynamics is belt work. This is the negative-heuristic invariant in formal form. -/
theorem actual_is_admissible (a : Actual) : L3Admissible a.val.val :=
  a.val.property

end Trt.Core
