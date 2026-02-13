---
name: basecamp-automation
description: Automate Basecamp-oriented project routines such as to-do planning, status check-ins, milestone tracking, and update message preparation. Use when asked to standardize team updates, convert notes into action items, or generate recurring project-ops workflows.
---

# Basecamp Automation

Automate recurring project operations with clear templates and execution steps.

## Quick Workflow

1. Define project context (team, objective, cadence).
2. Convert raw notes into structured to-dos and milestones.
3. Generate status update payloads (daily/weekly).
4. Validate ownership, due dates, and blockers.
5. Return publish-ready text and checklist.

## Core Tasks

- Build task lists from meeting notes.
- Generate weekly status updates.
- Track blockers, owners, and deadlines.
- Standardize progress reporting format.

## Operational Rules

- Keep updates objective and concise.
- Always include owner + due date on action items.
- Separate facts, risks, and asks.

## Scripts

Use `scripts/basecamp_update_builder.py` for structured status generation.

Example:
- `python3 scripts/basecamp_update_builder.py --project "Website Revamp" --done "Header concluído" --next "Integrar checkout" --blockers "Dependência API"`
- `python3 scripts/basecamp_update_builder.py --project "Website Revamp" --mode weekly --done "Landing publicada" --next "A/B test"`
- `python3 scripts/basecamp_update_builder.py --project "Website Revamp" --mode retro --done "Pipeline estável" --blockers "Falta owner QA"`

## References

- Daily/Weekly templates: `references/daily-weekly-templates.md`
- Retrospective template: `references/retrospective-template.md`
