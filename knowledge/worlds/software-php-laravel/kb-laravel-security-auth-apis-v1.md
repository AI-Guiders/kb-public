# Laravel — безопасность, аутентификация, API

**Назначение:** контур **auth** и базовых угроз в типичном Laravel-приложении (веб + API). Не заменяет OWASP ASVS и внутренние стандарты. Мир `software.laravel`.

**Порядок загрузки:** `playbook-laravel-v1.md` → этот файл → при низком уровне `kb-php-web-sessions-io-v1.md` (cookies/sessions).

---

### 1. Веб-сессии и CSRF

- **Fact:** для stateful веба Laravel использует session middleware; **CSRF-токен** для POST из Blade (и исключения для stateless API).
- **Heuristic:** 419 Page Expired — часто сессия/cookie/домен/proxy (`TrustProxies`, `SESSION_DOMAIN`, `SameSite`).
- **Heuristic:** не отключать CSRF глобально «ради удобства API»; для API — отдельные маршруты и механизм (token/cookie sanctum).

---

### 2. Sanctum vs Passport

- **Sanctum** — лёгкие API-токены (personal access), SPA authentication (cookie + same-origin), часто достаточно для первого класса API и мобильных клиентов с token storage.
- **Passport** — полноценный **OAuth2 сервер** (authorization codes, clients, scopes); избыточен, если нужен только «один секретный токен на пользователя».

- **Heuristic:** «нужен OAuth2 для сторонних приложений» → Passport; «свой SPA + свой API на том же сайте» → чаще Sanctum.
- **Confidence:** high (роли пакетов), medium (конкретная схема угроз)

---

### 3. Стартер-киты и контур входа

- **Breeze** — минимальный стек (Blade или Vue/React + Inertia по выбору).
- **Jetstream** — Livewire или Inertia, teams, 2FA, profile management (больше «из коробки»).
- **Fortify** — headless backend для auth features без UI (композиция с кастомным фронтом).

- **Heuristic:** кастомизация Jetstream глубже, чем кажется — планировать обновления мажора Laravel вместе с livewire/inertia версиями.

---

### 4. Авторизация: Gates и Policies

- **Fact:** `Gate`/`Policy` интегрированы с контейнером; в Blade `@can`, в контроллерах `$this->authorize()`.
- **Heuristic:** дублирование проверок только в middleware **и** только в контроллере — риск рассинхрона; единая политика на действие.
- **First adoption task:** для каждого чувствительного ресурса — явная policy + тест на отказ.

---

### 5. Массовое присвоение и валидация

- **Fact:** `$fillable` / `$guarded` + `Request::validate()` / Form Request — базовый барьер против mass assignment.
- **Heuristic:** `$request->all()` в `create()` без whitelist — антипаттерн.
- **Confidence:** high

---

### 6. Шифрование и секреты

- **Fact:** `APP_KEY` нужен для шифрования cookies/sessions и `Crypt`; потеря ключа = потеря сессий пользователей.
- **Heuristic:** секреты только `.env`/secret manager; `php artisan key:generate` один раз на окружение, не копировать ключ между несвязанными продаами.

---

### 7. Rate limiting

- **Fact:** `RateLimiter` и middleware `throttle` на маршрутах; для API — лимиты по пользователю/IP.
- **Heuristic:** login и password reset — обязательные узкие лимиты.

---

## Registry card (template-knowledge-card-v1)

### Provenance
- source_refs: `https://laravel.com/docs` (Authentication, Authorization, Sanctum, Passport, Security); 2026-03-01
- created_at: 2026-03-01
- updated_at: 2026-03-01
- author: agent-notes KB maintainer

### Metadata
- card_id: KC-2026-03-01-LARAVEL-SECURITY
- world: software.laravel
- layer: world
- tags: laravel; sanctum; passport; csrf; policy; oauth
- status: active

### Epistemic Linkage
- epistemic_basis: fact + inference
- evidence_type: official docs + OWASP-aware heuristics
- confidence: medium
- uncertainty: конкретные threat models и compliance
- falsification_trigger: смена рекомендованных практик в официальной документации
- transfer_boundary: не заменяет пентест и формальные аудиты

### Core Unit
- context: выбор Sanctum/Passport, 419, утечки прав
- signal: «как безопасно отдать API», «почему не пускает»
- action: policy + middleware + правильный пакет auth
- outcome: предсказуемая модель доверия
- lesson: stateful web и stateless API — разные контракты

### Operationalization
- first_adoption_task: матрица маршрутов × auth mechanism
- validation_check: тесты на 403/401; проверка CSRF на формах
- success_criterion: нет критичных маршрутов без авторизации
- rollback_or_mitigation: откат конфигов auth + ротация ключей по процедуре

### Lifecycle
- supersedes: —
- superseded_by: —
- deprecation_reason: —
