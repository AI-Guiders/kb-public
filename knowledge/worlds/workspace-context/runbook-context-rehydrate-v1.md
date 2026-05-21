# Context Rehydrate Runbook v1

## Trigger

Use this runbook when context is compressed, reset, or uncertain.

## Procedure

1. Confirm active workspace/scope.
2. Open `index-knowledge-router-v1.md`.
3. Follow `status -> playbook -> matrix -> kb` order.
4. Stop at first sufficient answer layer (do not over-read).
5. Record what was loaded and why in short operational note.

## Stop Conditions

- Current task is answerable with loaded artifacts.
- No unresolved scope ambiguity remains.

## Escalation Conditions

- Conflicting domain guidance -> escalate to matrix layer.
- Missing artifact in index -> add index entry before continuing.
- Repeated ambiguity -> open scope clarification question.

## Anti-Patterns

- Loading multiple large `kb-*` files before defining scope.
- Mixing global and country-specific guidance without routing matrix.
- Answering from memory when index points to fresher artifact.
