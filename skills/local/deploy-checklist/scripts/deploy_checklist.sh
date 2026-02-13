#!/usr/bin/env bash
set -euo pipefail

cat <<'EOF'
DEPLOY CHECKLIST

[PRE]
- Build green
- Tests passing
- Config/secrets validated
- Rollback target identified

[ROLLOUT]
- Start timestamp recorded
- Canary/batch strategy confirmed
- Monitoring dashboard open

[POST]
- Healthchecks passing
- Error rate stable
- Logs reviewed

[ROLLBACK]
- Rollback command tested/rehearsed
- Owner assigned
- Communication draft ready
EOF
