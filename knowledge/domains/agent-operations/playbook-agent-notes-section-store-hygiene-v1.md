**Tags:** #agent-operations #domains #living #playbook

﻿# Playbook — agent-notes / TaskKnowledge section-store hygiene

**Status:** Active (P0+P1 shipped in AgentNotes.Core 2.1.4–2.1.5 / MCP 2.1.3–2.1.4)  
**Date:** 2026-07-17  
**Контур:** agent-operations · agent-notes MCP + TaskKnowledge markdown cards  
**Связь:** `compact_hot_context` (hot notes); TK `upsert_section`; `validate_sections` / `normalize_sections`; checkpoint ADR 0001 (PD = md sections)

## Проблема (AS IS агента)

1. Сломанные/дубли `<!-- section:id -->` → upsert мимо или раздувает файл.
2. «Почти секция» одними `##` без маркеров → приходится `write` целиком.
3. Длинный narrative без структуры → промах при compact / dig-out.

## Решение (направление)

Гигиена **section-store**, не Hoare-парсер и не второй формат KB.

### P0 — на записи

| Норма | Поведение MCP |
|-------|----------------|
| **upsert strict** | Дубли id / unclosed / orphan close → **reject** + диагностика, не silent append |
| **validate_sections(path)** | Список id, дубли, broken pairs (preview tool) |

### P1 — repair

| Норма | Поведение |
|-------|-----------|
| **normalize_sections(path)** | Как `compact_hot_context`: схлопнуть дубли (keep last), починить пары; preview/apply |
| **allowlist** (optional) | Template объявляет допустимые `section_id`; чужие → warning |

### P2 — миграция и чтение

| Норма | Поведение |
|-------|-----------|
| **ensure_sections_from_headings** | `## Foo` → `<!-- section:foo -->` по правилам шаблона (one-shot migrate) |
| **outline read** | mode=outline: toc section ids + первые N строк / обязательный `meta`/`summary` |
| **бюджет секции** | soft limit; overflow → scratch + ссылка |

### Не делать

- Не заменять section markers YAML/TOML «везде» ради гигиены.
- Не валить семантику PD (pre/post/next) в agent-notes — контракт шага читает **TaskKnowledge.Core** / consumer; KB держит текст + маркеры.
- Не hard-fail на каждом старом файле без normalize path.

## Порядок внедрения

1. Reject на битых секциях при upsert (knowledge + agent-notes hot + TK cards).  
2. `validate_sections` + `normalize_sections`.  
3. Outline read / section budget.  
4. ensure-from-headings — по факту миграций.

## Criterion

- Агент не раздувает файл повторным upsert при дубле id.  
- `validate_sections` ловит broken до правки.  
- Длинный KB-файл читается outline без полного dump по умолчанию (когда tool появится).

## Tasks (черновик ids)

- `an-section-upsert-strict`  
- `an-section-validate-normalize`  
- `an-knowledge-outline-read`  
- `tk-section-parity` (те же инварианты в TaskKnowledge MCP)
