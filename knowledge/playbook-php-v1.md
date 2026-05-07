# PHP Playbook v1

## Purpose

Операционный контракт для **мира `software.php`** (8.x, ориентир **8.4+**): среда, Composer, SAPI, диагностика, безопасность, полный фундаментальный проход. Детали релиза и рантайма — `kb-php-fundamentals-v1.md`; **карта всех слоёв PHP** — `index-knowledge-php-cluster-v1.md`. **WordPress / Drupal / Symfony full stack / зоопарк Packagist** — `index-knowledge-php-adjacent-ecosystem-v1.md` → целевой kb.

## Scope

- Версия PHP и согласованность сред (local/CI/prod)
- Composer: lock, platform, audit, scripts
- CLI vs php-fpm: разная диагностика
- Миграция минорных/патчей PHP
- Когда грузить какой kb из PHP-кластера
- Смежные платформы на PHP (не Laravel): см. § Adjacent ecosystem

## Adjacent ecosystem (WordPress, Drupal, Symfony, Packagist)

- **Карта:** `index-knowledge-php-adjacent-ecosystem-v1.md` — один целевой kb за запрос.
- **Composer audit, SemVer, Spatie и сторонние пакеты:** `kb-composer-packagist-thirdparty-v1.md` (дополняет контракты этого playbook про lockfile).

## Full fundamental pass (миру php)

Выполнять **последовательно** только при явном запросе «полный проход» / онбординг по PHP (не в каждом чате):

0. **Опционально:** `kb-php-versions-and-evolution-v1.md` — если есть легаси 5.x/7.x или нужна хронология фич по мажорам.
1. `kb-php-fundamentals-v1.md` — платформа, OPcache, 8.4, FPM, JIT/preload outline.
2. `kb-php-language-semantics-v1.md` — язык, типы, ошибки, ООП.
3. `kb-php-web-sessions-io-v1.md` — HTTP, сессии, cookies, upload, потоки.
4. `kb-php-data-persistence-v1.md` — PDO, SQL-дисциплина, транзакции.
5. `kb-php-tooling-quality-v1.md` — тесты, статанализ, Rector, CI.

**Миграция между мажорами (5→7→8):** помимо шага 0 — официальные страницы `migration70` … `migration84` на php.net и `UPGRADING` между минорами; KB не заменяет их построчно.

**Остановка:** после шага, отвечающего на вопрос; не читать следующий kb без нужды.

## Evidence-Based Working Format

- **Fact:** `php -v`, `php -i` (релевантные директивы), SAPI из `php_sapi_name()`.
- **Hypothesis:** ожидаемый эффект изменения.
- **Check:** минимальный reproduce (скрипт, тест, curl).
- **Decision criterion:** тесты + отсутствие новых deprecations в CI при `E_ALL`.
- **Confidence mark:** явно.

## Core Contracts

- Одна **источник правды** по версии PHP: `composer.json` + образ CI + прод-образ.
- `composer.lock` под версионированием для **приложений**.
- Не полагаться на глобально установленный PHP без проверки в проекте.

## Runtime Contracts

- Разделять **веб** (OPcache, fpm workers, timeouts, preload) и **CLI** (`memory_limit`, batch).
- После деплоя: политика сброса OPcache / перезапуск fpm при смене кода.

## Dependency Contracts

- Регулярно `composer audit` в CI.
- Явные `ext-*` в `require`, если без них приложение не поднимается.

## Security Contracts

- Прод: `display_errors=Off`, логирование отдельно от ответа пользователю.
- Секреты через env/secret store; сессии — `session_regenerate_id` при смене уровня доверия (см. `kb-php-web-sessions-io-v1.md`).

## Metrics

- Время CI на целевой версии PHP.
- Deprecations count в логах.
- Инциденты рассинхрона версий / расширений.

## Revisit Triggers

- Обновление PHP в проде; массовые deprecations после `composer update`.
- Смена SAPI (FrankenPHP, Octane, RoadRunner) — пересмотреть таймауты, долгоживущие процессы, OPcache.

## Layer (memory-architecture)

- **L1:** `status-php-laravel-v1.md` → этот playbook.
- **L1 deep:** один или цепочка kb по `index-knowledge-php-cluster-v1.md`.
- **Laravel поверх PHP:** `playbook-laravel-v1.md` (не подменять фреймворком знание рантайма).