# CPIT Pair-Failure Formalization: Results

**Work package:** WP-TRT-LRT-ONTO-0001
**Subject:** Co-Primitive Irreducibility Theorem (CPIT), theorem candidate
v0.1, 2026-09-19 (co-primitive-irreducibility-theorem.md, this folder)
**Date:** 2026-11-12
**Artifact:** formalization/TrtFormalization/Core/Irreducibility.lean
(namespace Trt.Core.Cpit), imported by formalization/TrtFormalization.lean.
Core/Primitives.lean is not modified.
**Toolchain:** Lean v4.28.0 (repo pin). The module is Mathlib-free and
imports nothing.

## What was proved

The pair-failure half of CPIT (its sections 2 to 5), as three checked finite
countermodels plus a packaged corollary. The constitutive conditions were
fixed in advance, extracted from the hard core and CPIT (design note,
2026-11-12, section 2): a state counts as determinate-actual (predicate
DetAct) iff it is differentiated (it is the unique bearer of its content;
the I role), its content is determinate under the fixed predicate Det
(same-respect Non-Contradiction; the L role) and passes the structure's
admissibility gate adm, and it is the terminus of a transition (the A role,
predicate trans). Contents range over a sixteen-content space: two atoms,
each with a positive and a negative same-respect component.

- **lemma1_LI_without_A** (L + I, no A). In modelNoA the two states bear the
  distinct determinate contents P and Q; the gate is Det itself, which
  visibly excludes the contradictory contents PB and QB also present in the
  content space; every state is differentiated, determinate, and admissible;
  the transition relation is empty; and no state is DetAct. The A-condition
  is the only failing condition. This is CPIT Lemma 1's catalogue point made
  finite: a complete admissible differentiated specification instantiates
  nothing.
- **lemma2_LA_without_I** (L + A, no I). In modelNoI the representation map
  is constant at P into the full rich content space; transitions fire
  between every pair; every state's content is determinate and admissible;
  no state is differentiated, because the two states are content-identical,
  and none is DetAct. The failure is attributed to representation, not to
  the universe: the alternative one-point content space was rejected at
  design time for exactly that reason.
- **lemma3_IA_without_L** (I + A, no L). In modelNoL the two states bear PB
  and QB, the two distinct same-respect contradictory contents, so
  representation is injective and differentiation holds; transitions fire
  between every pair; the gate admits everything (no filter, which is what
  L's absence means at the gate); no state's content satisfies Det, and no
  state is DetAct. Contradictory contents remain representable, as in every
  model here; only in this one do they reach transition termini unfiltered.
- **cpit_pair_failure.** The three failures packaged: no state of modelNoA,
  modelNoI, or modelNoL is DetAct (CPIT section 5, pair-failure half).
- **Gate certificates.** lawful_modelNoA and lawful_modelNoI certify that
  the minus-A and minus-I structures' gates enforce determinacy (L present
  as a working gate). not_lawful_modelNoL certifies that the minus-L
  structure is the only unlawful one: its gate admits the contradictory
  content PB. The attribution of each failure to exactly one missing
  component is thereby explicit.
- **detAct_conditions.** The necessity direction: any DetAct state is
  differentiated, has determinate content, and is a transition terminus.
  Included for completeness and labelled for what it is: definitional,
  given the constitutive conditions. It is the formal counterpart of CPIT's
  boxed necessity claim and carries no independent weight.

## Terminology mapping (read this before citing)

The corpus uses "D" in two senses, and this formalization keeps them apart.

- **DetAct** (the module's target predicate) is determinate actuality in
  CPIT's sense: the constituted target of the irreducibility claim.
- **CPIT's "D"** means determinate actuality, as above. Where CPIT writes D,
  read DetAct.
- **The hard core's "D"** means the actualizable domain (ActualizableState
  in Core/Primitives.lean), the middle term of the architecture
  R --L3--> D --A--> X. DetAct sits on the X-side of that map, not at D.
- Module vocabulary against the core's: rep and Differentiated carry the I
  role; Det and adm carry the L role; trans is A, an independently typed
  transition relation, never defined as "whatever actualizes"; DetAct is
  structure-relative X.

## Build evidence

- Standalone check: `lean TrtFormalization/Core/Irreducibility.lean`
  (Lean 4.28.0, no imports), exit code 0, no errors or warnings.
- Project build: `lake build` in formalization/, exit code 0.
  Output line: "Build completed successfully (5 jobs)", with
  TrtFormalization.Core.Irreducibility built as job 3 of 5.
- Sorry scan: zero occurrences of `sorry` or `admit` as tactics in the new
  module (comment text excluded from the scan).
- Proofs close by `decide` or by short explicit arguments, as designed.
  The three lemmas and the corollary depend only on the standard axioms
  propext and Quot.sound; no Classical.choice, no sorryAx, and no
  TRT-specific axiom. In particular the core's declared axiom
  actualizable_is_l3_admissible does not touch these results: the module
  does not use the core's Actualizable/Obtains vocabulary.

## Axiom audit (verbatim)

Output of `#print axioms` for the module's theorems, run against the built
project (Lean 4.28.0):

```text
'Trt.Core.Cpit.lemma1_LI_without_A' depends on axioms: [propext, Quot.sound]
'Trt.Core.Cpit.lemma2_LA_without_I' depends on axioms: [propext, Quot.sound]
'Trt.Core.Cpit.lemma3_IA_without_L' depends on axioms: [propext, Quot.sound]
'Trt.Core.Cpit.cpit_pair_failure' depends on axioms: [propext, Quot.sound]
'Trt.Core.Cpit.detAct_conditions' does not depend on any axioms
'Trt.Core.Cpit.lawful_modelNoA' depends on axioms: [propext]
'Trt.Core.Cpit.lawful_modelNoI' does not depend on any axioms
'Trt.Core.Cpit.not_lawful_modelNoL' depends on axioms: [propext]
```

## Limits: what this does not prove

- **Not metaphysical independence, and not non-definability.** A
  countermodel shows the pair, as independent data, does not suffice. It
  does not show that no derivation of the third component from the pair
  exists. CPIT does not claim otherwise, and neither does this filing.
- **Not the necessity of the triad as a derived result.** The necessity
  direction above is definitional. The companion necessity analysis
  (co-primitive-necessity.md, this folder) leaves its joint-sufficiency
  target explicitly not yet derived; nothing here derives it.
- **Not the full L3 package.** The countermodels test the determinacy core
  of L, same-respect Non-Contradiction, which is the law with discriminating
  work in Lemma 3. Identity is carried by content identity in the encoding,
  and Excluded Middle, per the 2026-11-12 scoping, binds propositions over
  actualized states, the level at which the target predicate is defined.
- **Not I-infinity's unboundedness.** Differentiation is formalized at
  CPIT's own minimal strength: unique bearer of content, distinction
  between states. No finite model captures unbounded representability, and
  pair-failure needs only the minimal notion.
- **Nothing about Mind, substance, a bearer, or perfection.** CPIT section
  10 rates "CPIT -> Mind: NOT CLAIMED." This work does not touch it.
- **Not the second clause of charter obligation 1** (resistance to collapse
  into a single primitive under three aspects). A monoprimitive wearing
  three aspects is a different reduction shape from a missing component;
  these countermodels do not test it.
- **Not a closure of the WP-TRT-CORE-0001 A-reduction challenge.** That
  review's open challenge asks whether A can be eliminated without
  explanatory loss, and its residual burden is to make the
  representation/efficacy distinction rigorous. This formalization makes
  half of that distinction rigorous inside its framework: representation is
  exactly the rep/adm data, efficacy is exactly the trans data, and Lemma 1
  exhibits the gap between a complete representation and any obtaining
  rather than asserting it. It does not close the challenge. The
  reductionist's live move is untouched: propose that trans is derivable
  from representation and laws, in which case the minus-A model is refused
  not as false but as incomplete. What the formalization does is locate the
  remaining question exactly: anyone eliminating A must now say whether a
  stipulated or derived transition relation counts as A or as a
  redescription of it, against three checked models in which everything
  else is present.

## Claim status

No claim file is changed by this filing. ONT-002 and ONT-004 keep
proof_status prose_only and their current epistemic status until the
programme lead rules otherwise. This note records machine-checked support
under those claims; it does not relabel them.

Human-Curated, AI-Enabled (HCAE)
