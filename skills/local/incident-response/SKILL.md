---
name: incident-response
description: Triage and coordinate incident response with severity, timeline, mitigation, and comms structure. Use when asked to handle outages, degraded services, security events, or urgent production incidents.
---

# Incident Response

## Overview

Run a fast, structured incident workflow to stabilize systems and keep communication clear.

## Incident Flow

1. Classify severity and impact.
2. Build timeline and current status.
3. Mitigate immediate customer impact.
4. Investigate root cause candidates.
5. Track decisions and owner actions.
6. Prepare post-incident summary.

## Operational Rules

- Prioritize containment and service restoration.
- Keep an explicit timeline with UTC timestamps.
- Avoid speculative root-cause claims before evidence.
- Request confirmation before disruptive remediation.

## Scripts

Use `scripts/incident_log.py` to append structured incident timeline entries.

## Output Format

Return:
- Severity + impact
- Timeline entries
- Mitigation status
- Next actions and owners
