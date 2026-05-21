# CMD Playbook v1

## Purpose
Dedicated playbook for Windows CMD/batch automation in legacy and compatibility scenarios.

## Scope
- Batch reliability constraints
- Quoting and variable expansion pitfalls
- Errorlevel-based control flow
- Safe interop with modern tooling

## Evidence-Based Working Format
- Fact: describe concrete batch failure or compatibility requirement.
- Hypothesis: define smallest batch change to resolve it.
- Check: run deterministic test scenario with explicit outputs.
- Decision criterion: predefined success/failure threshold.
- Confidence mark: explicit certainty level.

## Core Contracts
- Use CMD only when compatibility requires it.
- Keep quoting explicit for all file paths.
- Validate delayed expansion behavior before rollout.
- Keep control flow readable and deterministic.

## Error Contracts
- Use `if errorlevel` checks consistently.
- Preserve exit code semantics for calling processes.
- Avoid fall-through behavior in failure branches.
- Surface command failure context in logs.

## Project-Aware Contracts
- Resolve target directory before write operations.
- Guard destructive commands with explicit target confirmation.
- Keep environment assumptions documented.
- Prefer wrapper scripts when orchestration complexity grows.

## Interop Contracts
- Be explicit when invoking PowerShell, Bash, Python, or Docker from CMD.
- Normalize return-code handling at boundaries.
- Keep encoding and locale behavior visible when parsing text outputs.
- Minimize fragile parsing of tool output strings.

## Metrics
- Success rate in legacy automation flows.
- Incidents caused by quoting or delayed expansion.
- Time to diagnose `errorlevel` control-flow failures.
- Frequency of CMD-specific regressions after changes.

## Revisit Triggers
- Rising maintenance cost of batch scripts.
- Repeated interop issues with modern toolchain.
- Frequent regressions from environment drift.
