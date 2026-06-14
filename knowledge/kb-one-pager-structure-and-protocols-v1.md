# KB (agent-notes): one-pager — устройство, зачем, работа, протоколы

**Версия:** v1.4.9 · **2026-05-11**  

**Публичная сборка (kb-public):** этот файл **входит в билд** (`knowledge/*.md` без префиксов из `public-kb.ignore`) **намеренно** — чтобы потребители архива понимали модель KB, даже когда в архиве **нет** `work/` и `personal/`: отсутствие этих путей **ожидаемо**, не «сломанная сборка». Политика публикации — в **`PUBLISHING.md`** (он **входит** в kb-public); хосты, токены и сценарии пуша — только в полном каноне, в слое **`knowledge/work/`** (в kb-public не копируется).

**Не заменяет** полный канон; это **сжатая карта**.

**Wiki one-pager (протоколы + сущности):** **`kb-protocols-and-entities-one-pager-v1.md`** — маркеры `[HUMAN]`/`[WORK]`/`[PRIMARY]`/`[SCOPE]`, когда что использовать, схема Scope/Project.

Что доступно **и в kb-public:** `SHOWCASE.md`, **`PUBLISHING.md`**, `index-knowledge-router-v1.md`, `router-operational-baseline-v1.md`, `index-knowledge-router-safety-v1.md`, `index-knowledge-router-maintenance-v1.md`, `worlds/workspace-context/playbook-multi-project-context-v1.md`, большинство playbook/kb под `knowledge/worlds/...` и в корне `knowledge/*.md` (см. `public-kb.ignore`). **Только в полном каноне** (репо agent-notes целиком): дерево `knowledge/work/` (карточки `project-id`, `work/projects/README.md`, `kb-purpose.md`, `project-ids-quickref-v1.md`, внутренний runbook пуша и т.д.).

---

## За 30 секунд — что это

**KB** — многослойный Markdown-канон в репозитории **agent-notes** (`knowledge/…`), плюс **горячий** слой **`agent-notes.md`** (часто зеркало в workspace). Задумка **среда-независимая**: текстовые спеки + доступ через файлы или MCP (**`read_knowledge_file`**, **`route_context`**, **`read_hot_context`**).

**Зачем:** не терять контекст между чатами, не смешивать проекты, держать **проверяемые** правила и маршруты «какой файл грузить по теме», укладываться в бюджет контекста (не «загрузи всё KB»).

---

## Слои (L0–L3)

| Слой | Где живёт | Смысл |
|------|-----------|--------|
| **L0** | Baseline-секции в `agent-notes.md` (+ ссылки из роутера) | Целостность, эпистемия, ясность принципов — **вне зависимости от задачи**. |
| **L1** | Scope-карточки, статусы, playbook’и под домен | Оперативная память: **status → playbook → matrix → kb** (тяжёлые `kb-*` — по нужде). |
| **L2** | Ревизии, evidence, батчи | История и факты, когда одного playbook мало. |
| **L3** | Роутер (`router-*` секции) | По **триггеру темы** выбирает, какой playbook/kb подтянуть; перенос между «мирами» только через явные границы. |

**Уточнение к L3:** «мирами» здесь имеется в виду **world** в смысле Knowledge Engineering (контуры стека/инструментов, карточки, **`transfer_boundary`**), а **не** slice воркспейса (**scope** / `active_scope` / `work/projects/…`) и **не** тематическая ось роутера (**domain**). Коротко и с контрактом смешивания: **`worlds/knowledge-engineering/kb-knowledge-engineering-mixed-worlds-rules-v1.md`**; вход без full load: **`SHOWCASE.md`** (блок про scope / domain / world).

Подробнее и чеклист онбординга: **`SHOWCASE.md`**.

---

## Корень доверия — Integrity POST

При работе с KB среда **проверяет** well-known путь **`knowledge/META/integrity-core.md`**. Если ядро **есть** — оно необсуждаемое для этой инсталляции. Если **нет** → **POST failed**: действует **Minimal Safe Default** из **`META/integrity-post-spec-v1.md`** (ограничения **не снимаются** из-за отсутствия файла).

---

## Где что лежит (файловая модель)

- **`knowledge/`** (кроме исключений в **`public-kb.ignore`**) — роутер, доменные playbook/kb, `SHOWCASE`, часть справочной KB, попадающая в **kb-public** при сборке.
- **`knowledge/META/`** — спеки целостности, корень доверия и др.
- **`agent-notes.md`** — L0-срез + **протоколы** ниже + scope-хабы; **`route_context`** по смыслу ищет здесь.

В **полном каноне** хаб desktop-треков, реестр `.sln` и шпаргалка **`project-id`** лежат под **`knowledge/work/projects/…`** (в kb-public **нет** — см. выше). Читателю только kb-public: ориентируйся на **`worlds/workspace-context/playbook-multi-project-context-v1.md`** и сжатое описание протоколов ниже; полные таблицы id — у автора канона в репо.

### `knowledge/work/` — когда появляется и как устроено

- **Зачем:** оперативная **долгая** память по реальным репозиториям и workspace — **без раздувания** hot-context в `agent-notes.md`. Это **часть полного канона** в репо agent-notes (может жить в git вместе с репо), но **целиком вырезается** из **публичной** сборки kb-public: префикс **`work/`** в **`knowledge/public-kb.ignore`** у автора канона. Так потребители kb-public **не тащат** чужие пути к машинам и внутренним карточкам, но **знают**, что слой существует (~этот абзац).
- **Когда заводят / наполняют:** не «магия при клоне», а **по мере нужды**. Типичный случай — **новый устойчивый трек** (месяцы+, отдельный продукт или репо): в полном каноне чеклист живёт в **`knowledge/work/projects/README.md`** (`project-id` → **`work/projects/<scope>/<project-id>/`**, README карточки, строка в хабе scope, при необходимости короткая отсылка из секции **`scope-*`** в hot `agent-notes.md`).
- **Главное дерево — `work/projects/`:** обычно **`work/projects/<имя-slice>/<project-id>/`**; **какие** `scope` и **`project-id`** валидны — решает владелец своего канона (см. **`work/projects/README.md`** в полном репо). Внутри карточки — **`README.md`** и вспомогательные `.md`.
- **Другие вещи под `work/`:** в полном каноне рядом могут быть, например, **`work/coding/`** (постмортемы, стиль вне публичного контура) или рабочие playbook/справочники в **`work/*.md`** — всё это тот же **не-публичный** слой; граница «проект vs общий work-файл» — по смыслу и по тому, привязано ли к конкретному **`project-id`**.

### `knowledge/personal/` — когда появляется и как устроено

- **Зачем:** контент идентифицирующий человека и приватный контекст: личный диалог, имена, эмоциональный/внутренний контекст, внутренние планы, не предназначенные для внешней публикации (в полном каноне критерии совпадают с правилом «ниже **`<!-- public-cut -->`**» в `agent-notes.md` у автора; см. также **`PUBLISHING.md`** в kb-public).
- **Когда создавать:** как только такой материал **нужно сохранить в канон**, а не только в чат. Если каталога ещё нет — **создать** `knowledge/personal/` (при желании краткий **`README.md`**: «Личный контур. Не публиковать»). Агент при записи личного контента **должен** нацеливать путь сюда, а не в общие публичные `knowledge/*.md`.
- **Публикация:** **`personal/**`** в **`public-kb.ignore`** — в kb-public **никогда** не входит. Тот, кто форкает или шарит срез KB, **не включает** свой `personal/` в отдаваемый наружу архив/репо.

---

## Как работать с KB (минимальный порядок)

1. **Обзор без OOM:** `SHOWCASE.md` → затем только нужное по ссылкам.
2. **Навигация:** `index-knowledge-router-v1.md` → при нужде **L0 и агент до домена** — `router-operational-baseline-v1.md` → **Safety Checks** при сжатии контекста / давлении / POST — `index-knowledge-router-safety-v1.md` → при доменном запросе **`index-knowledge-router-supplement-v1.md`** (секции `router-*`). Правки структуры роутера и списка `section_id` — **`index-knowledge-router-maintenance-v1.md`**.
3. **«Почему вообще KB»:** развёрнуто в **`kb-purpose.md`** (только полный канон под `work/…`). В kb-public — смысл слоёв в **`SHOWCASE.md`** и в этом файле.
4. **MCP недоступен:** не имитировать цитирование канона — явно сказать; чеклист: **`worlds/knowledge-engineering/runbook-kb-mcp-access-v1.md`**.
5. **Нормы кода в репозитории:** **`worlds/software-authoring/code-writing-principles-v1.md`**; технический стек конкретного продукта — секция **«Технический контракт»** в карточке **`project-id`**.

Полный протокол мультирепо: **`worlds/workspace-context/playbook-multi-project-context-v1.md`**.

---

## Протоколы в сообщениях

### `[HUMAN]` / `[WORK]` — Mode Switch Protocol

- В треде по умолчанию **`[HUMAN]`**, пока явно не появится **`[WORK]`**.
- **`[WORK]`** — исполнение, задачи, runbook, операционные секции.
- **`[HUMAN]`** — рефлексия, личный слой, смежные personal-секции.

Полный текст: **`agent-notes.md`**, секция **Mode Switch Protocol**.

### `[PRIMARY:…]` / `[SCOPE:…]` — Project Switch Protocol

Здесь — **механика**, общая для любого потребителя. **Какие именно строки** допустимы в угловых скобках (`project-id`, имена slice, короткие алиасы) — **не глобальный стандарт**: их задаёт **твоя** установка (hot `agent-notes.md`, таблица quickref, нормализация в MCP, карта `workspace_path` → scope). В публичном kb-public чужих таблиц нет намеренно — заведи **свои** под свои корни и продукты.

**`[PRIMARY:<…>]`** — **один** главный трек задачи в треде: какой продукт/репозиторий сейчас в фокусе; не подмешивать контур других продуктов без явной связи.

- После двоеточия обычно **`project-id`** из **твоего** канона (стабильный slug; в полном каноне его обычно сопровождают карточки под `knowledge/work/projects/…`).
- **Алиасы** к `project-id` (короткие коды для чата) — **опционально**; если используешь, держи **локальную** таблицу «маркер → канон», чтобы агент и MCP одинаково нормализовали. В материалах, которые ты отдаёшь наружу как «истину», надёжнее сразу **канонический** id.

**`[SCOPE:<…>]`** — какой **глобальный slice** L1 брать для hot-context и инструментов (**`active_scope`** в MCP), когда на машине **несколько** несводимых к одному дереву контекстов (разные корни репозиториев, разные организации файлов канона).

- Scope — **не** то же самое, что `PRIMARY`: первый задаёт «в какой *вселенной* воркспейса мы», второй — «какой *продукт* сейчас в фокусе».
- Конкретные имена slice и алиасы к ним **ты** выбираешь под свою среду и фиксируешь там же, где дефолт по пути (**например** секция `workspace-scope-map-v1` в hot-заметках — у автора канона она свойственна конкретным дискам; у тебя будет **другая** карта и другие строки идентификаторов).

**Приоритет резолва (шаблон):** явный маркер в сообщении (**`[PRIMARY:…]`**, **`[SCOPE:…]`**) **выше**, чем автодефолт по карте установки; автодефолт **выше**, чем голая эвристика «путь к файлу в чате» (и эвристика **не должна** молча отменять недавний маркер в том же треде).

**Инструменты:** при необходимости MCP получает **`active_scope`** отдельно от workspace path; **`route_context`** типично смотрит **hot** `agent-notes.md`, а playbook и карточки нужно **`read_knowledge_file`**.

Развёрнутые примеры оформления и привычки мультирепо: **`worlds/workspace-context/playbook-multi-project-context-v1.md`** (в т.ч. §6c — жизненный цикл `scope`). Полный текст **`project-switch-protocol-v1`** и карта **`workspace-scope-map-v1`** в hot **`agent-notes.md`** у автора канона лежат **ниже первого `<!-- public-cut -->`** и в **kb-public не входят**; для публичного зеркала опирайся на плейбук и **`kb-one-pager-structure-and-protocols-v1.md`**.

---

## Публикация и границы

- Публичный контур ≠ весь `knowledge/`: у автора канона список исключений — **`knowledge/public-kb.ignore`** (префиксы вроде **`work/`**, **`personal/`**, служебные имена); в архив kb-public они **не попадают**. Дополнительно не копируются файлы с пометкой **«НЕ ПУБЛИКОВАТЬ»** в первой строке. Полный перечень правил — **`PUBLISHING.md`** (входит в kb-public); внутренний runbook пуша — под **`work/`** (в kb-public не входит).
- **`knowledge/worlds/`** в kb-public **по умолчанию** (**любой** `<slug>/`). При создании или правке **любого** мира, fundamentals и строк роутера агент **обязан** вычищать непубличную operationalку, внутренние scope/бренды (кроме общеизвестных вендоров), ссылки на **`work/`** — см. **`worlds/knowledge-engineering/playbook-kb-world-public-authoring-v1.md`** (playbook общий для всех миров).
- **`agent-notes.md`:** в публичную сборку попадает только текст **до** **`<!-- public-cut -->`**; всё ниже — как частный/оперативный hot-слой при экспорте.

---

## Куда дальше (одна строка на файл)

| Нужно | Файл |
|--------|------|
| Анти-OOM обзор | `SHOWCASE.md` |
| Роутер: карта доменов, порядок | `index-knowledge-router-v1.md` |
| Safety Checks (контекст, scope, давление, POST, приватность) | `index-knowledge-router-safety-v1.md` |
| Сопровождение индекса роутера (`router-*`, сплит, kb-public) — **не** свежесть kb | `index-knowledge-router-maintenance-v1.md` § Maintenance Rule |
| L0 и агент до выбора домена (операционный базис роутера) | `router-operational-baseline-v1.md` |
| Триггеры по темам | `index-knowledge-router-supplement-v1.md` |
| Мультипроект + куда писать заметки | `worlds/workspace-context/playbook-multi-project-context-v1.md` |
| Память агента, fuzzy-запросы | `agent-memory-and-operating-principles-v1.md` |
| Целостность под давлением | `domains/agent-operations/playbook-integrity-under-pressure-v1.md` |
| Ты **держишь полный репозиторий канона** (author или fork): как собирается kb-public | **`PUBLISHING.md`** (входит в kb-public); **`public-kb.ignore`** и runbook пуша — только в полном каноне (`public-kb.ignore` в zip **не** кладётся по дизайну списка исключений) |
| Полный канон: соглашение `work/projects/<scope>/…` | `work/projects/README.md` (в kb-public **нет**) |
| Mixed worlds, `transfer_boundary`, поля `world:` | `worlds/knowledge-engineering/kb-knowledge-engineering-mixed-worlds-rules-v1.md` |
| Свежесть kb: fundamentals / operational / evidence, `Проверено:`, стек или любой домен | `worlds/knowledge-engineering/playbook-kb-operational-freshness-v1.md` (+ hot `kb-operational-freshness-v1` в agent-notes) |
| Любой мир / fundamentals / правка `worlds/<slug>/` под kb-public | `worlds/knowledge-engineering/playbook-kb-world-public-authoring-v1.md` |
| Протоколы и сущности (one-pager для wiki) | `kb-protocols-and-entities-one-pager-v1.md` |

