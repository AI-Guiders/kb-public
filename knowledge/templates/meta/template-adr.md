---
type: Template
title: 'ADR NNN: <Title>'
description: '```yaml'
tags: [template, templates, adr]
subtype: ADR
---

# ADR NNN: <Title>

## Frontmatter (заполнить при создании; шапочная конвенция в теле не дублируется)

```yaml
---
type: ADR
title: '<краткий заголовок>'
description: '<одно предложение: что решено>'
status: stable        # stable = Accepted · draft = Proposed · deprecated = Superseded/Rejected
tags: [adr, <домен>]
supersedes: []        # concept-id предшественников, если есть
---
```

## Связано (буллеты с аннотацией связи — тип ребра прозой, читаемо)

- [NNN](NNN-slug.md) — <чем связан: конституционная совместимость / наследие / альтернатива>
- [playbook](../path/to/playbook.md) — операционная часть решения

## Context

(Проблема и силы, которые давят на решение.)

## Decision

(Что решили — однозначно.)

## Consequences

### Positive

- …

### Negative / trade-offs

- …

## Alternatives considered

| Вариант | Почему не выбран |
|---------|------------------|
| … | … |

## Notes

- **KB-own ADR**: живут в `knowledge/adr/`, concepts канон-бандла, контур непубличный; `Статус`/`Дата`/`Supersedes` поднимаются во frontmatter (по касанию).
- **Продуктовые ADR**: SSOT — репо продукта (свой OKF-бандл), в KB не копируются; KB-граф индексирует как `Adr`-узлы.
- One ADR — одно решение; мотивация из чатов — в `operator-notes/`/project note со ссылкой из ADR.

