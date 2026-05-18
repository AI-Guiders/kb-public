# Hot section (template)

Вставка в **`agent-notes.md`** (personal primary) между маркерами:

```markdown
<!-- section:<section_id> -->
…содержимое…
<!-- /section:<section_id> -->
```

**section_id:** `A-Za-z0-9._-` (напр. `active-scope`, `knowledge-roots-routing-v1`, `door-to-singularity`).

## Правила

- **Коротко:** L0/L1 — только то, что нужно каждую сессию; детали в `knowledge/`.
- **Без секретов** в org/public hot.
- Обновление: `upsert_agent_notes_section` (MCP), не полная перезапись файла без нужды.
- После смены scope/roots — `memory_health` / `route_context`.

## Содержимое (пример структуры)

- Текущий scope / project-id
- 3–7 буллетов: пути, ADR, «не смешивать с …»
- Ссылка на `work/projects/…/README.md` или status мира

## Newcomer-набор

Готовые секции для чистой установки: [`../newcomer/`](../newcomer/) + `playbook-knowledge-stack-clean-setup-v1.md`.