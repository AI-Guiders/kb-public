# PHP — веб-вход, сессии, cookies, потоки (нативный слой)

**Назначение:** фундамент **веб-части без фреймворка**: суперглобалы, сессии, заголовки, загрузка файлов, потоки. Мир **`software.php`**. Фреймворки (Laravel Request/Response) — поверх этих механизмов.

---

### 1. Суперглобалы и доверие к входу

- **Fact:** `$_GET`, `$_POST`, `$_COOKIE`, `$_SERVER`, `$_FILES` заполняются SAPI; значения **всегда строки** (кроме структуры массивов); `$_REQUEST` — объединение по настройкам (не использовать как безопасный «универсальный» источник).
- **Heuristic:** валидация через `filter_input`, `filter_var`, явные схемы; не использовать сырые суперглобалы в глубине домена — прогон через слой Input DTO.

---

### 2. CSRF, формы, методы HTTP

- **Fact:** PHP не навязывает CSRF-защиту; state-changing запросы должны защищаться токеном/двойной cookie и т.д. на уровне приложения.
- **Heuristic:** для cookie-session приложений — синхронизировать политику SameSite с моделью CSRF; не полагаться только на `Referer`.

---

### 3. Сессии: механика и fixation

- **Fact:** `session_start()` поднимает хранилище (файлы по умолчанию, redis/memcached через handler); идентификатор в cookie `PHPSESSID` (имя настраивается).
- **Heuristic:** при повышении привилегий — **`session_regenerate_id(true)`** против fixation; хранить в сессии только serializable данные; не класть тяжёлые объекты с открытыми ресурсами.

---

### 4. Параметры cookie (session и свои)

- **Fact:** `session_set_cookie_params` и `setcookie`/`setrawcookie` принимают `lifetime`, `path`, `domain`, `secure`, `httponly`, `samesite`.
- **Heuristic:** прод на HTTPS — `secure=true`, `httponly=true` для session cookie; `samesite=Lax` или `Strict` по модели (API cross-site — отдельная политика).

---

### 5. Заголовки: `header()`, ранний вывод

- **Fact:** заголовки должны уйти до тела; любой вывод (echo, BOM UTF-8 в include, warning) ломает установку заголовков.
- **Heuristic:** `output_buffering` в dev может маскировать проблему — в проде лучше устранить ранний вывод; для редиректов — `exit` после `header('Location:...')`.

---

### 6. Загрузка файлов `$_FILES`

- **Fact:** PHP кладёт временный путь, оригинальное имя, MIME из клиента (не доверять), размер, код ошибки загрузки.
- **Heuristic:** проверять `UPLOAD_ERR_OK`; перемещать через `move_uploaded_file`; **не** использовать клиентское имя в пути; хранить вне webroot или через прокси; скан на malware — вне зоны PHP-only KB.

---

### 7. Path traversal и раскрытие пути

- **Fact:** `include`, `file_get_contents`, `readfile` с пользовательским фрагментом пути опасны.
- **Heuristic:** allowlist путей или chroot-логика; `realpath` + проверка префикса базовой директории.

---

### 8. Потоки и обёртки `php://`

- **Fact:** stream API (`fopen`, `file_get_contents` с контекстом) поддерживает обёртки `http://`, `file://`, `php://memory`, `php://temp` и т.д.
- **Heuristic:** удалённые URL в `fopen` — осознанно (SSRF-риск); таймауты и лимиты через `stream_context_create`.

---

### 9. JSON и HTTP API без фреймворка

- **Fact:** `json_encode`/`json_decode`; флаги `JSON_THROW_ON_ERROR` (7.3+) для явных исключений.
- **Heuristic:** для API — явный `Content-Type: application/json`; глубина и размер тела ограничивать на веб-сервере и в приложении.

---

### 10. Встроенный сервер `php -S`

- **Fact:** однопоточный dev-сервер; не для продакшена.
- **Heuristic:** не воспроизводить на нём поведение fpm под нагрузкой; использовать только локальную разработку.

---

## Registry card (template-knowledge-card-v1)

### Provenance
- source_refs: `https://www.php.net/manual/en/reserved.variables.php`; OWASP session/cookie cheat sheets (обобщение); KB 2026-03-01.
- created_at: 2026-03-01
- updated_at: 2026-03-01

### Metadata
- card_id: KC-2026-03-01-PHP-WEB-L1
- world: software.php
- layer: world
- tags: php; http; session; cookies; upload; streams
- status: active

### Epistemic Linkage
- epistemic_basis: fact + inference
- confidence: high
- transfer_boundary: конкретные лимиты nginx/apache — вне этого файла

### Core Unit
- context: чистый PHP веб, legacy endpoints, отладка «headers already sent»
- signal: сессия теряется, файл не заливается, редирект не работает
- action: пройти §1–8; проверить SAPI и ini
- lesson: суперглобалы недоверенны; сессия требует дисциплины

### Operationalization
- first_adoption_task: чек-лист cookie flags + regenerate_id на login
- validation_check: тесты сессии и upload с ошибками клиента
- success_criterion: нет утечек пути и сырого MIME в решениях

### Lifecycle
- supersedes: —
- superseded_by: —
- deprecation_reason: —