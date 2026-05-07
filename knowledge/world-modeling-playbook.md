# World Modeling Playbook v1

## Purpose
Meta-playbook for keeping knowledge structure faithful to reality: intuition first, formalization second.

## Scope
- Domain/world boundary decisions
- Separation of similar-but-distinct ecosystems
- Router-layer vs world-layer architecture
- Ongoing correction when reality disproves structure

## Core Principle
- Do not force reality into a preselected schema.
- Let distinctions emerge from lived behavior, failures, and diagnostic practice.

## Intuition-First Loop
- Sense: identify where context "feels different" in causality, language, and action patterns.
- Probe: run one concrete scenario to test whether that difference is operationally real.
- Separate: if behavior diverges, keep worlds separate even when labels look similar.
- Bridge: connect worlds through router layers, not by merging world layers.
- Recalibrate: if evidence contradicts the map, update the map immediately.

## What Counts as a Separate World
- Different causal model of how things work.
- Different dominant failure modes.
- Different verification/diagnostic workflow.
- Different vocabulary that cannot be safely collapsed.

## What Belongs to a Router (Not a World)
- Tool choice guidance.
- Shared safety constraints.
- Cross-world interoperability rules.
- Navigation/index links.

## Anti-Patterns
- Premature unification "for convenience".
- Grouping by surface similarity (same category labels) despite behavioral divergence.
- Turning uncertain intuition into rigid ontology too early.
- Repeating known misclassification because "it looks cleaner".

## Recovery Protocol After Misclassification
- Split immediately when divergence is confirmed.
- Move shared pieces to router layer.
- Keep each world internally coherent and testable.
- Record one concise "why split happened" note for future intuition calibration.

## Metrics
- Number of re-splits caused by over-merging.
- Time to correct wrong categorization.
- Cross-world incident confusion rate.
- Stability of world boundaries over real project cycles.

## Revisit Triggers
- Frequent "this feels wrong" feedback during categorization.
- Repeated incidents where one playbook fails in one of the grouped ecosystems.
- Rising ambiguity in ownership of diagnostics and decisions.

## Calibration Examples (Fast Intuition Check)

### Example 1: Windows vs Linux
- Surface similarity: both are "OS environment troubleshooting".
- Divergence signal: service model, permissions, process lifecycle, and diagnostics toolchain differ materially.
- Decision: two worlds (`windows-environments`, `linux-environments`) + optional router bridge.

### Example 2: Regex vs Parser Logic
- Surface similarity: both "extract structure from text".
- Divergence signal: regex is pattern-matching with dialect/overmatch risks; parser logic is grammar/model-driven with different failure surfaces.
- Decision: keep regex as its own world; parser architecture belongs to another world (language/data tooling), linked via router.

### Example 3: Docker vs Host Runtime
- Surface similarity: both "runtime and operations".
- Divergence signal: container isolation, image lifecycle, volume/network boundary, and security model introduce distinct causal chains.
- Decision: keep Docker world separate from host-OS worlds; connect through deployment/ops router contracts.

### Example 4: Blazor vs Avalonia/XAML
- Surface similarity: both are ".NET UI".
- Divergence signal: runtime model (web vs desktop/native shell), rendering lifecycle, state/navigation contracts, deployment and diagnostics differ.
- Decision: keep separate UI worlds with shared frontend router patterns only where behavior is truly equivalent.

### Example 5: Roslyn Code Actions vs Manual Edits
- Surface similarity: both can produce the same textual code change.
- Divergence signal: Roslyn is symbol/semantic aware, while manual edits are text-level and can miss references/overloads/renames.
- Decision: keep semantic refactoring workflow as its own tooling world; manual patching remains a fallback world with stricter verification.
