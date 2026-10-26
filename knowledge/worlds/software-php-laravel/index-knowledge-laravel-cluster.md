---
type: Index
title: Кластер Laravel (миру `software.laravel` / `software.web-backend`) — навигация v1
description: '**Назначение:** карта **полного контура** Laravel: версии, экосистема, безопасность, фундамент Symfony, долгоживущие воркеры и фронтенд-стеки. Контракт memory-architecture: **status → playbook-php (при сомнениях по PHP) → playbook-laravel → один целевой kb**. Этот файл — **маршрутизатор**, не заменяет playbook.'
tags: [software-php-laravel, worlds]
language: ru
world: software
subworld: php-laravel
---
# Кластер Laravel (миру `software.laravel` / `software.web-backend`) — навигация v1


**Назначение:** карта **полного контура** Laravel: версии, экосистема, безопасность, фундамент Symfony, долгоживущие воркеры и фронтенд-стеки. Контракт memory-architecture: **status → playbook-php (при сомнениях по PHP) → playbook-laravel → один целевой kb**. Этот файл — **маршрутизатор**, не заменяет playbook.

**Статус домена:** `status-php-laravel.md`.

---

## Порядок чтения (full Laravel pass)

Выполнять **по запросу** или при онбординге на незнакомый проект; не грузить все kb одновременно.

1. `kb-laravel-fundamentals.md` — HTTP-цикл, Eloquent, очереди, конфиг/кеш, тесты (база фреймворка).
2. `kb-laravel-versions-upgrades.md` — мажоры 8→12+, требования PHP, политика апгрейда, что сверять в docs.
3. `kb-laravel-first-party-packages.md` — Horizon, Telescope, Scout, Cashier, Socialite, Sail, Dusk, Valet, Pint, Reverb и др.
4. `kb-laravel-security-auth-apis.md` — Sanctum, Passport, Breeze/Jetstream/Fortify, политики, CSRF, API-контуры.
5. `kb-laravel-symfony-underpinnings.md` — какие компоненты Symfony под капотом, когда читать symfony.com.
6. `kb-laravel-async-realtime-deployment.md` — Octane, FrankenPHP, RoadRunner, Swoole-стек, Horizon/worker, подводные камни state.
7. `kb-laravel-frontend-stacks.md` — Blade-first, Livewire, Filament, Inertia (+ Vue/React).

**Нижний слой:** при любых низкоуровневых вопросах PHP — `index-knowledge-php-cluster.md` и соответствующие `kb-php-*`.

---

## Таблица: вопрос → куда смотреть

| Тип вопроса | Первичный kb |
|-------------|----------------|
| С какой версии Laravel / PHP совместимость, upgrade 10→11→12 | `kb-laravel-versions-upgrades.md` |
| Что сломалось после мажора, `str_*`/`enum`, структура приложения 11+ | `kb-laravel-versions-upgrades.md` + официальный Upgrade Guide ветки |
| Очереди Horizon, Telescope в проде, Scout, Cashier, Socialite | `kb-laravel-first-party-packages.md` |
| SPA API tokens, OAuth2, мобильный клиент, Sanctum vs Passport | `kb-laravel-security-auth-apis.md` |
| Политики, gates, CSRF, шифрование, массовое присвоение | `kb-laravel-security-auth-apis.md` + fundamentals |
| HttpKernel, Console, Process, Mime, Translation — «откуда это в Laravel» | `kb-laravel-symfony-underpinnings.md` |
| Octane / FrankenPHP / RoadRunner, memory leaks, синглтоны | `kb-laravel-async-realtime-deployment.md` |
| WebSockets, Laravel Reverb, broadcasting | `kb-laravel-async-realtime-deployment.md` |
| Livewire vs Inertia vs Filament, когда что выбирать | `kb-laravel-frontend-stacks.md` |
| Базовый маршрут, middleware, Eloquent N+1 | `kb-laravel-fundamentals.md` |

---

## Правила нагрузки контекста

- **Один kb за раз** плюс `playbook-laravel.md`, если нужны операционные контракты.
- **Версия — из `composer.lock`**, не из памяти; нумерация docs на laravel.com/docs/X.x должна совпадать с мажором приложения.
- **Legacy (Laravel ≤9):** отдельно проверять EOL и security-only ветки; матрица в `kb-laravel-versions-upgrades.md`.

---

## Registry note

- **world:** software.laravel  
- **layer:** router (индекс кластера)  
- **status:** active  
- **updated_at:** 2026-03-01

