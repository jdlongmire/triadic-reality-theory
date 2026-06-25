#!/usr/bin/env bash
# Recommended build: fetch Mathlib cache, then build.
set -euo pipefail
cd "$(dirname "$0")/.."
source ~/.elan/env 2>/dev/null || true
lake exe cache get
lake build
