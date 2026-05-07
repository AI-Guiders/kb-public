# Wissance WebApiToolkit — полный стек слоёв (fundamental → operational)

Источник: [Wissance/WebApiToolkit](https://github.com/Wissance/WebApiToolkit), README и Wiki.

## Назначение KB
Эта KB-страница описывает **все слои**, которые нужны агентам, чтобы **проектировать, собирать, разворачивать и сопровождать** REST backend на базе WebApiToolkit.

**База идеи** (из README): библиотека позволяет поднять CRUD REST API «почти одной строкой» за счёт:
- автогенерации контроллеров (assembly on-the-fly)
- вынесения логики в **Manager** слой
- стандартизации ответов/ошибок и query-поведения

README: https://raw.githubusercontent.com/Wissance/WebApiToolkit/master/README.md

---

## L0 — Fundamental (концептуальные основы)

### L0.1 Architectural principle: Controller ≈ thin, Manager ≈ core
- Контроллеры (REST/gRPC/SignalR) должны быть **тонкими адаптерами транспорта**.
- Вся прикладная логика и работа с хранилищем концентрируется в **Manager**.

README заявляет общий контракт через `IModelManager` и возможность переиспользовать один Manager для разных транспортов.

### L0.2 Standardization principle
Цель — **одинаковое поведение** у всех CRUD эндпоинтов:
- единый формат ответа/ошибок
- единые paging/sorting/filter правила
- единые bulk правила

(в README: “Output of all REST methods is standardize”, “Unified error format out of the box”, paging/sorting/filter, bulk)

---

## L1 — Library/Package layer (что подключать)

### L1.1 Основные пакеты
По README (NuGet бейджи):
- `Wissance.WebApiToolkit.Core` — базовые контракты/контроллеры/менеджеры/утилиты
- `Wissance.WebApiToolkit.Ef` — EF-ориентированная реализация и DI entrypoints
- `Wissance.WebApiToolkit.AWS.S3` — S3 utilities (опционально)

### L1.2 Target frameworks
`Wissance.WebApiToolkit.Core` и `Wissance.WebApiToolkit.Ef` таргетят `net6.0;net8.0;net9.0`.

---

## L2 — Code-generation & Composition layer (как появляется контроллер)

### L2.1 On-the-fly generation
Контроллер генерируется в runtime (assembly) и подключается к MVC как application part.

### L2.2 DI entrypoints (точки входа)
Ключевые entrypoints (EF пакет):
- `Wissance.WebApiToolkit.Ef.Extensions.ServiceCollectionExtensions.AddSimplifiedAutoController(...)`
- `Wissance.WebApiToolkit.Ef.Extensions.ServiceCollectionExtensions.AddFullyConfiguredAutoController(...)`

Обе функции делают 3 вещи:
- **регистрируют scoped manager** (через `EfBasedManagerFactory`)
- **генерируют controller assembly** (через `OnTheFlyServicesGenerator.GenerateController(...)`)
- **возвращают Assembly**

Источник кода: https://raw.githubusercontent.com/Wissance/WebApiToolkit/a1016f6631d3a7bcc76eb986ff6abcd1b0e5e91f/Wissance.WebApiToolkit/Wissance.WebApiToolkit.Ef/Extensions/ServiceCollectionExtensions.cs

### L2.3 Подключение в ASP.NET Core
Рекомендуемый шаблон (README):
1) вызвать `services.AddSimplifiedAutoController<...>(...)` → получить `Assembly`
2) `services.AddControllers().AddApplicationPart(assembly).AddControllersAsServices();`

README: https://raw.githubusercontent.com/Wissance/WebApiToolkit/master/README.md

---

## L3 — Domain & Contract layer (что должен предоставить проект)

### L3.1 Entity identity contract
Для автоконтроллера есть generic constraints:
- `TObj : class, IModelIdentifiable`
- `TId : IComparable`

Т.е. сущность должна реализовать контракт идентификации, а ключ быть сравнимым.

Источник: `ServiceCollectionExtensions.cs` (см. L2.2).

### L3.2 Resource naming contract
Тебе нужен **стабильный `resourceName`** (строка), из которого строится имя сборки/контроллера и маршрутизация ресурса.

---

## L4 — Query semantics layer (paging/sorting/filter)

### L4.1 Read filter contract
Generic constraint:
- `TFilter : class, IReadFilterable`

---

## L5 — Application/Manager layer (ядро приложения)

### L5.1 Stable boundary
Менеджер — это boundary между транспортом и persistence/business.

README: “support to work with any persistent storage (`IModelManager` interface)”

### L5.2 EF implementation path
EF путь подразумевает:
- `DbContext`
- EF-based manager factory:
  - `EfBasedManagerFactory.CreateSimplifiedManager(...)`
  - `EfBasedManagerFactory.CreateFullyDefinedManager(...)`

Источник: `ServiceCollectionExtensions.cs` (см. L2.2).

### L5.3 Extensibility path (как агент расширяет поведение)
Чтобы агент мог “строить приложения”, в KB фиксируем стандартные варианты расширения:
- **Custom manager**: своя реализация `IModelManager` (или composition поверх EF менеджера)
- **ManagerConfiguration**: использовать `AddFullyConfiguredAutoController(...)` и `ManagerConfiguration` для тонкой настройки поведения менеджера
- **FilterFunc**: в simplified-варианте есть `filterFunc` для запрета/разрешения элементов (вход: объект; выход: bool)

---

## L6 — Persistence & Infrastructure layer

### L6.1 EF DbContext
Проект должен владеть:
- конфигурацией `DbContext` (connection string, migrations, provider)
- жизненным циклом/миграциями

### L6.2 Storage portability
Если нужна БД не EF — реализовать `IModelManager` для другого storage.

---

## L7 — API Surface layer (CRUD + Bulk)

### L7.1 CRUD surface
Контроллеры предоставляют `GET/POST/PUT/DELETE` в едином формате.

### L7.2 Bulk surface
README: bulk `Create/Update/Delete` на уровне контроллера и интерфейса.

---

## L8 — Cross-cutting layer (responses, errors, logging)

### L8.1 Unified response & error model
README заявляет унификацию ответов и ошибок.

---

## L9 — Security layer (обязательное поверх автогенерации)
Автогенерация CRUD **не** закрывает требования безопасности.

---

## L10 — Testing & Quality layer

---

## L11 — Delivery layer (build/release)

---

## L12 — Operational layer (deploy, run, support)

---

## L13 — Agent-facing “recipe” (что агент должен уметь сделать автоматически)

---

## API Contract (exact)
Это точная спецификация, выведенная из базовых контроллеров WebApiToolkit.

### Base routes
- **CRUD/read** контроллеры: `api/[controller]`
  - задаётся атрибутом `[Route("api/[controller]")]`
  - источник: `Wissance.WebApiToolkit.Core.Controllers.BasicReadController` и наследники

Источник: https://raw.githubusercontent.com/Wissance/WebApiToolkit/a1016f6631d3a7bcc76eb986ff6abcd1b0e5e91f/Wissance.WebApiToolkit/Wissance.WebApiToolkit.Core/Controllers/BasicReadController.cs

- **Bulk** контроллеры: `api/bulk/[controller]`
  - задаётся атрибутом `[Route("api/bulk/[controller]")]`
  - источник: `Wissance.WebApiToolkit.Core.Controllers.BasicBulkCrudController`

Источник: https://raw.githubusercontent.com/Wissance/WebApiToolkit/a1016f6631d3a7bcc76eb986ff6abcd1b0e5e91f/Wissance.WebApiToolkit/Wissance.WebApiToolkit.Core/Controllers/BasicBulkCrudController.cs

---

### Endpoints: Read (list)
`GET /api/{ControllerName}`

**Query parameters**:
- `page` (int?, default = 1, min = 1)
- `size` (int?, default = 25, min = 1)
- `sort` (string) — имя поля/свойства для сортировки
- `order` (string) — `asc` или `desc` (любой другой ввод → трактуется как `asc`)
- `additionalFilters` — параметры фильтрации, собираемые через `TFilter : IReadFilterable` → `IDictionary`

Факты:
- значения по умолчанию: `page=1`, `size=25` (см. `PagingUtils`)
- порядок сортировки: если `order` пустой/неизвестный → `Ascending` (см. `SortOption`)

Источники:
- `BasicReadController.ReadAsync(...)`: https://raw.githubusercontent.com/Wissance/WebApiToolkit/a1016f6631d3a7bcc76eb986ff6abcd1b0e5e91f/Wissance.WebApiToolkit/Wissance.WebApiToolkit.Core/Controllers/BasicReadController.cs
- `PagingUtils`: https://raw.githubusercontent.com/Wissance/WebApiToolkit/a1016f6631d3a7bcc76eb986ff6abcd1b0e5e91f/Wissance.WebApiToolkit/Wissance.WebApiToolkit.Core/Utils/PagingUtils.cs
- `SortOption`: https://raw.githubusercontent.com/Wissance/WebApiToolkit/a1016f6631d3a7bcc76eb986ff6abcd1b0e5e91f/Wissance.WebApiToolkit/Wissance.WebApiToolkit.Core/Data/SortOption.cs
- `IReadFilterable`: https://raw.githubusercontent.com/Wissance/WebApiToolkit/a1016f6631d3a7bcc76eb986ff6abcd1b0e5e91f/Wissance.WebApiToolkit/Wissance.WebApiToolkit.Core/Data/IReadFilterable.cs
- `EmptyAdditionalFilters`: https://raw.githubusercontent.com/Wissance/WebApiToolkit/a1016f6631d3a7bcc76eb986ff6abcd1b0e5e91f/Wissance.WebApiToolkit/Wissance.WebApiToolkit.Core/Data/EmptyAdditionalFilters.cs

**Response body envelope**: `OperationResultDto<PagedDataDto<TRes>>`
- `OperationResultDto<T>` JSON содержит:
  - `Success: bool`
  - `Message: string`
  - `Data: T`
- поле `Status: int` в JSON **не сериализуется** (помечено `[JsonIgnore]`), но HTTP status код выставляется в `HttpContext.Response.StatusCode = result.Status`

Источники:
- `BasicReadController` (выставление status + возвращаемое тело): https://raw.githubusercontent.com/Wissance/WebApiToolkit/a1016f6631d3a7bcc76eb986ff6abcd1b0e5e91f/Wissance.WebApiToolkit/Wissance.WebApiToolkit.Core/Controllers/BasicReadController.cs
- `OperationResultDto`: https://raw.githubusercontent.com/Wissance/WebApiToolkit/a1016f6631d3a7bcc76eb986ff6abcd1b0e5e91f/Wissance.WebApiToolkit/Wissance.WebApiToolkit.Dto/OperationResultDto.cs
- `PagedDataDto`: https://raw.githubusercontent.com/Wissance/WebApiToolkit/a1016f6631d3a7bcc76eb986ff6abcd1b0e5e91f/Wissance.WebApiToolkit/Wissance.WebApiToolkit.Dto/PagedDataDto.cs

**`PagedDataDto<T>` поля**:
- `Page: long`
- `Total: long`
- `Pages: long`
- `Data: IList<T>`

---

### Endpoints: Read (by id)
`GET /api/{ControllerName}/{id}`

- `{id}` берётся из route (`[HttpGet("{id}")]`)
- Response: `OperationResultDto<TRes>`
- HTTP status выставляется по `result.Status`

Источник: `BasicReadController.ReadByIdAsync(...)`: https://raw.githubusercontent.com/Wissance/WebApiToolkit/a1016f6631d3a7bcc76eb986ff6abcd1b0e5e91f/Wissance.WebApiToolkit/Wissance.WebApiToolkit.Core/Controllers/BasicReadController.cs

---

### Endpoints: CRUD
Базовые mutating-операции реализованы в `BasicCrudController` (на базе `api/[controller]`).

- `POST /api/{ControllerName}`
  - body: `TRes`
  - response: `OperationResultDto<TRes>`

- `PUT /api/{ControllerName}/{id}`
  - body: `TRes`
  - response: `OperationResultDto<TRes>`

- `DELETE /api/{ControllerName}/{id}`
  - response body: отсутствует (метод возвращает `Task`, но выставляет `HttpContext.Response.StatusCode`)

Источник: `BasicCrudController`: https://raw.githubusercontent.com/Wissance/WebApiToolkit/a1016f6631d3a7bcc76eb986ff6abcd1b0e5e91f/Wissance.WebApiToolkit/Wissance.WebApiToolkit.Core/Controllers/BasicCrudController.cs

---

### Endpoints: Bulk
Базовые bulk-операции реализованы в `BasicBulkCrudController` (на базе `api/bulk/[controller]`).

- `POST /api/bulk/{ControllerName}`
  - body: `TRes[]`
  - response: `OperationResultDto<TRes[]>`

- `PUT /api/bulk/{ControllerName}`
  - body: `TRes[]`
  - response: `OperationResultDto<TRes[]>`

- `DELETE /api/bulk/{ControllerName}?id={id1}&id={id2}...`
  - query: `id: TId[]`
  - response body: отсутствует (метод возвращает `Task`, но выставляет status)

Источник: `BasicBulkCrudController`: https://raw.githubusercontent.com/Wissance/WebApiToolkit/a1016f6631d3a7bcc76eb986ff6abcd1b0e5e91f/Wissance.WebApiToolkit/Wissance.WebApiToolkit.Core/Controllers/BasicBulkCrudController.cs

---

### Manager contract (exact)
Контроллеры вызывают `IModelManager<TRes, TObj, TId>`.

Методы:
- `CreateAsync(TRes)` → `OperationResultDto<TRes>`
- `BulkCreateAsync(TRes[])` → `OperationResultDto<TRes[]>`
- `UpdateAsync(TId, TRes)` → `OperationResultDto<TRes>`
- `BulkUpdateAsync(TRes[])` → `OperationResultDto<TRes[]>`
- `DeleteAsync(TId)` → `OperationResultDto<bool>`
- `BulkDeleteAsync(TId[])` → `OperationResultDto<bool>`
- `GetAsync(page,size,sorting,parameters)` → `OperationResultDto<Tuple<IList<TRes>, long>>`
- `GetByIdAsync(TId)` → `OperationResultDto<TRes>`

Источник: `IModelManager`: https://raw.githubusercontent.com/Wissance/WebApiToolkit/a1016f6631d3a7bcc76eb986ff6abcd1b0e5e91f/Wissance.WebApiToolkit/Wissance.WebApiToolkit.Core/Managers/IModelManager.cs

---

### Operational notes (важно для агентского генератора)
- **HTTP status** берётся из `OperationResultDto.Status`, но **в JSON его нет** → клиентам нельзя полагаться на наличие `status` в теле.
- Для `DELETE` (и обычного, и bulk) контроллер возвращает `Task`/пустой body → клиенты должны смотреть на HTTP status.
- `sort` поддерживает **одну колонку** (как минимум на уровне контракта `SortOption`).
- `order` принимает только `asc|desc` (case-insensitive) → иначе `asc`.
- `page/size` не могут выключить пагинацию: “no option to receive all data without paging” (комментарий в `BasicReadController`).

---

## Пример wiring (из TestApp)
В TestApp показан вариант с `AddFullyConfiguredAutoController(...)` + `ManagerConfiguration`.

Источник: https://raw.githubusercontent.com/Wissance/WebApiToolkit/a1016f6631d3a7bcc76eb986ff6abcd1b0e5e91f/Wissance.WebApiToolkit/Wissance.WebApiToolkit.TestApp/Startup.cs

---

## Ссылки
- Репо: https://github.com/Wissance/WebApiToolkit
- README: https://raw.githubusercontent.com/Wissance/WebApiToolkit/master/README.md
- Wiki: https://github.com/Wissance/WebApiToolkit/wiki
- DI entrypoints (EF): https://raw.githubusercontent.com/Wissance/WebApiToolkit/a1016f6631d3a7bcc76eb986ff6abcd1b0e5e91f/Wissance.WebApiToolkit/Wissance.WebApiToolkit.Ef/Extensions/ServiceCollectionExtensions.cs
## TFilter template (exact pattern for agents)
Этот раздел нужен, чтобы агент мог **автоматически генерировать фильтры** для `GET /api/{Controller}`.

### Факт из WebApiToolkit
`BasicReadController.ReadAsync(...)` получает `TFilter additionalFilters` и делает:
- `additionalFilters.SelectFilters()` → `IDictionary additionalQueryParams`
- передаёт это в `Manager.GetAsync(..., parameters: additionalQueryParams)`

Источник: `BasicReadController.ReadAsync(...)`: https://raw.githubusercontent.com/Wissance/WebApiToolkit/a1016f6631d3a7bcc76eb986ff6abcd1b0e5e91f/Wissance.WebApiToolkit/Wissance.WebApiToolkit.Core/Controllers/BasicReadController.cs

Контракт фильтра:
- `TFilter : IReadFilterable`
- `IReadFilterable.SelectFilters(): IDictionary`

Источник: `IReadFilterable`: https://raw.githubusercontent.com/Wissance/WebApiToolkit/a1016f6631d3a7bcc76eb986ff6abcd1b0e5e91f/Wissance.WebApiToolkit/Wissance.WebApiToolkit.Core/Data/IReadFilterable.cs

---

### Правила для агентов (обязательные)
- **Правило 1 — ключи словаря**: ключи в `IDictionary` должны быть **стабильными** и совпадать с тем, что ожидает реализация `IModelManager.GetAsync(..., parameters)`.
  - По умолчанию удобно использовать те же имена, что и в query (`from`, `to`, `status`, …).
- **Правило 2 — не класть null/пустое**: `SelectFilters()` должен исключать `null`, пустые строки, пустые коллекции.
- **Правило 3 — типы значений**: клади в словарь значения в типах, которые менеджер реально умеет обработать (обычно `string`, `int`, `bool`, `DateTime`, arrays).
- **Правило 4 — имена query-параметров**: если нужно фиксированное имя в URL, используй `[FromQuery(Name = "...")]` на свойстве.

---

### Шаблон `TFilter` (рекомендуемый)
Пример фильтра, который агент может генерировать “по умолчанию”:

```csharp
using System;
using System.Collections;
using System.Collections.Generic;
using Microsoft.AspNetCore.Mvc;
using Wissance.WebApiToolkit.Core.Data;

public sealed class MyResourceFilters : IReadFilterable
{
    // Пример диапазона дат: ?from=2022-01-01&to=2024-12-31
    [FromQuery(Name = "from")]
    public DateTime? From { get; init; }

    [FromQuery(Name = "to")]
    public DateTime? To { get; init; }

    // Пример точного совпадения: ?status=Active
    [FromQuery(Name = "status")]
    public string? Status { get; init; }

    // Пример числового фильтра: ?minScore=10
    [FromQuery(Name = "minScore")]
    public int? MinScore { get; init; }

    // Пример мульти-значения: ?id=1&id=2&id=3
    [FromQuery(Name = "id")]
    public int[]? Id { get; init; }

    public IDictionary SelectFilters()
    {
        var dict = new Dictionary<string, object>();

        if (From is not null) dict["from"] = From.Value;
        if (To is not null) dict["to"] = To.Value;

        if (!string.IsNullOrWhiteSpace(Status)) dict["status"] = Status!;
        if (MinScore is not null) dict["minScore"] = MinScore.Value;

        if (Id is { Length: > 0 }) dict["id"] = Id;

        return dict;
    }
}
```

### Как агенту связать `TFilter` с контроллером
- Для автогенерации через `AddSimplifiedAutoController<..., TFilter>` / `AddFullyConfiguredAutoController<..., TFilter>` — передай этот тип `TFilter` как generic параметр.
- Для ручных контроллеров на базе `BasicReadController<TRes, TObj, TId, TFilter>` — укажи `TFilter` в generic параметрах.

### Пустой фильтр
Если фильтров нет — используй `EmptyAdditionalFilters`.

Источник: https://raw.githubusercontent.com/Wissance/WebApiToolkit/a1016f6631d3a7bcc76eb986ff6abcd1b0e5e91f/Wissance.WebApiToolkit/Wissance.WebApiToolkit.Core/Data/EmptyAdditionalFilters.cs