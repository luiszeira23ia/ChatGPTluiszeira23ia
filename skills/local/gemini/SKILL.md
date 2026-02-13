---
name: gemini
description: Use Google Gemini workflows for text generation, summarization, extraction, and multimodal prompt tasks. Use when asked to draft/refine content with Gemini-style prompting, compare variants, or structure prompts for Gemini API/CLI usage.
---

# Gemini

## Overview

Run practical Gemini-oriented prompting workflows for drafting, rewriting, summarizing, and structured outputs.

## Quick Workflow

1. Define task objective and output format.
2. Build a concise system/task prompt.
3. Generate first candidate.
4. Iterate with constraints (tone, length, schema).
5. Return final result + optional alternate variant.

## Common Tasks

- Prompt design for Gemini API/CLI.
- Content rewrite by tone/style.
- Summaries with bullet key points.
- Structured extraction into JSON shape.

## Operational Rules

- Make output format explicit (markdown/json/plain).
- Prefer short iterative prompts over giant one-shot prompts.
- For factual tasks, request source-aware phrasing and uncertainty notes.

## Scripts

Use `scripts/prompt_scaffold.py` to generate reusable prompt templates.

Example:
- `python3 scripts/prompt_scaffold.py --task "resumir reunião" --format bullets --tone formal`

## Output Format

Return:
- Prompt used (or template)
- Result
- Optional variant
- Notes/assumptions
