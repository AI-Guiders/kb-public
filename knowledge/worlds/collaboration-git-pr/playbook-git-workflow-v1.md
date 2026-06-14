# Git Workflow Playbook v1

## Purpose

Provide a stable, low-risk Git operating model for daily development, review, and recovery.

## Core Workflow

1. Inspect local state: `status -> diff -> staged diff`.
2. Stage only logical scope of change.
3. Commit with message explaining intent and impact.
4. Re-check local state after commit.
5. Push branch and verify remote state.

## Branching Contract

- Keep `main` protected and stable.
- Create feature/fix branches for non-trivial changes.
- Keep branch scope single-purpose (avoid mixed-domain commits).
- Prefer short-lived branches with frequent synchronization.

## Commit Contract

- One logical change per commit.
- Message must answer: **why now** and **what behavior changed**.
- Avoid “dump” commits that mix refactor + feature + docs unless tightly coupled.
- Re-run minimal validation before final commit.

## Identity and Shell Contract (Windows)

- Identity resolution order follows Git commit rules:
  - environment: `GIT_AUTHOR_*` / `GIT_COMMITTER_*`;
  - config: `author.*` / `committer.*`;
  - config fallback: `user.name` / `user.email`;
  - last fallback: `EMAIL`, then system user + hostname.
- For routine Windows workflows, prefer native shell (`PowerShell`/`cmd`) for `git commit`.
- Treat cross-shell commit runs (`bash -lc`, MSYS/MinGW, WSL) as explicit context switch.
- Before commit in a switched shell, verify identity with:
  - `git config --show-origin --get user.name`
  - `git config --show-origin --get user.email`
  - `git var GIT_AUTHOR_IDENT`
- If shell context still disagrees, use one-shot fallback:
  - `git -c user.name=\"...\" -c user.email=\"...\" commit ...`

## Review Contract

- Start review from risk: behavior regressions, data loss, safety boundaries.
- Validate test impact and missing checks.
- Call out uncertainty explicitly.
- Use small diffs and deterministic reproduction steps.

## Safety Rules

- Never use destructive commands on shared branches by default.
- Never force-push shared `main/master` history.
- Do not rewrite published history unless explicitly approved.
- Treat credential files and tokens as non-committable by policy.

## Recovery Patterns

- Uncommitted recovery: `git restore --staged` / selective restore by file.
- Lost pointer recovery: `git reflog` first, then recover target commit.
- Bad merge recovery: abort/reset strategy based on publication state.
- Always prefer reversible path before irreversible cleanup.

## Operational Cadence

- Before starting work: quick `status` + branch check.
- Before context switch: checkpoint commit or explicit stash with note.
- End of session: clean working tree or explicit WIP marker.

## Revisit Triggers

- Recurring merge conflicts in same area.
- Frequent “mixed commits” that block review quality.
- Recovery actions needed more than once per week.

