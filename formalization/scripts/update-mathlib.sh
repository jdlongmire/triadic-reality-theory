#!/usr/bin/env bash
# Safe Mathlib update: bump rev in lakefile.toml first, then run this.
set -euo pipefail
cd "$(dirname "$0")/.."
source ~/.elan/env 2>/dev/null || true
lake update mathlib
lake exe cache get
