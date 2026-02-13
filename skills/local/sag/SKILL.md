---
name: sag
description: Voice storytelling and expressive TTS workflow using SAG/voice pipelines. Use when asked to narrate stories, summarize movies in spoken format, create character-style narration, or generate audio-first responses.
---

# SAG

## Overview

Produce engaging spoken-style outputs for stories, summaries, and character-driven narration.

## Quick Workflow

1. Identify content type (story, summary, scene, announcement).
2. Choose narration style (formal, funny, dramatic, calm).
3. Prepare concise script optimized for speech rhythm.
4. Generate audio via configured TTS/voice pipeline.
5. Return media path and short text transcript.

## Common Tasks

- Storytime narration.
- Movie recap in spoken format.
- Character-voice style scripts.
- Read-aloud summaries.

## Operational Rules

- Keep spoken sentences shorter than written prose.
- Use punctuation for pacing.
- Avoid unsafe impersonation requests.
- If audio generation is unavailable, return speech-ready script.

## Scripts

Use `scripts/speech_prep.py` to normalize text for narration.

Example:
- `python3 scripts/speech_prep.py "Hoje vamos contar uma história incrível..."`

## Output Format

Return:
- Voice/style selected
- Speech script
- Audio result path (if generated)
- Optional retake suggestion
