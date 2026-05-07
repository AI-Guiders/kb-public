# ADR in KB

Этот каталог хранит архитектурные решения для самого KB и его операционного контура.

## Scope

- Что относится к устройству KB (структура, маршрутизация, дистрибуция, уровни).
- Как KB взаимодействует с потребителями (например, CIDE).
- Правила эволюции канона (форматы, governance, совместимость).

## Naming

- Формат файла: `NNN-short-title.md`
- `NNN` — 3-значный номер (`001`, `002`, ...)
- `short-title` — краткий slug в kebab-case

## Minimal template

- `# ADR NNN: Title`
- `Статус` / `Дата`
- `Supersedes` / `Extended by` (по возможности)
- `Контекст`
- `Решение`
- `Последствия`
- `План внедрения` (если нужен)

## Notes

- ADR здесь не заменяют `status-*` и `playbook-*`; они фиксируют архитектурные развилки.
- Для ссылок из роутера можно использовать краткую отсылку в `index-knowledge-router-v1.md` при необходимости.

## Timeline (restored from commit history)

- `001-kb-public-publishing-pipeline.md`
- `002-integrity-post-and-epistemic-baseline.md`
- `003-multi-project-scope-and-project-cards.md`
- `004-router-supplement-and-l1-pool.md`
- `005-kb-base-cide-bundle.md`
- `006-zettelkasten-overlay-for-kb.md`
- `007-kb-project-constitution.md`
