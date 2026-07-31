---
metadata_schema_version: 1.0
document_id: DOC-0074
title: AI Change Classification Matrix
plane: Repository Operating Model
domain: Agent System
class: Policy
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/repository-operating-model/agent-system/ai-change-classification-matrix.md
related_concepts:
  - CONCEPT-0001
  - CONCEPT-0074
dependencies:
  - DOC-0001
  - DOC-0016
  - DOC-0065
  - DOC-0070
  - DOC-0071
  - DOC-0072
  - DOC-0073
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Owner
owned_domains:
  - Agent System
type: STANDARD
purpose: Defines the exact change classes that every repository commit must belong to. Exactly one class per commit.
scope: All repository changes by AI agents and humans.
---

# AI Change Classification Matrix

## Purpose

Every commit in this repository must belong to exactly one change class. This makes commits deterministic, reviewable, and traceable. No commit may span multiple classes.

---

## Change Classes (Mutually Exclusive)

| Class Code | Class Name | Plane Affected | Description |
| --- | --- | --- | --- |
| **DOC-CANON** | Canonical Documentation | Both | Create/update canonical specification documents (Authority: Canonical) |
| **DOC-DERIVED** | Derived Documentation | Both | Create/update derived documents (Index, Guide, Reference, READMEs) |
| **DOC-POLICY** | Policy Documentation | Repository Operating Model | Create/update policies, standards, governance documents |
| **DOC-ARCH** | Architecture Documentation | Product Specification | Create/update ADRs, architecture specs, component diagrams |
| **DOC-HIST** | Historical Documentation | Both | Add/move to historical, supersession, archival |
| **REG-CONCEPT** | Concept Registry Update | Repository Operating Model | Add/modify/supersede concepts in Concept Registry |
| **REG-DOCUMENT** | Document Registry Update | Repository Operating Model | Add/modify documents in Document Registry |
| **REG-TRACE** | Traceability Registry Update | Repository Operating Model | Add/modify traceability relationships |
| **REG-GOV** | Registry Governance Change | Repository Operating Model | Modify registry governance rules, schema, policies |
| **META-FIX** | Metadata Fix | Both | Fix frontmatter only (no content change) |
| **REF-REPAIR** | Cross-Reference Repair | Both | Fix broken links, anchors, DOC-ID/CONCEPT-ID references |
| **NAV-UPDATE** | Navigation Update | Both | Update README navigation, Canonical Owner Maps, subdomain lists |
| **FOLDER-SPLIT** | Folder Split | Both | Split domain/subdomain per split policy (semantic, not alphabetical) |
| **FOLDER-MOVE** | Folder Move/Rename | Both | Move/rename folders with registry + reference updates |
| **VALID-SPEC** | Validator Specification | Repository Operating Model | Create/update validator specifications |
| **VALID-IMPL** | Validator Implementation | Repository Operating Model | Implement validator code/scripts |
| **AI-GOV** | AI Governance Policy | Repository Operating Model | Create/update AI capability matrix, decision tree, contracts |
| **LIFECYCLE** | Lifecycle Transition | Both | Promote/demote document status (Draft→Review→Active→Deprecated→Archived) |
| **CONCEPT-LIFECYCLE** | Concept Lifecycle | Repository Operating Model | Proposed→Active→Merged→Superseded→Alias Only→Historical |
| **REFACTOR** | Code Refactor | Product Specification | Internal code restructure without behavior change |
| **FEATURE** | Product Feature | Product Specification | New product behavior or modification |
| **CONFIG** | Configuration Change | Product Specification | Feature flags, config schemas, environment config |
| **SCRIPT** | Repository Script | Repository Operating Model | Local scripts, validation tools, automation scripts |

---

## Classification Rules

### Rule 1: Exactly One Class Per Commit
```
✅ CORRECT: Commit only DOC-CANON changes
❌ WRONG: Commit mixes DOC-CANON + REG-DOCUMENT
```
If a change logically spans classes, split into multiple commits.

### Rule 2: Registry Updates Follow Document Changes
```
Order in same commit (not separate commits):
1. DOC-CANON / DOC-DERIVED / DOC-POLICY / DOC-ARCH / DOC-HIST
2. REG-CONCEPT (if new concept)
3. REG-DOCUMENT (always)
4. REG-TRACE (if relationships change)
5. NAV-UPDATE (if navigation affected)
```

### Rule 3: Metadata-Only Changes Use META-FIX
```
✅ CORRECT: Fix status field only → META-FIX
❌ WRONG: Fix status + add content → DOC-DERIVED
```

### Rule 4: Reference Repairs Use REF-REPAIR
```
✅ CORRECT: Fix broken link only → REF-REPAIR
❌ WRONG: Fix link + update content → DOC-DERIVED
```

### Rule 5: Folder Operations Are Distinct
```
FOLDER-SPLIT: Exceeds 25 docs, creates new subdomain Concept IDs
FOLDER-MOVE: Renames/moves existing folder, no new subdomain
```

### Rule 6: Lifecycle Transitions Are Explicit
```
LIFECYCLE: Document status change (Draft→Review, Active→Deprecated, etc.)
CONCEPT-LIFECYCLE: Concept state change (Active→Superseded, etc.)
```

---

## Commit Message Format Per Class

| Class | Prefix | Format |
| --- | --- | --- |
| DOC-CANON | `docs(canon):` | `docs(canon): <action> <concept-id> - <summary>` |
| DOC-DERIVED | `docs(derived):` | `docs(derived): <action> <doc-id> - <summary>` |
| DOC-POLICY | `docs(policy):` | `docs(policy): <action> <domain> - <summary>` |
| DOC-ARCH | `docs(arch):` | `docs(arch): <action> <adr-id|concept> - <summary>` |
| DOC-HIST | `docs(hist):` | `docs(hist): <action> <doc-id> - <summary>` |
| REG-CONCEPT | `registry(concept):` | `registry(concept): <action> CONCEPT-XXXX - <summary>` |
| REG-DOCUMENT | `registry(doc):` | `registry(doc): <action> DOC-XXXX - <summary>` |
| REG-TRACE | `registry(trace):` | `registry(trace): <action> TRACE-XXXX - <summary>` |
| REG-GOV | `registry(gov):` | `registry(gov): <action> - <summary>` |
| META-FIX | `meta:` | `meta: fix <field> in <doc-id> - <summary>` |
| REF-REPAIR | `ref:` | `ref: repair <target> in <doc-id> - <summary>` |
| NAV-UPDATE | `nav:` | `nav: update <domain> README - <summary>` |
| FOLDER-SPLIT | `structure(split):` | `structure(split): split <domain> into <subdomains> - <summary>` |
| FOLDER-MOVE | `structure(move):` | `structure(move): move <from> to <to> - <summary>` |
| VALID-SPEC | `validator(spec):` | `validator(spec): <action> VAL-XXX - <summary>` |
| VALID-IMPL | `validator(impl):` | `validator(impl): <action> VAL-XXX - <summary>` |
| AI-GOV | `ai(gov):` | `ai(gov): <action> <policy> - <summary>` |
| LIFECYCLE | `lifecycle:` | `lifecycle: <from>→<to> <doc-id> - <summary>` |
| CONCEPT-LIFECYCLE | `concept(lifecycle):` | `concept(lifecycle): <from>→<to> CONCEPT-XXXX - <summary>` |
| REFACTOR | `refactor:` | `refactor: <component> - <summary>` |
| FEATURE | `feat:` | `feat: <component> - <summary>` |
| CONFIG | `config:` | `config: <component> - <summary>` |
| SCRIPT | `script:` | `script: <action> <script> - <summary>` |

---

## Examples

### Example 1: New Canonical Document
```
docs(canon): create AI Memory System specification CONCEPT-0120

Add new canonical specification for AI memory system with
context priority matrix, memory lifecycle, and knowledge index.

Registry-Version: 1.1.1
Validator-Pass: VAL-001,VAL-002,VAL-003,VAL-004,VAL-005,VAL-006,VAL-007,VAL-008
```

### Example 2: Update Derived Document + Registry + Navigation
```
docs(derived): update AI README navigation for new memory docs

Update AI domain README with Canonical Owner Map entries for
memory, prompts, knowledge subdomains.

registry(doc): register DOC-0111, DOC-0131, DOC-0401
nav: update AI README Canonical Owner Map

Validator-Pass: VAL-001,VAL-002,VAL-004,VAL-008
```

### Example 3: Folder Split
```
structure(split): split AI domain into orchestration, runtime, providers, memory, safety, prompts, knowledge, learning, explainability

Create 9 subdomains with Concept IDs CONCEPT-0101 through CONCEPT-0131.
Update AI README with full Canonical Owner Map.
Create subdomain READMEs per governance standard.

Registry-Version: 1.1.1
Validator-Pass: VAL-001,VAL-002,VAL-003,VAL-004,VAL-005,VAL-006,VAL-007,VAL-008
```

### Example 4: Metadata Fix Only
```
meta: fix authority enum in DOC-0114 AI README

Change authority from "Derived" to "Derived" (was typo "Derivedd")

Validator-Pass: VAL-002
```

### Example 5: Reference Repair
```
ref: repair broken DOC-099 reference in DOC-0102 AI Orchestration

Replace invalid DOC-099 with correct DOC-0121 AI Planner

Validator-Pass: VAL-001
```

### Example 6: Lifecycle Transition
```
lifecycle: Review→Active DOC-0102 AI Orchestration

Promote AI Orchestration spec to Active after review approval.
Update version to 1.1.0.

Validator-Pass: VAL-002,VAL-003,VAL-004
```

### Example 7: Concept Lifecycle
```
concept(lifecycle): Active→Superseded CONCEPT-0069 merged into CONCEPT-0079

APEX Architecture consolidated into Architecture canonical concept.
Update CONCEPT-0069 as alias with canonical_concept_id=CONCEPT-0079.

Registry-Version: 1.1.1
Validator-Pass: VAL-003,VAL-004,VAL-008
```

---

## Quick Classification Checklist

Before committing, answer:
1. What is the **primary** artifact changed? (doc, registry, nav, structure, validator, ai-gov, lifecycle, code)
2. Is it **canonical** or **derived**? (for docs)
3. Is it **metadata only**? → META-FIX
4. Is it **reference only**? → REF-REPAIR
5. Is it a **folder split** (>25 docs)? → FOLDER-SPLIT
6. Is it a **lifecycle transition**? → LIFECYCLE or CONCEPT-LIFECYCLE
7. Is it **product code**? → REFACTOR or FEATURE

**If uncertain → STOP. Classify first. Then commit.**

---

## Related Documents
- [AI Capability Matrix](./ai-capability-matrix.md)
- [AI Decision Tree](./ai-decision-tree.md)
- [AI Execution Contract](./ai-execution-contract.md)
- [AI Failure Policy](./ai-failure-policy.md)
- [AI Commit Policy](./ai-commit-policy.md)
- [AI Push Policy](./ai-push-policy.md)
- [AI Workspace Policy](./ai-workspace-policy.md)
- [Registry Governance Standard](../registries/registry-governance-standard.md)