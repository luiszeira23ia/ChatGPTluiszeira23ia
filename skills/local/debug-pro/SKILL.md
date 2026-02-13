---
name: debug-pro
description: Systematic debugging workflow for apps, scripts, and services. Use when asked to investigate errors, reproduce bugs, isolate root causes, inspect logs/traces, compare expected vs actual behavior, and propose safe fixes with verification steps.
---

# Debug Pro

## Overview

Apply a fast, structured debugging process focused on reproducibility, evidence, and minimal-risk fixes.

## Quick Workflow

1. Reproduce the issue reliably.
2. Capture error signals (logs, stack traces, status, inputs).
3. Isolate failing boundary (config, dependency, code path, environment).
4. Form hypotheses and test one variable at a time.
5. Implement smallest safe fix.
6. Verify with regression checks.

## Core Tasks

- Parse and summarize stack traces.
- Build minimal reproductions.
- Diff expected vs observed behavior.
- Validate fix and add guardrails.

## Operational Rules

- Prefer read-only diagnosis before state-changing actions.
- Keep evidence snippets tied to conclusions.
- Avoid broad changes until root cause confidence is high.

## Scripts

Use `scripts/log_focus.py` to filter error-significant log lines.

Examples:
- `python3 scripts/log_focus.py app.log`
- `python3 scripts/log_focus.py app.log --keywords error,exception,timeout,failed`

## Output Format

Return:
- Symptom and reproduction status
- Evidence highlights
- Root cause hypothesis/confidence
- Fix + verification checklist
