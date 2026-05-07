# Laravel — фронтенд-стеки: Blade, Livewire, Filament, Inertia

**Назначение:** выбор и границы **UI-слоёв** вокруг Laravel без привязки к одной версии пакета (версии — из `composer.lock` / `package.json`). Мир `software.laravel` + `software.web-frontend` (частично).

**Порядок загрузки:** `kb-laravel-fundamentals-v1.md` → этот файл. Auth для SPA — `kb-laravel-security-auth-apis-v1.md`.

---

### 1. Blade-first (серверный рендер)

- **Fact:** шаблоны Blade, layouts, компоненты `<x-*>`, стеки `@push`; минимум JS или Alpine точечно.
- **Heuristic:** лучший TTFB для простых форм и админок без heavy interactivity; SEO-дружелюбно из коробки.
- **Confidence:** high

---

### 2. Livewire

- **Fact:** полноценные **динамические компоненты** на сервере: состояние на бэкенде, ре-рендер фрагментов через HTTP (или morphing в новых версиях).
- **Heuristic:** удобно для «богатых форм» и админок без отдельного SPA; следить за **количеством round-trips** и размером payload.
- **Heuristic:** валидация и авторизация — на сервере в компоненте/формах Livewire; не дублировать бизнес-правила только в JS.
- **Confidence:** medium (эволюция Livewire 2/3)

---

### 3. Filament

- **Fact:** админ-панели и внутренние CRUD на базе Livewire; плагины, ресурсы, таблицы, формы.
- **Heuristic:** быстрый time-to-market для internal tools; кастомизация глубже средней — закладывать время на изучение конвенций Filament.
- **Heuristic:** обновления Filament привязаны к версиям Livewire и Laravel — планировать вместе с upgrade guide Laravel.

---

### 4. Inertia.js

- **Fact:** **SPA-подобный** UX без отдельного API: Laravel отдаёт **Inertia responses**, фронт — Vue или React (официально поддерживаемые адаптеры).
- **Heuristic:** хороший компромисс для product UI с навигацией как в SPA; общие контракты валидации через shared props.
- **Heuristic:** SEO для публичных страниц — продумать SSR (где доступно) или гибрид с Blade.

---

### 5. Сравнительная эвристика (не догма)

| Потребность | Часто подходит |
|-------------|----------------|
| Простые страницы, SEO | Blade |
| Интерактив без отдельного SPA repo | Livewire |
| Внутренняя админка из коробки | Filament |
| Продуктовый UI в стиле SPA, команда знает Vue/React | Inertia |

- **First adoption task:** одно решение на продукт (или явные границы зон Blade vs Inertia), не смешивать без стандарта.
- **Success criterion:** единый стиль auth, ошибок валидации и loading states.

---

### 6. Сборка активов

- **Fact:** Vite — современный дефолт в стартерах Laravel; `npm run build` в CI для prod.
- **Heuristic:** кеширование manifest и CDN — в playbook деплоя; не забывать `vite` директивы в Blade.

---

## Registry card (template-knowledge-card-v1)

### Provenance
- source_refs: `https://laravel.com/docs` (Blade, Frontend: Vite, starter kits); livewire.laravel.com; filamentphp.com; inertiajs.com — обобщение 2026-03-01
- created_at: 2026-03-01
- updated_at: 2026-03-01
- author: agent-notes KB maintainer

### Metadata
- card_id: KC-2026-03-01-LARAVEL-FRONTEND
- world: software.laravel
- layer: world
- tags: laravel; blade; livewire; filament; inertia; vite
- status: active

### Epistemic Linkage
- epistemic_basis: inference + fact
- evidence_type: official docs + экосистемные сайты
- confidence: medium
- uncertainty: версии Livewire/Filament и breaking changes
- falsification_trigger: смена рекомендованного bundler или стартера в Laravel docs
- transfer_boundary: не сравнение с React/Next отдельно от Laravel

### Core Unit
- context: выбор стека UI, апгрейд Filament/Livewire
- signal: «что использовать для админки/SPA»
- action: таблица эвристик + auth слой
- outcome: меньше гибридного хаоса
- lesson: один доминирующий UI-паттерн на продукт проще сопровождать

### Operationalization
- first_adoption_task: ADR «frontend stack» в репо
- validation_check: E2E на критичных user flows
- success_criterion: согласованная обработка ошибок и auth
- rollback_or_mitigation: feature flags для новых UI-модулей

### Lifecycle
- supersedes: —
- superseded_by: —
- deprecation_reason: —
