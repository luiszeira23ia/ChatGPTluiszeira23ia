# SQL Playbook: Safe Migration
- Validate scope and rollback first.
- Run in staging with realistic volume.
- Apply in steps: schema -> backfill batch -> constraints.
- Monitor locks/latency/replication lag.
- Keep rollback SQL ready.
