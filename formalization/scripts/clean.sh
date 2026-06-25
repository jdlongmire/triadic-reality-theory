#!/usr/bin/env bash
# Remove TRT oleans only (leaves the Mathlib cache intact).
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf .lake/build/lib/TrtFormalization* 2>/dev/null || true
echo "cleaned TRT build artifacts"
