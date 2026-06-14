<!-- markdownlint-disable MD022 MD032 -->

# Git Safety and Recovery Rules v1

Set: 16 rules.  
Focus: safe operation, clean history, and deterministic recovery.

---

## Rule 01
- world: tooling.git
- epistemic_basis: `fact`
- confidence: `high`
- signal: unknown repository state before edit
- action: run `git status` before any change operation
- transfer_boundary: all repositories

## Rule 02
- world: tooling.git
- epistemic_basis: `fact`
- confidence: `high`
- signal: broad staging includes unrelated files
- action: stage only explicit files/scopes for logical commit
- transfer_boundary: all repositories

## Rule 03
- world: tooling.git
- epistemic_basis: `fact`
- confidence: `high`
- signal: commit message explains only "what"
- action: include intent and behavioral impact in commit message
- transfer_boundary: all repositories

## Rule 04
- world: tooling.git
- epistemic_basis: `fact`
- confidence: `high`
- signal: one commit contains unrelated domains
- action: split into logical commits by concern
- transfer_boundary: all repositories

## Rule 05
- world: tooling.git
- epistemic_basis: `fact`
- confidence: `high`
- signal: local branch diverges from remote silently
- action: inspect ahead/behind status before push
- transfer_boundary: shared repositories

## Rule 06
- world: tooling.git
- epistemic_basis: `fact`
- confidence: `high`
- signal: request to force push shared branch
- action: block by default and require explicit approval
- transfer_boundary: shared `main/master` and team branches

## Rule 07
- world: tooling.git
- epistemic_basis: `fact`
- confidence: `high`
- signal: destructive cleanup is considered first option
- action: choose reversible path first (`restore`, branch copy, reflog)
- transfer_boundary: all repositories

## Rule 08
- world: tooling.git
- epistemic_basis: `fact`
- confidence: `high`
- signal: merge conflict loops repeatedly in same files
- action: isolate conflict class and create focused reconciliation commit
- transfer_boundary: active collaborative branches

## Rule 09
- world: tooling.git
- epistemic_basis: `fact`
- confidence: `high`
- signal: secrets staged accidentally
- action: unstage immediately and rotate credential if leaked
- transfer_boundary: all repositories

## Rule 10
- world: tooling.git
- epistemic_basis: `fact`
- confidence: `high`
- signal: lost commit pointer after reset/rebase
- action: recover via `git reflog` before further operations
- transfer_boundary: all repositories

## Rule 11
- world: tooling.git
- epistemic_basis: `inference`
- confidence: `medium`
- signal: review quality drops on large PRs
- action: keep PR scope narrow and commit series readable
- transfer_boundary: code review workflows

## Rule 12
- world: tooling.git
- epistemic_basis: `fact`
- confidence: `high`
- signal: branch accumulates long-lived drift
- action: synchronize branch frequently and resolve early
- transfer_boundary: long-running feature branches

## Rule 13
- world: tooling.git
- epistemic_basis: `fact`
- confidence: `high`
- signal: unfinished work needs context switch
- action: checkpoint with commit or named stash note
- transfer_boundary: all repositories

## Rule 14
- world: tooling.git
- epistemic_basis: `inference`
- confidence: `medium`
- signal: repetitive hotfixes after merge
- action: strengthen pre-merge validation checklist for changed areas
- transfer_boundary: release-facing branches

## Rule 15
- world: tooling.git
- epistemic_basis: `fact`
- confidence: `high`
- signal: uncertainty about impact of reset/clean
- action: create safety branch before irreversible operation
- transfer_boundary: all repositories

## Rule 16
- world: tooling.git
- epistemic_basis: `fact`
- confidence: `high`
- signal: "clean tree" policy absent at session end
- action: end with clean state or explicit WIP marker
- transfer_boundary: all repositories

---

## Source Footing

- Practical Git safety protocol from operational multi-agent workflows.
- Repeated incident patterns around staging drift, force-push risk, and recovery needs.

<!-- markdownlint-enable MD022 MD032 -->

