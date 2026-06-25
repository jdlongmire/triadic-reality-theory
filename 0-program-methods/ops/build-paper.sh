#!/usr/bin/env bash
# Build a TRT paper PDF from its canonical Markdown (single-source rule).
# Usage: build-paper.sh <source.md> <output.pdf>
set -euo pipefail
SRC="${1:?source .md required}"
OUT="${2:?output .pdf required}"
pandoc "$SRC" -o "$OUT" \
  --pdf-engine=xelatex \
  -V geometry:margin=1in \
  -V mainfont="DejaVu Serif" \
  -V mathfont="DejaVu Math TeX Gyre" \
  --toc --number-sections
echo "built: $OUT"
