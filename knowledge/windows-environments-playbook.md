# Windows Environments Playbook v1

## Purpose
Project-independent playbook for reliable engineering and troubleshooting on Windows hosts.

## Scope
- Windows process/service runtime behavior
- Security and identity context
- Filesystem and path semantics
- Operational diagnostics baseline

## Evidence-Based Working Format
- Fact: capture concrete host symptom (startup failure, permission denial, runtime instability).
- Hypothesis: define smallest plausible Windows-level cause.
- Check: run minimal reproducible verification command set.
- Decision criterion: predefine close/escalate threshold.
- Confidence mark: explicit certainty and residual risk.

## Core Windows Contracts
- Service account and token context must be explicit.
- UAC/policy boundaries must be validated for privileged actions.
- Path and file-lock assumptions must be explicit.
- Encoding and locale expectations must be declared.

## Runtime and Service Contracts
- Service lifecycle, dependencies, and startup policy must be deterministic.
- Startup arguments and environment variables must be explicit.
- Failure actions and restart policy must be intentional, not default.
- Background workers must support graceful stop/restart.

## Security and Identity Contracts
- Verify execution identity before diagnosing application logic.
- Validate ACL ownership and inheritance on critical paths.
- Keep credential scope minimal and auditable.
- Separate interactive-user assumptions from service-host reality.

## Shell Context Contract (Git and Tooling)
- Distinguish shell families explicitly: `PowerShell/cmd`, Git Bash (MSYS/MinGW), WSL.
- Assume config visibility can differ across shell families until proven otherwise.
- For author/identity incidents, verify in the active shell:
  - `git config --show-origin --get user.name`
  - `git config --show-origin --get user.email`
  - `git var GIT_AUTHOR_IDENT`
- Check process environment overrides in the active shell:
  - `GIT_AUTHOR_NAME`, `GIT_AUTHOR_EMAIL`, `GIT_COMMITTER_NAME`, `GIT_COMMITTER_EMAIL`, `EMAIL`.
- Prefer native Windows shell for canonical repo operations unless cross-shell behavior is intentionally required.

## Filesystem and IO Contracts
- Normalize paths and quote paths with spaces.
- Model file-sharing/locking behavior explicitly.
- Keep mutation boundaries explicit for automation scripts.
- Detect long-path and permission edge cases early.

## Diagnostics Baseline
- Event Viewer + structured application logs.
- Process/resource counters and service status checks.
- Startup/failure timeline reconstruction from host evidence.
- One concise root-cause and prevention delta per incident.

## Metrics
- Mean time to identify Windows host root cause.
- Frequency of service-account/ACL-related incidents.
- Startup failure recovery time.
- Reopen rate for Windows environment incidents.

## Revisit Triggers
- Repeat incidents caused by identity/policy mismatch.
- Frequent path/locking regressions.
- Service instability with unclear host-level ownership.
