---
type: Misconception Card
title: 'Misconception: mc-kolb-only-in-chat'
tags: [llm-native-card, misconception, epistemic-scene, cdp-adr-0002]
language: ru
world: epistemic
subworld: scene
---

# Misconception: mc-kolb-only-in-chat

- id: mc-kolb-only-in-chat
- kind: misconception
- false_claim: «Я в inference-space» = сказать это в ответе / CoT; journal не нужен.
- why_wrong: Chat и CoT не переживают compaction и turn boundary. Без kolb-journal (DRAFT workbook) нет перечитываемого следа мысли: ни self-recheck, ни продолжение линии любым агентом. Journal ≠ жизнь между инференсами и ≠ JSON-форма — но без листа вспышка не оставляет рабочий материал. Spaces схлопываются в перформанс одной вспышки.
- correction_definition: kolb-journal
- applies_when: agent names Kolb/space only in dialogue text
- does_not_apply: step written to journal (finding/session/scratch) with settle fields
- inference_hooks: kolb-journal, curiosity-kolb-loop, inference-space
- delta_radius_hint: If next turn cannot re-read own prior decision+reason_changed — journal was missing.

