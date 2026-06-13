# Fundamentals: сборка, References и vendor API (v1)

**Мир:** `engineering.cad`

---

## Scope

Как в типичном workspace CAD-команды устроены **References**, **снимки DLL**, **HintPath** и **конфигурации** — без конкретных путей диска.

---

## Core concepts

### 1) Два слоя зависимостей

| Слой | Содержимое | Назначение |
|------|------------|------------|
| **References (git)** | ObjectArx headers, Autodesk/nanoCAD interop, EPPlus, OpenXml, … | Общие бинарники и заголовки для всех продуктов |
| **Product References** (напр. Aveva) | `Aveva.*.dll` по папкам версий продукта | API конкретных релизов E3D/ADM/TAGS |
| **NuGet** (напр. Tekla) | `TeklaOpenAPI` | Версионированный Open API |

### 2) Паттерн HintPath «установка ИЛИ снимок»

```xml
<HintPath Condition="Exists('C:\Program Files\…\vendor.dll')">…</HintPath>
<HintPath Condition="Exists('..\..\References\…\vendor.dll')">…</HintPath>
```

- CI/разработчик **без** установленного САПР собирает по снимку в repo.
- С установленным продуктом — предпочтение Program Files (актуальнее interop).

### 3) Конфигурации = продукт + TFM

- Имя `Debug_E3D310` / `Release_NC23.1_net48` кодирует **целевой хост**.
- `DefineConstants` включают тег продукта для `#if` и условных ссылок.
- Один solution может собирать **десятки** конфигураций — выбирать одну осознанно.

### 4) ObjectARX headers

- Папки по **году SDK** (`inc/`), не по году AutoCAD напрямую — но соответствие таблице Autodesk обязательно проверять по документации.

### 5) SDK / Help (концептуально)

- Папка **SDK** в workspace часто зарезервирована под **CHM/PDF/примеры** вендора.
- Может быть пустой на share — тогда справка с **установки САПР** или портала вендора.
- **References ≠ SDK**: References — для **компиляции**; SDK — для **чтения человеком**.

### 6) Что не класть в обобщённый KB

- Строки подключения к корпоративным SQL для телеметрии утилит.
- UNC-пути, внутренние wiki, имена серверов.
- Проектные модели заказчика.

---

## Anti-patterns

- Коммитить пароли в `ConnStr.txt` — только шаблон + локальный файл в деплое.
- Смешивать DLL разных версий Aveva в одну папку output.
- Ожидать, что пустая папка Autodesk в References заполнится сама — часто DLL копируют с установки один раз.

---

## Links

- [software-dotnet-csharp/kb-dotnet-fundamentals-v1.md](../software-dotnet-csharp/kb-dotnet-fundamentals-v1.md)

**Версия:** v1.0 · 2026-06-04