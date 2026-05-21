# Git Multi-Remote Backup Runbook v1

## Goal

Keep canonical KB available even if one host becomes unavailable by maintaining synchronized `main` on multiple remotes.

Current target pair:

- `origin`
- `wissance`

## Policy

- Every semantic update to canonical KB (`agent-notes.md`, `knowledge/*`) is pushed to both remotes.
- No force-push to shared `main` in normal operation.
- Divergence is resolved by integration (`fetch` + `merge`), not overwrite.
- Merge-only workflow for shared branches: no `rebase` on `main`.

## Daily Flow (fast path)

1. `git status --short`
2. logical commit(s)
3. push primary:
   - `git push origin main`
4. push backup:
   - `git push wissance main`
5. verify:
   - `git ls-remote --heads origin main`
   - `git ls-remote --heads wissance main`

## Pre-Push Checklist

- Working tree clean or intentionally scoped.
- Commit message explains intent and behavioral impact.
- No accidental secrets in staged files.
- `main` is not behind remote unexpectedly:
  - `git fetch --all --prune`
  - inspect `git status -sb`.

## Weekly Verify Cadence

At least once per week:

1. `git fetch --all --prune`
2. Check remotes configured:
   - `git remote -v`
3. Check divergence:
   - `git log --oneline --left-right --cherry-pick --no-merges main...origin/main -n 20`
   - `git log --oneline --left-right --cherry-pick --no-merges main...wissance/main -n 20`
4. If local is ahead one remote only -> push missing remote.
5. If remote has unique commits -> integrate safely (see Recovery path).

## Recovery Path: backup remote rejects push (non-fast-forward)

Symptom:

- `git push wissance main` returns `fetch first` / non-fast-forward.

Safe sequence:

1. `git fetch wissance`
2. inspect divergence:
   - `git log --oneline --left-right --cherry-pick --no-merges main...wissance/main -n 30`
3. integrate without force (merge-only):
   - `git merge --no-edit wissance/main`
   - resolve conflicts if any, then commit merge
4. push again:
   - `git push wissance main`

If merge should be cancelled:

- `git merge --abort`

## Minimal Incident Mode (one host down)

- Continue commits locally.
- Push to available remote.
- Keep a local note of missing pushes.
- When host returns, run weekly verify and backfill missing commits.

## Success Criterion

- `main` on `origin` and `wissance` points to equivalent commit lineage for canonical KB updates.

