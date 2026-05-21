# Laravel — first-party пакеты и инструменты экосистемы

**Назначение:** карта **официальных** пакетов вокруг `laravel/framework`: зачем каждый, типичные контракты деплоя. Не заменяет docs конкретного пакета. Мир `software.laravel`.

**Порядок загрузки:** `playbook-laravel-v1.md` → этот файл.

---

### 1. Наблюдаемость и операции

- **Telescope** — отладка запросов, jobs, событий, mail (в основном **dev/stage**; в проде — осознанно, с ACL и отключением по умолчанию).
- **Horizon** — dashboard и балансировка для **Redis-очередей**; метрики, теги, пауза воркеров.
- **Pint** — code style (PHP CS Fixer wrapper); CI-контракт: `pint --test` или автофикс по политике команды.

- **Heuristic:** «тормозит очередь» → сначала Horizon/metrics + failed_jobs, не сразу масштабирование воркеров.
- **Confidence:** high

---

### 2. Поиск, платежи, интеграции

- **Scout** — full-text / драйверы (Meilisearch, Algolia, Typesense, database); синхронизация индекса с моделями.
- **Cashier (Stripe)** — подписки, webhooks, invoicing; **всегда** проверять подпись webhook и идемпотентность обработчиков.
- **Socialite** — OAuth-провайдеры для «войти через …»; секреты клиентов только в env.

- **Heuristic:** Scout без стратегии reindex → рассинхрон индекса и БД после миграций.
- **Confidence:** medium

---

### 3. DevEx и окружение

- **Sail** — Docker-обвязка для локальной разработки; не смешивать с прод-оркестратором без документации.
- **Valet** (macOS) — лёгкий локальный nginx + dnsmasq; Windows/Linux — аналоги вне этого kb.
- **Dusk** — браузерные E2E (ChromeDriver); в CI — отдельный job, детерминизм времени/сети.
- **Envoy** — задачи деплоя по SSH; секреты через agent/config, не в репо.

- **Confidence:** medium

---

### 4. Realtime (краткая отсылка)

- **Reverb** — first-party WebSocket-сервер для broadcasting (см. детали в `kb-laravel-async-realtime-deployment-v1.md`).

---

### 5. Выбор пакета (эвристика)

| Симптом | Куда смотреть |
|---------|----------------|
| Нужен UI очередей Redis | Horizon |
| Нужен профайлинг запросов в dev | Telescope |
| Нужен поиск по моделям | Scout + драйвер |
| Подписки Stripe | Cashier |
| OAuth login | Socialite |
| Локально «как на проде» контейнеры | Sail |
| E2E в браузере | Dusk |

- **First adoption task:** в `composer.json` отметить, какие `laravel/*` пакеты реально используются (не «повисшие» зависимости).
- **Success criterion:** каждый пакет имеет владельца и env-переменные в README.

---

## Registry card (template-knowledge-card-v1)

### Provenance
- source_refs: `https://laravel.com/docs` (разделы Horizon, Telescope, Scout, Cashier, Socialite, Sail, Dusk, Pint); 2026-03-01
- created_at: 2026-03-01
- updated_at: 2026-03-01
- author: agent-notes KB maintainer

### Metadata
- card_id: KC-2026-03-01-LARAVEL-PACKAGES
- world: software.laravel
- layer: world
- tags: laravel; horizon; telescope; scout; cashier; sail
- status: active

### Epistemic Linkage
- epistemic_basis: fact + inference
- evidence_type: official Laravel docs
- confidence: medium
- uncertainty: версии пакетов и breaking changes в минорах
- falsification_trigger: удаление/переименование пакета в официальной экосистеме
- transfer_boundary: сторонние пакеты (Filament, Spatie и т.д.) — в других kb или точечно

### Core Unit
- context: выбор инструмента, дебаг очередей/поиска/платежей
- signal: «что поставить из laravel/*»
- action: таблица симптом → пакет → docs
- outcome: меньше случайных зависимостей
- lesson: first-party ≠ автоматически нужен в каждом проекте

### Operationalization
- first_adoption_task: инвентаризация laravel/* в composer.json
- validation_check: smoke сценарий для каждого включённого пакета
- success_criterion: нет неиспользуемых тяжёлых пакетов в проде
- rollback_or_mitigation: отключение service provider / удаление пакета по плану

### Lifecycle
- supersedes: —
- superseded_by: —
- deprecation_reason: —
