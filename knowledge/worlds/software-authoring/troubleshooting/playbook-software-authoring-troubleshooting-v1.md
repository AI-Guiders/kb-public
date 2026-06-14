# Playbook: software.authoring — troubleshooting (v1)

> **Контур:** A · kb-public  
> **Когда:** «сделай красиво», god-class, switch/Kind, Skia, новый экран, DDD-мода, смешение слоёв  
> **Матрица (полная):** [`../matrix-software-cross-domain-transfer-v1.md`](../matrix-software-cross-domain-transfer-v1.md)

**Порядок:** `../status-software-authoring-v1.md` → **эта таблица** → целевой playbook → kb по вопросу. Перед cross-world: [`../knowledge-engineering/matrix-do-not-transfer-v1.md`](../knowledge-engineering/matrix-do-not-transfer-v1.md).

---

## Fast symptom router

| Симптом | Сначала | Потом | Не делать |
|---------|---------|-------|-----------|
| `switch` / `enum Kind` в renderer, handler, VM | `playbook-ooad-agent-operational-v1.md` | `playbook-domain-nouns-verbs-decomposition-v1.md` | ещё ветка в том же `switch` |
| God-class / VM > ~800 строк | OOA&D шаг 5 + nouns-verbs | `code-writing-principles-v1.md` | 20 микро-классов без домена |
| Визуал, layout, цвет, шрифт | HCI (`../hci-ux-dx/playbook-hci-core-v1.md`) | OOA&D если растёт union | Nielsen вместо типов |
| Новый экран / панель / wizard | 7-шаговый OOA&D | Avalonia playbook | пиксели без словаря |
| Биндинг, тема, Dock, axaml | [`../software-dotnet-avalonia/troubleshooting/`](../software-dotnet-avalonia/troubleshooting/) | HCI для copy | полный OOA&D |
| CSxxxx / analyzer / warning | [`../software-dotnet-tooling-roslyn/troubleshooting/`](../software-dotnet-tooling-roslyn/troubleshooting/) | code action | редизайн домена |
| PFD / cockpit / scan (метафора) | `../aviation-human-factors/kb-aviation-pfd-mfd-efis-eicas-fundamentals-v1.md` | HCI + Avalonia | FAA в code-review |
| DDD / Clean «архитектура» | `status-software-authoring-v1` + OOA&D | Track C `map-engineering-reading-v1` | папки без сущностей |
| Одна строка цвет/отступ | `code-writing-principles-v1.md` | — | OOA&D-проход |
| `*Snapshot` / DTO уже есть | nouns-verbs: presentation догоняет domain | SceneBuilder + `ISkia*Entity` | дубль домена в Control |
| Jank в `Draw` | профиль hot path, кэш layout | — | OOA&D с нуля |
| Коммит, ветка, submodule | [`../collaboration-git-pr/troubleshooting/`](../collaboration-git-pr/troubleshooting/) | — | структура классов |
| API / MCP / Telegram | `../software-integration-kb/` | — | UI entity model |

**Именованный продукт** (`[PRIMARY:…]`, layout/настройки одного IDE) — **не эта таблица:** [`work/troubleshooting/README.md`](../../../work/troubleshooting/README.md).

---

## Ложные гипотезы (software, общие)

| Гипотеза | Почему |
|----------|--------|
| «Починить Skia» при узкой колонке окна | Часто shell/layout **конкретного приложения** — см. product playbook в `work/`; иначе Avalonia troubleshooting |
| OOA&D на каждый однострочный фикс | `code-writing-principles` достаточно |
| Перенос WPF-паттерна 1:1 в Avalonia | API и lifecycle отличаются — см. Avalonia troubleshooting |

---

## Как дополнять

Новая строка — здесь и в `matrix-software-cross-domain-transfer-v1.md` § Fast symptom router (держать синхронно).

