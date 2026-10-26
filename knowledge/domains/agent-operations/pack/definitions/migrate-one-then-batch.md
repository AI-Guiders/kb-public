---
type: Definition Card
title: Migrate one, then batch
description: Массовая миграция — только после эталона на 1–2 файлах. «Потом поправлю» без gate = почти наверняка забудешь, пока человек не пнёт.
tags: [llm-native-card, definition, agent-operations]
---

# Migrate one, then batch

- id: migrate-one-then-batch
- kind: definition
- informal: Массовая миграция — только после эталона на 1–2 файлах. «Потом поправлю» без gate = почти наверняка забудешь, пока человек не пнёт.
- formal.order: draft_transform → apply_to_1_or_2 → inspect → fix_now → batch → verify_or_open_tracked_item
- gate_step: golden_pair_ok before batch
- gate_done: no_silent_later_fix; deferred_only_if_task_or_finding_written
- llm_cue: Did I say «потом поправлю»? Either fix now or open a tracked item — do not rely on memory.
- related: mc-mass-migrate-script-first, delta-radius-gate, stage-result
- sources: work/projects/door-to-singularity/cascade-ide/note-llm-native-world-product.md

