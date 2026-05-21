# Automation Scripting Playbook v1

## Purpose
Router playbook for project-aware automation decisions across scripting and container tools.

## Scope
- Tool selection by task profile
- Shared safety contracts for all automation
- Evidence-based execution flow
- Links to specialized subdomain playbooks

## Evidence-Based Working Format
- Fact: describe current manual burden or failure pattern.
- Hypothesis: state which automation change removes that burden and why.
- Check: run the smallest deterministic scenario.
- Decision criterion: define success/failure threshold before rollout.
- Confidence mark: tag certainty level explicitly.

## Project-Aware Global Contracts
- Resolve workspace/repo root explicitly before mutating actions.
- Declare mutation boundary: what can change and what must remain untouched.
- Keep environment assumptions explicit (`required tools`, `required vars`, `required permissions`).
- Make logs actionable and preserve deterministic exit codes.
- Prefer dry-run for bulk/destructive operations.

## Tool Selection Matrix
- Use `powershell-playbook.md` for Windows-first automation and object pipelines.
- Use `bash-playbook.md` for Unix/POSIX flows and shell orchestration.
- Use `python-playbook.md` for complex parsing/transformation and reusable logic.
- Use `cmd-playbook.md` only for legacy batch compatibility constraints.
- Use [`../pattern-regex/regex-playbook.md`](../pattern-regex/regex-playbook.md) when matching/parsing logic is core to the task.
- Use `docker-playbook.md` when reproducibility and environment parity are required.

## Cross-Tool Safety Rules
- Never run destructive commands against ambiguous target paths.
- Keep quoting/escaping explicit for all paths containing spaces.
- Avoid hidden global state; pass inputs explicitly.
- Include rollback or restore path for stateful operations.

## Metrics
- Time saved vs manual process.
- Failure frequency and mean time to recovery.
- Number of reruns needed for successful completion.
- Environment-specific failure rate.

## Revisit Triggers
- Frequent manual interventions in scripted flows.
- Rising automation flakiness across environments.
- Repeat incidents caused by wrong tool choice.
- Onboarding friction for running core scripts.
