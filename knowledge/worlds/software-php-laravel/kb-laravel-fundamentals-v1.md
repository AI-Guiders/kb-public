# Laravel — фундаментальный слой (framework на PHP)

**Назначение:** опорная карта **Laravel** как full-stack PHP-фреймворка (HTTP, консоль, очереди, ORM) в связке с **PHP 8.2+** (для Laravel 12 — диапазон **8.2–8.5** по документации laravel.com/docs/12.x). Слой **L1 world** (миру `software.laravel` / `software.web-backend`). Рантайм PHP без фреймворка — в `kb-php-fundamentals-v1.md`.

**Расширенный контур Laravel (версии, пакеты, безопасность, Symfony, Octane/Reverb, Livewire/Filament/Inertia):** карта и порядок — `index-knowledge-laravel-cluster-v1.md` и kb из той карты; этот файл — **шаг 1** полного Laravel pass.

**Порядок загрузки:** `status-php-laravel-v1.md` → `playbook-php-v1.md` (при сомнениях по PHP/Composer) → `playbook-laravel-v1.md` → этот файл.

---

### 1. Место Laravel в стеке

- **Fact:** Laravel задаёт структуру приложения (контейнер IoC, конфиг, провайдеры), маршрутизацию, слой HTTP, абстракции к БД (**Eloquent**), очереди, события, расписание (**Scheduler**), CLI (**Artisan**). Версия фреймворка и требования к PHP задаются в `composer.json` проекта и документации релиза.
- **Heuristic:** не обсуждать «Laravel» без указания **мажорной версии** приложения (10/11/12) и фактической версии PHP; поведение и API различаются между мажорами.
- **First adoption task:** в README сервиса: Laravel X.Y, PHP A.B, способ деплоя (octane / fpm / horizon).
- **Success criterion:** новый участник понимает контур приложения за один проход по README + `routes/`.
- **Confidence:** high

---

### 2. Жизненный цикл запроса и границы слоёв

- **Fact:** HTTP-запрос проходит **middleware**, попадает в **router** → контроллер / closure / invokable; ответ формируется через response; исключения могут маппиться в HTTP через handler. Консольные команды идут через **Artisan** с отдельным bootstrap.
- **Heuristic:** бизнес-правила не смешивать с middleware «толстыми» порциями; тяжёлую работу выносить в jobs/queue.
- **First adoption task:** для каждого нового маршрута определить: auth? validation? rate limit? idempotency?
- **Success criterion:** предсказуемая цепочка middleware; тестируемые контроллеры/действия.
- **Confidence:** high

---

### 3. Данные: Eloquent, миграции, транзакции

- **Fact:** **Eloquent** — ORM с моделями, отношениями, scope’ами; **миграции** версионируют схему; **фабрики/сидеры** — для dev/test. Транзакции через `DB::transaction`.
- **Heuristic:** N+1 запросы — первая гипотеза при «медленных страницах»; использовать eager loading осознанно; индексы — на уровне миграций, а не только «в голове».
- **First adoption task:** включить в CI минимальный набор тестов, затрагивающих критичные запросы (или Laravel Pint + статические проверки + ручной профайлинг на стейдже).
- **Success criterion:** нет необъяснимого роста числа запросов на типовой экран.
- **Confidence:** medium

---

### 4. Конфигурация, окружение, кеш

- **Fact:** `.env` задаёт секреты и среду; `config/*` — кешируемые значения; `php artisan config:cache`, `route:cache`, `view:cache` используются в проде для производительности; после смены env нужен redeploy/clear кеша.
- **Heuristic:** **никогда** не коммитить `.env` с секретами; в проде не полагаться на «забытый» `config:cache` от старой схемы.
- **First adoption task:** документировать обязательные переменные окружения (таблица имя / назначение / пример без секрета).
- **Success criterion:** поднятие нового окружения по чек-листу env без угадывания.
- **Confidence:** high

---

### 5. Очереди, фоновые задачи, расписание

- **Fact:** **Queue** worker обрабатывает jobs; **Horizon** (опционально) даёт UI и метрики для Redis-очередей; **Scheduler** требует cron entry `schedule:run` каждую минуту.
- **Heuristic:** долгие HTTP-запросы — кандидаты в job; идемпотентность и retry policy описывать явно.
- **First adoption task:** для каждого job: timeout, tries, backoff, failed handler.
- **Success criterion:** нет «потерянных» задач без мониторинга failed_jobs / алертов.
- **Confidence:** medium

---

### 6. Тестирование и качество

- **Fact:** стандартный стек: **PHPUnit** или **Pest**; HTTP-тесты через `get/post` helpers; фабрики моделей; параллельный прогон в CI.
- **Heuristic:** критичные use-case покрыть интеграционными тестами с реальной БД (test sqlite/mysql) важнее, чем 100% покрытие утилит.
- **First adoption task:** минимальный smoke suite на deploy; статанализ (PHPStan/Larastan) по мере зрелости.
- **Success criterion:** регрессии ловятся до продакшена.
- **Confidence:** medium

---

## Registry card (template-knowledge-card-v1)

### Provenance (происхождение)
- source_refs: `https://laravel.com/docs/12.x/releases` (требования PHP); обобщение архитектуры Laravel из официальной документации; связка с кластером Laravel 2026-03-01.
- created_at: 2026-02-28
- updated_at: 2026-03-01
- author: agent-notes KB maintainer

### Metadata
- card_id: KC-2026-02-28-LARAVEL-L1
- world: software.laravel
- layer: world
- tags: laravel; php; eloquent; queue; artisan; http; cluster-entry
- status: active

### Epistemic Linkage
- epistemic_basis: fact + inference
- evidence_type: official Laravel docs + общеотраслевые практики
- confidence: medium
- uncertainty: детали конкретного мажора (10 vs 11 vs 12) — всегда сверять с docs выбранной ветки
- falsification_trigger: несовпадение с документацией для заявленной версии Laravel
- transfer_boundary: не переносить соглашения одного мажора на другой без чтения upgrade guide

### Core Unit
- context: проектирование фич, отладка Laravel, деплой, очереди
- signal: «где разместить логику», «почему 500», «как кешировать», «как тестировать»
- action: playbook-laravel-v1 → точечный kb; версии из composer.lock
- outcome: решения в рамках идиоматичного Laravel
- lesson: Laravel силён соглашениями — сначала конвенции, потом кастом

### Operationalization
- first_adoption_task: задокументировать версии и обязательные env; настроить CI
- validation_check: `php artisan test`, smoke после `config:cache`
- success_criterion: стабильный деплой и наблюдаемость очередей
- rollback_or_mitigation: откат релиза + очистка кеша конфигов

### Lifecycle
- supersedes: —
- superseded_by: —
- deprecation_reason: —