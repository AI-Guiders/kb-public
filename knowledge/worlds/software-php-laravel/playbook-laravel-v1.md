# Laravel Playbook v1

## Purpose

Операционный контракт для приложений на **Laravel** (ориентир **10.x / 11.x / 12.x**; точная версия — из `composer.lock`). Сочетать с `playbook-php-v1.md` для вопросов чистого PHP/Composer. **Полный контур по версиям и смежным темам:** `index-knowledge-laravel-cluster-v1.md` → целевые `kb-laravel-*` (не грузить все сразу).

## Scope

- Маршруты, middleware, контроллеры — границы ответственности
- Конфиг/кеш/окружение
- Очереди и scheduler
- Тесты и миграции схемы

## Evidence-Based Working Format

- **Fact:** версии `laravel/framework` и PHP из `composer.lock` / `php artisan --version`.
- **Hypothesis:** ожидаемый эффект изменения (latency, корректность, side effects в очередях).
- **Check:** `php artisan test`, smoke на критичных маршрутах; для очередей — прогон worker в dev/stage.
- **Decision criterion:** тесты + отсутствие регрессий в логах при типовой нагрузке.
- **Confidence mark:** явно.

## Core Contracts

- **Convention over configuration:** сначала искать «как принято в Laravel», затем кастом.
- Новые HTTP-фичи: явно определить auth, validation, authorization policy, rate limiting где уместно.
- Долгие операции — в **queue**, не в синхронном запросе без веской причины.

## Config & Deploy Contracts

- После изменения `.env` или `config/*` в проде — `config:cache` в пайплайне или осознанный отказ с обоснованием.
- Документировать обязательные переменные окружения.

## Data Contracts

- Изменения схемы — только через **миграции**; откат плана миграции описывать.
- Подозрение на N+1 — профилировать запросы (Telescope/debugbar на stage, лог запросов).

## Queue & Schedule Contracts

- У каждого job: retries, timeout, idempotency note.
- Scheduler: проверить cron на всех репликах приложения (не дублировать `schedule:run` без координации).

## Testing Contracts

- Минимальный набор feature-тестов на аутентификацию и критичные API.
- Использовать фабрики вместо ручного создания больших графов объектов в тестах.

## Metrics

- Failed jobs count; latency p95 основных маршрутов; ошибки 5xx после деплоя.

## Revisit Triggers

- Upgrade Laravel мажора — читать **Upgrade Guide** ветки docs (`kb-laravel-versions-upgrades-v1.md`).
- Включение Octane/Horizon/Reverb — `kb-laravel-async-realtime-deployment-v1.md` (память, restart воркеров, channel auth).
- Новый UI-стек (Livewire/Filament/Inertia) — `kb-laravel-frontend-stacks-v1.md`.

## Full Laravel pass (по явному запросу)

1. `kb-laravel-fundamentals-v1.md`
2. `kb-laravel-versions-upgrades-v1.md` (если вопрос версий/миграции)
3. Далее **один** тематический kb из кластера: пакеты, security, Symfony, async/realtime, frontend — см. таблицу в `index-knowledge-laravel-cluster-v1.md`.

## Layer (memory-architecture)

- **L1:** этот playbook после status и при необходимости `playbook-php-v1.md`.
- **Deep:** фундамент — `kb-laravel-fundamentals-v1.md`; углубление — `kb-laravel-*` по кластеру `index-knowledge-laravel-cluster-v1.md`.
