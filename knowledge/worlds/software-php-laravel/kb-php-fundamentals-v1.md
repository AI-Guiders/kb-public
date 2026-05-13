# PHP 8.4+ — фундаментальный слой (рантайм и язык)

**Назначение:** опорная карта PHP как **рантайма** для ветки **8.4+** (и соседних 8.x): версии, SAPI, OPcache, типизация, релиз 8.4, Composer, безопасность, JIT/GC/preload, FPM, расширения. Слой **L1 world** (миру `software.php`).

**Полный фундаментальный проход по миру PHP:** `index-knowledge-php-cluster-v1.md` → при необходимости **`kb-php-versions-and-evolution-v1.md`** (легаси 5/7, хронология фич) → этот файл → `kb-php-language-semantics-v1.md` → `kb-php-web-sessions-io-v1.md` → `kb-php-data-persistence-v1.md` → `kb-php-tooling-quality-v1.md`. Laravel — отдельно: `kb-laravel-fundamentals-v1.md`.

**Порядок загрузки (memory-architecture):** `status-php-laravel-v1.md` → `playbook-php-v1.md` → точечный kb (или кластер по карте).

---

### 1. Ветка PHP 8.x и позиция 8.4

- **Fact:** PHP 8.4 выпущен **21.11.2024** (официальный анонс php.net/releases/8.4). Ветка 8.x — текущая линия развития языка; для новых проектов целесообразно оставаться на поддерживаемой минорной версии (8.3/8.4/8.5 по мере выхода патчей).
- **Heuristic:** в любом обсуждении называть **точную минорную версию** (`8.4.x`) и окружение (CLI / php-fpm / встроенный сервер); не смешивать с PHP 7.x или «просто PHP» без версии.
- **First adoption task:** зафиксировать в репозитории `composer.json` → `require.php` и при необходимости `config.platform.php`, чтобы CI и локальная среда совпадали с production.
- **Success criterion:** нет расхождений «локально 8.3, прод 8.4» без явной политики; обновления патчей запланированы.
- **Confidence:** high

---

### 2. Режимы исполнения и Opcache

- **Fact:** типичные SAPI: **CLI** (скрипты, Artisan, cron), **php-fpm** / mod_php (веб), реже embed. **OPcache** кеширует байткод и сильно влияет на latency/throughput веб-приложений; в CLI по умолчанию часто отключён или ограничен.
- **Heuristic:** диагностику «тормозит прод» разделять: веб (OPcache, fpm pool, autoload) vs CLI (память, I/O).
- **First adoption task:** для production-веба проверить включение OPcache и политику revalidate; для деплоя — сброс/перезапуск воркеров при выкладке.
- **Success criterion:** понятная матрица «среда → SAPI → что смотреть в первую очередь».
- **Confidence:** high

---

### 3. Строгость типов и модель языка (8.x)

- **Fact:** в PHP 8.x усилена типизация: `TypeError` на несовместимых типах, union/intersection types, `readonly`, `enum` (с 8.1), атрибуты; `strict_types=1` задаёт строгую семантику для скаляров в пользовательском коде.
- **Heuristic:** новый код в критичных границах (public API, интеграции) — с явными типами и по возможности `declare(strict_types=1)` в модулях; легаси трогать точечно.
- **First adoption task:** для публичных пакетов описать в README политику strict_types и уровень PHPStan/Psalm.
- **Success criterion:** меньше молчаливых приведений типов на границах системы.
- **Confidence:** high

---

### 4. Поверхность PHP 8.4 (язык и стандартная библиотека)

- **Fact (основные темы релиза):** property hooks; asymmetric visibility; lazy objects через Reflection; `array_find`, `array_find_key`, `array_any`, `array_all`; mbstring (`mb_trim` и др.); DateTime микросекунды / `createFromTimestamp`; `#[Deprecated]`; PCRE2 и изменения regex; bcrypt default cost **10→12**; `exit`/`die` как функции; libcurl **≥7.61.0**. Источники: php.net/releases/8.4, php.watch/versions/8.4.
- **Heuristic:** при миграции 8.3→8.4 — тесты, статанализ, deprecations; отдельно **пароли** и **regex**.
- **First adoption task:** CI на PHP 8.4 + `composer validate`.
- **Success criterion:** нет сюрпризов от bcrypt/PCRE/deprecations.
- **Confidence:** high

---

### 5. Composer и зависимости

- **Fact:** **Composer** — менеджер зависимостей; `composer.lock` для приложений; `require.php` — минимальная версия PHP; `replace`, `conflict`, `provide` влияют на разрешение.
- **Heuristic:** `composer audit` в CI; private packages — репозитории в `repositories`, не коммитить токены.
- **First adoption task:** `composer install --no-dev` в артефакте деплоя.
- **Success criterion:** воспроизводимые билды.
- **Confidence:** high

---

### 6. Безопасность и эксплуатация (минимум)

- **Fact:** прод: без stack trace пользователю; сессии/cookie — secure flags; патчи PHP по каналу ОС/образа.
- **Heuristic:** валидация входа до логики; OWASP Top 10 для веба — вне этого файла, но baseline здесь согласован.
- **First adoption task:** чек-лист: `display_errors=Off`, секреты в env, отдельный пользователь для fpm.
- **Success criterion:** нет утечек трасс; секреты не в git.
- **Confidence:** high

---

### 7. JIT (OPcache JIT) — когда имеет смысл

- **Fact:** JIT компилирует горячий opcode в нативный код; выигрыш **зависит от нагрузки** (CPU-bound вычисления в PHP) и может быть незначителен для типичного I/O-bound веба.
- **Heuristic:** бенчмаркировать с реалистичным профилем; не включать «на удачу» без измерений; следить за совместимостью расширений.
- **First adoption task:** сравнить RPS/latency до/после на стейдже для **своего** кода.
- **Confidence:** medium

---

### 8. Сборка мусора и циклы ссылок

- **Fact:** refcount + циклический GC; деструкторы и циклы могут откладывать очистку; большие графы объектов — пики памяти.
- **Heuristic:** долгоживущие worker’ы (queue consumer) — периодически сбрасывать состояние или рестарт по политике; не хранить гигантские деревья в памяти без нужды.
- **Confidence:** medium

---

### 9. Preloading (`opcache.preload`)

- **Fact:** preloading загружает указанный PHP-скрипт при старте воркера, прогревая классы в OPcache; требует корректного **preload-скрипта** и осознанного порядка зависимостей.
- **Heuristic:** полезно на крупных фреймворках; при обновлении кода — перезапуск fpm; ошибка в preload ломает старт воркера.
- **Confidence:** medium

---

### 10. Расширения: типичный набор для веба

- **Fact:** часто нужны: `openssl`, `mbstring`, `intl`, `pdo` + драйвер БД, `json`, `curl`, `zip`, `xml`/`dom` (интеграции); отсутствие ext ломает `composer install` на `ext-*` требованиях.
- **Heuristic:** в `composer.json` явно `ext-*` в `require`; Docker-образы — официальные или с документированным списком ext.
- **Confidence:** high

---

### 11. php-fpm: пулы и наблюдаемость

- **Fact:** `pm` (static/dynamic/ondemand), `pm.max_children`, `request_terminate_timeout`, `slowlog` — основные рычаги стабильности; нехватка воркеров → очередь запросов; утечки → исчерпание пула.
- **Heuristic:** мониторить `listen queue`, время ответа; slowlog для запросов > порога.
- **Confidence:** high

---

### 12. Лимиты `php.ini` (память, время, загрузка)

- **Fact:** `memory_limit`, `max_execution_time`, `max_input_time`, `upload_max_filesize`, `post_max_size` влияют на веб и CLI по-разному; CLI часто `max_execution_time=0`.
- **Heuristic:** согласовать с reverse proxy (таймауты nginx) и с UX больших upload; не завышать лимиты «на всякий случай» без мониторинга.
- **Confidence:** high

---

### 13. Веб-сервер vs встроенный `php -S`

- **Fact:** прод — nginx/apache + fpm (или unit, frankenphp и т.д.); `php -S` только для разработки.
- **Heuristic:** не воспроизводить security/perf поведение прода на встроенном сервере.
- **Confidence:** high

---

### 14. Reflection и метапрограммирование

- **Fact:** Reflection API инспектирует классы/атрибуты; **lazy objects** (8.4) завязаны на reflection; DI-контейнеры и сериализаторы используют reflection intensively.
- **Heuristic:** кешировать результаты рефлексии на горячем пути; не строить бизнес-логику на «магии» без тестов.
- **Confidence:** medium

---

## Registry card (template-knowledge-card-v1)

### Provenance (происхождение)
- source_refs: `https://www.php.net/releases/8.4/en.php`; `https://php.watch/versions/8.4`; manual opcache/preload/JIT; KB 2026-02-28, обновлено 2026-03-01 (полный проход).
- created_at: 2026-02-28
- updated_at: 2026-03-01
- author: agent-notes KB maintainer

### Metadata
- card_id: KC-2026-02-28-PHP-84-L1
- world: software.php
- layer: world
- tags: php; php-8.4; runtime; composer; opcache; fpm; jit
- status: active

### Epistemic Linkage
- epistemic_basis: fact + inference
- evidence_type: official release notes + manual
- confidence: high
- uncertainty: JIT/preload выигрыш — только измерениями на своём коде
- falsification_trigger: смена supported versions на php.net
- transfer_boundary: не переносить на PHP 7.x без проверки

### Core Unit
- context: версия, SAPI, прод-поведение, миграция 8.3→8.4
- signal: perf, opcache, fpm, лимиты ini
- action: §1–14 + кластер `index-knowledge-php-cluster-v1.md`
- outcome: согласованная платформа PHP
- lesson: рантайм = версия + SAPI + ini + расширения

### Operationalization
- first_adoption_task: зафиксировать образ PHP и список ext
- validation_check: `php -i` в CI артефакте; health endpoint
- success_criterion: предсказуемое поведение под нагрузкой
- rollback_or_mitigation: откат образа; отключение preload/JIT

### Lifecycle
- supersedes: —
- superseded_by: —
- deprecation_reason: —