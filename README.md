---
metadata_schema_version: 1.0
document_id: DOC-0005
title: Repository README
plane: Repository Operating Model
domain: Governance
class: Index
authority: Canonical
status: Active
owner: Runtime Team
version: 1.1.0
canonical_source: README.md
related_concepts:
  - CONCEPT-0005
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-01
concept_role: Owner
owned_domains:
  - Governance
type: OVERVIEW
purpose: Readme documentation.
scope: Reference documentation.
---

# Repository README

This repository uses a two-plane documentation knowledge model. The root is intentionally minimal and contains only repository-level control and entry files.

## Approved repository architecture

```
Repository Root
│
├── Repository Entry & Execution
│   (README.md, AGENTS.md, AGENTS_RULES.md,
│    REPOSITORY-EXECUTION-MODEL.md,
│    REBUILD-SYSTEM-SPECIFICATION.md,
│    validators/)
│
└── docs/
    ├── apex-repository-docs/
    └── apex-app-docs/
```

`docs/` is the documentation knowledge base and contains exactly two permanent documentation roots. `docs/apex-repository-docs/` describes the repository itself (governance, standards, registries, traceability, validation, workflows, contribution, documentation lifecycle, agent system). `docs/apex-app-docs/` describes the APEX application (architecture, runtime, AI, execution, dashboard, security, windows, plugins, interfaces, testing, state machines). No third permanent documentation root is permitted under `docs/`.

## Canonical root controls

- [AGENTS](./AGENTS.md) — agent operating contract.
- [Agent Rules](./AGENTS_RULES.md) — detailed repository agent rules.
- [Repository Knowledge Model](./REBUILD-SYSTEM-SPECIFICATION.md) — canonical knowledge architecture.
- [Repository Execution Model](./REPOSITORY-EXECUTION-MODEL.md) — local-first/no-CI execution policy.

## Documentation entry points

- [Documentation Index](./docs/README.md)
- [Concept Registry](./docs/apex-repository-docs/registries/CONCEPT-REGISTRY.md)
- [Document Registry](./docs/apex-repository-docs/registries/DOCUMENT-REGISTRY.md)
- [Traceability Registry](./docs/apex-repository-docs/registries/TRACEABILITY-REGISTRY.md)

## First product-specification reads

- [Architecture](./docs/apex-app-docs/architecture/architecture.md)
- [AI Pipeline](./docs/apex-app-docs/ai/runtime/ai-pipeline.md)
- [Runtime Operations](./docs/apex-app-docs/operations/reliability/runtime-operations.md)
- [Trading Lifecycle](./docs/apex-app-docs/execution/trading/trading-lifecycle.md)
- [Execution Lifecycle](./docs/apex-app-docs/execution/transactions/execution-lifecycle.md)
- [Database Schema](./docs/apex-app-docs/data/persistence/database-schema.md)
- [Security Contracts](./docs/apex-app-docs/security/security-contracts.md)

## Rule

If behavior is not explicit in a canonical owner document, stop and clarify rather than inventing behavior. All validation is local-first; this repository intentionally contains no GitHub Actions or CI/CD automation.
