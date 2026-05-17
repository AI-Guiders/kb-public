# Playbook: свежесть знаний в каноне (agent entry) — v1

**Назначение:** **одна точка входа для агента**, когда задача про **устаревание или перепроверку любого знания** в `knowledge/` — не только .NET: гуманитарные карточки, психология, HCI, продуктовые runbook’и, evidence, слои **fundamentals → operational**, поля `Проверено:` / provenance, `deprecated` / `supersedes`, «куда записать обновление». Не заменяет доменные playbook’и — **сужает** выбор файлов и порядок действий.

**Среда-независимость:** текст в `knowledge/`; чтение через MCP `read_knowledge_file` или локальный клон.

**Связь:**
- `templates/template-knowledge-card-v1.md` (Provenance, Core Unit, Operationalization, Lifecycle)
- `META/provenance-contract-v1.md`
- Layer contract (пример): `worlds/evidence-humanities-shelf/kb-covey-7-habits-evidence-v1.md` § Layer contract
- `playbook-knowledge-engineering-core-v1.md` (§ Deprecation, Operating rhythm, quality gates)
- `index-knowledge-router-supplement-v1.md` → `router-kb-operational-freshness`
- `playbook-learn-basics-when-stuck-v1.md` — если неясна **семантика** предмета, сначала матчасть, потом правка kb
- `runbook-kb-mcp-access-v1.md` — если **не читается** канон
- Карта трёх контуров (агент-диспетчер, без PWA): `domains/agent-operations/map-kb-three-contours-v1.md`
- Идея UI для людей (не обязательна агенту): `work/projects/door-to-singularity/kb-management-center/README.md`

**Версия:** v1.2 · 2026-05-16 — явная связь с **Maintenance Policy** доменов и **Maintenance Rule** роутера (разные сущности). v1.1 — слои fundamentals/operational.

**Не путать с Maintenance Rule роутера:** `index-knowledge-router-maintenance-v1.md` § Maintenance Rule — только **сопровождение индекса** (supplement, Domain Entry Map, `router-*`, kb-public). **Свежесть знаний** — этот playbook + **`status-*` § Maintenance Policy / Next review triggers** по домену.

---

## 1. Когда открывать этот playbook (триггеры)

- «Устарело», «просрочено», «давно не проверяли», «актуально ли», «перепроверить kb»
- **`Проверено:`**, `updated_at`, `source_refs`, `deprecated`, `supersedes`, `status: draft`
- Смена **источника правды** (издание книги, новая спецификация, релиз платформы, bump пакета, смена политики в `status-*` § Next review triggers)
- «Какой файл править», «куда записать факт», «операционка vs фундаментал»
- Сомнение: kb **противоречит** первоисточнику, репо или более свежему `playbook-*` / `status-*`

**Не открывать** для первичной навигации по домену без вопроса свежести — сначала `index-knowledge-router-v1.md` (Domain Entry Map).

---

## 2. Слои знания и где уже зафиксированы сроки

Перед выбором файлов из §5 определить **слой** целевого знания. Один домен (JS, психология, CIDE) может иметь **оба** слоя в разных файлах.

### 2.1 Слои (навигация, не дублировать доменные playbook)

| Слой | Что хранит | Маркеры в каноне |
|------|------------|------------------|
| **Fundamentals** | Определения, модели, «как устроено» | Секции **Fundamentals**; `kb-*-fundamentals-v1.md`; Core Unit в карточке |
| **Operational** | Процедуры, версии, «что делаем сейчас» | `playbook-*-operational-v1.md`; **Operationalization**; `operational.md` в `work/projects/…` |
| **Evidence / snapshot** | Факт + URL/строка; снимок версий | `EV-*`, **`Проверено:`**; таблицы пакетов в project kb |

**Контракт слоёв:** `templates/template-knowledge-card-v1.md`; пример **Layer contract** — `kb-covey-7-habits-evidence-v1.md`. Полный fundamentals + operational по смыслу — `agent-memory-and-operating-principles-v1.md` §0.

**Порядок загрузки в домене:** `status-*` → operational playbook → fundamentals kb → evidence (см. Retrieval hint в том же `status-*`).

### 2.2 Где в каноне уже лежат правила перепроверки (источник правды)

| Уровень | Файл | Что там |
|---------|------|---------|
| **Роутер (редакторы)** | `index-knowledge-router-maintenance-v1.md` § **Maintenance Rule** | Сплит supplement, Domain Entry Map, список `router-*` — **не** сроки свежести kb |
| **Домен** | `status-<domain>-v1.md` | **`Maintenance Policy`**, **`Next review triggers`** — событийные и плановые триггеры **этого** мира (PHP, JS, psychology, aviation, git, KE, …) |
| **Meta KE** | `playbook-knowledge-engineering-core-v1.md` § **Operating Rhythm** | micro / weekly / biweekly / monthly для карточек и deprecation |
| **Meta KE** | `status-knowledge-engineering-v1.md` § **Maintenance Policy** | refresh cadence meta-домена |
| **Governance** | `kb-knowledge-engineering-operations-rules-v1.md` (напр. KC-177) | домен без maintenance policy → silent decay; нужны refresh triggers |

**Порядок для агента:** сначала **`status-*` целевого домена** (если есть Maintenance Policy / Next review triggers) — **они сильнее** общих эвристик ниже. Этот playbook только **сводит слои и маршрут**; новые глобальные TTL сюда **не изобретать**.

### 2.3 Если в домене нет явной политики

- Спросить держателя канона или зафиксировать **в `status-*`** при закрытии домена (см. KC-177).
- Временная эвристика только до появления политики: fundamentals — реже (событие + долгий цикл); operational/evidence — при расхождении с источником и по событиям релиза/bump.

**Приоритет при конфликте:** `status-*` / доменный `playbook-*` сильнее устаревшего `kb-*`; эпистемика L0 — не усиливать непроверённое.

---

## 3. Быстрый порядок (≤ 60 с)

| Шаг | Действие |
|-----|----------|
| 1 | Определить **слой** (§2): fundamentals / operational / evidence |
| 2 | Классифицировать **тип задачи** (§4): домен / стек / возраст / lifecycle / слои канона |
| 3 | Открыть **только** строки реестра §5 для типа (+ `project-id` из `[PRIMARY:…]` для `work/projects/…`) |
| 4 | Сверить с **источником правды** (книга/спека, официальная дока, репо, `composer.lock` / `csproj` — по смыслу слоя) |
| 5 | Правка: факт + **provenance**; для evidence — **`Проверено: YYYY-MM-DD`**; для карточек — `updated_at`, при необходимости lifecycle |
| 6 | Если знание неверно и не чинится точечно → `deprecated`, `superseded_by` (`playbook-knowledge-engineering-core-v1.md`) |

---

## 4. Типы задач

| Тип | Примеры запроса | Куда смотреть в §5 |
|-----|-----------------|-------------------|
| **0. Слой / плановая перепроверка** | «просрочен fundamentals», «когда проверять operational», обход `Проверено:` | `knowledge-layers` + целевой домен (`domain-entry`) |
| **A. Домен (без привязки к .NET)** | устарел kb по психологии, HCI, авиации, книге | `domain-entry` → status → playbook домена |
| **B. Платформа / рантайм** | новый .NET, TFM, PHP 8.x, ECMA edition | `dotnet-platform`, `php-laravel`, `javascript-cluster`, … |
| **C. UI / продукт / пакеты** | Avalonia bump, таблица NuGet vs `csproj` | `avalonia-cide`, `project-card-evidence` |
| **D. Возраст / provenance** | старый `updated_at`, битые URL, нет `source_refs` | `provenance-meta` + файл |
| **E. Слои канона (personal/org/public)** | куда писать, kb-public | `layers-publishing` |
| **F. MCP** | не читается kb | `mcp-access` |

Тип **0** выполнять **перед** A–F, если вопрос именно про «какой слой и какой горизонт перепроверки».

---

## 5. Реестр: «что отслеживать → какие файлы открыть»

Загружать **по одному–два kb + один playbook** за раз, не весь список.

### `knowledge-layers`

| Триггер | Файлы (порядок) |
|---------|------------------|
| Неясно fundamentals vs operational | §2 этого playbook → `templates/template-knowledge-card-v1.md` → пример Layer contract: `kb-covey-7-habits-evidence-v1.md` |
| Ритм / политика перепроверки (канон) | `status-<domain>-v1.md` § Maintenance Policy / Next review triggers → при meta KE: `playbook-knowledge-engineering-core-v1.md` § Operating Rhythm · `status-knowledge-engineering-v1.md` § Maintenance Policy · KC-177 в `kb-knowledge-engineering-operations-rules-v1.md` |
| **Не** сроки свежести kb | `index-knowledge-router-maintenance-v1.md` § Maintenance Rule — только индекс роутера |
| Provenance на любой существенной правке | `META/provenance-contract-v1.md` |

### `domain-entry`

| Триггер | Файлы (порядок) |
|---------|------------------|
| Любой **не-.NET** домен или «устарело в мире X» | `index-knowledge-router-v1.md` — строка Domain Entry Map → **`status-<domain>-v1.md`** → доменный **`playbook-*`** → **один** целевой `kb-*` (fundamentals и/или operational по §2, не все сразу) |
| Fundamentals → operational в домене | supplement § `router-<domain>` (напр. `router-human-perception`, `router-javascript`) |
| Плановая перепроверка домена | `status-*` § **Next review triggers** / **Maintenance policy** — событийные триггеры важнее календаря |

### `dotnet-platform`

| Триггер | Файлы (порядок) |
|---------|------------------|
| .NET / TFM / SDK / миграция | supplement § `router-dotnet` → `worlds/software-dotnet-csharp/kb-dotnet-fundamentals-v1.md` → при миграции `kb-dotnet-playbooks-v1.md` → при инженерных фактах `worlds/software-engineering-evidence/kb-engineering-evidence-v1.md` |
| C# / Roslyn / диагностики | `worlds/software-dotnet-tooling-roslyn/playbook-csharp-roslyn-mcp-diagnostics-v1.md` |
| CIDE: runtime vs Learn | `work/projects/door-to-singularity/cascade-ide/kb-dotnet-runtime-reference-stance-v1.md` |

### `php-laravel` / `javascript-cluster`

| Триггер | Файлы |
|---------|--------|
| PHP / Laravel / WP / Drupal | supplement § `router-php-laravel` → `status-php-laravel-v1.md` § Next review triggers → cluster index + один `kb-php-*` / `kb-laravel-*` |
| JavaScript / npm / CSP | supplement § router JS → `playbook-javascript-operational-v1.md` § fundamentals → operational |

### `avalonia-cide`

| Триггер | Файлы (порядок) |
|---------|------------------|
| Avalonia / Dock / CIDE UI | supplement § `router-avalonia-ui` → `status-avalonia-cascade-ide-ui-v1.md` → operational playbook → `kb-avalonia-ui-dock-fundamentals-v1.md` |
| Таблица пакетов vs факт | `work/projects/door-to-singularity/cascade-ide/kb-cide-evidence-card-spec-v1.md` + `CascadeIDE.csproj` |
| Мёртвые URL / VerifyAccess | `kb-avalonia-docs-vs-source-notes-v1.md` |

### `project-card-evidence`

| Триггер | Файлы (порядок) |
|---------|------------------|
| Любой **`project-id`** в `work/projects/…` | README карточки → локальные `kb-*` / `EV-*` / `operational.md` |
| После bump зависимостей | обновить снимок и **`Проверено:`** в spec/evidence; не дублировать в корень `knowledge/` без причины |

### `provenance-meta`

| Триггер | Файлы |
|---------|--------|
| Существенная правка факта | `META/provenance-contract-v1.md` + `templates/template-knowledge-card-v1.md` |
| Новая карточка | шаблон + `playbook-knowledge-engineering-core-v1.md` § Promotion quality gates |

### `layers-publishing`

| Триггер | Файлы |
|---------|--------|
| personal / org / public | `kb-one-pager-structure-and-protocols-v1.md` § слои; `PUBLISHING.md`; `playbook-multi-project-context-v1.md` §6c |

### `mcp-access`

| Триггер | Файлы |
|---------|--------|
| MCP не читает kb | `runbook-kb-mcp-access-v1.md` |

---

## 6. Чеклисты (коротко)

### Плановая перепроверка по слою

1. Открыть **`status-<domain>-v1.md`** — § Maintenance Policy / Next review triggers (§2.2).
2. Классифицировать файл: **fundamentals / operational / evidence** (§2.1).
3. **Fundamentals:** сверить с первоисточником; `falsification_trigger`; `updated_at` / `source_refs`.
4. **Operational:** события из status + текущий процесс/репо; обновить operational playbook при смене практики.
5. **Evidence:** **`Проверено:`**; при несовпадении с репо/докой — исправить evidence или правило продукта.

### После релиза платформы или bump пакетов (operational / evidence)

1. Событийный триггер из `status-*` или project spec.
2. Только релевантные строки §5 (`dotnet-platform`, `avalonia-cide`, …) — не весь supplement.
3. Источник правды: release notes / Learn / lockfile / `csproj`.
4. **`Проверено:`** + provenance в затронутых файлах.

### После правки гуманитарной / книжной карточки (fundamentals)

1. Сверка формулировок с изданием (`source_refs`, якоря страниц при наличии).
2. **Operationalization** в карточке — отражает ли текущую практику команды; если нет — обновить operational слой, не раздувать fundamentals.
3. `updated_at`; при смене смысла — `supersedes` / новая карточка.

---

## 7. Что писать пользователю

- **Слой** (fundamentals / operational / evidence) и **тип** задачи.
- **1–3 файла** (пути) и **источник правды**.
- Если менялся только полный канон / `work/` — явно сказать; kb-public требует сборки (`PUBLISHING.md`).

---

## 8. Антипаттерны

- Сводить свежесть kb **только к .NET** — сначала §2 и Domain Entry Map.
- Грузить **все** fundamentals домена при точечном operational вопросе.
- Обновлять kb **без** provenance / даты после смены факта.
- Путать **свежесть** с **первичным изучением** домена (`playbook-learn-basics-when-stuck-v1.md`).

---

## 9. Версия

v1.2 · 2026-05-16 — делегирование сроков в `status-*` Maintenance Policy / KE Operating Rhythm; отличие от router Maintenance Rule.  
v1.1 · 2026-05-16 — слои fundamentals/operational/evidence.  
v1.0 · 2026-05-16 — первая централизация agent UX (KBMC — отдельный PWA).
