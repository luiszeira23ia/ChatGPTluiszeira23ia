---
name: github
description: Work with GitHub repositories, issues, pull requests, labels, releases, and project hygiene using fast CLI-first workflows. Use when asked to inspect repos, create/update issues/PRs, review diffs, comment, triage backlog, or summarize GitHub activity.
---

# GitHub

## Overview

Execute GitHub tasks with a CLI-first approach (`gh` + `git`) and produce concise operational summaries.

## Quick Workflow

1. Identify repository and target object (issue, PR, release, branch).
2. Check auth/context first (`gh auth status`, current remote).
3. Run read-only inspection before mutation.
4. Apply requested change.
5. Return links/IDs and exact results.

## Common Tasks

### Repo inspection

- Show remotes and default branch.
- List open issues/PRs with filters.
- Summarize recent activity (titles, authors, status).

### Issue/PR triage

- Create/update issue titles, body, labels, assignees.
- Comment with clear action items.
- Link related issue/PR when context asks.

### PR review support

- Inspect files changed and high-risk areas.
- Summarize diff by component.
- Post review-ready notes/checklists when asked.

### Release hygiene

- Draft release notes from merged PRs.
- Tag/release with version requested.
- Confirm artifacts/links.

## Operational Rules

- Never merge/close/delete without explicit user request.
- Prefer read-only commands if intent is ambiguous.
- Include direct GitHub URL(s) in final output.
- If `gh` auth is missing, stop and report the exact command to authenticate.

## Scripts

Use `scripts/gh_quick.sh` for frequent read-only commands.

Examples:
- `bash scripts/gh_quick.sh auth`
- `bash scripts/gh_quick.sh prs owner/repo`
- `bash scripts/gh_quick.sh issues owner/repo`
- `bash scripts/gh_quick.sh activity owner/repo`

## Output Format

Return:
- Actions taken (bullets)
- Object IDs/URLs (issue, PR, release)
- Current status (open/closed/merged)
- Optional next step
