# Playbook: Retry Strategy
- Retry only idempotent actions.
- Re-snapshot before each retry.
- Limit retries (max 2-3) with clear reason.
- Abort and report when state diverges.
