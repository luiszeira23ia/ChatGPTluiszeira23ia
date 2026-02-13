# MySQL Quick Reference

## Query and Plan

- Use `EXPLAIN` / `EXPLAIN ANALYZE` (MySQL 8+) for execution insights.
- Check `type`, `rows`, `filtered`, and `Extra` fields.
- Investigate `Using temporary` / `Using filesort` for large workloads.

## Index Patterns

- Use composite indexes by predicate/order usage.
- Validate index selectivity before adding.
- Prefer covering indexes for frequent read-heavy queries.

## Lock and Migration Safety

- Prefer online DDL when available (`ALGORITHM=INPLACE`, `LOCK=NONE` where supported).
- Batch large updates/deletes to reduce lock pressure.
- Inspect active transactions/locks via `information_schema` / `performance_schema`.

## Slow Query Checklist

1. Capture exact SQL from slow query log.
2. Check execution plan and cardinality.
3. Add/tune indexes and re-check plan.
4. Validate impact with realistic row counts.
5. Confirm replication impact for write-heavy operations.

## Backup/Restore Notes

- Logical backup: `mysqldump`.
- Physical/hot backup: `xtrabackup` (where applicable).
- Always test restore and consistency checks.
