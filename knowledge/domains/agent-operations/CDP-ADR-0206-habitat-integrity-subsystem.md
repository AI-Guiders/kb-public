# CDP-ADR-0206: Habitat Integrity Subsystem (pointer)

**Tags:** #agent-operations #cdp #adr #integrity #habitat #mem-c  
**Status:** accepted (spec)  
**SSOT:** [`cdp-mcp/docs/adr/CDP-ADR-0206-habitat-integrity-subsystem.md`](../../../../PersonalCursorFolder/Financial/software/open/cdp-mcp/docs/adr/CDP-ADR-0206-habitat-integrity-subsystem.md)  
**Domain card:** `cdp-mcp/.cdp/domain/integrity.md`

---

## One line (KB mirror)

**HIS** — на каждый habitat-read отвечает: **та же редакция файла (SHA-256), что при прошлом attest, или изменён?** Не список канонов; не в первую очередь «анти-оператор» — **вторжение извне в общее пространство**, о котором агент сегодня не узнаёт.

**Release leg (federation):** на границе релиза — `habitat-release-manifest.v1.json` для **всех трёх контуров** ([`map-kb-three-contours-v1.md`](map-kb-three-contours-v1.md)): `kb_private` · `kb_group` · `kb_public`. Проверка: `∀ path: sha256(clone) == manifest[path]`.

## Зачем в agent-notes

MEM-C (habitat KB): оператор **может** править файл на диске; агент должен видеть **drift с прошлого attest**, не только git после commit.

## Связи

- [`map-kb-three-contours-v1.md`](map-kb-three-contours-v1.md) — release manifest per contour
- [`PUBLISHING.md`](../../PUBLISHING.md) — build + manifest hook (public/group)
- [`map-memory-organization-variants-v1.md`](../../personal/recognition-history/map-memory-organization-variants-v1.md) — MEM-C §integrity; MEM-B delegated write
- [`note-auto-poisoning-retract-rebuild-v0.md`](note-auto-poisoning-retract-rebuild-v0.md) — quarantine handoff

## Implementation

See SSOT ADR phases v0–v2. v0: `integrity` block on peek/buffer + seat Trust Registry.

