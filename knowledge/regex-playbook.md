# Regex Playbook v1

## Purpose
Dedicated playbook for reliable regular expression design, validation, and maintenance.

**Knowledge cluster (syntax, engines, dialects, карта глав MRE3):** `index-knowledge-regex-cluster-v1.md` и `kb-regex-*` в этом каталоге; маршрутизация в `index-knowledge-router-v1.md` (секция `router-regex`). Загружать playbook первым, затем точечно один `kb-regex-*` по вопросу.

## Scope
- Pattern design and readability
- Dialect differences across engines
- Safety against false positives and destructive matches
- Test discipline for evolving patterns

## Evidence-Based Working Format
- Fact: capture concrete mismatch, parse failure, or overmatch.
- Hypothesis: define exactly how pattern change should fix behavior.
- Check: run pattern on representative positive and negative samples.
- Decision criterion: predefined accept/reject thresholds.
- Confidence mark: separate certainty from guesswork.

## Core Contracts
- Treat regex as code: document intent and boundaries.
- Prefer explicit anchors, groups, and boundaries over broad wildcards.
- Keep patterns reviewable; split complex intent into staged patterns if needed.
- Use named groups where supported for semantic clarity.

## Dialect Awareness
- .NET/PowerShell: engine semantics and options differ from POSIX tools.
- Bash toolchain: `grep/sed/awk` regex variants are not interchangeable.
- Python `re`: behavior differs from .NET in lookbehinds/options and flags.
- Always record target engine with the pattern.

## Safety Rules
- Validate against counterexamples before production use.
- Add guardrails when regex output drives file mutations.
- Avoid silent fallback behavior on no-match in destructive flows.
- Prefer parser logic over regex if grammar complexity becomes high.

## Testing Contracts
- Keep test fixtures for positive, negative, and edge samples.
- Include encoding and locale variants where relevant.
- Add regression tests for every bug-inducing pattern change.
- Record known non-goals explicitly.

## Metrics
- False-positive rate.
- False-negative rate.
- Time to diagnose regex-driven incidents.
- Number of regex changes without regressions.

## Revisit Triggers
- Repeated parsing incidents caused by pattern drift.
- Increasing pattern complexity with low readability.
- Frequent cross-engine incompatibility failures.
