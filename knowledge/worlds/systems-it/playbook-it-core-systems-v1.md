# IT Playbook v1

## Purpose

Operational IT reference layer for design, diagnostics, and decision-making.

## Core Method
- Use evidence-first reasoning (`invariant -> failure boundary -> verification -> decision`).
- Start from workload shape, not tool preference.
- Optimize for p99 and failure behavior, not only average metrics.

## Domain Blocks
- Algorithms and data structures:
  - `it-dsa-core-v1`
  - `it-dsa-patterns-v1`
  - `it-dsa-glossary-v1`
- Databases:
  - `it-databases-core-v1`
  - `it-db-patterns-v1`
  - `it-db-glossary-v1`
- Networking:
  - `it-network-core-v1`
  - `it-network-glossary-v1`
- Distributed systems and runtime:
  - `it-distributed-systems-core-v1`
  - `it-runtime-os-compiler-v1`
- Platform and reliability:
  - `it-cloud-platform-v1`
  - `it-security-observability-v1`
  - `it-symptom-playbook-v1`

## Decision Utilities
- `it-decision-matrix-v1` for quick architecture triage.
- `it-learning-loop-v1` for incident-to-knowledge conversion.
- `it-anti-pattern-atlas-v1` for early risk signals.

## Source Governance
- Source freshness policy: `it-source-freshness-policy-v1`
- Source citation contract: `it-source-citation-contract-v1`
- Source map and mini-index:
  - `it-source-index-map-v1`
  - `it-source-mini-index-v1`

## Maintenance Rules
- Keep this file as a stable map and concise summary.
- Keep detailed examples and long-term expansions in canonical section blocks.
