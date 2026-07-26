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
- Root architecture overview: `APEX-ARCHITECTURE.md`
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
- `APEX-ARCHITECTURE.md`
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
