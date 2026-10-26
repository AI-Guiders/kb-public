---
type: Note
title: LUS prod — обновление Ingest API (2026-07-09)
description: '**Статус:** publish готов · **отдельного «Upgrade-пакета» в репо нет**'
---
# LUS prod — обновление Ingest API (2026-07-09)

**Статус:** publish готов · **отдельного «Upgrade-пакета» в репо нет**

## Что имелось в виду

На prod API уже стоит в `C:\Services\UrsaLicenseUsage\Api`. Нужно **перелить свежий publish** и перезапустить службу — migrate накатится при старте.

«Handoff без пароля» = **не шифровать 7z паролем**, а не новый тип дистрибутива. Стандартный handoff — `package-secure-handoff.ps1` (7z + пароль). Для **обновления** уже установленного API достаточно `publish\api\`.

## Артефакт сборки

| Что | Путь |
|-----|------|
| Publish API (Release) | `URSA.LicenseUsage/publish/api/` |
| Install-скрипт | `publish/api/Install-UrsaLicenseUsageApi.ps1` |
| Инструкция | `docs/infra/INSTALL_Api_RU.md` |

Сборка: `scripts/publish-api.ps1 -Configuration Release`

> Ad-hoc zip `Ursa.LicenseUsage.Api-upgrade-20260709.zip` — лишний; можно игнорировать или удалить.

## Prod-контур (без секретов в этом файле)

| Параметр | Значение |
|----------|----------|
| SQL | `DPC-AV-M-DCMS` / `UrsaLicenseUsage` |
| Служба | `UrsaLicenseUsageApi` |
| Путь | `C:\Services\UrsaLicenseUsage\Api` |
| Порт | 5280 |
| Health | `GET /v1/health` |

Секреты — в **существующем** `api.toml` на сервере. Перед копированием publish — **бэкап** `api.toml`.

## Обновление на prod

1. С машины сборки: скопировать `publish\api\*` на сервер (robocopy / zip без пароля — как удобно IT).
2. На сервере **не перетирать** prod `api.toml` (в publish лежит dev/handoff-копия для первой установки).
3. PowerShell от администратора:
   ```powershell
   cd C:\Services\UrsaLicenseUsage\Api
   powershell -ExecutionPolicy Bypass -File .\Install-UrsaLicenseUsageApi.ps1 -Upgrade -StartService
   ```
4. `Invoke-RestMethod http://localhost:5280/v1/health`

## Зачем обновлять

Новые EF-миграции / SQL views для DashSpec stakeholder: warm agg, utilization, peak segments, idle browse/detail.

## Миграции (июль 2026)

WarmReportViewsFromAggregates, WarmAggExtendedTablesAndViews, StakeholderKpiViewAndExtendedAggMapping, StakeholderPeakSegmentViewsNoTop, StakeholderIdleByUserDayView, HourlyActivityView, PeakAppsPerUserByPeriodView, EventsDetailUsageDateAlias, PeakConcurrentProxyHeatmapView.

## Полный handoff (первая установка)

`publish-api.ps1` + `package-agent-installer.ps1` + `package-secure-handoff.ps1 -Password <…>` → `Ursa.LicenseUsage-Handoff-1.0.0.0.7z` (API zip + agent zip + docs + `006_api_dbowner_login.sql`).

Для **update** уже поднятого API — только publish + `-Upgrade`.

## После API

DashSpec: `scripts/publish-dashspec.ps1` (порт 5295). Агенты не трогать.

