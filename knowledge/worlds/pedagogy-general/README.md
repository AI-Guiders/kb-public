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
| **Status** | [`status-pedagogy-school-subjects-v1.md`](status-pedagogy-school-subjects-v1.md) | DoD, guardrails, покрытие subject worlds |
| **Playbook (F→O)** | [`playbook-pedagogy-fundamentals-to-operational-v1.md`](playbook-pedagogy-fundamentals-to-operational-v1.md) | Порядок перед lab/authoring |
| **Master router** | [`playbook-pedagogy-school-subjects-v1.md`](playbook-pedagogy-school-subjects-v1.md) | Маршрут по предметам |
| **Fundamentals** | [`kb-pedagogy-fundamentals-v1.md`](kb-pedagogy-fundamentals-v1.md) | ЗУН, gate, teacher vs field |
| **Scientific evidence (index)** | [`kb-pedagogy-scientific-evidence-v1.md`](kb-pedagogy-scientific-evidence-v1.md) | DOI, read_depth, cross-cutting papers |
| **Synthesis** | [`kb-pedagogy-evidence-global-v1.md`](kb-pedagogy-evidence-global-v1.md) | Rosenshine + CLT → operational mapping |
| **RU developmental (authoring hints)** | [`kb-pedagogy-developmental-methods-ru-v1.md`](kb-pedagogy-developmental-methods-ru-v1.md) | Эльконин, Занков — **не** formal doctrine |
| **Reading map** | [`map-pedagogy-school-subjects-reading-v1.md`](map-pedagogy-school-subjects-reading-v1.md) | Tracks A–D, ingest protocol |
| **Transfer** | [`matrix-pedagogy-cross-subject-transfer-v1.md`](matrix-pedagogy-cross-subject-transfer-v1.md) | Subject ↔ subject; pedagogy ↔ cognition L1 |

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

Строка **Pedagogy (school subjects)** в [`index-knowledge-router-v1.md`](../../index-knowledge-router-v1.md); supplement: `router-pedagogy-school-subjects`.

## Публикация (kb-public)

Перед коммитом: [`../knowledge-engineering/playbook-kb-world-public-authoring-v1.md`](../knowledge-engineering/playbook-kb-world-public-authoring-v1.md).

**Версия:** v1.0 · 2026-06-06

