<!-- markdownlint-disable MD022 MD032 -->

# PR Review Risk Rules v1

Set: 10 rules.  
Focus: high-signal review with low process overhead.

---

## Rule 01
- world: tooling.pr-review
- epistemic_basis: `fact`
- confidence: `high`
- signal: review starts from coding style
- action: start from behavior risk and failure modes
- transfer_boundary: all PR reviews

## Rule 02
- world: tooling.pr-review
- epistemic_basis: `fact`
- confidence: `high`
- signal: change touches persistence/state transitions
- action: require explicit data-integrity check path
- transfer_boundary: data-affecting PRs

## Rule 03
- world: tooling.pr-review
- epistemic_basis: `fact`
- confidence: `high`
- signal: critical branch logic changed without tests
- action: block merge until verification exists
- transfer_boundary: behavior-changing PRs

## Rule 04
- world: tooling.pr-review
- epistemic_basis: `inference`
- confidence: `medium`
- signal: PR mixes unrelated concerns
- action: split into logical units before merge
- transfer_boundary: medium/large PRs

## Rule 05
- world: tooling.pr-review
- epistemic_basis: `fact`
- confidence: `high`
- signal: reviewer notes “not sure”
- action: label uncertainty and request targeted evidence
- transfer_boundary: all PR reviews

## Rule 06
- world: tooling.pr-review
- epistemic_basis: `fact`
- confidence: `high`
- signal: operational behavior changed (timeouts/retries/limits)
- action: require rollback or mitigation note
- transfer_boundary: reliability-sensitive PRs

## Rule 07
- world: tooling.pr-review
- epistemic_basis: `fact`
- confidence: `high`
- signal: potential secret/token exposure
- action: block immediately and require rotation plan
- transfer_boundary: all repositories

## Rule 08
- world: tooling.pr-review
- epistemic_basis: `inference`
- confidence: `medium`
- signal: reviewer comments are many but low impact
- action: prioritize top risk findings and de-prioritize trivia
- transfer_boundary: all PR reviews

## Rule 09
- world: tooling.pr-review
- epistemic_basis: `fact`
- confidence: `high`
- signal: merge pressure bypasses unresolved high-risk comment
- action: keep PR unmerged until risk resolved or explicitly accepted
- transfer_boundary: protected branches

## Rule 10
- world: tooling.pr-review
- epistemic_basis: `fact`
- confidence: `high`
- signal: post-merge regressions repeat
- action: fold incident lesson into review rule/check
- transfer_boundary: active codebases

---

## Source Footing

- Practical review patterns from multi-agent and production-adjacent workflows.
- Recurring failure classes: missed behavior regressions, mixed PR scope, weak verification paths.

<!-- markdownlint-enable MD022 MD032 -->

