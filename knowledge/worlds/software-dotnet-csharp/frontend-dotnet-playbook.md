# Frontend .NET Playbook v1

## Purpose
Unified frontend engineering playbook for .NET UI stacks:
- Blazor
- Avalonia
- XAML-based UI patterns

## Scope
- Architecture and state boundaries
- Rendering performance and responsiveness
- UX consistency and accessibility
- Test strategy for UI behavior

## Evidence-Based Working Format
- Fact: capture observable issue or outcome (latency, rerender loop, state drift, UX friction).
- Hypothesis: define the expected improvement and mechanism.
- Check: implement a minimal change and verify with focused measurement.
- Decision criterion: predefine keep/rollback/escalate threshold.
- Confidence mark: tag confidence separately from preference.

## Architecture Baseline
- Keep domain and application logic outside UI components.
- Separate state ownership from rendering concerns.
- Prefer explicit data flow over implicit coupling.
- Treat navigation and component lifecycle as first-class contracts.

## Blazor Track
- Component boundaries and parameter design.
- Rendering discipline (`ShouldRender`, memoization, event frequency control).
- State containers and async data loading patterns.
- WASM vs Server tradeoffs and failure modes.

## Avalonia and XAML Track

**CascadeIDE / Dock / дизайн-имплементация:** полная цепочка **status → playbook → kb** — `status-avalonia-cascade-ide-ui-v1.md`, `playbook-avalonia-dock-ui-v1.md`, `kb-avalonia-ui-dock-fundamentals-v1.md`; маршрутизатор индекса: секция `router-avalonia-ui` в `index-knowledge-router-v1.md`.

- MVVM boundaries and command/state flow.
- Resource dictionaries, styling, and theme consistency.
- Visual tree cost control and virtualization strategy.
- Cross-platform behavior and input parity checks.

## UI Quality Contracts
- One primary action per context.
- Explicit loading/empty/error states.
- Keyboard-first support for critical workflows.
- Deterministic back navigation and preserved context.

## Testing Contracts
- Component-level behavior tests for key interactions.
- Integration tests for critical user journeys.
- Snapshot testing only as a supplement, not as sole confidence source.
- Regression checklist for high-risk UI flows.

## Metrics
- Time-to-interactive for critical screens.
- Rerender frequency in hot paths.
- UI error/retry rate.
- Flow completion rate for primary tasks.

## Revisit Triggers
- Growing UI latency or input lag.
- Repeat regressions in the same flows.
- Support feedback about navigation confusion.
- Increased divergence between UI stacks (Blazor/Avalonia/XAML).

