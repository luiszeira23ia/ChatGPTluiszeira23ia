---
name: brave
description: Run fast web research and fact-finding with Brave Search. Use when asked to search the web, compare sources, gather links, check recent updates, or build concise evidence-based summaries from multiple pages.
---

# Brave

## Overview

Perform rapid web discovery, then validate key claims by fetching and comparing multiple sources.

## Quick Workflow

1. Convert user request into 1-3 focused search queries.
2. Run Brave search and shortlist credible sources.
3. Fetch readable content for top results.
4. Cross-check claims across at least 2 sources for important facts.
5. Return concise findings with links.

## Search Patterns

- Broad discovery: high-level query, then narrow by entity/date.
- Fresh news: use freshness filters (24h/week/month).
- Regional context: set country/language when relevant.
- Verification: search claim + source + contradiction terms.

## Quality Rules

- Prefer primary sources (official docs, vendor pages, standards).
- Mark uncertainty when sources conflict.
- Separate facts from interpretation.
- Avoid single-source conclusions for sensitive claims.

## Scripts

Use `scripts/query_builder.py` to generate structured query sets from a topic.

Example:
- `python3 scripts/query_builder.py "openclaw discord relay setup"`

## Output Format

Return:
- Key findings (bullets)
- Source links (2-5)
- Confidence note (high/medium/low)
- Gaps or next checks
