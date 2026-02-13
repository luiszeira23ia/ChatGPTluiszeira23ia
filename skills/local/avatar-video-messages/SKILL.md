---
name: avatar-video-messages
description: Create short avatar-led video messages from text scripts with consistent voice, pacing, and export settings. Use when asked to generate talking-avatar announcements, status updates, welcome videos, or social-ready spoken clips.
---

# Avatar Video Messages

## Overview

Produce concise talking-avatar videos from text with stable formatting for announcements and updates.

## Quick Workflow

1. Define message objective, audience, and target platform.
2. Prepare speech script with short, spoken-friendly sentences.
3. Select avatar/voice/style parameters.
4. Generate a render payload and validate duration constraints.
5. Export in the requested format and provide delivery-ready metadata.

## Core Tasks

- Convert plain text into speech-ready scripts.
- Build structured render payloads for avatar video tools/APIs.
- Enforce platform-safe durations (short clips by default).
- Produce caption-friendly text blocks.

## Operational Rules

- Keep default clips short (15–60s) unless explicitly requested.
- Avoid impersonation and deceptive identity use.
- Mark placeholders when avatar provider/API keys are missing.

## Scripts

Use `scripts/avatar_payload.py` to generate a standard render payload JSON.

Examples:
- `python3 scripts/avatar_payload.py --title "Status" --script "Deploy concluído com sucesso."`
- `python3 scripts/avatar_payload.py --title "Boas-vindas" --script "Bem-vindos ao canal." --voice pt-BR-Female --style formal --duration 30 -o payload.json`

## Output Format

Return:
- Script final
- Render config (avatar/voice/style/duration)
- Output file path or payload path
- Optional revision suggestions
