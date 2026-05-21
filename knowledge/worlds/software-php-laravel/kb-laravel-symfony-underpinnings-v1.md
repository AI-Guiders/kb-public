# Laravel — связь с Symfony: компоненты и границы ответственности

**Назначение:** объяснить, **почему** в Laravel встречаются классы и концепции Symfony (HttpFoundation, Console, Process, …) и **когда** идти в документацию symfony.com. Мир `software.laravel` + пересечение с `software.php`.

**Порядок загрузки:** `kb-laravel-fundamentals-v1.md` → этот файл. Глубокий PHP — `kb-php-language-semantics-v1.md`.

---

### 1. Факт: Laravel строится на компонентах Symfony

- **Fact:** ядро HTTP-абстракций, консоль, процессы, MIME, переводы, rate limiter, finder и др. historically/фактически опираются на **symfony/*** пакеты (конкретный набор зависит от версии `laravel/framework` — смотреть `composer.lock`).
- **Heuristic:** stack trace с `Symfony\Component\HttpFoundation` — норма, не «ошибка фреймворка».
- **Confidence:** high

---

### 2. Типичные точки контакта разработчика

| Область | Symfony-слой (концептуально) | Практика в Laravel |
|---------|--------------------------------|-------------------|
| Request/Response | HttpFoundation | `Illuminate\Http\Request` оборачивает/наследует поведение foundation |
| Console | Console | `artisan` команды, стиль вывода, сигналы |
| Subprocess / shell | Process | `Illuminate\Support\Process` (обёртки вокруг Process component в современных версиях) |
| MIME / guess types | Mime | загрузки файлов, ответы с типами |
| Translation | Translation | `__()`, lang files |
| Routing (частично) | Routing concepts | Laravel router — свой DSL, но идеи middleware/pipeline родственны |

- **Heuristic:** баг «на границе HTTP» (заголовки, cookies, stream) — иногда проще искать по **Symfony HttpFoundation** + версии пакета в lockfile.

---

### 3. Когда читать Symfony docs вместо Laravel

- **Низкоуровневые детали** Response (стримы, BinaryFileResponse), Cookie flags, нюансы консольного I/O.
- **Версионная несовместимость** после `composer update`, когда меняется минор Symfony под капотом Laravel.

- **Heuristic:** сначала **Laravel docs** для идиоматичного API; Symfony — для edge cases и мажоров компонентов.

---

### 4. Что эта KB не покрывает

- **WordPress / Drupal** — см. `index-knowledge-php-adjacent-ecosystem-v1.md` и `kb-wordpress-architecture-ops-v1.md` / `kb-drupal-architecture-ops-v1.md`.
- **Прямая разработка на Symfony Framework** — `kb-symfony-framework-fundamentals-v1.md`; здесь только **мост** для Laravel-разработчика.

---

## Registry card (template-knowledge-card-v1)

### Provenance
- source_refs: composer dependencies `laravel/framework`; Symfony component docs; обобщение 2026-03-01
- created_at: 2026-03-01
- updated_at: 2026-03-01
- author: agent-notes KB maintainer

### Metadata
- card_id: KC-2026-03-01-LARAVEL-SYMFONY
- world: software.laravel
- layer: world
- tags: laravel; symfony; http-foundation; console
- status: active

### Epistemic Linkage
- epistemic_basis: fact + inference
- evidence_type: dependency graph + official Symfony/Laravel docs
- confidence: medium
- uncertainty: точный список компонентов на каждом миноре Laravel
- falsification_trigger: смена зависимостей в новом релизе laravel/framework
- transfer_boundary: не руководство по чистому Symfony Full Stack

### Core Unit
- context: stack trace в Symfony, странное поведение Response/Cookie
- signal: «это Laravel или Symfony»
- action: lockfile → компонент → нужная doc ветка
- outcome: быстрее локализовать слой
- lesson: Laravel = оркестрация + соглашения поверх компонентов

### Operationalization
- first_adoption_task: знать major/minor symfony/* из composer.lock при апгрейде
- validation_check: регрессия интеграционных тестов после composer update
- success_criterion: нет сюрпризов от изменения symfony/* в патче
- rollback_or_mitigation: pin зависимости только как временная мера + тикет

### Lifecycle
- supersedes: —
- superseded_by: —
- deprecation_reason: —
