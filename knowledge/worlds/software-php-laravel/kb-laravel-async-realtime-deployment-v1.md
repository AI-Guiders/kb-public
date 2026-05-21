# Laravel — асинхронность, долгоживущие воркеры, realtime, деплой

**Назначение:** контур **очередей**, **Octane/FrankenPHP/RoadRunner**, **broadcasting/Reverb**, типичные **подводные камни состояния** и связь с деплоем. Мир `software.laravel`. База очередей — `kb-laravel-fundamentals-v1.md` §5.

**Порядок загрузки:** `playbook-laravel-v1.md` → этот файл. PHP OPcache/preload — `kb-php-fundamentals-v1.md`.

---

### 1. Классический PHP-FPM + queue workers

- **Fact:** каждый HTTP-запрос — отдельный lifecycle; **queue worker** — долгоживущий PHP-процесс, держащий приложение в памяти между jobs.
- **Heuristic:** глобальные/static синглтоны, кеш в памяти в service provider — в worker могут **устаревать** между задачами; после деплоя — **restart workers** (`queue:restart`, supervisor signal, Horizon).
- **Confidence:** high

---

### 2. Laravel Octane

- **Fact:** Octane держит приложение **загруженным** между запросами (Swoole/RoadRunner/FrankenPHP — в зависимости от конфигурации и версии docs).
- **Heuristic:** любое **мутабельное состояние** в синглтонах (коллекции в памяти, счётчики) — риск утечки между запросами; использовать stateless сервисы или явную очистку.
- **Heuristic:** `config:cache`, `route:cache` остаются важны; memory profiling обязателен при внедрении.
- **Check:** нагрузочный тест + проверка RSS процесса со временем.
- **Confidence:** medium (детали зависят от драйвера Octane)

---

### 3. FrankenPHP и RoadRunner

- **Fact:** **FrankenPHP** (Caddy/app server) и **RoadRunner** — альтернативные application servers для PHP worker-модели; интеграция с Laravel через Octane или нативные адаптеры (см. актуальные docs).
- **Heuristic:** при миграции с FPM проверять: загрузку `.env`, таймауты, лимиты тел запросов, совместимость расширений PHP.

---

### 4. Горизонтальное масштабирование очередей

- **Fact:** несколько воркеров → идемпотентность job и **блокировки** (cache lock, unique jobs) где нужно.
- **Heuristic:** cron `schedule:run` на **одной** ноде или с распределённой блокировкой — иначе дубли задач.

---

### 5. Realtime: broadcasting и Reverb

- **Fact:** Laravel Broadcasting + **Reverb** (WebSocket server) — типичный стек для push-событий на фронт; альтернативы: Pusher, Ably, self-hosted socket.io (вне first-party).
- **Heuristic:** авторизация каналов (`channels.php`) — критична; не оставлять private каналы без проверки.
- **Confidence:** medium

---

### 6. Контракты деплоя (сводка)

- После выката: `php artisan migrate --force` (по политике), `config:cache` / `route:cache` / `view:cache`, **restart queue workers / Octane**.
- Не полагаться на «старый» opcode в долгоживущих процессах без reload.

---

## Registry card (template-knowledge-card-v1)

### Provenance
- source_refs: `https://laravel.com/docs` (Queues, Horizon, Octane, Broadcasting, Reverb); 2026-03-01
- created_at: 2026-03-01
- updated_at: 2026-03-01
- author: agent-notes KB maintainer

### Metadata
- card_id: KC-2026-03-01-LARAVEL-ASYNC-RT
- world: software.laravel
- layer: world
- tags: laravel; octane; horizon; reverb; roadrunner; frankenphp
- status: active

### Epistemic Linkage
- epistemic_basis: fact + inference
- evidence_type: official Laravel docs + практики SRE
- confidence: medium
- uncertainty: конкретные цифры памяти и драйверы по версиям
- falsification_trigger: смена рекомендованной интеграции в docs
- transfer_boundary: не заменяет runbook конкретного k8s/VM

### Core Unit
- context: memory leak в Octane, дубли scheduler, WS auth
- signal: «после деплоя старое поведение», «растёт память»
- action: restart policy + stateless services + channel auth
- outcome: стабильные воркеры и предсказуемый деплой
- lesson: долгоживущий процесс ≠ FPM-запрос

### Operationalization
- first_adoption_task: документировать restart workers в CD pipeline
- validation_check: canary + memory graph после деплоя
- success_criterion: нет дрейфа состояния между запросами/jobs
- rollback_or_mitigation: откат образа + hard restart всех воркеров

### Lifecycle
- supersedes: —
- superseded_by: —
- deprecation_reason: —
