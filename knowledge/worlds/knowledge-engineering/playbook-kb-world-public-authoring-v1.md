# Playbook: авторинг **любого** мира и kb под kb-public (v1)

**Назначение:** обязательный контракт для **агента и человека** при создании или существенной правке файлов, которые **попадают в публичную сборку** (`build-public-kb.ps1` → kb-public). Это **не** «само собой» — проверять **до коммита**, даже если материал пока только в полном каноне.

**Область:** **каждый** каталог `knowledge/worlds/<slug>/` — без исключения по домену (`engineering-cad`, `software-dotnet-csharp`, `cognition-language-acquisition`, `medicine-evidence`, `knowledge-engineering`, …). Файл лежит в `knowledge-engineering/` только как **мета-playbook** канона; правило **не** ограничено миром knowledge.engineering.

**Связано:** [`PUBLISHING.md`](../../PUBLISHING.md) · [`templates/worlds/README.md`](../../templates/worlds/README.md) · [`playbook-kb-operational-freshness-v1.md`](playbook-kb-operational-freshness-v1.md)

---

## Когда обязателен

| Действие | Где |
|----------|-----|
| Новый или расширенный **любой мир** | `knowledge/worlds/<slug>/` — **любой** slug (README, status, playbook, fundamentals, map, troubleshooting A) |
| Новая строка **Domain Entry Map** | `index-knowledge-router-v1.md` (и при необходимости supplement) |
| **Fundamentals / operational** в `worlds/` | `kb-*-fundamentals-v1.md`, `playbook-*-operational-v1.md` |
| Правки **hub** `worlds/README.md`, каталоги миров | любой текст, уходящий в kb-public |

**Не заменяет:** слой **`work/`** (там **можно** scope, пути, внутренние имена) и **`personal/`** (не публикуется).

---

## Допущение по умолчанию

Всё под **`knowledge/worlds/`** (кроме путей из **`public-kb.ignore`**) **будет** скопировано в kb-public. Пиши так, будто файл уже читает внешний человек без доступа к твоему диску и внутренним карточкам.

**Разделение слоёв:**

| Слой | Содержание | Публично |
|------|------------|----------|
| **`worlds/<slug>/`** | vendor-neutral предметка: платформы, API-модели, сборка, общие playbooks | **да** |
| **`work/projects/…`** | scope, clone, диск, лицензии команды, runbook репо | **нет** |
| **`personal/`** | личное | **нет** |

Operational playbook **внутри `worlds/`** описывает **как агент ходит по kb**, а не «где лежит клон на D:\…».

---

## Вычистить перед сохранением (чеклист)

### 1. Операционка и идентификаторы

- [ ] Нет **`[SCOPE:…]`**, **`[PRIMARY:…]`**, внутренних **project-id** / codename продуктов (если не общеизвестный публичный продукт вендора).
- [ ] Нет ссылок и отсылок к **`knowledge/work/`**, **`work/projects/`**, «см. карточку в work».
- [ ] Нет **машинных путей** (`D:\…`, `C:\Users\…`, UNC, внутренние FQDN, URL Confluence/wiki команды).
- [ ] Нет **ConnStr**, токенов, ключей лицензий, имён внутренних SQL/серверов.

### 2. Бренды и имена

| Можно | Нельзя (в `worlds/`) |
|-------|----------------------|
| Публичные **вендоры и платформы** (Autodesk, AVEVA, Tekla, Microsoft, Nanosoft, …) | Внутренние кодовые имена линейки продуктов, employer-specific стеки |
| Открытые **стандарты**, NuGet, публичные API-имена | Клиенты, заказчики, внутренние монорепо без публичного имени |
| Общеизвестные **open-source** проекты по делу | «Наш продукт X», unless X is genuinely public brand |

При сомнении: **обобщить** («multi-CAD plugin repository», «managed addin») или вынести в **`work/`**.

### 3. Роутер и hub

- [ ] В **Domain Entry Map** нет колонки «диск» / путей к `work/`.
- [ ] В **README мира** нет блока «указатель на work» — только фраза, что clone/диск **вне kb** (без пути в дереве канона).

### 4. Слой operational vs fundamentals

- [ ] **Fundamentals** — определения, anti-patterns, vendor docs; без «как у нас в SSCADRepo».
- [ ] **Operational в `worlds/`** — порядок загрузки kb, Roslyn, verify; без привязки к частному workspace.

---

## Процедура агента (кратко)

1. Создать/править по шаблонам **`templates/worlds/`**.
2. Пройти чеклист § «Вычистить» (включая `grep` по новому каталогу: `work/`, `SCOPE:`, `D:\\`, внутренние codename).
3. При новом миру — обновить **router** без operational-хвостов.
4. Перед пушем в публичное зеркало (если maintainer): **`scripts/build-public-kb.ps1`** и выборочно просмотреть `dist/public-kb/knowledge/worlds/<slug>/`.
5. Внутреннюю operationalку (scope, clone, license governance) — только **`work/projects/<scope>/`**.

---

## Anti-patterns

- «Уберём URSA в следующем коммите» — **сразу** писать нейтрально в `worlds/`.
- Дублировать в fundamentals то, что уже в **`work/`**, «чтобы агенту было удобнее» — агент в полном каноне читает work отдельно.
- Ссылаться на **`work/`** в публичном тексте «для полноты» — в kb-public ссылка битая и раскрывает структуру private-слоя.
- Класть **`playbook-*-operational`** в `worlds/` с содержанием clone/scope — такой operational → в **`work/`** или сузить до kb-only.

---

## Links

| Нужно | Файл |
|--------|------|
| Исключения путей | `knowledge/public-kb.ignore` |
| Политика публикации | `PUBLISHING.md` |
| Шаблоны миров | `templates/worlds/` |
| One-pager | `kb-one-pager-structure-and-protocols-v1.md` § Публикация |

**Версия:** v1.1 · 2026-06-05
