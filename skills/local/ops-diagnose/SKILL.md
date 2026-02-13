---
name: ops-diagnose
description: Diagnose infrastructure and service issues with fast, structured operational checks. Use when asked to investigate downtime, high resource usage, failing services, networking issues, logs, or incident triage on Linux hosts.
---

# Ops Diagnose

## Overview

Run a structured incident triage flow to quickly isolate root cause candidates and recommend safe next actions.

## Quick Workflow

1. Identify symptom (down, slow, erroring, unreachable).
2. Check host health (CPU, RAM, disk, load).
3. Check service state and recent logs.
4. Check network/listening ports/connectivity.
5. Correlate timeline and likely causes.
6. Propose mitigation + verification steps.

## Core Checks

### Host health

- Uptime/load and resource saturation.
- Disk capacity/inodes and IO pressure.
- OOM/restart indicators.

### Service health

- Process and systemd status.
- Restart counts and crash loops.
- Recent error logs with timestamps.

### Network health

- Listener ports and bind interfaces.
- DNS/connectivity reachability checks.
- TLS/endpoint behavior where relevant.

## Operational Rules

- Prefer read-only diagnostics before restart actions.
- Never restart critical service without explicit confirmation unless user asked.
- Include exact command evidence for key conclusions.
- Mark uncertainty where data is incomplete.

## Scripts

Use `scripts/ops_snapshot.sh` to collect a quick host/service snapshot.

Examples:
- Host snapshot:
  - `bash scripts/ops_snapshot.sh`
- Snapshot with service focus:
  - `bash scripts/ops_snapshot.sh nginx`

## Output Format

Return:
- Symptom summary
- Evidence (key command outputs)
- Likely cause(s) ranked
- Immediate mitigation and follow-up checks
