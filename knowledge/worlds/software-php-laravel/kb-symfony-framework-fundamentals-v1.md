# Symfony Framework — фундамент (full stack, не только «под Laravel»)

**Назначение:** карта **Symfony как приложения**: Kernel, bundles, DI-контейнер, конфигурация, HTTP, консоль, типичные компоненты. Отличается от `kb-laravel-symfony-underpinnings-v1.md` (там — роль Symfony **внутри** Laravel; читать его, если проект на Laravel). Мир `software.symfony`.

**Порядок:** `playbook-php-v1.md` → этот файл. Общий PHP — `kb-php-*`.

---

### 1. Kernel и жизненный цикл запроса

- **Fact:** `HttpKernel` обрабатывает Request → события ядра (request, controller, view, response, exception, terminate) → Response.
- **Heuristic:** отладка middleware-подобного поведения — через **event subscribers** и порядок приоритетов.
- **Confidence:** high

---

### 2. Bundles и структура проекта

- **Fact:** функциональность упаковывается в **bundles**; приложение — набор bundles + конфиг `config/packages/*`.
- **Heuristic:** Symfony **Flex** и рецепты настраивают пакеты при `composer require`; не коммитить секреты в yaml.

---

### 3. Dependency Injection

- **Fact:** сервисы регистрируются в контейнере; автоконфигурация и autowiring (в современных версиях) снижают бойлерплейт; интерфейсы → реализации в `services.yaml`.
- **Heuristic:** сервис `public: false` по умолчанию — инъекция через конструктор, не `$container->get()` в бизнес-коде.

---

### 4. Routing и контроллеры

- **Fact:** маршруты — атрибуты / yaml / php config; контроллеры возвращают Response, JsonResponse или render (Twig).
- **Heuristic:** единообразие с Laravel заканчивается на уровне «есть router»; синтаксис и conventions другие.

---

### 5. Doctrine ORM (типичный стек)

- **Fact:** в экосистеме Symfony часто **Doctrine**; сущности, миграции, репозитории.
- **Heuristic:** отличия от Eloquent — другой язык запросов (DQL, QueryBuilder); не переносить паттерны Laravel без проверки.

---

### 6. Messenger, Mailer, Scheduler

- **Fact:** **Messenger** — очереди и message bus; **Mailer** — абстракция почты; интеграция с cron через scheduler-пакеты или системный cron + консольные команды.
- **Heuristic:** как и в Laravel, идемпотентность обработчиков сообщений и retry policy — явно в коде/конфиге.

---

### 7. Тестирование

- **Fact:** **PHPUnit**, **WebTestCase**, Kernel test; иногда Panther для браузера.
- **Heuristic:** `kb-php-tooling-quality-v1.md` — общий слой; Symfony-специфика — документация testing ветки symfony.com/doc.

---

### 8. Версии и апгрейды

- **Fact:** мажор Symfony (5 → 6 → 7 …) сопровождается **upgrade guides** и deprecations; LTS-ветки для долгой поддержки.
- **Heuristic:** всегда сверять с **версией**, зафиксированной в `composer.lock`, не с «последней статьёй в блоге».

---

### 9. Граница с Laravel и Drupal

- **Laravel** — другой full-stack; общие компоненты Symfony не делают приложения взаимозаменяемыми.
- **Drupal** — CMS на Symfony; разработка модулей Drupal ≠ разработка чистого Symfony app, но HttpFoundation и т.д. родственны.

---

## Registry card (template-knowledge-card-v1)

### Provenance
- source_refs: `https://symfony.com/doc/current/index.html`; 2026-03-01
- created_at: 2026-03-01
- updated_at: 2026-03-01
- author: agent-notes KB maintainer

### Metadata
- card_id: KC-2026-03-01-SYMFONY-FW
- world: software.symfony
- layer: world
- tags: symfony; http-kernel; di; doctrine; messenger
- status: active

### Epistemic Linkage
- epistemic_basis: fact + inference
- evidence_type: official Symfony documentation
- confidence: medium
- uncertainty: минорные изменения между LTS и current
- falsification_trigger: несовпадение с doc выбранной ветки
- transfer_boundary: не заменяет чтение doc по конкретному компоненту

### Core Unit
- context: greenfield Symfony, миграция с другого фреймворка
- signal: «bundle vs package», «где сервисы»
- action: kernel events + services.yaml
- outcome: идиоматичная структура проекта
- lesson: Symfony явный и явно конфигурируемый

### Operationalization
- first_adoption_task: зафиксировать major symfony/* в README
- validation_check: `bin/console lint:container` где доступно
- success_criterion: деплой с `composer install --no-dev` и env
- rollback_or_mitigation: откат lockfile

### Lifecycle
- supersedes: —
- superseded_by: —
- deprecation_reason: —

