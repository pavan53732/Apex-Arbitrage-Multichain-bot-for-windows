# SOURC- [6]: ./root-files.txt

[1]: ./PROJECT-TREE-COMPLETE-STUCTURE.md
[2]: ./2025-07-24__Thamudu-Chilling-Chat__2025-07.md
[3]: ./2025-07-24__Thamudu-Chilling-Chat__2025-08.md
[4]: ./2025-07-24__Thamudu-Chilling-Chat__2025-09.md
[5]: ./Bot-Blue-Print.md
[6]: ./root-files.txt

## Root levelILE### deprecated-modules

Deprecated modules are kept for provenance and upgrade safety, mirroring file names, order, and subfolder contents exactly as listed in the canonical tree. Notes align with the blueprint's deprecation guidance for flashloan logic and legacy engines.[3][1]

- [1] PROJECT-TREE-COMPLETE-STUCTURE.md
- [2] 2025-07-24__Thamudu-Chilling-Chat__2025-07.md
- [3] 2025-07-24__Thamudu-Chilling-Chat__2025-08.md
- [4] 2025-07-24__Thamudu-Chilling-Chat__2025-09.md
- [5] Bot-Blue-Print.md
- [6] root-files.txt

## Root level

This r### ### deprecated-modules

Deprecated modules are kept for provenance and upgrade safety, mirroring file names, order, and subfolder contents exactly as listed in the canonical tree. Notes align with the blueprint's deprecation guidance for flashloan logic and legacy engines.[3][1]precated-modules

Deprecated modules are kept for provenance and upgrade safety, mirroring file names, order, and subfolder contents exactly as listed in the canonical tree. Notes align with the blueprint's deprecation guidance for flashloan logic and legacy engines.[3][1]

```textduces the root of the repository exactly as ordered in the canonical tree and attaches a short purpose line to each entry for precise operational usage. File purposes and terms are additional

```text
Apex Arbitrage Multichain bot/
├── .dockerignore                              # Docker build exclusions: node_modules, logs, OS artifacts [attached_file:4]
├── .editorconfig                              # Cross‑editor standards: indent, charset, EOL, trim whitespace [attached_file:4]
├── .env                                       # Runtime variables: RPC URLs, API keys, feature flags [attached_file:4]
├── .env.example                               # Template of required env vars, no secrets [attached_file:4]
├── .eslintrc                                  # JS/TS lint configuration [attached_file:4]
├── .flake8                                    # Python lint/complexity configuration [attached_file:4]
├── .gitignore                                 # Git exclusions: secrets, builds, caches, OS files [attached_file:4]
├── .prettierrc                                # Code formatting rules [attached_file:4]
├── .stylelintrc                               # CSS/SCSS lint rules [attached_file:4]
├── ai-feedback.sqlite                         # SQLite: model feedback and ratings [attached_file:4]
├── ai-training.sqlite                         # SQLite: training/catalog metadata [attached_file:4]
├── analytics.sqlite                           # SQLite: analytics KPIs and aggregates [attached_file:4]
├── api_reference.md                           # Backend API reference and schemas [attached_file:4]
├── audit-trail.sqlite                         # SQLite: immutable audit trail store [attached_file:4]
├── backup-meta.json                           # Backup schedules, retention, encryption info [attached_file:4]
├── Bot Blue Print.md                          # Master system blueprint and dataflows [attached_file:4]
├── chains.json                                # Chain/RPC configuration, chainId keyed [attached_file:4]
├── CHANGELOG.md                               # Versioned changes history [attached_file:4]
├── changes.md                                 # Recent deltas and scaffolding notes [attached_file:4]
├── CODE_OF_CONDUCT.md                         # Community standards and reporting [attached_file:4]
├── compliance.sqlite                          # SQLite: KYC/AML/compliance states [attached_file:4]
├── CONTRIBUTING.md                            # Contribution and PR process [attached_file:4]
├── docker-compose.yml                         # Multi‑service orchestration for dev/stage [attached_file:4]
├── forensics.sqlite                           # SQLite: incidents and forensic artifacts [attached_file:4]
├── hardhat.config.js                          # Ethereum development framework config [attached_file:4]
├── HEALTHCHECK.md                             # Health endpoints and probes [attached_file:4]
├── LEGAL.md                                   # Legal notices and license context [attached_file:4]
├── LICENSE                                    # OSS license file [attached_file:4]
├── logs.sqlite                                # SQLite: application logs sink [attached_file:4]
├── Makefile                                   # Build/test/deploy automation [attached_file:4]
├── manifest.csv                               # Inventory CSV export [attached_file:4]
├── manifest.json                              # Structured inventory export [attached_file:4]
├── manifest.md                                # Human‑readable inventory index [attached_file:4]
├── operator-guide.md                          # Operations handbook [attached_file:4]
├── package.json                               # Node manifest for root tooling [attached_file:4]
├── PROJECT FILES AND FOLDERS DETAILS .MD      # Ultra‑granular catalog (this output) [attached_file:4]
├── PROJECT TREE COMPLETE STUCTURE .md         # Canonical file tree baseline [attached_file:4]
├── README.md                                  # Overview, setup, architecture [attached_file:4]
├── requirements.txt                           # Python dependencies [attached_file:4]
├── roadmap.md                                 # Roadmap and milestones [attached_file:4]
├── root files.txt                             # Root files specification and policies [attached_file:4]
├── SECURITY.md                                # Security policy and procedures [attached_file:4]
├── tsconfig.json                              # TypeScript compiler options [attached_file:4]
└── wall-of-fame.md                            # Contributors and acknowledgments [attached_file:4]
```

### .devcontainer

This subtree defines the reproducible dev environment for IDEs and containers in the exact order shown by the canonical tree. The items map directly to developer onboarding in the blueprint and are required for agent‑safe workspace initialization.[1][5]

```text
.devcontainer/
├── devcontainer.json                          # VS Code container: image, features, extensions [attached_file:4]
├── Dockerfile                                 # Dev image with Node/Python/chain toolchains [attached_file:4]
├── env.example                                # Container‑scoped env placeholders [attached_file:4]
├── extensions.json                            # Required/recommended extensions [attached_file:4]
├── postCreateCommand.sh                       # Post‑create bootstrap tasks [attached_file:4]
├── README.md                                  # Dev container usage notes [attached_file:4]
├── requirements.txt                           # Dev Python requirements [attached_file:4]
└── settings.json                              # Workspace settings in container [attached_file:4]
```

### .github

The GitHub meta and workflow subtree is reproduced exactly and is the CI/CD and community backbone referenced across logs and the blueprint. Workflow files enforce tree validation, lint/test, deployment, monitoring, and synchronization per repository policy.[1]

```text
.github/
├── CODEOWNERS                                 # Code ownership and review routing [attached_file:4]
├── dependabot.yml                             # Dependency update automation [attached_file:4]
├── FUNDING.yml                                # Sponsor configuration [attached_file:4]
├── README.md                                  # Repo‑specific docs [attached_file:4]
├── SECURITY.md                                # Security disclosure policy [attached_file:4]
├── support.md                                 # Support channels and triage [attached_file:4]
├── ISSUE_TEMPLATE/
│   ├── bug_report.md                          # Bug report template [attached_file:4]
│   ├── feature_request.md                     # Feature request template [attached_file:4]
│   ├── general_question.md                    # General inquiry template [attached_file:4]
│   └── README.md                              # Templates guide [attached_file:4]
├── PULL_REQUEST_TEMPLATE/
│   ├── pull_request.md                        # PR checklist and validation [attached_file:4]
│   └── README.md                              # PR guidelines [attached_file:4]
└── workflows/
    ├── check-project-tree.yml                 # Tree vs manifest verification [attached_file:4]
    ├── ci.yml                                 # Lint/test/build/audit [attached_file:4]
    ├── deploy.yml                             # Staging/production deploy and rollback [attached_file:4]
    ├── lint.yml                               # Code formatting and lint gates [attached_file:4]
    ├── monitor.yml                            # Health and uptime monitoring [attached_file:4]
    ├── README.md                              # Workflow documentation [attached_file:4]
    ├── sync-fork.yml                          # Upstream synchronization [attached_file:4]
    └── test.yml                               # Unit/integration/E2E tests [attached_file:4]
```

### .husky

These hooks enforce commit hygiene, staged linting, and pre‑push gates; names and order match the canonical tree exactly. The presence and configuration are also referenced in the logs for conventional commit enforcement and CI signal quality.[2][1]

```text
.husky/
├── commit-msg                                 # Conventional commit validation [attached_file:4]
├── commitlint.config.js                       # Commit types/scopes rules [attached_file:4]
├── lint-staged.config.js                      # Staged lint/format runner [attached_file:4]
├── pre-commit                                 # Lint/test/security checks [attached_file:4]
├── pre-push                                   # Build/test and branch policies [attached_file:4]
└── README.md                                  # Hook setup and troubleshooting [attached_file:4]
```

### .vscode

Workspace configuration is retained in the exact order and used for consistent debugging and tasks across contributors and agents. These files are also cited in root files.txt for IDE policy conformance.[6][1]

```text
.vscode/
├── extensions.json                            # Workspace extension hints [attached_file:4]
├── launch.json                                # Debug profiles (Node, Python, browser) [attached_file:4]
├── README.md                                  # Workspace usage and tips [attached_file:4]
├── settings.json                              # Editor/formatter settings [attached_file:4]
└── tasks.json                                 # Build/test/lint tasks [attached_file:4]
```

### ai-modules

The ai-modules root and subtrees below are reproduced in full as present in the canonical tree, with consistent descriptions matching the blueprint and logs. This section is foundational for model orchestration, routing, scoring, features, training, and simulations.[5][1]

```text
ai-modules/
├── ai-engine.js                               # AI orchestration: model selection, inference, aggregation [attached_file:4]
├── aiConfig.json                              # AI configuration: routing, thresholds, features [attached_file:4]
├── decisionMaker.js                           # Ensemble/council voting and safeguards [attached_file:4]
├── modelRouter.js                             # Dynamic routing, fallback, A/B [attached_file:4]
├── patternLearner.js                          # Pattern recognition for setups and risk [attached_file:4]
├── README.md                                  # AIML overview and usage [attached_file:4]
├── scoreArbOpportunity.js                     # Arbitrage opportunity scoring [attached_file:4]
├── tokenReputationIndex.py                    # Token reliability/volatility index [attached_file:4]
└── tradeOutcomeLogger.js                      # Outcome logging for training and drift checks [attached_file:4]
```

#### ai-modules/datasets

Datasets are used for features, labels, and historical trade outcomes as documented in logs and canonical listings. Filenames and roles are consistent with the training and evaluation pipeline in the blueprint.[5][1]

```text
ai-modules/datasets/
├── README.md                                  # Dataset guide and ethics [attached_file:4]
├── ai-decision-corpus.json                    # Decision/XAI corpus [attached_file:4]
├── features.csv                               # Engineered features matrix [attached_file:4]
├── profitLabels.json                          # Labels for profit/risk tasks [attached_file:4]
└── trade-history.csv                          # Annotated trades for training [attached_file:4]
```

#### ai-modules/features

Feature extractors assemble model‑ready vectors from real‑time signals per canonical entries and logs. These files align to the modelRouter and scoring modules referenced above.[2][1]

```text
ai-modules/features/
├── README.md                                  # Feature schema and versioning [attached_file:4]
├── featureExtractor.js                        # Feature orchestration [attached_file:4]
├── gasFeeSpikeFeature.js                      # Gas spike detector [attached_file:4]
├── latencyProfileFeature.js                   # Network latency profiler [attached_file:4]
└── priceDeltaFeature.js                       # Price delta/divergence indicator [attached_file:4]
```

#### ai-modules/integration

Integration helpers bridge AI logic into the broader backend and UI surfaces in the exact files listed by the tree. This is mirrored in the July/August logs for runtime wiring notes and webhook behavior.[2][1]

```text
ai-modules/integration/
├── aiBridgeAdapter.js                         # Input schema mapping/backpressure [attached_file:4]
├── aiHooks.js                                 # Runtime hooks and streaming updates [attached_file:4]
├── aiLogFormatter.js                          # Normalize logs for retraining [attached_file:4]
├── aiWebhookReceiver.js                       # External webhooks and auth/limits [attached_file:4]
└── README.md                                  # Integration guide and tests [attached_file:4]
```

#### ai-modules/models

Model weights and outputs follow the exact structure in the canonical tree, with README files guiding promotion and rollback. Formats span PyTorch, ONNX, JSON configs, and scikit‑learn pipelines as listed.[1]

```text
ai-modules/models/
├── README.md                                  # Models catalog and lifecycle [attached_file:4]
├── modelWeights/
│   ├── decisionNet-v1.pt                      # PyTorch checkpoint [attached_file:4]
│   ├── patternNet-v2.onnx                     # ONNX model [attached_file:4]
│   ├── README.md                              # Weights policy and hashes [attached_file:4]
│   ├── scorerModel.json                       # Scorer config [attached_file:4]
│   └── volatilityClassifier.pkl               # scikit‑learn pipeline [attached_file:4]
└── trainingOutputs/
    ├── accuracy-report.txt                    # Metrics report [attached_file:4]
    ├── README.md                              # Outputs guide [attached_file:4]
    ├── token-risk-score-histogram.png         # Risk distribution plot [attached_file:4]
    └── trade-learning-curve.png               # Learning curve [attached_file:4]
```

#### ai-modules/notebooks

Notebook names and roles are listed as in the tree and used for analysis per blueprint guidance. These inform risk and latency policies reflected in DecisionMaker and Router modules.[5][1]

```text
ai-modules/notebooks/
├── README.md                                  # Repro and env setup [attached_file:4]
├── latency-vs-profit.ipynb                    # Latency impact on profitability [attached_file:4]
├── model-training-logistics.ipynb             # Preprocess, tuning, evaluation [attached_file:4]
├── risk-surface-analysis.ipynb                # Multi‑dimensional risk surfaces [attached_file:4]
└── trade-pattern-exploration.ipynb            # Pattern discovery/anomalies [attached_file:4]
```

#### ai-modules/simulation

Simulation tools reflect the exact files in the canonical tree and are cited in logs for validation workflows. They are also referenced in blueprint procedures for acceptance gates before model promotion.[1][5]

```text
ai-modules/simulation/
├── README.md                                  # Simulation modes and acceptance [attached_file:4]
├── aiReplayValidator.js                       # Counterfactual replay validator [attached_file:4]
├── analyzeAIErrorCases.js                     # Failure mode analysis [attached_file:4]
└── simulateAITrade.js                         # Scenario simulation and metrics [attached_file:4]
```

#### ai-modules/tests

Test files match the canonical list and enforce stability against golden datasets in CI as documented in workflows and logs. These are required by the check‑project‑tree and CI gates described above.[1]

```text
ai-modules/tests/
├── README.md                                  # Test plan and coverage gates [attached_file:4]
├── testFeatureExtractor.test.js               # Feature correctness/consistency [attached_file:4]
├── testModelRouter.test.js                    # Routing behaviors [attached_file:4]
├── testPatternLearner.test.js                 # Pattern accuracy/drift tests [attached_file:4]
└── testScoreArbOpportunity.test.js            # Scoring regression tests [attached_file:4]
```

#### ai-modules/train

Training assets are listed exactly as in the canonical tree and reflected in logs for SOPs, configs, and scripts. These files link to datasets and model outputs above for full promotion pipelines.[2][1]

```text
ai-modules/train/
├── README.md                                  # Training SOP and promotion rules [attached_file:4]
├── config.yaml                                # Paths, hyperparameters, splits [attached_file:4]
├── evaluate.py                                # Post‑train metrics and export [attached_file:4]
├── preprocess.py                              # Cleaning and feature assembly [attached_file:4]
├── train.py                                   # Main trainer [attached_file:4]
└── trainFineTune.py                           # Incremental fine‑tuning [attached_file:4]
```

### archive

The archive root contains the top-level index and retention/recovery guidance used by audits, rollbacks, and provenance workflows, matching names and order from the canonical tree. Each entry exists verbatim in the project tree and is included without additions or reordering.[1]

```text
archive/
├── README.md                                 # Archive overview: organization, retention, access procedures
└── README_ARCHIVE_GUIDE.md                   # Filing system, cleanup procedures, recovery methods
```

### archived-tests

This folder preserves legacy tests and their logs for historical benchmarks and diffing, reflecting the exact files and structure provided in the canonical tree export. It is referenced during migrations to validate behavior changes and regression impacts using historical samples.[2][1]

```text
archive/archived-tests/
├── aiScoring-legacy.test.js                  # Legacy AI scoring tests: deprecated algorithms, historical benchmarks
├── README.md                                 # Archived tests: organization, significance, migration notes
├── testLegacyFlashloan.js                    # Legacy flashloan tests: old interfaces and deprecated protocols
├── tradeSamples-v1.json                      # Historical trade samples: market data and execution logs
└── archived-output-logs/
    ├── ai-trace-legacy.log                   # Legacy AI decision traces and outputs
    ├── README.md                             # Log format, analysis tools, historical context
    ├── trade-diffs-old.json                  # Expected vs actual trade diffs for regression analysis
    └── tx-failure-snapshots.log              # Transaction failure snapshots and error stacks
```


### deprecated-modules

Deprecated modules are kept for provenance and upgrade safety, mirroring file names, order, and subfolder contents exactly as listed in the canonical tree. Notes align with the blueprint’s deprecation guidance for flashloan logic and legacy engines.[3][1]

```text
archive/deprecated-modules/
├── flashloan-logic-legacy.sol                # Legacy flashloan contract with known security issues
├── legacy-arbEngine-v1.js                    # Deprecated arbitrage engine superseded by current implementation
├── old-ai-model.py                           # Outdated AI model architecture replaced by newer council approach
├── README.md                                 # Deprecation reasons and migration paths
└── ui-backup-2023-12/
    ├── app.js                                # Legacy React app entry point
    ├── index.html                            # Old UI shell for reference
    ├── main.css                              # Historical styling and tokens
    └── README.md                             # Context and migration notes for the archived UI
```

### docs

The archived documentation subtree captures API diffs, compliance audits, deprecation notices, incidents, migrations, ADRs, onboarding, and playbooks, with exact filenames and hierarchy from the canonical tree. These documents are used for audit trails, upgrade planning, and security and policy references.[2][1]

```text
archive/docs/
├── README.md                                 # Archive docs index and navigation
├── api-diffs/
│   ├── contracts-diff-v1-v2.md               # Contract API changes and migration guidance
│   └── README.md                             # Versioning strategy and compatibility matrix
├── compliance-logs/
│   ├── audit-2023Q2.md                       # Q2 2023 compliance audit report
│   ├── audit-2024-GDPR-report.md             # GDPR privacy and data handling audit
│   └── README.md                             # Compliance history index and context
├── deprecation-notices/
│   ├── deprecated-flashloan-2023.md          # Flashloan deprecation timeline and alternatives
│   └── README.md                             # Deprecation policy and support timeline
├── incident-reports/
│   ├── incident-2023-07-22.md                # Postmortem: root cause, impact, resolution
│   └── README.md                             # Incident report format and follow‑ups
├── migration-notes/
│   ├── migration-v2.0.md                     # Breaking changes, upgrade path, testing
│   └── README.md                             # Migration procedures and rollback
├── old-adrs/
│   ├── adr-001-example.md                    # Historical decision record and context
│   ├── adr-002-example.md                    # Technical choice, trade‑offs, consequences
│   └── README.md                             # ADR index and status notes
├── onboarding/
│   ├── onboarding-v1.md                      # Legacy onboarding workflow and tools
│   └── README.md                             # Onboarding archive index and usage
└── playbooks/
    ├── failover-v1.sh                        # Legacy failover procedure script
    ├── README.md                             # Playbooks archive overview
    └── runbook-legacy.md                     # Legacy ops runbook for historical procedures
```

### migration-logs

Migration logs and schema references here support auditability and reproducibility of DB evolution, with file names and order taken directly from the canonical tree. These artifacts are consulted for failure analysis, rollbacks, and change tracking across releases.[1][2]

```text
archive/migration-logs/
├── db-schema-v1.sql                          # Baseline schema: tables, indexes, constraints
├── migration-2024-12-20.log                  # 2024-12 migration: changes, issues, timings
├── migration-2025-06-01.log                  # 2025-06 migration: major version upgrade notes
├── migration-2025-07-15.log                  # 2025-07 migration: performance/index optimizations
├── migration-failures.log                    # Failure cases and rollback entries
├── migration-summary.csv                     # Summaries of changes and success rates
└── README.md                                 # Log format and troubleshooting procedures
```

### old-configs

Retired configuration files are preserved here for compatibility and security comparisons, exactly as listed in the canonical project tree. These are used during adapter upgrades and compliance reviews to validate drift and scope of changes.[3][1]

```text
archive/old-configs/
├── chains-v1.json                            # Legacy chain RPCs and gas configs
├── dexes-legacy.json                         # Deprecated DEX adapter configuration
├── flashloanParams-v1.json                   # Early flashloan fee structures and providers
├── README.md                                 # Legacy config index and migration notes
├── risk-profiles-archive.json                # Archived risk profiles and calibrations
├── strategy-params-legacy.yaml               # Deprecated strategy parameters
└── tokens-old.json                           # Delisted/changed asset addresses and metadata
```

### previous-releases

Historical release packages and integrity files provide provenance, reproducibility, and rollback pathways, listed precisely per the canonical tree. These artifacts are referenced by deployment and audit processes to ensure verifiable supply chains.[2][1]

```text
archive/previous-releases/
├── README.md                                 # Previous releases index and guidance
├── release-notes-v1.md                       # v1 features, fixes, known issues
├── release-v1.0.zip                          # v1.0 package: sources/binaries/docs
├── release-v1.1-beta.zip                     # v1.1 beta with experimental features
├── release-v1.2-integrity.sha256             # Integrity hashes for v1.2 artifacts
└── release-v1.2.zip                          # v1.2 stable release package with patches
### backend
The backend root contains config, build, orchestration, and developer-operation docs that govern the entire backend stack exactly as enumerated in the canonical listing.[1]

```text
backend/
├── .eslintrc                                  # JS/TS lint rules for backend code [attached_file:9]
├── .flake8                                    # Python lint rules for backend scripts/tools [attached_file:9]
├── .gitignore                                 # Ignore patterns for artifacts/secrets/logs [attached_file:9]
├── .prettierrc                                # Formatter configuration for consistent diffs [attached_file:9]
├── .stylelintrc                               # Style lint for CSS/SCSS fragments [attached_file:9]
├── api_reference.md                           # Canonical backend API reference [attached_file:9]
├── CHANGELOG.md                               # Chronological backend changes [attached_file:9]
├── CONTRIBUTING.md                            # Contributor setup and PR policy [attached_file:9]
├── docker-compose.yml                         # Local/stage orchestration (APIs/DBs/monitors) [attached_file:9]
├── Dockerfile                                 # Hardened backend image build [attached_file:9]
├── jest.config.js                             # Test runner and coverage config [attached_file:9]
├── LICENSE                                    # Backend code license [attached_file:9]
├── Makefile                                   # One‑shot tasks used by CI/operators [attached_file:9]
├── operator-guide.md                          # Runbooks for ops: deploy/rollback/incident [attached_file:9]
├── package.json                               # Node deps and scripts for backend [attached_file:9]
├── pyproject.toml                             # Python toolchain configuration [attached_file:9]
├── README.md                                  # Backend overview and setup [attached_file:9]
├── requirements.txt                           # Python dependencies for tasks [attached_file:9]
├── SECURITY.md                                # Vulnerability disclosure and hardening [attached_file:9]
├── tree_structure.txt                         # Snapshot of backend tree for audits [attached_file:9]
└── tsconfig.json                              # TypeScript compiler settings [attached_file:9]
```

### backend/backup

The backup subtree holds the disaster‑recovery index and procedures that audits reference during drills and incident reviews.[1]

```text
backend/backup/
└── README.md                                  # Backup/restore SLOs, integrity checks, DR procedures [attached_file:9]
```

### backend/contracts

The contracts subtree lists core on‑chain modules and their documentation, interfaces, scripts, sources, and tests in the exact order shown by the canonical tree.[1]

```text
backend/contracts/
├── AlphaNFT.sol                               # Access/reputation NFT [attached_file:9]
├── ArbitrageExecutor.sol                      # Atomic path and profit routing [attached_file:9]
├── DigitalTwinBridge.sol                      # Twin state synchronization [attached_file:9]
├── DisputeResolution.sol                      # Arbitration lifecycle [attached_file:9]
├── Events.sol                                 # Canonical events for indexers [attached_file:9]
├── FlashLoanArbitrage.sol                     # Flashloan arbitrage core [attached_file:9]
├── GovernanceModule.sol                       # On‑chain governance primitives [attached_file:9]
├── InsurancePool.sol                          # Premiums, coverage, payouts [attached_file:9]
├── IntentSolver.sol                           # Intent routing and solver market [attached_file:9]
├── OperatorNFT.sol                            # Operator credential/delegation NFT [attached_file:9]
├── QuantumReadyModule.sol                     # PQ‑readiness scaffolding [attached_file:9]
├── README.md                                  # Contracts index and conventions [attached_file:9]
├── ReputationOracle.sol                       # Reputation scoring/slashing [attached_file:9]
├── SocialImpactDistributor.sol                # ESG allocation logic [attached_file:9]
└── UpgradableProxy.sol                        # Safe upgrade proxy pattern [attached_file:9]
```

### backend/contracts/docs

Contract docs support audits, proofs, and ops, mirroring the filenames and order in the export exactly.[1]

```text
backend/contracts/docs/
├── ai-agent-integration.md                    # Agent/oracle integration patterns [attached_file:9]
├── audits.md                                  # Security findings and remediations [attached_file:9]
├── contract-architecture.md                   # Module diagrams and interactions [attached_file:9]
├── coverage-report.md                         # Coverage summaries and gaps [attached_file:9]
├── cross-chain-bridges.md                     # Supported bridges and risks [attached_file:9]
├── digital-twin-architecture.md               # Twin design/validation [attached_file:9]
├── events-reference.md                        # Event schemas and consumers [attached_file:9]
├── formal-verification.md                     # Specs and proof scope [attached_file:9]
├── governance-design.md                       # Governance mechanism design [attached_file:9]
├── insurance-mechanisms.md                    # Risk/claims mechanisms [attached_file:9]
├── interface-specs.md                         # ABIs and compat notes [attached_file:9]
├── plugin-architecture.md                    # Extension lifecycle and trust [attached_file:9]
├── quantum-resilience.md                      # PQ threat/mitigation roadmap [attached_file:9]
├── README.md                                  # Docs index and workflow [attached_file:9]
├── test-playbooks.md                          # Unit/fuzz/integration plans [attached_file:9]
└── upgradeability.md                          # Proxy/storage layout/rollback [attached_file:9]
```

### backend/contracts/interfaces

Interfaces ensure adapter and module interoperability; ordering below matches the canonical source listing.[1]

```text
backend/contracts/interfaces/
├── IAIAgentInterface.sol                      # Agent callback interface [attached_file:9]
├── IAIOracle.sol                              # AI oracle feed interface [attached_file:9]
├── IAlphaNFT.sol                              # AlphaNFT interface [attached_file:9]
├── IAlphaSignal.sol                           # Alpha signal provider interface [attached_file:9]
├── IBridge.sol                                # Bridge integration interface [attached_file:9]
├── ICompliance.sol                            # Compliance gating interface [attached_file:9]
├── IDEXAdapter.sol                            # DEX adapter interface [attached_file:9]
├── IDigitalTwinBridge.sol                     # Twin bridge interface [attached_file:9]
├── IERC20.sol                                 # ERC‑20 interface [attached_file:9]
├── IFlashLoanProvider.sol                     # Flashloan provider interface [attached_file:9]
├── IForkSimulation.sol                        # Fork/simulation interface [attached_file:9]
├── IGovernance.sol                            # Governance actions interface [attached_file:9]
├── IInsurance.sol                             # Insurance pool interface [attached_file:9]
├── IIntentSolver.sol                          # Intent solver interface [attached_file:9]
├── IOperatorNFT.sol                           # Operator NFT interface [attached_file:9]
├── IOracle.sol                                # Oracle interface [attached_file:9]
├── IPluginMarket.sol                          # Plugin marketplace interface [attached_file:9]
├── IReputationOracle.sol                      # Reputation oracle interface [attached_file:9]
├── IRewardDistributor.sol                     # Reward distribution interface [attached_file:9]
├── ISocialImpact.sol                          # Social impact interface [attached_file:9]
├── IUpgradeBeacon.sol                         # Upgrade beacon interface [attached_file:9]
├── IZKVerifier.sol                            # ZK verifier interface [attached_file:9]
└── README.md                                  # Interfaces index and notes [attached_file:9]
```

### backend/contracts/scripts

Deployment and ops scripts appear exactly as exported, supporting verification, upgrades, snapshots, and forks.[1]

```text
backend/contracts/scripts/
├── alpha-nft-mint.js                          # Mint helper for AlphaNFT [attached_file:9]
├── deploy.js                                  # Contract deployment orchestrator [attached_file:9]
├── digital-twin-runner.js                     # Twin sync/validation runner [attached_file:9]
├── fork-test.js                               # Mainnet-fork quick tests [attached_file:9]
├── governance-init.js                         # Governance bootstrap tasks [attached_file:9]
├── README.md                                  # Scripts usage/safety notes [attached_file:9]
├── simulate-arb.js                            # Arbitrage simulation runner [attached_file:9]
├── snapshot.js                                # Chain snapshot helper [attached_file:9]
├── upgrade.js                                 # Proxy upgrade flow [attached_file:9]
└── verify.js                                  # Explorer verification script [attached_file:9]
```

### backend/contracts/src/executors

This folder contains the on-chain executors for alpha-gated actions, arbitrage routes, batching, twin checks, governance applications, insurance operations, liquidation flows, plugin actions, and a sandbox executor, listed in canonical order.[1]

```text
backend/contracts/src/executors/
├── alpha-signal-executor.sol                  # Executes alpha‑gated operations under defined policies [attached_file:9]
├── arb-executor.sol                           # Core arbitrage route execution with atomicity guarantees [attached_file:9]
├── batch-executor.sol                         # Batching for multi‑step sequences to optimize gas/atomic flows [attached_file:9]
├── digital-twin-executor.sol                  # Twin‑mediated validation and guarded execution hooks [attached_file:9]
├── governance-executor.sol                    # Applies passed governance proposals to enact changes [attached_file:9]
├── insurance-executor.sol                     # Executes insurance operations (premium, claims, payouts) [attached_file:9]
├── liquidation-executor.sol                   # Liquidation routines for risk containment and recovery [attached_file:9]
├── plugin-executor.sol                        # Safe harness for plugin‑driven on‑chain actions [attached_file:9]
├── README.md                                  # Executors overview, invariants, and integration notes [attached_file:9]
└── sandbox-executor.sol                       # Restricted executor for fork/sandbox evaluation paths [attached_file:9]
```

### backend/contracts/src/governance

This subtree implements governance primitives including disputes, fork voting, token mechanics, proposal registry, timelocks, and vote tallying, mirroring canonical names and order.[1]

```text
backend/contracts/src/governance/
├── dispute-manager.sol                        # Dispute intake, evidence handling, and resolution lifecycle [attached_file:9]
├── fork-voting.sol                            # Governance voting via fork‑based consensus model [attached_file:9]
├── governance-token.sol                       # Token used for governance power and weighting [attached_file:9]
├── proposal-registry.sol                      # Index and state machine for governance proposals [attached_file:9]
├── README.md                                  # Governance module notes and expected invariants [attached_file:9]
├── timelock.sol                               # Enforced delay for secure execution of passed proposals [attached_file:9]
└── voting.sol                                 # Vote casting, counting, and quorum checks [attached_file:9]
```

### backend/contracts/src/interfaces

This folder holds internal interfaces used within the src layer to formalize module boundaries and enable safe upgrades, listed exactly as exported.[1]

```text
backend/contracts/src/interfaces/
├── IAIAgentInterface.sol                      # Agent callback interface for decisions and status [attached_file:9]
├── IAlphaFeed.sol                             # Alpha feed interface for signal distribution [attached_file:9]
├── IArbScore.sol                              # Interface for arbitrage scoring and ranking [attached_file:9]
├── IAudit.sol                                 # Audit logging/reporting interface [attached_file:9]
├── IExecutionModule.sol                       # Interface for execution‑capable modules [attached_file:9]
├── IIncident.sol                              # Incident reporting interface for on‑chain signals [attached_file:9]
├── IRewardVault.sol                           # Reward custody and distribution interface [attached_file:9]
├── IUpgradeBeacon.sol                         # Upgrade beacon interface for proxy patterns [attached_file:9]
└── README.md                                  # Interfaces overview and usage notes [attached_file:9]
```

### backend/contracts/src/onchain-governance

This subtree defines the on-chain governance composition and consensus mechanisms, including council, DAO organization, fork‑consensus, proposal factory, and upgrade voting, in canonical order.[1]

```text
backend/contracts/src/onchain-governance/
├── council.sol                                # Council composition and coordination logic [attached_file:9]
├── dao.sol                                    # DAO rules, roles, and proposal lifecycle enforcement [attached_file:9]
├── fork-consensus.sol                         # Fork‑based consensus coordination primitives [attached_file:9]
├── proposal-factory.sol                       # Factory for standardized proposal creation [attached_file:9]
├── README.md                                  # On‑chain governance overview and invariants [attached_file:9]
└── upgrade-voting.sol                         # Voting flow specific to upgrade decisions [attached_file:9]
```

### backend/contracts/src/proofs

This folder contains proof contracts for AI audits, general audits, fraud, quantum resilience, replay protection, and ZK proofs/utilities, matching the canonical names and order.[1]

```text
backend/contracts/src/proofs/
├── ai-audit.sol                               # Assertions and attestations for AI‑assisted decisions [attached_file:9]
├── audit-proof.sol                            # General audit proof scaffolding and verification [attached_file:9]
├── fraud-proof.sol                            # Fraud proof submission and validation mechanics [attached_file:9]
├── quantum-proof.sol                          # Quantum‑resilience proof structures [attached_file:9]
├── README.md                                  # Proofs module documentation and guarantees [attached_file:9]
├── replay-attack-guard.sol                    # Replay attack detection and rejection guard [attached_file:9]
├── zk-proof.sol                               # ZK proof harness coordinating verifiers [attached_file:9]
└── zk-snark-utils.sol                         # Utility library for SNARK operations [attached_file:9]
```

### backend/contracts/src/registries

This subtree implements registries for core addresses, assets, modules, NFTs, operators, and plugins, provided in exact canonical order.[1]

```text
backend/contracts/src/registries/
├── address-registry.sol                       # Registry of critical on‑chain addresses [attached_file:9]
├── asset-registry.sol                         # Registry of supported assets and metadata [attached_file:9]
├── module-registry.sol                        # Registry of enabled modules and versions [attached_file:9]
├── nft-registry.sol                           # Registry of NFTs under protocol governance [attached_file:9]
├── operator-registry.sol                      # Registry of authorized operators and roles [attached_file:9]
├── plugin-registry.sol                        # Registry of available plugins with lifecycle states [attached_file:9]
└── README.md                                  # Registries overview and access controls [attached_file:9]
```

### backend/contracts/src/test

The test suite under src validates core contract behaviors across NFTs, executors, twin bridge, dispute flow, arbitrage, governance, insurance, intents, reputation, upgrade safety, and ZK verification, matching the canonical names and order.[1]

```text
backend/contracts/src/test/
├── alpha-nft.test.js                          # Validates AlphaNFT mint/burn/transfer rules, role gating, and event emission paths for operator credentialing [attached_file:9]
├── batch-executor.test.js                     # Asserts atomic multi-step execution, revert-on-failure behavior, and expected gas/ordering semantics for batched ops [attached_file:9]
├── digital-twin-bridge.test.js                # Checks twin sync/validation flows, event schemas, and rejection on state divergence to preserve on-chain/twin parity [attached_file:9]
├── dispute-resolution.test.js                 # Covers evidence intake, deadlines, arbitration outcomes, and state transitions across dispute lifecycles [attached_file:9]
├── flashloan-arbitrage.test.js                # Ensures flashloan paths settle atomically with enforced slippage and profit routing invariants under adversarial cases [attached_file:9]
├── governance-module.test.js                  # Exercises proposal creation, voting, quorum, timelock delays, and secure execution sequencing per governance rules [attached_file:9]
├── insurance-pool.test.js                     # Verifies premium calculation, coverage activation, claim assessment, and payout authorization with proper events [attached_file:9]
├── intent-solver.test.js                      # Tests intent submission, solver competition/selection, settlement hooks, and failure/timeout handling [attached_file:9]
├── operator-nft.test.js                       # Confirms operator role issuance/delegation, permission checks, and auditability via emitted events [attached_file:9]
├── README.md                                  # Index and guidance for running, structuring, and extending src-level contract tests in CI and locally [attached_file:9]
├── reputation-oracle.test.js                  # Validates scoring updates, slashing conditions, reward accrual, and integration signals for downstream modules [attached_file:9]
├── upgradable-proxy.test.js                   # Proves storage layout stability, proxy upgrade safety, and rollback procedures across implementation changes [attached_file:9]
└── zk-proof.test.js                           # Verifies proof submission/verification paths, failure cases, and integration with zk-snark utilities and verifiers [attached_file:9]
```

### Apex Arbitrage Multichain bot\backend\core

The core root contains orchestrators, scanners, simulators, MEV protection, failover, and execution helpers that the backend runtime wires together.[1][2]

```text
backend/core/
├── agent-orchestrator.js                      # Coordinates agent lifecycles and inter-module signaling [attached_file:9]
├── ai-controller.js                           # Facade to AI modules for inference and scoring [attached_file:9]
├── alpha-signal-broadcaster.js                # Broadcasts alpha signals with audit/dedupe [attached_file:9]
├── automated-risk-manager.js                  # Enforces dynamic risk caps/kill-switches [attached_file:9]
├── bridge-scanner.js                          # Cross-chain bridge event scanner [attached_file:9]
├── bundle-composer.js                         # Composes transaction batches/bundles [attached_file:9]
├── cross-market-adapter.js                    # Normalized integration across venues [attached_file:9]
├── digital-twin-simulator.js                  # Twin simulations to validate strategies [attached_file:9]
├── execute-arbitrage.js                       # Entry to execute arb with pre/post checks [attached_file:9]
├── failover-engine.js                         # Controls failover and fallback routing [attached_file:9]
├── gas-optimizer.js                           # Gas estimation and optimization [attached_file:9]
├── incident-response-core.js                  # Incident orchestration and escalation [attached_file:9]
├── index.js                                   # Core entry/wiring for orchestrated runtime [attached_file:9]
├── liquidity-scanner.js                       # Liquidity scans to refresh routes [attached_file:9]
├── mev-defender.js                            # Detects/mitigates MEV adversaries [attached_file:9]
├── module-sandbox.js                          # Sandboxes dynamically loaded modules [attached_file:9]
├── monitor-prices.js                          # Tracks price feeds and volatility [attached_file:9]
├── parallel-sim-runner.js                     # Runs simulations concurrently [attached_file:9]
├── profit-safeguard.js                        # Enforces profit thresholds/halts [attached_file:9]
├── prompt-sync-input.js                       # Gated operator confirmations [attached_file:9]
├── README.md                                  # Core overview and wiring map [attached_file:9]
├── shadow-bot-manager.js                      # Parallel "shadow" strategy runner [attached_file:9]
└── simulate-trade.js                          # Single-route simulation/traces [attached_file:9]
```

### Apex Arbitrage Multichain bot\backend\core\data\simulation-snapshots

Simulation snapshots are curated for reproducibility and forensics during core validation workflows.[2]

```text
backend/core/data/simulation-snapshots/
├── README.md                                  # Snapshot provenance and replay guide [attached_file:9]
├── snapshot-20250701.json                     # July 1, 2025 snapshot [attached_file:9]
├── snapshot-20250715.json                     # July 15, 2025 snapshot [attached_file:9]
└── snapshot-20250730.json                     # July 30, 2025 snapshot [attached_file:9]
```

### Apex Arbitrage Multichain bot\backend\core\docs

Core documentation details architecture, flowcharts, migrations, quickstart, and troubleshooting for the runtime.[2]

```text
backend/core/docs/
├── architecture.md                            # Core architecture and module boundaries [attached_file:9]
├── core-flowcharts.md                         # Orchestrator/scan/exec flow diagrams [attached_file:9]
├── migration-notes.md                         # Safe migration guidance across versions [attached_file:9]
├── quickstart.md                              # Start core locally and run sims [attached_file:9]
├── README.md                                  # Docs index and contribution workflow [attached_file:9]
└── troubleshooting.md                         # Common runtime issues and fixes [attached_file:9]
```

### Apex Arbitrage Multichain bot\backend\core\hooks

Reusable hooks expose reactive state for alerts, bundle status, rollbacks, and simulation lifecycle in operator UIs.[2]

```text
backend/core/hooks/
├── README.md                                  # Hooks usage and interfaces [attached_file:9]
├── use-alerts-hook.js                         # Subscribe to alert channels with ack/dedupe [attached_file:9]
├── use-bundle-status.js                       # Live bundle compose/submit status [attached_file:9]
├── use-rollback-hook.js                       # Rollback triggers and state for recovery [attached_file:9]
└── use-simulation-hook.js                     # Simulation lifecycle and stream handling [attached_file:9]
```

### Apex Arbitrage Multichain bot\backend\core\tests

Core tests cover bundle composition, twin simulation, failover, and incidents; a nested hooks suite validates each hook's behavior.[2]

```text
backend/core/tests/
├── bundle-composer.test.js                    # Dependency ordering and revert strategy checks [attached_file:9]
├── core-unit.test.js                          # Core primitives unit suite [attached_file:9]
├── digital-twin-simulator.test.js             # Twin parity and reporting validations [attached_file:9]
├── failover-engine.test.js                    # Failover triggers/fallback recovery [attached_file:9]
├── incident-response-core.test.js             # Incident orchestration flows [attached_file:9]
├── README.md                                  # Tests index and CI wiring [attached_file:9]
└── hooks/                                     # Hook-specific tests in canonical order [attached_file:9]
```

### Apex Arbitrage Multichain bot\backend\core\tests\hooks

Hook tests validate alert streams, bundle state transitions, rollback idempotency, and simulation result handling.[2]

```text
backend/core/tests/hooks/
├── README.md                                  # Hook tests guidance/contracts [attached_file:9]
├── use-alerts-hook.test.js                    # Noisy channel behavior and dedupe [attached_file:9]
├── use-bundle-status.test.js                  # State transitions and terminal states [attached_file:9]
├── use-rollback-hook.test.js                  # Triggers, retry, and idempotency [attached_file:9]
└── use-simulation-hook.test.js                # Result streaming and error propagation [attached_file:9]
```

### Apex Arbitrage Multichain bot\backend\core\utils

Utilities provide rate limiting, context propagation, error reporting, job queues, logging, nonce management, and stateful caching for core flows.[2]

```text
backend/core/utils/
├── api-rate-limiter.js                        # Shared API rate limiter [attached_file:9]
├── context-propagator.js                      # Carries trace/request context across async [attached_file:9]
├── error-reporter.js                          # Normalized error reporting and alerts [attached_file:9]
├── job-queue.js                               # Lightweight orchestrated task queue [attached_file:9]
├── logger.js                                  # Structured logger with correlation IDs [attached_file:9]
├── nonce-manager.js                           # Prevent nonce collisions per account [attached_file:9]
├── README.md                                  # Utils index and extension notes [attached_file:9]
└── stateful-cache.js                          # TTL/eviction cache for hot data [attached_file:9]
```

