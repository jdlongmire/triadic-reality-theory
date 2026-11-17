/-
  Triadic Reality Theory — CPIT Pair-Failure Countermodels
  Formalization of the pair-failure half of the Co-Primitive Irreducibility
  Theorem (CPIT, theorem candidate v0.1, WP-TRT-LRT-ONTO-0001, 2026-09-19),
  per the approved design note (2026-11-12).

  For each pair of co-primitives, one concrete finite structure is exhibited
  in which the third component is absent, the other two are present and
  functional, and no state is determinate-actual. The constitutive conditions
  are fixed in advance (design note section 2): a state counts as
  determinate-actual iff it is differentiated (I role), its content is
  determinate and passes the structure's admissibility gate (L role), and it
  is the terminus of a transition (A role).

  Vocabulary mapping to Core/Primitives.lean: `rep` and differentiation carry
  the I role, `Det` and `adm` carry the L role, `trans` is A (an independently
  typed transition relation, never defined as "whatever actualizes"), and
  `DetAct` is structure-relative X. Terminology warning: CPIT's D means
  determinate actuality, the constituted target; the hard core's D means the
  actualizable domain. `DetAct` is CPIT's sense. This module does not import
  or modify Primitives.lean, whose fixed opaque constants cannot vary across
  structures.

  Scope: pair-insufficiency of the components as independent data, relative
  to the stated conditions. This is not a proof of metaphysical independence
  or of non-definability of any primitive from the other two, and it does not
  close the A-reduction challenge left open by WP-TRT-CORE-0001.
-/
namespace Trt.Core.Cpit

/-- Contents over two atoms. Each atom carries a positive and a negative
    same-respect component: ((p, not-p), (q, not-q)). -/
abbrev Content := Prod (Prod Bool Bool) (Prod Bool Bool)

/-- Determinacy of content (the L-condition): no atom is affirmed and denied
    in the same respect. Fixed once, for all structures; not structure data. -/
abbrev Det (c : Content) : Prop :=
  Not (c.1.1 /\ c.1.2) /\ Not (c.2.1 /\ c.2.2)

/-- A triadic structure: the data by which the three roles could be present. -/
structure Structure where
  State : Type
  rep : State -> Content          -- I role: differentiation of states into contents
  adm : Content -> Prop           -- L role as gate: the structure's admissibility filter (the D-gate)
  trans : State -> State -> Prop  -- A role: transition relation

/-- x is differentiated: x is the unique bearer of its content. -/
abbrev Differentiated (M : Structure) (x : M.State) : Prop :=
  forall y, M.rep y = M.rep x -> y = x

/-- Determinate actuality, structure-relative (CPIT's target; the X-side of
    the hard core's map). All three constitutive conditions. -/
abbrev DetAct (M : Structure) (x : M.State) : Prop :=
  Differentiated M x /\ Det (M.rep x) /\ M.adm (M.rep x) /\ exists y, M.trans y x

/-- L is present as a working gate iff the structure's filter enforces
    determinacy (the model-level content of actualizable -> L3-admissible). -/
abbrev Lawful (M : Structure) : Prop :=
  forall c, M.adm c -> Det c

/-- Determinate content: atom p affirmed. -/
def P : Content := ((true, false), (false, false))

/-- Determinate content: atom q affirmed. -/
def Q : Content := ((false, false), (true, false))

/-- Contradictory content: atom p affirmed and denied in the same respect. -/
def PB : Content := ((true, true), (false, false))

/-- Contradictory content: atom q affirmed and denied in the same respect. -/
def QB : Content := ((false, false), (true, true))

/-- Lemma 1 model: L and I present and functional, A absent. -/
abbrev modelNoA : Structure where
  State := Fin 2
  rep := fun i => if i = 0 then P else Q
  adm := Det
  trans := fun _ _ => False

/-- Lemma 2 model: L and A present and functional, I absent. -/
abbrev modelNoI : Structure where
  State := Fin 2
  rep := fun _ => P
  adm := Det
  trans := fun _ _ => True

/-- Lemma 3 model: I and A present and functional, L absent (no filter). -/
abbrev modelNoL : Structure where
  State := Fin 2
  rep := fun i => if i = 0 then PB else QB
  adm := fun _ => True
  trans := fun _ _ => True

/-- CPIT Lemma 1: L + I without A. Admissible, differentiated,
    determinacy-passing states exist; nothing transitions; nothing is
    determinate-actual, and the only failing condition is the A-condition. -/
theorem lemma1_LI_without_A :
    (forall x y, Not (modelNoA.trans y x))
    /\ (forall x, Differentiated modelNoA x /\ Det (modelNoA.rep x)
        /\ modelNoA.adm (modelNoA.rep x))
    /\ (forall x, Not (DetAct modelNoA x)) := by decide

/-- CPIT Lemma 2: L + A without I. Transitions fire maximally and every
    state's content is admissible and determinate; representation is
    constant, so no state is differentiated and none is determinate-actual. -/
theorem lemma2_LA_without_I :
    (forall x y, modelNoI.rep x = modelNoI.rep y)
    /\ (forall x y, modelNoI.trans y x)
    /\ (forall x, Det (modelNoI.rep x) /\ modelNoI.adm (modelNoI.rep x))
    /\ (forall x, Not (DetAct modelNoI x)) := by decide

/-- CPIT Lemma 3: I + A without L. Representation separates the states and
    transitions fire maximally and the gate admits everything; both states
    bear same-respect contradictory contents, so neither is determinate,
    and neither is determinate-actual. -/
theorem lemma3_IA_without_L :
    (forall c, modelNoL.adm c)
    /\ (forall x y, modelNoL.rep x = modelNoL.rep y -> x = y)
    /\ (forall x y, modelNoL.trans y x)
    /\ (forall x, Not (Det (modelNoL.rep x)))
    /\ (forall x, Not (DetAct modelNoL x)) := by
  refine ⟨fun _ => trivial, by decide, fun _ _ => trivial, by decide, by decide⟩

/-- CPIT section 5, pair-failure half, packaged. -/
theorem cpit_pair_failure :
    (forall x, Not (DetAct modelNoA x))
    /\ (forall x, Not (DetAct modelNoI x))
    /\ (forall x, Not (DetAct modelNoL x)) := by decide

/-- The minus-A structure's gate enforces determinacy: L is present. -/
theorem lawful_modelNoA : Lawful modelNoA := fun _c h => h

/-- The minus-I structure's gate enforces determinacy: L is present. -/
theorem lawful_modelNoI : Lawful modelNoI := fun _c h => h

/-- The minus-L structure is the only unlawful one: its gate admits the
    contradictory content PB, so L is absent as a working gate. -/
theorem not_lawful_modelNoL : Not (Lawful modelNoL) :=
  fun h => (h PB trivial).1 ⟨rfl, rfl⟩

/-- The necessity direction, included for completeness and labelled for what
    it is: definitional, given the constitutive conditions. This is the
    formal counterpart of CPIT's boxed D => (L and I and A), and it carries
    no independent weight. -/
theorem detAct_conditions (M : Structure) (x : M.State) (h : DetAct M x) :
    Differentiated M x /\ Det (M.rep x) /\ exists y, M.trans y x :=
  And.intro h.1 (And.intro h.2.1 h.2.2.2)

end Trt.Core.Cpit
