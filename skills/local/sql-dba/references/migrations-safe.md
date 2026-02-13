# Safe Migration Checklists (PostgreSQL/MySQL)

## 1) Add nullable column (low risk)

1. Confirm column purpose and default behavior.
2. Add column as NULL first.
3. Deploy application reading logic compatible with NULL.
4. Backfill gradually if needed.
5. Add constraints only after data is consistent.

## 2) Backfill in batches

1. Select stable batching key (id or created_at).
2. Process small chunks with commit per batch.
3. Sleep/throttle between batches on high load.
4. Track progress checkpoints and retry safely.
5. Stop on replication lag/latency regression.

## 3) Create index online

### PostgreSQL
- Prefer `CREATE INDEX CONCURRENTLY`.
- Avoid inside transaction block.
- Monitor lock/wait and IO.

### MySQL
- Prefer online DDL where supported (`ALGORITHM=INPLACE`, `LOCK=NONE`).
- Validate engine/table supports online mode.

## 4) Enforce NOT NULL safely

1. Backfill all NULL values.
2. Validate with count query.
3. Add constraint in maintenance window if needed.
4. Keep rollback path (drop constraint).

## 5) Rename/drop column (higher risk)

1. Deploy app version that no longer depends on old column.
2. Observe for one release cycle.
3. Drop in controlled window with backup ready.
4. Keep revert plan and timeline.

## 6) Rollback checklist

- Pre-captured schema diff and backup reference.
- Clear revert SQL prepared and tested in staging.
- Owner + decision threshold defined.
- Post-rollback verification queries ready.

## Pre-Change Gate (Go/No-Go)

- [ ] Backup/checkpoint confirmed
- [ ] Staging validation completed
- [ ] Execution plan reviewed
- [ ] Monitoring dashboards open
- [ ] Rollback command tested
- [ ] Stakeholders informed
