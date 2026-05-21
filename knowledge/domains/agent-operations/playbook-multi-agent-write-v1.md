# Multi-agent write v1

Тело секции `multi-agent-write-protocol-v1` из `agent-notes.md`. Hub оркестрации: `knowledge/worlds/agent-orchestration/`.

<!-- section:multi-agent-write-protocol-v1 -->
## Multi-Agent Write Protocol v1
- Context: Auto mode may rotate models/agents inside one long-running workflow.
- Goal: prevent note corruption, overwrite races, and context drift under parallel writes.

- Write roles:
  - append-only channel: default for concurrent agents (safe by design).
  - section-upsert channel: only for owned sections with lock metadata.

- Lock metadata contract (for upsert-capable writes):
  - owner_agent: <agent label>
  - lease_started_at: <ISO datetime>
  - lease_ttl_sec: <integer>
  - base_revision: <latest known revision id or timestamp>

- Safe write sequence:
  1) read hot context,
  2) acquire section lease (owner + ttl),
  3) perform minimal upsert,
  4) release lease marker,
  5) append short write-log entry.

- Conflict policy:
  - if lease active by another agent -> fallback to append-only note with "pending-merge" tag.
  - if base revision changed during write -> do not force overwrite; append diff-intent and retry merge.
  - never delete unknown sections during conflict resolution.

- Merge policy:
  - prefer additive merge first,
  - if semantic conflict remains: keep both variants with conflict tags and resolve in next compaction pass.

- Compaction policy:
  - run periodic compact pass to merge duplicates and clear resolved conflict tags.
  - preserve decision records and source anchors during compaction.

- Reliability invariants:
  - no blind overwrite,
  - no destructive conflict resolution,
  - every write traceable by owner and timestamp.
<!-- /section:multi-agent-write-protocol-v1 -->
