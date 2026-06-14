# Status: PHP / Laravel v1

**Канон перечня артефактов домена:** § Closure snapshot ниже; полный инвентарь имён файлов для людей и сборок — ещё `knowledge/README.md` (список Files). В `index-knowledge-router-v1.md` в таблице доменов — короткий указатель, без дублирования всего списка kb.

## Closure snapshot

- **Мир PHP (`software.php`) — полный фундаментальный контур v1:**
  - Карта: `index-knowledge-php-cluster-v1.md`
  - Эволюция языка **5.x→8.x**, миграции, таблица «фича→версия»: `kb-php-versions-and-evolution-v1.md`
  - Платформа / рантайм: `kb-php-fundamentals-v1.md` (вкл. JIT, GC, preload, FPM, ini, расширения)
  - Язык: `kb-php-language-semantics-v1.md`
  - Веб (нативный): `kb-php-web-sessions-io-v1.md`
  - Данные (PDO): `kb-php-data-persistence-v1.md`
  - Инструменты и CI: `kb-php-tooling-quality-v1.md`
- **Laravel (`software.laravel` / web-backend) — кластер v1:**
  - Карта: `index-knowledge-laravel-cluster-v1.md`
  - Фундамент: `kb-laravel-fundamentals-v1.md`
  - Версии и апгрейды: `kb-laravel-versions-upgrades-v1.md`
  - First-party пакеты: `kb-laravel-first-party-packages-v1.md`
  - Безопасность и API auth: `kb-laravel-security-auth-apis-v1.md`
  - Symfony под капотом: `kb-laravel-symfony-underpinnings-v1.md`
  - Async, Octane, Reverb, деплой воркеров: `kb-laravel-async-realtime-deployment-v1.md`
  - Фронтенд-стеки: `kb-laravel-frontend-stacks-v1.md`
- **Смежная PHP-экосистема (closure v2):**
  - Карта: `index-knowledge-php-adjacent-ecosystem-v1.md`
  - WordPress: `kb-wordpress-architecture-ops-v1.md`
  - Drupal: `kb-drupal-architecture-ops-v1.md`
  - Symfony Framework (full stack): `kb-symfony-framework-fundamentals-v1.md`
  - Composer / Packagist / сторонние пакеты: `kb-composer-packagist-thirdparty-v1.md`
- **Playbooks:** `playbook-php-v1.md`, `playbook-laravel-v1.md`
- **Router:** `router-php-laravel` в `index-knowledge-router-v1.md`

## Operational invariant (не gap)

- Конкретные **номера версий** пакетов и ядер (WP/Drupal/Symfony) в этой KB не фиксируются — источник истины: **`composer.lock`**, версия ядра WP, `drupal/core` в проекте, официальные release notes.

## Next review triggers

- **PHP 8.5** stable или смена политики поддержки на php.net.
- **Laravel 13+** или крупные изменения структуры в docs.
- Новые системные инциденты: рассинхрон ext между средами, preload/JIT регрессии, массовые deprecations.

## Retrieval hint (memory-architecture)

1. Этот `status-*`
2. `playbook-php-v1.md` (и при UI/API на Laravel — `playbook-laravel-v1.md`)
3. PHP: по таблице в `index-knowledge-php-cluster-v1.md` — **один** целевой `kb-php-*`, если не запрошен full pass
4. Laravel: по таблице в `index-knowledge-laravel-cluster-v1.md` — **один** целевой `kb-laravel-*`
5. WordPress / Drupal / Symfony / Composer-экосистема: `index-knowledge-php-adjacent-ecosystem-v1.md` — **один** целевой kb

## Full pass hint

- Запрос вида «полный фундаментальный проход по PHP» → `playbook-php-v1.md` § Full fundamental pass (5 шагов + остановки).
- Запрос вида «полный проход по Laravel / все версии и темы» → `index-knowledge-laravel-cluster-v1.md` § порядок чтения + `playbook-laravel-v1.md` § Full Laravel pass (без одновременной загрузки всех kb).
- Запрос про **WordPress / Drupal / Symfony / Composer-зоопарк** → `index-knowledge-php-adjacent-ecosystem-v1.md` → один целевой kb.
