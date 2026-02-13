---
name: backup-restore
description: Create and verify backups with practical restore workflows for files, directories, and service data. Use when asked to back up data, validate recovery readiness, build retention routines, or execute safe restore procedures.
---

# Backup Restore

## Overview

Perform reliable backup and restore operations with explicit verification and recovery confidence checks.

## Quick Workflow

1. Identify scope (what data, where, and why).
2. Create timestamped backup artifact.
3. Generate checksum and backup manifest.
4. Validate artifact readability/integrity.
5. Test restore path (dry-run or sample restore).
6. Report retention and rollback guidance.

## Core Tasks

### Backup creation

- Archive file sets into compressed, timestamped outputs.
- Exclude temp/cache paths to reduce size and noise.
- Save checksum (`sha256`) and manifest summary.

### Restore execution

- Restore into a safe target path first when possible.
- Validate permissions/ownership after restore.
- Confirm expected file counts and key paths.

### Verification and hygiene

- Run periodic verification on backup artifacts.
- Track retention windows and prune old backups safely.
- Keep at least one recent known-good snapshot.

## Operational Rules

- Never overwrite production data blindly.
- Prefer test restore before full restore when impact is high.
- Stop and confirm if backup scope is ambiguous.
- Report any skipped files and permission errors explicitly.

## Scripts

Use `scripts/backup_tool.sh` for quick archive + checksum operations.

Examples:
- Create backup:
  - `bash scripts/backup_tool.sh backup /data/project ./backups project`
- Verify backup:
  - `bash scripts/backup_tool.sh verify ./backups/project-20260101-010101.tar.gz`
- Restore backup:
  - `bash scripts/backup_tool.sh restore ./backups/project-20260101-010101.tar.gz ./restore-test`

## Output Format

Return:
- What was backed up/restored
- Artifact paths + checksum status
- Validation result
- Caveats and next recommended step
