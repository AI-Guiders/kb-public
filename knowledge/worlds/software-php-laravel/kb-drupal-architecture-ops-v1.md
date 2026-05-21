# Drupal — архитектура и операции (ядро, модули, конфигурация)

**Назначение:** опорная карта **Drupal 8+** (современное ядро на Symfony-компонентах): структура, модули, сущности, конфигурация, деплой. Мир `software.drupal`. Drupal 7 и ниже — legacy; упоминать только как «наследие».

**Порядок:** `status-php-laravel-v1.md` → `playbook-php-v1.md` → этот файл. Symfony детали ядра — при необходимости `kb-symfony-framework-fundamentals-v1.md`.

---

### 1. Ядро и стек

- **Fact:** Drupal **8+** использует **Symfony** (HttpKernel, Routing, EventDispatcher и др. — конкретный набор зависит от версии `drupal/core` в composer.lock).
- **Heuristic:** отладка «странного» HTTP-поведения — иногда пересекается с пониманием Symfony request cycle.
- **Confidence:** high

---

### 2. Модули и хуки

- **Fact:** расширение через **модули** (и темы); классические **hooks** сосуществуют с **событиями** (EventSubscriber) в OOP-стиле.
- **Heuristic:** новый код предпочтительно на сервисах и плагинах ядра (plugin system), не только на procedural hooks где есть API.

---

### 3. Сущности и поля

- **Fact:** контент и конфигурация моделируются **сущностями**, **полями**, **типами сущностей**; данные в БД + метаданные схемы.
- **Heuristic:** прямые SQL в обход API сущностей — ломают кеш, хуки и целостность; использовать Entity API.

---

### 4. Конфигурация: config sync

- **Fact:** конфиг в YAML (`config/sync` в типичном рабочем процессе); **configuration management** — экспорт/импорт между средами.
- **Heuristic:** ручные правки конфига только на проде без sync — дрейф сред; процедура: export → VCS → deploy → import.
- **First adoption task:** документировать, что считается «конфигом» vs «контентом» в проекте.

---

### 5. Кеш, агрегация, производительность

- **Fact:** многоуровневое кеширование (render cache, page cache, dynamic page cache); теги кеша при инвалидации.
- **Heuristic:** «не обновилось на сайте» — сначала кеш Drupal + reverse proxy, не сразу код.

---

### 6. Обновления и миграции

- **Fact:** обновление ядра и контрибов через **Composer**; **update.php** / database updates после выката.
- **Heuristic:** мажор Drupal — миграционный проект (данные, модули, API changes); читать release notes ветки.

---

### 7. Безопасность и права

- **Fact:** система **permissions** и **roles**; проверки в route access, entity access.
- **Heuristic:** кастомные маршруты без `_permission` / `_custom_access` — риск.
- **Confidence:** medium

---

### 8. Drush и CLI

- **Fact:** **Drush** — стандартный CLI для кеша, конфига, крон, миграций.
- **Heuristic:** автоматизация деплоя через Drush команды в CI/CD.

---

## Registry card (template-knowledge-card-v1)

### Provenance
- source_refs: `https://www.drupal.org/docs`; Symfony dependency via drupal/core; 2026-03-01
- created_at: 2026-03-01
- updated_at: 2026-03-01
- author: agent-notes KB maintainer

### Metadata
- card_id: KC-2026-03-01-DRUPAL-OPS
- world: software.drupal
- layer: world
- tags: drupal; entities; config-sync; drush; symfony
- status: active

### Epistemic Linkage
- epistemic_basis: fact + inference
- evidence_type: official Drupal docs
- confidence: medium
- uncertainty: версия core и снятие deprecated API
- falsification_trigger: смена архитектуры в будущих мажорах Drupal
- transfer_boundary: не WordPress; не чистый Symfony app без Drupal

### Core Unit
- context: модуль, деплой конфига, апгрейд core
- signal: «config sync», «почему пустой render»
- action: Entity API + config workflow
- outcome: воспроизводимые среды
- lesson: в Drupal конфиг — код; контент — данные

### Operationalization
- first_adoption_task: composer.lock + список кастомных модулей
- validation_check: `drush cr` + smoke после deploy
- success_criterion: нет дрейфа config между stage/prod
- rollback_or_mitigation: откат релиза + импорт предыдущего config snapshot

### Lifecycle
- supersedes: —
- superseded_by: —
- deprecation_reason: —
