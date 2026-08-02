---
metadata_schema_version: 1.0
document_id: DOC-0016
title: Agent System README
plane: Repository Operating Model
domain: Agent System
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: AGENTS.md
related_concepts:
  - CONCEPT-0001
  - CONCEPT-0018
  - CONCEPT-0070
  - CONCEPT-0447
  - CONCEPT-0448
  - CONCEPT-0449
  - CONCEPT-0450
  - CONCEPT-0451
  - CONCEPT-0452
  - CONCEPT-0453
dependencies:
  - DOC-0001
  - DOC-0018
  - DOC-0070
  - DOC-0447
  - DOC-0448
  - DOC-0449
  - DOC-0450
  - DOC-0451
  - DOC-0452
  - DOC-0453
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains:
  - Agent Profiles
---

# Agent System

## Purpose and scope

Rules and guidance for repository-facing coding and documentation agents.

## What belongs here

Agent operating guides, agent profiles, agent navigation, skills, AI governance policies, and repository AI rules.

## What does not belong here

Product AI runtime/model behavior, product AI orchestration, product AI memory, or any product AI specifications.

## Canonical owner map

| Subdomain | Concept ID | Canonical Owner | README |
| --- | --- | --- | --- |
| agent-profiles | CONCEPT-0018 | [Agent Profiles README](agent-profiles/README.md) | [Agent Profiles README](agent-profiles/README.md) |
| agent-system | CONCEPT-0439 | [AI Capability Matrix](ai-capability-matrix.md) | (self) |
| agent-system | CONCEPT-0447 | [AI Decision Tree](ai-decision-tree.md) | (self) |
| agent-system | CONCEPT-0448 | [AI Execution Contract](ai-execution-contract.md) | (self) |
| agent-system | CONCEPT-0449 | [AI Failure Policy](ai-failure-policy.md) | (self) |
| agent-system | CONCEPT-0450 | [AI Change Classification Matrix](ai-change-classification-matrix.md) | (self) |
| agent-system | CONCEPT-0451 | [AI Commit Policy](ai-commit-policy.md) | (self) |
| agent-system | CONCEPT-0452 | [AI Push Policy](ai-push-policy.md) | (self) |
| agent-system | CONCEPT-0453 | [AI Workspace Policy](ai-workspace-policy.md) | (self) |

## Document classes expected

- Index
- Guide
- Reference
- Specification
- Policy
- Registry (only in registry folders)
- Historical (only in historical folders)
- Generated (only in generated folders)

## Relationship to adjacent domains

Agent System defines repository AI behavior. It is governed by Repository Operating Model standards. Product Specification / AI domain owns product AI behavior and must not redefine repository agent rules.

## Subdomain navigation

### agent-profiles

- Concept: `CONCEPT-0018`
- Canonical Owner: [Agent Profiles README](agent-profiles/README.md)
- Folder README: [Agent Profiles README](agent-profiles/README.md)

Documents:
- [Aider Agent Profile](agent-profiles/aider.md) — Reference
- [Antigravity Agent Profile](agent-profiles/antigravity.md) — Reference
- [ChatGPT Agent Profile](agent-profiles/chatgpt.md) — Reference
- [Claude Agent Profile](agent-profiles/claude.md) — Reference
- [Cline Agent Profile](agent-profiles/cline.md) — Reference
- [Codebuff Agent Profile](agent-profiles/codebuff.md) — Reference
- [Copilot Agent Profile](agent-profiles/copilot.md) — Reference
- [Cursor Agent Profile](agent-profiles/cursor.md) — Reference
- [Gemini Agent Profile](agent-profiles/gemini.md) — Reference
- [GitHub Copilot CLI Agent Profile](agent-profiles/github-copilot-cli.md) — Reference
- [Google Code Assistant Agent Profile](agent-profiles/google-code-assistant.md) — Reference
- [Kilo Code Agent Profile](agent-profiles/kilo-code.md) — Reference
- [Llama CPP Agent Profile](agent-profiles/llama-cpp.md) — Reference
- [Ollama Agent Profile](agent-profiles/ollama.md) — Reference
- [OpenCode Agent Profile](agent-profiles/opencode.md) — Reference
- [Perplexity Agent Profile](agent-profiles/perplexity.md) — Reference
- [Qodo Agent Profile](agent-profiles/qodo.md) — Reference
- [Qwen Agent Profile](agent-profiles/qwen.md) — Reference
- [Raycast Agent Profile](agent-profiles/raycast.md) — Reference
- [Roo Code Agent Profile](agent-profiles/roo-code.md) — Reference
- [Tabnine Agent Profile](agent-profiles/tabnine.md) — Reference
- [Warp Agent Profile](agent-profiles/warp.md) — Reference
- [Windsurf Agent Profile](agent-profiles/windsurf.md) — Reference
- [Zed Agent Profile](agent-profiles/zed.md) — Reference

## AI Governance Documents

| Document ID | Title | Class | Authority | Status |
| --- | --- | --- | --- | --- |
| DOC-0017 | [Agent Index](agent-index.md) | Index | Derived | Active |
| DOC-0019 | [Agent Guide](agent-guide.md) | Guide | Derived | Active |
| DOC-0045 | [Skills](skills.md) | Reference | Derived | Active |
| DOC-0046 | [Agent Navigation](agent-navigation.md) | Reference | Derived | Active |
| DOC-0070 | [AI Capability Matrix](ai-capability-matrix.md) | Policy | Canonical | Active |
| DOC-0071 | [AI Decision Tree](ai-decision-tree.md) | Policy | Canonical | Active |
| DOC-0072 | [AI Execution Contract](ai-execution-contract.md) | Policy | Canonical | Active |
| DOC-0073 | [AI Failure Policy](ai-failure-policy.md) | Policy | Canonical | Active |
| DOC-0074 | [AI Change Classification Matrix](ai-change-classification-matrix.md) | Policy | Canonical | Active |
| DOC-0075 | [AI Commit Policy](ai-commit-policy.md) | Policy | Canonical | Active |
| DOC-0076 | [AI Push Policy](ai-push-policy.md) | Policy | Canonical | Active |
| DOC-0077 | [AI Workspace Policy](ai-workspace-policy.md) | Policy | Canonical | Active |

## Before adding a document here

- Identify the active Concept ID in the Concept Registry before creating a new document.
- Update an existing canonical owner instead of creating a duplicate specification when the concept already exists.
- Place the document in the narrowest matching subdomain folder.
- Assign a stable Document ID only if the document is new permanent repository knowledge.
- Add or update metadata, registries, README navigation, and cross-references in the same change.
- Run local metadata, registry, traceability, link, stale-path, empty-folder, and repository hygiene validation before committing.
- Do not add generated documentation, CI/CD files, GitHub Actions, temporary reports, or repository automation.
