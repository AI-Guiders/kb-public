---
type: Index
title: Мир **logistics.warehouse**
description: '**Идентификатор мира:** `logistics.warehouse`'
tags: [logistics-warehouse, readme, worlds]
language: ru
world: logistics
subworld: warehouse
---
# Мир **logistics.warehouse**


**Идентификатор мира:** `logistics.warehouse`  
**Назначение:** маркетплейсы и этикетки (Ozon, Wildberries, Яндекс Маркет); видеозахват штрихкодов и QR на складе; камеры и NVR под читаемость кода на записи.

## Карта материалов

| Роль | Файл | Содержание |
|------|------|------------|
| **Status** | [`status-warehouse.md`](status-warehouse.md) | Состояние домена, порядок загрузки, границы мира. |
| **Playbook** | [`playbook-warehouse.md`](playbook-warehouse.md) | Маршрутизация: какой kb грузить по типу запроса. |
| **KB — этикетки** | [`kb-warehouse-marketplace-labels.md`](kb-warehouse-marketplace-labels.md) | Размеры, dpi, форматы, маркировка, Честный знак. |
| **KB — видео** | [`kb-warehouse-barcode-video.md`](kb-warehouse-barcode-video.md) | px/модуль, FOV, кодек, зоны съёмки, типовой кейс. |
| **KB — L1** | [`kb-warehouse-barcode-video-models-l1.md`](kb-warehouse-barcode-video-models-l1.md) | Модели камер, даташиты, evidence on demand. |

## История

v1.0 — перенос из корня `knowledge/` в `worlds/logistics-warehouse/` (ветка `feature/kb-taxonomy-layout-v1`).

