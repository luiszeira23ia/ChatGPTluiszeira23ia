#!/usr/bin/env bash
set -euo pipefail

# Helper to print recommended nodes.camera_snap calls parameters.
# Usage:
#   camsnap_helper.sh <front|back|both> [maxWidth] [quality]

facing="${1:-front}"
max_width="${2:-1280}"
quality="${3:-80}"

if [[ "$facing" != "front" && "$facing" != "back" && "$facing" != "both" ]]; then
  echo "Invalid facing: $facing"
  echo "Use: front | back | both"
  exit 1
fi

cat <<EOF
Use nodes.camera_snap with:
- facing: $facing
- maxWidth: $max_width
- quality: $quality
- delayMs: 0 (optional)
- node: <target-node-id>
EOF
