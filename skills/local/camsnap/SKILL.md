---
name: camsnap
description: Capture and manage camera snapshots/clips from paired nodes with a fast verification workflow. Use when asked to take a quick photo from front/back cameras, save evidence images, or perform basic camera checks.
---

# CamSnap

## Overview

Capture camera snapshots quickly and reliably from paired nodes, then return file paths and capture context.

## Quick Workflow

1. Confirm target node and camera facing (`front`, `back`, or `both`).
2. Capture a snapshot with suitable quality/size.
3. Validate output exists and is readable.
4. Return result path(s) and metadata.

## Common Tasks

- Quick front-camera check.
- Back-camera environment capture.
- Dual capture (`both`) for diagnostics.
- Delay-based capture for setup time.

## Operational Rules

- Never expose private images to public channels without explicit request.
- Prefer lower resolution for quick checks; increase quality only when needed.
- If capture fails, report exact failure and retry suggestion.

## Scripts

Use `scripts/camsnap_helper.sh` for quick command templates.

Examples:
- `bash scripts/camsnap_helper.sh front`
- `bash scripts/camsnap_helper.sh back 1200 85`
- `bash scripts/camsnap_helper.sh both 1600 90`

## Output Format

Return:
- Capture performed (facing + quality)
- Output path(s)
- Capture notes (delay/lighting/errors)
- Optional next step
