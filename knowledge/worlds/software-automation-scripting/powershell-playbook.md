# PowerShell Playbook v1

## Purpose
Dedicated playbook for reliable Windows-first automation using PowerShell.

## Scope
- Object pipeline design
- Command composition and error contracts
- Script safety for repo-aware automation
- Interop with external tools

## Evidence-Based Working Format
- Fact: capture failing command behavior or operational friction.
- Hypothesis: define the smallest script change with expected effect.
- Check: run deterministic validation path with explicit outputs.
- Decision criterion: keep/rollback thresholds.
- Confidence mark: explicit certainty level.

## Core Contracts
- Prefer object pipeline over fragile string parsing.
- Make path handling explicit and quote paths with spaces.
- Use strict error behavior for production scripts.
- Keep command intent clear with named parameters.

## Error and Exit Contracts
- Convert non-terminating errors to explicit failure when needed.
- Surface external command exit codes clearly.
- Avoid silent failures and swallowed exceptions.
- Log enough context to reproduce failures quickly.

## Project-Aware Contracts
- Resolve repository/workspace root before write operations.
- Keep mutation boundary explicit in script header.
- Require confirmation or dry-run for destructive operations.
- Record assumptions about tools, environment variables, and permissions.

## Interop Contracts
- Distinguish PowerShell-native behavior from external CLI behavior.
- Normalize outputs when chaining with Git/dotnet/docker tools.
- Keep encoding assumptions explicit for file IO and command output.
- Use predictable formatting for machine-consumable outputs.

## Metrics
- Automation success rate.
- Mean time to identify failing command.
- Re-run count before successful completion.
- Incidents caused by ambiguous path or quoting behavior.

## Revisit Triggers
- Frequent path/quoting regressions.
- Repeat failures from implicit error semantics.
- Growing script complexity without modularization.
