---
type: KB
description: 'Set: 16 rules.'
tags: [hci-ux-dx, kb, worlds]
language: en
epistemic: '`inference`'
world: hci
subworld: ux-dx
---
<!-- markdownlint-disable MD022 MD032 -->

# HCI Usability and Dialog Rules v1


Set: 16 rules.  
Focus: usable interfaces, predictable behavior, and low-friction human-agent dialogue.

---

## Rule 01
- world: hci.usability
- confidence: `high`
- signal: users ask "where am I?" or "what changed?"
- action: increase state visibility with clear page/flow context markers
- transfer_boundary: all interactive products

## Rule 02
- world: hci.usability
- confidence: `high`
- signal: high error rate in destructive operations
- action: require reversible path or explicit confirmation with impact preview
- transfer_boundary: high-impact actions

## Rule 03
- world: hci.usability
- confidence: `high`
- signal: repeated form submission failures
- action: validate near the field and provide immediate recovery guidance
- transfer_boundary: forms and structured input flows

## Rule 04
- world: hci.cognitive-load
- confidence: `medium`
- signal: users miss critical controls on dense screens
- action: reduce visual competition and promote primary action hierarchy
- transfer_boundary: operational dashboards and admin tools

## Rule 05
- world: hci.cognitive-load
- confidence: `high`
- signal: users copy values across screens from memory
- action: prefer recognition cues and contextual carry-over over recall-heavy steps
- transfer_boundary: multi-step workflows

## Rule 06
- world: hci.accessibility
- confidence: `high`
- signal: action path depends on pointer-only interaction
- action: provide full keyboard path for primary workflow
- transfer_boundary: all critical flows

## Rule 07
- world: hci.accessibility
- confidence: `high`
- signal: status is encoded only by color
- action: add textual/iconic redundant status markers
- transfer_boundary: all status and alert components

## Rule 08
- world: hci.feedback
- confidence: `high`
- signal: user repeats clicks under uncertain latency
- action: expose progress and disable duplicate action while processing
- transfer_boundary: async actions

## Rule 09
- world: hci.feedback
- confidence: `medium`
- signal: users abandon flow after generic error
- action: convert error text into one concrete next action
- transfer_boundary: error handling surfaces

## Rule 10
- world: hci.navigation
- confidence: `high`
- signal: users frequently backtrack across unrelated pages
- action: tighten information architecture and shorten navigation depth for primary jobs
- transfer_boundary: high-frequency tasks

## Rule 11
- world: hci.dialog
- confidence: `high`
- signal: assistant asks many low-value questions
- action: ask only missing information required for safe forward progress
- transfer_boundary: conversational UX

## Rule 12
- world: hci.dialog
- confidence: `high`
- signal: response confidence exceeds available evidence
- action: label uncertainty explicitly and propose smallest validating step
- transfer_boundary: conversational UX

## Rule 13
- world: hci.dialog
- confidence: `medium`
- signal: long responses block user action
- action: default to concise answer plus optional deep path
- transfer_boundary: conversational UX

## Rule 14
- world: hci.reliability
- confidence: `high`
- signal: regressions recur in the same user path
- action: add scenario-level regression check for that path
- transfer_boundary: release-critical flows

## Rule 15
- world: hci.measurement
- confidence: `high`
- signal: design debates rely on preference only
- action: resolve with task metrics (completion, error, recovery, time)
- transfer_boundary: product and UX review process

## Rule 16
- world: hci.governance
- confidence: `medium`
- signal: process weight rises without quality gains
- action: remove ritual steps that do not improve user outcomes
- transfer_boundary: design and review governance

---

## Source Footing

- ISO 9241 human-centered interaction principles.
- WCAG/WAI accessibility standards and implementation practice.
- Applied usability heuristics and production UX incident patterns.

<!-- markdownlint-enable MD022 MD032 -->

