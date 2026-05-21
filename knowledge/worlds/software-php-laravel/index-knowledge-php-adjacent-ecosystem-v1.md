# Смежная PHP-экосистема (CMS, Symfony, Packagist) — навигация v1

**Назначение:** маршрутизация **вне** «чистого PHP» и **вне** Laravel: WordPress, Drupal, полноценный **Symfony Framework**, а также **Composer / Packagist / сторонние пакеты**. Не смешивать миры без явного запроса.

**Статус и базовый playbook:** `status-php-laravel-v1.md`, `playbook-php-v1.md` (Composer, версии PHP, безопасность зависимостей).

**Миры (world tags):** `software.wordpress`, `software.drupal`, `software.symfony`, `software.php` (инструментарий пакетов).

---

## Таблица: вопрос → куда смотреть

| Тип вопроса | Первичный kb |
|-------------|----------------|
| Хуки, темы, плагины, wp-admin, обновления WP, безопасность | `kb-wordpress-architecture-ops-v1.md` |
| Сущности, модули, config sync, Drupal 8+ и Symfony | `kb-drupal-architecture-ops-v1.md` |
| Bundles, Kernel, DI, Flex, Messenger, не Laravel | `kb-symfony-framework-fundamentals-v1.md` |
| SemVer, Spatie и зоопарк пакетов, audit, abandoned | `kb-composer-packagist-thirdparty-v1.md` |
| Низкоуровневый PHP (сессии, PDO, язык) | `index-knowledge-php-cluster-v1.md` |
| Laravel | `index-knowledge-laravel-cluster-v1.md` |

---

## Правила нагрузки

- **Один** kb за запрос; WordPress ≠ Drupal ≠ Symfony — не переносить паттерны.
- Версии ядра и контрибов — из **фактического** проекта (composer.lock, wp core version, drupal/core), не из памяти.

---

## Registry note

- **layer:** router  
- **status:** active  
- **updated_at:** 2026-03-01
