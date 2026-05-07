## TPM-узел: формат манифеста (draft v1)

> Черновик для будущих реальных TPM-узлов. Не использовать как настоящий манифест; конкретные значения и подписи определяются при запуске узла.

### 1. Назначение

Манифест TPM-узла описывает:

- какие версии `integrity-core` считаются валидными;
- какими ключами и как они подписаны;
- где находится эталонная копия KB/kb-public;
- как обрабатываются отзыв (revocation) и форки.

Любая среда, реализующая Integrity POST с опорой на TPM-узел, может использовать этот формат для автоматической проверки.

### 2. Структура (JSON / YAML)

Минимальный набор полей (пример в JSON-псевдоформате):

```json
{
  "tpm_node_id": "gitlab-kb-root-1",
  "version": "1",
  "issuer": {
    "name": "Krawler Integrity Root",
    "organization": "Krawler",
    "contact": "security@example.org"
  },
  "keys": [
    {
      "key_id": "primary-signing-key-2026",
      "algorithm": "ed25519",
      "public_key": "<BASE64_OR_PEM>",
      "created_at": "2026-03-01T00:00:00Z",
      "expires_at": "2028-03-01T00:00:00Z",
      "usage": ["sign-core", "sign-manifest"]
    }
  ],
  "integrity_core_versions": [
    {
      "id": "integrity-core-v1.0.0",
      "path": "knowledge/META/integrity-core.md",
      "sha256": "<HEX_DIGEST>",
      "signed_at": "2026-03-01T00:00:00Z",
      "signatures": [
        {
          "key_id": "primary-signing-key-2026",
          "signature": "<BASE64_SIGNATURE>"
        }
      ],
      "status": "active"  // active | deprecated | revoked
    }
  ],
  "kb_public_reference": {
    "repo_url": "https://gitlab.example.org/Krawler/kb-public",
    "default_branch": "main",
    "commit": "<COMMIT_SHA>",
    "paths": [
      "knowledge/**",
      "META/integrity-core.md",
      "META/integrity-post-spec-v1.md"
    ]
  },
  "revocation": {
    "policy_url": "https://gitlab.example.org/Krawler/kb-public/-/wikis/Integrity-Revocation-Policy",
    "revoked_cores": [
      {
        "id": "integrity-core-v0.9.0",
        "reason": "experimental-only",
        "revoked_at": "2026-03-01T00:00:00Z"
      }
    ]
  },
  "federation": {
    "related_nodes": [
      {
        "tpm_node_id": "gitlab-kb-root-2",
        "relationship": "peer"
      }
    ],
    "quorum_rule": "2-of-3"  // пример: какие комбинации узлов считаются достаточными для доверия
  },
  "meta": {
    "created_at": "2026-03-01T00:00:00Z",
    "updated_at": "2026-03-01T00:00:00Z",
    "schema_version": "1"
  }
}
```

### 3. Как это может использоваться

- **Проверка integrity-core:** среда сравнивает текущий `integrity-core.md` по пути `knowledge/META/integrity-core.md` с `sha256` и `id` из манифеста; проверяет подпись `signatures` по `public_key`.
- **Проверка статуса:** если статус `revoked` или `deprecated`, среда может:
  - при `revoked` — отказаться использовать это ядро и вернуться к Minimal Safe Default;
  - при `deprecated` — предупредить и рекомендовать обновление.
- **Федерация:** если настроено несколько TPM-узлов, среда может требовать подтверждения от N из M манифестов (например, 2-of-3) для принятия версий `integrity_core_versions`.

### 4. Ограничения и статус

- Этот файл — **черновик**; реальный TPM-узел должен опубликовать свой конкретный манифест и ключи.
- До появления реальных узлов и подписанных манифестов архитектура Integrity POST остаётся в режиме prototyping (см. раздел 7 в `integrity-post-spec-v1.md`).

---

## Metadata (routing)

- **status:** draft — не использовать как операционный манифест.
- **layer:** META / reference only.
- **transfer_boundary:** при любом запросе по TPM/федерации указывать Transition Mode (`integrity-post-spec-v1.md` §7); не заявлять TPM-совместимость до появления реального узла и подписанного манифеста.

