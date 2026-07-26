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
- Documentation map: `docs/DOCUMENTATION-MAP.md`
- Architecture: `docs/ARCHITECTURE.md`
- Root architecture overview: `../APEX-ARCHITECTURE.md`
- Project structure: `docs/PROJECT-STRUCTURE.md`
- Module dependency: `docs/MODULE-DEPENDENCY.md`
- Trading engine: `docs/TRADING-ENGINE.md`
- Execution engine: `docs/EXECUTION-ENGINE.md`
- Strategy engine and strategy catalog: `docs/STRATEGIES.md`
- Risk engine: `docs/RISK-ENGINE.md`
- AI decision pipeline: `docs/AI-PIPELINE.md`
- Cloud AI integration: `docs/CLOUD-AI-INTEGRATION.md`
- AI settings: `docs/AI-SETTINGS.md`
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
- Backtesting methodology: `docs/BACKTESTING.md` (consumes simulation engine)
- Runtime operations: `docs/RUNTIME-OPERATIONS.md`
- Worker architecture: `docs/WORKER-ARCHITECTURE.md`
- Queue management: `docs/QUEUE-MANAGEMENT.md`
- Recovery and failover: `docs/RECOVERY-AND-FAILOVER.md`
- Monitoring and observability: `docs/MONITORING-OBSERVABILITY.md`
- Error handling and logging: `docs/ERROR-HANDLING-LOGGING.md`
- Security: `docs/SECURITY.md`
- Permission model: `docs/PERMISSION-MODEL.md`
- Configuration: `docs/CONFIGURATION.md`
- Database schema: `docs/DATABASE-SCHEMA.md`
- State management: `docs/STATE-MANAGEMENT.md`
- IPC protocol: `docs/IPC-PROTOCOL.md`
- IPC message catalog: `docs/IPC-MESSAGE-CATALOG.md` (catalog under IPC protocol authority)
- API contracts: `docs/API-CONTRACTS.md`
- API reference: `docs/API-REFERENCE.md`
- Event flow: `docs/EVENT-FLOW.md`
- Data flow: `docs/DATA-FLOW.md`
- Performance targets: `docs/PERFORMANCE-TARGETS.md`
- Non-functional requirements: `docs/NON-FUNCTIONAL-REQUIREMENTS.md`
- User workflows: `docs/USER-FLOWS.md`
- User guide: `docs/USER-GUIDE.md`
- Deployment and operations: `docs/DEPLOYMENT.md`
- Windows desktop shell: `docs/WINDOWS-DESKTOP.md`
- UI component spec: `docs/UI-COMPONENT-SPEC.md`
- Designer protocols: `docs/DESIGNER-PROTOCOLS.md`
- Testing guide: `docs/TESTING-GUIDE.md`
- Skills and agents: `docs/SKILLS.md`, `docs/AGENTS.md`
- Implementation roadmap: `docs/IMPLEMENTATION-ROADMAP.md`
- Component diagrams: `docs/COMPONENT-DIAGRAMS.md`

## Navigation-only stubs
These must not claim ownership and should only point to owners:
- `docs/README.md`
- `docs/BUILD-RELEASE-CICD.md`
- `docs/CHANGELOG.md`
- `docs/CODING-STANDARDS.md`
- `docs/CONTRIBUTING.md`
- `docs/DECISION-LOG.md`
- `docs/DESIGN-SYSTEM.md`
- `docs/ENHANCEMENT-ROADMAP.md`
- `docs/FAQ.md`
- `docs/FEATURE-MATRIX.md`
- `docs/FILE-STORAGE.md`
- `docs/GLOSSARY.md`
- `docs/KNOWN-LIMITATIONS.md`
- `docs/PAIR-DISCOVERY.md`
- `docs/PRICE-DISCOVERY.md`
- `docs/TOKEN-DISCOVERY.md`
- `docs/TROUBLESHOOTING.md`

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
- AI capability matrix: `docs/AI-CAPABILITY-MATRIX.md` (Authoritative; owned by AI capability governance; defines supported AI capabilities and measurement.)
- AI memory: `docs/AI-MEMORY.md` (Authoritative; owned by AI memory governance; defines memory storage, retrieval, and context handling.)
- Prompt engineering: `docs/PROMPT-ENGINEERING.md` (Authoritative; owned by AI prompt governance; defines prompt design and construction guidance.)
- AI cost management: `docs/AI-COST-MANAGEMENT.md` (Authoritative; owned by AI cost governance; defines cost tracking, limits, and optimisation.)
- Chain registry: `docs/CHAIN-REGISTRY.md` (Registry; owned by market/data/routing authority; lists supported chains and chain metadata.)
- DEX registry: `docs/DEX-REGISTRY.md` (Registry; owned by market/data/routing authority; lists supported DEXs and DEX metadata.)
- Token registry: `docs/TOKEN-REGISTRY.md` (Registry; owned by market/data/routing authority; lists token definitions and addresses.)
- Oracle registry: `docs/ORACLE-REGISTRY.md` (Registry; owned by market/data/routing authority; lists oracle providers and feeds.)
- Dashboard widgets: `docs/DASHBOARD-WIDGETS.md` (Authoritative; owned by desktop/UI authority; defines the available dashboard widgets.)
- Dashboard layout: `docs/DASHBOARD-LAYOUT.md` (Authoritative; owned by desktop/UI authority; defines layout, grid, and responsive behavior.)
- UX guidelines: `docs/UX-GUIDELINES.md` (Authoritative; owned by desktop/UI authority; defines interaction and presentation standards.)
- Versioning: `docs/VERSIONING.md` (Support; owned by governance/schema/config/API authorities; describes versioning strategy.)


## New autonomous OS contracts
- Runtime orchestrator: `docs/ORCHESTRATOR.md`
- AI orchestration: `docs/AI-ORCHESTRATION.md`
- AI agent specification: `docs/AI-AGENT-SPECIFICATION.md`
- AI consensus: `docs/AI-CONSENSUS.md`
- Plugin SDK: `docs/PLUGIN-SDK.md`
- Plugin marketplace: `docs/PLUGIN-MARKETPLACE.md`
- Domain model: `docs/DOMAIN-MODEL.md`
- Metrics: `docs/METRICS.md`
- Healthchecks: `docs/HEALTHCHECKS.md`


## Product surface contracts
- UI Dashboard: `docs/UI-DASHBOARD-SPEC.md`
- AI Provider Manager: `docs/AI-PROVIDER-MANAGER.md`
- AI Gateway: `docs/AI-GATEWAY.md`
- AI Memory System: `docs/AI-MEMORY-SYSTEM.md`
- Risk Engine: `docs/RISK-ENGINE.md`
- Notification Center: `docs/NOTIFICATION-CENTER.md`
- Chain Command Center: `docs/CHAIN-COMMAND-CENTER.md`
- DEX Intelligence: `docs/DEX-INTELLIGENCE.md`
- Wallet Command Center: `docs/WALLET-COMMAND-CENTER.md`
- Portfolio Analytics: `docs/PORTFOLIO-ANALYTICS.md`
- Enterprise Operations: `docs/ENTERPRISE-OPERATIONS.md`

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
- Dashboard Workspaces: `DASHBOARD-WORKSPACES.md`
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
- Feature Flags: `FEATURE-FLAGS.md`
- Configuration Profiles: `CONFIGURATION-PROFILES.md`
- AI Reasoning Policy: `AI-REASONING-POLICY.md`
- AI Context Window Management: `AI-CONTEXT-WINDOW-MANAGEMENT.md`
- Model Capability Negotiation: `MODEL-CAPABILITY-NEGOTIATION.md`
- Execution Policies: `EXECUTION-POLICIES.md`
- Route Scoring Model: `ROUTE-SCORING-MODEL.md`
- Market Regime Detection: `MARKET-REGIME-DETECTION.md`
- Resource Manager: `RESOURCE-MANAGER.md`
- Task Scheduler: `TASK-SCHEDULER.md`
- Self-Healing: `SELF-HEALING.md`

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
- AI Tools: `AI-TOOLS.md`
- AI Planner: `AI-PLANNER.md`
- AI Reflection: `AI-REFLECTION.md`
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
- Diagnostics: `DIAGNOSTICS.md`
- Bootstrap Sequence: `BOOTSTRAP-SEQUENCE.md`
- Event Catalog: `EVENT-CATALOG.md`


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
- `AI-GATEWAY.md`
- `AI-CONSENSUS.md`
- `AI-MEMORY-SYSTEM.md`
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
| 0 | docs/RUNTIME-OPERATIONS.md | Runtime coordination | Layer anchor |
| 1 | docs/ORCHESTRATOR.md | State-machine orchestration | Defers to RUNTIME-OPERATIONS |
| 2 | docs/BOOTSTRAP-SEQUENCE.md | Startup sequencing | Defers to ORCHESTRATOR |
| 3 | docs/SHUTDOWN-LIFECYCLE.md | Shutdown sequencing | Defers to ORCHESTRATOR |
| 4 | docs/SERVICE-LIFECYCLE.md | Service lifecycle | Defers to RUNTIME-OPERATIONS |
| 5 | docs/WORKER-ARCHITECTURE.md | Worker design | Defers to RUNTIME-OPERATIONS |
| 6 | docs/WORKER-POOL.md | Pool orchestration | Defers to WORKER-ARCHITECTURE |
| 7 | docs/QUEUE-MANAGEMENT.md | Queue management | Defers to WORKER-POOL |
| 8 | docs/RECOVERY-AND-FAILOVER.md | Recovery/failover | Defers to RUNTIME-OPERATIONS |
| 9 | docs/HEALTHCHECKS.md | Health probes | Defers to RUNTIME-OPERATIONS |
| 10 | docs/TASK-SCHEDULER.md | Task scheduling | Defers to RUNTIME-OPERATIONS |
| 11 | docs/SELF-HEALING.md | Auto-recovery | Defers to RUNTIME-OPERATIONS |
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
| 0 | docs/AI-PIPELINE.md | AI decision pipeline | Layer anchor |
| 1 | docs/AI-ORCHESTRATION.md | AI orchestration | Defers to AI-PIPELINE |
| 2 | docs/AI-AGENT-SPECIFICATION.md | Agent specification | Defers to AI-ORCHESTRATION |
| 3 | docs/AI-CONSENSUS.md | Multi-agent consensus | Defers to AI-ORCHESTRATION |
| 4 | docs/AI-PROVIDER-MANAGER.md | Provider management | Defers to AI-PIPELINE |
| 5 | docs/AI-GATEWAY.md | AI gateway | Defers to AI-PROVIDER-MANAGER |
| 6 | docs/AI-SETTINGS.md | AI settings | Defers to AI-PIPELINE |
| 7 | docs/AI-TOOLS.md | AI tool registry | Defers to AI-PIPELINE |
| 8 | docs/AI-PLANNER.md | AI planning | Defers to AI-ORCHESTRATION |
| 9 | docs/AI-REFLECTION.md | AI reflection | Defers to AI-ORCHESTRATION |
| 10 | docs/AI-MEMORY.md | AI memory | Defers to AI-PIPELINE |
| 11 | docs/AI-MEMORY-SYSTEM.md | Memory system contract | Defers to AI-MEMORY |
| 12 | docs/AI-KNOWLEDGE-INDEX.md | Knowledge index | Defers to AI-MEMORY |
| 13 | docs/AI-COST-MANAGEMENT.md | Cost management | Defers to AI-PIPELINE |
| 14 | docs/AI-CAPABILITY-MATRIX.md | Capability matrix | Defers to AI-PROVIDER-MANAGER |
| 15 | docs/AI-CONTEXT-WINDOW-MANAGEMENT.md | Context window mgmt | Defers to AI-PIPELINE |
| 16 | docs/AI-REASONING-POLICY.md | Reasoning policy | Defers to AI-ORCHESTRATION |
| 17 | docs/AI-SAFETY-BOUNDARY.md | Safety boundary | Defers to AI-ORCHESTRATION |
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
| 0 | docs/UI-DASHBOARD-SPEC.md | Dashboard spec | Layer anchor |
| 1 | docs/DASHBOARD-LAYOUT.md | Layout composition | Defers to UI-DASHBOARD-SPEC |
| 2 | docs/DASHBOARD-WIDGETS.md | Widget catalog | Defers to UI-DASHBOARD-SPEC |
| 3 | docs/DASHBOARD-WORKSPACES.md | Workspace persistence | Defers to UI-DASHBOARD-SPEC |
| 4 | docs/UX-GUIDELINES.md | UX/interaction guide | Defers to UI-DASHBOARD-SPEC |
| 5 | docs/UI-COMPONENT-SPEC.md | Component spec | Defers to UI-DASHBOARD-SPEC |
| 6 | docs/DESIGN-SYSTEM.md | Design system | Defers to UX-GUIDELINES |
| 7 | docs/DESIGNER-PROTOCOLS.md | Designer protocols | Defers to UI-DASHBOARD-SPEC |

### Layer 9 — Windows Platform
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | docs/WINDOWS-DESKTOP.md | Windows desktop shell | Layer anchor |
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
| 0 | docs/SECURITY.md | Security | Layer anchor |
| 1 | docs/SECURITY-CONTRACTS.md | Security contracts | Defers to SECURITY |
| 2 | docs/PERMISSION-MODEL.md | Permission model | Defers to SECURITY-CONTRACTS |
| 3 | docs/TRUST-BOUNDARIES.md | Trust boundaries | Defers to SECURITY-CONTRACTS |
| 4 | docs/SECRET-LIFECYCLE.md | Secret lifecycle | Defers to SECURITY |

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
| 3 | docs/APP-BUILDER-DEPLOYMENT-GUIDE.md | Deployment guide | Defers to APP-BUILDER-WORKFLOW |
| 4 | docs/PLUGIN-LIFECYCLE.md | Plugin lifecycle | Defers to PLUGIN-SDK |
| 5 | docs/PLUGIN-MARKETPLACE.md | Plugin marketplace | Defers to PLUGIN-SDK |
| 6 | docs/PLUGIN-SANDBOX-CONTRACT.md | Plugin sandbox | Defers to PLUGIN-SDK |

### Layer 14 — Configuration & Governance
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | docs/CONFIGURATION.md | Configuration | Layer anchor |
| 1 | docs/CONFIGURATION-REFERENCE.md | Key-by-key reference | Defers to CONFIGURATION |
| 2 | docs/CONFIGURATION-PROFILES.md | Profile system | Defers to CONFIGURATION |
| 3 | docs/FEATURE-FLAGS.md | Feature flags | Defers to CONFIGURATION |
| 4 | docs/FEATURE-GATES.md | Feature gates | Defers to FEATURE-FLAGS |
| 5 | docs/CONTRACT-REGISTRY.md | Contract registry | Defers to CONFIGURATION |
| 6 | docs/SYSTEM-CAPABILITY-REGISTRY.md | Capability registry | Defers to CONFIGURATION |

### Layer 15 — Events & Messaging
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | docs/EVENT-BUS.md | Event bus | Layer anchor |
| 1 | docs/EVENT-CATALOG.md | Event catalog | Defers to EVENT-BUS |
| 2 | docs/EVENT-OWNERSHIP-MATRIX.md | Ownership matrix | Defers to EVENT-CATALOG |

### Layer 16 — Monitoring & Observability
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | docs/MONITORING-OBSERVABILITY.md | Monitoring/observability | Layer anchor |
| 1 | docs/METRICS.md | Metrics catalog | Defers to MONITORING-OBSERVABILITY |
| 2 | docs/DIAGNOSTICS.md | Diagnostics | Defers to MONITORING-OBSERVABILITY |
| 3 | docs/ERROR-HANDLING-LOGGING.md | Error handling/logging | Defers to MONITORING-OBSERVABILITY |
| 4 | docs/ERROR-CATALOG.md | Error catalog | Defers to ERROR-HANDLING-LOGGING |
| 5 | docs/ERROR-CODES.md | Error codes | Defers to ERROR-HANDLING-LOGGING |
| 6 | docs/FAILURE-MATRIX.md | Failure matrix | Defers to ERROR-HANDLING-LOGGING |
| 7 | docs/FAILURE-RECOVERY-MATRIX.md | Failure recovery matrix | Defers to FAILURE-MATRIX |
| 8 | docs/RECOVERY-PLAYBOOK.md | Recovery playbook | Defers to FAILURE-RECOVERY-MATRIX |
| 9 | docs/PERFORMANCE-TARGETS.md | Performance targets | Defers to MONITORING-OBSERVABILITY |
| 10 | docs/NON-FUNCTIONAL-REQUIREMENTS.md | NFRs | Defers to MONITORING-OBSERVABILITY |
| 11 | docs/RESOURCE-MANAGER.md | Resource manager | Defers to MONITORING-OBSERVABILITY |

### Layer 17 — Simulation & Testing
| Priority | Document | Role | Authority |
|----------|----------|------|-----------|
| 0 | docs/SIMULATION-ENGINE.md | Simulation framework | Layer anchor |
| 1 | docs/BACKTESTING.md | Backtesting | Defers to SIMULATION-ENGINE |
| 2 | docs/TESTING-GUIDE.md | Testing guide | Defers to SIMULATION-ENGINE |

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
| 0 | docs/CONTRIBUTING.md | Contributing guide | Layer anchor |
| 1 | docs/CODING-STANDARDS.md | Coding standards | Defers to CONTRIBUTING |
| 2 | docs/BUILD-RELEASE-CICD.md | Build/release/CI/CD | Defers to CONTRIBUTING |
| 3 | docs/DEPLOYMENT.md | Deployment guide | Defers to BUILD-RELEASE-CICD |
| 4 | docs/USER-GUIDE.md | User guide | Standalone |
| 5 | docs/USER-FLOWS.md | User workflows | Standalone |
| 6 | docs/FAQ.md | FAQ | Standalone |
| 7 | docs/TROUBLESHOOTING.md | Troubleshooting | Standalone |
| 8 | docs/IMPLEMENTATION-ROADMAP.md | Roadmap | Standalone |
| 9 | docs/ENHANCEMENT-ROADMAP.md | Enhancement roadmap | Standalone |
| 10 | docs/CHANGELOG.md | Changelog | Standalone |
| 11 | docs/KNOWN-LIMITATIONS.md | Known limitations | Standalone |
| 12 | docs/GLOSSARY.md | Glossary | Standalone |
| 13 | docs/FEATURE-MATRIX.md | Feature matrix | Standalone |
| 14 | docs/VERSIONING.md | Versioning | Standalone |

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
| docs/RUNTIME-OPERATIONS.md | 1.0.0 | Canonical | 2025-01-15 | Runtime |
| docs/TRADING-ENGINE.md | 1.0.0 | Review | 2025-01-15 | Trading |
| docs/EXECUTION-ENGINE.md | 1.0.0 | Review | 2025-01-15 | Execution |
| docs/AI-PIPELINE.md | 1.0.0 | Canonical | 2025-01-15 | AI |
| docs/RISK-ENGINE.md | 1.0.0 | Review | 2025-01-15 | Risk |
| docs/SECURITY.md | 1.0.0 | Review | 2025-01-15 | Security |
| docs/CONFIGURATION.md | 1.0.0 | Canonical | 2025-01-15 | Config |
| docs/DATABASE-SCHEMA.md | 1.0.0 | Draft | 2025-01-15 | Data |
| docs/SECURITY-CONTRACTS.md | 1.0.0 | Draft | 2025-01-15 | Security |
| docs/STATE-MANAGEMENT.md | 1.0.0 | Draft | 2025-01-15 | Runtime |
| docs/EVENT-BUS.md | 1.0.0 | Draft | 2025-01-15 | Runtime |
| docs/MONITORING-OBSERVABILITY.md | 1.0.0 | Draft | 2025-01-15 | Ops |
| docs/SIMULATION-ENGINE.md | 1.0.0 | Draft | 2025-01-15 | Trading |
| docs/PLUGIN-SDK.md | 1.0.0 | Draft | 2025-01-15 | Plugin |
| docs/WINDOWS-DESKTOP.md | 1.0.0 | Draft | 2025-01-15 | Windows |
| docs/IPC-PROTOCOL.md | 1.0.0 | Draft | 2025-01-15 | Runtime |
| docs/WALLET-MANAGEMENT.md | 1.0.0 | Draft | 2025-01-15 | Trading |
| docs/API-CONTRACTS.md | 1.0.0 | Draft | 2025-01-15 | Architecture |
| docs/MARKET-DATA.md | 1.0.0 | Draft | 2025-01-15 | Trading |
| docs/UI-DASHBOARD-SPEC.md | 1.0.0 | Draft | 2025-01-15 | UI |
| docs/CONTRIBUTING.md | 1.0.0 | Draft | 2025-01-15 | DevRel |
| docs/DOCUMENTATION-LIFECYCLE.md | 1.0.0 | Draft | 2025-01-15 | Architecture |
| DOCUMENTATION-MAP.md | 1.2.0 | Canonical | 2026-07-27 | Architecture |
| docs/TRACEABILITY-MATRIX.md | 1.0.0 | Canonical | 2025-01-15 | Architecture |
| docs/MODULE-OWNERSHIP-MATRIX.md | 1.0.0 | Draft | 2025-01-15 | Architecture |
| docs/CANONICAL-SOURCE-RULES.md | 1.0.0 | Draft | 2025-01-15 | Architecture |
| docs/CROSS-REFERENCE-INDEX.md | 1.0.0 | Draft | 2025-01-15 | Architecture |
| docs/FEATURE-FLAGS.md | 1.0.0 | Draft | 2025-01-15 | Config |
| docs/FEATURE-GATES.md | 1.0.0 | Draft | 2025-01-15 | Config |
| docs/CONFIGURATION-REFERENCE.md | 0.1.0 | Draft | 2026-07-27 | Config |
| docs/EVENT-OWNERSHIP-MATRIX.md | 0.1.0 | Draft | 2026-07-27 | Runtime |
| docs/AI-TOOL-INVOCATION-CONTRACT.md | 0.1.0 | Draft | 2026-07-27 | AI |
| docs/PROMPT-LIFECYCLE.md | 0.1.0 | Draft | 2026-07-27 | AI |
| docs/CONTEXT-PRIORITY-MATRIX.md | 1.0.0 | Draft | 2025-01-15 | AI |
| docs/AI-SAFETY-BOUNDARY.md | 1.0.0 | Draft | 2025-01-15 | AI |
| docs/AI-STATE-MACHINE.md | 1.0.0 | Draft | 2025-01-15 | AI |
| docs/ENGINE-STATE-MACHINE.md | 1.0.0 | Draft | 2025-01-15 | Runtime |
| docs/EXECUTION-STATE-MACHINE.md | 1.0.0 | Draft | 2025-01-15 | Execution |
| docs/WORKER-STATE-MACHINE.md | 1.0.0 | Draft | 2025-01-15 | Runtime |
| docs/PLUGIN-STATE-MACHINE.md | 1.0.0 | Draft | 2025-01-15 | Plugin |
| docs/SERVICE-STATE-MACHINE.md | 1.0.0 | Draft | 2025-01-15 | Runtime |
| docs/FAILURE-MATRIX.md | 1.0.0 | Draft | 2025-01-15 | Runtime |
| docs/FAILURE-RECOVERY-MATRIX.md | 1.0.0 | Draft | 2025-01-15 | Runtime |
| docs/RECOVERY-PLAYBOOK.md | 1.0.0 | Draft | 2025-01-15 | Runtime |
| docs/THREADING-MODEL.md | 1.0.0 | Draft | 2025-01-15 | Runtime |
| docs/CONCURRENCY-MODEL.md | 1.0.0 | Draft | 2025-01-15 | Runtime |
| docs/MEMORY-LIFECYCLE.md | 1.0.0 | Draft | 2025-01-15 | Runtime |
| docs/RESOURCE-BUDGET-SPECIFICATION.md | 1.0.0 | Draft | 2025-01-15 | Ops |
| docs/CAPACITY-PLANNING.md | 1.0.0 | Draft | 2025-01-15 | Ops |
| docs/TIMING-SPECIFICATION.md | 1.0.0 | Draft | 2025-01-15 | Ops |
| docs/DATA-OWNERSHIP.md | 1.0.0 | Draft | 2025-01-15 | Data |
| docs/DEPENDENCY-AUTHORITY-RULES.md | 1.0.0 | Draft | 2025-01-15 | Architecture |
| docs/SECRET-LIFECYCLE.md | 1.0.0 | Draft | 2025-01-15 | Security |
| docs/TRUST-BOUNDARIES.md | 1.0.0 | Draft | 2025-01-15 | Security |
| docs/ERROR-CATALOG.md | 1.0.0 | Draft | 2025-01-15 | Ops |
| docs/ERROR-CODES.md | 1.0.0 | Draft | 2025-01-15 | Ops |

---

## Referenced-By / References-From Mapping

Each document in the repository should be listed once in each direction. The tables below show the dense dependency graph.

### References-From (each doc → docs it references)

| Document | References |
|----------|------------|
| AGENTS.md | docs/ARCHITECTURE.md, docs/AI-PIPELINE.md, docs/RUNTIME-OPERATIONS.md, docs/TRADING-LIFECYCLE.md, docs/EXECUTION-LIFECYCLE.md, docs/DATABASE-SCHEMA.md, docs/SECURITY-CONTRACTS.md |
| ../APEX-ARCHITECTURE.md | docs/DOCUMENTATION-MAP.md, docs/ARCHITECTURE.md, docs/PROJECT-STRUCTURE.md, docs/TRADING-ENGINE.md, docs/EXECUTION-ENGINE.md, docs/ORCHESTRATOR.md, docs/DOMAIN-MODEL.md |
| docs/ARCHITECTURE.md | docs/ORCHESTRATOR.md, docs/TRADING-ENGINE.md, docs/EXECUTION-ENGINE.md, docs/AI-PIPELINE.md, docs/RUNTIME-OPERATIONS.md, docs/STATE-MANAGEMENT.md, docs/CHAIN-REGISTRY.md, docs/DEX-REGISTRY.md, docs/TOKEN-REGISTRY.md, docs/ORACLE-REGISTRY.md, docs/DASHBOARD-LAYOUT.md, docs/DASHBOARD-WIDGETS.md, docs/UX-GUIDELINES.md, docs/VERSIONING.md, docs/DOMAIN-MODEL.md |
| docs/RUNTIME-OPERATIONS.md | docs/ORCHESTRATOR.md, docs/BOOTSTRAP-SEQUENCE.md, docs/SHUTDOWN-LIFECYCLE.md, docs/SERVICE-LIFECYCLE.md, docs/RECOVERY-AND-FAILOVER.md, docs/HEALTHCHECKS.md, docs/WORKER-POOL.md, docs/CONFIGURATION.md, docs/STATE-MANAGEMENT.md |
| docs/TRADING-ENGINE.md | docs/TRADING-LIFECYCLE.md, docs/EXECUTION-ENGINE.md, docs/ORCHESTRATOR.md, docs/RISK-ENGINE.md |
| docs/EXECUTION-ENGINE.md | docs/TRANSACTION-LIFECYCLE.md, docs/RISK-ENGINE.md, docs/GAS-OPTIMISATION.md, docs/MEV-PROTECTION.md |
| docs/AI-PIPELINE.md | docs/AI-ORCHESTRATION.md, docs/AI-PROVIDER-MANAGER.md, docs/AI-GATEWAY.md, docs/AI-MEMORY.md, docs/AI-COST-MANAGEMENT.md, docs/AI-CONTEXT-WINDOW-MANAGEMENT.md, docs/AI-REASONING-POLICY.md |
| docs/CONFIGURATION.md | docs/AI-SETTINGS.md, docs/SECURITY.md, docs/RUNTIME-OPERATIONS.md, docs/DATABASE-SCHEMA.md, docs/AI-COST-MANAGEMENT.md, docs/VERSIONING.md, docs/PLUGIN-SDK.md, docs/HEALTHCHECKS.md |
| docs/SECURITY.md | docs/SECURITY-CONTRACTS.md, docs/PERMISSION-MODEL.md, docs/TRUST-BOUNDARIES.md, docs/SECRET-LIFECYCLE.md |
| docs/EVENT-BUS.md | docs/EVENT-CATALOG.md, docs/EVENT-OWNERSHIP-MATRIX.md |
| docs/STATE-MANAGEMENT.md | docs/ORCHESTRATOR.md, docs/TRADING-LIFECYCLE.md, docs/EXECUTION-LIFECYCLE.md, docs/SHUTDOWN-LIFECYCLE.md, docs/SERVICE-LIFECYCLE.md, docs/PLUGIN-LIFECYCLE.md |

### Referenced-By (each doc → docs that reference it)

| Document | Referenced By |
|----------|---------------|
| docs/ARCHITECTURE.md | AGENTS.md, ../APEX-ARCHITECTURE.md, README.md, CLAUDE.md, OPENCODE.md, docs/AGENTS.md |
| docs/ORCHESTRATOR.md | ../APEX-ARCHITECTURE.md, docs/ARCHITECTURE.md, docs/RUNTIME-OPERATIONS.md, docs/TRADING-ENGINE.md, docs/STATE-MANAGEMENT.md |
| docs/AI-PIPELINE.md | AGENTS.md, docs/ARCHITECTURE.md, README.md, CLAUDE.md, OPENCODE.md, docs/AGENTS.md |
| docs/RUNTIME-OPERATIONS.md | AGENTS.md, README.md, CLAUDE.md, OPENCODE.md, docs/CONFIGURATION.md |
| docs/TRADING-LIFECYCLE.md | AGENTS.md, README.md, CLAUDE.md, docs/ARCHITECTURE.md, docs/TRADING-ENGINE.md, docs/STATE-MANAGEMENT.md |
| docs/EXECUTION-LIFECYCLE.md | AGENTS.md, README.md, CLAUDE.md, docs/ARCHITECTURE.md, docs/STATE-MANAGEMENT.md |
| docs/DATABASE-SCHEMA.md | AGENTS.md, README.md, CLAUDE.md, OPENCODE.md, docs/CONFIGURATION.md |
| docs/SECURITY-CONTRACTS.md | AGENTS.md, README.md, CLAUDE.md, docs/ARCHITECTURE.md, docs/SECURITY.md |
| docs/CONFIGURATION.md | docs/RUNTIME-OPERATIONS.md |
| docs/EVENT-CATALOG.md | docs/EVENT-BUS.md |
| docs/TRUST-BOUNDARIES.md | docs/SECURITY.md |
| docs/SECRET-LIFECYCLE.md | docs/SECURITY.md |
| docs/PERMISSION-MODEL.md | docs/SECURITY.md |

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
- State machine contracts: `docs/AI-STATE-MACHINE.md`, `docs/ENGINE-STATE-MACHINE.md`, `docs/EXECUTION-STATE-MACHINE.md`, `docs/WORKER-STATE-MACHINE.md`, `docs/PLUGIN-STATE-MACHINE.md`, `docs/SERVICE-STATE-MACHINE.md`.
- Reliability contracts: `docs/ERROR-CATALOG.md`, `docs/ERROR-CODES.md`, `docs/FAILURE-MATRIX.md`, `docs/RECOVERY-PLAYBOOK.md`, `docs/FAILURE-RECOVERY-MATRIX.md`.
- Runtime contracts: `docs/THREADING-MODEL.md`, `docs/CONCURRENCY-MODEL.md`, `docs/MEMORY-LIFECYCLE.md`.
- AI contracts: `docs/AI-TOOL-INVOCATION-CONTRACT.md`, `docs/PROMPT-LIFECYCLE.md`, `docs/CONTEXT-PRIORITY-MATRIX.md`, `docs/AI-SAFETY-BOUNDARY.md`.
- Governance contracts: `docs/CANONICAL-SOURCE-RULES.md`, `docs/DOCUMENTATION-LIFECYCLE.md`, `docs/CROSS-REFERENCE-INDEX.md`, `docs/FEATURE-GATES.md`.
- Operational contracts: `docs/CONFIGURATION-REFERENCE.md`, `docs/TIMING-SPECIFICATION.md`, `docs/RESOURCE-BUDGET-SPECIFICATION.md`, `docs/CAPACITY-PLANNING.md`, `docs/MODULE-OWNERSHIP-MATRIX.md`, `docs/EVENT-OWNERSHIP-MATRIX.md`, `docs/DEPENDENCY-AUTHORITY-RULES.md`, `docs/DATA-OWNERSHIP.md`, `docs/SECRET-LIFECYCLE.md`, `docs/TRUST-BOUNDARIES.md`.
