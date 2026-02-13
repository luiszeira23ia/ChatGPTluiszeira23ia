---
name: discord-ops
description: Operate Discord servers/channels with safe moderation and channel hygiene workflows. Use when asked to manage channels, send announcements, run polls, handle reactions, inspect permissions, or perform light moderation actions.
---

# Discord Ops

## Overview

Execute practical Discord administration tasks with low-risk defaults and clear audit-style output.

## Quick Workflow

1. Confirm target server/channel/thread.
2. Inspect current state before mutation.
3. Apply minimal required change.
4. Confirm result and return IDs/links.

## Core Tasks

- Channel/category create/edit/move.
- Announcements, polls, and pins.
- Permission checks and quick diagnostics.
- Light moderation actions when explicitly requested.

## Operational Rules

- Never delete channels/messages without explicit confirmation.
- Prefer dry-run summary when request is ambiguous.
- Keep moderation actions transparent and reversible when possible.

## Scripts

Use `scripts/discord_payload.py` to build standardized announcement payload text.

## Output Format

Return:
- Action performed
- Target channel/message IDs
- Result status
- Follow-up recommendation
