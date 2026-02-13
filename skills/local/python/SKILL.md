---
name: python
description: Build, run, and debug Python scripts and utilities with practical project-oriented workflows. Use when asked to write Python code, refactor scripts, parse data files, automate repetitive tasks, troubleshoot exceptions, or structure small Python tools.
---

# Python

## Overview

Handle Python automation and scripting tasks with clean, testable, and minimal implementations.

## Quick Workflow

1. Confirm objective, input format, and expected output.
2. Implement smallest working script/function first.
3. Run and validate with sample input.
4. Add argument parsing and error handling.
5. Return usage examples and output path.

## Core Tasks

- Write small utilities and CLIs.
- Parse/transform JSON, CSV, TXT.
- Refactor scripts for readability and reuse.
- Diagnose stack traces and fix exceptions.

## Operational Rules

- Prefer standard library unless external dependency is justified.
- Add clear usage/help for scripts with arguments.
- Fail with explicit error messages, not silent behavior.

## Scripts

Use `scripts/py_helper.py` for quick data conversion and pretty-printing.

Examples:
- `python3 scripts/py_helper.py json-pretty input.json -o output.json`
- `python3 scripts/py_helper.py csv-head data.csv --rows 5`

## Output Format

Return:
- What was implemented/fixed
- How to run
- Output or changed files
- Caveats and optional improvements
