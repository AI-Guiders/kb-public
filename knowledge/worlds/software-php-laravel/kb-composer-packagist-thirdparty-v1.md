# Composer, Packagist и сторонняя экосистема PHP

**Назначение:** контракты **управления зависимостями** и навигация по **популярным семействам** пакетов (в т.ч. Spatie для Laravel), без фиксации версий в KB. Мир `software.php` (tooling). Сочетается с `playbook-php-v1.md`.

---

### 1. Источник истины

- **Fact:** для конкретного проекта единственный контракт версий — **`composer.lock`** (+ `composer.json` для диапазонов).
- **Heuristic:** ответы вида «пакет X в версии Y» без lockfile — гипотеза; всегда проверять lock или `composer show`.

---

### 2. SemVer и ограничения

- **Fact:** `^`, `~`, exact version, `*` — разная семантика риска обновлений; `minimum-stability` и `prefer-stable` влияют на резолв.
- **Heuristic:** библиотека с 0.x может ломать API на миноре — читать changelog пакета.

---

### 3. Безопасность и здоровье пакетов

- **Fact:** `composer audit` (и экосистема advisories) — обязательный элемент CI для приложений.
- **Heuristic:** **abandoned** пакет в `composer outdated` — план замены; **replacement** подсказка от maintainers — рассмотреть миграцию.
- **Heuristic:** форки с 3 звёздами и последним коммитом 5 лет назад — красный флаг для продакшена.

---

### 4. Платформенные требования

- **Fact:** `config.platform` — пин виртуальной версии PHP/ext для резолва на CI без полного образа; должен отражать реальный прод.
- **Heuristic:** рассинхрон ext (`ext-sodium`, `ext-intl`) между dev и prod — классический «works on my machine».

---

### 5. Автозагрузка и скрипты

- **Fact:** PSR-4 в `composer.json`; `scripts` для post-install; оптимизация автозагрузчика в проде (`--optimize-autoloader`, `classmap-authoritative` где уместно).
- **Confidence:** high

---

### 6. Семейства сторонних пакетов (ориентиры, не каталог версий)

| Семья / вендор | Типичное назначение |
|----------------|---------------------|
| **spatie/laravel-*** | Утилиты для Laravel: permissions, backup, медиа, настройки, очереди-обвязки и т.д. |
| **nesbot/carbon** | Даты/время (часто транзитивно через Laravel) |
| **guzzlehttp/guzzle** | HTTP-клиент |
| **league/flysystem** | Файловые абстракции |
| **ramsey/uuid** | UUID |
| **monolog/monolog** | Логирование |

- **Heuristic:** перед внедрением нового `vendor/*` — лицензия, активность, совместимость с **твоим** major Laravel/PHP из lockfile.
- **Transfer_boundary:** не дублировать документацию каждого пакета — только маршрутизация и риски.

---

### 7. Конфликты и разрешение

- **Fact:** `composer why` / `why-not` — диагностика цепочки зависимостей.
- **Heuristic:** `conflict` в composer.json — последнее средство; лучше обновить общий транзитивный пакет или заменить зависимость.

---

## Registry card (template-knowledge-card-v1)

### Provenance
- source_refs: `https://getcomposer.org/doc/`; обобщение практик Packagist; 2026-03-01
- created_at: 2026-03-01
- updated_at: 2026-03-01
- author: agent-notes KB maintainer

### Metadata
- card_id: KC-2026-03-01-COMPOSER-ECO
- world: software.php
- layer: world
- tags: composer; packagist; semver; spatie; security-audit
- status: active

### Epistemic Linkage
- epistemic_basis: fact + inference
- evidence_type: Composer official docs + industry practice
- confidence: high
- uncertainty: конкретные CVE и версии — только из audit/lock
- falsification_trigger: смена команд composer или политики Packagist
- transfer_boundary: не npm/pip

### Core Unit
- context: новый пакет, конфликт версий, abandoned
- signal: «можно ли обновить», «откуда тянется»
- action: lockfile + audit + why
- outcome: осознанный dependency graph
- lesson: lockfile в VCS для приложений

### Operationalization
- first_adoption_task: CI шаг `composer audit`
- validation_check: reproducible `composer install` из lock
- success_criterion: нет незакрытых critical advisories без исключения
- rollback_or_mitigation: revert lock + composer install

### Lifecycle
- supersedes: —
- superseded_by: —
- deprecation_reason: —

