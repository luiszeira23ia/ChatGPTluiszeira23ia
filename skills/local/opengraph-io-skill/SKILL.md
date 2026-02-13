---
name: opengraph-io-skill
description: Fetch and analyze Open Graph metadata for URLs using OpenGraph.io-style workflows. Use when asked to extract og:title/description/image, validate social preview cards, troubleshoot unfurl issues, or prepare link preview diagnostics.
---

# OpenGraph.io Skill

Extract and validate social card metadata for URLs.

## Quick Workflow

1. Validate URL format and reachability.
2. Fetch Open Graph payload (title, description, image, site_name, type).
3. Compare OG fields with page tags and expected sharing behavior.
4. Report gaps and recommended fixes.

## Core Tasks

- Inspect OG/Twitter card fields.
- Identify missing or weak metadata.
- Validate image dimensions/availability.
- Produce preview readiness checklist.

## Operational Rules

- Keep raw response snippets for evidence.
- Highlight critical missing fields first (title, description, image).
- Distinguish fetch failures from metadata issues.

## Scripts

Use `scripts/og_payload_template.py` to build request templates.

Examples:
- `python3 scripts/og_payload_template.py --url https://example.com`
- `python3 scripts/og_payload_template.py --url https://example.com --api-base https://opengraph.io/api/1.1/site`
