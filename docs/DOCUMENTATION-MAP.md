---
last_updated: 2026-07-29
type: INDEX
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Documentation Map documentation.
scope: Reference documentation.
canonical_source: docs/DOCUMENTATION-MAP.md if filename.startswith('docs/') else DOCUMENTATION-MAP.md
---

# Documentation Map

## Document type
Document type: [INDEX]

# Documentation Map

## Purpose
Defines ownership, authority, and cross-reference rules for the documentation set.

## Ownership rules
- Each subsystem must have exactly one authoritative owner document.
- Overview, navigation, and index files must not claim subsystem authority.
- If a topic has its own lifecycle, state machine, APIs, workflows, or data model, it requires a single owner document.
- Shared cross-cutting topics such as logging, configuration, state, and security are owned once and referenced elsewhere.
- Navigation stubs must point to the owner document and must not redefine behavior.

## Canonical owners
- Agent navigation: `docs/AGENTS.md`
- Documentation map: `docs/DOCUMENTATION-MAP.md`
- Governance conventions: `docs/README-GOVERNANCE.md`
- Architecture: `docs/ARCHITECTURE.md`
- Root architecture overview: `../APEX-ARCHITECTURE.md`
- Project structure: `docs/PROJECT-STRUCTURE.md`
- Module dependency: `docs/MODULE-DEPENDENCY.md`
- Trading engine: `docs/TRADING-ENGINE.md`
- Execution engine: `docs/EXECUTION-ENGINE.md`
- Strategy engine and strategy catalog: `docs/STRATEGIES.md`
- Risk engine: `docs/RISK-ENGINE.md`
- AI decision pipeline: `docs/ai/runtime/AI-PIPELINE.md`
- Cloud AI integration: `docs/CLOUD-AI-INTEGRATION.md`
- AI settings: `docs/ai/providers/AI-SETTINGS.md`
- AI memory system: `docs/ai/memory/AI-MEMORY-SYSTEM.md`
  - Deprecated: `docs/ai/memory/AI-MEMORY.md` → redirects to `ai/memory/AI-MEMORY-SYSTEM.md`
- Error handling and logging: `docs/ERROR-HANDLING-LOGGING.md`
- Permission model: `docs/security/PERMISSION-MODEL.md`
- Security contracts: `docs/security/SECURITY-CONTRACTS.md` (policy mandates enforced by `security/SECURITY.md`)
- Market data: `docs/MARKET-DATA.md`
- Market intelligence: `docs/MARKET-INTELLIGENCE.md`
- Opportunity detection detail: `docs/OPPORTUNITY-DETECTION.md` (owned under market intelligence authority)
- Opportunity ranking detail: `docs/OPPORTUNITY-RANKING.md` (owned under market intelligence authority)
- Routing engine: `docs/ROUTING-ENGINE.md`
- Liquidity analysis: `docs/LIQUIDITY-ANALYSIS.md`
- Slippage model: `docs/SLIPPAGE-MODEL.md`
- Gas optimisation: `docs/GAS-OPTIMISATION.md`
- MEV protection: `docs/MEV-PROTECTION.md`
- Order management: `docs/ORDER-MANAGEMENT.md`
- Transaction lifecycle: `docs/TRANSACTION-LIFECYCLE.md`
- Chain integration: `docs/CHAIN-INTEGRATION.md`
- Chain intelligence: `docs/CHAIN-INTELLIGENCE.md`
- DEX integration: `docs/DEX-INTEGRATION.md`
- Portfolio management: `docs/PORTFOLIO-MANAGEMENT.md`
- Position management: `docs/POSITION-MANAGEMENT.md`
- Wallet management: `docs/WALLET-MANAGEMENT.md`
- Asset management: `docs/ASSET-MANAGEMENT.md`
- Simulation framework: `docs/SIMULATION-ENGINE.md`
- Backtesting methodology: `docs/testing/BACKTESTING.md` (consumes simulation engine)
- Runtime operations: `docs/operations/RUNTIME-OPERATIONS.md`
- Worker architecture: `docs/WORKER-ARCHITECTURE.md`
- Queue management: `docs/QUEUE-MANAGEMENT.md`
- Recovery and failover: `docs/operations/RECOVERY-AND-FAILOVER.md`
- Monitoring and observability: `docs/operations/MONITORING-OBSERVABILITY.md`
- Error handling and logging: `docs/ERROR-HANDLING-LOGGING.md`
- Security: `docs/security/SECURITY.md`
- Permission model: `docs/security/PERMISSION-MODEL.md`
- Configuration: `docs/configuration/CONFIGURATION.md`
- Database schema: `docs/DATABASE-SCHEMA.md`
- State management: `docs/STATE-MANAGEMENT.md`
- IPC protocol: `docs/IPC-PROTOCOL.md` (CONTRACT; v1.0.0)
- IPC message catalog: `docs/IPC-MESSAGE-CATALOG.md` (REFERENCE; v1.0.0; catalog under IPC protocol authority — complete message type catalog)
- API contracts: `docs/API-CONTRACTS.md`
- API reference: `docs/API-REFERENCE.md`
- Event flow: `docs/EVENT-FLOW.md`
- Data flow: `docs/DATA-FLOW.md`
- Performance targets: `docs/performance/PERFORMANCE-TARGETS.md`
- Non-functional requirements: `docs/NON-FUNCTIONAL-REQUIREMENTS.md`
- User workflows: `docs/guides/USER-FLOWS.md`
- User guide: `docs/guides/USER-GUIDE.md`
- Deployment and operations: `docs/deployment/DEPLOYMENT.md`
- Windows desktop shell: `docs/windows/WINDOWS-DESKTOP.md`
- UI component spec: `docs/ui/UI-COMPONENT-SPEC.md`
- Designer protocols: `docs/DESIGNER-PROTOCOLS.md`
- Testing guide: `docs/guides/TESTING-GUIDE.md`
- Skills and agents: `docs/development/SKILLS.md`, `docs/AGENTS.md`
- Implementation roadmap: `docs/development/IMPLEMENTATION-ROADMAP.md`
- Component diagrams: `docs/COMPONENT-DIAGRAMS.md`

## Navigation-only stubs
These must not claim ownership and should only point to owners:
- `docs/README.md`
- `docs/deployment/BUILD-RELEASE-CICD.md`
- `docs/CHANGELOG.md`
- `docs/development/CODING-STANDARDS.md`
- `docs/development/CONTRIBUTING.md`
- `docs/DECISION-LOG.md`
- `docs/ui/DESIGN-SYSTEM.md`
- `docs/development/ENHANCEMENT-ROADMAP.md`
- `docs/reference/FAQ.md`
- `docs/FEATURE-MATRIX.md`
- `docs/FILE-STORAGE.md`
- `docs/reference/GLOSSARY.md`
- `docs/KNOWN-LIMITATIONS.md`
- `docs/PAIR-DISCOVERY.md`
- `docs/PRICE-DISCOVERY.md`
- `docs/TOKEN-DISCOVERY.md`
- `docs/guides/TROUBLESHOOTING.md`

## Cross-reference rules
- Every owner document must include a `Cross-references` section.
- Navigation stubs must reference only their authoritative owners.
- Do not duplicate lifecycle or ownership claims across multiple docs.
- When two docs touch the same topic, the non-owner must link to the owner.
- Matrix docs, registries, and UX guidance must link back to their authoritative subsystem owners and adjacent governance docs.

## Cross-references
- `../APEX-ARCHITECTURE.md`
- `docs/ARCHITECTURE.md`
- `docs/PROJECT-STRUCTURE.md`


## Additional governed documents
- AI capability matrix: `docs/ai/reference/AI-CAPABILITY-MATRIX.md` (Authoritative; owned by AI capability governance; defines supported AI capabilities and measurement.)
- AI memory: `docs/ai/memory/AI-MEMORY.md` (Authoritative; owned by AI memory governance; defines memory storage, retrieval, and context handling.)
- Prompt engineering: `docs/PROMPT-ENGINEERING.md` (Authoritative; owned by AI prompt governance; defines prompt design and construction guidance.)
- AI cost management: `docs/AI-COST-MANAGEMENT.md` (Authoritative; owned by AI cost governance; defines cost tracking, limits, and optimisation.)
- Chain registry: `docs/CHAIN-REGISTRY.md` (Registry; owned by market/data/routing authority; lists supported chains and chain metadata.)
- DEX registry: `docs/DEX-REGISTRY.md` (Registry; owned by market/data/routing authority; lists supported DEXs and DEX metadata.)
- Token registry: `docs/TOKEN-REGISTRY.md` (Registry; owned by market/data/routing authority; lists token definitions and addresses.)
- Oracle registry: `docs/ORACLE-REGISTRY.md` (Registry; owned by market/data/routing authority; lists oracle providers and feeds.)
- Dashboard widgets: `docs/dashboard/DASHBOARD-WIDGETS.md` (Authoritative; owned by desktop/UI authority; defines the available dashboard widgets.)
- Dashboard layout: `docs/dashboard/DASHBOARD-LAYOUT.md` (Authoritative; owned by desktop/UI authority; defines layout, grid, and responsive behavior.)
- UX guidelines: `docs/ui/UX-GUIDELINES.md` (Authoritative; owned by desktop/UI authority; defines interaction and presentation standards.)
- Versioning: `docs/deployment/VERSIONING.md` (Support; owned by governance/schema/config/API authorities; describes versioning strategy.)


## New autonomous OS contracts
- Runtime orchestrator: `docs/ORCHESTRATOR.md` (CONTRACT; v1.0.0; owns startup/shutdown sequencing, platform mode transitions, subsystem gating, recovery delegation)
- AI orchestration: `docs/ai/orchestration/AI-ORCHESTRATION.md` (CONTRACT; v1.0.0; owns multi-agent coordination, orchestration modes, consensus protocol)
- AI agent specification: `docs/ai/reference/AI-AGENT-SPECIFICATION.md` (stub; owned by AI-ORCHESTRATION.md)
- AI consensus: `docs/ai/reasoning/AI-CONSENSUS.md` (stub; owned by AI-ORCHESTRATION.md)
- Plugin SDK: `docs/PLUGIN-SDK.md`
- Plugin marketplace: `docs/PLUGIN-MARKETPLACE.md`
- Domain model: `docs/DOMAIN-MODEL.md` (CONTRACT; v1.1.0; owns entity definitions, PKs, relationships, invariants)
- Metrics: `docs/reference/METRICS.md` (stub)
- Healthchecks: `docs/operations/HEALTHCHECKS.md` (CONTRACT; v1.1.0; owns health probe definitions, health state machine, aggregate health score)

## Cross-system integration contracts (Phase 1-4 additions)
- End-to-end wiring: `docs/END-TO-END-WIRING-CONTRACT.md` (CONTRACT; v1.0.0; owns signal flow, data flow contract, event sequencing, failure branching, timing budget, config ownership)
- Runtime flow lifecycle: `docs/RUNTIME-FLOW-LIFECYCLE.md` (CONTRACT; v1.0.0; owns 10 runtime flows with step-by-step sequencing)
- State machine index: `docs/state-machines/STATE-MACHINE-INDEX.md` (INDEX; v1.1.0; owns inter-state-machine coupling, startup/shutdown state coupling, recovery coordination)
- Recovery coordination: `docs/operations/RECOVERY-COORDINATION.md` (CONTRACT; owns multi-failure recovery coordination, phased recovery ordering)
- Feature flag governance: `docs/configuration/FEATURE-FLAG-GOVERNANCE-AND-ROLLOUT-MATRIX.md` (CONTRACT; owns feature flag definitions, rollout stages)
- Documentation status review: `docs/DOCUMENTATION-STATUS-REVIEW-WORKFLOW.md` (CONTRACT; owns documentation review and lifecycle governance)

## Windows Platform contracts (deepened Phase 5)
- Windows app architecture: `docs/windows/WINDOWS-APP-ARCHITECTURE.md` (CONTRACT; v1.0.0; owns 4-process model, tray lifecycle, sleep/resume, portable mode, crash dumps)
- Windows service integration: `docs/windows/WINDOWS-SERVICE-INTEGRATION.md` (CONTRACT; v1.0.0; owns service lifecycle state machine, recovery actions, session 0)
- Windows network resilience: `docs/windows/WINDOWS-NETWORK-RESILIENCE.md` (CONTRACT; v1.0.0; owns network detection, reconnect backoff, proxy handling, DNS)
- Windows notification integration: `docs/windows/WINDOWS-NOTIFICATION-INTEGRATION.md` (CONTRACT; v1.0.0; owns notification channels, severity mapping, rate limiting)
- Windows security integration: `docs/security/WINDOWS-SECURITY-INTEGRATION.md` (CONTRACT; v1.0.0; owns DPAPI, code signing, update chain, AppContainer)
- Windows desktop: `docs/windows/WINDOWS-DESKTOP.md` (CONTRACT; v1.0.0; owns window states, first-run wizard, offline/degraded UI)
- Windows deployment: `docs/deployment/WINDOWS-DEPLOYMENT.md` (CONTRACT; v1.0.0; owns 3 package formats, installer lifecycle, update/rollback)

## Deepened subsystem contracts (Phase 5)
- Dashboard widgets: `docs/dashboard/DASHBOARD-WIDGETS.md` (CONTRACT; v1.0.0; deepened — lifecycle hooks, rendering pipeline, dependency graph)
- Dashboard runtime: `docs/dashboard/DASHBOARD-RUNTIME.md` (CONTRACT; v1.0.0; deepened — init sequence, IPC bridge contract)
- Dashboard layout: `docs/dashboard/DASHBOARD-LAYOUT.md` (CONTRACT; v1.0.0; deepened — dock contract schema, layout serialization + migration)
- Dashboard workspaces: `docs/dashboard/DASHBOARD-WORKSPACES.md` (CONTRACT; v1.0.0; deepened — cross-subsystem integration)
- AI provider manager: `docs/ai/providers/AI-PROVIDER-MANAGER.md` (CONTRACT; v1.0.0; deepened — 7-provider inventory, scoring algorithm, failover matrix)
- Trading engine: `docs/TRADING-ENGINE.md` (CONTRACT; v1.0.0; deepened — 11-step execution algorithm, risk scoring, MEV decision tree)
- Execution engine: `docs/EXECUTION-ENGINE.md` (CONTRACT; v1.0.0; deepened — multi-chain execution, gas handling)
- Threading model: `docs/performance/THREADING-MODEL.md` (CONTRACT; v1.0.0; deepened — thread ownership matrix, deadlock prevention)
- Worker pool: `docs/WORKER-POOL.md` (CONTRACT; v1.0.0; deepened — lifecycle state machine, priority queues, scaling policy)
- Task scheduler: `docs/TASK-SCHEDULER.md` (CONTRACT; v1.0.0; deepened — 5 scheduler components, 16 scheduled tasks)
- Plugin lifecycle: `docs/PLUGIN-LIFECYCLE.md` (CONTRACT; v1.0.0; deepened — discovery, dependency resolution, capability negotiation)
- Event bus: `docs/EVENT-BUS.md` (CONTRACT; v1.0.0; deepened — producer/consumer contracts, exactly-once protocol, DLQ)
- Database schema: `docs/DATABASE-SCHEMA.md` (CONTRACT; v1.0.0; deepened — query patterns, backup/restore, partitioning)
- Security: `docs/security/SECURITY.md` (CONTRACT; v1.0.0; deepened — STRIDE threat model, secure update chain)
- Testing: `docs/testing/TESTING.md` (CONTRACT; v1.0.0; deepened — 10-layer pyramid, contract/state-machine/chaos testing)
- IPC protocol: `docs/IPC-PROTOCOL.md` (CONTRACT; v1.0.0; deepened — named pipe transport, envelope schema, typed channel catalog, delivery semantics, versioning, anonymization)
- IPC message catalog: `docs/IPC-MESSAGE-CATALOG.md` (REFERENCE; v1.0.0; deepened — complete message type catalog with 7 categories, payload schemas, error behavior)## Product surface contracts
- UI Dashboard: `docs/dashboard/UI-DASHBOARD-SPEC.md`
- AI Provider Manager: `docs/ai/providers/AI-PROVIDER-MANAGER.md`
- AI Gateway: `docs/ai/runtime/AI-GATEWAY.md`
- AI Memory System: `docs/ai/memory/AI-MEMORY-SYSTEM.md`
- Risk Engine: `docs/RISK-ENGINE.md`
- Notification Center: `docs/NOTIFICATION-CENTER.md`
- Chain Command Center: `docs/CHAIN-COMMAND-CENTER.md`
- DEX Intelligence: `docs/DEX-INTELLIGENCE.md`
- Wallet Command Center: `docs/WALLET-COMMAND-CENTER.md`
- Portfolio Analytics: `docs/PORTFOLIO-ANALYTICS.md`
- Enterprise Operations: `docs/operations/ENTERPRISE-OPERATIONS.md`

- TRADING-LIFECYCLE.md — Authoritative

- EXECUTION-LIFECYCLE.md — Authoritative

- SHUTDOWN-LIFECYCLE.md — Authoritative

- INTERFACE-PROVIDER-ADAPTER.md — Authoritative

- INTERFACE-AGENT-MESSAGE.md — Authoritative

- INTERFACE-TOOL-CALL.md — Authoritative

- INTERFACE-NOTIFICATION-CHANNEL.md — Authoritative

- SECURITY-CONTRACTS.md — Authoritative

- PERFORMANCE-SLOS.md — Authoritative


## Authority Conflicts
- AI-PIPELINE.md slimmed down; orchestration, consensus, provider, and memory logic now owned by dedicated docs.
- RUNTIME-OPERATIONS.md slimmed down; health, recovery, and shutdown logic now owned by dedicated docs.
- DASHBOARD-LAYOUT.md and DASHBOARD-WIDGETS.md slimmed down; UI interaction logic now owned by UI-DASHBOARD-SPEC.md.
- ARCHITECTURE.md and SIMULATION-ENGINE.md slimmed down; trading and execution lifecycle now owned by lifecycle docs.

- STRATEGY-ROTATION.md — Authoritative

- CHAIN-ROTATION.md — Authoritative

- TOKEN-INTELLIGENCE.md — Authoritative

- ROUTE-OPTIMIZATION.md — Authoritative

- CONTRACT-MANAGEMENT.md — Authoritative

- PROVIDER-RESILIENCE.md — Authoritative


## Ultra Vision ownership
- Strategy rotation: `STRATEGY-ROTATION.md`
- Chain rotation: `CHAIN-ROTATION.md`
- Token intelligence: `TOKEN-INTELLIGENCE.md`
- Route optimization: `ROUTE-OPTIMIZATION.md`
- Contract management: `CONTRACT-MANAGEMENT.md`
- Provider resilience: `PROVIDER-RESILIENCE.md`

- EVENT-BUS.md — Authoritative

- WORKER-POOL.md — Authoritative

- REGISTRY-SYSTEM.md — Authoritative

- DASHBOARD-WORKSPACES.md — Authoritative

- LEARNING-PIPELINE.md — Authoritative


## Infrastructure contracts
- Event Bus: `EVENT-BUS.md`
- Worker Pool: `WORKER-POOL.md`
- Registry System: `REGISTRY-SYSTEM.md`
- Dashboard Workspaces: `dashboard/DASHBOARD-WORKSPACES.md`
- Learning Pipeline: `LEARNING-PIPELINE.md`

- DECISION-ENGINE.md — Authoritative

- POLICY-ENGINE.md — Authoritative


## Governance contracts
- Decision Engine: `DECISION-ENGINE.md`
- Policy Engine: `POLICY-ENGINE.md`

- APEX-KERNEL.md — Authoritative

- SERVICE-REGISTRY.md — Authoritative

- DEPENDENCY-GRAPH.md — Authoritative

- EXPLAINABILITY.md — Authoritative

- WORKFLOW-BUILDER.md — Authoritative

- KNOWLEDGE-GRAPH.md — Authoritative


## APEX DNA contracts
- APEX Kernel: `APEX-KERNEL.md`
- Service Registry: `SERVICE-REGISTRY.md`
- Dependency Graph: `DEPENDENCY-GRAPH.md`
- Explainability: `EXPLAINABILITY.md`
- Workflow Builder: `WORKFLOW-BUILDER.md`
- Knowledge Graph: `KNOWLEDGE-GRAPH.md`

- GOVERNANCE-EXPLAINABILITY.md — Authoritative

- LIVE-ARCHITECTURE-VIEWER.md — Authoritative

- DATA-GOVERNANCE.md — Authoritative


## Central governance contracts
- Governance Explainability: `GOVERNANCE-EXPLAINABILITY.md`
- Live Architecture Viewer: `LIVE-ARCHITECTURE-VIEWER.md`
- Data Governance: `DATA-GOVERNANCE.md`

- DECISION-LEDGER.md — Authoritative

- CONTEXT-BUILDER.md — Authoritative

- RUNTIME-KNOWLEDGE.md — Authoritative

- SYSTEM-CAPABILITY-REGISTRY.md — Authoritative

- FEATURE-FLAGS.md — Authoritative

- CONFIGURATION-PROFILES.md — Authoritative

- AI-REASONING-POLICY.md — Authoritative

- AI-CONTEXT-WINDOW-MANAGEMENT.md — Authoritative

- MODEL-CAPABILITY-NEGOTIATION.md — Authoritative

- EXECUTION-POLICIES.md — Authoritative

- ROUTE-SCORING-MODEL.md — Authoritative

- MARKET-REGIME-DETECTION.md — Authoritative

- RESOURCE-MANAGER.md — Authoritative

- TASK-SCHEDULER.md — Authoritative

- SELF-HEALING.md — Authoritative


## Final platform doctrines
- Decision Ledger: `DECISION-LEDGER.md`
- Context Builder: `CONTEXT-BUILDER.md`
- Runtime Knowledge: `RUNTIME-KNOWLEDGE.md`
- System Capability Registry: `SYSTEM-CAPABILITY-REGISTRY.md`
- Feature Flags: `configuration/FEATURE-FLAGS.md`
- Configuration Profiles: `configuration/CONFIGURATION-PROFILES.md`
- AI Reasoning Policy: `ai/reasoning/AI-REASONING-POLICY.md`
- AI Context Window Management: `ai/runtime/AI-CONTEXT-WINDOW-MANAGEMENT.md`
- Model Capability Negotiation: `MODEL-CAPABILITY-NEGOTIATION.md`
- Execution Policies: `EXECUTION-POLICIES.md`
- Route Scoring Model: `ROUTE-SCORING-MODEL.md`
- Market Regime Detection: `MARKET-REGIME-DETECTION.md`
- Resource Manager: `RESOURCE-MANAGER.md`
- Task Scheduler: `TASK-SCHEDULER.md`
- Self-Healing: `operations/SELF-HEALING.md`

- APEX-OS.md — Authoritative

- SERVICE-LIFECYCLE.md — Authoritative

- PLUGIN-LIFECYCLE.md — Authoritative

- WORKSPACE-MANAGER.md — Authoritative

- AI-TOOLS.md — Authoritative

- AI-PLANNER.md — Authoritative

- AI-REFLECTION.md — Authoritative

- AI-KNOWLEDGE-INDEX.md — Authoritative

- TRADE-EXPLAINER.md — Authoritative

- MARKET-SESSION.md — Authoritative

- OPPORTUNITY-LIFECYCLE.md — Authoritative


## Consolidated doctrinal owners
- APEX OS: `APEX-OS.md`
- Service Lifecycle: `SERVICE-LIFECYCLE.md`
- Plugin Lifecycle: `PLUGIN-LIFECYCLE.md`
- Workspace Manager: `WORKSPACE-MANAGER.md`
- AI Tools: `ai/tools/AI-TOOLS.md`
- AI Planner: `ai/planning/AI-PLANNER.md`
- AI Reflection: `ai/reasoning/AI-REFLECTION.md`
- AI Knowledge Index: `AI-KNOWLEDGE-INDEX.md`
- Trade Explainer: `TRADE-EXPLAINER.md`
- Market Session: `MARKET-SESSION.md`
- Opportunity Lifecycle: `OPPORTUNITY-LIFECYCLE.md`

- CONTRACT-REGISTRY.md — Authoritative

- RPC-MANAGER.md — Authoritative

- CACHE-MANAGER.md — Authoritative

- UPDATE-MANAGER.md — Authoritative

- DIAGNOSTICS.md — Authoritative

- BOOTSTRAP-SEQUENCE.md — Authoritative

- EVENT-CATALOG.md — Authoritative


## Governance-mode owners
- Contract Registry: `CONTRACT-REGISTRY.md`
- RPC Manager: `RPC-MANAGER.md`
- Cache Manager: `CACHE-MANAGER.md`
- Update Manager: `UPDATE-MANAGER.md`
- Diagnostics: `operations/DIAGNOSTICS.md`
- Bootstrap Sequence: `BOOTSTRAP-SEQUENCE.md`
- Event Catalog: `reference/EVENT-CATALOG.md`


## ADRs
- `adr/0001-provider-abstraction.md`
- `adr/0002-event-driven-kernel.md`
- `adr/0003-plugin-first-architecture.md`
- `adr/0004-polygon-first.md`
- `adr/0005-ai-memory.md`
- `adr/0006-runtime-governance.md`
- `adr/0007-workspace-model.md`
- `adr/0008-orchestrator-state-machine.md`


## Deepened owner docs
- `ai/runtime/AI-GATEWAY.md`
- `ai/reasoning/AI-CONSENSUS.md`
- `ai/memory/AI-MEMORY-SYSTEM.md`
- `DECISION-LOG.md`


## Deepening pass
- AI Consensus
- AI Gateway
- AI Memory System
- Decision Log


## Deepening pass - tranche 2
- Interface Provider Adapter
- Plugin Marketplace
- Risk Engine
- AI Agent Specification


## Deepening pass - tranche 3
- Interface Agent Message
- Interface Notification Channel
- Interface Tool Call
- AI Cost Management


## Deepening pass - tranche 4
- AI Knowledge Index
- AI Orchestration
- AI Provider Manager
- AI Reflection


## Deepening pass - tranche 5
- AI Settings
- Chain Registry
- DEX Registry
- Event Bus


## Deepening pass - tranche 6
- Event Flow
- Healthchecks
- Metrics
- Oracle Registry


## Deepening pass - tranche 7
- Data Flow
- Registry System
- Security
- Token Registry


## Deepening pass - tranche 8
- Token Discovery
- AI Capability Matrix
- AI Tools
- Decision Engine


## Deepening pass - tranche 9
- Opportunity Lifecycle
- Orchestrator
- Plugin Lifecycle
- Plugin SDK


## Deepening pass - tranche 10
- Opportunity Ranking
- Prompt Engineering
- Security Contracts
- Service Lifecycle


## Deepening pass - tranche 11
- Workspace Manager
- AI Context Window Management
- AI Memory
- AI Planner


## Deepening pass - tranche 12
- Bootstrap Sequence
- Cache Manager
- Contract Management
- Contract Registry


## Deepening pass - tranche 13
- Portfolio Management
- Asset Management
- Decision Ledger
- Event Catalog


## Deepening pass - tranche 14
- Portfolio Analytics
- IPC Message Catalog
- Execution Lifecycle
- Knowledge Graph


## Deepening pass - tranche 15
- IPC Protocol
- Opportunity Detection
- Position Management
- RPC Manager


## Deepening pass - tranche 16
- Runtime Knowledge
- Service Registry
- Shutdown Lifecycle
- System Capability Registry


## Deepening pass - tranche 17
- Token Intelligence
- Trading Lifecycle
- Update Manager
- Versioning


## Deepening pass - tranche 18
- Wallet Management
- AI Reasoning Policy
- Configuration Profiles
- Dashboard Workspaces


## Deepening pass - tranche 19
- UI Dashboard Spec
- Dashboard Layout
- Dashboard Widgets
- Wallet Command Center


## Deepening pass - tranche 20
- Build Release CICD
- User Guide
- UI Component Spec
- Context Builder


## Deepening pass - tranche 21
- UX Guidelines
- Data Governance
- Database Schema
- Designer Protocols


## Deepening pass - tranche 22
- Design System
- Execution Policies
- Liquidity Analysis
- Model Capability Negotiation


## Deepening pass - tranche 23
- Slippage Model
- Domain Model
- Permission Model
- Route Scoring Model


## Deepening pass - tranche 24
- Policy Engine
- Provider Resilience
- Resource Manager
- Route Optimization

## Canonical-Source Hierarchy (by Layer)

The documentation set is organised into layers. Each layer has a single authority anchor that owns the layer contract. All other docs in the layer defer to that anchor.

### Layer 0 — Foundation / OS
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | APEX-OS.md | Constitution & philosophy | Ultimate authority |
| 1 | APEX-KERNEL.md | Kernel specification | Defers to APEX-OS |
| 2 | DEPENDENCY-GRAPH.md | Module dependency graph | Defers to APEX-KERNEL |
| 3 | SERVICE-REGISTRY.md | Service discovery | Defers to DEPENDENCY-GRAPH |

### Layer 1 — Architecture & Structure
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | docs/ARCHITECTURE.md | System boundaries | Layer anchor |
| 1 | ../APEX-ARCHITECTURE.md | Root architecture index | Defers to ARCHITECTURE |
| 2 | docs/PROJECT-STRUCTURE.md | Repo layout | Defers to ARCHITECTURE |
| 3 | docs/MODULE-DEPENDENCY.md | Inter-module deps | Defers to ARCHITECTURE |
| 4 | docs/COMPONENT-DIAGRAMS.md | Visual diagrams | Defers to ARCHITECTURE |
| 5 | docs/LIVE-ARCHITECTURE-VIEWER.md | Live viz tool | Defers to ARCHITECTURE |

### Layer 2 — Runtime & Operations
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | docs/operations/RUNTIME-OPERATIONS.md | Runtime coordination | Layer anchor |
| 1 | docs/ORCHESTRATOR.md | State-machine orchestration | Defers to RUNTIME-OPERATIONS |
| 2 | docs/BOOTSTRAP-SEQUENCE.md | Startup sequencing | Defers to ORCHESTRATOR |
| 3 | docs/SHUTDOWN-LIFECYCLE.md | Shutdown sequencing | Defers to ORCHESTRATOR |
| 4 | docs/SERVICE-LIFECYCLE.md | Service lifecycle | Defers to RUNTIME-OPERATIONS |
| 5 | docs/WORKER-ARCHITECTURE.md | Worker design | Defers to RUNTIME-OPERATIONS |
| 6 | docs/WORKER-POOL.md | Pool orchestration | Defers to WORKER-ARCHITECTURE |
| 7 | docs/QUEUE-MANAGEMENT.md | Queue management | Defers to WORKER-POOL |
| 8 | docs/operations/RECOVERY-AND-FAILOVER.md | Recovery/failover | Defers to RUNTIME-OPERATIONS |
| 9 | docs/operations/HEALTHCHECKS.md | Health probes | Defers to RUNTIME-OPERATIONS |
| 10 | docs/TASK-SCHEDULER.md | Task scheduling | Defers to RUNTIME-OPERATIONS |
| 11 | docs/operations/SELF-HEALING.md | Auto-recovery | Defers to RUNTIME-OPERATIONS |
| 12 | docs/UPDATE-MANAGER.md | Update management | Defers to RUNTIME-OPERATIONS |

### Layer 3 — Trading & Execution
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | docs/TRADING-ENGINE.md | Trade orchestration | Layer anchor |
| 1 | docs/EXECUTION-ENGINE.md | Transaction execution | Defers to TRADING-ENGINE |
| 2 | docs/TRADING-LIFECYCLE.md | Trade state machine | Defers to TRADING-ENGINE |
| 3 | docs/EXECUTION-LIFECYCLE.md | Execution state machine | Defers to EXECUTION-ENGINE |
| 4 | docs/TRANSACTION-LIFECYCLE.md | Transaction states | Defers to EXECUTION-ENGINE |
| 5 | docs/RISK-ENGINE.md | Risk enforcement | Defers to TRADING-ENGINE |
| 6 | docs/STRATEGIES.md | Strategy catalog | Defers to TRADING-ENGINE |
| 7 | docs/STRATEGY-ROTATION.md | Strategy rotation | Defers to STRATEGIES |
| 8 | docs/OPPORTUNITY-DETECTION.md | Opportunity detection | Defers to MARKET-INTELLIGENCE |
| 9 | docs/OPPORTUNITY-RANKING.md | Opportunity ranking | Defers to MARKET-INTELLIGENCE |
| 10 | docs/OPPORTUNITY-LIFECYCLE.md | Opportunity states | Defers to MARKET-INTELLIGENCE |
| 11 | docs/ORDER-MANAGEMENT.md | Order management | Defers to EXECUTION-ENGINE |
| 12 | docs/DECISION-ENGINE.md | Decision engine | Defers to TRADING-ENGINE |
| 13 | docs/POLICY-ENGINE.md | Policy engine | Defers to DECISION-ENGINE |
| 14 | docs/TRADE-EXPLAINER.md | Trade explainability | Defers to TRADING-ENGINE |

### Layer 4 — Market Data & Intelligence
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | docs/MARKET-DATA.md | Market data | Layer anchor |
| 1 | docs/MARKET-INTELLIGENCE.md | Market intelligence | Defers to MARKET-DATA |
| 2 | docs/MARKET-SESSION.md | Market session | Defers to MARKET-INTELLIGENCE |
| 3 | docs/MARKET-REGIME-DETECTION.md | Regime detection | Defers to MARKET-INTELLIGENCE |
| 4 | docs/ROUTING-ENGINE.md | Route selection | Defers to MARKET-INTELLIGENCE |
| 5 | docs/ROUTE-OPTIMIZATION.md | Route optimization | Defers to ROUTING-ENGINE |
| 6 | docs/ROUTE-SCORING-MODEL.md | Route scoring | Defers to ROUTE-OPTIMIZATION |
| 7 | docs/LIQUIDITY-ANALYSIS.md | Liquidity analysis | Defers to MARKET-INTELLIGENCE |
| 8 | docs/SLIPPAGE-MODEL.md | Slippage model | Defers to LIQUIDITY-ANALYSIS |
| 9 | docs/GAS-OPTIMISATION.md | Gas optimization | Defers to MARKET-INTELLIGENCE |
| 10 | docs/MEV-PROTECTION.md | MEV protection | Defers to MARKET-INTELLIGENCE |
| 11 | docs/CHAIN-INTELLIGENCE.md | Chain intelligence | Defers to MARKET-INTELLIGENCE |
| 12 | docs/TOKEN-INTELLIGENCE.md | Token intelligence | Defers to CHAIN-INTELLIGENCE |

### Layer 5 — Chain & DEX Integration
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | docs/CHAIN-INTEGRATION.md | Chain adapter guide | Layer anchor |
| 1 | docs/CHAIN-REGISTRY.md | Chain registry | Defers to CHAIN-INTEGRATION |
| 2 | docs/CHAIN-ROTATION.md | Chain rotation | Defers to CHAIN-REGISTRY |
| 3 | docs/DEX-INTEGRATION.md | DEX adapter guide | Defers to CHAIN-INTEGRATION |
| 4 | docs/DEX-REGISTRY.md | DEX registry | Defers to DEX-INTEGRATION |
| 5 | docs/DEX-INTELLIGENCE.md | DEX intelligence | Defers to DEX-REGISTRY |
| 6 | docs/TOKEN-REGISTRY.md | Token registry | Defers to CHAIN-INTEGRATION |
| 7 | docs/ORACLE-REGISTRY.md | Oracle registry | Defers to CHAIN-INTEGRATION |

### Layer 6 — AI & Decision Pipeline
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | docs/ai/runtime/AI-PIPELINE.md | AI decision pipeline | Layer anchor |
| 1 | docs/ai/orchestration/AI-ORCHESTRATION.md | AI orchestration | Defers to AI-PIPELINE |
| 2 | docs/ai/reference/AI-AGENT-SPECIFICATION.md | Agent specification | Defers to AI-ORCHESTRATION |
| 3 | docs/ai/reasoning/AI-CONSENSUS.md | Multi-agent consensus | Defers to AI-ORCHESTRATION |
| 4 | docs/ai/providers/AI-PROVIDER-MANAGER.md | Provider management | Defers to AI-PIPELINE |
| 5 | docs/ai/runtime/AI-GATEWAY.md | AI gateway | Defers to AI-PROVIDER-MANAGER |
| 6 | docs/ai/providers/AI-SETTINGS.md | AI settings | Defers to AI-PIPELINE |
| 7 | docs/ai/tools/AI-TOOLS.md | AI tool registry | Defers to AI-PIPELINE |
| 8 | docs/ai/planning/AI-PLANNER.md | AI planning | Defers to AI-ORCHESTRATION |
| 9 | docs/ai/reasoning/AI-REFLECTION.md | AI reflection | Defers to AI-ORCHESTRATION |
| 10 | docs/ai/memory/AI-MEMORY.md | AI memory | Defers to AI-PIPELINE |
| 11 | docs/ai/memory/AI-MEMORY-SYSTEM.md | Memory system contract | Defers to AI-MEMORY |
| 12 | docs/AI-KNOWLEDGE-INDEX.md | Knowledge index | Defers to AI-MEMORY |
| 13 | docs/AI-COST-MANAGEMENT.md | Cost management | Defers to AI-PIPELINE |
| 14 | docs/ai/reference/AI-CAPABILITY-MATRIX.md | Capability matrix | Defers to AI-PROVIDER-MANAGER |
| 15 | docs/ai/runtime/AI-CONTEXT-WINDOW-MANAGEMENT.md | Context window mgmt | Defers to AI-PIPELINE |
| 16 | docs/ai/reasoning/AI-REASONING-POLICY.md | Reasoning policy | Defers to AI-ORCHESTRATION |
| 17 | docs/ai/safety/AI-SAFETY-BOUNDARY.md | Safety boundary | Defers to AI-ORCHESTRATION |
| 18 | docs/MODEL-CAPABILITY-NEGOTIATION.md | Model negotiation | Defers to AI-PROVIDER-MANAGER |
| 19 | docs/CLOUD-AI-INTEGRATION.md | Cloud AI integration | Defers to AI-PIPELINE |

### Layer 7 — Wallet & Assets
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | docs/WALLET-MANAGEMENT.md | Wallet management | Layer anchor |
| 1 | docs/WALLET-COMMAND-CENTER.md | Wallet command center | Defers to WALLET-MANAGEMENT |
| 2 | docs/ASSET-MANAGEMENT.md | Asset management | Defers to WALLET-MANAGEMENT |
| 3 | docs/PORTFOLIO-MANAGEMENT.md | Portfolio management | Defers to ASSET-MANAGEMENT |
| 4 | docs/PORTFOLIO-ANALYTICS.md | Portfolio analytics | Defers to PORTFOLIO-MANAGEMENT |
| 5 | docs/POSITION-MANAGEMENT.md | Position management | Defers to PORTFOLIO-MANAGEMENT |

### Layer 8 — Dashboard & UI
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | docs/dashboard/UI-DASHBOARD-SPEC.md | Dashboard spec | Layer anchor |
| 1 | docs/dashboard/DASHBOARD-LAYOUT.md | Layout composition | Defers to UI-DASHBOARD-SPEC |
| 2 | docs/dashboard/DASHBOARD-WIDGETS.md | Widget catalog | Defers to UI-DASHBOARD-SPEC |
| 3 | docs/dashboard/DASHBOARD-WORKSPACES.md | Workspace persistence | Defers to UI-DASHBOARD-SPEC |
| 4 | docs/ui/UX-GUIDELINES.md | UX/interaction guide | Defers to UI-DASHBOARD-SPEC |
| 5 | docs/ui/UI-COMPONENT-SPEC.md | Component spec | Defers to UI-DASHBOARD-SPEC |
| 6 | docs/ui/DESIGN-SYSTEM.md | Design system | Defers to UX-GUIDELINES |
| 7 | docs/DESIGNER-PROTOCOLS.md | Designer protocols | Defers to UI-DASHBOARD-SPEC |

### Layer 9 — Windows Platform
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | docs/windows/WINDOWS-DESKTOP.md | Windows desktop shell | Layer anchor |
| 1 | docs/WINDOWS-INSTALLER-SPEC.md | Installer spec | Defers to WINDOWS-DESKTOP |
| 2 | docs/SERVICE-MODE.md | Windows service mode | Defers to WINDOWS-DESKTOP |

### Layer 10 — IPC & Communication
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | docs/IPC-PROTOCOL.md | IPC protocol | Layer anchor |
| 1 | docs/IPC-MESSAGE-CATALOG.md | IPC message catalog | Defers to IPC-PROTOCOL |
| 2 | docs/EVENT-FLOW.md | Event flow | Defers to IPC-PROTOCOL |
| 3 | docs/DATA-FLOW.md | Data flow | Defers to IPC-PROTOCOL |

### Layer 11 — Security & Trust
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | docs/security/SECURITY.md | Security | Layer anchor |
| 1 | docs/security/SECURITY-CONTRACTS.md | Security contracts | Defers to SECURITY |
| 2 | docs/security/PERMISSION-MODEL.md | Permission model | Defers to SECURITY-CONTRACTS |
| 3 | docs/TRUST-BOUNDARIES.md | Trust boundaries | Defers to SECURITY-CONTRACTS |
| 4 | docs/security/SECRET-LIFECYCLE.md | Secret lifecycle | Defers to SECURITY |

### Layer 12 — Data & Persistence
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | docs/DATABASE-SCHEMA.md | Database schema | Layer anchor |
| 1 | docs/STATE-MANAGEMENT.md | State management | Defers to DATABASE-SCHEMA |
| 2 | docs/CACHE-MANAGER.md | Cache management | Defers to STATE-MANAGEMENT |
| 3 | docs/CONTEXT-BUILDER.md | Context builder | Defers to STATE-MANAGEMENT |
| 4 | docs/RUNTIME-KNOWLEDGE.md | Runtime knowledge | Defers to CONTEXT-BUILDER |
| 5 | docs/DECISION-LEDGER.md | Decision ledger | Defers to DATABASE-SCHEMA |
| 6 | docs/FILE-STORAGE.md | File storage | Defers to DATABASE-SCHEMA |
| 7 | docs/KNOWLEDGE-GRAPH.md | Knowledge graph | Defers to CONTEXT-BUILDER |

### Layer 13 — Plugins
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | docs/PLUGIN-SDK.md | Plugin SDK | Layer anchor |
| 1 | docs/APP-BUILDER-PLUGIN-SYSTEM.md | Plugin system | Defers to PLUGIN-SDK |
| 2 | docs/APP-BUILDER-WORKFLOW.md | App builder workflow | Defers to APP-BUILDER-PLUGIN-SYSTEM |
| 3 | docs/deployment/APP-BUILDER-DEPLOYMENT-GUIDE.md | Deployment guide | Defers to APP-BUILDER-WORKFLOW |
| 4 | docs/PLUGIN-LIFECYCLE.md | Plugin lifecycle | Defers to PLUGIN-SDK |
| 5 | docs/PLUGIN-MARKETPLACE.md | Plugin marketplace | Defers to PLUGIN-SDK |
| 6 | docs/PLUGIN-SANDBOX-CONTRACT.md | Plugin sandbox | Defers to PLUGIN-SDK |

### Layer 14 — Configuration & Governance
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | docs/configuration/CONFIGURATION.md | Configuration | Layer anchor |
| 1 | docs/configuration/CONFIGURATION-REFERENCE.md | Key-by-key reference | Defers to CONFIGURATION |
| 2 | docs/configuration/CONFIGURATION-PROFILES.md | Profile system | Defers to CONFIGURATION |
| 3 | docs/configuration/FEATURE-FLAGS.md | Feature flags | Defers to CONFIGURATION |
| 4 | docs/FEATURE-GATES.md | Feature gates | Defers to FEATURE-FLAGS |
| 5 | docs/CONTRACT-REGISTRY.md | Contract registry | Defers to CONFIGURATION |
| 6 | docs/SYSTEM-CAPABILITY-REGISTRY.md | Capability registry | Defers to CONFIGURATION |

### Layer 15 — Events & Messaging
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | docs/EVENT-BUS.md | Event bus | Layer anchor |
| 1 | docs/reference/EVENT-CATALOG.md | Event catalog | Defers to EVENT-BUS |
| 2 | docs/EVENT-OWNERSHIP-MATRIX.md | Ownership matrix | Defers to EVENT-CATALOG |

### Layer 16 — Monitoring & Observability
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | docs/operations/MONITORING-OBSERVABILITY.md | Monitoring/observability | Layer anchor |
| 1 | docs/reference/METRICS.md | Metrics catalog | Defers to MONITORING-OBSERVABILITY |
| 2 | docs/operations/DIAGNOSTICS.md | Diagnostics | Defers to MONITORING-OBSERVABILITY |
| 3 | docs/ERROR-HANDLING-LOGGING.md | Error handling/logging | Defers to MONITORING-OBSERVABILITY |
| 4 | docs/ERROR-CATALOG.md | Error catalog | Defers to ERROR-HANDLING-LOGGING |
| 5 | docs/reference/ERROR-CODES.md | Error codes | Defers to ERROR-HANDLING-LOGGING |
| 6 | docs/FAILURE-MATRIX.md | Failure matrix | Defers to ERROR-HANDLING-LOGGING |
| 7 | docs/operations/FAILURE-RECOVERY-MATRIX.md | Failure recovery matrix | Defers to FAILURE-MATRIX |
| 8 | docs/operations/RECOVERY-PLAYBOOK.md | Recovery playbook | Defers to FAILURE-RECOVERY-MATRIX |
| 9 | docs/performance/PERFORMANCE-TARGETS.md | Performance targets | Defers to MONITORING-OBSERVABILITY |
| 10 | docs/NON-FUNCTIONAL-REQUIREMENTS.md | NFRs | Defers to MONITORING-OBSERVABILITY |
| 11 | docs/RESOURCE-MANAGER.md | Resource manager | Defers to MONITORING-OBSERVABILITY |

### Layer 17 — Simulation & Testing
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | docs/SIMULATION-ENGINE.md | Simulation framework | Layer anchor |
| 1 | docs/testing/BACKTESTING.md | Backtesting | Defers to SIMULATION-ENGINE |
| 2 | docs/guides/TESTING-GUIDE.md | Testing guide | Defers to SIMULATION-ENGINE |

### Layer 18 — API & Contracts
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | docs/API-CONTRACTS.md | API contracts | Layer anchor |
| 1 | docs/API-REFERENCE.md | API reference | Defers to API-CONTRACTS |
| 2 | docs/DOMAIN-MODEL.md | Domain model | Defers to API-CONTRACTS |
| 3 | docs/CONTRACT-MANAGEMENT.md | Contract management | Defers to DOMAIN-MODEL |

### Layer 19 — Developer & User Guides
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | docs/development/CONTRIBUTING.md | Contributing guide | Layer anchor |
| 1 | docs/development/CODING-STANDARDS.md | Coding standards | Defers to CONTRIBUTING |
| 2 | docs/deployment/BUILD-RELEASE-CICD.md | Build/release/CI/CD | Defers to CONTRIBUTING |
| 3 | docs/deployment/DEPLOYMENT.md | Deployment guide | Defers to BUILD-RELEASE-CICD |
| 4 | docs/guides/USER-GUIDE.md | User guide | Standalone |
| 5 | docs/guides/USER-FLOWS.md | User workflows | Standalone |
| 6 | docs/reference/FAQ.md | FAQ | Standalone |
| 7 | docs/guides/TROUBLESHOOTING.md | Troubleshooting | Standalone |
| 8 | docs/development/IMPLEMENTATION-ROADMAP.md | Roadmap | Standalone |
| 9 | docs/development/ENHANCEMENT-ROADMAP.md | Enhancement roadmap | Standalone |
| 10 | docs/CHANGELOG.md | Changelog | Standalone |
| 11 | docs/KNOWN-LIMITATIONS.md | Known limitations | Standalone |
| 12 | docs/reference/GLOSSARY.md | Glossary | Standalone |
| 13 | docs/FEATURE-MATRIX.md | Feature matrix | Standalone |
| 14 | docs/deployment/VERSIONING.md | Versioning | Standalone |

### Layer 20 — Documentation Governance
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | DOCUMENTATION-MAP.md | This document | Layer anchor |
| 1 | docs/CANONICAL-SOURCE-RULES.md | Canonical source rules | Defers to DOCUMENTATION-MAP |
| 2 | docs/DOCUMENTATION-LIFECYCLE.md | Documentation lifecycle | Defers to DOCUMENTATION-MAP |
| 3 | docs/CROSS-REFERENCE-INDEX.md | Cross-reference index | Defers to DOCUMENTATION-MAP |
| 4 | docs/TRACEABILITY-MATRIX.md | Traceability matrix | Defers to DOCUMENTATION-MAP |
| 5 | docs/MODULE-OWNERSHIP-MATRIX.md | Module ownership | Defers to DOCUMENTATION-MAP |
| 6 | docs/DEPENDENCY-AUTHORITY-RULES.md | Dep/authority rules | Defers to CANONICAL-SOURCE-RULES |
| 7 | docs/DATA-OWNERSHIP.md | Data ownership | Defers to CANONICAL-SOURCE-RULES |

---

## Document Status / Version Metadata

Each canonical document in the set should carry the following front-matter fields in its body:

| Field | Required | Description |
|-------|----------|-------------|
| Version | Yes | Semantic version (MAJOR.MINOR.PATCH) |
| Status | Yes | One of: `Draft`, `Review`, `Canonical`, `Deprecated`, `Archived` |
| Last Updated | Yes | ISO-8601 date of last substantive change |
| Owner | Yes | Team or individual responsible |
| Document Type | Yes | `[INDEX]`, `[OVERVIEW]`, `[REFERENCE]`, `[CONTRACT]`, `[GUIDE]`, `[REGISTRY]` |

### Current status of core documents

| Document | Version | Status | Last Updated | Owner |
|----------|---------|--------|-------------|-------|
| APEX-OS.md | 1.0.0 | Canonical | 2025-01-15 | Architecture |
| docs/ARCHITECTURE.md | 1.0.0 | Canonical | 2025-01-15 | Architecture |
| docs/operations/RUNTIME-OPERATIONS.md | 1.0.0 | Canonical | 2025-01-15 | Runtime |
| docs/TRADING-ENGINE.md | 1.0.0 | Review | 2025-01-15 | Trading |
| docs/EXECUTION-ENGINE.md | 1.0.0 | Review | 2025-01-15 | Execution |
| docs/ai/runtime/AI-PIPELINE.md | 1.0.0 | Canonical | 2025-01-15 | AI |
| docs/RISK-ENGINE.md | 1.0.0 | Review | 2025-01-15 | Risk |
| docs/security/SECURITY.md | 1.0.0 | Review | 2025-01-15 | Security |
| docs/configuration/CONFIGURATION.md | 1.0.0 | Canonical | 2025-01-15 | Config |
| docs/DATABASE-SCHEMA.md | 1.0.0 | Draft | 2025-01-15 | Data |
| docs/security/SECURITY-CONTRACTS.md | 1.0.0 | Draft | 2025-01-15 | Security |
| docs/STATE-MANAGEMENT.md | 1.0.0 | Draft | 2025-01-15 | Runtime |
| docs/EVENT-BUS.md | 1.0.0 | Draft | 2025-01-15 | Runtime |
| docs/operations/MONITORING-OBSERVABILITY.md | 1.0.0 | Draft | 2025-01-15 | Ops |
| docs/SIMULATION-ENGINE.md | 1.0.0 | Draft | 2025-01-15 | Trading |
| docs/PLUGIN-SDK.md | 1.0.0 | Draft | 2025-01-15 | Plugin |
| docs/windows/WINDOWS-DESKTOP.md | 1.0.0 | Draft | 2025-01-15 | Windows |
| docs/IPC-PROTOCOL.md | 1.0.0 | Draft | 2025-01-15 | Runtime |
| docs/WALLET-MANAGEMENT.md | 1.0.0 | Draft | 2025-01-15 | Trading |
| docs/API-CONTRACTS.md | 1.0.0 | Draft | 2025-01-15 | Architecture |
| docs/MARKET-DATA.md | 1.0.0 | Draft | 2025-01-15 | Trading |
| docs/dashboard/UI-DASHBOARD-SPEC.md | 1.0.0 | Draft | 2025-01-15 | UI |
| docs/development/CONTRIBUTING.md | 1.0.0 | Draft | 2025-01-15 | DevRel |
| docs/DOCUMENTATION-LIFECYCLE.md | 1.0.0 | Draft | 2025-01-15 | Architecture |
| DOCUMENTATION-MAP.md | 1.2.0 | Canonical | 2026-07-27 | Architecture |
| docs/TRACEABILITY-MATRIX.md | 1.0.0 | Canonical | 2025-01-15 | Architecture |
| docs/MODULE-OWNERSHIP-MATRIX.md | 1.0.0 | Draft | 2025-01-15 | Architecture |
| docs/CANONICAL-SOURCE-RULES.md | 1.0.0 | Draft | 2025-01-15 | Architecture |
| docs/CROSS-REFERENCE-INDEX.md | 1.0.0 | Draft | 2025-01-15 | Architecture |
| docs/configuration/FEATURE-FLAGS.md | 1.0.0 | Draft | 2025-01-15 | Config |
| docs/FEATURE-GATES.md | 1.0.0 | Draft | 2025-01-15 | Config |
| docs/configuration/CONFIGURATION-REFERENCE.md | 0.1.0 | Draft | 2026-07-27 | Config |
| docs/EVENT-OWNERSHIP-MATRIX.md | 0.1.0 | Draft | 2026-07-27 | Runtime |
| docs/ai/tools/AI-TOOL-INVOCATION-CONTRACT.md | 0.1.0 | Draft | 2026-07-27 | AI |
| docs/PROMPT-LIFECYCLE.md | 0.1.0 | Draft | 2026-07-27 | AI |
| docs/CONTEXT-PRIORITY-MATRIX.md | 1.0.0 | Draft | 2025-01-15 | AI |
| docs/ai/safety/AI-SAFETY-BOUNDARY.md | 1.0.0 | Draft | 2025-01-15 | AI |
| docs/ai/reference/AI-STATE-MACHINE.md | 1.0.0 | Draft | 2025-01-15 | AI |
| docs/state-machines/ENGINE-STATE-MACHINE.md | 1.0.0 | Draft | 2025-01-15 | Runtime |
| docs/state-machines/EXECUTION-STATE-MACHINE.md | 1.0.0 | Draft | 2025-01-15 | Execution |
| docs/state-machines/WORKER-STATE-MACHINE.md | 1.0.0 | Draft | 2025-01-15 | Runtime |
| docs/state-machines/PLUGIN-STATE-MACHINE.md | 1.0.0 | Draft | 2025-01-15 | Plugin |
| docs/state-machines/SERVICE-STATE-MACHINE.md | 1.0.0 | Draft | 2025-01-15 | Runtime |
| docs/FAILURE-MATRIX.md | 1.0.0 | Draft | 2025-01-15 | Runtime |
| docs/operations/FAILURE-RECOVERY-MATRIX.md | 1.0.0 | Draft | 2025-01-15 | Runtime |
| docs/operations/RECOVERY-PLAYBOOK.md | 1.0.0 | Draft | 2025-01-15 | Runtime |
| docs/performance/THREADING-MODEL.md | 1.0.0 | Draft | 2025-01-15 | Runtime |
| docs/CONCURRENCY-MODEL.md | 1.0.0 | Draft | 2025-01-15 | Runtime |
| docs/ai/memory/MEMORY-LIFECYCLE.md | 1.0.0 | Draft | 2025-01-15 | Runtime |
| docs/performance/RESOURCE-BUDGET-SPECIFICATION.md | 1.0.0 | Draft | 2025-01-15 | Ops |
| docs/performance/CAPACITY-PLANNING.md | 1.0.0 | Draft | 2025-01-15 | Ops |
| docs/TIMING-SPECIFICATION.md | 1.0.0 | Draft | 2025-01-15 | Ops |
| docs/DATA-OWNERSHIP.md | 1.0.0 | Draft | 2025-01-15 | Data |
| docs/DEPENDENCY-AUTHORITY-RULES.md | 1.0.0 | Draft | 2025-01-15 | Architecture |
| docs/security/SECRET-LIFECYCLE.md | 1.0.0 | Draft | 2025-01-15 | Security |
| docs/TRUST-BOUNDARIES.md | 1.0.0 | Draft | 2025-01-15 | Security |
| docs/ERROR-CATALOG.md | 1.0.0 | Draft | 2025-01-15 | Ops |
| docs/reference/ERROR-CODES.md | 1.0.0 | Draft | 2025-01-15 | Ops |

---

## Referenced-By / References-From Mapping

Each document in the repository should be listed once in each direction. The tables below show the dense dependency graph.

### References-From (each doc → docs it references)

| Document | References |
|----------|------------|
| AGENTS.md | docs/ARCHITECTURE.md, docs/ai/runtime/AI-PIPELINE.md, docs/operations/RUNTIME-OPERATIONS.md, docs/TRADING-LIFECYCLE.md, docs/EXECUTION-LIFECYCLE.md, docs/DATABASE-SCHEMA.md, docs/security/SECURITY-CONTRACTS.md |
| ../APEX-ARCHITECTURE.md | docs/DOCUMENTATION-MAP.md, docs/ARCHITECTURE.md, docs/PROJECT-STRUCTURE.md, docs/TRADING-ENGINE.md, docs/EXECUTION-ENGINE.md, docs/ORCHESTRATOR.md, docs/DOMAIN-MODEL.md |
| docs/ARCHITECTURE.md | docs/ORCHESTRATOR.md, docs/TRADING-ENGINE.md, docs/EXECUTION-ENGINE.md, docs/ai/runtime/AI-PIPELINE.md, docs/operations/RUNTIME-OPERATIONS.md, docs/STATE-MANAGEMENT.md, docs/CHAIN-REGISTRY.md, docs/DEX-REGISTRY.md, docs/TOKEN-REGISTRY.md, docs/ORACLE-REGISTRY.md, docs/dashboard/DASHBOARD-LAYOUT.md, docs/dashboard/DASHBOARD-WIDGETS.md, docs/ui/UX-GUIDELINES.md, docs/deployment/VERSIONING.md, docs/DOMAIN-MODEL.md |
| docs/operations/RUNTIME-OPERATIONS.md | docs/ORCHESTRATOR.md, docs/BOOTSTRAP-SEQUENCE.md, docs/SHUTDOWN-LIFECYCLE.md, docs/SERVICE-LIFECYCLE.md, docs/operations/RECOVERY-AND-FAILOVER.md, docs/operations/HEALTHCHECKS.md, docs/WORKER-POOL.md, docs/configuration/CONFIGURATION.md, docs/STATE-MANAGEMENT.md |
| docs/TRADING-ENGINE.md | docs/TRADING-LIFECYCLE.md, docs/EXECUTION-ENGINE.md, docs/ORCHESTRATOR.md, docs/RISK-ENGINE.md |
| docs/EXECUTION-ENGINE.md | docs/TRANSACTION-LIFECYCLE.md, docs/RISK-ENGINE.md, docs/GAS-OPTIMISATION.md, docs/MEV-PROTECTION.md |
| docs/ai/runtime/AI-PIPELINE.md | docs/ai/orchestration/AI-ORCHESTRATION.md, docs/ai/providers/AI-PROVIDER-MANAGER.md, docs/ai/runtime/AI-GATEWAY.md, docs/ai/memory/AI-MEMORY.md, docs/AI-COST-MANAGEMENT.md, docs/ai/runtime/AI-CONTEXT-WINDOW-MANAGEMENT.md, docs/ai/reasoning/AI-REASONING-POLICY.md |
| docs/configuration/CONFIGURATION.md | docs/ai/providers/AI-SETTINGS.md, docs/security/SECURITY.md, docs/operations/RUNTIME-OPERATIONS.md, docs/DATABASE-SCHEMA.md, docs/AI-COST-MANAGEMENT.md, docs/deployment/VERSIONING.md, docs/PLUGIN-SDK.md, docs/operations/HEALTHCHECKS.md |
| docs/security/SECURITY.md | docs/security/SECURITY-CONTRACTS.md, docs/security/PERMISSION-MODEL.md, docs/TRUST-BOUNDARIES.md, docs/security/SECRET-LIFECYCLE.md |
| docs/EVENT-BUS.md | docs/reference/EVENT-CATALOG.md, docs/EVENT-OWNERSHIP-MATRIX.md |
| docs/STATE-MANAGEMENT.md | docs/ORCHESTRATOR.md, docs/TRADING-LIFECYCLE.md, docs/EXECUTION-LIFECYCLE.md, docs/SHUTDOWN-LIFECYCLE.md, docs/SERVICE-LIFECYCLE.md, docs/PLUGIN-LIFECYCLE.md |

### Referenced-By (each doc → docs that reference it)

| Document | Referenced By |
|----------|---------------|
| docs/ARCHITECTURE.md | AGENTS.md, ../APEX-ARCHITECTURE.md, README.md, CLAUDE.md, OPENCODE.md, docs/AGENTS.md |
| docs/ORCHESTRATOR.md | ../APEX-ARCHITECTURE.md, docs/ARCHITECTURE.md, docs/operations/RUNTIME-OPERATIONS.md, docs/TRADING-ENGINE.md, docs/STATE-MANAGEMENT.md |
| docs/ai/runtime/AI-PIPELINE.md | AGENTS.md, docs/ARCHITECTURE.md, README.md, CLAUDE.md, OPENCODE.md, docs/AGENTS.md |
| docs/operations/RUNTIME-OPERATIONS.md | AGENTS.md, README.md, CLAUDE.md, OPENCODE.md, docs/configuration/CONFIGURATION.md |
| docs/TRADING-LIFECYCLE.md | AGENTS.md, README.md, CLAUDE.md, docs/ARCHITECTURE.md, docs/TRADING-ENGINE.md, docs/STATE-MANAGEMENT.md |
| docs/EXECUTION-LIFECYCLE.md | AGENTS.md, README.md, CLAUDE.md, docs/ARCHITECTURE.md, docs/STATE-MANAGEMENT.md |
| docs/DATABASE-SCHEMA.md | AGENTS.md, README.md, CLAUDE.md, OPENCODE.md, docs/configuration/CONFIGURATION.md |
| docs/security/SECURITY-CONTRACTS.md | AGENTS.md, README.md, CLAUDE.md, docs/ARCHITECTURE.md, docs/security/SECURITY.md |
| docs/configuration/CONFIGURATION.md | docs/operations/RUNTIME-OPERATIONS.md |
| docs/reference/EVENT-CATALOG.md | docs/EVENT-BUS.md |
| docs/TRUST-BOUNDARIES.md | docs/security/SECURITY.md |
| docs/security/SECRET-LIFECYCLE.md | docs/security/SECURITY.md |
| docs/security/PERMISSION-MODEL.md | docs/security/SECURITY.md |

---

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.


## Final remaining tranche
- Deepened 76 remaining owner docs.

## End-to-End Ownership Flow
- Documentation ownership flows from domain owner docs to cross-cutting references.
- Use this map to locate the canonical owner before editing any related cross-cutting document.
- Do not create new owner documents for views already owned by existing subsystem docs.

## Authority metadata
- Each listed owner includes its canonical source and scope.
- If a document conflicts with its owner, the owner document wins.

## Additional canonical owners
- State machine contracts: `docs/ai/reference/AI-STATE-MACHINE.md`, `docs/state-machines/ENGINE-STATE-MACHINE.md`, `docs/state-machines/EXECUTION-STATE-MACHINE.md`, `docs/state-machines/WORKER-STATE-MACHINE.md`, `docs/state-machines/PLUGIN-STATE-MACHINE.md`, `docs/state-machines/SERVICE-STATE-MACHINE.md`.
- Reliability contracts: `docs/ERROR-CATALOG.md`, `docs/reference/ERROR-CODES.md`, `docs/FAILURE-MATRIX.md`, `docs/operations/RECOVERY-PLAYBOOK.md`, `docs/operations/FAILURE-RECOVERY-MATRIX.md`.
- Runtime contracts: `docs/performance/THREADING-MODEL.md`, `docs/CONCURRENCY-MODEL.md`, `docs/ai/memory/MEMORY-LIFECYCLE.md`.
- AI contracts: `docs/ai/tools/AI-TOOL-INVOCATION-CONTRACT.md`, `docs/PROMPT-LIFECYCLE.md`, `docs/CONTEXT-PRIORITY-MATRIX.md`, `docs/ai/safety/AI-SAFETY-BOUNDARY.md`.
- Governance contracts: `docs/CANONICAL-SOURCE-RULES.md`, `docs/DOCUMENTATION-LIFECYCLE.md`, `docs/CROSS-REFERENCE-INDEX.md`, `docs/FEATURE-GATES.md`.
- Operational contracts: `docs/configuration/CONFIGURATION-REFERENCE.md`, `docs/TIMING-SPECIFICATION.md`, `docs/performance/RESOURCE-BUDGET-SPECIFICATION.md`, `docs/performance/CAPACITY-PLANNING.md`, `docs/MODULE-OWNERSHIP-MATRIX.md`, `docs/EVENT-OWNERSHIP-MATRIX.md`, `docs/DEPENDENCY-AUTHORITY-RULES.md`, `docs/DATA-OWNERSHIP.md`, `docs/security/SECRET-LIFECYCLE.md`, `docs/TRUST-BOUNDARIES.md`.
