# Note: KB reorganization — rhetoric layer & agent operations v1

**Tags:** #knowledge-engineering #kb-taxonomy #rhetoric-pragmatics #living  
**Status:** proposal + first slice shipped 2026-08-22  
**ADR context:** [009-kb-entry-structure-and-pre-open-onboarding.md](../../adr/009-kb-entry-structure-and-pre-open-onboarding.md) — **инкремент**, не big bang.

## Вопрос

«Уже пора реорганизовать KB?» — **пора точечно**, не «перетащить всё».

## Диагноз

1. **Рост без оси:** `domains/agent-operations` (как действовать) + `evidence-humanities-shelf` (разнородная эвиденция) + `culture-dialogue-insights` (живой диалог) — **без** явного мира «речевые ситуации / жанры».
2. **Смешение слоёв** в одном ответе агента: operational playbook + disclaimer-жанр + теория — модель и люди путают.
3. **Fundamental pass** отложен: speech_situation обсуждался как теги, без первоисточников.

## Принцип реорганизации (три слоя)

| Слой | Где | Что |
|------|-----|-----|
| **Evidence + fundamentals** | `worlds/<slug>/` | Первоисточники → `kb-*-evidence-v1` → fundamentals spine |
| **Operational** | `domains/agent-operations/` | Playbooks, `speech_situation` теги, integrity, XL scenarios |
| **Applied / личное** | `personal/`, `culture-dialogue-insights` | Самоотчёты, инсайты диалога — gold, не теория |

**Не ломать:** `work/`, router в корне, Integrity POST, ADR 009 легаси-пути.

## Что сделано (slice 1)

- Новый мир **`worlds/rhetoric-pragmatics/`** (`rhetoric.pragmatics`) — status, playbook, fundamentals, map fundamental pass, Bitzer + Bakhtin evidence.
- Шаблон **`template-speech-situation-metadata.md`** + pilot tags на playbooks.
- Router row + `router-rhetoric-pragmatics` в supplement.

## Что не делать сейчас

- Массовый перенос `evidence-humanities-shelf` (логика, utility, Covey) — **остаются**; bridge в `matrix-rhetoric-pragmatics-bridge.md`.
- Перенос всех `domains/agent-operations` playbooks в worlds.
- Новая папка `routers/` без ADR и MCP migration.
- «Перетегировать 500 файлов» — только event-driven + pilot map.

## Slice 2 (следующий)

1. Grice + Vatz evidence (Tier 1 map).
2. XL scenario `register-self-report-vs-disclaimer` из wetware report.
3. +5 playbooks в `map-speech-situation-tagged-cards-v0`.
4. Практический канон ораторского искусства (учебник/справочник ситуаций×форм — **не** фиксированная книга; лучший доступный источник + `source_refs`).

## Slice 3 (когда упрётся)

- **Split humanities shelf?** Только если shelf перестаёт быть navigable — риторика/аргументация уже в rhetoric-pragmatics; логика может остаться или получить `worlds/logic-argumentation/` при отдельном fundamental pass.
- **Router Domain Entry Map** — не раздувать строки; детали в hub README + status closure snapshot (как PHP cluster).

## Критерий «пора ли ещё»

- Агент **RTFM** speech_situation перед внешним текстом (checklist в playbook rhetoric).
- XL пилот: register-only pairs улучшают `situation_purity` vs baseline.
- Fundamental pass: ≥5 evidence-карт с provenance.

## Ссылки

- Hub: [`worlds/rhetoric-pragmatics/README.md`](../worlds/rhetoric-pragmatics/README.md)
- Taxonomy: [`META/kb-taxonomy.md`](../META/kb-taxonomy.md)

