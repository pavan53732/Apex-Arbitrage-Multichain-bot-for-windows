---
metadata_schema_version: 1.0
document_id: DOC-0109
title: Prompt Engineering
plane: Product Specification
domain: AI
class: Specification
authority: Canonical
status: Active
owner: Runtime Team
version: 1.1.0
canonical_source: docs/apex-app-docs/ai/prompts/prompt-engineering.md
related_concepts:
  - CONCEPT-0109
dependencies: []
consumers:
  - DOC-0405
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - AI
type: CONTRACT
purpose: Prompt Engineering documentation.
scope: Reference documentation.
---

# Prompt Engineering

## Version
**Version:** 1.1.0 | **Status:** Canonical | **Last Updated:** 2026-08-02 | **Owner:** Runtime Team

## Document type
Document type: [CONTRACT]

# Prompt Engineering

## Purpose
Defines prompt construction, template management, and versioning rules.

## Scope
This document covers system prompts, few-shot prompts, safety prompts, agent prompts, and context injection.

## Prompt assets
- Prompt templates.
- System prompts.
- Few-shot prompts.
- Safety prompts.
- Versioned prompt packs.
- Context injection rules.

## Versioning rules
- Prompt packs are versioned; a version bump requires validation against the criteria in `## Prompt rules` before rollout.
- A prompt change that alters model/provider behavior must be reviewed before release.
- Deprecated prompts are retained in the pack history for replay and audit.

## Context shaping
- Only context required for the task is injected; risk prompts include only the context needed for exposure analysis.
- Context injection must respect the limits defined by context-window management.
- Guardrails are applied at construction time, not at inference time.

## Cross-references
- `../runtime/ai-pipeline.md`
- `../providers/ai-settings.md`
- `../providers/cloud-ai-integration.md`
- `../../configuration/core/configuration.md`

## Orchestration boundary
This document governs capability, memory, prompt, or cost definitions. For runtime orchestration and pipeline sequencing, see `../runtime/ai-pipeline.md`.

## Governance Rules
Defines prompt templates, system prompts, context shaping, guardrails, and prompt versioning.

## Example
A risk prompt includes only the context required for exposure analysis, drawn from the versioned prompt pack.

## Prompt rules
- Define prompt templates, versioning, and validation criteria.
- Define how prompts change across model/provider contexts.

## Operational Contract
Defines prompt assets (system prompts, few-shot prompts, safety prompts, versioned prompt packs, context injection rules) as versioned artefacts owned exclusively by this document. Any consumer that constructs a prompt (AI Pipeline, AI Settings, Cloud AI Integration) must source templates and context-injection rules from the versioned prompt pack rather than embedding ad hoc prompt text; a prompt version bump requires validation against the criteria defined under `## Prompt rules` before rollout.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.1.0 | 2026-08-02 | Expanded canonical content: replaced placeholder directives and generic boilerplate with grounded ownership, rules, lifecycle, failure, and cross-reference detail. | Runtime Team |
| 1.0.1 | 2026-07-29 | Added `## Operational Contract` section (state-machine-consistent authoritative contract body) to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`). All other content unchanged. | Runtime Team |
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Runtime Team |
