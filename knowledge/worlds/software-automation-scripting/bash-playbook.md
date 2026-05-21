# Bash Playbook v1

## Purpose
Dedicated playbook for Unix shell scripting with predictable behavior and portability discipline.

## Scope
- Shell safety and strictness
- Portability and POSIX boundaries
- Script composition and process control
- Reliability in CI and local workflows

## Evidence-Based Working Format
- Fact: identify concrete shell failure or nondeterministic behavior.
- Hypothesis: define smallest change that should stabilize behavior.
- Check: validate in minimal reproducible shell scenario.
- Decision criterion: explicit close/escalate threshold.
- Confidence mark: explicit certainty level.

## Core Contracts
- Use strict mode where applicable (`set -euo pipefail`).
- Quote variables defensively.
- Keep inputs explicit; avoid hidden environment coupling.
- Prefer small composable scripts over long monoliths.

## Portability Contracts
- Define target shell (`bash` vs POSIX `sh`) explicitly.
- Avoid bash-specific features when portability is required.
- Keep tool dependencies explicit (`awk/sed/grep` variants matter).
- Validate behavior on representative runtime environments.

## Process and Pipeline Contracts
- Preserve meaningful exit codes through pipelines.
- Avoid subshell surprises with stateful variables.
- Keep temporary file lifecycle explicit and safe.
- Make retries explicit for network-bound operations.

## Project-Aware Contracts
- Resolve repo root before mutating operations.
- Keep destructive paths guarded and explicit.
- Include dry-run mode for mass operations.
- Record required tools and versions in script headers.

## Metrics
- Script reproducibility across environments.
- Pipeline failure diagnosis time.
- Frequency of quoting/expansion defects.
- Local/CI behavior divergence rate.

## Revisit Triggers
- Repeat failures from shell option misunderstandings.
- Environment-specific behavior drift.
- Increase in brittle one-liner dependencies.
