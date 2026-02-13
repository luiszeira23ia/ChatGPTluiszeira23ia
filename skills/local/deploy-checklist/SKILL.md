---
name: deploy-checklist
description: Run safe deployment checklists with pre-check, rollout, verification, and rollback planning. Use when asked to prepare or execute deploys, confirm readiness, reduce risk, or standardize release steps.
---

# Deploy Checklist

## Overview

Use a disciplined deployment flow to reduce change risk and speed up recovery when needed.

## Phases

1. Pre-deploy checks (build, tests, config, capacity).
2. Rollout execution (canary/batch/full).
3. Post-deploy verification (health, logs, key metrics).
4. Rollback readiness and communication.

## Operational Rules

- Block deploy if critical pre-check fails.
- Keep rollback command/path ready before rollout.
- Record timestamps for each phase.

## Scripts

Use `scripts/deploy_checklist.sh` to print a runbook checklist and track completion.

## Output Format

Return:
- Checklist status by phase
- Risks found
- Go/No-Go recommendation
- Rollback plan summary
