---
name: powerpoint-creator
description: Create presentation outlines and slide-ready content for PowerPoint decks. Use when asked to build slide structures, speaker notes, agenda flows, pitch decks, status decks, or training presentations with clear narrative progression.
---

# PowerPoint Creator

## Overview

Turn goals and source material into a structured slide narrative ready for deck production.

## Quick Workflow

1. Define audience, objective, and time limit.
2. Build slide storyline (hook -> context -> insight -> action).
3. Draft per-slide title and bullets.
4. Add speaker notes and visual suggestions.
5. Return final deck blueprint.

## Core Tasks

- Executive status presentations.
- Project update decks.
- Pitch/investor narratives.
- Training and onboarding slides.

## Operational Rules

- One main idea per slide.
- Prefer short bullets and strong headlines.
- Keep transitions explicit between sections.

## Scripts

Use `scripts/deck_outline.py` to generate deck skeletons.

Example:
- `python3 scripts/deck_outline.py --topic "Q1 Product Update" --slides 10`

## Output Format

Return:
- Slide-by-slide outline
- Speaker notes summary
- Visual/chart suggestions
- Optional shortened version (if time-constrained)
