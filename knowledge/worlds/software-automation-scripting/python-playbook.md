# Python Playbook v1

## Purpose
Dedicated playbook for robust Python usage in automation, data processing, and tooling tasks.

## Scope
- Runtime and dependency discipline
- Script-to-module evolution
- Data parsing and encoding safety
- Testability and maintainability

## Evidence-Based Working Format
- Fact: capture current failure mode or maintainability pain.
- Hypothesis: define expected improvement from change.
- Check: validate with minimal deterministic run and tests.
- Decision criterion: success/failure thresholds before adoption.
- Confidence mark: explicit certainty level.

## Core Contracts
- Keep environment reproducible (venv/lock policy documented).
- Make input/output contracts explicit.
- Isolate pure transformation logic from side effects.
- Use explicit encoding and locale assumptions.

## Code Quality Contracts
- Prefer typed boundaries where it reduces ambiguity.
- Keep modules small and single-purpose.
- Treat exceptions as contract signals, not hidden control flow.
- Avoid global mutable state in reusable scripts.

## Data and Parsing Contracts
- Validate schema assumptions early.
- Handle malformed data with clear error paths.
- Keep regex/parsing logic test-covered.
- Preserve provenance metadata when transforming datasets.

## Testing Contracts
- Unit-test core parsing and transformation functions.
- Add integration tests for IO-heavy workflows.
- Keep fixture sets for edge cases and regressions.
- Track flaky behavior and remove nondeterminism sources.

## Metrics
- Script failure rate in routine runs.
- Mean time to diagnose Python task failures.
- Regression frequency after parser changes.
- Time from ad-hoc script to maintainable module.

## Revisit Triggers
- Repeated encoding or dependency issues.
- Scripts growing beyond maintainable size.
- Frequent runtime surprises from implicit assumptions.

