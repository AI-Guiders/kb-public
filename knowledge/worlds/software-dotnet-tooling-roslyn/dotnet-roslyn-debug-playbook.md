# .NET Roslyn and Debug Playbook v1

## Related

- Обязательный чеклист агента Cursor (Roslyn MCP, `file_path` по каждому затронутому `.cs`): [`playbook-csharp-roslyn-mcp-diagnostics-v1.md`](playbook-csharp-roslyn-mcp-diagnostics-v1.md).

## Purpose
Specialized playbook for C# diagnostics, refactorings, and debug workflows in .NET projects.

## Scope
- Roslyn-first diagnostics and code actions
- Structured build/test validation
- Debug session orchestration and evidence capture
- Fast root-cause isolation for C# runtime and logic failures

## Evidence-Based Working Format
- Fact: capture the exact failing diagnostic, test, or runtime symptom.
- Hypothesis: define the minimal likely cause.
- Check: apply smallest fix and re-run the shortest validating loop.
- Decision criterion: predefine close/escalate threshold.
- Confidence mark: explicit certainty tag and unresolved risk.

## Roslyn-First Contracts
- Use Roslyn diagnostics as primary source for C# errors/warnings.
- Prefer `get_code_actions` + `apply_code_action` over manual edits when available.
- Use symbol-aware navigation (`go_to_definition`, `find_usages`) for refactoring.
- Use semantic rename (`roslyn_rename`) for identifier-safe renames.

## Diagnostic Loop
- Scope diagnostic pass: file -> project -> solution.
- Fix highest-severity issues first, then warnings with behavior risk.
- Re-run diagnostics after each meaningful batch.
- Track recurring warning classes into checklist updates.

## Debug Session Contracts
- Always make target and arguments explicit before launch.
- Keep breakpoints tied to current target artifact.
- Use continue/step/inspect cycle with explicit assumption checks.
- End session with concise root cause + fix verification note.

## Build/Test Validation Contracts
- Run build after structural refactors.
- Run impacted tests before broad test suites.
- Treat flaky tests as defects in feedback reliability.
- Keep local loop aligned with CI contracts.

## Common Failure Patterns
- Symbol rename without usage sweep -> semantic drift.
- Manual fix bypassing code action -> hidden style/semantic inconsistency.
- Debug without stable repro -> misleading observations.
- Multi-fix commit without intermediate checks -> unclear causality.

## Metrics
- Time to first valid diagnosis.
- Time to green build after first failure.
- Ratio of code-action fixes vs manual fixes.
- Reopen rate for fixed debug incidents.

## Revisit Triggers
- Repeat diagnostic classes over multiple cycles.
- High debug time with weak reproducibility.
- Frequent mismatch between local and CI outcomes.
- Rising regressions after refactors.
