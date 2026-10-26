---
type: Playbook
title: 'Playbook: PHP / Laravel — troubleshooting'
description: '> **Контур:** A · kb-public'
tags: [living, playbook, software-php-laravel, worlds]
world: software
subworld: php-laravel
---
# Playbook: PHP / Laravel — troubleshooting


> **Контур:** A · kb-public  
> **Когда:** «что поставить из laravel/*», очереди, поиск, платежи, OAuth  
> **Пакеты (детали):** [`../kb-laravel-first-party-packages.md`](../kb-laravel-first-party-packages.md)

---

## Симптом → пакет / область

| Симптом | Куда смотреть |
|---------|----------------|
| UI очередей Redis | Horizon |
| Профайлинг запросов (dev) | Telescope |
| Поиск по моделям | Scout + драйвер |
| Подписки Stripe | Cashier |
| OAuth login | Socialite |
| Локально «как прод» в Docker | Sail |
| E2E в браузере | Dusk |
| PDO / транзакции / SQL | `kb-php-data-persistence.md` |
| Версии PHP / breaking | `kb-php-versions-and-evolution.md` |

**Чеклист:** инвентаризация `laravel/*` в `composer.json`; smoke на каждый включённый пакет; нет «тяжёлых» неиспользуемых в проде.

---

## Роутер кластера

Полный проход PHP: `index-knowledge-php-cluster.md` → `playbook-php.md` § Full fundamental pass (не грузить все kb сразу).  
Laravel: `index-knowledge-laravel-cluster.md` → `playbook-laravel.md`.

---

## Как дополнять

Строка в таблицу + при необходимости карточка в `kb-laravel-first-party-packages.md` §5.

