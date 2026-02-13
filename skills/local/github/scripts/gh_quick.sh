#!/usr/bin/env bash
set -euo pipefail

cmd="${1:-}"
repo="${2:-}"

usage() {
  cat <<'EOF'
Usage:
  gh_quick.sh auth
  gh_quick.sh prs <owner/repo>
  gh_quick.sh issues <owner/repo>
  gh_quick.sh activity <owner/repo>
EOF
}

if [[ -z "$cmd" ]]; then
  usage
  exit 1
fi

case "$cmd" in
  auth)
    gh auth status
    ;;
  prs)
    [[ -n "$repo" ]] || { echo "Missing repo"; usage; exit 1; }
    gh pr list --repo "$repo" --limit 20 --json number,title,author,state,url,updatedAt
    ;;
  issues)
    [[ -n "$repo" ]] || { echo "Missing repo"; usage; exit 1; }
    gh issue list --repo "$repo" --limit 20 --json number,title,author,state,url,updatedAt
    ;;
  activity)
    [[ -n "$repo" ]] || { echo "Missing repo"; usage; exit 1; }
    echo "== PRs =="
    gh pr list --repo "$repo" --limit 10 --json number,title,state,url,updatedAt
    echo "== Issues =="
    gh issue list --repo "$repo" --limit 10 --json number,title,state,url,updatedAt
    ;;
  *)
    usage
    exit 1
    ;;
esac
