# PR Review Playbook v1

## Purpose

Keep review useful and fast: catch regressions early without turning review into paperwork.

## Review Order

1. Behavior risk first (what can break for users).
2. Data/safety risk second (loss, corruption, security, irreversible ops).
3. Test adequacy third (what proves the change is safe).
4. Readability/maintainability fourth (can next person change this safely).

## Minimal Reviewer Contract

- Start from changed behavior, not style trivia.
- Prefer 3-7 high-impact comments over many low-value notes.
- Mark uncertainty explicitly.
- Suggest concrete fix or validation step for each critical finding.

## Minimal Author Contract

- Explain intent and risk area in PR description.
- Include quick validation steps (build/test/manual checks).
- Keep PR scope focused; split unrelated changes.

## Stop Conditions

- No unresolved high-severity findings.
- Risky changes have a clear verification path.
- Reviewer understands why this change exists now.

## Anti-Patterns

- Review by checklist only, without reading behavior impact.
- Endless style comments while missing regression risk.
- “Looks fine” with no test or verification signal.

