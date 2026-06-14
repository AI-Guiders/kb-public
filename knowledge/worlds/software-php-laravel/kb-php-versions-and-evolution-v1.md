# PHP — эволюция языка с ветки 5.x по 8.x (версии и особенности)

**Назначение:** **хронология и миграционные опоры**: что появилось в каком мажоре/миноре, типовые ломания при апгрейде, что считать легаси. Дополняет `kb-php-fundamentals-v1.md` (рантайм 8.4+) и `kb-php-language-semantics-v1.md` (семантика 8.x). Мир `software.php`.

**Порядок:** при вопросах «с какой версии фича», «миграция 5→7→8», «почему сломалось после апгрейда» — этот файл **или** php.net/releases + migration guides. Не заменяет построчный NEWS каждого патча.

**Первоисточник по спору:** `php.net/manual` и `php.net/releases/X.Y` для **заявленной** версии интерпретатора.

---

## 0. Политика поддержки (эвристика)

- **Fact:** ветки PHP выходят из активной поддержки по расписанию на php.net (EOL). **PHP 5.x и 7.x** на 2026 год — **исторический легаси**; новый код под них не целить.
- **Heuristic:** прод на EOL-ветке — только с планом миграции и исключением по рискам; security patches прекращаются после EOL.
- **Confidence:** high (процесс), medium (конкретные даты — всегда php.net)

---

## 1. PHP 5.x (ориентир 5.0 — 5.6)

### 1.0 Ранний PHP 5.0 — 5.2 (только контекст)

- **Fact:** **5.0** ввёл Zend Engine 2 и лучшее ООП; **5.1** — PDO по умолчанию, производительность; **5.2** — фильтры валидации, JSON-расширение и др. Без **namespaces** и **closures** как в 5.3+ код другой эпохи.
- **Heuristic:** археология репозиториев «до 5.3» — читать исторический manual; в KB деталь не разворачивается.
- **Confidence:** medium

### 1.1 Контекст (5.3 — 5.6)

- **Fact:** **5.3** (2009) — перелом для «современного» PHP: **namespaces** (`\`), **closures** (анонимные функции), **late static binding** (`static::`), **goto** (ограниченно). **5.4** — встроенный веб-сервер (CLI), **traits**, короткий синтаксис массива `[]`, closure может использовать `$this` в контексте объекта. **5.5** — **generators** / `yield`, `finally`, **password_hash** / **password_verify**. **5.6** — **variadic** `...$args`, `**` степень, `use function/const`, константы выражений для скаляров.
- **Heuristic:** код «только 5.2» — другая эпоха (без namespace); при чтении легаси смотреть минимум **5.3+** или раньше по дате проекта.
- **Confidence:** high

### 1.2 Типичные легаси-паттерны 5.x

- Нет type hints на скалярах (только классы/массивы/callable в поздних 5.x), много «магических» приведений.
- **mysql_*** (удалено в **7.0**) — замена **PDO** / **mysqli**.
- Старые стили ООП без namespace — глобальные имена классов.

---

## 2. Переход PHP 5.6 → 7.0 (крупнейший разрыв)

### 2.1 Удалённое и замены

- **Fact (ориентир):** расширение **mysql** удалено → **PDO** / **mysqli**. **ereg** / **split** (POSIX regex) удалены → **preg_***. Модификатор **`/e`** у **preg_replace** удалён (RCE-риск в прошлом). Многие **deprecated** из 5.x стали ошибками или удалены; **ASP-стиль тегов** и часть старых практик больше не поддерживаются.
- **Heuristic:** любой проект «5.6 в проде» при переносе на 7 — инвентаризация расширений и **динамических вызовов** с неверным числом аргументов (часто ломается).
- **Confidence:** high

### 2.2 Новое в PHP 7.0 (язык)

- **Fact:** **scalar type declarations** (`int`, `float`, `string`, `bool`) + **strict mode** через `declare(strict_types=1);` в файле. **Return type declarations**. Оператор **`??`** (null coalesce). Оператор **`<=>`** (spaceship). **Anonymous classes**. **Unicode codepoint escape** в строках `\u{...}`. Обработка ошибок: многие фатальные ошибки преобразованы в **Throwable** / подклассы (**Error** vs **Exception**).
- **Heuristic:** после 7.0 отладка «раньше был fatal, теперь catch» — проверить иерархию **Throwable**.
- **Confidence:** high

---

## 3. PHP 7.1

- **Fact:** **nullable types** (`?Type`), **void** return, **iterable** pseudo-type, **list()** с ключами, **class constant visibility** (`public const` в классе), **multiple catch**, **asymmetric** `try/catch/finally` улучшения, **void** нельзя return value.
- **Confidence:** high

---

## 4. PHP 7.2

- **Fact:** тип **`object`** для параметров/возврата; **abstract method override** с более широким аргументом (parameter type widening); новые типы для **json_encode** ошибок; **sodium** extension в ядро (крипто-поверхность).
- **Confidence:** high

---

## 5. PHP 7.3

- **Fact:** **flexible heredoc/nowdoc** (более читаемые закрывающие идентификаторы); **trailing commas** в вызовах функций и методов; **is_countable()**; **array_key_first** / **array_key_last**; ослабление ограничений на **`continue`** в `switch` (поведение уточнено).
- **Confidence:** high

---

## 6. PHP 7.4 (последний стабильный минор линии 7)

- **Fact:** **typed properties** (`public int $x;`). **Arrow functions** `fn($x) => $x + 1`. **Spread** в массивах `[...$a]`. Оператор **`??=`**. **Covariant return types** и **contravariant arguments** для возвратов/параметров в наследовании. **Underscore** как разделитель в числовых литералах. **__serialize** / **__unserialize** для кастомной сериализации объекта. Устаревание многих конструкций в пользу 8.0 (см. deprecations в manual 7.4).
- **Heuristic:** миграция **7.4 → 8.0** часто тяжелее, чем между минорами 8.x — готовить **Rector** / статанализ и тесты.
- **Confidence:** high

---

## 7. PHP 8.0

### 7.1 Крупные нововведения

- **Fact:** **Union types** (`string|int`). **Named arguments** при вызове функций. **Attributes** (`#[...]`) вместо docblock-only аннотаций в стиле 8.0. **`match`** выражение. **`nullsafe` оператор** `?->`. **Constructor property promotion**. **`mixed` type**. **`static` return type** уточнения. **WeakMap**. **str_contains**, **str_starts_with**, **str_ends_with**. JIT (начальная интеграция; конфигурация через opcache).
- **Heuristic:** **имена параметров** у встроенных функций стали частью публичного API для named arguments — переименования в минорах 8.x давали поломки; после обновлений смотреть changelog.
- **Confidence:** high

### 7.2 Ломания (направление)

- **Fact:** много прежних **notice/warning** стали **Error**/**TypeError**/**ValueError**; строже арифметика/конкатенация с null; изменения в порядке вычисления/побочных эффектов в отдельных конструкциях — сверять migration guide 8.0.
- **Heuristic:** «на 7.4 работало» — прогон тестов с `E_ALL` и PHP 8.0+.
- **Confidence:** medium (детали — по migration guide)

---

## 8. PHP 8.1

- **Fact:** **Enums** (`enum`, backed enums, methods in enum). **Readonly properties**. **`never` return type**. **First-class callable syntax** (`strlen(...)`). **fibers** (`Fiber` class) для низкоуровневой кооперативной многозадачности. **Intersection types** `A&B` (вместе с union по правилам грамматики). **final** на константах класса. **`new` в default parameter values** (ограниченно). Deprecations: передача **null** в non-nullable внутренним параметрам и др. — путь к 9.x.
- **Confidence:** high

---

## 9. PHP 8.2

- **Fact:** **`readonly` classes**. Самостоятельные типы **`true`**, **`false`**, **`null`** в union (уточнение системы типов). **DNF types** (объединение пересечений) для параметров/возвратов где поддерживается грамматика. Константы в **traits**. **Random extension** (`Random\Engine`, и т.д.) — новая криптостойкая/тестируемая генерация. Множество deprecations (динамические свойства по умолчанию у классов — на пути к запрету в 8.2+ с `[AllowDynamicProperties]` / миграция).
- **Heuristic:** после 8.2 **динамические свойства** — явная зона риска; объявлять свойства или использовать `#[AllowDynamicProperties]`.
- **Confidence:** high

---

## 10. PHP 8.3

- **Fact:** **`json_validate()`**. **Typed class constants**. Атрибут **`#[\Override]`** для явного override. **`mb_str_pad`**. Улучшения **Random**, **LDAP**, readonly-клонирование (**readonly** amend). Множество мелких исправлений и deprecations.
- **Confidence:** high

---

## 11. PHP 8.4

- **Fact:** см. детально **`kb-php-fundamentals-v1.md`** § про 8.4 и **`kb-php-language-semantics-v1.md`** (property hooks, asymmetric visibility, новые array helpers, `#[Deprecated]`, bcrypt cost, PCRE и т.д.). Здесь — якорь: **8.4 = текущий ориентир эволюции языка** вместе с 8.3/8.5 в политике проекта.
- **Confidence:** high

---

## 12. PHP 8.5+

- **Fact:** новые миноры после 8.4 — по **`https://www.php.net/releases/`** и **UPGRADING** в исходниках/документации; в KB не дублировать полный список: он устаревает каждый релиз.
- **Heuristic:** при апгрейде **всегда** читать **UPGRADING** для промежуточных миноров, если перепрыгиваешь несколько версий.
- **Confidence:** high (процесс)

---

## 13. Сводная таблица «фича → с какой версии» (краткая)

| Возможность | С версии (ориентир) |
|-------------|---------------------|
| Namespaces, closures (как в 5.x) | 5.3 |
| Traits | 5.4 |
| Generators `yield` | 5.5 |
| Variadic `...` | 5.6 |
| Scalar / return types, `??`, `<=>`, Throwable | 7.0 |
| Nullable `?T`, void, iterable | 7.1 |
| `object` type | 7.2 |
| Trailing comma in call, `is_countable` | 7.3 |
| Typed properties, arrow fn, spread array, `??=` | 7.4 |
| Union, named args, attributes, match, `?->`, promotion | 8.0 |
| Enum, readonly prop, never, Fiber | 8.1 |
| Readonly class, `true`/`false`/`null` standalone, Random ext | 8.2 |
| `json_validate`, typed const, `#[Override]` | 8.3 |
| Property hooks, asymmetric visibility (см. fundamentals) | 8.4 |

---

## 14. Миграция: практический порядок

1. Зафиксировать **текущую** и **целевую** версию и **путь** (например 7.4 → 8.2 → 8.4, не обязательно каждый минор в проде, но просмотреть UPGRADING между ними).
2. Включить **статический анализ** и **тесты** с максимальным уровнем диагностик.
3. **Rector** / codemods по политике команды для механических замен.
4. Прогон на **staging** с реальными данными; отдельно **CLI** и **веб** (OPcache).
5. Проверить **расширения** (`php -m`), **ini**, **Docker-образы**.

---

## Registry card (template-knowledge-card-v1)

### Provenance
- source_refs: `https://www.php.net/releases/` (ветки 5.6–8.x); `https://www.php.net/manual/en/migration70.php`, `migration71` … `migration84` где существуют; обобщение KB 2026-03-01
- created_at: 2026-03-01
- updated_at: 2026-03-01
- author: agent-notes KB maintainer

### Metadata
- card_id: KC-2026-03-01-PHP-EVOLUTION
- world: software.php
- layer: world
- tags: php; php5; php7; php8; migration; changelog
- status: active

### Epistemic Linkage
- epistemic_basis: fact + inference
- evidence_type: official php.net releases + migration pages
- confidence: medium
- uncertainty: полный список изменений каждого патча; поведение edge cases
- falsification_trigger: расхождение с migration guide для указанной пары версий
- transfer_boundary: не заменяет чтение UPGRADING при конкретном апгрейде проекта

### Core Unit
- context: легаси, апгрейд, «с какой версии доступно»
- signal: «на 7 работало», «есть ли enum»
- action: таблица §13 + migration docs
- outcome: осознанный план миграции
- lesson: большие скачки — смотреть все промежуточные UPGRADING

### Operationalization
- first_adoption_task: записать текущую PHP в CI и прод
- validation_check: `php -v` + `composer platform`
- success_criterion: нет неучтённых deprecations в целевой ветке
- rollback_or_mitigation: откат образа PHP + прежний lock

### Lifecycle
- supersedes: —
- superseded_by: —
- deprecation_reason: —

