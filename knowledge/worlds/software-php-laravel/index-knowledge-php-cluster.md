---
type: Index
title: Кластер PHP (**world (KE):** `software.php`) — навигация v1
description: '**Назначение:** точка входа при **полном или частичном** фундаментальном проходе по PHP без фреймворка. Следовать контракту memory-architecture: **status → playbook → kb**; этот файл — **карта «задача → файл»**, не заменяет playbook.'
tags: [software-php-laravel, worlds]
language: ru
world: software
subworld: php-laravel
---
# Кластер PHP (**world (KE):** `software.php`) — навигация v1


**Назначение:** точка входа при **полном или частичном** фундаментальном проходе по PHP без фреймворка. Следовать контракту memory-architecture: **status → playbook → kb**; этот файл — **карта «задача → файл»**, не заменяет playbook.

**Статус домена:** `status-php-laravel.md` (блок PHP + Laravel). Для чистого PHP достаточно статуса и `playbook-php.md`.

---

## Порядок чтения (full fundamental pass)

0. **Опционально (легаси, миграция с 5.x/7.x, «с какой версии фича»):** `kb-php-versions-and-evolution.md` — эволюция PHP 5.3→8.x, таблица фич, типовые ломания 5.6→7, 7.4→8.
1. `kb-php-fundamentals.md` — версии, SAPI, OPcache, типизация, 8.4, Composer, security baseline, JIT/GC/preload/FPM (расширенный блок).
2. `kb-php-language-semantics.md` — семантика языка, ООП, ошибки, пространства имён, сравнения, опасные API.
3. `kb-php-web-sessions-io.md` — суперглобалы, сессии, cookies, заголовки, загрузка файлов, потоки.
4. `kb-php-data-persistence.md` — PDO, транзакции, подготовленные запросы, обход без ORM.
5. `kb-php-tooling-quality.md` — тесты, статанализ, миграции версий, отладка, CI.

**Laravel:** после слоя PHP — `playbook-laravel.md` + `index-knowledge-laravel-cluster.md` (карта) → `kb-laravel-fundamentals.md` и при необходимости остальные `kb-laravel-*`.

---

## Таблица: вопрос → куда смотреть

| Тип вопроса | Первичный kb |
|-------------|----------------|
| Какая версия, миграция 8.3→8.4, OPcache, JIT, preloading | `kb-php-fundamentals.md` |
| Эволюция с PHP 5/7, мажорные ломания, «с какой версии enum/union/traits» | `kb-php-versions-and-evolution.md` |
| strict_types, union types, enum, readonly, match, attributes | `kb-php-language-semantics.md` |
| Fatal vs Exception, Throwable, кастомные ошибки | `kb-php-language-semantics.md` § ошибки |
| Почему «ломается» сессия / fixation / cookie flags | `kb-php-web-sessions-io.md` |
| $_FILES, MIME, path traversal при upload | `kb-php-web-sessions-io.md` |
| PDO vs mysqli, prepared statements, deadlocks | `kb-php-data-persistence.md` |
| PHPUnit vs Pest, PHPStan уровни, Rector | `kb-php-tooling-quality.md` |
| Composer scripts, platform, audit, conflict | `kb-php-fundamentals.md` + `playbook-php.md` |

---

## Правила нагрузки контекста

- **Не грузить все шесть kb сразу** — только по строке таблицы или по этапу full pass (0 опционально, 1→5).
- При **узком баге** — один kb + официальная документация php.net по затронутой функции.
- При **споре о поведении** — первоисточник: версия PHP + php.net/manual, не блоги.

---

## Смежные миры (не чистый PHP и не Laravel)

- WordPress, Drupal, Symfony full stack, Packagist/сторонние пакеты — `index-knowledge-php-adjacent-ecosystem.md`.

---

## Registry note

- **world:** software.php  
- **layer:** router (индекс кластера)  
- **status:** active  
- **updated_at:** 2026-03-01 (шаг 0 evolution)

