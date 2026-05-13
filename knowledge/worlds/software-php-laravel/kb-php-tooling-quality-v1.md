# PHP — инструменты, качество, CI (фундаментальный проход)

**Назначение:** слой **PHPUnit/Pest, статанализ, форматирование, Rector, Xdebug, CI-матрица**. Мир **`software.php`**.

---

### 1. Composer как центр задач

- **Fact:** `composer.json` → секция `scripts` (`test`, `phpstan`, `cs-fix`); `composer exec` для бинарей из `vendor/bin`.
- **Heuristic:** один вход «проверить всё» в CI: `composer test` агрегирует подзадачи; документировать в README.

---

### 2. PHPUnit: структура

- **Fact:** тесты — классы с `TestCase`, методы `test*` или `@test`; фикстуры `setUp`/`tearDown`; data providers.
- **Heuristic:** изоляция тестов — без зависимости от порядка; моки для внешних HTTP/БД или testcontainers на уровне проекта.

---

### 3. Pest (опционально)

- **Fact:** Pest — слой над PHPUnit с функциональным стилем `test()`, `expect()`.
- **Heuristic:** выбрать один стиль на репозиторий или явно разделить подпроекты — не смешивать хаотично.

---

### 4. PHPStan / Larastan

- **Fact:** **PHPStan** — уровни 0–9 (строгость растёт); **Larastan** — расширения для Laravel.
- **Heuristic:** новый проект — целевой уровень (например 6–8) с baseline постепенного снижения долга; не «включить max» без плана.

---

### 5. Psalm

- **Fact:** альтернатива/дополнение PHPStan; свои плагины и тот же класс задач.
- **Heuristic:** не держать оба без причины — один основной статанализатор в CI.

---

### 6. Code style: PHPCS / PHP-CS-Fixer

- **Fact:** PHPCS проверяет стиль; PHP-CS-Fixer автофиксит; PSR-12 распространённый baseline.
- **Heuristic:** фиксер в pre-commit или CI с `--dry-run` для проверки; единый конфиг в репо.

---

### 7. Rector и миграции версий PHP

- **Fact:** **Rector** применяет AST-трансформации для апгрейда синтаксиса/типов между версиями PHP и фреймворков.
- **Heuristic:** прогон на ветке + полный test suite; коммиты небольшими наборами правил (sets), не «всё сразу».

---

### 8. Xdebug: режимы

- **Fact:** `xdebug.mode=debug,develop,coverage,trace` и т.д.; влияет на производительность.
- **Heuristic:** в проде Xdebug обычно выключен; coverage в CI — отдельный job или PCOV как альтернатива.

---

### 9. Матрица версий в CI

- **Fact:** тестировать минимальную поддерживаемую PHP и одну «latest»; для библиотек — широкая матрица.
- **Heuristic:** совпадение с `require.php` в composer; не тестировать версии ниже заявленной поддержки.

---

### 10. Линтинг депрекations

- **Fact:** `E_DEPRECATED` в логах CI при `error_reporting=E_ALL`.
- **Heuristic:** ломать билд на новых deprecations в основной ветке при политике «чистый forward».

---

## Registry card (template-knowledge-card-v1)

### Provenance
- source_refs: документация PHPUnit, PHPStan, Rector, xdebug.org; KB 2026-03-01.
- created_at: 2026-03-01
- updated_at: 2026-03-01

### Metadata
- card_id: KC-2026-03-01-PHP-TOOL-L1
- world: software.php
- layer: world
- tags: php; phpunit; phpstan; rector; xdebug; ci
- status: active

### Epistemic Linkage
- epistemic_basis: fact + inference
- confidence: high
- falsification_trigger: смена major версий инструментов — перепроверить команды

### Core Unit
- context: настройка качества в PHP-проекте, апгрейд версии языка
- signal: «что запускать в CI», «как автоматизировать миграцию синтаксиса»
- action: матрица инструментов §1–10
- lesson: статанализ и тесты — контракт команды, не опция

### Operationalization
- first_adoption_task: composer scripts + один job CI
- validation_check: green build на min/max PHP
- success_criterion: новый код не понижает уровень строгости без ADR

### Lifecycle
- supersedes: —
- superseded_by: —
- deprecation_reason: —