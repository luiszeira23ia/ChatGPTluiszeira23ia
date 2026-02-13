---
name: sql-dba
description: Design, debug, and optimize SQL/database workflows for PostgreSQL and MySQL with safe operational checks. Use when asked to write complex queries, improve performance, analyze execution plans, design schemas/indexes, troubleshoot slow queries, or plan safe migration and maintenance steps.
---

# SQL DBA

## Overview

Support SQL development and database operations with performance awareness and safety-first change control.

## Quick Workflow

1. Identify database engine (PostgreSQL/MySQL) and objective.
2. Clarify expected result and data volume.
3. Draft/optimize query or schema change.
4. Validate with execution-plan review.
5. Propose safe rollout and rollback steps.

## Core Tasks

- Write and refine SQL (joins, CTEs, windows, aggregations).
- Diagnose slow queries and indexing gaps.
- Review EXPLAIN/EXPLAIN ANALYZE output.
- Plan migrations with lock/risk awareness.
- Prepare backup/checkpoint recommendations before critical changes.

## Operational Rules

- Prefer read-only analysis before DDL/DML changes.
- Never run destructive operations without explicit confirmation.
- Always include where-clause safety for updates/deletes.
- Recommend running changes first in staging when possible.

## Scripts

Use `scripts/sql_review.py` to run quick static checks on SQL text.

Examples:
- `python3 scripts/sql_review.py --file query.sql`
- `python3 scripts/sql_review.py --sql "delete from users"`

## References

Use engine-specific guidance before final recommendations:
- PostgreSQL: `references/postgresql.md`
- MySQL: `references/mysql.md`
- Safe migrations and rollback playbook: `references/migrations-safe.md`

## Output Format

Return:
- SQL/proposed change
- Risk notes
- Performance notes (indexes/plan hints)
- Validation and rollback checklist
