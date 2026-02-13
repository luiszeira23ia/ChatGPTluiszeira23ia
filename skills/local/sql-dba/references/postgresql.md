# PostgreSQL Quick Reference

## Query and Plan

- Prefer `EXPLAIN (ANALYZE, BUFFERS, VERBOSE)` for real execution behavior.
- Look for sequential scans on large tables when index access is expected.
- Watch for high `Rows Removed by Filter` and misestimates.

## Index Patterns

- Use B-Tree for equality/range lookups.
- Use partial indexes for filtered hot paths.
- Use multi-column indexes in left-prefix order of predicates.
- Avoid over-indexing high-write tables.

## Lock and Migration Safety

- Prefer `CREATE INDEX CONCURRENTLY` in production.
- Break large updates/deletes into batches.
- Check active locks:
  - `select * from pg_locks l join pg_stat_activity a on l.pid=a.pid;`
- Set lock timeout/session statement timeout before risky DDL.

## Slow Query Checklist

1. Confirm exact SQL + bind values.
2. Compare estimated vs actual rows.
3. Inspect missing/unused indexes.
4. Validate stats freshness (`ANALYZE`).
5. Re-test after index/query change.

## Backup/Restore Notes

- Logical backup: `pg_dump` / `pg_dumpall`.
- Physical backup: `pg_basebackup` or storage snapshots.
- Test restore regularly in isolated environment.
