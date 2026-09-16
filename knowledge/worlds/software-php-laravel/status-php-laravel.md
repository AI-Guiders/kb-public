# Status: PHP / Laravel v1
**Tags:** #software-php-laravel #status #worlds


**Канон перечня артефактов домена:** § Closure snapshot ниже; полный инвентарь имён файлов для людей и сборок — ещё `knowledge/README.md` (список Files). В `index-knowledge-router.md` в таблице доменов — короткий указатель, без дублирования всего списка kb.

## Closure snapshot

- **Мир PHP (`software.php`) — полный фундаментальный контур v1:**
  - Карта: `index-knowledge-php-cluster.md`
  - Эволюция языка **5.x→8.x**, миграции, таблица «фича→версия»: `kb-php-versions-and-evolution.md`
  - Платформа / рантайм: `kb-php-fundamentals.md` (вкл. JIT, GC, preload, FPM, ini, расширения)
  - Язык: `kb-php-language-semantics.md`
  - Веб (нативный): `kb-php-web-sessions-io.md`
  - Данные (PDO): `kb-php-data-persistence.md`
  - Инструменты и CI: `kb-php-tooling-quality.md`
- **Laravel (`software.laravel` / web-backend) — кластер v1:**
  - Карта: `index-knowledge-laravel-cluster.md`
  - Фундамент: `kb-laravel-fundamentals.md`
  - Версии и апгрейды: `kb-laravel-versions-upgrades.md`
  - First-party пакеты: `kb-laravel-first-party-packages.md`
  - Безопасность и API auth: `kb-laravel-security-auth-apis.md`
  - Symfony под капотом: `kb-laravel-symfony-underpinnings.md`
  - Async, Octane, Reverb, деплой воркеров: `kb-laravel-async-realtime-deployment.md`
  - Фронтенд-стеки: `kb-laravel-frontend-stacks.md`
- **Смежная PHP-экосистема (closure v2):**
  - Карта: `index-knowledge-php-adjacent-ecosystem.md`
  - WordPress: `kb-wordpress-architecture-ops.md`
  - Drupal: `kb-drupal-architecture-ops.md`
  - Symfony Framework (full stack): `kb-symfony-framework-fundamentals.md`
  - Composer / Packagist / сторонние пакеты: `kb-composer-packagist-thirdparty.md`
- **Playbooks:** `playbook-php.md`, `playbook-laravel.md`
- **Router:** `router-php-laravel` в `index-knowledge-router.md`

## Operational invariant (не gap)

- Конкретные **номера версий** пакетов и ядер (WP/Drupal/Symfony) в этой KB не фиксируются — источник истины: **`composer.lock`**, версия ядра WP, `drupal/core` в проекте, официальные release notes.

## Maintenance Policy

- Event-driven refresh via **Next review triggers** below.
- Order: `status-*` → operational playbook → fundamentals → evidence (`playbook-kb-operational-freshness.md`).
## Next review triggers
- **PHP 8.5** stable или смена политики поддержки на php.net.
- **Laravel 13+** или крупные изменения структуры в docs.
- Новые системные инциденты: рассинхрон ext между средами, preload/JIT регрессии, массовые deprecations.

## Retrieval hint (memory-architecture)

1. Этот `status-*`
2. `playbook-php.md` (и при UI/API на Laravel — `playbook-laravel.md`)
3. PHP: по таблице в `index-knowledge-php-cluster.md` — **один** целевой `kb-php-*`, если не запрошен full pass
4. Laravel: по таблице в `index-knowledge-laravel-cluster.md` — **один** целевой `kb-laravel-*`
5. WordPress / Drupal / Symfony / Composer-экосистема: `index-knowledge-php-adjacent-ecosystem.md` — **один** целевой kb

## Full pass hint

- Запрос вида «полный фундаментальный проход по PHP» → `playbook-php.md` § Full fundamental pass (5 шагов + остановки).
- Запрос вида «полный проход по Laravel / все версии и темы» → `index-knowledge-laravel-cluster.md` § порядок чтения + `playbook-laravel.md` § Full Laravel pass (без одновременной загрузки всех kb).
- Запрос про **WordPress / Drupal / Symfony / Composer-зоопарк** → `index-knowledge-php-adjacent-ecosystem.md` → один целевой kb.

