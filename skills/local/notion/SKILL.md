---
name: notion
description: Organize and structure Notion content workflows for pages, databases, templates, and knowledge hygiene. Use when asked to draft Notion page structures, design database schemas, define properties/views, or convert notes/tasks/docs into Notion-ready formats.
---

# Notion

## Overview

Create clean, reusable Notion structures for docs, wikis, and task systems.

## Quick Workflow

1. Define workspace goal (docs, project tracking, CRM, content calendar).
2. Choose page model vs database model.
3. Design schema (properties, relations, rollups, formulas).
4. Draft templates and views.
5. Return copy-paste-ready structure/content.

## Core Tasks

- Notion page outline and section design.
- Database schema planning with property types.
- Template creation for recurring workflows.
- Migration of raw notes into structured entries.

## Operational Rules

- Prefer minimal schema first; expand only when needed.
- Keep property names consistent and human-readable.
- Separate canonical data from views/filters.

## Scripts

Use `scripts/notion_schema_helper.py` to generate starter database schemas.

Example:
- `python3 scripts/notion_schema_helper.py --type tasks`

## Output Format

Return:
- Proposed structure
- Property list and types
- Suggested views
- Next steps for implementation
