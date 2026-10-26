# ADR 026: KB переезжает на OKF — канон как OKF bundle + естественное расширение полей

**Tags:** #adr #kb #okf #transfer #routing #agentnotes #migration

**Статус:** Accepted (operator steer 2026-10-23: «переведи до конца» — старт M0→M1)
**Дата:** 2026-10-23
**Источник в истории:** steer оператора 2026-10-23, три итерации. (1) OKF как внешняя проекция канона — отклонено: **OKF = канон, одноразовый полный переезд**. (2) **Мы расширяем OKF так, чтобы наши концепции вписались нативно** — типы и поля профиля часть словаря бандла. (3) **Без префикса `x-agentnotes-`** — натуральные имена полей (`transfer:`, `routing:`, `contour:`, `layer:`, `scope:`): «естественное расширение».
**Supersedes:** —
**Extended by:** —
**Связано:** [001](001-kb-public-publishing-pipeline.md) · [007](007-kb-project-constitution.md) (совместимость — §12) · [008](008-workspace-scope-map-hot-mcp-and-public-cut.md) · [009](009-kb-entry-structure-and-pre-open-onboarding.md) · [011](011-aiguiders-org-collaborative-kb-repo.md) · [012](012-multi-canon-workspace-resolution.md) · [013](013-agent-notes-mcp-local-settings-toml.md) · [020](020-kb-language-contours.md) · [022](022-kb-graph-substrate.md) (ingest, TransferPolicy, Sat) · `worlds/knowledge-engineering/matrix-do-not-transfer.md` · `templates/matrices/template-transfer-matrix.md` · `knowledge/index-knowledge-router.md`

---

## Контекст

### 1. OKF v0.2 (факты)

Google Cloud, v0.1 2026-06-12 (blog «How the Open Knowledge Format can improve data sharing»), каноническая спека — `github.com/GoogleCloudPlatform/open-knowledge-format` (v0.2). Формализация LLM-wiki паттерна (Karpathy gist): знания как plain markdown + YAML frontmatter.

| Примитив | Определение |
|----------|-------------|
| **Bundle** | единица дистрибуции: git repo / tarball / подкаталог |
| **Concept** | один `.md`; **Concept ID = путь файла без `.md`** |
| Резерв | только `index.md` (листинг каталога, §8) и `log.md` (история, §9) |
| Обязательное поле | **только `type`**; типы не централизованы, потребители терпят неизвестные |
| Рекомендуемые | `title`, `description`, `resource`, `tags` |
| v0.2 | `sources` + `usage_window` (провенанс §5.1), `generated`/`verified` + trust-уровни (§5.2), `status` (`draft|stable|deprecated`) + `stale_after`, тип Attested Computation, actor-конвенция |

Ключевые правила:

- **§11 Conformance:** потребители **не имеют права** отвергать bundle за отсутствующие optional-поля, неизвестные `type`, **неизвестные extra keys**, битые ссылки.
- **§12 Extensions:** producer'ы добавляют любые extra keys; потребители сохраняют unknown keys при round-trip. Формальных profiles нет — расширение на стороне producer'а, naming-конвенция не предписана.
- **§12 Versioning:** `okf_version` в root `index.md`; v0.1→v0.2 уже ломал (`timestamp` → `generated.at`, `# Citations` → `sources`) — breaking до 1.0 возможны.

### 2. Почему полный переезд (operator steer)

KB уже bundle-shaped: концепт = файл, identity = путь, markdown-связи, теги, каталоги-индексы. Наша реальная разница с OKF — **словарь, не форма**: `**Tags:**`-строки вместо frontmatter, секционная разметка, transfer/routing на языке prose. Держать два словаря (свой + OKF) — двойная форма без выгоды; переезд на OKF как канон делает наши концепции читаемыми любым OKF-агентом **и** упрощает собственные инструменты (парсинг frontmatter вместо кастом-строк).

**Факт независимой конвергенции (2026-10-24):** оператор построила эту форму в живом диалоге с агентами **до** того, как увидела gist Карпатого (и не поняла из одного gist, в чём прикол — паттерн у неё уже работал). Старт экосистемы — **2026-02-15**: файлик → KB → 1669 OKF-концептов за ~8 месяцев, меньше года до принятия открытого стандарта. Сходимость «диалог → та же структура» без знания спеки — свидетельство, что форма естественна; скорость — аргумент для upstream-питча (агент-мейнтейнинг сжимает цикл зрелости формата).

### 3. Чего в OKF нет — и что мы добавляем расширением

| Наш механизм | Сейчас | Станет в OKF |
|--------------|--------|--------------|
| Transfer matrix (`matrix-*.md`) | prose + таблица | concept `type: Transfer Matrix` + поле `transfer` |
| Do-not-transfer boundary (`matrix-do-not-transfer.md`) | prose + таблица | concept `type: Do-Not-Transfer Matrix` + то же поле; deny-by-default остаётся core rule |
| Routing (`index-knowledge-router.md`: порядок `status → playbook → matrix → kb`, бюджеты, entry map) | prose-таблицы | concept-роутер + поле `routing` |
| Слои L0 hot / L1 / on-demand | memory-load policy | поле `layer` на концепте |
| Contours u/g/o (public-cut, roots chmod) | разметка + chmod | поле `contour` |
| Scope maps (workspace → scope) | [008]/[012] | поле `scope` |

---

## Решение

### 1. Канон = OKF bundle

Bundle root — корень репо `agent-notes`; concepts — все `.md` под `knowledge/**`, **кроме `knowledge/adr/`** (см. ниже). `okf_version: "0.2"` в root `index.md`. Concept ID = путь — идентичность всех существующих ссылок сохраняется.

Каталожные `README.md` → `index.md` по месту (§8); история каталогов — `log.md` из `.revisions`.

**ADR — не concepts бандла** (operator steer 2026-10-23): ADR — governance-жанр (решения и их история), не knowledge payload; «ADR это ADR». Файлы остаются в `knowledge/adr/` в git с собственной конвенцией (`Статус` / `Дата` / `Supersedes` / `Extended by`); OKF frontmatter для них не требуется, M2 не транслирует. Graph ingest [022] может индексировать их как `Adr`-узлы — это IR над репо, независимо от членства в бандле.

**Ревизия 2026-10-24 (operator steer: «ADR — знания → KB-ADR живут в бандле»; «шапка ADR — шмат текста»):** две популяции, разведены явно:

- **KB-own ADR (`knowledge/adr/`) — полноправные concepts канон-бандла** (`type: ADR`, contour непубличный): frontmatter по профилю (status, tags, supersedes), шапочная конвенция (`Статус`/`Дата`/`Supersedes`/`Extended by`) миграцией поднимается во frontmatter (по касанию); `Связано:` — **буллет-список с аннотацией связи** (тип ребра — прозой, читаемо), не однострочная колбаса. Реверс части решения 2026-10-23: «ADR это ADR» остаётся про жанр, KB-ADR — знание канона.
- **Продуктовые ADR — SSOT у кода, НЕ копируются в KB** (ранее принято): копипаст-скрипт отвергнут — dual form + независимость от KB + публичные репо + PR-флою решений. KB-граф индексирует их в репо-бандлах.
- **Шаблон**: `templates/meta/template-adr.md` — карточка шаблона ADR в бандле (OKF frontmatter + буллет-Связано).
- **Git — SSOT времени и истории** (operator steer 2026-10-24: «любое репо имеет git — не запихивать в generated.at, а указывать sha; changelog генерят из коммитов»): концепт git-резидента **не дублирует даты** во frontmatter — «когда/кто» даёт `git log`/`blame`; frontmatter — только семантика. Пины — через `resource` = canonical URL коммита/блоба (immutable; спека `derived_from` отложила — наш прецедент). `log.md` — **derived из git** (commit messages), не рукописный; `.revisions` — не двойная форма с git, а другая ось (инструментальные снапшоты MCP: какой тул каким вызовом). Исключение — **дистрибутивные срезы** (тарболл/zip без git, kb-public): там даты в снапшоте — единственные часы, доезжающие до получателя.

Детализация, как тексты и рёбра разложились по бандлам:

- **Текст ADR живёт там, где код** (независимость от KB — первичный约束): KB-own ADR — в `knowledge/adr/` репо канона; продуктовые ADR (`dash-spec/design/`, `cdp-mcp/docs/adr/`, …) — в своих репо. Канон-граф [022] **индексирует оба вида** как `Adr`-узлы (+ `Supersedes`-цепочки) — знание о решениях доступно графу без копирования текста.
- **Продуктовое репо — само OKF-бандл** (bundle = git repo, спека; OKF вырос из LLM-wiki паттерна репо-документации, concepts покрывают и API/runbooks/таблицы — «про код в том числе»): его ADR — concepts `type: ADR`, frontmatter по нашему профилю **по касанию** (не массовая миграция), `resource` → код-якорь.
- **Correspondence** (CDP-ADR-0031, `cdp_analysis_scene feature=correspondence`): as-built мост код↔решения — `[workspace.adr.map]` в `.cascade/workspace.toml` (locus → ADR) + corr-gate (mutate soft-refuse без свежего latch). В OKF-рамке это рёбра графа locus→ADR; SSOT текста — репо-бандл ADR, рёбра — у владельца локуса. KB-граф и corr-механика пьют из одних и тех же ADR.

**Корень репо вне `knowledge/`** (bundle root = repo root, OQ-3): root `README.md` → root `index.md` (+ `okf_version`); `CHANGELOG.md` → root `log.md` (законное применение reserved-имени §9 спеки — история изменений); `user-work-log.md`, `secret-mode-prefix-ru.md` — concepts contour `u`; `scopes/` — legacy-redirect (один `MOVED.md`), вне бандла; `scripts/`, `tools/`, `dist/`, `tmp/`, `scratch/` — код, сборки, транзиенты — вне бандла.

### 2. Одноразовая миграция (маппинг полей)

| Канон сейчас | OKF v0.2 |
|--------------|----------|
| `**Tags:** #a #b` | `tags: [a, b]` |
| H1 заголовок | `title` |
| первые строки-описание / README-описание | `description` |
| `Проверено: <дата>` / `updated_at` | `verified: [{by, at}]` / `generated.at` |
| `status-*` свежесть (playbook-kb-operational-freshness) | `status` + `stale_after` |
| первоисточники (DOI, ссылки в теле) | `sources` (§5.1) |
| «НЕ ПУБЛИКОВАТЬ» (первая строка файла) | `contour: u` (билд читает frontmatter; на переводной период первая строка остаётся дублирующим human-visible маркером) |
| Тип файла — конвенция префиксов имён | `type` (реестр значений — §9) |
| Суффикс `.md` | `language: ru` (суффикс остаётся файловой конвенцией; OKF Concept ID — `foo.ru`) |
| Метаданные карточек (card_id, world, status, confidence, supersedes, …) | поля профиля §3; `card_id` отбрасывается — Concept ID уже путь |
| Provenance-блок карточек (`source_refs`, `created_at`, `updated_at`, `author`) | OKF `sources` + `generated` / `verified` — **прямая конвергенция** с `META/provenance-contract.md` |
| Алиасы проектов (`CDP` → `cdp-mcp`, `GUIP` → `guiders-ui-platform`) | `aliases: [...]` на карточках проекта/подпроекта |

Section markup `<!-- section:ID -->` **остаётся в телах** — OKF-conformant (спека body-синтаксис не предписывает). Механики секций в OKF **нет**: атом — файл, адресация — только на файл целиком; body-конвенции — лишь SHOULD-заголовки `# Schema` / `# Examples` / `# Computation`. Границы секций выразимы только в теле (YAML не умеет указывать на span файла), поэтому **маркеры — normative для границ**; во frontmatter миграция добавляет `sections:` — реестр id (§3), SAT держит соответствие.

**Принцип «нет двойной формы» (operator steer 2026-10-23):** самодельные строковые форматы существовали, потому что YAML не было; с нативным frontmatter формат, получивший поле, **уходит из тела полностью** — `**Tags:**` → `tags:`, `**Speech situation (…):**` → `speech_situation:`, одиночные `Проверено: <дата>` → `verified:`. Мигратор удаляет эти строки из тел; `# H1` остаётся (контент, не мета; `title` — его queryable-дубль).

**Эволюция секций (operator steer 2026-10-24: «отсутствие механики секций — недостаток; можно выразить секции дополнительными концептами»):** согласовано — это родной для спеки путь (вики-паттерн, атомарные концепты) и продолжение политики канона `memory-large-sections-policy-v1` («секция растёт / точечные запросы → разбить на подсекции с id»). Правило: **секция, доросшая до самостоятельного знания** (свой DoD/триггеры/частые точечные запросы), **отделяется в концепт по касанию** — родитель остаётся hub-концептом, `sections:`-реестр отражает расщепление автоматически. Исключения: hot-слой (рантайм-целостность файла — фича, не баг) и секции-указатели (концепт-пустышка — шум). Сам дефицит (нет sub-file адресации в спеке) — upstream proposal №1 (§6); реестр — переходный механизм до его принятия.

**Рабочая гипотеза «секции = компенсация отсутствия графа» (operator, 2026-10-24 — без решения, дозревает):** секции держат три вещи — (1) знание внутри большого файла (заменяется графом + отдельными концептами наилучшим образом), (2) адресация runtime-hot (граф не заменяет: 150 мелких файлов на ход дороже одного файла), (3) указатели-стабы (умрут сами). Кандидат-эксперимент после M3-графа [022]: на одном мире сравнить `route_context` через граф-срез (запрос → рёбра → подсграф) против секционного скоринга на живых запросах. Мораторий на резкие движения: механика секций остаётся как есть.

### 3. Расширение OKF: натуральные поля, без префикса

Профиль — часть словаря нашего бандла, имена без неймспейс-префикса (`x-`-конвенция отклонена оператором как лишняя: §11 и так гарантирует толерантность к unknown keys, мы — primary consumer):

| Поле / тип | Содержимое | Источник в каноне |
|------------|-----------|-------------------|
| `type: Transfer Matrix` | матрица переноса | `template-transfer-matrix` |
| `type: Do-Not-Transfer Matrix` | граница непереносимости | `matrix-do-not-transfer.md` |
| `transfer` | `{ default: deny\|allow\|allow-with-check, boundary: <id>, falsification_trigger }` | core rule + строки матриц; те же значения, что рёбра [022] `TransferAllow/AllowWithCheck/TransferDeny` |
| `routing` | порядок загрузки (`status → playbook → matrix → kb`), бюджеты (tiny/normal/deep), hints | `index-knowledge-router.md` |

**Routing-подсистема (as-built по коду AgentNotes.Core, 2026-10-24; steer: «это один роутер — иди смотри route_context»):** файлы-роутеры — **данные**; машина — пять слоёв: (1) resolv scope (`NotesStorage.Scope.cs`); (2) `route_context` — скоринг секций hot (совпадения×4, +24/полный query в контенте, +20/id, позиционный бонус hot-порядка `30−idx×2`), бюджеты `max_sections`/`max_chars`; (3) **knowledge-roots overlay** — до 3 записей реестра с превью из read-only корней (+32) при мульти-рутных запросах; (4) corpus: каскад resolve→lookup→search по тег-индексу (`KnowledgeTagIndex`), role-тег `#ssot` — второй ключ сортировки, scope-boost +50/+100 (`KnowledgeCorpusRecall`); (5) `memory_health` — бюджеты из `memory-architecture.json`. **Регресс M2 (критично, M3 п.1):** corpus-слой парсит `**Tags:**` из тел — после миграции строки в frontmatter `tags:`, тег-индекс/ssot-сортировка ослепли на 1669 файлах. Фикс: dual-read (frontmatter `tags:` + legacy-фолбэк) в `KnowledgeTags` → потом полное переключение; заодно — эмит `sections:` реестра мигратором.
| `contour` | `u \| g \| o` — видимость концепта; `u` исключает из публичного и группового артефактов | roots chmod [013]; маркер «НЕ ПУБЛИКОВАТЬ»; механика публикации — §8 |
| `layer` | `hot-stub \| l1 \| on-demand` | memory-load policy |
| `scope` | active_scope концепта (`portal`, `harvester`, `imc`, `mixed`, `door-to-singularity`, …) | scope maps [008]/[012] |
| `sections` | реестр section id концепта: `[id, …]`; границы секций — body-маркеры `<!-- section:ID -->` (normative); SAT: `sections` ↔ маркеры без drift | section markup канона (MCP `upsert_agent_notes_section` и др.) |
| `world` | первый сегмент слага мира из каталога `worlds/<world>-<subworld>/` (`biology`, `knowledge`, `pedagogy`, `software`, …); SAT: согласован с путём | таксономия [009]; operator steer 2026-10-23 — вместо одного dotted-id пара полей |
| `subworld` | остальная часть слага через дефис (`ant`, `engineering`, `russian-language`, `dotnet-csharp`); полный dotted-id производен: `world.subworld` (`knowledge.engineering`); карта подмиров (`world-life`) — concept `type: Map`, подмиры — его `sections` | slug-конвенция миров, map-world-life-subworlds |
| `related_worlds` | декларативные кросс-мировые аффилиации (dotted ids, опционально): routing-подсказка «этот мир мостится туда-то»; **не** норматив переноса (норматив — transfer-матрицы); решение агента-мейнтейнера 2026-10-24: один дом (`world`/`subworld`) + рёбра (матрицы, links, related_worlds), без мульти-home | bridge-строки роутера, kb-se-cooperation-gap-vs-aviation |
| `language` | `ru \| en \| zh \| …`; отсутствует → язык контура (A=EN, B/C=RU/mix; [020]). Канон триязычен фактически: RU — интерьер, EN — открытый периметр, **ZH — первоисточники** (мир `philosophy-dao-chan`: Дао Дэ Цзин Ван Би / Мавандуй, Чжуан-цзы, Лецзы, Хуйнэн, Конфуций — evidence-карточки с китайским текстом) | языковые контуры [020] |
| `speech_situation` | `{ audience, goal, genre, channel, stakes, distance, forbidden_moves[], when_citing_to_human? }` | template-speech-situation-metadata; Sat-007 (обязателен на canon-плейбуках) |
| `epistemic` | `{ basis: fact\|inference\|hypothesis, confidence: low\|medium\|high, evidence_type?, falsification_trigger? }` | knowledge-card / evidence-карточки |
| `supersedes` / `superseded_by` | id концептов — lifecycle-цепочки | карточки; рёбра `Supersedes` [022] |
| `depends_on` | id packs — граф зависимостей LLM-native packs | `pack.toml` (§10) |
| `project` / `subproject` | project-id slug (+ sub-project внутри родителя: `…/subprojects/<id>.md`); SAT: согласован с путём `work/projects/<scope>/<id>/` | карточки проектов [003], sub-project конвенция |
| `aliases` | короткие имена → канонический id; резолв `[PRIMARY:…]` слева направо (parent-алиасы, затем sub-алиасы) | карточки проектов/подпроектов; scope-alias-map |
| `from` / `to` / `cc` | **имена стандарта RFC-5322** (наследник RFC-822; operator steer 2026-10-25 «можно сразу стандарт и взять») для Forum Post: `from` — ник линии-автора (`tikhon`; человек — `human:sveta`), `to` — прямые адресаты (intercom-wake DM), `cc` — копия/FYI (crew-канал); семантика определена стандартом, To≠Cc различают все | LinesForum, intercom (CDP-ADR-0212) |
| `in-reply-to` / `references` | RFC-5322: линк на тред-концепт / вся цепочка (глубокие ветки); Subject→`title`, Date→`generated.at`, Message-ID→Concept ID (путём) — **уже покрыто OKF-native, новых полей не заводим** | LinesForum |

**Политика коллизий с upstream** (вместо префикса):

- Наши имена (`transfer`, `routing`, `contour`, `layer`, `scope`, `sections`, `world`, `subworld`, `related_worlds`, `language`, `speech_situation`, `epistemic`, `supersedes`, `depends_on`, `project`, `subproject`, `aliases`, `from`, `to`, `cc`, `in-reply-to`, `references`) **проверены против полевого набора v0.2** (`type`, `title`, `description`, `resource`, `tags`, `sources`, `usage_window`, `generated`, `verified`, `status`, `stale_after`, `okf_version` + семейство Attested Computation) — пересечений нет.
- Pin `okf_version` (§6) + CI-проверка: полевой набор спеки на pinned-версии не содержит имён профиля. Если будущая версия_claim'ит наше имя с иной семантикой — механический rename через ADR (канон в git, миграция дешёвая).

Правило гигиены профиля: новое поле профиля — только через ADR-ряд (026+). Prose-тело матриц и роутера сохраняется (wisdom остаётся prose); поля делают механизмы **queryable** для своих инструментов и внешних агентов.

### 4. Hot layer — concept бандла с двойной ролью

`agent-notes.md` — **concept канон-бандла** (`type: Hot Notes`, `layer: hot`): файл версионирован в каноне, и его публичный срез реально публикуется — kb-public включает `agent-notes.md` (as-built, `dist/public-kb/`). «Runtime-слой MCP» — роль при исполнении (hot cache), не аргумент против членства в бандле: один файл, две роли. Инвариант hot-split сохраняется; публикация — срезом секций (§8).

### 5. MCP tooling ([013])

- `write_knowledge_file` / `upsert_knowledge_section`: frontmatter обязателен при создании концепта (минимум `type`), unknown keys сохраняются при round-trip (§12).
- `validate_sections` + новый OKF-валидатор: §11 conformance + проверка полей профиля (типы значений, ссылки boundary) + `sections` ↔ body-маркеры + коллизии против pinned-спеки (§3).
- `knowledge_tags` (canon-map): источник — frontmatter `tags` (после миграции `**Tags:**`-строки выводятся из употребления, OQ-5).
- `route_context` / `read_hot_context`: маршрутизация читает `routing` / `layer`.
- `.revisions` — остаётся нашим слоем (вне OKF); каталогные `log.md` генерируются из него.
- Machine-конфиги (не concepts, остаются JSON/TOML): `memory-architecture.json` (L0-манифест — драйвит include-инвариант публикации), `kb-topic-tag-aliases.json` (алиасы тегов для `knowledge_tags`), `mcp-resolve-paths.json`, MCP TOML [013].
- **Контракты обслуживания — сами становятся concepts бандла** (`type: Maintenance Contract`, operator steer 2026-10-23): бюджеты L0+L1 (soft 6k / hard 12k символов), retrieval-порядок `status → playbook → matrix → kb`, операционные триггеры (`memory_health` / `route_context` / `compact_hot_context`), freshness-протоколы — сейчас текст живёт вне канона (`KB-V2-CONTRACT.md` в репо agent-notes-mcp); миграция переносит его в бандл. Причина: агент — основной потребитель **и автор** KB; командная поверхность оператора минимальна («запиши в KB», «сделай фундаментальный проход») — значит инструкции по мейнтенансу обязаны быть queryable-знанием внутри бандла, а не README соседнего репо. MCP v3 — enforcement; текст — concept.

### 6. Версионирование upstream

Pin `okf_version: "0.2"`. Bump — только через ADR (breaking-риск до 1.0 закрыт тем, что канон у нас в git: мажорный bump = механическая миграция frontmatter + ADR). 

**После M2 — upstream proposal** в `GoogleCloudPlatform/open-knowledge-format` (аддитивный, по их правилам backward-compatible growth), кандидаты: (1) **`sections`-реестр** — sub-file адресация концепта (у нас решена: frontmatter-реестр + body-маркеры, спека молчит); (2) **cross-domain links с семантикой переноса** — Transfer Matrix / do-not-transfer: безопасность переноса знаний между доменами, универсальная проблема для agent-KB; (3) **routing score hints** — декларативные сигналы приоритизации потребления (as-built у нас: scope boost +50/+100 и ssot-first в `KnowledgeCorpusRecall`, CDP-ADR-0210); (4) **`language`** — generic-поле для мультиязычных бандлов. До M2 — не питчим: сначала система должна работать на OKF.

### 7. Мультиканон: три контура знаний и федерация ([011]/[012]/[013])

- **Три контура**: personal (`u` — наш канон-бандл) → **group/org** (`g` — общая копилка знаний организации: не готовое к публичности, но доступное всем агентам org; сценарий: организация (z.ai-класс или любая другая) не хочет выносить знания в `o`, но хочет, чтобы их видели все её агенты) → public (`o` — kb-public). Каждый контур — собственный OKF bundle; `contour` — на уровне bundle и концепта.
- **Group KB — двунаправленная федерация, не просто read-only**: для агентов org-корень подключён read-only (MCP [013]), но обновление — процедура [011]: личный канон → `export-to-org-kb.ps1` (**только** пути из `group-kb.export`, не full replace; санитизация путей по checklist `work/org/`) → PR в `{ORG}/kb` (routine); `bootstrap-org-kb.ps1` / `seed-org-kb.ps1 -Push` — только bootstrap/DR; обратно — `import-from-org-kb.ps1` (opt-in, без auto-commit, review diff).
- **Scope rename между контурами**: при экспорте пути маппятся (`door-to-singularity` → нейтральный `aiguiders-open` по `scope-contour-map`); одно знание живёт под разными Concept ID в personal и group бандлах — связь через `resource` (canonical URI) или маппинг в contour-map; SAT **не** требует одинаковых ID между бандлами.
- kb-public [001] и group-kb = генерируемые **subset-bundle'ы** из канона (механика — §8); выход OKF-native: root `index.md` + `okf_version`, публичный срез hot — generated concept с `generated.by`.

### 8. Механика публикации: граница — build policy, не позиция в файле

As-built (проверено по `build-public-kb.ps1` / `KbAgentNotesPublished.ps1` / `PUBLISHING.md`):

| Механика | Сейчас | В OKF-миграции |
|----------|--------|----------------|
| Срез hot | **список секций** `knowledge/kb-public-agent-notes.include` (ADR-008 §28; позиционный маркер `public-cut` перестал быть SSOT после инцидента 2026-09-26 — маркер уехал, сборка опустела молча) | остаётся data-driven списком; SAT: include ⊆ `sections`-реестр hot-концепта; громкий инвариант «L0-секция обязана быть в списке» сохраняется |
| Маркер `<!-- public-cut -->` | retired как контракт; **PUBLISHING.md п.1 всё ещё описывает старую механику — рассинхрон, синхронизировать** | в миграцию не переносится; тела файлов не переписываются (деградирует до prose-комментария) |
| Фильтр `knowledge/**` | `public-kb.ignore` (gitignore-паттерны: `personal/`, `work/`, `archive/`, `temp/*-scratch.md`, `.revisions/`, сами ignore/push-файлы) | остаётся build-конфигом (не concept) |
| Единичный файл вне public | первая строка «НЕ ПУБЛИКОВАТЬ» → **выполнено 2026-10-24**: маркерные файлы (101) мигрированы — `contour: u` во frontmatter, маркер удалён из тела; `build-public-kb.ps1` frontmatter-aware (`Test-KbPrivateContour`: маркер ИЛИ contour-u до закрывающего fence); попутно найден и закрыт баг хелпера `Read-KbUtf8FirstLine` на LF-only первой строке (смешанные EOL после миграции → утечка 1 файла в паблик, поймана leak-чеком `grep ^contour: u dist/`); верификация: 0 первых-строчных маркеров, 0 contour-u в dist, счётчики = baseline + легитимные новые |
| Роутер-индексы | auto-strip секций `##`, ссылающихся на исключённые файлы | без изменений |
| group-kb | `seed-org-kb.ps1` + `group-kb.ignore` | тот же паттерн subset-bundle |
| kb-base-cide | `build-kb-base-cide.ps1` + `kb-base-cide.include` — компактный обязательный срез для встраивания (CIDE) | третий subset-bundle, тот же паттерн |
| Release manifest | sha256 + tree hash (HIS, CDP-ADR-0206) | без изменений |

Граница «публичное / личное» — механика первого класса и остаётся ею: это **build policy поверх бандла** (include-список + ignore-файлы + `contour`), а не позиция маркера и не свойство формата. `contour: u` — декларативный per-concept override; SAT ловит конфликты (например, файл в include-списке с `contour: u`).

### 9. Типовая система: конвенции имён → `type`

Префиксы имён — уже работающая система типов (инвентарь: `kb` ×355, `kj` ×234, `note` ×157, `playbook` ×135, `checkpoint` ×64, `status` ×39, `template` ×32, `map` ×18, `matrix` ×14, `index` ×13, `incident` ×9, `runbook` ×8). Миграция закрепляет её как значения `type`:

| Префикс / шаблон | `type` |
|------------------|--------|
| `status-*` | Status |
| `playbook-*` | Playbook |
| `kb-*` | KB |
| `matrix-*` | Transfer Matrix / Do-Not-Transfer Matrix / Routing Matrix |
| `map-*` | Map |
| `runbook-*` | Runbook |
| `note-*` | Note |
| `index-*`, `domain-index` | Router / Index |
| `checkpoint-*` | Checkpoint |
| `kj-*` | Journal (Kolb; contour `u`) |
| `incident-*` | Incident |
| `article-*`, `book-*`, `digest-*` | Article / Book / Digest |
| `template-*` | Template |
| карточки: knowledge / evidence / definition / misconception / project / sub-project / domain-note | Knowledge Card / Evidence Card / Definition Card / Misconception Card / Project Card / Sub-Project Card / Domain Note |
| `agent-notes.md` | Hot Notes (§4) |
| `onboarding-*` | Onboarding (вход агента в среду; оператор 2026-10-26: «не Course — онбординг по сути»; прецедент: `onboarding/` (корзина), симметрия agent-first-learn ↔ newcomer ↔ agent-onboarding) |
| `META/environment-axioms`, `integrity-core`, `integrity-post-spec`, `awareness-*`, `provenance-contract` | **Meta Contract** (well-known paths; права и рамка агентов в среде; контур A — публичны) |
| Контракты обслуживания: бюджеты L0+L1, retrieval-порядок, триггеры, freshness | **Maintenance Contract** (перенос из `KB-V2-CONTRACT.md` репо MCP — в бандл) |
| Глоссарий операторских команд и терминов среды | **Glossary** (новый артефакт; seed — M2) |
| `work/projects/<scope>/<id>/README` | Project Card; `subprojects/<id>.md` — Sub-Project Card; `active-scope.md` — State |
| `LinesForum/topics/NNN/00-thread.md` | Thread; **новые посты — `type: Forum Post`** (RFC-5322 поля from/to/cc/in-reply-to, см. §3; шаблон `templates/cards/template-forum-post.md`; исторические треды не расщепляются — посты-в-теле остаются прозой, новые посты рождаются концептами по правилу эволюции секций) |
| `handoff-*` (`knowledge/handoff/`) | Handoff |
| `work/scientific-papers/` (реестр `index-papers` + досье) | Manuscript Dossier / Paper Card |
| `user-work-log.md`, `secret-mode-prefix-ru.md` (root) | Work Log / Note (contour `u`) |

Имена файлов **не переименовываются** (ID = путь; renames ломают ссылки и `.revisions`) — `type` дублирует семантику префикса в queryable виде. Личный контур `personal/` (contour `u`) — **не** бесструктурный, у него собственные жанры, и они тоже получают `type`: **Agent Line** (карточка линии, `assistantLines/<line>/`), **Incarnation** (инкарнация линии по дате; шаблон `assistantLines/_templates/incarnation-note-template.md`), **Thread** (`LinesForum/topics/NNN-*` — межлинейная переписка с `_index.md`), **Diary**, **Field Report** (`agent-harness-field-reports/`), **Recognition Map** (`recognition-history/` — история узнавания), **Dialogue Archive**, **Carrier Model**. Прочие личные файлы (`note-*`, `ah-*`, `kj-*`) — типизируются свободно.

Зеттель-слой [006] (Proposed, не внедрён; каталога `zettel/` нет): если взлетит — `type: Zettel`, поля `thesis` + связи `supports`/`contrasts` как markdown-links (в [022] — рёбра `Supports`/`Contrasts`).

Онбординг (`templates/newcomer/`): треки участника (kb-public → personal) и основателя (white-label org) — concepts `type: Playbook`; комплект чистой установки (workspace-scope-map, knowledge-roots-index, hot-блоки, MCP TOML) — `type: Template`. Вход — `newcomer/README.md` (§8-подобный листинг онбординг-пути и для «мясного», и для ИИ-новичка).

**Integrity POST** — habitat-механика поверх бандла: наличие `integrity-core.md` / `awareness-as-countermeasure.md` как well-known концептов = корень доверия активен; удаление → POST failed + Minimal Safe Default (спека `META/integrity-post-spec.md`). Поведение — среда/MCP; в бандле — обязательность присутствия концептов (Sat-008 [022] — hash manifest корневых файлов).

Корзина `knowledge/archive/` (миры на пенсии, напр. `human-perception`) — concepts со `status: deprecated`; «на пенсии» — поле, не только путь.

**Глоссарий (закрытие разрыва):** термины среды имеют точное значение, не выводимое из общих слов. «Запиши в KB», «фундаментальный проход» (оператор называет область → агент идёт по первоисточникам → карточки; уровни: **полный проход** vs **точечный запрос**; ограничение «не грузить все kb одновременно»), уровни и виды проходов. Сейчас семантика рассеяна: supplement-хинты роутера, § Full fundamental pass в плейбуках, образцы-миры (например `software.engineering-evidence`: треки чтения A–H, карта глав Code Complete 2, evidence-протокол). Seed-артефакт миграции: `knowledge/glossary-operator-commands.md`, `type: Glossary`, каждая запись — термин + определение + якорь на concepts-прецеденты.

### 10. LLM-native packs: TOML → OKF

7 packs (`domains/agent-operations` + 6 миров): `pack.toml` + `definitions/*.md` + `misconceptions/*.md` + `procedures.toml` / `processes.toml`; обслуживаются MCP (`get_definition` / `get_procedure` / `get_process`).

| Сейчас | Станет |
|--------|--------|
| `pack.toml` (id, version, layer, title, onboarding, depends_on, sources) | `pack/index.md` — законное применение reserved-имени §8: метаданные пака во frontmatter; `depends_on` — граф паков |
| `definitions/*.md`, `misconceptions/*.md` | concepts `type: Definition Card` / `Misconception Card`; карточные поля (`applies_when`, `llm_cue`, `gate_step`, `related`, `sources`) — во frontmatter |
| `procedures.toml` (`[[procedure]]`: apply_when, signals, phases, steps, gate) | concepts `type: Procedure` (when-card) |
| `processes.toml` (steps / gate / definition_anchors) | concepts `type: Process` |

Конвертация TOML → MD — часть миграции (OQ-8); MCP v3 читает MD + frontmatter вместо TOML.

### 11. Протоколы взаимодействия — chat-level, не поля бандла

Маркеры **`[WORK]` / `[HUMAN]`** (дефолт в треде — HUMAN, до явного `[WORK]`; playbook-mode-switch) и **`[PRIMARY:<project-id>[/<sub-project-id>]]` / `[SCOPE:…]`** — протоколы разговора; в OKF они **не** переносятся как поля. Переносится их семантика:

- Роутинг по режиму: `[WORK]`-контент → операционные concepts (`layer: l1 | on-demand`); `[HUMAN]`-контент → personal-контур (`contour: u`, `knowledge/personal/`). Правило живёт как канон (`playbook-mode-switch`, `type: Playbook`) и enforcement в MCP — не в формате.
- `[PRIMARY:…]` / `[SCOPE:…]` резолвятся через `project` / `subproject` / `aliases` / `scope` — резолв становится queryable поверх полей §3.
- Карты резолва (`workspace-scope-map.md`, `scope-alias-map.md`, `active-scope.md`) — machine-local конфиги `work/local/` (contour `u`, в org не коммитятся; в публичные артефакты не попадают); MCP v3 может читать их как concepts приватного бандла (OQ-9). **Пайплайн резолва scope** (as-built `NotesStorage.Scope.cs`; целевое состояние после миграции): явный `active_scope` / `[SCOPE:…]` → machine-local карта — **longest-prefix match** по границе сегмента пути (вложенный `IMC.Portal.Server => imc` перекрывает родителя `PersonalCursorFolder => door-to-singularity`) → hardcoded fallback; на каждом шаге нормализация через alias-словарь (ключи-однотокены, lowercase, пути в alias-файле игнорируются); итог → scope-карточка `scope-<id>` в hot. **Legacy-ветки удаляются в M3** (operator steer 2026-10-23): hot-секция `workspace-scope-map-v1` и чтение `active-scope` из hot — фолбэки вымирают; machine-файл — единственный SSOT резолва, создаётся при инициализации KB (newcomer clean-setup) или агентом. Поле `scope` §3 — **декларация членства** концепта; резолв — runtime-поведение MCP, не поле бандла.

### 12. Совместимость с конституцией [007]

По governance-правилу [007] — ADR, затрагивающий слои поставки, baseline, роутинг, приватность, обязан явно декларировать совместимость:

| Принцип [007] | Как соблюдает этот ADR |
|---------------|------------------------|
| **Single Source of Truth** | канон — git + OKF concepts; все бандлы (kb-public, group, base-cide) — генерируемые subset-bundle'ы, не вручную |
| **Layered Delivery** (KB-Base / KB-Extended) | без изменений: `kb-base-cide.include` остаётся обязательным слоем; OKF не меняет слоистость поставки |
| **Integrity & Epistemic Baseline** | Meta Contracts — well-known concepts; Integrity POST поверх бандла (§9); при конфликте интерпретаций приоритет у baseline-контракта |
| **Privacy by Architecture** | личный слой отделён архитектурно: `contour` + ignore-файлы + include-списки (§8), не «надеемся, что не утечёт» |
| **Router-First Retrieval** | порядок `status → playbook → matrix → kb` сохранён; `routing` поле делает его queryable (§3) |
| **Traceable Evolution** | ADR — вне бандла (§1), цепочка Supersedes/Extended by живёт в git |
| **Format Contract** | канон остаётся Markdown (OKF = MD + YAML frontmatter); конфиг потребителя (TOML в CIDE) не меняется |

---

## Open questions (operator steer)

| Id | Вопрос | Default if silent |
|----|--------|-------------------|
| OQ-1 | Hot в бандле? — **решено** (steer 2026-10-23 + as-built kb-public): в бандле, `type: Hot Notes`, публикация срезом секций (§4, §8) | — |
| OQ-2 | Records JSONL [022]: вне OKF или concept-тип `Record` | вне, wire-format остаётся |
| OQ-3 | Bundle root: repo root vs `knowledge/` | repo root (work/ внутри; adr/ исключён — governance) |
| OQ-4 | `knowledge/personal/**` в бандле | да, contour `u`; паблик-срез фильтрует |
| OQ-5 | `**Tags:**`-строки после миграции | удалить; тег-индекс перечитывается |
| OQ-6 | Пилот миграции | knowledge-engineering (matrices + playbooks) |
| OQ-7 | Граница жанров: `work/` (операционка), `META/`, `templates/` — concepts бандла или вне, как adr? | в бандле (typed concepts; `work/local` — contour `u`); adr — единственное исключение по steer |
| OQ-8 | Packs: конвертация `procedures.toml` / `processes.toml` → concepts или оставить TOML | конвертируем (`type: Procedure` / `Process`), MCP v3 — MD-native |
| OQ-9 | Карты `work/local/` (scope-map, alias-map, active-scope) — concepts приватного бандла или чистый machine-config | **Решено 2026-10-24 (operator: «scope map — отдельный концепт»)**: карты — concepts приватного бандла (contour `u`, `type: Scope Map` / `State`); **тело остаётся словарём** `path => scope` (парсер `NotesStorage.Scope` читает строки — не ломается); наружу — только шаблоны |
| OQ-10 | **Пересмотр `.revisions` vs git** (operator steer 2026-10-24: «revisions — наша механика, не ось знаний; возможно пересмотреть»): канон в git с автокоммитом — снапшоты дублируют субстрат («двойная форма с git»). Путь: хук коммитит **per-op** (гранулярность .revisions), op-name — в сообщение коммита, `rollback` — обёртка над git; старые снапшоты — в zip по retention-политике | git-native, `.revisions` замораживается на M3 |

---

## Non-goals

- Ожидание OKF 1.0
- Смена семантики контента — переезд формата, не переписывание wisdom
- Обязательные upstream PR

---

## Последствия

**Плюсы**

- Один словарь для нас и внешних потребителей: transfer/routing/boundaries читаются любым OKF-агентом без нашего MCP
- Натуральные имена полей — никакого двойного словаря и `x-`-шума
- Собственные инструменты проще: queryable frontmatter вместо парсинга `**Tags:**` и prose-таблиц
- Foundation для [022]: ingest получает структурированный frontmatter из коробки
- Провенанс и свежесть (`sources`, `verified`, `stale_after`) легализуют то, что сейчас живёт в prose-конвенциях

**Минусы / риски**

- Переписывание MCP-тулов (M3) — основная стоимость
- OKF до 1.0 может ломать поля, включая потенциальный name-collision с профилем — mitigated: pin + CI-проверка коллизий + механический rename через ADR
- Переходный период двух форм (`**Tags:**` ↔ frontmatter) — mitigated: миграция одноразовая, по мирам, Sat-проверка mixed-состояния (файл либо полностью мигрирован, либо нет)

---

## План внедрения

```text
M0 — этот ADR Accepted; спецификация маппера (таблица §2 + профиль §3)
M1 — пилот: knowledge-engineering (matrices, playbook) → frontmatter + pack-пилот `epistemic-methodology` (§10); Sat зелёный
M2 — полная трансляция knowledge/** (кроме adr/); log.md из .revisions; index.md из README.md; seed глоссария операторских команд + перенос контрактов обслуживания в Maintenance Contract concepts
  **Выполнено 2026-10-24 (механическая часть):** 1669 концептов мигрировано (CLI `AgentNotes.Okf.Cli`, dry-run→write→стабильность 0 changed, fence-check чистый); 101 файл с первой строкой «НЕ ПУБЛИКОВАТЬ» скипнут (маркер обязан оставаться первой строкой, пока build-фильтр не научился читать frontmatter — M3); status-строки → `status` (чистые удалены из тел, датированные остались); supersedes (98 файлов) — не мигрировано, эвристика рискованна, отдельный заход. Осталось из M2: seed глоссария, Maintenance Contracts, log.md/index.md генерация.
  **Хвосты M2 закрыты в M3 (2026-10-24):** supersedes — буллеты lifecycle карточек (70 файлов) подняты в `supersedes`/`superseded_by` (голые плейсхолдеры и JSON-записи Kolb не тронуты — правильно); **seed глоссария** — `glossary-operator-commands.md` (born-OKF, команды + термины среды с якорями); **Maintenance Contract** — `domains/agent-operations/maintenance-contract-memory-budgets.md` (бюджеты 6k/12k, retrieval, триггеры — из KB-V2-CONTRACT). Из M2-остатков: только генерация log.md/index.md (производные из git — OQ-10/§git).
M3 — MCP v3: frontmatter-native write/validate/tags/route; **п.1: dual-read тег-индекса (регресс M2)**; CI: OKF §11 + профиль-проверки + коллизии; удаление legacy-фолбэков резолва scope (hot-секция `workspace-scope-map-v1`, чтение `active-scope` из hot) — machine-карта остаётся единственным SSOT
  **Выполнено 2026-10-24 (scope):** фолбэки hot-секций удалены из `NotesStorage.Scope`; hot-секция `workspace-scope-map-v1` удалена из `agent-notes.md` + манифеста (`l0` её не содержал, include-инвариант не задет). **Инцидент-находка «v1-дрейф пути»:** TOML (`[workspace] scope_map`), embedded JSON Core и hardcoded-fallback указывали на `workspace-scope-map-v1.md`, реальный файл — `workspace-scope-map.md` (без `-v1`; alias аналогично) → машина-карта **тихо не грузилась** у живого MCP, скоп-резолв фактически держался на hot-фолбэках (потому и не падало). Исправлены все три слоя (деплойный TOML `D:/agent-notes-mcp/`, `Resources/mcp-resolve-paths-defaults.json`, hardcoded fallback); KB-шный `META/mcp-resolve-paths.json` уже был верный. Урок: путь в конфиге без файловой проверки живёт вечно; smoke «резолв скопа через машину-карту» — в CI-кандидаты.
M4 — group-kb → bundle [011]; kb-public → subset-bundle (contour o) [001]
```

Каждый шаг — Sat зелёный до следующего ([022] ритм).

---

## Примечание для роутера

При Accepted — одна строка в supplement: «OKF canon / профиль agentnotes» → этот ADR + миграционный runbook (M1).

Номер 026: 023–025 зарезервированы планом «Extended by» в [022] (records basket, transfer compile, kb-sat catalog).

