# Information Management Playbook v1

## Purpose
Project-independent domain base for engineering Information Management (IM).
This file stores stable IM concepts, rules, and decision patterns that do not depend on a specific product.

## Domain Goal
- Keep engineering information consistent, traceable, and auditable across its lifecycle.
- Reduce semantic ambiguity between source systems, users, and downstream consumers.

## Core Domain Objects
- Document
- Revision
- Version
- File
- Tag
- Relationship (Document-Tag, Document-Document, Tag-System, Tag-Tag)
- Attribute and Classification
- Workflow State (Draft, Verified, Approved, Archived, Superseded)
- Provenance (source system, source field, sync event)

## Canonical Domain Rules
- Every critical field must be traceable to source provenance.
- Revision and version semantics must be explicit and non-ambiguous.
- Lifecycle transitions must be guarded and auditable.
- Validation must return actionable diagnostics (where, why, impact, fix path).
- Human-readable state must match system state at all times.
- Reference data (classifiers, dictionaries, unit systems) must be versioned.
- Bulk updates must support preview (dry-run) and deterministic rollback.

## Architecture Lens (Pipeline/Compiler Model)
- Ingestion adapters -> parse and normalize source payloads.
- Semantic validation -> enforce IM invariants.
- Canonical IR -> source-agnostic information graph.
- Passes -> dedup, conflict resolution, enrichment, indexing.
- Projections -> API contracts, UI workbench views, exports, reports.

## Integration and Interop Principles
- Keep canonical contracts stable and explicit at boundaries.
- Separate source-specific mapping from canonical ontology.
- Preserve backward compatibility with versioned contract evolution.
- Treat source connectors as replaceable adapters, not core domain logic.

## UX Contracts
- Progressive disclosure with expert acceleration paths.
- Context-preserving navigation across Document/Revision/Version.
- Semantic compare over metadata + links + file preview.
- Conflict center with safe bulk operations and dry-run preview.
- Approval board with immutable approval snapshots.

## Evidence Contract
- Treat IM/AVEVA claims as factual only with source docs or code references.
- Separate facts from hypotheses in design notes.
- Record confidence and evidence quality independently.
- Keep a glossary for overloaded terms (document, revision, version, baseline, status).

## Open Questions Backlog
- Canonical mapping of AVEVA-like concepts to neutral IM ontology.
- Conflict precedence policy across multiple upstream systems.
- Minimal immutable snapshot schema for approvals.
- IR versioning strategy for long-running migration compatibility.

## Project Overlay Contract
- Product-specific decisions (for example IMC UX, repo paths, sprint scopes) stay in canonical notes sections like `scope-imc` and related `imc-*` blocks.
- This playbook remains domain-only and reusable across projects.
