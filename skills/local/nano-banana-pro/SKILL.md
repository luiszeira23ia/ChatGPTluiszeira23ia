---
name: nano-banana-pro
description: Generic rapid-task utility skill scaffold for experiments and custom automations. Use when the user asks for quick prototyping tasks, lightweight data formatting, helper scripts, or iterative utility workflows that do not fit an existing specialized skill.
---

# Nano Banana Pro

## Overview

Provide a flexible, quick-turn workflow for small custom automations and utility operations.

## Quick Workflow

1. Confirm the exact utility objective.
2. Choose minimal deterministic script/tooling.
3. Execute with safe defaults and clear output paths.
4. Validate result and summarize next action.

## Task Types

- Text normalization and formatting.
- Small data transformations (CSV/JSON/TXT).
- Repetitive command wrapping.
- Utility helpers for ad-hoc workflows.

## Operational Rules

- Prefer reversible operations and explicit output files.
- Avoid destructive edits unless explicitly requested.
- Keep scripts small, readable, and reusable.
- Report assumptions when requirements are vague.

## Scripts

Use `scripts/quick_util.py` as a starter utility.

Examples:
- `python3 scripts/quick_util.py slugify "Nano Banana Pro"`
- `python3 scripts/quick_util.py lines path/to/file.txt`

## Output Format

Return:
- What was executed
- Output/result
- Any caveat
- Suggested next step
