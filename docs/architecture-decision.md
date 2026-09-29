---
layout: default
title: Site Architecture
---
# Pages architecture decision

**Decision:** repository-local Jekyll under `/docs`, published by GitHub Pages, with MathJax 3 loaded explicitly in the shared layout.

**Reasons:** minimal framework surface, native GitHub Pages compatibility, no JavaScript application framework, canonical Markdown retained, responsive static output, and controlled browser-side LaTeX rendering independent of the GitHub native-app Markdown renderer.

**Math contract:** source uses ordinary LaTeX delimiters. MathJax renders inline and display mathematics on Pages. The compact identity is canonical:

$$\boxed{\chi\equiv\mathsf{A}(I_\infty\mid L_3)}$$

**Content contract:** Pages explains the repository corpus. It does not become an independent source of ontology. The accessible and technical paths share the same semantic invariants.
