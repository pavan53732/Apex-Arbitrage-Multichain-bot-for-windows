---
metadata_schema_version: 1.0
document_id: DOC-0233
title: Test Case Registry
plane: Product Specification
domain: Testing
class: Registry
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/testing/test-case-registry.md
related_concepts:
  - CONCEPT-0233
dependencies: []
consumers:
  - DOC-0049
  - DOC-0059
  - DOC-0234
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: "Canonical registry of all architecture-level test case IDs referenced by the traceability matrix. Each ID maps to a subsystem, a test category, and the validating document."
scope: None
---

# Test Case Registry

## Document type
Document type: [REFERENCE]

## Version
**Version:** 0.1.0 | **Status:** Draft | **Last Updated:** 2026-07-27 | **Owner:** Runtime Team

## Purpose
Canonical registry of all architecture-level test case IDs referenced by the traceability matrix. Each ID maps to a subsystem, a test category, and the validating document.

---

## 1. AI Pipeline Tests

| Test ID | Subsystem | Category | Validated By | Description |
|---------|-----------|----------|--------------|-------------|
| `test-ai-failover-001` | AI Pipeline | Failover | AI-PIPELINE.md | Provider failover chain is followed correctly |
| `test-context-determinism-001` | AI Pipeline | Determinism | AI-PIPELINE.md | Same inputs produce same assembled context |
| `test-tool-invocation-001` | AI Pipeline | Tool runtime | AI-TOOL-INVOCATION-CONTRACT.md | Tool invocation respects timeout and retry |
| `test-prompt-lifecycle-001` | AI Pipeline | Lifecycle | PROMPT-LIFECYCLE.md | Prompt flows through valid state transitions |
| `test-prompt-compression-001` | AI Pipeline | Compression | PROMPT-LIFECYCLE.md | Compression strategies produce correct output |
| `test-tool-circuit-breaker-001` | AI Pipeline | Circuit breaker | AI-TOOL-INVOCATION-CONTRACT.md | Circuit breaker opens after N failures |
| `test-memory-injection-001` | AI Pipeline | Memory | PROMPT-LIFECYCLE.md | Memory content is correctly injected |

## 2. Trading Engine Tests

| Test ID | Subsystem | Category | Validated By | Description |
|---------|-----------|----------|--------------|-------------|
| `test-slippage-001` | Trading Engine | Execution | TRADING-ENGINE.md | Slippage check triggers halt at threshold |
| `test-trade-rollback-001` | Trading Engine | Recovery | TRADING-ENGINE.md | Failed trade correctly rolls back |
| `test-risk-enforcement-001` | Trading Engine | Risk | RISK-ENGINE.md | Risk limits block out-of-bounds trades |
| `test-atomicity-001` | Execution Engine | Atomicity | EXECUTION-ENGINE.md | Multi-leg trade executes atomically |
| `test-retry-001` | Execution Engine | Recovery | EXECUTION-ENGINE.md | Retry strategy matches expected behavior |

## 3. Configuration Tests

| Test ID | Subsystem | Category | Validated By | Description |
|---------|-----------|----------|--------------|-------------|
| `test-config-reload-001` | Configuration | Runtime | CONFIGURATION-REFERENCE.md | Config reload leaves runtime in consistent state |
| `test-config-validation-001` | Configuration | Validation | CONFIGURATION-REFERENCE.md | Invalid config is rejected with clear error |
| `test-config-reload-semantics-001` | Configuration | Reload | CONFIGURATION-REFERENCE.md | Key-specific reload/restart semantics are correct |
| `test-config-profile-merge-001` | Configuration | Profiles | CONFIGURATION-REFERENCE.md | Profile merging produces correct canonical config |

## 4. Plugin Tests

| Test ID | Subsystem | Category | Validated By | Description |
|---------|-----------|----------|--------------|-------------|
| `test-plugin-sandbox-001` | Plugin System | Sandbox | PLUGIN-SANDBOX-CONTRACT.md | Plugin cannot escape sandbox filesystem |
| `test-plugin-manifest-001` | Plugin System | Manifest | PLUGIN-SDK.md | Invalid manifest is rejected at load time |
| `test-plugin-sandbox-limits-001` | Plugin System | Resource | RESOURCE-BUDGET-SPECIFICATION.md | Plugin cannot exceed resource budget |

## 5. Runtime Tests

| Test ID | Subsystem | Category | Validated By | Description |
|---------|-----------|----------|--------------|-------------|
| `test-startup-shutdown-001` | Runtime | Lifecycle | RUNTIME-OPERATIONS.md | Startup/shutdown follows phase order |
| `test-recovery-001` | Runtime | Recovery | RECOVERY-PLAYBOOK.md | Recovery procedure matches playbook |
| `test-startup-sequence-001` | Runtime | Sequencing | RUNTIME-OPERATIONS.md | Startup correctly waits for dependencies |
| `test-worker-lifecycle-001` | Runtime | Workers | THREADING-MODEL.md | Worker pool lifecycle matches spec |
| `test-workspace-autosave-001` | Dashboard | Workspace | DASHBOARD-WORKSPACES.md | Workspace autosave preserves state correctly |
| `test-workspace-restore-001` | Dashboard | Workspace | DASHBOARD-WORKSPACES.md | Corrupt workspace falls back to default |

## 6. Event System Tests

| Test ID | Subsystem | Category | Validated By | Description |
|---------|-----------|----------|--------------|-------------|
| `test-event-delivery-001` | Event System | Delivery | EVENT-OWNERSHIP-MATRIX.md | Event delivery guarantees meet spec |
| `test-event-priority-001` | Event System | Priority | EVENT-CATALOG.md | Priority ordering is respected |
| `test-dlq-routing-001` | Event System | DLQ | EVENT-CATALOG.md | Failed events route to correct DLQ |

## 7. Security Tests

| Test ID | Subsystem | Category | Validated By | Description |
|---------|-----------|----------|--------------|-------------|
| `test-secret-lifecycle-001` | Security | Secrets | SECRET-LIFECYCLE.md | Secret lifecycle transitions are correct |
| `test-trust-boundary-001` | Security | Boundaries | TRUST-BOUNDARIES.md | Trust boundary enforcement matches matrix |
| `test-audit-retention-001` | Security | Audit | SECRET-LIFECYCLE.md | Audit events are retained for correct duration |

## 8. Resource Tests

| Test ID | Subsystem | Category | Validated By | Description |
|---------|-----------|----------|--------------|-------------|
| `test-resource-plugin-enforcement-001` | Resource Management | Budget | RESOURCE-BUDGET-SPECIFICATION.md | Plugin resource enforcement matches budget |

---

## Cross-References

- **TRACEABILITY-MATRIX.md** — Maps requirements to test cases.
- **architecture-tests/validate_traceability.py** — Validates test case IDs against this registry.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 0.1.0 | 2026-07-27 | Initial test case registry with 32 test case IDs across 8 subsystems | Runtime Team |
