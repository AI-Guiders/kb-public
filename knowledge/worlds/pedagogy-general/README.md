---
type: Index
title: Мир **pedagogy.general**
description: '**Идентификатор мира:** `pedagogy.general`'
tags: [pedagogy-general, readme, worlds]
world: pedagogy
subworld: general
---
# Мир **pedagogy.general**


**Идентификатор мира:** `pedagogy.general`  
**Каталог:** `knowledge/worlds/pedagogy-general/`  
**Назначение:** сквозная **школьная предметная педагогика** (instruction science + subject fundamentals) для authoring curriculum и gate-конструктов. **Не** замена учебника; **не** академическая лингвистика «для зачёта».

**Не путать с:**

| Мир | Граница |
|-----|---------|
| [`../cognition-language-acquisition/`](../cognition-language-acquisition/) | human **child L1 acquisition** (Snow, Clark, Saxton) — `transfer_boundary: deny` → school pedagogy spec без bridge |
| [`../ml-learning-dynamics/`](../ml-learning-dynamics/) | ML-аналоги curriculum/replay — `allow-with-check` |
| [`../math-numerics-pde/`](../math-numerics-pde/) | инженерная numerics, не школьная math pedagogy |

## Слои канона (порядок загрузки)

| Слой | Файл | Роль |
|------|------|------|
| **Status** | [`status-pedagogy-school-subjects.md`](status-pedagogy-school-subjects.md) | DoD, guardrails, покрытие subject worlds |
| **Playbook (F→O)** | [`playbook-pedagogy-fundamentals-to-operational.md`](playbook-pedagogy-fundamentals-to-operational.md) | Порядок перед lab/authoring |
| **Master router** | [`playbook-pedagogy-school-subjects.md`](playbook-pedagogy-school-subjects.md) | Маршрут по предметам |
| **Fundamentals** | [`kb-pedagogy-fundamentals.md`](kb-pedagogy-fundamentals.md) | ЗУН, gate, teacher vs field |
| **Scientific evidence (index)** | [`kb-pedagogy-scientific-evidence.md`](kb-pedagogy-scientific-evidence.md) | DOI, read_depth, cross-cutting papers |
| **Synthesis** | [`kb-pedagogy-evidence-global.md`](kb-pedagogy-evidence-global.md) | Rosenshine + CLT → operational mapping |
| **RU developmental (authoring hints)** | [`kb-pedagogy-developmental-methods-ru.md`](kb-pedagogy-developmental-methods-ru.md) | Эльконин, Занков — **не** formal doctrine |
| **Reading map** | [`map-pedagogy-school-subjects-reading.md`](map-pedagogy-school-subjects-reading.md) | Tracks A–D, ingest protocol |
| **Transfer** | [`matrix-pedagogy-cross-subject-transfer.md`](matrix-pedagogy-cross-subject-transfer.md) | Subject ↔ subject; pedagogy ↔ cognition L1 |

## Subject worlds

| Мир | Папка |
|-----|-------|
| `pedagogy.russian-language` | [`../pedagogy-russian-language/`](../pedagogy-russian-language/) |
| `pedagogy.literature` | [`../pedagogy-literature/`](../pedagogy-literature/) |
| `pedagogy.mathematics` | [`../pedagogy-mathematics/`](../pedagogy-mathematics/) |
| `pedagogy.physics` | [`../pedagogy-physics/`](../pedagogy-physics/) |
| `pedagogy.chemistry` | [`../pedagogy-chemistry/`](../pedagogy-chemistry/) |
| `pedagogy.biology` | [`../pedagogy-biology/`](../pedagogy-biology/) |
| `pedagogy.history` | [`../pedagogy-history/`](../pedagogy-history/) |
| `pedagogy.geography` | [`../pedagogy-geography/`](../pedagogy-geography/) |
| `pedagogy.social-studies` | [`../pedagogy-social-studies/`](../pedagogy-social-studies/) |
| `pedagogy.second-native-language` | [`../pedagogy-second-native-language/`](../pedagogy-second-native-language/) |
| `pedagogy.informatics` | [`../pedagogy-informatics/`](../pedagogy-informatics/) |
| `pedagogy.visual-arts` | [`../pedagogy-visual-arts/`](../pedagogy-visual-arts/) |

Музыка (теория): [`../arts-music/`](../arts-music/) — не дублировать.

## Router

Строка **Pedagogy (school subjects)** в [`index-knowledge-router.md`](../../index-knowledge-router.md); supplement: `router-pedagogy-school-subjects`.

## Публикация (kb-public)

Перед коммитом: [`../knowledge-engineering/playbook-kb-world-public-authoring.md`](../knowledge-engineering/playbook-kb-world-public-authoring.md).

