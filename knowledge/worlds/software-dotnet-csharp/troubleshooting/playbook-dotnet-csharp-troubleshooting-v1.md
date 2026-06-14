# Playbook: .NET / C# runtime — troubleshooting (v1)

> **Контур:** A · kb-public  
> **Когда:** «тормозит» сервис, высокий CPU/GC, миграция Framework → .NET, неясный TFM  
> **Playbooks DOTNET-01..03:** [`../kb-dotnet-playbooks-v1.md`](../kb-dotnet-playbooks-v1.md)

---

## Симптом → playbook / шаг

| Симптом | Куда |
|---------|------|
| Неясно какой TFM / EOL | kb DOTNET-01 |
| Миграция Framework → .NET 8/10 | kb DOTNET-02 (слои, пилот, стратегия) |
| CPU, latency, OOM, «подвисает» | **§ Perf cycle** ниже (DOTNET-03) |
| Ошибки компиляции / analyzer | [`../../software-dotnet-tooling-roslyn/troubleshooting/`](../../software-dotnet-tooling-roslyn/troubleshooting/) |

---

## DOTNET-03 — perf / stability (сводка)

1. Подтвердить симптом **метриками/логами** (CPU, память, latency, errors, health), не только «кажется».
2. `dotnet-counters` / OpenTelemetry: GC, thread pool, RPS.
3. При подтверждении — короткий `dotnet-trace` в окне нагрузки.
4. Hot path + allocation profile; sync-over-async, starvation.
5. Малые change-set + измерение до/после.

**Exit:** документированное улучшение с цифрами, не «подкрутили флаги».

---

## Как дополнять

Новые симптомы runtime — таблица + при необходимости новый под-playbook в `kb-dotnet-playbooks-v1.md`.

