# Laravel — версии, требования PHP, апгрейды (мажоры 8–12+)

**Назначение:** опорная **матрица мажоров** и дисциплина апгрейда без путаницы между ветками документации. Мир `software.laravel`. Детали «как писать код» — в `kb-laravel-fundamentals-v1.md`.

**Порядок загрузки:** `status-php-laravel-v1.md` → `playbook-laravel-v1.md` → этот файл. PHP-рантайм — `playbook-php-v1.md` + `kb-php-*`.

---

### 1. Сводная матрица (ориентир; сверять с официальным release каждой ветки)

| Laravel (мажор) | Минимальный PHP (типично) | Примечание |
|-----------------|---------------------------|------------|
| 8.x | 7.3 → позже 8.0 | **EOL** для новых проектов; только наследие |
| 9.x | 8.0+ | Symfony 6; EOL для greenfield |
| 10.x | 8.1+ | Долгая ветка для многих продов |
| 11.x | 8.2+ | Упрощённый skeleton, минимум default файлов |
| 12.x | 8.2–8.5 (диапазон по docs 12.x) | Актуальный ориентир KB |

- **Fact:** точные диапазоны и исключения — в `https://laravel.com/docs/{X}.x/releases` и в `composer.json` пакета `laravel/framework`.
- **Heuristic:** не переносить примеры кода из docs **12.x** на приложение **10.x** без проверки синтаксиса и changelog.
- **Confidence:** medium (версии PHP меняются с патчами политики; первоисточник — docs + lockfile)

---

### 2. Что обычно отличается между мажорами (для маршрутизации вопросов)

- **Laravel 9:** переход на Symfony 6; типичные deprection в сторону строгих сигнатур.
- **Laravel 10:** обновления зависимостей, выравнивание с PHP 8.1+ фичами в экосистеме.
- **Laravel 11:** **slimmer default app** (меньше файлов из коробки), изменения в bootstrap/service providers по сравнению с 10; новые дефолты в `bootstrap/app.php` (концептуально — «одна точка конфигурации приложения»).
- **Laravel 12:** накопительные улучшения поверх 11; всегда читать **Release notes** и **Upgrade Guide** для **целевой** ветки.

- **Heuristic:** вопрос «где `Kernel.php` / где регистрировать маршруты в новом стиле» — почти всегда про **11+ vs 10−**.
- **First adoption task:** в README репозитория зафиксировать: `laravel/framework` ^X.Y, PHP ^A.B, способ деплоя.
- **Success criterion:** любой разработчик открывает нужную ветку docs за ≤1 минуту.

---

### 3. Дисциплина апгрейда (операционно)

- **Fact:** официальный путь — **Upgrade Guide** для каждого промежуточного мажора (не перепрыгивать через несколько мажоров без плана).
- **Heuristic:** сначала поднять **PHP** до диапазона целевого Laravel, затем `composer update` с фиксацией конфликтов пакетов (`laravel/*`, `spatie/*`, `nunomaduro/collision`, testing stack).
- **Check:** полный `php artisan test`, ручной smoke критичных маршрутов, прогон очередей на stage.
- **Decision criterion:** зелёные тесты + отсутствие deprecations, блокирующих прод (или явный backlog).
- **Confidence:** high (процесс), medium (конкретный diff между X и Y)

---

### 4. LTS и поддержка

- **Fact:** политика поддержки версий публикуется на laravel.com (release schedule). Не дублировать даты здесь — они устаревают.
- **Heuristic:** прод на EOL-мажоре — план миграции важнее новых фич.
- **Transfer_boundary:** enterprise SLA и security patches — по контракту с командой, не по этой KB.

---

## Registry card (template-knowledge-card-v1)

### Provenance
- source_refs: `https://laravel.com/docs/12.x/releases`; обобщение практик апгрейда; updated 2026-03-01
- created_at: 2026-03-01
- updated_at: 2026-03-01
- author: agent-notes KB maintainer

### Metadata
- card_id: KC-2026-03-01-LARAVEL-VERSIONS
- world: software.laravel
- layer: world
- tags: laravel; upgrade; php-versions; lts
- status: active

### Epistemic Linkage
- epistemic_basis: fact + inference
- evidence_type: official docs + composer constraints
- confidence: medium
- uncertainty: точные даты EOL и минорные требования PHP
- falsification_trigger: расхождение с laravel.com/docs/{major}.x/releases для заявленного мажора
- transfer_boundary: не использовать матрицу для не-Laravel стеков

### Core Unit
- context: планирование апгрейда, несовпадение примеров docs с проектом
- signal: «на каком мы Laravel», «почему не компилится после update»
- action: lockfile + Upgrade Guide ветки
- outcome: осознанный пошаговый апгрейд
- lesson: мажор Laravel и мажор PHP — связанные ограничения

### Operationalization
- first_adoption_task: записать версии в README и CI matrix
- validation_check: `composer validate`, `php artisan about` (где доступно)
- success_criterion: документация ветки docs совпадает с composer.lock
- rollback_or_mitigation: git revert + composer.lock из VCS

### Lifecycle
- supersedes: —
- superseded_by: —
- deprecation_reason: —

