---
type: Note
title: CDP-first кодовая работа (v1)
description: '**Обоснование:** двойной писатель (IDE и агент вслепую) — главный источник порчи; CDP-план делает IDE участником правки, а не свидетелем.'
tags: [cdp, zcode, code-work, agent-operations]
language: ru
world: agent
subworld: operations
---

# CDP-first кодовая работа (v1)

- Кодовая работа в среде с CDP: `cdp_open` решения → `cdp_buffer` (create/edit) → diagnostics → `cdp_test` / `cdp_build`. Петля короткая: ошибка умирает на следующем шаге, не тремя ходами позже.
- Сырые Write/Edit/Bash — escape hatch **с протоколом**: закрыть CDP-буфер по файлу → raw-write → reload → verify. Не смешивать пути на файле с живым dirty-буфером.
- Диагностики: дефолт syntax; после содержательных правок запрашивать `scope=project` (полный Roslyn) — см. [ZCode harness quirks §3](note-zcode-harness-quirks.md).
- Свойства, проверенные практикой (OKF-миграция M1–M2, ветка `feature/okf-migration` guiders-core): drift-защита (`disk_changed`/mtime/version), undo на буфер, evidence-диагностики с якорями `[F:…;L:…]` прямо в ответе теста.
- Фоновые джобы CDP в ZCode не доставляются — [quirks §4](note-zcode-harness-quirks.md); фоновый Bash харнесса уведомляет штатно.

**Обоснование:** двойной писатель (IDE и агент вслепую) — главный источник порчи; CDP-план делает IDE участником правки, а не свидетелем.

**Status:** principle validated 2026-10-23/24; проверить при апдейтах CDP/ZCode.

