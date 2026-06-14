# Принципы написания кода (C# / .NET) v1

Публичный канон для **kb-public** и роутера: нормы стиля, асинхронности и работы в репозитории. **Расширенная версия, датированные постмортемы и черновые заметки** — в `knowledge/work/coding/code-writing.md` (в выгрузке без `work/` недоступен).

Этот файл **не заменяет** официальную документацию Microsoft: [Framework Design Guidelines](https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/), [C# coding conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions), [identifier names](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/identifier-names).

---

## Опорные внешние ссылки

| Тема | Ссылка |
|------|--------|
| Соглашения по C# (docs) | [Common C# code conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions) |
| Имена | [Identifier names](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/identifier-names) |
| Стиль .NET Runtime | [coding-style.md](https://github.com/dotnet/runtime/blob/main/docs/coding-guidelines/coding-style.md) |
| Публичные API | [Framework Design Guidelines](https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/) |
| `ConfigureAwait` | [ConfigureAwait FAQ](https://devblogs.microsoft.com/dotnet/configureawait-faq/) |
| `IDisposable` / `using` | [using statement](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/using-statement), [`IAsyncDisposable`](https://learn.microsoft.com/en-us/dotnet/api/system.iasyncdisposable) |
| `HttpClient` | [HttpClientFactory / устойчивые HTTP-вызовы](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/implement-resilient-applications/use-httpclientfactory-to-implement-resilient-http-requests) |
| Культура, форматы | [`CultureInfo`](https://learn.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo) (`InvariantCulture` vs `CurrentCulture`) |
| Логирование | [Logging in .NET](https://learn.microsoft.com/en-us/dotnet/core/extensions/logging) |
| Уязвимости NuGet | [`dotnet list package`](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-list-package) (в т.ч. `--vulnerable`) |

Инструменты: [.editorconfig](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/code-style-rule-options), `dotnet format`, анализаторы (`Microsoft.CodeAnalysis.NetAnalyzers` и правила проекта).

---

## Именование (кратко)

- Типы, методы, свойства, события — `PascalCase`; параметры и локальные — `camelCase`.
- Интерфейсы — префикс `I`; атрибуты — суффикс `Attribute`.
- Приватные поля — часто `_camelCase`; статические приватные — `s_`; thread-static — `t_` (см. runtime guide).
- Не использовать `__` подряд в именах (зарезервировано компилятором).
- Ясность важнее краткости; аббревиатуры — только общепринятые.

---

## Вёрстка и формат

- Скобки Allman; отступ как в проекте; явная видимость у членов типа.
- Согласованность с файлом/компонентом и `.editorconfig`; новый код не ломает стиль соседнего кода без причины.

---

## Язык и надёжность

- Возможности актуального `LangVersion`; nullable reference types — осмысленные контракты, без злоупотребления `!`.
- `var`, когда тип очевиден; иначе явный тип.
- Ключевые слова типов (`string`, `int`), не `System.String` в обычном коде.
- Исключения — ловить только обрабатываемое; не использовать исключения для обычного control flow.
- LINQ — для читаемости; на hot path — измерять.

---

## Инженерные принципы (кратко)

- **Магические числа и строки** — по возможности заменять **именованными константами/enum**, имя отражает смысл; «голое» число/строка допустимы, если контекст однозначен — иначе это сознательное исключение.
- **SOLID, DRY, KISS** — ориентиры, не догма; отступление нормально, если **осознанно** (зачем и какой ценой).
- **Композиция важнее наследования**; глубокие иерархии и «базовый класс на всё» — только при явной пользе. См. [Framework Design Guidelines](https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/) (в т.ч. устойчивые абстракции, члены типов).
- **Разделение ответственности**: узкие типы и методы; зависимости — через абстракции/конструктор там, где это упрощает тесты и смену реализаций.

---

## Асинхронность

- `async`/`await` для I/O; избегать sync-over-async (`.Result`, `.Wait()`, `GetAwaiter().GetResult()`) без веской причины и комментария.
- `async void` — только обработчики событий UI; иначе `Task` / `ValueTask`.
- **`ConfigureAwait(false)`** — в обобщённом **библиотечном** коде, на каждом релевантном `await` (см. FAQ). В коде приложения (UI после await, типичный ASP.NET Core) — не навязывать `false` без нужды.
- `CancellationToken` по цепочке для отменяемых операций.

---

## Тесты и качество

- TDD или тест рядом с изменением — предпочтительно для нетривиальной логики; осознанные исключения допустимы.
- Рефакторинг без смены поведения — те же проверки/тесты; для UI — снапшоты или критичные сценарии.
- Предупреждения анализаторов: сначала причина, потом фикс; подавления — с обоснованием.

---

## Безопасность

- Секреты не в коде; ввод извне — валидация и безопасные паттерны (параметризация, экранирование) по доменным playbook.

---

## Типичные ловушки (кратко)

- **Ресурсы:** освобождать `IDisposable` / `IAsyncDisposable` через `using` / `await using`; не подавлять исключения так, что объект остаётся в невалидном состоянии без явной схемы.
- **`HttpClient`:** не создавать новый экземпляр на каждый запрос; в ASP.NET — **`IHttpClientFactory`** / политика переиспользования; иначе — один долгоживущий экземпляр по документации для сценария.
- **`IEnumerable`:** повторное перечисление может быть дорогим или с побочными эффектами — для нескольких проходов **материализовать** (`ToList` и т.п.) осознанно.
- **Культура:** для протоколов, парсинга «сырых» данных, логов в машиночитаемом виде — **`InvariantCulture`**; для текста UI — **`CurrentCulture`** (см. таблицу ссылок).
- **Логи:** структурированное логирование и уровни; **не** писать секреты и лишний PII.
- **Потоки:** избегать общей **изменяемой статики** без синхронизации; при конкуренции — `Concurrent*`, явные примитивы (`lock`, `SemaphoreSlim`) по смыслу.
- **`ValueTask`:** использовать только понимая семантику (в т.ч. повторный `await` одного и того же экземпляра); иначе предпочтительнее `Task`.
- **Сборка / AOT:** при таргете **Native AOT** / trimming — отдельные ограничения (рефлексия, динамика); см. [Native AOT](https://learn.microsoft.com/en-us/dotnet/core/deploying/native-aot/).
- **Зависимости:** периодически **`dotnet list package --vulnerable`** и обновления с учётом breaking changes.

---

## Операционные правила репозитория

- Коммиты **по смыслу** (фича / рефакторинг / стиль — раздельно).
- Массовые правки — **узкая область**; `externals/**` и вендор не трогать без решения.
- Рефакторинг после проверки; имена констант и ID — **доменный смысл**.
- Сложность: один смысл на метод; рост файла — сигнал к разбиению.

---

## Версионирование

- **v1** — публичный срез для kb-public; актуальная дата смыслового обновления — **2026-04-16** (в т.ч. § «Типичные ловушки», расширение таблицы ссылок). Существенное изменение норм — новая версия файла (`v2` и т.д.) или явная пометка в сообщении коммита; отдельный changelog не обязателен.

