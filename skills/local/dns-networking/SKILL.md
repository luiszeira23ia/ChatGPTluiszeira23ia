---
name: dns-networking
description: Diagnose DNS and network connectivity issues with structured checks for resolution, routing, latency, ports, and TLS endpoints. Use when asked to troubleshoot domain resolution failures, service reachability, packet loss, timeout errors, or network-path anomalies on Linux hosts.
---

# DNS Networking

## Overview

Run fast, evidence-based DNS and network diagnostics with clear isolation between name resolution, transport, and application-layer failures.

## Quick Workflow

1. Identify symptom (DNS fail, timeout, refused, intermittent).
2. Verify DNS resolution from host and alternate resolver.
3. Validate routing/path and basic connectivity.
4. Check target ports/TLS handshake and service response.
5. Summarize likely fault domain and next action.

## Core Tasks

- DNS checks (`A/AAAA/CNAME/MX/NS`, TTL, resolver mismatch).
- Connectivity checks (ICMP/TCP reachability, route/path).
- Port and endpoint checks (open/listening, timeout/refused).
- TLS endpoint checks (certificate validity/basic handshake).

## Operational Rules

- Prefer read-only commands for diagnosis.
- Compare results across at least 2 resolvers on DNS issues.
- Distinguish clearly: DNS vs network path vs app/service.
- Include command evidence for conclusions.

## Scripts

Use `scripts/net_diag.sh` for quick host/domain diagnostics.

Examples:
- `bash scripts/net_diag.sh --host example.com`
- `bash scripts/net_diag.sh --host api.example.com --port 443 --resolver 1.1.1.1`

## References

- DNS troubleshooting flow: `references/dns-checklist.md`
- Network path checklist: `references/network-checklist.md`

## Output Format

Return:
- Symptom summary
- Evidence snippets
- Fault-domain assessment
- Mitigation and verification steps
