# Tooling and Debug Playbook v1

## Purpose
Playbook for build, test, diagnostics, and debugging workflows across .NET projects.

## Related Specialized Playbook
- `.NET Roslyn and Debug`: `dotnet-roslyn-debug-playbook.md` (symbol-aware diagnostics/refactoring/debug depth).

## Scope
- Build and test reliability
- Debug loop speed
- Diagnostic signal quality
- Incident-to-fix workflow discipline

## Evidence-Based Working Format
- Fact: capture failing signal (build break, flaky test, runtime fault).
- Hypothesis: define likely cause and smallest corrective action.
- Check: validate with focused rebuild/retest/debug step.
- Decision criterion: predefine close/escalate threshold.
- Confidence mark: separate certainty from speculation.

## Operational Baseline
- Keep the shortest reliable feedback loop first (lint/diagnostics/build/test).
- Prefer structured diagnostics over ad-hoc log reading.
- Isolate failures by scope: file -> project -> solution.
- Keep debugging state reproducible (breakpoints, target, args, environment).

## Build and Test Contracts
- Build failures are fixed before optional refactors.
- Tests are grouped by confidence level (smoke, integration, extended).
- Flaky tests are tracked explicitly and not silently ignored.
- CI and local contracts stay aligned where practical.

## Diagnostics Contracts
- Treat warnings as triage candidates, not noise by default.
- Use language-native diagnostics providers when available.
- Keep issue-to-fix traceability in notes/checklists.
- Prefer one validated root cause over multiple speculative fixes.

## Identity Failure Triage (Git)
- Symptom class: `Author identity unknown` / `empty ident name`.
- Minimal triage order:
  1. In the same shell that failed, check config origin:
     - `git config --show-origin --get user.name`
     - `git config --show-origin --get user.email`
  2. Inspect effective ident:
     - `git var GIT_AUTHOR_IDENT`
     - `git var GIT_COMMITTER_IDENT`
  3. Inspect environment overrides in that shell:
     - `GIT_AUTHOR_*`, `GIT_COMMITTER_*`, `EMAIL`.
- Close condition:
  - commit succeeds in intended shell with expected author ident.
- Safe workaround when shell mismatch persists:
  - one-shot commit with `git -c user.name=... -c user.email=... commit ...`.

## Debugging Workflow
- Reproduce with minimal scenario first.
- Confirm expected/actual state before stepping deeper.
- Verify assumptions after each step-out/continue cycle.
- End each session with one concise root-cause note.

## Tools Coverage
- .NET build/test and runtime diagnostics toolchain.
- Roslyn-based code diagnostics and code actions.
- Debugger orchestration through MCP-connected flows.
- Log and trace capture for post-incident analysis.

## Metrics
- Mean time to identify root cause.
- Mean time to restore a broken build/test pipeline.
- Reopen rate for previously fixed defects.
- Percentage of incidents with documented root cause.

## Revisit Triggers
- Build/test cycle times trending upward.
- Repeated failure classes with no checklist updates.
- High debug session time with low signal.
- Frequent regressions after seemingly successful fixes.
