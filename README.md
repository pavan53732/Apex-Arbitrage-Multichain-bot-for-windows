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
version: 1.0.0
canonical_source: README.md
related_concepts:
  - CONCEPT-0005
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Governance
type: OVERVIEW
purpose: Readme documentation.
scope: Reference documentation.
---

# Repository README

This repository uses a two-plane documentation knowledge model. The root is intentionally minimal and contains only repository-level control and entry files.

## Canonical root controls

- [AGENTS](./AGENTS.md) — agent operating contract.
- [Agent Rules](./AGENTS_RULES.md) — detailed repository agent rules.
- [Repository Knowledge Model](./REBUILD-SYSTEM-SPECIFICATION.md) — canonical knowledge architecture.
- [Repository Execution Model](./REPOSITORY-EXECUTION-MODEL.md) — local-first/no-CI execution policy.

## Documentation entry points

- [Documentation Index](./docs/README.md)
- [Concept Registry](./docs/repository-operating-model/registries/CONCEPT-REGISTRY.md)
- [Document Registry](./docs/repository-operating-model/registries/DOCUMENT-REGISTRY.md)
- [Traceability Registry](./docs/repository-operating-model/registries/TRACEABILITY-REGISTRY.md)

## First product-specification reads

- [Architecture](./docs/product-specification/architecture/architecture.md)
- [AI Pipeline](./docs/product-specification/ai/runtime/ai-pipeline.md)
- [Runtime Operations](./docs/product-specification/operations/reliability/runtime-operations.md)
- [Trading Lifecycle](./docs/product-specification/execution/trading/trading-lifecycle.md)
- [Execution Lifecycle](./docs/product-specification/execution/transactions/execution-lifecycle.md)
- [Database Schema](./docs/product-specification/data/database-schema.md)
- [Security Contracts](./docs/product-specification/security/security-contracts.md)

## Rule

If behavior is not explicit in a canonical owner document, stop and clarify rather than inventing behavior. All validation is local-first; this repository intentionally contains no GitHub Actions or CI/CD automation.
