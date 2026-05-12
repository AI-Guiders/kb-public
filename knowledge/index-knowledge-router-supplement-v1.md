# Knowledge Router — Supplement (detailed domain routes) v1

**Роль:** триггеры «когда грузить какой playbook/kb» по темам — все секции `<!-- section:router-* -->` и `learn-basics-when-stuck-router`. Раньше жили в `index-knowledge-router-v1.md` сразу после Context Budget.

**Точка входа:** `index-knowledge-router-v1.md` — Baseline, Domain Entry Map, Safety Checks, Maintenance. Этот файл подключают, когда нужен **доменный** маршрут по запросу (или по `route_context`).

**Редактирование:** `upsert_knowledge_section` с `file_path: index-knowledge-router-supplement-v1.md` и прежними `section_id` (`router-logic`, …).

**Обратная совместимость:** в старых документах встречается «секция `router-…` в `index-knowledge-router-v1.md`» — смысл тот же; физически секции перенесены **сюда** (рефакторинг v2 split).

---

<!-- section:router-logic -->

## Logic: everyday and formal (evidence base)

- **При запросах о логике, аргументации, кванторах («все/везде» vs «хотя бы один»), необходимости и достаточности, типичных ошибках в рассуждениях:** загружать `knowledge/kb-logic-everyday-and-formal-evidence-v1.md` — обычная логика (кванторы в речи, условие, необходимость/достаточность), связка с формальной (∀, ∃, импликация), evidence-кейсы из практики, связь с scope-disambiguation и эпистемией. Операционная секция scope-disambiguation-all-everywhere-v1 в agent-notes опирается на этот документ как на логический фундамент.
<!-- /section:router-logic -->

<!-- section:router-value-utility -->


## Value / Utility / Underdetermination (evidence base)

- **При запросах о критериях полезности, ценности, сравнении вариантов или обосновании оценочных суждений:** загружать `knowledge/kb-utility-value-underdetermination-evidence-v1.md` — обзор по теории полезности (EU, критика), теории ценности (axiology, good for / attributive, плюрализм), несоизмеримости (incommensurability, parity), теореме Эрроу. Операционный принцип «полезность недоопределена» в `agent-memory-and-operating-principles-v1.md` опирается на этот evidence-based документ.
<!-- /section:router-value-utility -->

<!-- section:router-bci-medicine -->


## BCI / Medicine (evidence base)

- **При запросах о BCI (интерфейсы мозг–компьютер), нейрореабилитации (инсульт, SCI, locked-in, речь при параличе, ДЦП, нейрофидбек) или evidence-based по этим направлениям медицины:** загружать `knowledge/kb-bci-evidence-based-medicine-v1.md` — уровни доказательности, мета-анализы/RCT, ссылки на Cochrane/PubMed/PMC/NEJM/Nature; сводная таблица по направлениям. Домен: Medicine (Evidence); status → playbook → kb. Клинические решения — по руководствам и протоколам; документ только навигация.
<!-- /section:router-bci-medicine -->

<!-- section:router-secret-mode -->


## Secret Mode (активатор дисциплинированного режима)

- **При запросах про дисциплинированный режим, «что делаю + зачем», совместную ясность без победы в споре или про активатор для текстового агента:** загружать `secret-mode-prefix-ru.md` (корень репо agent-notes). Расширенный префикс — 6 посылок после «Secret Mode activated»; применим к любому текстовому агенту. Связь с multiworld: тег `secret-mode` в kb-knowledge-engineering-multiworld-rules-v1.md.
<!-- /section:router-secret-mode -->

<!-- section:router-clarification -->


## Clarification: general / vague query

- **При общем или размытом запросе** (нет явного scope, outcome или домена): загружать `knowledge/playbook-clarification-general-query-v1.md` — лестница снятия неопределённости (переформулировка → варианты A/B/C → минимальный безопасный шаг), использование route_context до вопроса, правило одного вопроса. Не загружать несколько доменных веток «на угад»; не сыпать уточняющими вопросами — один вопрос, снимающий максимум измерений.
<!-- /section:router-clarification -->

<!-- section:router-polyamory -->


## Polyamory (reference, culture.global)

- **При запросах о полиамории, полиаморах, согласованной немоногамии (CNM), структурах отношений (иерархия, solo poly, relationship anarchy), этике и терминологии:** загружать `knowledge/kb-polyamory-reference-v1.md` — определения, этический фундамент, типовые структуры, термины (мета, комперсия, NRE, границы, veto), неэтичное поведение, мифы, связь с психологией, книги для углубления. **Мир:** `culture.global`. При переносе в страновой контекст или в психологический/терапевтический контур — через `matrix-culture-routing-v1.md`.
<!-- /section:router-polyamory -->

<!-- section:router-therapy -->


## Therapy / Support boundaries

- **При запросах о терапии, поддерживающем контакте, границах «агент vs терапевт», когда направлять к специалисту, травме, флешбэках, кризисе, психологической первой помощи:** загружать `knowledge/kb-therapy-and-support-boundaries-v1.md` и секцию **agent-supportive-listening-gap-v1** в agent-notes. В документе: терапия vs поддерживающее слушание, признаки кризиса и серьёзных индикаторов, травма-информированный отклик и grounding (вне клиники), PFA-контекст, операционная таблица для агента. Агент не терапевт; может «заполнять пробел» (отражение, признание, без советов); при риске — предложить специалиста или экстренную службу.
<!-- /section:router-therapy -->

<!-- section:router-uncanny-valley -->


## Human perception (psychophysiology): fundamentals → operational

- **При запросах о психофизиологии восприятия, когнитивной нагрузке, усталости и внимании в контексте UX/IDE/агента**, о том, «почему интерфейс бесит без бага», о конкуренции зон экрана за внимание, о прерываниях потока и предсказуемости фидбека: загружать **`knowledge/playbook-human-perception-operational-v1.md`** — чеклисты и мост к HCI/продукту. Фундамент понятий (внимание, рабочая память, нагрузка, стресс, заметность): **`knowledge/kb-human-perception-fundamentals-v1.md`**. **Первоисточники, DOI, таблица «идея → статья»:** **`knowledge/kb-human-perception-scientific-evidence-v1.md`** — при обосновании ревью, споре о цитировании или углублении в научный слой. **Evidence-карточки по первоисточникам (`kb-human-perception-*-evidence-v1`):** `knowledge/kb-human-perception-miller-1956-evidence-v1.md`, `knowledge/kb-human-perception-treisman-gelade-1980-evidence-v1.md` (или по запросу конкретной работы). Карта мира и границы переноса: **`knowledge/worlds/cognition-human-perception/README.md`** (`cognition.human-perception`).
- **Порядок:** `status-human-perception-v1.md` → operational playbook → fundamentals kb → при необходимости **scientific-evidence** kb; затем при узком UI‑вопросе — **HCI** (`playbook-hci-core-v1.md`, при необходимости `kb-hci-usability-and-dialog-rules-v1.md`, `kb-ui-ux-literature-evidence-v1.md`). Не подменять **Psychology** при клинических запросах.
- **Пересечение с CascadeIDE:** метафора кокпита и иерархия внимания — в ADR репозитория (напр. 0021, 0076); KB даёт слой «почему», не дублирует нормативы продукта.
<!-- /section:router-human-perception -->

<!-- section:router-videography -->


## Videography / Cinematography (theory reference)

- **При запросах о теории видеосъёмки, кинематографии, композиции, типах планов (EWS/CU/MCU и др.), правиле 180°/30°, свете (трёхточечный, high/low key), движении камеры (pan, tilt, dolly, tracking), глубине резкости, непрерывном монтаже, broadcast (LUFS/EBU R128, broadcast-safe), кодеках доставки (H.264, ProRes и др.), прикладном видеонаблюдении (CCTV, охранные камеры, размещение, слепые зоны, покрытие, retention, персональные данные):** загружать `knowledge/kb-videography-cinematography-theory-v1.md` — теория + операционный слой (R1–R8 + R9–R12 для surveillance), broadcast, кодеки; прикладное видеонаблюдение — мир **media.video-surveillance** (§13); для планирования съёмки, разбора кадра, проверки доставки/эфира и проектирования систем видеонаблюдения.
<!-- /section:router-videography -->

<!-- section:router-ml -->


## ML (applied, OCR, barcode, QR)

- **При запросах о машинном обучении (парадигмы, supervised/unsupervised, классификация, регрессия), OCR (распознавание текста, Tesseract, препроцессинг, облако vs on-device), распознавании штрихкодов и 2D-кодов (barcode, QR, Data Matrix, UPC, EAN, Code 128, требования к изображению, ML Kit, ZXing):** загружать `knowledge/kb-ml-applied-theory-v1.md` — фундамент ML и прикладные задачи; OCR (пайплайн, препроцессинг, OEM/PSM); 1D/2D коды, типы и выбор решения; операционные правила R1–R7; мир **software.ml-applied**.
<!-- /section:router-ml -->

<!-- section:router-dotnet -->


## .NET runtimes and migration

- **При запросах общего уровня о .NET как платформе (линии .NET Framework vs .NET (Core/5+), TFMs, типы приложений, SDK/CLI‑модель):** загружать:
  - `knowledge/kb-dotnet-fundamentals-v1.md` — фундаментальные понятия о рантаймах, TFM, моделях приложений и границах с нативным кодом;
  - `knowledge/kb-engineering-evidence-v1.md` — секции про C#/.NET 10, диагностику и историю/совместимость .NET Framework 1.0→4.x как слой инженерных фактов/эвиденции.
- **При запросах вида «как выбрать версию .NET/TFM», «как планировать миграцию с .NET Framework», «как запускать базовый диагностический цикл»:** дополнительно загружать `knowledge/kb-dotnet-playbooks-v1.md` — playbook’и DOTNET‑01..03.
- Это **слой платформы/рантайма** в мире engineering; для доменно‑специфичных тем (портал, CA‑симуляции и т.п.) он должен сочетаться с соответствующими областями (portal, simulations).
<!-- /section:router-dotnet -->

<!-- section:router-de-dx -->


## Developer Experience (DE/DX)

- **При запросах о developer experience, DX, DE/DX, эргономике доставки, трение в тулинге, онбординге разработчика, «лёгком пути», lead time / cycle time / change failure rate / MTTR (DORA-ориентир), time-to-first-edit / time-to-first-contribution, малых батчах и обратной связи до merge:** загружать `knowledge/de-dx-playbook.md` — принципы, метрики, формат evidence-based работы.
- **Литература IDE и опыта разработчика** (принципы Osmani, интегрированная среда Smalltalk-80, Boxer/diSessa — не путать с метриками команды из playbook): `knowledge/kb-ide-dx-literature-evidence-v1.md`. Загружать при проектировании **IDE**, инструмента, обосновании «трения», TTC, единого окна, режимов редактора/отладки.
- **Классика UI/UX** (Norman, Nielsen, Shneiderman, Krug): `knowledge/kb-ui-ux-literature-evidence-v1.md` — эвристики и язык ревью интерфейса; пересечение с HCI.
- **Порядок:** при узком вопросе достаточно `de-dx-playbook.md`; при пересечении с циклом кода — добавить **Git** (`playbook-git-workflow-v1.md`), **PR Review** (`playbook-pr-review-v1.md`); при боли в сборке/тестах/отладке — `tooling-debug-playbook.md`; при фокусе на UI/диалоге — **HCI** (`playbook-hci-core-v1.md`, при необходимости `kb-hci-usability-and-dialog-rules-v1.md`, `kb-ui-ux-literature-evidence-v1.md`) и/или `ui-ux-playbook.md`.
- **Продуктовые числовые бюджеты** (latency редактора, acceptance перед релизом конкретного приложения) — не дублировать в KB: держать в ADR/доках репозитория продукта; KB даёт общий слой DX. Для desktop IDE на Avalonia — см. домен **Avalonia UI (CascadeIDE)** в Domain Entry Map.
<!-- /section:router-de-dx -->

<!-- section:router-php-laravel -->


## PHP runtime (8.4+) and Laravel framework

- **Порядок загрузки:** `status -> playbook -> kb` (см. Domain Entry Map — домен **PHP / Laravel**).
- **Полный фундаментальный проход по миру PHP (без фреймворка):** начать с `knowledge/index-knowledge-php-cluster-v1.md` (таблица «вопрос → файл» и порядок из 5 kb); затем по шагам `playbook-php-v1.md` § Full fundamental pass — **не грузить все kb одновременно** без явного запроса.
- **Точечные запросы по PHP:**
  - платформа, версии, OPcache, JIT, preloading, FPM, ini, расширения, Composer, bcrypt/PCRE/8.4 → `knowledge/kb-php-fundamentals-v1.md`;
  - хронология языка с **PHP 5.x/7.x**, миграции мажоров, «с какой версии появилась фича» → `knowledge/kb-php-versions-and-evolution-v1.md`;
  - семантика языка, типы, ООП, enum, ошибки, namespace, `==` vs `===`, опасные API → `knowledge/kb-php-language-semantics-v1.md`;
  - сессии, cookies, суперглобалы, upload, заголовки, потоки → `knowledge/kb-php-web-sessions-io-v1.md`;
  - PDO, SQL, транзакции, миграции без ORM → `knowledge/kb-php-data-persistence-v1.md`;
  - PHPUnit/Pest, PHPStan/Psalm, Rector, Xdebug, CI-матрица → `knowledge/kb-php-tooling-quality-v1.md`.
- **Всегда перед углублением:** `knowledge/status-php-laravel-v1.md` + `knowledge/playbook-php-v1.md`.
- **Laravel — база:** `knowledge/playbook-laravel-v1.md`, затем `knowledge/kb-laravel-fundamentals-v1.md` — **поверх** слоя PHP, не вместо него.
- **Laravel — полный контур (версии 8→12+, first-party пакеты, Sanctum/Passport, Symfony под капотом, Octane/FrankenPHP/RoadRunner/Reverb, Livewire/Filament/Inertia):** `knowledge/index-knowledge-laravel-cluster-v1.md` (таблица «вопрос → kb» и порядок full pass) → **один** целевой `kb-laravel-*` за раз; апгрейды — `kb-laravel-versions-upgrades-v1.md` + официальный Upgrade Guide ветки.
- **Связь:** `kb-engineering-evidence-v1.md` при необходимости общих инженерных фактов; OWASP/внутренние стандарты — для угрозной модели вне этих kb.
- **Смежная экосистема PHP (WordPress, Drupal, Symfony full stack, Composer/Packagist/сторонние пакеты):** `knowledge/index-knowledge-php-adjacent-ecosystem-v1.md` → **один** из `kb-wordpress-architecture-ops-v1.md`, `kb-drupal-architecture-ops-v1.md`, `kb-symfony-framework-fundamentals-v1.md`, `kb-composer-packagist-thirdparty-v1.md`; не смешивать паттерны CMS и фреймворков.
- **Цепочки миров:** `software.php` ↔ `software.laravel` / `software.web-backend`; отдельно `software.wordpress`, `software.drupal`, `software.symfony` — подменять друг друга нельзя.
<!-- /section:router-php-laravel -->

<!-- section:router-javascript -->


## JavaScript / ECMAScript language core

- **Порядок загрузки:** `status -> playbook -> kb` (см. Domain Entry Map — домен **JavaScript (ECMAScript)**). Playbook операционного слоя: **`playbook-javascript-operational-v1.md`** (мост **fundamentals → operational** и контракты CI/репо).
- **Структура:** **fundamentals** — четыре карточки языка по `knowledge/index-knowledge-javascript-cluster-v1.md` § fundamentals; **operational** — `knowledge/kb-javascript-operational-ecosystem-v1.md` § operational (или сразу при чисто npm/CSP/tooling вопросе).
- **Полный проход по миру `software.javascript`:** index § фаза A → фаза B + `playbook-javascript-operational-v1.md` § Full pass — **не грузить все kb одновременно**.
- **Точечные запросы (fundamentals):**
  - редакции ECMA-262, ESM/CommonJS/`import.meta`, транспилятор vs полифилл; **движки и хосты** → `knowledge/kb-javascript-ecmascript-and-modules-v1.md`;
  - принуждения типов, `===`, UTF-16, TDZ, замыкания, функции/стрелки/`this` → `knowledge/kb-javascript-types-coercion-and-scope-v1.md`;
  - прототипы, `class`/private `#`, итерируемость → `knowledge/kb-javascript-objects-prototypes-and-classes-v1.md`;
  - Promises, async/await, микро/макрозадачи, AbortSignal → `knowledge/kb-javascript-async-and-event-loop-v1.md`.
- **Operational:** lockfile/npm/semver, ESLint/бандлеры, тест‑раннеры, CSP/XSS/`eval`, audit → **`knowledge/kb-javascript-operational-ecosystem-v1.md`**. Старый путь `kb-javascript-runtime-tooling-and-security-baseline-v1.md` — только stub с перенаправлением.
- **Перед углублением:** `knowledge/status-javascript-v1.md` + `knowledge/playbook-javascript-operational-v1.md`.
- **TypeScript** — отдельная линия; **не смешивать** с этим кластером без явного указания.
- **RegExp (flavor JS):** `regex-playbook.md` → `kb-regex-flavors-practice-v1.md` § JavaScript.
- **Связь:** `kb-engineering-evidence-v1.md`; DOM/Web API — MDN/платформа, не этот кластер.
<!-- /section:router-javascript -->

<!-- section:router-avalonia-ui -->


## Avalonia UI / Dock (CascadeIDE, desktop .NET)

- **Порядок загрузки:** `status -> playbook -> kb` (см. Domain Entry Map — домен **Avalonia UI (CascadeIDE)**).
- **При запросах об Avalonia, AXAML, MVVM, темах Fluent, `DynamicResource`, Dock.Avalonia, Dock.Model (`DockControl`, документы, tool windows), реализации макета CascadeIDE, ошибках биндингов и стилей, AvaloniaEdit, Markdown.Avalonia в контексте desktop IDE:**
  1. `knowledge/status-avalonia-cascade-ide-ui-v1.md` — версии пакетов и guardrails;
  2. `knowledge/playbook-avalonia-dock-ui-v1.md` — операционные контракты A–F;
  3. `knowledge/kb-avalonia-ui-dock-fundamentals-v1.md` — фундамент (модель UI, Dock vs `DockPanel`, темы, компоновка).
- **Продуктовые правила интерфейса:** дополнительно `playbook-hci-core-v1.md`, `ui-ux-playbook.md`, при необходимости `kb-hci-usability-and-dialog-rules-v1.md`, `kb-ui-ux-literature-evidence-v1.md`.
- **Обоснование принципов IDE/DX (литература):** `kb-ide-dx-literature-evidence-v1.md` (Osmani, Goldberg, diSessa); не заменяет `de-dx-playbook.md` (процесс поставки).
- **Общий .NET frontend (Blazor / сравнение стеков):** `frontend-dotnet-playbook.md`.
- **Карта концепт → разметка** в репозитории приложения: `cascade-ide/docs/ux/concept-to-implementation-map-v1.md` (не дублировать в KB — ссылка).
<!-- /section:router-avalonia-ui -->

<!-- section:router-math-numerics -->


## Math / Numerics (PDE/ODE/IDE, schemes)

- **При запросах о математической постановке задач для симуляции (PDE/ODE/IDE, начальные/граничные условия, выбор тестовых задач):** загружать:
  - `knowledge/kb-math-pde-fundamentals-v1.md` — классы PDE (эллиптические/параболические/гиперболические), heat/wave/Poisson, IC/BC, типы граничных условий, well-posedness;
  - `knowledge/kb-math-ode-ide-fundamentals-v1.md` — ODE, Volterra/Fredholm IE/IDE, когда и зачем использовать интегральные/интегро-дифференциальные формы, высокоуровневая классификация.
- **При запросах о численных схемах и устойчивости (конечные разности, CFL, сходимость, измерение ошибок):** загружать `knowledge/kb-math-numerical-schemes-fundamentals-v1.md` — консистентность/устойчивость/сходимость, CFL-ограничения, стандартные стенсилы и сеточные эксперименты.
- Эти документы — **общий фундамент** для инженерных симуляций (в т.ч. equation→CA→CUDA), не отдельный мир; их следует использовать как слой математики/численного анализа поверх соответствующих доменных миров (engineering, physics, и т.д.).
<!-- /section:router-math-numerics -->

<!-- section:router-equation-ca-cuda-validation -->


## Equation→CA→CUDA / PDE solver validation

- **При запросах о валидации решателей 2D heat, проверке корректности численного решения equation-to-ca-cuda, критериях «прошёл/не прошёл» (нормы ошибки, сходимость, референс):** загружать:
  - `knowledge/kb-pde-solver-validation-fundamentals-v1.md` — что такое валидация PDE-решателя, почему одного скаляра недостаточно, референс и нормы;
  - `knowledge/kb-equation-ca-cuda-validation-evidence-v1.md` — факты и эвристики по референсным задачам, нормам, CFL, воспроизводимости;
  - `knowledge/playbook-equation-ca-cuda-validation-v1.md` — пошаговый контракт базовой валидации (референс, нормы, сходимость, метаданные, критерии прохождения).
- Дополнительно при необходимости: `knowledge/kb-math-numerical-schemes-fundamentals-v1.md` (уже в router-math-numerics). Слой валидации для проекта equation-to-ca-cuda; решения о корректности — по критериям из KB, не по одному числу на выходе.
<!-- /section:router-equation-ca-cuda-validation -->

<!-- section:router-warehouse -->


## Warehouse (barcode video, marketplace labels)

- Порядок загрузки: status → playbook → kb. **При запросах о требованиях маркетплейсов (Ozon, Wildberries, Яндекс Маркет) к этикеткам, размерам, штрихкодам и маркировке:** загружать `knowledge/kb-warehouse-marketplace-labels-v1.md` — размеры, dpi, форматы (GS1-128, EAN, Data Matrix), Честный знак. **При запросах о видеозахвате штрихкодов/QR на складе, настройке камер и NVR под читаемость кода на записи:** загружать `knowledge/kb-warehouse-barcode-video-v1.md` — пиксели на модуль (QR 3–3,5, штрихкод ≥2), разрешение, FOV, освещение, кодек, глубина резкости, две зоны съёмки. Для запросов о конкретных моделях камер (Hikvision DS-2CD2083G2-IU и др.), даташитах и evidence-расчёте px/модуль — дополнительно **L1 on demand:** `knowledge/kb-warehouse-barcode-video-models-l1-v1.md`. По запросу, затрагивающему и этикетки, и видео — оба основных файла. Мир **logistics.warehouse**.
<!-- /section:router-warehouse -->

<!-- section:router-music -->


## Music

- **При запросах о музыке (теория, нотация, гармония, физика звука, психоакустика, строи, незападная):** загружать `knowledge/playbook-music-v1.md` для маршрутизации; затем по теме запроса — соответствующий kb: **fundamentals** (нотация, pitch, ритм, лады, гармония, транспонирование) → `kb-music-theory-fundamentals-v1.md`; **физика/психоакустика** (волны, спектр, Фурье, громкость, тембр, маскировка) → `kb-music-acoustics-v1.md`; **строи, темперации, коммы, JI** → `kb-music-temperaments-math-v1.md`; **макам, рага, микротоновость** → `kb-music-non-western-v1.md`. Мир **arts.music**.
<!-- /section:router-music -->

<!-- section:router-regex -->


## Regex (кластер MRE3 / Friedl + операционный контракт)

- **При запросах о регулярных выражениях (паттерны, диалекты, производительность, .NET/JS/Java/PCRE):** сначала операционный контракт — `knowledge/regex-playbook.md` (дизайн, диалекты, тестирование, безопасность).
- **Точка входа кластера:** `knowledge/index-knowledge-regex-cluster-v1.md` — порядок чтения и таблица «задача → файл».
- **По типу вопроса (не грузить все kb сразу):** шпаргалка `kb-regex-quickref-v1.md`; синтаксис и утверждения `kb-regex-syntax-features-v1.md`; Unicode и границы `kb-regex-unicode-boundaries-v1.md`; движки и катастрофический backtracking `kb-regex-engines-efficiency-v1.md`; API языков и практика `kb-regex-flavors-practice-v1.md`; соответствие глав русскоязычного PDF издания книги Friedl — `kb-regex-mre3-ru-chapter-map-v1.md`.
- **Порядок загрузки:** `regex-playbook.md` → `index-knowledge-regex-cluster-v1.md` → один целевой `kb-regex-*` по вопросу.
<!-- /section:router-regex -->

<!-- section:router-sysadmin-ops -->


## Sysadmin: Zabbix, Grafana, networks

- **При запросах по Zabbix, Grafana, мониторингу и алертингу, дашбордам и источникам данных, основам сетей (OSI, VLAN, диагностика), выбору инструмента («мониторинг vs визуализация», аналоги Zabbix/Grafana):** загружать `knowledge/domain-index-v1.md` (роутер доменов и ключевые слова), при сравнении задач и инструментов — `knowledge/tool-purpose-and-books-v1.md`, затем соответствующий `playbook-*` и `kb-*-reference-v1.md` из таблицы домена. Материалы доменов zabbix-monitoring, grafana, network-fundamentals лежат в корне `knowledge/`. Домены 1С, nginx, backup, incidents, SSH, Wireshark — playbook в `knowledge/work/` (см. таблицу в `domain-index-v1.md`).
<!-- /section:router-sysadmin-ops -->

<!-- section:learn-basics-when-stuck-router -->


## Learn basics when stuck (agent discipline)

- **При повторяющихся ошибках по одной задаче (CHAT_ID_INVALID, 404, неверный формат и т.п.), неясной семантике API/домена или фактическом угадывании параметров:** загружать `knowledge/playbook-learn-basics-when-stuck-v1.md` — правило: остановиться, изучить матчасть (официальная документация, KB, Context7/MCP), при необходимости зафиксировать факты в KB, затем продолжать. Не метаться trial-and-error.
<!-- /section:learn-basics-when-stuck-router -->

<!-- section:router-agent-autonomy -->


## Agent autonomy without mentor (external world)

- **При подготовке к самостоятельной работе без постоянного «учителя в контуре», при расширении scope за привычную среду (внешние API, чужие репо, неоднозначные источники), при вопросах о доверии к процессу без человека или о границах самостоятельных решений:** загружать `knowledge/playbook-agent-autonomy-and-routing-v1.md` — инварианты (Integrity POST, baseline), четыре режима (действовать / уточнить / отказаться / остановиться), transfer boundaries, эпистемика, связь с `playbook-learn-basics-when-stuck-v1.md`, `playbook-multi-project-context-v1.md`, `playbook-clarification-general-query-v1.md`. Не путать автономию с угадыванием в незнакомом домене.
<!-- /section:router-agent-autonomy -->

<!-- section:router-multi-project-context -->


## Multi-project workspace / rational context

- **При запросах о множестве репозиториев, выборе проекта, смешении контекстов между MCP и IDE, рациональном использовании памяти между проектами, «куда смотреть» в домашнем workspace, заведении нового workspace `scope`:** загружать `knowledge/playbook-multi-project-context-v1.md` — первичный `project-id`, порядок навигации (хаб → карточка `door-to-singularity` → README репо), §6c (жизненный цикл `scope`), что не подмешивать без зависимости, кластеры связанных репо, граница hot-context и длинного KB. Не перечислять все проекты «на всякий случай». Явное переключение primary/scope в чате — маркеры `[PRIMARY:…]`, `[SCOPE:…]`; полный текст протокола у автора канона может быть только в hot `agent-notes.md` ниже `<!-- public-cut -->` — тогда опираться на этот плейбук и `kb-one-pager-structure-and-protocols-v1.md`.
<!-- /section:router-multi-project-context -->

<!-- section:router-session-summary -->


## Длинная сессия / итоги / читаемый экспорт чата

- **При разросшемся треде; по запросу пользователя подвести итоги / зафиксировать договорённости; по инициативе агента предложить подвести итоги** (длинный тред, риск потери нити, выгодно зафиксировать); **или** когда нужен читаемый экспорт вместо непрозрачного сжатия контекста: загружать `knowledge/playbook-session-summary-and-chat-export-v1.md`; операционный принцип — `knowledge/agent-memory-and-operating-principles-v1.md` §9. При работе с сырым `*.jsonl` Cursor — `tools/Export-CursorJsonlTranscript.ps1` (см. `tools/README.md`).
<!-- /section:router-session-summary -->

<!-- section:router-kb-mcp-access -->


## KB: доступ через MCP (agent-notes)

- **При сбоях чтения `knowledge/` через agent-notes MCP, вопросах про `AGENT_NOTES_CANON_PATH`, после Reload Window, рассинхроне «MCP подключён» vs «агент не видит тулы», или когда нужно явно зафиксировать поведение «контур чтения канона недоступен»:** загружать `knowledge/runbook-kb-mcp-access-v1.md`. Не дублирует L0 baseline; только операционный слой чтения файлов канона. Связь: `SHOWCASE.md`, `agent-memory-and-operating-principles-v1.md` §7a, `playbook-multi-project-context-v1.md` §6–§6c.
<!-- /section:router-kb-mcp-access -->

<!-- section:router-captain-parallel-agents -->


## Cursor: капитан и параллельные субагенты (Task)

- **При координации нескольких субагентов (Task), параллельной разведке по репозиторию, декомпозиции крупной задачи на воркеров в Cursor:** загружать `knowledge/playbook-captain-parallel-agents-v1.md` — роли капитан/воркер, бриф, антипаттерны; область — любой проект/workspace, не один продукт (в плейбуке есть пример Cascade IDE). Связь: `playbook-multi-project-context-v1.md` (primary/scope), `agent-memory-and-operating-principles-v1.md`.
<!-- /section:router-captain-parallel-agents -->
