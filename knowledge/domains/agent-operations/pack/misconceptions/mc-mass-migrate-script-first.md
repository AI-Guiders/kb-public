---
type: Misconception Card
title: 'Misconception: mc-mass-migrate-script-first'
tags: [llm-native-card, misconception, agent-operations]
language: ru
---

# Misconception: mc-mass-migrate-script-first

- id: mc-mass-migrate-script-first
- kind: misconception
- false_claim: Увидел тонну файлов → написал скрипт → прогнал на всём → «ошибки потом поправлю».
- why_wrong: Типичный LLM-паттерн. Скрипт не доказан на 1–2 эталонах; массовый прогон закрепляет косяки; фраза «потом поправлю» часто = амнезия до пинка человека — ошибки не замечаются сами.
- correction_definition: migrate-one-then-batch
- delta_radius_hint: Prove on 1–2 files first; no deferred-fix stack without a tracked gate; do not batch hoping to notice issues later.

