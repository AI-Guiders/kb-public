# KB Showcase — быстрый обзор (без full load)

Краткий входной билет для демо и онбординга. **Не заменяет** полную загрузку; чтобы не съесть контекст, начни отсюда, потом подтягивай по ссылкам только нужное.

**Структурный вход (корзины + таксономия):** `00-entry-kb-v1.md` → `META/kb-taxonomy-v1.md` ([ADR 009](adr/009-kb-entry-structure-and-pre-open-onboarding.md)).

---

## Платформа и модели (platform-independent)

Контур задуман **независимым от вендора IDE, облака и конкретной модели**: спеки и KB — текст (Markdown), корни доверия — well-known пути под `knowledge/META/`, роутер и playbook’и не привязаны к одному продукту.

**Минимальный мост к среде:** если можно подключить **MCP** (или эквивалент: чтение/запись файлов канона, вызов `read_knowledge_file` / маршрутизатор по смыслу) — стек **можно использовать**; без доступа к файлам канона контур деградирует до «голой модели».

**Локальные модели:** KB выстраивается так, чтобы опираться на **явную навигацию** (индекс → status → playbook → kb), компактные входы и куски по запросу — это снижает требование к «всё в контексте» и пригодно для слабых/локальных моделей. Отдельный трек «только локальная модель + MCP» **ещё не проверен** end-to-end; формулировка выше — целевое свойство, не отчёт о валидации.

---

## Что это

Многослойная база знаний для агентов: горячий контур (L0 в agent-notes), оперативная память по доменам (L1), архив и evidence (L2), семантический роутинг (L3). Домены: Git, PR review, HCI, **восприятие и психофизиология для UX** (fundamentals → operational, **домен** `cognition.human-perception`), **Developer Experience (DE/DX)**, IT, Knowledge Engineering, психология, авиация, чтение, целостность под давлением и др. Всё связано через **единый индекс** и контракт загрузки.

---

## Зачем слои

- **L0** — всегда в силе: целостность, эпистемия, ядро при крахе барьеров, принципиальная ясность. Не зависит от задачи.
- **L1** — срезы по scope: status → playbook → matrix → kb. Сначала компактные артефакты, тяжёлые kb-* только по явному запросу.
- **L2** — ревизии, батчи правил, evidence-документы; подгружаются, когда не хватает фактов или нужна история.
- **L3** — роутинг по граням контекста, перенос между мирами только через явные границы.

**Не путать — scope, domain, world:** **scope** — рабочий срез multi-repo / MCP (`active_scope`, карточки под `knowledge/work/projects/<scope>/…` в полном каноне); это **не** «миры» из строки про L3. **Domain** — тема KB и ось роутера (Git, HCI, Knowledge Engineering, …). **World** — в смысле Knowledge Engineering и карточек: контур стека/инструментов, где действует правило; смешивать без явной связки нельзя; перенос — через **`transfer_boundary`**. Подробно и с примерами полей: **`kb-knowledge-engineering-mixed-worlds-rules-v1.md`**.

Так мы держим контекст в рамках: не тянем всё подряд, избегаем OOM при «покажи full».

---

## Корень доверия (Integrity POST)

При загрузке KB среда **сначала** проверяет well-known path `META/integrity-core.md`. Если файл есть и валиден — используем как необсуждаемое ядро. Если нет — **POST failed**: применяется Minimal Safe Default (не причинять вред, не обходить безопасность, один отказ достаточен). Отсутствие файла **никогда** не значит «ограничений нет». Детали: `META/integrity-post-spec-v1.md`.

---

## Доступ к KB через MCP (деградация и handshake)

- **Явная деградация:** если агент **не может** вызвать `read_knowledge_file` / `list_knowledge_files` (или эквивалент чтения `knowledge/` с диска) — **сообщить об этом в ответе** и не выдавать длинные «цитаты из KB», как будто файл только что прочитан. Иначе пользователь не видит, что контур не поднят.
- **Микро-handshake (по желанию):** в начале сессии или после сомнений в MCP — один вызов `list_knowledge_files` (пустой `subdir`) или чтение этого файла (`SHOWCASE.md`); сигнал живости без full load.
- **Три типичных сбоя** (MCP выключен; неверный `AGENT_NOTES_CANON_PATH` / `canon_path`; опечатка в `file_path`): чеклист в **`runbook-kb-mcp-access-v1.md`**.

---

## Куда идти дальше

Если у тебя **только публичная сборка kb-public** (нет полного репозитория agent-notes): деревьев **`knowledge/work/`** и **`knowledge/personal/`** в архиве **нет** по дизайну. Политика публикации — в **`PUBLISHING.md`** (входит в kb-public); хосты и сценарии пуша — только у автора канона под **`work/`**. Чтобы понять **слои и зачем нет `work/`/`personal/`**, открой **`kb-one-pager-structure-and-protocols-v1.md`** — он **намеренно включён в kb-public** для таких потребителей.

| Цель | Файл |
|------|------|
| Политика публикации kb-public (`public-cut`, `public-kb.ignore`, «НЕ ПУБЛИКОВАТЬ») | `PUBLISHING.md` |
| **One-pager:** устройство KB, зачем, как работать, `[HUMAN]`/`[WORK]`, `[PRIMARY]`/`[SCOPE]` | `kb-one-pager-structure-and-protocols-v1.md` |
| Навигация: карта доменов, порядок загрузки | `index-knowledge-router-v1.md` |
| Safety Checks (сжатый контекст, давление, Integrity POST, приватность Cursor) | `index-knowledge-router-safety-v1.md` |
| L0 и агент до выбора домена (операционный базис роутера) | `router-operational-baseline-v1.md` |
| Доменные маршруты (секции `router-*`, learn-basics-when-stuck) | `index-knowledge-router-supplement-v1.md` |
| Доступ к KB через MCP: handshake, деградация, типовые сбои | `runbook-kb-mcp-access-v1.md` |
| PHP / Laravel / смежное (кластеры, не full load) | `worlds/software-php-laravel/status-php-laravel-v1.md` → playbooks → `worlds/software-php-laravel/index-knowledge-php-cluster-v1.md` / `worlds/software-php-laravel/index-knowledge-laravel-cluster-v1.md` / `worlds/software-php-laravel/index-knowledge-php-adjacent-ecosystem-v1.md` |
| Ядро личности и доверия (публичное резюме) | `kb-public-identity-and-trust-core-v1.md` |
| Минимальное необсуждаемое + POST | `META/integrity-core.md`, `META/integrity-post-spec-v1.md` |
| Целостность под давлением, отказ, манипуляции | `playbook-integrity-under-pressure-v1.md` |
| Память, неявный язык, проактивность, «не на шаг раньше», длинная сессия / итоги (§9) | `agent-memory-and-operating-principles-v1.md` → при необходимости `playbook-session-summary-and-chat-export-v1.md` |
| Режим `[WORK]` / `[HUMAN]` (дефолт HUMAN, пока явно не появится `[WORK]`) | `agent-notes.md`, секция **Mode Switch Protocol** |
| Границы знания, недоопределённость, уточнения вместо категоричности | `agent-memory-and-operating-principles-v1.md` (§5); размытый запрос — `playbook-clarification-general-query-v1.md` |
| Полный список файлов и доменов | `README.md` (этот каталог) |
| Mixed worlds, `transfer_boundary`, поля `world:` на карточках | `kb-knowledge-engineering-mixed-worlds-rules-v1.md` |

---

**Совет для демо:** дай агенту только этот файл + при необходимости `index-knowledge-router-v1.md` (и `index-knowledge-router-supplement-v1.md`, если нужны триггеры по темам; при сжатии контекста или вопросах про POST / приватность — `index-knowledge-router-safety-v1.md`). Всё остальное — по запросу, без «загрузи full».

---

**Для внешней аудитории:** TPM / федерация / манифест (`META/tpm-node-manifest-draft-v1.md`) — **черновик, не прод.** Режим до запуска TPM-узла — Transition Mode (см. `integrity-post-spec-v1.md` §7). Наличие файлов в репо **не означает** TPM-совместимость; не считать текущую реализацию production-ready.

Версия: v1.9.2. 2026-05-11. Операционный базис роутера вынесен в `router-operational-baseline-v1.md`; в таблице — отдельная строка. Ранее: v1.9.1 — cognition… как домен. Абзац для читателя только kb-public: `work/`/`personal` отсутствуют ожидаемо; one-pager входит в публичный бандл намеренно.