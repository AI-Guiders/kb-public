# PHP — данные и персистентность (PDO и обход без ORM)

**Назначение:** фундамент **работы с БД из PHP** без привязки к Laravel/Eloquent: PDO, подготовленные запросы, транзакции, типичные ошибки. Мир **`software.php`**.

---

### 1. Почему PDO как дефолт

- **Fact:** **PDO** — унифицированный слой с драйверами (`mysql`, `pgsql`, `sqlite`, …); единый стиль prepared statements; исключения в режиме `ERRMODE_EXCEPTION`.
- **Heuristic:** новый код без тяжёлого ORM — PDO + тонкий репозиторий; mysqli допустим, но два API в одном проекте — только с обоснованием.

---

### 2. Подключение и DSN

- **Fact:** DSN строка зависит от драйвера; учётные данные не хардкодить — env/config вне VCS.
- **Heuristic:** для MySQL 8 — явно charset `utf8mb4` в DSN; timezone — задавать на соединении или в сервере согласованно.

---

### 3. Подготовленные запросы и плейсхолдеры

- **Fact:** именованные и позиционные плейсхолдеры; для `IN (...)` — собирать плейсхолдеры динамически или использовать альтернативы (временные таблицы) — не конкатенировать сырые значения.
- **Heuristic:** никогда не интерполировать пользовательские данные в SQL; идентификаторы таблиц/колонок — allowlist, не параметры prepared statement.

---

### 4. Эмуляция prepared statements

- **Fact:** PDO может эмулировать prepares на клиенте (`ATTR_EMULATE_PREPARES`); для MySQL влияет на повторное использование планов и экранирование.
- **Heuristic:** для прод-MySQL часто отключают эмуляцию (`false`), если нет причин иначе — проверить поведение лимитов/типов.

---

### 5. Транзакции и изоляция

- **Fact:** `beginTransaction` / `commit` / `rollBack`; уровень изоляции задаётся SQL `SET TRANSACTION` (зависит от СУБД).
- **Heuristic:** бизнес-операция «всё или ничего» — одна транзакция на use-case; не держать транзакции открытыми на время HTTP long poll.

---

### 6. Deadlock и retry

- **Fact:** при deadlock СУБД откатывает одну транзакцию — приложение должно уметь **retry** идемпотентной операции.
- **Heuristic:** логировать код ошибки; ограничить число повторов с backoff.

---

### 7. Потоковое чтение и память

- **Fact:** `fetch` в цикле vs `fetchAll` — последний раздувает память на больших выборках.
- **Heuristic:** отчёты и миграции данных — итерация с лимитом/ключом или курсоры (если поддерживаются).

---

### 8. N+1 на уровне ручных запросов

- **Fact:** без ORM N+1 всё равно возможен: цикл по списку ID с запросом внутри.
- **Heuristic:** собрать ID → один запрос `WHERE id IN (...)` + карта в памяти; или JOIN с осознанием дублирования строк.

---

### 9. Миграции схемы без фреймворка

- **Fact:** инструменты: **Phinx**, **Doctrine Migrations**, самописные SQL с таблицей версий.
- **Heuristic:** миграции идемпотентны в рамках версии; никогда не править уже применённую миграцию в истории — новая миграция.

---

### 10. SQLite и продакшен

- **Fact:** SQLite удобен для тестов/edge; в высоконагруженном concurrent write — ограничения.
- **Heuristic:** явно документировать, если прод на SQLite; иначе считать dev-only по умолчанию для web-scale записи.

---

## Registry card (template-knowledge-card-v1)

### Provenance
- source_refs: `https://www.php.net/manual/en/book.pdo.php`; KB 2026-03-01.
- created_at: 2026-03-01
- updated_at: 2026-03-01

### Metadata
- card_id: KC-2026-03-01-PHP-DB-L1
- world: software.php
- layer: world
- tags: php; pdo; sql; transactions; migrations
- status: active

### Epistemic Linkage
- epistemic_basis: fact + inference
- confidence: high
- transfer_boundary: тюнинг конкретной СУБД — вендорная документация

### Core Unit
- context: сырой SQL из PHP, легаси скрипты, микросервис без ORM
- signal: SQL injection, утечки соединений, deadlock
- action: prepared statements + транзакции + профилирование запросов
- lesson: PDO не отменяет дисциплину SQL

### Operationalization
- first_adoption_task: ERRMODE_EXCEPTION + единый слой репозитория
- validation_check: статический поиск конкатенации в SQL
- success_criterion: нет сырого пользовательского ввода в SQL

### Lifecycle
- supersedes: —
- superseded_by: —
- deprecation_reason: —