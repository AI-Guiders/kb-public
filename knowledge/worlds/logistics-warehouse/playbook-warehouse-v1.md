# Warehouse Playbook v1

## Purpose

Операционный контракт для домена «склад: видеозахват штрихкодов/QR и требования маркетплейсов к этикеткам». Порядок загрузки: status → playbook → kb (никогда не стартовать с kb без явного запроса).

## When to Load Which KB

- **Только этикетки** (Ozon, WB, Яндекс Маркет: размеры, dpi, форматы, маркировка) → `kb-warehouse-marketplace-labels-v1.md`.
- **Только видеозахват/камеры** (читаемость ШК на записи, px/модуль, FOV, настройки 4K, модели Hikvision) → `kb-warehouse-barcode-video-v1.md`. При запросе о конкретных моделях камер, даташитах, расчёте px/модуль по FOV или evidence «почему 4K не читает» — дополнительно подгружать **L1 (on demand):** `kb-warehouse-barcode-video-models-l1-v1.md`.
- **И этикетки, и видео** → оба файла.

## Core Invariants

- Два типоразмера этикеток: 40×50 мм и 120×70 мм. Две зоны захвата: выход из принтера и зона на столе/на товаре.
- Мир **logistics.warehouse**. Внутренние регламенты и привязка к конкретным столам — за пределами kb; расчёт по данным камеры и зоны — по формулам в kb.

## Router Reference

Индекс: `index-knowledge-router-v1.md`, секция **Warehouse (barcode video, marketplace labels)**. Domain Entry Map: status-warehouse-v1, playbook-warehouse-v1, kb-warehouse-*.

## Maintenance

Детали и evidence — в kb. Playbook держать кратким; расширения — в kb через MCP (write_knowledge_file / upsert_knowledge_section).