---
name: canvas
description: Build and inspect interactive browser-canvas workflows using OpenClaw canvas tools. Use when asked to present web UIs on node canvases, navigate pages, execute JavaScript, capture snapshots, or automate quick visual checks.
---

# Canvas

## Overview

Operate node-hosted canvases for visual testing, quick UI checks, and lightweight browser-based automation.

## Quick Workflow

1. Present or target an existing canvas session.
2. Navigate to target URL.
3. Execute required checks/actions.
4. Capture snapshot/screenshot evidence.
5. Summarize findings and next steps.

## Core Tasks

- Present/hide canvas sessions.
- Navigate and run JavaScript on pages.
- Capture snapshots for validation.
- Push/reset A2UI event streams when needed.

## Operational Rules

- Prefer snapshots for evidence after each critical step.
- Keep JS eval snippets minimal and safe.
- Confirm target node before running actions.

## Scripts

Use `scripts/canvas_js_snippets.py` to print ready-to-use JS snippets.

Examples:
- `python3 scripts/canvas_js_snippets.py --snippet title`
- `python3 scripts/canvas_js_snippets.py --snippet ready-state`

## Output Format

Return:
- Actions performed
- Canvas target/node
- Snapshot evidence paths/notes
- Issues found + recommended next action
