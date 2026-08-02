---
metadata_schema_version: 1.0
document_id: DOC-0441
title: Glossary
plane: Repository Operating Model
domain: Registries
class: Registry
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-repository-docs/registries/GLOSSARY.md
related_concepts:
  - CONCEPT-0441
dependencies:
  - DOC-0006
consumers:
  - DOC-0007
validator_coverage:
  - VAL-002
  - VAL-004
  - VAL-011
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Registries
registry_version: 1.0.0
registry_schema_version: 1.0
registry_model: canonical-terminology
last_regenerated: 2026-08-02
---

# Glossary

Canonical terminology registry. One term, one meaning. Detects synonyms, homonyms, and undefined terms across the repository.

## Registry Metadata

| Field | Value |
| --- | --- |
| Registry version | 1.0.0 |
| Registry schema version | 1.0 |
| Registry model | Canonical terminology with concept mapping |
| Last regenerated | 2026-08-02 |
| Defined terms | 52 |

## Usage

Every term in this glossary has exactly one canonical definition. Documents must use terms consistently with these definitions. VAL-011 (Terminology Validator) enforces this.

## Terms

| Term ID | Term | Canonical Definition | Concept ID | Domain | Related Terms |
| --- | --- | --- | --- | --- | --- |
| TERM-0001 | Orchestrator | The central runtime service that coordinates worker lifecycle, task scheduling, and pipeline execution | CONCEPT-0087 | Runtime | orchestration engine, workflow orchestrator |
| TERM-0002 | Worker | A runtime execution unit that processes tasks within a workspace | CONCEPT-0092 | Runtime | worker pool, worker process |
| TERM-0003 | Workspace | An isolated execution environment for a workflow or task group | CONCEPT-0100 | Runtime | sandbox, execution context |
| TERM-0004 | Pipeline | A sequence of processing stages through which data or tasks flow | CONCEPT-0103 | AI | workflow, execution pipeline |
| TERM-0005 | Plugin | An extension module that integrates with the APEX kernel via a defined contract | CONCEPT-0244 | Plugins | extension, add-on, module |
| TERM-0006 | Provider | An external service or API that delivers data or capabilities to APEX | CONCEPT-0104 | AI | service provider, external service |
| TERM-0007 | Kernel | The core APEX runtime that loads plugins, manages services, and provides foundational APIs | CONCEPT-0065 | Architecture | core, engine, runtime core |
| TERM-0008 | State Machine | A model of states and transitions governing a component's lifecycle | CONCEPT-0379 | State Machines | state model, lifecycle model |
| TERM-0009 | Contract | A formal specification of an interface, API, or protocol that producers and consumers must satisfy | CONCEPT-0251 | Interfaces | agreement, protocol, specification |
| TERM-0010 | Event Bus | A publish-subscribe message system for inter-component communication | CONCEPT-0253 | Interfaces | message bus, pub-sub |
| TERM-0011 | IPC | Inter-Process Communication protocol used between APEX components | CONCEPT-0254 | Interfaces | inter-process communication, RPC |
| TERM-0012 | ADR | Architecture Decision Record — a documented architectural decision with context, rationale, and consequences | CONCEPT-0070 | Architecture | decision record, architectural decision |
| TERM-0013 | Canonical Source | The authoritative document that owns and defines a concept | CONCEPT-0052 | Standards | source of truth, authoritative document |
| TERM-0014 | Registry | A structured catalog of entities (documents, concepts, traces, teams, terms) with stable identity | CONCEPT-0007 | Registries | catalog, index, inventory |
| TERM-0015 | Plane | The top-level documentation boundary — either Repository Operating Model or Product Specification | — | Governance | documentation plane, governance boundary |
| TERM-0016 | Domain | A bounded context within a plane grouping related documents and concepts | — | Governance | subdomain, bounded context |
| TERM-0017 | Repository Operating Model | The plane governing repository structure, agent behavior, validation, and governance | CONCEPT-0003 | Governance | ROM, repository governance |
| TERM-0018 | Product Specification | The plane specifying the APEX application architecture, runtime, AI, execution, market, and operations | — | Architecture | PS, product documentation |
| TERM-0019 | Trading Engine | The core execution component that manages trading strategies, order placement, and execution | CONCEPT-0284 | Execution | trade executor, execution engine |
| TERM-0020 | Risk Engine | The component that evaluates and enforces risk parameters on trading decisions | CONCEPT-0282 | Execution | risk manager, risk assessment |
| TERM-0021 | Policy Engine | The component that evaluates policies and rules governing execution decisions | CONCEPT-0281 | Execution | rule engine, governance engine |
| TERM-0022 | Decision Engine | The component that makes execution decisions based on inputs from risk and policy engines | CONCEPT-0279 | Execution | decision maker, execution decider |
| TERM-0023 | Simulation Engine | The component that simulates trades and strategies against historical or synthetic data | CONCEPT-0283 | Execution | backtest engine, simulation runner |
| TERM-0024 | Routing Engine | The component that determines optimal execution paths across chains and DEXs | CONCEPT-0304 | Market | route optimizer, path finder |
| TERM-0025 | RPC Manager | The component managing blockchain RPC connections, rate limiting, and failover | CONCEPT-0305 | Market | RPC client, connection manager |
| TERM-0026 | Chain | A blockchain network integrated with APEX for trading or data | CONCEPT-0302 | Market | blockchain, network, chain network |
| TERM-0027 | DEX | Decentralized Exchange — an on-chain venue for token swaps | CONCEPT-0303 | Market | decentralized exchange, swap venue |
| TERM-0028 | Arbitrage | Trading strategy exploiting price differences across venues or chains | CONCEPT-0278 | Execution | arb, cross-venue trading |
| TERM-0029 | MEV | Maximal Extractable Value — value extracted from transaction ordering | CONCEPT-0322 | Market | miner extractable value, sandwich attack |
| TERM-0030 | Gas | The computational cost of executing transactions on a blockchain | CONCEPT-0315 | Market | transaction fee, gas price |
| TERM-0031 | Slippage | The difference between expected and actual execution price | CONCEPT-0316 | Market | price impact, execution slippage |
| TERM-0032 | Liquidity | The availability of tokens for trading at a given price level | CONCEPT-0316 | Market | market depth, liquidity pool |
| TERM-0033 | Token | A digital asset on a blockchain, including native coins and contract tokens | CONCEPT-0309 | Market | asset, coin, digital asset |
| TERM-0034 | Wallet | A cryptographic key manager for blockchain accounts and asset custody | CONCEPT-0301 | Execution | key store, account manager |
| TERM-0035 | Portfolio | A collection of assets and positions managed by APEX | CONCEPT-0293 | Execution | holdings, asset collection |
| TERM-0036 | Position | An active or planned holding in a specific asset | CONCEPT-0294 | Execution | holding, exposure |
| TERM-0037 | Order | A request to execute a trade at specified parameters | CONCEPT-0291 | Execution | trade order, execution order |
| TERM-0038 | Strategy | A defined approach to trading with specific entry/exit rules | CONCEPT-0295 | Execution | trading strategy, algorithm |
| TERM-0039 | Opportunity | A detected profitable trading scenario across venues | CONCEPT-0323 | Market | arbitrage opportunity, trading opportunity |
| TERM-0040 | Dashboard | The user interface surface for monitoring and controlling APEX | CONCEPT-0213 | Dashboard | UI, control panel, workspace view |
| TERM-0041 | Widget | A self-contained UI component on the dashboard | CONCEPT-0215 | Dashboard | dashboard component, UI widget |
| TERM-0042 | Bootstrap | The startup sequence that initializes the APEX runtime | CONCEPT-0086 | Runtime | startup, initialization |
| TERM-0043 | Shutdown | The graceful termination sequence for the APEX runtime | CONCEPT-0097 | Runtime | termination, graceful exit |
| TERM-0044 | Service Lifecycle | The lifecycle states of a runtime service from registration to disposal | CONCEPT-0096 | Runtime | service states, service management |
| TERM-0045 | Concurrency | The threading and parallelism model for APEX components | CONCEPT-0095 | Runtime | threading, parallelism, async |
| TERM-0046 | Cache | A temporary data store for performance optimization | CONCEPT-0265 | Data | memory cache, data cache |
| TERM-0047 | Knowledge Graph | A structured representation of documents, concepts, and their relationships for query and reasoning | CONCEPT-0275 | Data | graph, semantic graph, relationship graph |
| TERM-0048 | Context Builder | The component that assembles execution context from knowledge sources | CONCEPT-0270 | Data | context assembler, knowledge assembler |
| TERM-0049 | Decision Ledger | An append-only record of decisions made by the execution system | CONCEPT-0273 | Data | audit log, decision log |
| TERM-0050 | Validator | A governance check that verifies a specific property of the repository | CONCEPT-0066 | Validation | checker, verification, lint rule |
| TERM-0051 | Traceability | The ability to trace relationships between documents, concepts, and implementations | CONCEPT-0008 | Traceability | relationship tracking, dependency tracking |
| TERM-0052 | Agent | An AI assistant operating on the repository under defined contracts and policies | CONCEPT-0001 | Agent System | AI agent, assistant, AI tool |

## Governance

- New terms must be registered before use in canonical specifications.
- Term changes require updating all documents using the term.
- Deprecated terms are retained with a pointer to the replacement term.
- VAL-011 enforces term usage consistency.
