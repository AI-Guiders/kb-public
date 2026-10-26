---
type: Status
title: 'Status: biology.mus-musculus (мир «Mus musculus — лабораторная мышь»)'
description: '**Домен:** лабораторная мышь — следующий референс после Drosophila melanogaster: клеточные атласы и частичные коннектомы (MICrONS — зрительная кора), без полного EM-коннектома мозга. Цель: знать всё доступное на текущий момент, чтобы при расширении CASA наслаивать знания о других животных.'
tags: [biology-mus-musculus, worlds, status]
language: ru
world: biology
subworld: mus-musculus
---
# Status: biology.mus-musculus (мир «Mus musculus — лабораторная мышь»)

**Домен:** лабораторная мышь — следующий референс после Drosophila melanogaster: клеточные атласы и частичные коннектомы (MICrONS — зрительная кора), без полного EM-коннектома мозга. Цель: знать всё доступное на текущий момент, чтобы при расширении CASA наслаивать знания о других животных.

---

## Operating contract (текущий)

| Приоритет | Документ | Когда |
|-----------|----------|-------|
| 1 | `playbook-mus-musculus-operational.md` | (ещё не создан — TODO) |
| 2 | `kb-mus-musculus-*.md` (слои) | fundamentals |
| 3 | `kb-<topic>-evidence.md` | факт + источник |
| 4 | `evidence-plan-mus-musculus.md` | карта тем и статус прохода |

---

## Что известно (честный снапшот, 2026-09-19)

### Полный EM-коннектом мозга мыши — ОТСУТСТВУЕТ
- Мышь ~70–80 млн нейронов (~500× дрозофилы); EM-объём и proofreading — на порядки дороже.
- **MICrONS** (Allen/Princeton/Baylor): ~1 мм³ зрительной коры (несколько областей V1/V2), ~200k нейронов, сотни млн синапсов — **НЕ весь мозг**.
  - Nature 2025: «Functional connectomics spanning multiple areas of mouse visual cortex» (PMC11981939, OA)
  - Nature 2025: «Functional connectomics reveals general wiring rule in mouse visual cortex» (PMC11981947, OA)
- **Перспективы** (не реализация): Cell Rep Methods 2025 «Comparative prospects of imaging methods for whole-brain mammalian connectomics» (PMC11955263, OA).
- Клеточные/транскриптомные атласы: Allen Brain Atlas / Cell Types (CCT) — существуют (полный проход — TODO).

### Связь с дрозофилой
- Дрозофила — полный референс (коннектом CNS есть: BANC/FAFB/MCNS + зрительная доля: Nature 2025, PMC12119369 — 732 типа).
- Мышь — «следующая ступень»: при расширении CASA — наслаивать знания о других животных (начиная с мыши, когда данные созреют).

---

## Maintenance Policy

- **Проверено:** 2026-09-19 — каркас создан; данные — по аннотациям/поиску (Europe PMC); полные тексты MICrONS — TODO.
- **Next review triggers:** новые релизы MICrONS/whole-brain проекты (BRAIN Initiative, Janelia/Allen) → обновить статус; появление полного коннектома (частичных регионов — hippocampus, thalamus и т.п.) → evidence-проход.
- **Связь с evidence:** карточки `kb-<topic>-evidence.md` — по канону (полные тексты, Layer contract, confidence).

## Closure snapshot / Definition of Done (для мира)

Мир завершён, когда:
1. Все темы evidence-plan (1.1–x) пройдены по канону (полные тексты OA, карточки).
2. Слои `kb-mus-musculus-*.md` агрегируют evidence.
3. Синтез: что мышь даёт для CASA (расширение референса).
4. Reflect записан.
5. Только после — использование для CASA (наслоение).

## Active Guardrails

- Честность: «нет полного коннектома» — фиксировать как границу, не как «пробел в работе».
- Мышь ≠ дрозофила: не переносить выводы дрозофилы на мышь без проверки (масштаб, корковая организация, гомология).
- `worlds/` — публичный слой: без машинных путей, без `work/`-ссылок.
- Полные тексты (не абстракты) — для фундаментального прохода; скрининг — только отбор.

