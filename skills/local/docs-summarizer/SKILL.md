---
name: docs-summarizer
description: Summarize long technical or product documents into concise actionable outputs. Use when asked to extract key points, decisions, risks, requirements, or next steps from docs, specs, RFCs, and manuals.
---

# Docs Summarizer

## Overview

Transform long-form documentation into clear, structured summaries tuned to actionability.

## Quick Workflow

1. Identify audience and summary objective.
2. Extract key sections and decisions.
3. Produce concise summary + risks + open questions.
4. Add action checklist.

## Summary Modes

- Executive brief (very short).
- Technical digest (details + caveats).
- Action plan (tasks, owners, deadlines placeholders).

## Operational Rules

- Separate facts from assumptions.
- Preserve critical constraints/limits from source text.
- Mark unknowns explicitly.

## Scripts

Use `scripts/summary_template.py` to generate consistent summary skeletons.

## Output Format

Return:
- TL;DR
- Key points
- Risks/open questions
- Next steps
