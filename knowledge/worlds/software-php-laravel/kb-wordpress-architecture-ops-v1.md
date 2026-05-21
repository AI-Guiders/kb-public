# WordPress — архитектура и операции (ядро, темы, плагины)

**Назначение:** опорная карта **WordPress как CMS/платформы** для агентов и разработчиков: жизненный цикл запроса, расширяемость, данные, обновления и базовая безопасность. Мир `software.wordpress`. Не руководство по дизайну тем.

**Порядок:** `status-php-laravel-v1.md` → `playbook-php-v1.md` (Composer только если Bedrock/roots; иначе авто-загрузчик плагинов) → этот файл. Нативный PHP — `kb-php-*` при низкоуровневых багах.

---

### 1. Ядро и жизненный цикл

- **Fact:** запрос обрабатывается через bootstrap ядра → парсинг URL → query → шаблон (theme); плагины подключаются по порядку загрузки и хуков.
- **Heuristic:** «ничего не срабатывает» — проверить **приоритет хука**, отключение плагинов, fatal в `debug.log`.
- **Confidence:** high

---

### 2. Хуки: actions и filters

- **Fact:** **do_action** / **add_action** — побочные эффекты; **apply_filters** / **add_filter** — трансформация данных. Имена хуков — контракт между ядром, темой и плагинами.
- **Heuristic:** тяжёлую логику не вешать на `init` с приоритетом по умолчанию без нужды; избегать N запросов к БД из каждого filter callback.
- **First adoption task:** документировать кастомные хуки плагина (имя, когда, аргументы).

---

### 3. Темы и плагины

- **Fact:** тема — presentation + `functions.php`; плагины — изолированная функциональность. Child theme — способ безопасно переопределять родительскую тему.
- **Heuristic:** правки ядра и чужих плагинов напрямую в `wp-content` — антипаттерн; использовать hooks, child theme, must-use plugins по политике.

---

### 4. Данные: wpdb, CPT, таксономии

- **Fact:** глобальный объект **wpdb** для SQL (экранирование через prepared-подобные методы); Custom Post Types и taxonomies регистрируются на `init`.
- **Heuristic:** сырые запросы без подготовки — SQLi-риск; сравнить с `kb-php-data-persistence-v1.md`.
- **Confidence:** medium

---

### 5. Пользователи, роли, capabilities

- **Fact:** модель прав — **roles + capabilities**; проверки через `current_user_can` и т.п.
- **Heuristic:** «админ всё может» в кастомном коде — дыра; явные capability checks на опасных действиях.

---

### 6. Обновления и окружения

- **Fact:** обновления ядра/плагинов/тем — через админку или WP-CLI; несовместимости после мажора PHP — типичный класс инцидентов.
- **Heuristic:** staging + бэкап БД/файлов до обновления; для продакшена — отключение редактора файлов в админке.

---

### 7. Безопасность (baseline)

- **Fact:** ключи и соли в `wp-config.php`; ограничение login rate; права на файлы; HTTPS для админки.
- **Heuristic:** известные уязвимости в популярных плагинах — держать авто-обновления или мониторинг CVE.
- **Transfer_boundary:** не заменяет пентест; см. OWASP.

---

### 8. Bedrock / Composer (кратко)

- **Fact:** **Roots Bedrock** и аналоги переносят конфиг в `.env`, структуру каталогов и Composer для ядра/плагинов — тогда `composer.lock` обязателен в VCS.
- **Heuristic:** смешение «классического» WP и Bedrock в одной голове — путаница путей; уточнять у проекта.

---

## Registry card (template-knowledge-card-v1)

### Provenance
- source_refs: `https://developer.wordpress.org/`; обобщение 2026-03-01
- created_at: 2026-03-01
- updated_at: 2026-03-01
- author: agent-notes KB maintainer

### Metadata
- card_id: KC-2026-03-01-WP-OPS
- world: software.wordpress
- layer: world
- tags: wordpress; hooks; plugins; themes; security
- status: active

### Epistemic Linkage
- epistemic_basis: fact + inference
- evidence_type: official developer docs
- confidence: medium
- uncertainty: версия ядра и контриб-модуля
- falsification_trigger: крупные архитектурные изменения в будущих мажорах WP
- transfer_boundary: не Laravel/Symfony full stack

### Core Unit
- context: плагин, тема, инцидент после обновления
- signal: «какой хук», «почему 500 в админке»
- action: hooks + лог + версии
- outcome: предсказуемые расширения без правок ядра
- lesson: WP — событийная модель; сначала хук, потом код

### Operationalization
- first_adoption_task: версия WP + список активных плагинов в README
- validation_check: staging clone + smoke админки
- success_criterion: обновления по чек-листу
- rollback_or_mitigation: бэкап + откат плагина

### Lifecycle
- supersedes: —
- superseded_by: —
- deprecation_reason: —
