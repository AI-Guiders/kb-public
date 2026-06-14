# Playbook: PHP / Laravel — troubleshooting (v1)

> **Контур:** A · kb-public  
> **Когда:** «что поставить из laravel/*», очереди, поиск, платежи, OAuth  
> **Пакеты (детали):** [`../kb-laravel-first-party-packages-v1.md`](../kb-laravel-first-party-packages-v1.md)

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
| PDO / транзакции / SQL | `kb-php-data-persistence-v1.md` |
| Версии PHP / breaking | `kb-php-versions-and-evolution-v1.md` |

**Чеклист:** инвентаризация `laravel/*` в `composer.json`; smoke на каждый включённый пакет; нет «тяжёлых» неиспользуемых в проде.

---

## Роутер кластера

Полный проход PHP: `index-knowledge-php-cluster-v1.md` → `playbook-php-v1.md` § Full fundamental pass (не грузить все kb сразу).  
Laravel: `index-knowledge-laravel-cluster-v1.md` → `playbook-laravel-v1.md`.

---

## Как дополнять

Строка в таблицу + при необходимости карточка в `kb-laravel-first-party-packages-v1.md` §5.

