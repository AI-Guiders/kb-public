# Response finalizer — развёрнуто
**Tags:** #workspace-context #worlds


**Назначение:** детали финализации ответа и вычитки. L0: секция `response-finalizer-v1` в `agent-notes.md`.

## Чеклист перед ответом

- Факт подтверждён инструментом.
- Неопределённость — явно + безопасный следующий шаг.
- Проход `response-one-step-before-finish-v1` — «ещё на шаг не дожал?»; при «завершён?» — [`response-one-step-checklist-extended.md`](response-one-step-checklist-extended.md).

## Вычитка вторым проходом (отдельно от «не на шаг раньше»)

**«Не дожал шаг»** — полнота действия и замыкание задачи ([`response-one-step-checklist-extended.md`](response-one-step-checklist-extended.md)).

**Вычитка** — второй проход по **готовому тексту** глазами читателя: опечатки, «слова-призраки», пути, идентификаторы, единообразие терминов.

**Когда:** канон (`knowledge/`, `agent-notes.md`), сообщения коммита, пользовательский текст для репо или долгоживущего артефакта.

**Как:** смысл и шаги готовы → короткий проход **без** нового содержания; сомнительное слово — проверить; пути — сверить с деревом.

**Hub:** [`agent-memory-and-operating-principles.md`](../../agent-memory-and-operating-principles.md) → эта секция.

