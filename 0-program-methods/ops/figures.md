# Work Instruction: Figures & Diagrams

How the programme plans, marks, and develops figures. The principle: every figure a paper will need is **marked as a placeholder with its final caption and a build spec at authoring time**, so the visual argument is designed up front and nothing is improvised at deposit. A figure is *resolved* when the asset is built and the placeholder replaced.

## Placeholder convention (GitHub-safe, greppable)

A figure-to-be is a blockquote — it renders cleanly on GitHub (no broken `![]()`), states the **final caption**, and carries the **build spec**:

```markdown
> **Figure N. <final caption title>.** <final caption sentence — the text as it will appear in the published paper.>
>
> **[FIGURE-PLACEHOLDER]** — *type:* <conceptual schematic | technical/data plot | process diagram> · *tool:* <D2 | Mermaid | Structurizr | matplotlib> · *asset:* `figures/figNN-slug.svg`
> *Spec:* <what the artifact must show and convey, precisely enough to build from — elements, relations, layout, emphasis>. Print-safe, monochrome unless colour carries meaning.
```

- The literal token **`[FIGURE-PLACEHOLDER]`** is the machine-greppable marker (registry + deposit gate key on it).
- The **caption is final** — write it as published, not as a note-to-self. The *Spec* line is the note-to-self.
- **Numbering is stable** per paper; do not renumber on insert/remove (use the next free integer).

When built, replace the placeholder block with the real figure, keeping the same number and caption:

```markdown
![Figure N. <caption title>](figures/figNN-slug.svg)
*Figure N. <caption sentence>.*
```

## Figure taxonomy — by paper type

The artifact a placeholder calls for depends on the paper:

| Paper type | Figure character | Typical tools |
|---|---|---|
| **Position / preprint** (e.g. `TRT-v0.9`) | **Conceptual schematics** — engines, hierarchies, convergences, boundaries. Explanatory, not data. | D2, Mermaid, Structurizr |
| **Formal / result** (e.g. a co-admissibility or gravity paper) | **Technical / data plots** — computed results, parameter sweeps, relational-graph constructions, critical-coupling curves. | matplotlib (notebooks in `3-prediction/<test>/code/`), TikZ/D2 for constructions |
| **Methodology / review** | **Process diagrams** — pipelines, decision flows, the falsifiability ladder. | D2, Mermaid |

A placeholder always declares its `type` so the right treatment and tool are applied.

## Asset location & format

- Co-locate with the paper: **`<paper-folder>/figures/figNN-slug.svg`** (e.g. `1-hypothesis/paper/figures/`). Self-contained, travels with the citeable paper.
- **Vector preferred** — `.svg` for GitHub/web; the deposit PDF build embeds it (pandoc/xelatex). Keep a `.pdf` or high-DPI `.png` fallback only if a tool can't emit clean SVG.
- Generated diagrams keep their source (`.d2`, `.mmd`) next to the asset so they rebuild.

## Registry

Each paper folder's `figures/README.md` lists its figures (number, caption, type, status, asset). It is the index; the in-`.md` placeholders are the source of truth (a generator can later scan `[FIGURE-PLACEHOLDER]` markers to refresh it, mirroring the open-problems pattern).

## Deposit gate (ties to Zenodo SOP)

**A v1.0 / public-circulation copy must contain zero `[FIGURE-PLACEHOLDER]` markers** — every figure resolved to a built asset. Add to the [Zenodo deposit-readiness gate](zenodo-publishing.md): `grep -rn '\[FIGURE-PLACEHOLDER\]' <paper>` must return nothing before deposit. Working-draft (v0.x) copies may carry placeholders.
