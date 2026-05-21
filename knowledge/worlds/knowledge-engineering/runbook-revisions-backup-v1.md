# Revisions Backup Runbook v1

## Goal

Keep `.revisions/` out of canonical Git history while preserving recoverability.

## Policy

- `.revisions/` is local operational history and is ignored by Git.
- Canonical repository stores only decision-grade memory (`agent-notes.md`, `knowledge/*`).
- Archive snapshots are created on schedule and before risky migrations.

## Recommended Cadence

- Weekly backup.
- Extra backup before:
  - large KB refactors,
  - alias retirements,
  - mass renames or compaction passes.

## Manual Backup (PowerShell)

From repository root:

```powershell
$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
New-Item -ItemType Directory -Force -Path ".\backups" | Out-Null
Compress-Archive -Path ".\.revisions\*" -DestinationPath ".\backups\revisions-$stamp.zip"
```

## Restore (PowerShell)

```powershell
Expand-Archive -Path ".\backups\revisions-YYYYMMDD-HHMMSS.zip" -DestinationPath ".\.revisions" -Force
```

## Verification

- Backup archive exists in `backups/`.
- Randomly open one snapshot file from extracted archive to validate readability.
- Keep at least last 4 weekly archives.
