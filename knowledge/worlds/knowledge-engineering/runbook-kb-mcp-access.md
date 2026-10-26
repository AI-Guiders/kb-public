---
type: Runbook
title: 'Runbook: доступ к KB через MCP (handshake, деградация, сбои)'
description: '**Назначение:** согласовать поведение агента, когда канон живёт в репозитории **agent-notes** и доступен через **agent-notes MCP** (`read_knowledge_file`, `list_knowledge_files`, запись — отдельные инструменты). Среда-независимо: тот же смысл, если чтение идёт с диска по well-known пути без MCP.'
tags: [knowledge-engineering, runbook, worlds]
language: ru
world: knowledge
subworld: engineering
sections: [hot-vs-full-agent-notes-read-v1]
---
# Runbook: доступ к KB через MCP (handshake, деградация, сбои)


**Назначение:** согласовать поведение агента, когда канон живёт в репозитории **agent-notes** и доступен через **agent-notes MCP** (`read_knowledge_file`, `list_knowledge_files`, запись — отдельные инструменты). Среда-независимо: тот же смысл, если чтение идёт с диска по well-known пути без MCP.

**Связь:** `SHOWCASE.md` § «Доступ к KB»; hub [`agent-memory-and-operating-principles.md`](../../agent-memory-and-operating-principles.md); §6–7 ниже; `playbook-multi-project-context.md` §6 (PRIMARY).

---

## 1. Явная деградация (контур чтения недоступен)

Если агент **не может** вызвать `read_knowledge_file` / `list_knowledge_files` (или эквивалент чтения файлов из `knowledge/`) — в ответе **коротко указать**, что контур чтения канона сейчас недоступен, и **не** выдавать длинные «цитаты из KB» или точные формулировки как будто файл только что прочитан.

Краткая самопроверка уместна: «могу ли я сейчас подтвердить путь из канона вызовом?» — если нет, одна честная фраза лучше ложного доверия. Объём — **одно предложение**, без морализаторства (практика в духе уже принятого поведения при «молчащем» MCP / после Reload — см. обсуждения в сессиях).

---

## 2. Микро-handshake (опционально)

**Зачем:** сигнал живости контура за мало токенов; пользователю видно, что KB не «в уме модели», а на проводе.

**Как (любой один шаг):**
- `list_knowledge_files` с пустым `subdir`; или
- `read_knowledge_file` с `file_path: "SHOWCASE.md"`.

Не превращать в обязательный тяжёлый ритуал на каждое сообщение — только по смыслу (новая сессия, сомнение в MCP, после Reload Window).

---

## 3. Три типичных сбоя (чеклист)

Таблица симптомов (канон): [`troubleshooting/playbook-knowledge-engineering-mcp-troubleshooting.md`](troubleshooting/playbook-knowledge-engineering-mcp-troubleshooting.md).

---

## 4. PRIMARY и канон

Маркер **`[PRIMARY:…]`** задаёт приоритет **карточки проекта** и путей из неё; он **не** заменяет проверку доступности MCP. Если PRIMARY — `agent-notes-kb`, а MCP молчит — сначала честно про деградацию (§1), потом действия.

---

## 5. Полный отказ MCP, «ключи в машине» и человек в контуре

**Парадокс загрузки:** этот runbook лежит в `knowledge/`; если **чтение канона через MCP недоступно полностью**, агент **не прочитает** и этот файл тем же контуром — инструкция «открой runbook» бессильна (аналог «ключи оставили в салоне»).

**Типичный реальный случай:** человек **не просит** править заметки/KB, пока не поднят MCP (или пока не работают с локальным клоном репо без агента). Тогда сценарий не раздувается.

**Где текст всё же полезен агенту:** частичные сбои (неверный `canon_path`, один файл не открывается, «сервер в UI» vs «нет тулов в чате»), новая сессия, сомнение в живости контура — без обвинения пользователя.

**Выход без размножения правил в конкретной IDE:** локальный клон **agent-notes**, открытие файла в редакторе, сообщение человека в чате, задачи вне канона. Канон задуман **vendor-aware** (см. `SHOWCASE.md`); не обязательно дублировать длинные блоки в настройках Cursor — достаточно внешнего якоря (клон, путь, починка MCP).

---

## 6. Запись в knowledge/ — CDP Memory (primary)

При изменении **`knowledge/`** канона — **CDP** `write_knowledge_file` / `upsert_knowledge_section` (facet Memory); escape: agent-notes MCP или явное согласование с оператором.

| Действие | Инструмент |
|----------|------------|
| Чтение | `read_knowledge_file` |
| Полная замена | `write_knowledge_file` |
| Конец файла | `append_knowledge_file` |
| Секция по `section_id` | `upsert_knowledge_section`, `delete_knowledge_section` |
| Удалить файл | `delete_knowledge_file` |
| Список | `list_knowledge_files` |

Канон: **`AGENT_NOTES_CANON_PATH`**. Provenance: [`META/provenance-contract.md`](../../META/provenance-contract.md), [`templates/template-knowledge-card.md`](../../templates/template-knowledge-card.md).

## 7. Чтение при недоступности MCP

Если **чтение** недоступно — не цитировать KB из памяти как факт; одна фраза про недоступность контура. Когда MCP/CDP снова доступен — §6 в силе. Подробнее §1–5 выше.

## 8. Имена и история — git, не inline

**Anti-pattern (не добавлять):**
- блоки `## Версия` / `**Версия:**` / changelog `v1.1 · дата · …` в теле файла;
- суффиксы `-v1`, `-v2` в **именах** файлов KB.

**SSOT истории** — git log. **Stable id** — путь + slug (`playbook-agent-pause-ground-continue.md`), не дублирующий номер версии. `section_id` в hot (`execution-gate-v1`) — отдельный контракт, не переименовывать при чистке файлов.

<!-- section:hot-vs-full-agent-notes-read-v1 -->
## Чтение hot vs каталог agent-notes.md

| Нужно | Инструмент |
|-------|------------|
| Always-on slice по scope | **`read_hot_context`** |
| Подобрать секции по запросу | **`route_context`** |
| Тело правила / playbook | **`read_knowledge_file`** (сначала `outline`, потом фрагмент) |
| Список файлов канона | **`list_knowledge_files`** |
| **Не** для контекста | **`read_agent_notes`** — отдаёт **весь** файл-секционник (~70k символов); только если человек явно просит просмотреть/diff hot-файл целиком |

CDP Memory facet — те же смыслы (`memory_world_read_knowledge_file`, recall). §6 — запись.

<!-- /section:hot-vs-full-agent-notes-read-v1 -->

