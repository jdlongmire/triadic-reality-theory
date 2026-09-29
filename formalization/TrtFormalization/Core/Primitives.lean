/-
  Triadic Reality Theory — Core Primitives
  Canonical normalization: WP-TRT-CORE-0001 (2026-09-29)

  Typed distinctions are encoded without assuming that L₃ coherence is sufficient
  for metaphysical actualizability. Primitive action A is kept distinct from the
  predicate that a state actually obtains.
-/
namespace Trt.Core

/-- R: representable informational content. This carrier expresses I∞ at the
    formal abstraction level. Representability alone carries no coherence,
    modal, or actuality entailment. -/
opaque Representable : Type

/-- Necessary L₃ filter: Identity, Non-Contradiction, Excluded Middle as an
    admissibility predicate over representable content. -/
opaque L3Admissible : Representable → Prop

/-- D-predicate: metaphysical actualizability. This is intentionally independent
    of L3Admissible so the formalization does not smuggle in the unproved
    sufficiency claim L₃-admissible → actualizable. -/
opaque Actualizable : Representable → Prop

/-- Canonical hard-core direction: every actualizable state must satisfy L₃. -/
axiom actualizable_is_l3_admissible
  (r : Representable) : Actualizable r → L3Admissible r

/-- D: the typed domain of actualizable representable states. -/
def ActualizableState : Type := { r : Representable // Actualizable r }

/-- Primitive A: fundamental state transition/change. No temporal parameter is
    built into the relation. Physical time and dynamics are downstream work. -/
opaque A : ActualizableState → ActualizableState → Prop

/-- X: whether an actualizable state obtains. Actuality is distinct from A so A
    is not defined circularly as "actualizing action." -/
opaque Obtains : ActualizableState → Prop

/-- X / χ: actualized reality. -/
def Actual : Type := { d : ActualizableState // Obtains d }
abbrev Chi : Type := Actual

/-- Every actual state is actualizable, by construction of X from D. -/
theorem actual_is_actualizable (x : Actual) : Actualizable x.val.val :=
  x.val.property

/-- Every actual state therefore satisfies the necessary L₃ filter. -/
theorem actual_is_l3_admissible (x : Actual) : L3Admissible x.val.val :=
  actualizable_is_l3_admissible x.val.val x.val.property

/-- Outcome actuality remains a downstream measurement distinction. -/
opaque OutcomeActual : Actual → Prop

end Trt.Core
