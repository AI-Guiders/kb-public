**Tags:** #logistics-warehouse #status #worlds

﻿# Warehouse Domain Status v1

## Scope

Видеозахват штрихкодов и QR на складе; требования маркетплейсов (Ozon, Wildberries, Яндекс Маркет) к этикеткам; настройка камер и NVR под читаемость кода на записи. Мир **logistics.warehouse**.

## Completion State

Status: **Done v1**

- `playbook-warehouse.md` — операционный контракт и маршрутизация по запросу.
- `kb-warehouse-marketplace-labels.md` — требования к этикеткам (размеры, dpi, форматы, Честный знак).
- `kb-warehouse-barcode-video.md` — читаемость ШК/QR с видео (px/модуль, FOV, кодек, две зоны), типовой кейс, документация и playbook по моделям камер.

## Retrieval Order

status → playbook → kb. По запросу: этикетки маркетплейсов → marketplace-labels; видеозахват, камеры, NVR → barcode-video; оба типа — оба kb.

## World

`logistics.warehouse`. Transfer boundary и внутренние регламенты — в kb.

## Next Handoff

Домен операционно закрыт на v1. Обновления по моделям камер и evidence — точечно в kb-warehouse-barcode-video.md через upsert_knowledge_section или append.

## Maintenance Policy

- Event-driven refresh (not calendar-only). Order: `status-*` → playbook → one `kb-*` per pass (`playbook-kb-operational-freshness.md`).
- **Next review triggers:**
  - New edition / major paper / platform release superseding cited claims
  - Broken `source_refs` / URL rot
  - Repeated field mismatch with practice or primary sources
  - Operator/agent flags a stale claim

