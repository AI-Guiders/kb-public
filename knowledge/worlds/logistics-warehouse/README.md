# Мир **logistics.warehouse**

**Идентификатор мира:** `logistics.warehouse`  
**Назначение:** маркетплейсы и этикетки (Ozon, Wildberries, Яндекс Маркет); видеозахват штрихкодов и QR на складе; камеры и NVR под читаемость кода на записи.

## Карта материалов

| Роль | Файл | Содержание |
|------|------|------------|
| **Status** | [`status-warehouse-v1.md`](status-warehouse-v1.md) | Состояние домена, порядок загрузки, границы мира. |
| **Playbook** | [`playbook-warehouse-v1.md`](playbook-warehouse-v1.md) | Маршрутизация: какой kb грузить по типу запроса. |
| **KB — этикетки** | [`kb-warehouse-marketplace-labels-v1.md`](kb-warehouse-marketplace-labels-v1.md) | Размеры, dpi, форматы, маркировка, Честный знак. |
| **KB — видео** | [`kb-warehouse-barcode-video-v1.md`](kb-warehouse-barcode-video-v1.md) | px/модуль, FOV, кодек, зоны съёмки, типовой кейс. |
| **KB — L1** | [`kb-warehouse-barcode-video-models-l1-v1.md`](kb-warehouse-barcode-video-models-l1-v1.md) | Модели камер, даташиты, evidence on demand. |

## История

v1.0 — перенос из корня `knowledge/` в `worlds/logistics-warehouse/` (ветка `feature/kb-taxonomy-layout-v1`).
