#!/usr/bin/env bash
set -euo pipefail

cmd="${1:-}"

timestamp() { date -u +"%Y%m%d-%H%M%S"; }

usage() {
  cat <<'EOF'
Usage:
  backup_tool.sh backup <source_path> <backup_dir> <name_prefix>
  backup_tool.sh verify <archive.tar.gz>
  backup_tool.sh restore <archive.tar.gz> <target_dir>
EOF
}

backup_cmd() {
  local src="$1"
  local outdir="$2"
  local prefix="$3"
  mkdir -p "$outdir"
  local ts
  ts="$(timestamp)"
  local archive="$outdir/${prefix}-${ts}.tar.gz"

  tar -czf "$archive" -C "$(dirname "$src")" "$(basename "$src")"
  sha256sum "$archive" > "${archive}.sha256"

  echo "backup_created: $archive"
  echo "checksum_file: ${archive}.sha256"
}

verify_cmd() {
  local archive="$1"
  if [[ ! -f "${archive}.sha256" ]]; then
    echo "ERROR: checksum file not found: ${archive}.sha256" >&2
    exit 2
  fi
  (cd "$(dirname "$archive")" && sha256sum -c "$(basename "$archive").sha256")
}

restore_cmd() {
  local archive="$1"
  local target="$2"
  mkdir -p "$target"
  tar -xzf "$archive" -C "$target"
  echo "restored_to: $target"
}

case "$cmd" in
  backup)
    [[ $# -eq 4 ]] || { usage; exit 1; }
    backup_cmd "$2" "$3" "$4"
    ;;
  verify)
    [[ $# -eq 2 ]] || { usage; exit 1; }
    verify_cmd "$2"
    ;;
  restore)
    [[ $# -eq 3 ]] || { usage; exit 1; }
    restore_cmd "$2" "$3"
    ;;
  *)
    usage
    exit 1
    ;;
esac
