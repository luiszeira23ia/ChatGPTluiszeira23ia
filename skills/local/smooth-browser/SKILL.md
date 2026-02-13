---
name: smooth-browser
description: Run smooth, reliable browser automations with stable refs, minimal flakiness, and human-like step sequencing. Use when asked to automate web tasks that require robust navigation, controlled interactions, snapshots, and repeatable verification flows.
---

# Smooth Browser

Automate browser flows with stability-first patterns.

## Quick Workflow

1. Open/focus target tab and capture initial snapshot.
2. Prefer stable refs and deterministic actions (click/type/press).
3. Verify UI state after each critical step.
4. Capture final snapshot/screenshot evidence.
5. Summarize outcome and any flaky points.

## Core Rules

- Prefer snapshot + targeted action loops.
- Avoid blind waits; wait for concrete UI conditions.
- Keep action granularity small to simplify retries.
- Re-resolve refs after navigation/major DOM updates.

## Scripts

Use `scripts/flow_checklist.py` to print a robust browser-run checklist.

Example:
- `python3 scripts/flow_checklist.py --task "login and export report"`

## Playbooks

Use these references for common stable flows:
- Login: `references/playbook-login.md`
- Form submit: `references/playbook-form-submit.md`
- Export/download: `references/playbook-export.md`
- Scrape lite: `references/playbook-scrape-lite.md`
