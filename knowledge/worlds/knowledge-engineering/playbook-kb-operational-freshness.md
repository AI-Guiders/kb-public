# Playbook: свежесть знаний в каноне (agent entry)
**Tags:** #knowledge-engineering #living #playbook #worlds


**Назначение:** **одна точка входа для агента**, когда задача про **устаревание или перепроверку любого знания** в `knowledge/` — не только .NET: гуманитарные карточки, психология, HCI, продуктовые runbook’и, evidence, слои **fundamentals → operational**, поля `Проверено:` / provenance, `deprecated` / `supersedes`, «куда записать обновление». Не заменяет доменные playbook’и — **сужает** выбор файлов и порядок действий.

**Среда-независимость:** текст в `knowledge/`; чтение через MCP `read_knowledge_file` или локальный клон.

**Связь:**
- **CDP desk (MLP):** `cdp_freshness` / `go=freshness` — harness Digest for URL watchlist (map: `work/projects/door-to-singularity/cascade-ide/note-cdp-kb-freshness-mlp.md`). Digest ≠ `Проверено:`. Ops include `nrt` / `clear` / `arm` / `tick` (0.5.717+).

- `templates/template-knowledge-card.md` (Provenance, Core Unit, Operationalization, Lifecycle)
- `META/provenance-contract.md`
- Layer contract (пример): `worlds/evidence-humanities-shelf/kb-covey-7-habits-evidence.md` § Layer contract
- `playbook-knowledge-engineering-core.md` (§ Deprecation, Operating rhythm, quality gates)
- `index-knowledge-router-supplement.md` → `router-kb-operational-freshness`
- `playbook-learn-basics-when-stuck.md` — если неясна **семантика** предмета, сначала матчасть, потом правка kb
- `runbook-kb-mcp-access.md` — если **не читается** канон
- Карта трёх контуров (агент-диспетчер, без PWA): `domains/agent-operations/map-kb-three-contours.md`
- Идея UI для людей (не обязательна агенту): `work/projects/door-to-singularity/kb-management-center/README.md`


**Не путать с Maintenance Rule роутера:** `index-knowledge-router-maintenance.md` § Maintenance Rule — только **сопровождение индекса** (supplement, Domain Entry Map, `router-*`, kb-public). **Свежесть знаний** — этот playbook + **`status-*` § Maintenance Policy / Next review triggers** по домену.

---

## 1. Когда открывать этот playbook (триггеры)

- «Устарело», «просрочено», «давно не проверяли», «актуально ли», «перепроверить kb»
- **`Проверено:`**, `updated_at`, `source_refs`, `deprecated`, `supersedes`, `status: draft`
- Смена **источника правды** (издание книги, новая спецификация, релиз платформы, bump пакета, смена политики в `status-*` § Next review triggers)
- «Какой файл править», «куда записать факт», «операционка vs фундаментал»
- Сомнение: kb **противоречит** первоисточнику, репо или более свежему `playbook-*` / `status-*`

**Не открывать** для первичной навигации по домену без вопроса свежести — сначала `index-knowledge-router.md` (Domain Entry Map).

---

## 2. Слои знания и где уже зафиксированы сроки

Перед выбором файлов из §5 определить **слой** целевого знания. Один домен (JS, психология, CIDE) может иметь **оба** слоя в разных файлах.

### 2.1 Слои (навигация, не дублировать доменные playbook)

| Слой | Что хранит | Маркеры в каноне |
|------|------------|------------------|
| **Fundamentals** | Определения, модели, «как устроено» | Секции **Fundamentals**; `kb-*-fundamentals.md`; Core Unit в карточке |
| **Operational** | Процедуры, версии, «что делаем сейчас» | `playbook-*-operational.md`; **Operationalization**; `operational.md` в `work/projects/…` |
| **Evidence / snapshot** | Факт + URL/строка; снимок версий | `EV-*`, **`Проверено:`**; таблицы пакетов в project kb |

**Контракт слоёв:** `templates/template-knowledge-card.md`; пример **Layer contract** — `kb-covey-7-habits-evidence.md`. Ответственность агента за слои — [`playbook-agent-knowledge-responsibility.md`](../../domains/agent-operations/playbook-agent-knowledge-responsibility.md).

**Порядок загрузки в домене:** `status-*` → operational playbook → fundamentals kb → evidence (см. Retrieval hint в том же `status-*`).

### 2.2 Где в каноне уже лежат правила перепроверки (источник правды)

| Уровень | Файл | Что там |
|---------|------|---------|
| **Роутер (редакторы)** | `index-knowledge-router-maintenance.md` § **Maintenance Rule** | Сплит supplement, Domain Entry Map, список `router-*` — **не** сроки свежести kb |
| **Домен** | `status-<domain>.md` | **`Maintenance Policy`**, **`Next review triggers`** — событийные и плановые триггеры **этого** мира (PHP, JS, psychology, aviation, git, KE, …) |
| **Meta KE** | `playbook-knowledge-engineering-core.md` § **Operating Rhythm** | micro / weekly / biweekly / monthly для карточек и deprecation |
| **Meta KE** | `status-knowledge-engineering.md` § **Maintenance Policy** | refresh cadence meta-домена |
| **Governance** | `kb-knowledge-engineering-operations-rules.md` (напр. KC-177) | домен без maintenance policy → silent decay; нужны refresh triggers |

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
| 6 | Если знание неверно и не чинится точечно → `deprecated`, `superseded_by` (`playbook-knowledge-engineering-core.md`) |

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
| Неясно fundamentals vs operational | §2 этого playbook → `templates/template-knowledge-card.md` → пример Layer contract: `kb-covey-7-habits-evidence.md` |
| Ритм / политика перепроверки (канон) | `status-<domain>.md` § Maintenance Policy / Next review triggers → при meta KE: `playbook-knowledge-engineering-core.md` § Operating Rhythm · `status-knowledge-engineering.md` § Maintenance Policy · KC-177 в `kb-knowledge-engineering-operations-rules.md` |
| **Не** сроки свежести kb | `index-knowledge-router-maintenance.md` § Maintenance Rule — только индекс роутера |
| Provenance на любой существенной правке | `META/provenance-contract.md` |

### `domain-entry`

| Триггер | Файлы (порядок) |
|---------|------------------|
| Любой **не-.NET** домен или «устарело в мире X» | `index-knowledge-router.md` — строка Domain Entry Map → **`status-<domain>.md`** → доменный **`playbook-*`** → **один** целевой `kb-*` (fundamentals и/или operational по §2, не все сразу) |
| Fundamentals → operational в домене | supplement § `router-<domain>` (напр. `router-human-perception`, `router-javascript`) |
| Плановая перепроверка домена | `status-*` § **Next review triggers** / **Maintenance policy** — событийные триггеры важнее календаря |

### `dotnet-platform`

| Триггер | Файлы (порядок) |
|---------|------------------|
| .NET / TFM / SDK / миграция | supplement § `router-dotnet` → `worlds/software-dotnet-csharp/kb-dotnet-fundamentals.md` → при миграции `kb-dotnet-playbooks.md` → при инженерных фактах `worlds/software-engineering-evidence/kb-engineering-evidence.md` |
| C# / Roslyn / диагностики | `worlds/software-dotnet-tooling-roslyn/playbook-csharp-roslyn-mcp-diagnostics.md` |
| CIDE: runtime vs Learn | `work/projects/door-to-singularity/cascade-ide/kb-dotnet-runtime-reference-stance.md` |

### `php-laravel` / `javascript-cluster`

| Триггер | Файлы |
|---------|--------|
| PHP / Laravel / WP / Drupal | supplement § `router-php-laravel` → `status-php-laravel.md` § Next review triggers → cluster index + один `kb-php-*` / `kb-laravel-*` |
| JavaScript / npm / CSP | supplement § router JS → `playbook-javascript-operational.md` § fundamentals → operational |

### `avalonia-cide`

| Триггер | Файлы (порядок) |
|---------|------------------|
| Avalonia / Dock / CIDE UI | supplement § `router-avalonia-ui` → `status-avalonia-cascade-ide-ui.md` → operational playbook → `kb-avalonia-ui-dock-fundamentals.md` |
| Таблица пакетов vs факт | `work/projects/door-to-singularity/cascade-ide/kb-cide-evidence-card-spec.md` + `CascadeIDE.csproj` |
| Мёртвые URL / VerifyAccess | `kb-avalonia-docs-vs-source-notes.md` |

### `project-card-evidence`

| Триггер | Файлы (порядок) |
|---------|------------------|
| Любой **`project-id`** в `work/projects/…` | README карточки → локальные `kb-*` / `EV-*` / `operational.md` |
| После bump зависимостей | обновить снимок и **`Проверено:`** в spec/evidence; не дублировать в корень `knowledge/` без причины |

### `provenance-meta`

| Триггер | Файлы |
|---------|--------|
| Существенная правка факта | `META/provenance-contract.md` + `templates/template-knowledge-card.md` |
| Новая карточка | шаблон + `playbook-knowledge-engineering-core.md` § Promotion quality gates |

### `layers-publishing`

| Триггер | Файлы |
|---------|--------|
| personal / org / public | `kb-one-pager-structure-and-protocols.md` § слои; `PUBLISHING.md`; `playbook-multi-project-context.md` §6c |

### `mcp-access`

| Триггер | Файлы |
|---------|--------|
| MCP не читает kb | `runbook-kb-mcp-access.md` |

---

## 6. Чеклисты (коротко)

### Плановая перепроверка по слою

1. Открыть **`status-<domain>.md`** — § Maintenance Policy / Next review triggers (§2.2).
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
- Путать **свежесть** с **первичным изучением** домена (`playbook-learn-basics-when-stuck.md`).

