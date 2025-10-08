# Project Complete Tree

Generated:
2025-10-04 06:32:06 +05:30
Source Root: Apex Arbitrage Multi chain bot/
File Count: 6165
Directory Count: 849

C:\USERS\PAVAN PC\DESKTOP\APEX ARBITRAGE MULTICHAIN BOT\APEX ARBITRAGE MULTICHAIN BOT
|   .dockerignore
|   .editorconfig
|   .env
|   .env.example
|   .eslintrc
|   .flake8
|   .gitignore
|   .prettierrc
|   .stylelintrc
|   ai-feedback.sqlite
|   ai-training.sqlite
|   analytics.sqlite
|   api_reference.md
|   audit-trail.sqlite
|   backup-meta.json
|   Bot Blue Print.md
|   chains.json
|   CHANGELOG.md
|   CODE_OF_CONDUCT.md
|   compliance.sqlite
|   CONTRIBUTING.md
|   docker-compose.yml
|   forensics.sqlite
|   hardhat.config.js
|   HEALTHCHECK.md
|   LEGAL.md
|   LICENSE
|   logs.sqlite
|   Makefile
|   manifest.csv
|   manifest.json
|   manifest.md
|   operator-guide.md
|   package.json
|   PROJECT FILES AND FOLDERS DETAILS .MD
|   PROJECT TREE COMPLETE STUCTURE .md
|   README.md
|   requirements.txt
|   roadmap.md
|   SECURITY.md
|   tsconfig.json
|   wall-of-fame.md
|
+---.devcontainer
|       devcontainer.json
|       Dockerfile
|       env.example
|       extensions.json
|       postCreateCommand.sh
|       README.md
|       requirements.txt
|       settings.json
|
+---.github
|   |   CODEOWNERS
|   |   dependabot.yml
|   |   FUNDING.yml
|   |   README.md
|   |   SECURITY.md
|   |   support.md
|   |
|   +---ISSUE_TEMPLATE
|   |       bug_report.md
|   |       feature_request.md
|   |       general_question.md
|   |       README.md
|   |
|   +---PULL_REQUEST_TEMPLATE
|   |       pull_request.md
|   |       README.md
|   |
|   \---workflows
|           check-project-tree.yml
|           ci.yml
|           deploy.yml
|           lint.yml
|           monitor.yml
|           README.md
|           sync-fork.yml
|           test.yml
|
+---.husky
|       commit-msg
|       commitlint.config.js
|       lint-staged.config.js
|       pre-commit
|       pre-push
|       README.md
|
+---.vscode
|       extensions.json
|       launch.json
|       README.md
|       settings.json
|       tasks.json
|
+---ai-modules
|   |   ai-engine.js
|   |   aiConfig.json
|   |   decisionMaker.js
|   |   modelRouter.js
|   |   patternLearner.js
|   |   README.md
|   |   scoreArbOpportunity.js
|   |   tokenReputationIndex.py
|   |   tradeOutcomeLogger.js
|   |
|   +---datasets
|   |       ai-decision-corpus.json
|   |       features.csv
|   |       profitLabels.json
|   |       README.md
|   |       trade-history.csv
|   |
|   +---features
|   |       featureExtractor.js
|   |       gasFeeSpikeFeature.js
|   |       latencyProfileFeature.js
|   |       priceDeltaFeature.js
|   |       README.md
|   |
|   +---integration
|   |       aiBridgeAdapter.js
|   |       aiHooks.js
|   |       aiLogFormatter.js
|   |       aiWebhookReceiver.js
|   |       README.md
|   |
|   +---models
|   |   |   README.md
|   |   |
|   |   +---modelWeights
|   |   |       decisionNet-v1.pt
|   |   |       patternNet-v2.onnx
|   |   |       README.md
|   |   |       scorerModel.json
|   |   |       volatilityClassifier.pkl
|   |   |
|   |   \---trainingOutputs
|   |           accuracy-report.txt
|   |           README.md
|   |           token-risk-score-histogram.png
|   |           trade-learning-curve.png
|   |
|   +---notebooks
|   |       latency-vs-profit.ipynb
|   |       model-training-logistics.ipynb
|   |       README.md
|   |       risk-surface-analysis.ipynb
|   |       trade-pattern-exploration.ipynb
|   |
|   +---simulation
|   |       aiReplayValidator.js
|   |       analyzeAIErrorCases.js
|   |       README.md
|   |       simulateAITrade.js
|   |
|   +---tests
|   |       README.md
|   |       testFeatureExtractor.test.js
|   |       testModelRouter.test.js
|   |       testPatternLearner.test.js
|   |       testScoreArbOpportunity.test.js
|   |
|   \---train
|           config.yaml
|           evaluate.py
|           preprocess.py
|           README.md
|           train.py
|           trainFineTune.py
|
+---archive
|   |   README.md
|   |   README_ARCHIVE_GUIDE.md
|   |
|   +---archived-tests
|   |   |   aiScoring-legacy.test.js
|   |   |   README.md
|   |   |   testLegacyFlashloan.js
|   |   |   tradeSamples-v1.json
|   |   |
|   |   \---archived-output-logs
|   |           ai-trace-legacy.log
|   |           README.md
|   |           trade-diffs-old.json
|   |           tx-failure-snapshots.log
|   |
|   +---deprecated-modules
|   |   |   flashloan-logic-legacy.sol
|   |   |   legacy-arbEngine-v1.js
|   |   |   old-ai-model.py
|   |   |   README.md
|   |   |   route-cache-old.js
|   |   |
|   |   \---ui-backup-2023-12
|   |           app.js
|   |           index.html
|   |           main.css
|   |           README.md
|   |
|   +---docs
|   |   |   README.md
|   |   |
|   |   +---api-diffs
|   |   |       contracts-diff-v1-v2.md
|   |   |       README.md
|   |   |
|   |   +---compliance-logs
|   |   |       audit-2023Q2.md
|   |   |       audit-2024-GDPR-report.md
|   |   |       README.md
|   |   |
|   |   +---deprecation-notices
|   |   |       deprecated-flashloan-2023.md
|   |   |       README.md
|   |   |
|   |   +---incident-reports
|   |   |       incident-2023-07-22.md
|   |   |       README.md
|   |   |
|   |   +---migration-notes
|   |   |       migration-v2.0.md
|   |   |       README.md
|   |   |
|   |   +---old-adrs
|   |   |       adr-001-example.md
|   |   |       adr-002-example.md
|   |   |       README.md
|   |   |
|   |   +---onboarding
|   |   |       onboarding-v1.md
|   |   |       README.md
|   |   |
|   |   \---playbooks
|   |           failover-v1.sh
|   |           README.md
|   |           runbook-legacy.md
|   |
|   +---migration-logs
|   |       db-schema-v1.sql
|   |       migration-2024-12-20.log
|   |       migration-2025-06-01.log
|   |       migration-2025-07-15.log
|   |       migration-failures.log
|   |       migration-summary.csv
|   |       README.md
|   |
|   +---migrations-logs
|   |       README.md
|   |
|   +---old-configs
|   |       chains-v1.json
|   |       dexes-legacy.json
|   |       flashloanParams-v1.json
|   |       README.md
|   |       risk-profiles-archive.json
|   |       strategy-params-legacy.yaml
|   |       tokens-old.json
|   |
|   \---previous-releases
|           README.md
|           release-notes-v1.md
|           release-v1.0.zip
|           release-v1.1-beta.zip
|           release-v1.2-integrity.sha256
|           release-v1.2.zip
|
+---backend
|   |   .eslintrc
|   |   .flake8
|   |   .gitignore
|   |   .prettierrc
|   |   .stylelintrc
|   |   api_reference.md
|   |   BACKEND.MD TOP DIRECTORY FROM PROJECT TREE COMPLETE STUCTURE .md
|   |   CHANGELOG.md
|   |   CONTRIBUTING.md
|   |   docker-compose.yml
|   |   Dockerfile
|   |   jest.config.js
|   |   LICENSE
|   |   Makefile
|   |   operator-guide.md
|   |   package.json
|   |   pyproject.toml
|   |   README.md
|   |   requirements.txt
|   |   SECURITY.md
|   |   tsconfig.json
|   |
|   +---backup
|   |       README.md
|   |
|   +---contracts
|   |   |   AlphaNFT.sol
|   |   |   ArbitrageExecutor.sol
|   |   |   DigitalTwinBridge.sol
|   |   |   DisputeResolution.sol
|   |   |   Events.sol
|   |   |   FlashLoanArbitrage.sol
|   |   |   GovernanceModule.sol
|   |   |   InsurancePool.sol
|   |   |   IntentSolver.sol
|   |   |   OperatorNFT.sol
|   |   |   QuantumReadyModule.sol
|   |   |   README.md
|   |   |   ReputationOracle.sol
|   |   |   SocialImpactDistributor.sol
|   |   |   UpgradableProxy.sol
|   |   |
|   |   +---docs
|   |   |       ai-agent-integration.md
|   |   |       audits.md
|   |   |       contract-architecture.md
|   |   |       coverage-report.md
|   |   |       cross-chain-bridges.md
|   |   |       digital-twin-architecture.md
|   |   |       events-reference.md
|   |   |       formal-verification.md
|   |   |       governance-design.md
|   |   |       insurance-mechanisms.md
|   |   |       interface-specs.md
|   |   |       plugin-architecture.md
|   |   |       quantum-resilience.md
|   |   |       README.md
|   |   |       test-playbooks.md
|   |   |       upgradeability.md
|   |   |
|   |   +---interfaces
|   |   |       IAIAgentInterface.sol
|   |   |       IAIOracle.sol
|   |   |       IAlphaNFT.sol
|   |   |       IAlphaSignal.sol
|   |   |       IBridge.sol
|   |   |       ICompliance.sol
|   |   |       IDEXAdapter.sol
|   |   |       IDigitalTwinBridge.sol
|   |   |       IERC20.sol
|   |   |       IFlashLoanProvider.sol
|   |   |       IForkSimulation.sol
|   |   |       IGovernance.sol
|   |   |       IInsurance.sol
|   |   |       IIntentSolver.sol
|   |   |       IOperatorNFT.sol
|   |   |       IOracle.sol
|   |   |       IPluginMarket.sol
|   |   |       IReputationOracle.sol
|   |   |       IRewardDistributor.sol
|   |   |       ISocialImpact.sol
|   |   |       IUpgradeBeacon.sol
|   |   |       IZKVerifier.sol
|   |   |       README.md
|   |   |
|   |   +---scripts
|   |   |       alpha-nft-mint.js
|   |   |       deploy.js
|   |   |       digital-twin-runner.js
|   |   |       fork-test.js
|   |   |       governance-init.js
|   |   |       README.md
|   |   |       simulate-arb.js
|   |   |       snapshot.js
|   |   |       upgrade.js
|   |   |       verify.js
|   |   |
|   |   \---src
|   |       |   README.md
|   |       |
|   |       +---executors
|   |       |       alpha-signal-executor.sol
|   |       |       arb-executor.sol
|   |       |       batch-executor.sol
|   |       |       digital-twin-executor.sol
|   |       |       governance-executor.sol
|   |       |       insurance-executor.sol
|   |       |       liquidation-executor.sol
|   |       |       plugin-executor.sol
|   |       |       README.md
|   |       |       sandbox-executor.sol
|   |       |
|   |       +---governance
|   |       |       dispute-manager.sol
|   |       |       fork-voting.sol
|   |       |       governance-token.sol
|   |       |       proposal-registry.sol
|   |       |       README.md
|   |       |       timelock.sol
|   |       |       voting.sol
|   |       |
|   |       +---interfaces
|   |       |       IAIAgentInterface.sol
|   |       |       IAlphaFeed.sol
|   |       |       IArbScore.sol
|   |       |       IAudit.sol
|   |       |       IExecutionModule.sol
|   |       |       IIncident.sol
|   |       |       IRewardVault.sol
|   |       |       IUpgradeBeacon.sol
|   |       |       README.md
|   |       |
|   |       +---onchain-governance
|   |       |       council.sol
|   |       |       dao.sol
|   |       |       fork-consensus.sol
|   |       |       proposal-factory.sol
|   |       |       README.md
|   |       |       upgrade-voting.sol
|   |       |
|   |       +---proofs
|   |       |       ai-audit.sol
|   |       |       audit-proof.sol
|   |       |       fraud-proof.sol
|   |       |       quantum-proof.sol
|   |       |       README.md
|   |       |       replay-attack-guard.sol
|   |       |       zk-proof.sol
|   |       |       zk-snark-utils.sol
|   |       |
|   |       +---registries
|   |       |       address-registry.sol
|   |       |       asset-registry.sol
|   |       |       module-registry.sol
|   |       |       nft-registry.sol
|   |       |       operator-registry.sol
|   |       |       plugin-registry.sol
|   |       |       README.md
|   |       |
|   |       \---test
|   |               alpha-nft.test.js
|   |               batch-executor.test.js
|   |               digital-twin-bridge.test.js
|   |               dispute-resolution.test.js
|   |               flashloan-arbitrage.test.js
|   |               governance-module.test.js
|   |               insurance-pool.test.js
|   |               intent-solver.test.js
|   |               operator-nft.test.js
|   |               README.md
|   |               reputation-oracle.test.js
|   |               upgradable-proxy.test.js
|   |               zk-proof.test.js
|   |
|   +---core
|   |   |   agent-orchestrator.js
|   |   |   ai-controller.js
|   |   |   alpha-signal-broadcaster.js
|   |   |   automated-risk-manager.js
|   |   |   bridge-scanner.js
|   |   |   bundle-composer.js
|   |   |   cross-market-adapter.js
|   |   |   digital-twin-simulator.js
|   |   |   execute-arbitrage.js
|   |   |   failover-engine.js
|   |   |   gas-optimizer.js
|   |   |   incident-response-core.js
|   |   |   index.js
|   |   |   liquidity-scanner.js
|   |   |   mev-defender.js
|   |   |   module-sandbox.js
|   |   |   monitor-prices.js
|   |   |   parallel-sim-runner.js
|   |   |   profit-safeguard.js
|   |   |   prompt-sync-input.js
|   |   |   README.md
|   |   |   shadow-bot-manager.js
|   |   |   simulate-trade.js
|   |   |
|   |   +---data
|   |   |   |   active-pools.json
|   |   |   |   README.md
|   |   |   |   route-cache.json
|   |   |   |   state-history.log
|   |   |   |
|   |   |   \---simulation-snapshots
|   |   |           README.md
|   |   |           snapshot-20250701.json
|   |   |           snapshot-20250715.json
|   |   |           snapshot-20250730.json
|   |   |
|   |   +---docs
|   |   |       architecture.md
|   |   |       core-flowcharts.md
|   |   |       migration-notes.md
|   |   |       quickstart.md
|   |   |       README.md
|   |   |       troubleshooting.md
|   |   |
|   |   +---hooks
|   |   |       README.md
|   |   |       use-alerts-hook.js
|   |   |       use-bundle-status.js
|   |   |       use-rollback-hook.js
|   |   |       use-simulation-hook.js
|   |   |
|   |   +---tests
|   |   |   |   bundle-composer.test.js
|   |   |   |   core-unit.test.js
|   |   |   |   digital-twin-simulator.test.js
|   |   |   |   failover-engine.test.js
|   |   |   |   incident-response-core.test.js
|   |   |   |   README.md
|   |   |   |
|   |   |   \---hooks
|   |   |           README.md
|   |   |           use-alerts-hook.test.js
|   |   |           use-bundle-status.test.js
|   |   |           use-rollback-hook.test.js
|   |   |           use-simulation-hook.test.js
|   |   |
|   |   \---utils
|   |           api-rate-limiter.js
|   |           context-propagator.js
|   |           error-reporter.js
|   |           job-queue.js
|   |           logger.js
|   |           nonce-manager.js
|   |           README.md
|   |           stateful-cache.js
|   |
|   +---coverage
|   |       README.md
|   |
|   +---data
|   |   |   active-pools.json
|   |   |   agent-scores.json
|   |   |   ai-evaluations.json
|   |   |   compliance-log.json
|   |   |   fork-state-diff.json
|   |   |   incident-log.json
|   |   |   market-depth.json
|   |   |   operator-profiles.json
|   |   |   oracle-feed-cache.json
|   |   |   plugin-usage.json
|   |   |   profit-log.json
|   |   |   README.md
|   |   |   risk-events.json
|   |   |   route-cache.json
|   |   |   simulation-runs.json
|   |   |   state-history.log
|   |   |   token-metadata.json
|   |   |   trade-history.json
|   |   |
|   |   +---ai-feedback
|   |   |       feedback-20250701.json
|   |   |       feedback-20250715.json
|   |   |       feedback-20250730.json
|   |   |       model-update-requests.json
|   |   |       README.md
|   |   |
|   |   +---analytics
|   |   |       ai-inference-20250701.json
|   |   |       ai-inference-20250715.json
|   |   |       ai-inference-20250730.json
|   |   |       anomaly-events-20250730.json
|   |   |       pool-liquidity-report-20250701.json
|   |   |       pool-liquidity-report-20250715.json
|   |   |       pool-liquidity-report-20250730.json
|   |   |       README.md
|   |   |       trade-alpha-scores-20250701.json
|   |   |       trade-alpha-scores-20250715.json
|   |   |       trade-alpha-scores-20250730.json
|   |   |
|   |   +---audit-trails
|   |   |       audit-20250701.log
|   |   |       audit-20250715.log
|   |   |       audit-20250730.log
|   |   |       event-archive-20250701.json
|   |   |       event-archive-20250715.json
|   |   |       event-archive-20250730.json
|   |   |       README.md
|   |   |
|   |   +---compliance-archive
|   |   |       kyc-report-20250701.pdf
|   |   |       kyc-report-20250715.pdf
|   |   |       kyc-report-20250730.pdf
|   |   |       README.md
|   |   |       sanctions-check-20250701.json
|   |   |       sanctions-check-20250715.json
|   |   |       sanctions-check-20250730.json
|   |   |
|   |   +---export
|   |   |       ai-inference-export-20250701.json
|   |   |       dashboard-report-20250730.pdf
|   |   |       export-20250701.csv
|   |   |       export-20250715.csv
|   |   |       export-20250730.csv
|   |   |       README.md
|   |   |
|   |   +---forensics
|   |   |       exploit-dump-20250701.json
|   |   |       exploit-dump-20250715.json
|   |   |       exploit-dump-20250730.json
|   |   |       README.md
|   |   |       root-cause-analysis.md
|   |   |       trade-anomaly-20250730.json
|   |   |
|   |   +---logs
|   |   |       ai-agent-20250701.log
|   |   |       ai-agent-20250715.log
|   |   |       ai-agent-20250730.log
|   |   |       engine-20250701.log
|   |   |       engine-20250715.log
|   |   |       engine-20250730.log
|   |   |       error-20250701.log
|   |   |       error-20250715.log
|   |   |       error-20250730.log
|   |   |       README.md
|   |   |       rotation-policy.md
|   |   |       trades-20250701.log
|   |   |       trades-20250715.log
|   |   |       trades-20250730.log
|   |   |       watchdog-20250701.log
|   |   |       watchdog-20250715.log
|   |   |       watchdog-20250730.log
|   |   |
|   |   +---operator-audit
|   |   |       ai-review-20250715.json
|   |   |       nlp-feedback-20250730.json
|   |   |       operator-actions-20250701.json
|   |   |       operator-actions-20250715.json
|   |   |       operator-actions-20250730.json
|   |   |       README.md
|   |   |
|   |   +---simulation-snapshots
|   |   |       post-fork-sim-20250715.json
|   |   |       pre-fork-sim-20250715.json
|   |   |       README.md
|   |   |       risk-test-20250715.json
|   |   |       snapshot-20250701.json
|   |   |       snapshot-20250715.json
|   |   |       snapshot-20250730.json
|   |   |
|   |   +---snapshots
|   |   |       agents-20250701.json
|   |   |       agents-20250715.json
|   |   |       agents-20250730.json
|   |   |       latest-snapshot.json
|   |   |       pools-20250701.json
|   |   |       pools-20250715.json
|   |   |       pools-20250730.json
|   |   |       README.md
|   |   |       sim-20250701.json
|   |   |       sim-20250715.json
|   |   |       sim-20250730.json
|   |   |
|   |   \---synthetic-datasets
|   |           deep-arb-ai-trainset.csv
|   |           fake-arb-scenarios.json
|   |           README.md
|   |           sim-synthetic-events.json
|   |           synthetic-prices-20250701.csv
|   |           synthetic-prices-20250715.csv
|   |           synthetic-profits-20250730.csv
|   |
|   +---docs
|   |   |   ai-integration.md
|   |   |   architecture.md
|   |   |   backend-api.md
|   |   |   backend-stack.md
|   |   |   ci-cd.md
|   |   |   code-quality.md
|   |   |   compliance.md
|   |   |   contract-integration.md
|   |   |   data-pipeline.md
|   |   |   db-schema.md
|   |   |   event-handling.md
|   |   |   event-reference.md
|   |   |   failover-guide.md
|   |   |   faq.md
|   |   |   fork-testing.md
|   |   |   formal-verification.md
|   |   |   incident-response.md
|   |   |   logging-monitoring.md
|   |   |   mainnet-deployment.md
|   |   |   mainnet-hardening.md
|   |   |   module-development.md
|   |   |   notification-guide.md
|   |   |   operator-guide.md
|   |   |   operator-roles.md
|   |   |   plugin-architecture.md
|   |   |   quickstart.md
|   |   |   README.md
|   |   |   release-notes.md
|   |   |   risk-management.md
|   |   |   roadmap.md
|   |   |   security.md
|   |   |   simulation-workflow.md
|   |   |   test-strategy.md
|   |   |   upgradeability.md
|   |   |
|   |   +---ai
|   |   |       ai-engine.md
|   |   |       ai-ml-pipeline.md
|   |   |       ai-models.md
|   |   |       ai-ops-guide.md
|   |   |       ai-testing-guide.md
|   |   |       ai-upgradeability.md
|   |   |       README.md
|   |   |
|   |   +---api
|   |   |       ai-engine-api.yaml
|   |   |       backend-api.yaml
|   |   |       dashboard-api.yaml
|   |   |       notification-api.yaml
|   |   |       plugin-api.yaml
|   |   |       README.md
|   |   |       simulation-api.yaml
|   |   |
|   |   +---compliance
|   |   |       aml-logs.md
|   |   |       compliance-audit.md
|   |   |       data-retention.md
|   |   |       kyc-flow.md
|   |   |       README.md
|   |   |       sanctions-workflow.md
|   |   |
|   |   +---dashboard
|   |   |       ai-dashboard.md
|   |   |       dashboard-api.md
|   |   |       dashboard-architecture.md
|   |   |       live-analytics-guide.md
|   |   |       notification-integration.md
|   |   |       overlays-integration.md
|   |   |       plugin-status-panel.md
|   |   |       README.md
|   |   |
|   |   +---diagrams
|   |   |       ai-integration.drawio
|   |   |       backend-architecture.drawio
|   |   |       ci-cd-pipeline.drawio
|   |   |       data-pipeline.drawio
|   |   |       failover-diagram.drawio
|   |   |       fork-testing.drawio
|   |   |       incident-response.drawio
|   |   |       operator-dashboard.drawio
|   |   |       plugin-system.drawio
|   |   |       README.md
|   |   |       risk-flow.drawio
|   |   |       simulation-workflow.drawio
|   |   |
|   |   +---formal
|   |   |       ai-formal-verification.md
|   |   |       contract-formal-verification.md
|   |   |       formal-verification-report.md
|   |   |       invariants.md
|   |   |       model-specs.md
|   |   |       README.md
|   |   |
|   |   +---legacy
|   |   |       deprecated-architecture.md
|   |   |       legacy-api.md
|   |   |       legacy-upgrade-guide.md
|   |   |       old-release-notes.md
|   |   |       README.md
|   |   |
|   |   +---migration
|   |   |       ai-migration.md
|   |   |       backend-migration.md
|   |   |       contract-migration.md
|   |   |       db-migration.md
|   |   |       plugin-migration.md
|   |   |       README.md
|   |   |
|   |   +---onboarding
|   |   |       ai-module-onboarding.md
|   |   |       auditor-onboarding.md
|   |   |       developer-onboarding.md
|   |   |       faq-onboarding.md
|   |   |       operator-onboarding.md
|   |   |       plugin-onboarding.md
|   |   |       README.md
|   |   |
|   |   +---playbooks
|   |   |       disaster-recovery.md
|   |   |       incident-playbook.md
|   |   |       ops-handover.md
|   |   |       README.md
|   |   |       rollback-playbook.md
|   |   |       upgrade-playbook.md
|   |   |
|   |   \---risk
|   |           ai-risk.md
|   |           bridge-risk.md
|   |           incident-catalog.md
|   |           kill-switch.md
|   |           mev-risk.md
|   |           oracle-risk.md
|   |           pool-risk.md
|   |           README.md
|   |           risk-dashboard.md
|   |           trade-risk.md
|   |
|   +---engine
|   |   |   adaptive-fee-controller.js
|   |   |   alpha-marketplace-engine.js
|   |   |   analytics-reporter.js
|   |   |   auto-strategy-composer.js
|   |   |   block-profiler.js
|   |   |   bundle-simulator.js
|   |   |   circuit-breaker.js
|   |   |   digital-twin-exec.js
|   |   |   dynamic-route-manager.js
|   |   |   economic-dao-governance-engine.js
|   |   |   flashloan-engine.js
|   |   |   fork-sync-validator.js
|   |   |   liquidity-shard-manager.js
|   |   |   loan-sizer.js
|   |   |   mev-aware-router.js
|   |   |   multi-modal-inference-engine.js
|   |   |   nlp-inference-engine.js
|   |   |   profit-curve-estimator.js
|   |   |   queue-optimizer.js
|   |   |   README.md
|   |   |   result-compressor.js
|   |   |   risk-mitigator.js
|   |   |   state-restorer.js
|   |   |   temporal-scheduler.js
|   |   |   trade-batch-manager.js
|   |   |   trade-throttler.js
|   |   |   volatility-guard.js
|   |   |
|   |   +---data
|   |   |   |   README.md
|   |   |   |
|   |   |   +---analytics
|   |   |   |       engine-analytics-20250701.json
|   |   |   |       engine-analytics-20250715.json
|   |   |   |       engine-analytics-20250730.json
|   |   |   |       README.md
|   |   |   |
|   |   |   +---batch-logs
|   |   |   |       batch-20250701.log
|   |   |   |       batch-20250715.log
|   |   |   |       batch-20250730.log
|   |   |   |       README.md
|   |   |   |
|   |   |   +---sim-results
|   |   |   |       README.md
|   |   |   |       sim-20250701.json
|   |   |   |       sim-20250715.json
|   |   |   |       sim-20250730.json
|   |   |   |
|   |   |   \---snapshots
|   |   |           README.md
|   |   |           state-20250701.json
|   |   |           state-20250715.json
|   |   |           state-20250730.json
|   |   |
|   |   +---docs
|   |   |       benchmarking.md
|   |   |       change-log.md
|   |   |       flashloan-engines.md
|   |   |       formal-verification.md
|   |   |       integration-guide.md
|   |   |       performance-tuning.md
|   |   |       README.md
|   |   |       workflows.md
|   |   |
|   |   +---hooks
|   |   |       README.md
|   |   |       use-alerts-hook.js
|   |   |       use-execution-hook.js
|   |   |       use-mev-detection-hook.js
|   |   |       use-rollback-hook.js
|   |   |
|   |   +---jobs
|   |   |       auto-report-uploader.js
|   |   |       README.md
|   |   |       result-cleaner.js
|   |   |       scheduled-job-runner.js
|   |   |
|   |   +---modules
|   |   |       arbitrage-scanner.js
|   |   |       execution-timer.js
|   |   |       historical-sim-analyzer.js
|   |   |       liquidity-impact-analyzer.js
|   |   |       opportunity-indexer.js
|   |   |       README.md
|   |   |       risk-histogram.js
|   |   |       slippage-simulator.js
|   |   |       strategy-verifier.js
|   |   |
|   |   +---tests
|   |   |   |   bundle-simulator.test.js
|   |   |   |   engine-integration.test.js
|   |   |   |   fork-sync-validator.test.js
|   |   |   |   liquidity-shard-manager.test.js
|   |   |   |   profit-curve-estimator.test.js
|   |   |   |   README.md
|   |   |   |
|   |   |   \---modules
|   |   |           arbitrage-scanner.test.js
|   |   |           execution-timer.test.js
|   |   |           liquidity-impact-analyzer.test.js
|   |   |           README.md
|   |   |           slippage-simulator.test.js
|   |   |           strategy-verifier.test.js
|   |   |
|   |   \---utils
|   |           api-rate-limiter.js
|   |           bundle-utils.js
|   |           error-reporter.js
|   |           fee-estimator.js
|   |           logger.js
|   |           nonce-manager.js
|   |           queue-utils.js
|   |           README.md
|   |           stateful-cache.js
|   |
|   +---examples
|   |   |   ai-sim-report.md
|   |   |   cli-usage.txt
|   |   |   config-presets.md
|   |   |   dashboard-tour.md
|   |   |   dryrun-results.md
|   |   |   experiment-log.md
|   |   |   mainnet-replay.md
|   |   |   operator-demo.md
|   |   |   param-quickstart.md
|   |   |   plugin-demo.md
|   |   |   README.md
|   |   |   sim-arb-day.json
|   |   |   strategy-walkthrough.md
|   |   |
|   |   +---ai-tuning
|   |   |       ai-ablation-study-20250701.md
|   |   |       ai-config-tuning-20250701.json
|   |   |       ai-hyperparam-search-20250701.json
|   |   |       ai-loss-curve-20250701.png
|   |   |       model-selection-demo-20250701.md
|   |   |       README.md
|   |   |
|   |   +---configs
|   |   |       ai-module.example.json
|   |   |       chains.example.json
|   |   |       dashboard.example.json
|   |   |       README.md
|   |   |       routers.example.json
|   |   |       sample-mode-presets.json
|   |   |       tokens.example.json
|   |   |
|   |   +---dashboard-screenshots
|   |   |       ai-arb-explorer.png
|   |   |       dashboard-main.png
|   |   |       failover-popup.png
|   |   |       fork-testing-ui.png
|   |   |       governance-panel.png
|   |   |       incident-popup.png
|   |   |       overlays-active.png
|   |   |       pool-heatmap.png
|   |   |       profit-log-chart.png
|   |   |       README.md
|   |   |       risk-dashboard.png
|   |   |       watchdog-alerts.png
|   |   |
|   |   +---legacy
|   |   |       deprecated-sim-output.json
|   |   |       legacy-arb-demo.json
|   |   |       legacy-config.json
|   |   |       legacy-dashboard.png
|   |   |       old-cli-usage.txt
|   |   |       README.md
|   |   |
|   |   +---mainnet-tx-samples
|   |   |       batch-tx-mainnet-20250701.json
|   |   |       batch-tx-mainnet-20250730.json
|   |   |       README.md
|   |   |       tx-arb-loss-2.json
|   |   |       tx-arb-profit-1.json
|   |   |       tx-fork-diverge-5.json
|   |   |       tx-mev-front-4.json
|   |   |       tx-revert-3.json
|   |   |
|   |   +---research-demos
|   |   |       ai-scorer-demo.md
|   |   |       alpha-patterns-demo.md
|   |   |       fork-testing-demo.md
|   |   |       gas-cost-demo.md
|   |   |       plugin-benchmark-demo.md
|   |   |       profit-gradient-demo.md
|   |   |       README.md
|   |   |       volatility-profile-demo.md
|   |   |
|   |   \---sim-outputs
|   |           ai-feedback-20250701.json
|   |           ai-trade-outputs-20250701.json
|   |           dryrun-output-20250701.log
|   |           dryrun-output-20250730.log
|   |           README.md
|   |           sim-run-20250701.json
|   |           sim-run-20250715.json
|   |           sim-run-20250730.json
|   |
|   +---legacy
|   |       README.md
|   |
|   +---migrations
|   |   |   migration-manifest.json
|   |   |   README.md
|   |   |   VERSIONS.md
|   |   |
|   |   +---ai
|   |   |   |   README.md
|   |   |   |   v1.0-load-base-model.py
|   |   |   |   v1.1-finetune-volatility.py
|   |   |   |   v1.2-update-weights.py
|   |   |   |   v1.3-score-thresholds.json
|   |   |   |   v1.4-dashboard-pipeline.py
|   |   |   |
|   |   |   \---rollback
|   |   |           README.md
|   |   |           v1.1-rollback.py
|   |   |           v1.2-rollback.py
|   |   |           v1.3-rollback.json
|   |   |
|   |   +---config
|   |   |   |   README.md
|   |   |   |   v1.0-defaults.json
|   |   |   |   v1.1-risk-profiles.json
|   |   |   |   v1.2-hotload-profiles.json
|   |   |   |   v1.3-operator-roles.json
|   |   |   |   v1.4-alert-thresholds.json
|   |   |   |
|   |   |   \---rollback
|   |   |           README.md
|   |   |           v1.1-rollback.json
|   |   |           v1.2-rollback.json
|   |   |           v1.3-rollback.json
|   |   |           v1.4-rollback.json
|   |   |
|   |   +---contracts
|   |   |   |   README.md
|   |   |   |   v1.0-core-deploy.js
|   |   |   |   v1.1-governance-module.js
|   |   |   |   v1.2-insurance-pool.js
|   |   |   |   v1.3-alpha-nft.js
|   |   |   |   v1.4-intent-solver.js
|   |   |   |   v1.5-zk-proof.js
|   |   |   |
|   |   |   \---rollback
|   |   |           README.md
|   |   |           v1.1-revert-governance.js
|   |   |           v1.2-revert-insurance.js
|   |   |           v1.3-revert-alpha-nft.js
|   |   |           v1.4-revert-intent-solver.js
|   |   |           v1.5-revert-zk-proof.js
|   |   |
|   |   +---db
|   |   |   |   README.md
|   |   |   |   v1.0-init-schema.sql
|   |   |   |   v1.1-ai-feedback-schema.sql
|   |   |   |   v1.2-event-log-enhancements.sql
|   |   |   |   v1.3-metrics-dashboard.sql
|   |   |   |   v1.4-kill-switch-schema.sql
|   |   |   |   v1.5-plugin-registry.sql
|   |   |   |
|   |   |   \---rollback
|   |   |           README.md
|   |   |           v1.1-rollback.sql
|   |   |           v1.2-rollback.sql
|   |   |           v1.3-rollback.sql
|   |   |           v1.4-rollback.sql
|   |   |           v1.5-rollback.sql
|   |   |
|   |   +---legacy
|   |   |       deprecated-contracts.js
|   |   |       legacy-ai-weights.json
|   |   |       legacy-db-schema.sql
|   |   |       legacy-plugin-registry.json
|   |   |       README.md
|   |   |
|   |   +---operator
|   |   |   |   README.md
|   |   |   |   v1.0-onboarding.json
|   |   |   |   v1.1-policy-update.md
|   |   |   |   v1.2-key-rotation.json
|   |   |   |   v1.3-handover-script.js
|   |   |   |
|   |   |   \---rollback
|   |   |           README.md
|   |   |           v1.1-rollback.md
|   |   |           v1.2-rollback.json
|   |   |           v1.3-rollback.js
|   |   |
|   |   +---plugin
|   |   |   |   README.md
|   |   |   |   v1.0-register-core-plugins.js
|   |   |   |   v1.1-dex-fallbacks.js
|   |   |   |   v1.2-ai-indexer.js
|   |   |   |   v1.3-failover-switch.js
|   |   |   |   v1.4-governance-marketplace.js
|   |   |   |
|   |   |   \---rollback
|   |   |           README.md
|   |   |           v1.1-rollback.js
|   |   |           v1.2-rollback.js
|   |   |           v1.3-rollback.js
|   |   |           v1.4-rollback.js
|   |   |
|   |   \---scripts
|   |           migrate-ai.py
|   |           migrate-all.js
|   |           migrate-config.js
|   |           migrate-contracts.js
|   |           migrate-db.js
|   |           migrate-operator.js
|   |           migrate-plugin.js
|   |           migration-audit-log.json
|   |           README.md
|   |           rollback-all.js
|   |
|   +---notebooks
|   |   |   README.md
|   |   |
|   |   +---ai
|   |   |       ablation-studies.ipynb
|   |   |       agent-explainability.ipynb
|   |   |       ai-dashboard-demo.ipynb
|   |   |       ai-evaluation-report.ipynb
|   |   |       ai-hyperparam-search.ipynb
|   |   |       alpha-replay-analysis.ipynb
|   |   |       feature-engineering.ipynb
|   |   |       federated-learning.ipynb
|   |   |       legacy-models-benchmark.ipynb
|   |   |       model-training.ipynb
|   |   |       pattern-discovery.ipynb
|   |   |       README.md
|   |   |       reinforcement-learning.ipynb
|   |   |       volatility-modeling.ipynb
|   |   |
|   |   +---analytics
|   |   |       alpha-signal-analytics.ipynb
|   |   |       dashboard-integration-demo.ipynb
|   |   |       model-drift-monitoring.ipynb
|   |   |       performance-tuning.ipynb
|   |   |       README.md
|   |   |       trade-metrics.ipynb
|   |   |
|   |   +---data-demo
|   |   |       export-demo.ipynb
|   |   |       live-feed-demo.ipynb
|   |   |       quick-exploration.ipynb
|   |   |       README.md
|   |   |       real-vs-sim-plots.ipynb
|   |   |
|   |   +---economics
|   |   |       funding-rate-models.ipynb
|   |   |       incentive-analysis.ipynb
|   |   |       insurance-models.ipynb
|   |   |       liquidity-curve-analysis.ipynb
|   |   |       market-sentiment.ipynb
|   |   |       protocol-tvl-charts.ipynb
|   |   |       README.md
|   |   |
|   |   +---explainability
|   |   |       incident-xai-audit.ipynb
|   |   |       local-vs-global-xai.ipynb
|   |   |       operator-xai-panel-demo.ipynb
|   |   |       README.md
|   |   |       saliency-map-demo.ipynb
|   |   |       XAI-overview.ipynb
|   |   |
|   |   +---legacy
|   |   |       deprecated-ai-models.ipynb
|   |   |       legacy-alpha-analysis.ipynb
|   |   |       legacy-engine-demo.ipynb
|   |   |       legacy-ops-walkthrough.ipynb
|   |   |       old-research-log.ipynb
|   |   |       README.md
|   |   |
|   |   +---MEV
|   |   |       block-timing.ipynb
|   |   |       frontrun-detection.ipynb
|   |   |       JIT-arb-analysis.ipynb
|   |   |       MEV-research-demo.ipynb
|   |   |       MEV-simulation.ipynb
|   |   |       README.md
|   |   |
|   |   +---operator
|   |   |       alert-incident-demo.ipynb
|   |   |       audit-log-explorer.ipynb
|   |   |       compliance-demo.ipynb
|   |   |       governance-interaction.ipynb
|   |   |       README.md
|   |   |       workflow-demo.ipynb
|   |   |
|   |   +---simulation
|   |   |       arb-simulation.ipynb
|   |   |       batch-execution.ipynb
|   |   |       fork-testing.ipynb
|   |   |       latency-benchmark.ipynb
|   |   |       README.md
|   |   |       scenario-testing.ipynb
|   |   |       shadow-sim-demo.ipynb
|   |   |       sim-vs-real-analysis.ipynb
|   |   |       simulation-outputs-demo.ipynb
|   |   |       synthetic-dataset-gen.ipynb
|   |   |       volatility-stress-test.ipynb
|   |   |
|   |   \---strategy
|   |           adaptive-risk.ipynb
|   |           dynamic-loan-sizing.ipynb
|   |           intent-based-routing.ipynb
|   |           MEV-defense-testing.ipynb
|   |           multi-token-arb.ipynb
|   |           profit-gradient-analysis.ipynb
|   |           README.md
|   |           real-vs-sim-comparison.ipynb
|   |           route-discovery.ipynb
|   |
|   +---onboarding
|   |       README.md
|   |
|   +---operator
|   |       README.md
|   |
|   +---overlays
|   |   |   ai-action-overlay.js
|   |   |   ai-audit-trail-overlay.js
|   |   |   ai-debug-overlay.js
|   |   |   ai-insight-panel.js
|   |   |   alert-toast-overlay.js
|   |   |   arbitration-overlay.js
|   |   |   dashboard-overlay.js
|   |   |   event-stream-overlay.js
|   |   |   incident-response-overlay.js
|   |   |   market-sentiment-overlay.js
|   |   |   operator-health-overlay.js
|   |   |   oracle-divergence-overlay.js
|   |   |   plugin-status-overlay.js
|   |   |   profit-loss-overlay.js
|   |   |   README.md
|   |   |   risk-control-overlay.js
|   |   |   simulation-overlay.js
|   |   |   social-impact-overlay.js
|   |   |   tx-history-overlay.js
|   |   |   xai-inspector.js
|   |   |
|   |   +---ar
|   |   |   |   ar-ai-analytics.js
|   |   |   |   ar-entrypoint.js
|   |   |   |   ar-incident-mapper.js
|   |   |   |   ar-market-overlay.js
|   |   |   |   ar-operator-analytics.js
|   |   |   |   ar-xai-visualizer.js
|   |   |   |   README.md
|   |   |   |
|   |   |   \---overlay-3d-assets
|   |   |           3d-bot-avatar.glb
|   |   |           3d-dashboard.glb
|   |   |           3d-explain-graph.glb
|   |   |           3d-gas-meter.glb
|   |   |           3d-health-bar.glb
|   |   |           3d-mev-shield.glb
|   |   |           3d-token.glb
|   |   |           README.md
|   |   |
|   |   +---docs
|   |   |       alerting-tuning.md
|   |   |       ar-integration-guide.md
|   |   |       dashboard-integration.md
|   |   |       incident-overlays.md
|   |   |       overlays-architecture.md
|   |   |       README.md
|   |   |       widget-development.md
|   |   |       xai-explainability.md
|   |   |
|   |   +---tests
|   |   |   |   ai-action-overlay.test.js
|   |   |   |   ai-audit-trail-overlay.test.js
|   |   |   |   ai-debug-overlay.test.js
|   |   |   |   ai-insight-panel.test.js
|   |   |   |   arbitration-overlay.test.js
|   |   |   |   dashboard-overlay.test.js
|   |   |   |   event-stream-overlay.test.js
|   |   |   |   incident-response-overlay.test.js
|   |   |   |   market-sentiment-overlay.test.js
|   |   |   |   oracle-divergence-overlay.test.js
|   |   |   |   plugin-status-overlay.test.js
|   |   |   |   profit-loss-overlay.test.js
|   |   |   |   README.md
|   |   |   |   risk-control-overlay.test.js
|   |   |   |   simulation-overlay.test.js
|   |   |   |   social-impact-overlay.test.js
|   |   |   |   xai-inspector.test.js
|   |   |   |
|   |   |   +---ar
|   |   |   |       ar-entrypoint.test.js
|   |   |   |       ar-incident-mapper.test.js
|   |   |   |       ar-xai-visualizer.test.js
|   |   |   |       README.md
|   |   |   |
|   |   |   \---widgets
|   |   |           mev-risk-widget.test.js
|   |   |           quick-arb-widget.test.js
|   |   |           README.md
|   |   |           wallet-health-widget.test.js
|   |   |
|   |   \---widgets
|   |           ai-status-widget.js
|   |           alpha-feed-widget.js
|   |           gas-trend-widget.js
|   |           governance-vote-widget.js
|   |           mev-risk-widget.js
|   |           oracle-deviation-widget.js
|   |           quick-arb-widget.js
|   |           README.md
|   |           time-sync-widget.js
|   |           tx-rollback-widget.js
|   |           wallet-health-widget.js
|   |
|   +---plugins
|   |   |   atomic-swap-batched.ts
|   |   |   bridge-latency-sniper.ts
|   |   |   flash-sandwich-mm.ts
|   |   |   hyper-bundle-engine.ts
|   |   |   micro-latency-arb-suite.ts
|   |   |   nft-gamefi-arb.ts
|   |   |   README.md
|   |   |
|   |   +---alpha-signal
|   |   |   |   ai-signal-orchestrator.js
|   |   |   |   alpha-nft-issuer.js
|   |   |   |   alpha-reputation.js
|   |   |   |   alpha-voting.js
|   |   |   |   micro-arb-detector.js
|   |   |   |   README.md
|   |   |   |   sandwich-detector.js
|   |   |   |   sniping-detector.js
|   |   |   |   trend-analyzer-v2.js
|   |   |   |   trend-analyzer.js
|   |   |   |   whale-signal.js
|   |   |   |
|   |   |   +---docs
|   |   |   |       alerts-integration.md
|   |   |   |       alpha-reputation-scores.md
|   |   |   |       alpha-signal-models.md
|   |   |   |       alpha-voting-protocol.md
|   |   |   |       arb-patterns.md
|   |   |   |       README.md
|   |   |   |
|   |   |   \---tests
|   |   |           ai-signal-orchestrator.test.js
|   |   |           alpha-nft-issuer.test.js
|   |   |           alpha-reputation.test.js
|   |   |           alpha-voting.test.js
|   |   |           micro-arb-detector.test.js
|   |   |           README.md
|   |   |           sandwich-detector.test.js
|   |   |           sniping-detector.test.js
|   |   |           trend-analyzer-v2.test.js
|   |   |           trend-analyzer.test.js
|   |   |           whale-signal.test.js
|   |   |
|   |   +---bridge-adapters
|   |   |   |   avalanche-adapter.js
|   |   |   |   axelar-adapter.js
|   |   |   |   circle-cctp-adapter.js
|   |   |   |   cross-twin-adapter.js
|   |   |   |   elliptic-adapter.js
|   |   |   |   layerzero-adapter.js
|   |   |   |   polygon-zkevm-adapter.js
|   |   |   |   range-cross-chain-adapter.js
|   |   |   |   README.md
|   |   |   |   relaychain-adapter.js
|   |   |   |   symbiosis-adapter.js
|   |   |   |   wormhole-adapter.js
|   |   |   |
|   |   |   +---docs
|   |   |   |       avalanche-guide.md
|   |   |   |       bridge-integrations.md
|   |   |   |       cross-chain-security.md
|   |   |   |       polygon-zkevm-guide.md
|   |   |   |       README.md
|   |   |   |       relaychain-integration.md
|   |   |   |
|   |   |   \---tests
|   |   |           avalanche-adapter.test.js
|   |   |           axelar-adapter.test.js
|   |   |           circle-cctp-adapter.test.js
|   |   |           cross-twin-adapter.test.js
|   |   |           elliptic-adapter.test.js
|   |   |           layerzero-adapter.test.js
|   |   |           polygon-zkevm-adapter.test.js
|   |   |           range-cross-chain-adapter.test.js
|   |   |           README.md
|   |   |           relaychain-adapter.test.js
|   |   |           symbiosis-adapter.test.js
|   |   |           wormhole-adapter.test.js
|   |   |
|   |   +---compliance
|   |   |   |   adverse-media-scanner.js
|   |   |   |   blacklist-module.js
|   |   |   |   dispute-module.js
|   |   |   |   forensics-module.js
|   |   |   |   jurisdiction-manager.js
|   |   |   |   kyc-aml-module.js
|   |   |   |   pep-checker.js
|   |   |   |   permission-validator.js
|   |   |   |   rbac-enforcer.js
|   |   |   |   README.md
|   |   |   |   sanctions-checker.js
|   |   |   |   whitelist-module.js
|   |   |   |
|   |   |   +---docs
|   |   |   |       compliance-checks.md
|   |   |   |       forensics-guide.md
|   |   |   |       governance-controls.md
|   |   |   |       kyc-flows.md
|   |   |   |       README.md
|   |   |   |       sanctions-lists.md
|   |   |   |
|   |   |   \---tests
|   |   |           adverse-media-scanner.test.js
|   |   |           blacklist-module.test.js
|   |   |           dispute-module.test.js
|   |   |           forensics-module.test.js
|   |   |           jurisdiction-manager.test.js
|   |   |           kyc-aml-module.test.js
|   |   |           pep-checker.test.js
|   |   |           permission-validator.test.js
|   |   |           rbac-enforcer.test.js
|   |   |           README.md
|   |   |           sanctions-checker.test.js
|   |   |           whitelist-module.test.js
|   |   |
|   |   +---dex-adapters
|   |   |   |   aggregator-adapter.js
|   |   |   |   balancer-adapter.js
|   |   |   |   cowswap-adapter.js
|   |   |   |   curve-adapter.js
|   |   |   |   dodo-adapter.js
|   |   |   |   fraxswap-adapter.js
|   |   |   |   kyber-adapter.js
|   |   |   |   maverick-adapter.js
|   |   |   |   orca-adapter.js
|   |   |   |   pancake-adapter.js
|   |   |   |   quickswap-adapter.js
|   |   |   |   README.md
|   |   |   |   sushi-adapter.js
|   |   |   |   synthetix-adapter.js
|   |   |   |   thorchain-adapter.js
|   |   |   |   traderjoe-adapter.js
|   |   |   |   uniswap-v3-adapter.js
|   |   |   |   vertex-adapter.js
|   |   |   |   woofi-adapter.js
|   |   |   |
|   |   |   +---docs
|   |   |   |       adapter-development.md
|   |   |   |       dex-architecture.md
|   |   |   |       gas-optimizations.md
|   |   |   |       integration-guide.md
|   |   |   |       README.md
|   |   |   |       slippage-models.md
|   |   |   |       supported-dexes.md
|   |   |   |
|   |   |   \---tests
|   |   |           aggregator-adapter.test.js
|   |   |           balancer-adapter.test.js
|   |   |           cowswap-adapter.test.js
|   |   |           curve-adapter.test.js
|   |   |           dodo-adapter.test.js
|   |   |           fraxswap-adapter.test.js
|   |   |           kyber-adapter.test.js
|   |   |           maverick-adapter.test.js
|   |   |           orca-adapter.test.js
|   |   |           pancake-adapter.test.js
|   |   |           quickswap-adapter.test.js
|   |   |           README.md
|   |   |           sushi-adapter.test.js
|   |   |           synthetix-adapter.test.js
|   |   |           thorchain-adapter.test.js
|   |   |           traderjoe-adapter.test.js
|   |   |           uniswap-v3-adapter.test.js
|   |   |           vertex-adapter.test.js
|   |   |           woofi-adapter.test.js
|   |   |
|   |   +---docs
|   |   |       adapter-api.md
|   |   |       alpha-patterns.md
|   |   |       fork-testing-guide.md
|   |   |       integration-scenarios.md
|   |   |       mev-risk-mitigation.md
|   |   |       plugin-development.md
|   |   |       plugins-architecture.md
|   |   |       README.md
|   |   |       registry-guide.md
|   |   |       smart-contract-integration.md
|   |   |
|   |   +---flashloan
|   |   |   |   aave-adapter.js
|   |   |   |   angle-adapter.js
|   |   |   |   compound-adapter.js
|   |   |   |   cream-adapter.js
|   |   |   |   dydx-adapter.js
|   |   |   |   flashbots-adapter.js
|   |   |   |   gearbox-adapter.js
|   |   |   |   makerdao-adapter.js
|   |   |   |   morpho-adapter.js
|   |   |   |   parasite-arb-adapter.js
|   |   |   |   radiant-adapter.js
|   |   |   |   README.md
|   |   |   |   stargate-adapter.js
|   |   |   |
|   |   |   +---docs
|   |   |   |       audit-log.md
|   |   |   |       flashloan-architecture.md
|   |   |   |       flashloan-risks.md
|   |   |   |       provider-integrations.md
|   |   |   |       README.md
|   |   |   |       upgrade-guide.md
|   |   |   |
|   |   |   \---tests
|   |   |           aave-adapter.test.js
|   |   |           angle-adapter.test.js
|   |   |           compound-adapter.test.js
|   |   |           cream-adapter.test.js
|   |   |           dydx-adapter.test.js
|   |   |           flashbots-adapter.test.js
|   |   |           gearbox-adapter.test.js
|   |   |           makerdao-adapter.test.js
|   |   |           morpho-adapter.test.js
|   |   |           parasite-arb-adapter.test.js
|   |   |           radiant-adapter.test.js
|   |   |           README.md
|   |   |           stargate-adapter.test.js
|   |   |
|   |   +---insurance
|   |   |   |   claim-auditor.js
|   |   |   |   claim-verifier.js
|   |   |   |   coverage-oracle.js
|   |   |   |   incident-monitor.js
|   |   |   |   insurance-pool-manager.js
|   |   |   |   payout-calculator.js
|   |   |   |   premium-calculator.js
|   |   |   |   README.md
|   |   |   |   risk-assessment-plugin.js
|   |   |   |   risk-modeler.js
|   |   |   |
|   |   |   +---docs
|   |   |   |       claim-workflow.md
|   |   |   |       insurance-architecture.md
|   |   |   |       pool-audits.md
|   |   |   |       README.md
|   |   |   |       risk-assessment-methods.md
|   |   |   |       risk-models.md
|   |   |   |
|   |   |   \---tests
|   |   |           claim-auditor.test.js
|   |   |           claim-verifier.test.js
|   |   |           coverage-oracle.test.js
|   |   |           incident-monitor.test.js
|   |   |           insurance-pool-manager.test.js
|   |   |           payout-calculator.test.js
|   |   |           premium-calculator.test.js
|   |   |           README.md
|   |   |           risk-assessment-plugin.test.js
|   |   |           risk-modeler.test.js
|   |   |
|   |   +---intent-solvers
|   |   |   |   auction-intent-solver.js
|   |   |   |   batch-intent-processor.js
|   |   |   |   cow-intent-solver.js
|   |   |   |   eco-intent-solver.js
|   |   |   |   intent-forker.js
|   |   |   |   intent-merger.js
|   |   |   |   keepers-intent-solver.js
|   |   |   |   README.md
|   |   |   |   rfq-intent-solver.js
|   |   |   |   sandwich-intent-solver.js
|   |   |   |   sniper-intent-solver.js
|   |   |   |   uniswapx-intent-solver.js
|   |   |   |
|   |   |   +---docs
|   |   |   |       auction-design.md
|   |   |   |       eco-intents.md
|   |   |   |       intent-architecture.md
|   |   |   |       intent-merging.md
|   |   |   |       README.md
|   |   |   |
|   |   |   \---tests
|   |   |           auction-intent-solver.test.js
|   |   |           batch-intent-processor.test.js
|   |   |           cow-intent-solver.test.js
|   |   |           eco-intent-solver.test.js
|   |   |           intent-forker.test.js
|   |   |           intent-merger.test.js
|   |   |           keepers-intent-solver.test.js
|   |   |           README.md
|   |   |           rfq-intent-solver.test.js
|   |   |           sandwich-intent-solver.test.js
|   |   |           sniper-intent-solver.test.js
|   |   |           uniswapx-intent-solver.test.js
|   |   |
|   |   +---internal
|   |   |       interface-definitions.ts
|   |   |       migration-tool.js
|   |   |       plugin-manager.ts
|   |   |       plugin-utils.js
|   |   |       plugins.json
|   |   |       README.md
|   |   |       registry.ts
|   |   |       test-utils.js
|   |   |
|   |   +---marketplace
|   |   |       governance-marketplace.js
|   |   |       module-marketplace-registry.json
|   |   |       module-marketplace.js
|   |   |       plugin-marketplace-registry.json
|   |   |       plugin-marketplace.js
|   |   |       README.md
|   |   |
|   |   +---model-marketplace
|   |   |       ai-model-marketplace-registry.json
|   |   |       ai-model-marketplace.js
|   |   |       ai-model-metadata.json
|   |   |       ai-model-proxy.js
|   |   |       ai-model-validator.js
|   |   |       README.md
|   |   |
|   |   +---oracles
|   |   |   |   ai-oracle.js
|   |   |   |   chainlink-oracle.js
|   |   |   |   compliance-oracle.js
|   |   |   |   external-data-oracle.js
|   |   |   |   fallback-oracle.js
|   |   |   |   liquidity-oracle.js
|   |   |   |   onchain-oracle.js
|   |   |   |   README.md
|   |   |   |   time-weighted-oracle.js
|   |   |   |   volatility-oracle.js
|   |   |   |   zero-knowledge-oracle.js
|   |   |   |
|   |   |   +---docs
|   |   |   |       data-sources.md
|   |   |   |       oracle-integrations.md
|   |   |   |       README.md
|   |   |   |       risk-mitigation.md
|   |   |   |       zk-proofs.md
|   |   |   |
|   |   |   \---tests
|   |   |           ai-oracle.test.js
|   |   |           chainlink-oracle.test.js
|   |   |           compliance-oracle.test.js
|   |   |           external-data-oracle.test.js
|   |   |           fallback-oracle.test.js
|   |   |           liquidity-oracle.test.js
|   |   |           onchain-oracle.test.js
|   |   |           README.md
|   |   |           time-weighted-oracle.test.js
|   |   |           volatility-oracle.test.js
|   |   |           zero-knowledge-oracle.test.js
|   |   |
|   |   +---social-impact
|   |   |   |   carbon-offset-module.js
|   |   |   |   charity-oracle.js
|   |   |   |   csr-audit.js
|   |   |   |   donation-router.js
|   |   |   |   esg-allocator.js
|   |   |   |   grants-engine.js
|   |   |   |   green-bond-manager.js
|   |   |   |   impact-scoring.js
|   |   |   |   impact-voting.js
|   |   |   |   README.md
|   |   |   |
|   |   |   +---docs
|   |   |   |       charity-protocols.md
|   |   |   |       csr-programs.md
|   |   |   |       esg-logic.md
|   |   |   |       impact-scoring-models.md
|   |   |   |       README.md
|   |   |   |       social-impact-flows.md
|   |   |   |
|   |   |   \---tests
|   |   |           carbon-offset-module.test.js
|   |   |           charity-oracle.test.js
|   |   |           csr-audit.test.js
|   |   |           donation-router.test.js
|   |   |           esg-allocator.test.js
|   |   |           grants-engine.test.js
|   |   |           green-bond-manager.test.js
|   |   |           impact-scoring.test.js
|   |   |           impact-voting.test.js
|   |   |           README.md
|   |   |
|   |   +---template
|   |   |       adapter-template.js
|   |   |       model-template.js
|   |   |       plugin-template.js
|   |   |       README.md
|   |   |       template-config.json
|   |   |
|   |   \---tests
|   |           ai-model-marketplace.test.js
|   |           atomic-swap-batched.test.ts
|   |           bridge-latency-sniper.test.ts
|   |           flash-sandwich-mm.test.ts
|   |           governance-marketplace.test.js
|   |           hyper-bundle-engine.test.ts
|   |           micro-latency-arb-suite.test.ts
|   |           nft-gamefi-arb.test.ts
|   |           plugin-manager.test.js
|   |           plugins-integration.test.js
|   |           README.md
|   |           test-utils.js
|   |
|   +---research
|   |   |   ai-experiments.md
|   |   |   economic-module-report.md
|   |   |   experiment-index.md
|   |   |   explainability-report.md
|   |   |   innovation-log.md
|   |   |   quantum-research-notes.md
|   |   |   README.md
|   |   |   regulatory-mapping-exploration.md
|   |   |   swarm-learning-overview.md
|   |   |   threat-models-research.md
|   |   |
|   |   +---adversarial
|   |   |       adversarial-attacks.ipynb
|   |   |       ai-robustness-analysis.ipynb
|   |   |       cross-chain-sim-attack.ipynb
|   |   |       MEV-defender-test.ipynb
|   |   |       protocol-fuzz-testing.ipynb
|   |   |       README.md
|   |   |       recovery-strategies.ipynb
|   |   |
|   |   +---alphaNFT
|   |   |       alphaNFT-attack-defense.ipynb
|   |   |       alphaNFT-game-theory.ipynb
|   |   |       alphaNFT-minting-analysis.ipynb
|   |   |       alphaNFT-protocol-experiments.ipynb
|   |   |       operator-nft-governance.ipynb
|   |   |       README.md
|   |   |
|   |   +---demos
|   |   |       ai-interactive-sim.ipynb
|   |   |       contract-governance-demo.ipynb
|   |   |       dashboard-xai-demo.ipynb
|   |   |       failover-event-demo.ipynb
|   |   |       intent-arbitrage-demo.ipynb
|   |   |       plugin-hotload-demo.ipynb
|   |   |       README.md
|   |   |
|   |   +---economics
|   |   |       agent-incentives-model.ipynb
|   |   |       insurance-experiment.ipynb
|   |   |       liquidity-experiment.ipynb
|   |   |       market-simulation-study.ipynb
|   |   |       protocol-fee-analysis.ipynb
|   |   |       README.md
|   |   |       social-impact-analysis.ipynb
|   |   |
|   |   +---federated
|   |   |       attack-resilience-test.ipynb
|   |   |       federated-setup-demo.ipynb
|   |   |       incentive-alignment.ipynb
|   |   |       model-aggregation-experiments.ipynb
|   |   |       node-participation-metrics.ipynb
|   |   |       privacy-eval.ipynb
|   |   |       README.md
|   |   |
|   |   +---legacy
|   |   |       deprecated-research-log.md
|   |   |       legacy-economic-models.ipynb
|   |   |       legacy-experiment-index.md
|   |   |       old-xai-notebook.ipynb
|   |   |       README.md
|   |   |
|   |   +---quantum
|   |   |       quantum-bridge-sim.ipynb
|   |   |       quantum-experiment-notes.md
|   |   |       quantum-pool-defense.ipynb
|   |   |       quantum-rng-prototype.ipynb
|   |   |       quantum-xai-visual.ipynb
|   |   |       README.md
|   |   |
|   |   +---swarm
|   |   |       async-learning-demo.ipynb
|   |   |       chain-consensus-models.ipynb
|   |   |       model-update-broadcast.ipynb
|   |   |       README.md
|   |   |       swarm-node-behavior.ipynb
|   |   |
|   |   \---xai
|   |           ai-decision-graph.ipynb
|   |           live-explainability-case.ipynb
|   |           model-introspection-demo.ipynb
|   |           operator-interpretability.ipynb
|   |           README.md
|   |           xai-attack-defense.ipynb
|   |           xai-dashboard-demo.ipynb
|   |
|   +---storage
|   |   |   access-log.json
|   |   |   agent-metadata.json
|   |   |   backup-secrets.enc
|   |   |   keyvault.json
|   |   |   legacy-wallet.json
|   |   |   operator-nft-log.json
|   |   |   operator-nfts.json
|   |   |   README.md
|   |   |   validator-registry.json
|   |   |
|   |   +---ai-agent-memory
|   |   |   |   ai-session-context.json
|   |   |   |   memory-20250701.json
|   |   |   |   memory-20250715.json
|   |   |   |   memory-20250730.json
|   |   |   |   README.md
|   |   |   |
|   |   |   \---memory-checkpoints
|   |   |           checkpoint-1.json
|   |   |           checkpoint-2.json
|   |   |           checkpoint-3.json
|   |   |           README.md
|   |   |
|   |   +---ai-agent-snapshots
|   |   |   |   ai-agent-memory-v1.json
|   |   |   |   ai-agent-memory-v2.json
|   |   |   |   ai-agent-snapshot-20250701.json
|   |   |   |   ai-agent-snapshot-20250715.json
|   |   |   |   ai-agent-snapshot-20250730.json
|   |   |   |   README.md
|   |   |   |
|   |   |   \---ai-session-logs
|   |   |           README.md
|   |   |           session-log-20250701.json
|   |   |           session-log-20250715.json
|   |   |           session-log-20250730.json
|   |   |
|   |   +---api-auth
|   |   |       api-access-log.json
|   |   |       api-key-metadata.json
|   |   |       oauth-credentials.json
|   |   |       README.md
|   |   |       session-tokens-20250730.json
|   |   |
|   |   +---backup
|   |   |       ai-memory-backup-20250701.json
|   |   |       backup-20250701.zip
|   |   |       backup-20250715.zip
|   |   |       backup-20250730.zip
|   |   |       config-backup-20250701.json
|   |   |       contracts-backup-20250701.json
|   |   |       README.md
|   |   |
|   |   +---config-snapshots
|   |   |       config-20250701.json
|   |   |       config-20250715.json
|   |   |       config-20250730.json
|   |   |       config-latest.json
|   |   |       README.md
|   |   |
|   |   +---forensic-archive
|   |   |       ai-anomaly-logs.json
|   |   |       full-trace-20250730.json
|   |   |       incident-evidence-20250701.zip
|   |   |       incident-evidence-20250715.zip
|   |   |       incident-evidence-20250730.zip
|   |   |       README.md
|   |   |
|   |   +---keys
|   |   |       ai-agent-key.pem
|   |   |       encryption-key.pem
|   |   |       legacy-wallet.json
|   |   |       mnemonic.txt
|   |   |       operator-key.pem
|   |   |       README.md
|   |   |       signing-key.pem
|   |   |
|   |   +---model-weight-snapshots
|   |   |       ai-governance.weights
|   |   |       digital-twin.weights
|   |   |       federated.weights
|   |   |       README.md
|   |   |       scorer.weights
|   |   |       session-weights-20250701.json
|   |   |       session-weights-latest.json
|   |   |       volatility.weights
|   |   |
|   |   +---plugin-vaults
|   |   |       compliance-adapter-vault.json
|   |   |       dex-adapter-vault.json
|   |   |       flashloan-adapter-vault.json
|   |   |       oracle-adapter-vault.json
|   |   |       plugin-auth-metadata.json
|   |   |       README.md
|   |   |
|   |   +---recovery-playbooks
|   |   |       cold-storage-guide.md
|   |   |       incident-response.md
|   |   |       README.md
|   |   |       restore-procedure.md
|   |   |
|   |   +---snapshots
|   |   |       operator-balances-20250730.json
|   |   |       README.md
|   |   |       session-context-20250730.json
|   |   |       snapshot-20250701.json
|   |   |       snapshot-20250715.json
|   |   |       snapshot-20250730.json
|   |   |       snapshot-latest.json
|   |   |       wallet-balances-20250730.json
|   |   |
|   |   +---strat-archive
|   |   |       archived-strategies.md
|   |   |       legacy-strategy.json
|   |   |       README.md
|   |   |       strategy-metadata.json
|   |   |       strategy-v1.json
|   |   |       strategy-v2.json
|   |   |
|   |   \---test
|   |           ai-agent-memory.test.js
|   |           backup-restore.test.js
|   |           config-snapshots.test.js
|   |           keyvault-security.test.js
|   |           plugin-vaults.test.js
|   |           README.md
|   |           storage-access.test.js
|   |           strat-archive.test.js
|   |
|   +---tests
|   |   |   README.md
|   |   |
|   |   +---ai
|   |   |       ai-dashboard-integration.test.py
|   |   |       ai-module-smoke.test.py
|   |   |       alpha-score.test.py
|   |   |       profit-gradient.test.py
|   |   |       README.md
|   |   |       route-selection.test.py
|   |   |       volatility-model.test.py
|   |   |
|   |   +---chaos
|   |   |       incident-chaos.test.js
|   |   |       node-crash-recovery.test.js
|   |   |       README.md
|   |   |       system-chaos.test.js
|   |   |
|   |   +---contracts
|   |   |       alpha-nft.test.js
|   |   |       batch-executor.test.js
|   |   |       digital-twin-bridge.test.js
|   |   |       dispute-resolution.test.js
|   |   |       flashloan-arbitrage.test.js
|   |   |       governance-module.test.js
|   |   |       insurance-pool.test.js
|   |   |       intent-solver.test.js
|   |   |       operator-nft.test.js
|   |   |       README.md
|   |   |       reputation-oracle.test.js
|   |   |       upgradable-proxy.test.js
|   |   |       zk-proof.test.js
|   |   |
|   |   +---coverage
|   |   |   |   ai-coverage.test.py
|   |   |   |   backend-coverage.test.js
|   |   |   |   contracts-coverage.test.js
|   |   |   |   coverage-report.html
|   |   |   |   coverage-summary.md
|   |   |   |   README.md
|   |   |   |
|   |   |   \---.nyc_output
|   |   |           README.md
|   |   |
|   |   +---docs
|   |   |       ai-testing.md
|   |   |       chaos-testing.md
|   |   |       coverage-guide.md
|   |   |       fork-testing.md
|   |   |       legacy-cases.md
|   |   |       mainnet-e2e.md
|   |   |       README.md
|   |   |       snapshot-methods.md
|   |   |       test-strategy.md
|   |   |       test-troubleshooting.md
|   |   |
|   |   +---e2e
|   |   |       ai-e2e.test.py
|   |   |       dashboard-e2e.test.js
|   |   |       failover-e2e.test.js
|   |   |       mainnet-e2e.test.js
|   |   |       README.md
|   |   |
|   |   +---fork
|   |   |       block-drift-fork.test.js
|   |   |       mainnet-fork.test.js
|   |   |       mempool-chaos.test.js
|   |   |       README.md
|   |   |       zk-sim-fork.test.js
|   |   |
|   |   +---fuzz
|   |   |       ai-fuzz.test.py
|   |   |       fork-fuzz.test.js
|   |   |       fuzz-arb-paths.test.js
|   |   |       plugin-fuzz.test.js
|   |   |       README.md
|   |   |
|   |   +---integration
|   |   |       ai-integration.test.py
|   |   |       contracts-integration.test.js
|   |   |       engine-integration.test.js
|   |   |       overlays-integration.test.js
|   |   |       plugins-integration.test.js
|   |   |       README.md
|   |   |       storage-integration.test.js
|   |   |       utils-integration.test.js
|   |   |       watchdog-integration.test.js
|   |   |
|   |   +---legacy
|   |   |       legacy-tests-summary.md
|   |   |       migration-checks.test.js
|   |   |       README.md
|   |   |
|   |   +---migration
|   |   |       contract-migration.test.js
|   |   |       db-migration.test.js
|   |   |       plugin-migration.test.js
|   |   |       README.md
|   |   |
|   |   +---performance
|   |   |       ai-latency-benchmark.test.py
|   |   |       fork-benchmark.test.js
|   |   |       gas-benchmark.test.js
|   |   |       README.md
|   |   |
|   |   +---plugin
|   |   |       alpha-signal-plugins.test.js
|   |   |       bridge-adapters.test.js
|   |   |       compliance-plugins.test.js
|   |   |       dex-adapters.test.js
|   |   |       flashloan-adapters.test.js
|   |   |       insurance-plugins.test.js
|   |   |       intent-solvers.test.js
|   |   |       model-marketplace.test.js
|   |   |       oracles-adapters.test.js
|   |   |       plugin-marketplace.test.js
|   |   |       README.md
|   |   |       template-plugins.test.js
|   |   |
|   |   +---python
|   |   |       ai-agent-tests.py
|   |   |       legacy-ml-tests.py
|   |   |       model-integration-tests.py
|   |   |       README.md
|   |   |       strategy-selection-tests.py
|   |   |       token-score-tests.py
|   |   |
|   |   +---regression
|   |   |       failed-trade-replay.test.js
|   |   |       patch-regression.test.js
|   |   |       README.md
|   |   |       snapshot-regression.test.js
|   |   |       upgrade-regression.test.js
|   |   |
|   |   +---runner
|   |   |       foundry.toml
|   |   |       hardhat.config.js
|   |   |       pytest.ini
|   |   |       README.md
|   |   |       test-runner.config.js
|   |   |
|   |   +---snapshot
|   |   |       README.md
|   |   |       snapshot-audit.test.js
|   |   |       snapshot-compare.test.js
|   |   |
|   |   +---unit
|   |   |       ai-unit.test.py
|   |   |       contracts-unit.test.js
|   |   |       core-unit.test.js
|   |   |       engine-unit.test.js
|   |   |       overlays-unit.test.js
|   |   |       plugins-unit.test.js
|   |   |       README.md
|   |   |       storage-unit.test.js
|   |   |       utils-unit.test.js
|   |   |       watchdog-unit.test.js
|   |   |
|   |   \---utils
|   |           analytics-utils.test.js
|   |           api-rate-limiter-utils.test.js
|   |           arb-throttler-utils.test.js
|   |           bridge-utils.test.js
|   |           cache-manager-utils.test.js
|   |           digital-twin-utils.test.js
|   |           error-handler-utils.test.js
|   |           fee-estimator-utils.test.js
|   |           gas-profiler-utils.test.js
|   |           job-queue-utils.test.js
|   |           key-management-utils.test.js
|   |           latency-profiler-utils.test.js
|   |           log-rotator-utils.test.js
|   |           migration-helper-utils.test.js
|   |           nonce-safety-utils.test.js
|   |           privacy-zk-utils.test.js
|   |           profit-gradient-filter-utils.test.js
|   |           README.md
|   |           sim-result-compressor.test.js
|   |           simulation-utils.test.js
|   |           social-graph-utils.test.js
|   |           stateful-cache-utils.test.js
|   |           tx-bundle-utils.test.js
|   |           volatility-watchdog-utils.test.js
|   |
|   +---utils
|   |   |   ai-sandbox.js
|   |   |   analytics.js
|   |   |   api-rate-limiter.js
|   |   |   arb-throttler.js
|   |   |   bridge-utils.js
|   |   |   browser-tools.js
|   |   |   cache-manager.js
|   |   |   cli-utils.js
|   |   |   context-propagator.js
|   |   |   cryptography-utils.js
|   |   |   digital-twin.js
|   |   |   env-loader.js
|   |   |   error-handler.js
|   |   |   error-reporter.js
|   |   |   esg-impact-utils.js
|   |   |   fee-estimator.js
|   |   |   fork-sync-validator.js
|   |   |   gas-profiler.js
|   |   |   incident-helper.js
|   |   |   job-queue.js
|   |   |   json-schema-validator.js
|   |   |   key-management.js
|   |   |   latency-profiler.js
|   |   |   license-checker.js
|   |   |   log-rotator.js
|   |   |   migration-helper.js
|   |   |   nonce-safety.js
|   |   |   notification.js
|   |   |   plugin-loader.js
|   |   |   privacy-zk-utils.js
|   |   |   profit-gradient-filter.js
|   |   |   README.md
|   |   |   sim-result-compressor.js
|   |   |   simulation.js
|   |   |   snapshot-manager.js
|   |   |   social-graph-utils.js
|   |   |   stateful-cache.js
|   |   |   token-reputation-index.py
|   |   |   trade-history.js
|   |   |   tx-bundle-utils.js
|   |   |   volatility-watchdog.js
|   |   |   webhook-helper.js
|   |   |
|   |   +---docs
|   |   |       api-rate-limiter.md
|   |   |       error-handling.md
|   |   |       migration-helper-guide.md
|   |   |       plugin-loader-guide.md
|   |   |       privacy-zk-utils.md
|   |   |       README.md
|   |   |       snapshot-manager.md
|   |   |       usage-examples.md
|   |   |       utils-overview.md
|   |   |
|   |   \---test
|   |           ai-sandbox.test.js
|   |           analytics.test.js
|   |           browser-tools.test.js
|   |           cache-manager.test.js
|   |           digital-twin.test.js
|   |           error-handler.test.js
|   |           fee-estimator.test.js
|   |           job-queue.test.js
|   |           migration-helper.test.js
|   |           nonce-safety.test.js
|   |           privacy-zk-utils.test.js
|   |           README.md
|   |           simulation.test.js
|   |           token-reputation-index.test.py
|   |           webhook-helper.test.js
|   |
|   \---watchdog
|       |   auto-restart.js
|       |   block-watchdog.js
|       |   circuit-breaker.js
|       |   event-listener.js
|       |   failover-manager.js
|       |   gas-spike-watchdog.js
|       |   incident-response-core.js
|       |   mev-alerts.js
|       |   notification-manager.js
|       |   README.md
|       |   revert-reason-logger.js
|       |   risk-trigger-handler.js
|       |   threshold-config.json
|       |   trade-kill-switch.js
|       |   watchdog-daemon.js
|       |
|       +---data
|       |   |   event-history.log
|       |   |   health-metrics.json
|       |   |   last-restart.log
|       |   |   README.md
|       |   |   risk-alerts.json
|       |   |
|       |   \---incidents
|       |           incident-20250701.json
|       |           incident-20250715.json
|       |           incident-20250730.json
|       |           README.md
|       |
|       +---docs
|       |       failover-and-ha.md
|       |       forensics.md
|       |       incident-response-guide.md
|       |       notification-channels.md
|       |       README.md
|       |       testing-checklists.md
|       |       thresholds-and-tuning.md
|       |       watchdog-architecture.md
|       |
|       +---hooks
|       |       README.md
|       |       use-auto-recover.js
|       |       use-event-trigger.js
|       |       use-health-check.js
|       |       use-latency-monitor.js
|       |       use-risk-hook.js
|       |
|       +---tests
|       |   |   auto-restart.test.js
|       |   |   block-watchdog.test.js
|       |   |   circuit-breaker.test.js
|       |   |   event-listener.test.js
|       |   |   failover-manager.test.js
|       |   |   gas-spike-watchdog.test.js
|       |   |   incident-response-core.test.js
|       |   |   mev-alerts.test.js
|       |   |   notification-manager.test.js
|       |   |   README.md
|       |   |   revert-reason-logger.test.js
|       |   |   risk-trigger-handler.test.js
|       |   |   trade-kill-switch.test.js
|       |   |   watchdog-daemon.test.js
|       |   |
|       |   +---hooks
|       |   |       README.md
|       |   |       use-auto-recover.test.js
|       |   |       use-event-trigger.test.js
|       |   |       use-health-check.test.js
|       |   |       use-latency-monitor.test.js
|       |   |       use-risk-hook.test.js
|       |   |
|       |   \---utils
|       |           block-latency-calc.test.js
|       |           dashboard-sync.test.js
|       |           error-aggregator.test.js
|       |           health-score.test.js
|       |           incident-archive.test.js
|       |           notification-helper.test.js
|       |           persistent-state.test.js
|       |           README.md
|       |
|       \---utils
|               block-latency-calc.js
|               dashboard-sync.js
|               error-aggregator.js
|               health-score.js
|               incident-archive.js
|               notification-helper.js
|               persistent-state.js
|               README.md
|
+---benchmarks
|   |   benchmarks-config.json
|   |   benchmarks-notes.md
|   |   cpu-profile.log
|   |   mempool-bench.js
|   |   performance-matrix.md
|   |   profiling-report.md
|   |   quick-bench.js
|   |   README.md
|   |   results.csv
|   |   sample-batch.json
|   |   test-batch.js
|   |
|   +---ai
|   |       adversarial-ai-bench.py
|   |       ai-bench-compare.ipynb
|   |       ai-benchmark-methodology.md
|   |       ai-benchmark-results.csv
|   |       ai-benchmark-scenarios.md
|   |       ai-fork-bench.py
|   |       ai-inference-traces.log
|   |       ai-integration-bench.py
|   |       ai-memory-profile.json
|   |       ai-models-tested.md
|   |       ai-perf-metrics.json
|   |       ai-scalability-demo.ipynb
|   |       README.md
|   |
|   +---configs
|   |       ai-benchmark-config.json
|   |       cpu-benchmarks-config.json
|   |       gas-benchmark-config.json
|   |       latency-benchmarks-config.json
|   |       mempool-benchmark-config.json
|   |       plugins-bench-config.json
|   |       README.md
|   |       test-matrix-20250701.json
|   |       toolchain-config.json
|   |
|   +---cpu
|   |       ai-module-cpu-bench.py
|   |       core-engine-cpu-bench.js
|   |       cpu-baseline.json
|   |       cpu-benchmark-compare.ipynb
|   |       cpu-benchmark-results.csv
|   |       cpu-benchmarks.md
|   |       cpu-methodology.md
|   |       cpu-usage-traces.log
|   |       plugin-cpu-bench.js
|   |       README.md
|   |
|   +---datasets
|   |       ai-benchmark-set-20250715.csv
|   |       arbsim-batch-20250701.csv
|   |       benchmark-dataset-sample.csv
|   |       benchmark-output-sample.json
|   |       datasets-changelog.md
|   |       gas-batch-20250701.csv
|   |       gas-benchmark-set-20250701.csv
|   |       input-data-template.json
|   |       mempool-benchmark-set-20250701.csv
|   |       mempool-events-20250701.json
|   |       plugin-batch-20250701.csv
|   |       README.md
|   |       regression-batch-20250701.csv
|   |       test-batch-20250701.csv
|   |       test-data-20250701.csv
|   |       test-data-20250715.csv
|   |       test-data-20250730.csv
|   |
|   +---docs
|   |       README.md
|   |
|   +---gas
|   |       ai-gas-bench.py
|   |       contracts-gas-bench.js
|   |       gas-benchmark-compare.ipynb
|   |       gas-benchmark-methodology.md
|   |       gas-benchmark-results.csv
|   |       gas-benchmark-traces.log
|   |       gas-benchmark.md
|   |       gas-cost-analysis.json
|   |       plugin-gas-bench.js
|   |       README.md
|   |       routes-gas-bench.js
|   |
|   +---latency
|   |       ai-latency-bench.py
|   |       dashboard-latency-bench.js
|   |       latency-bench-compare.ipynb
|   |       latency-benchmark-methodology.md
|   |       latency-benchmarks.md
|   |       latency-profiles.log
|   |       latency-results.csv
|   |       network-latency-bench.js
|   |       plugin-latency-bench.js
|   |       README.md
|   |
|   +---mempool
|   |       block-reorg-events.log
|   |       mempool-benchmark-methodology.md
|   |       mempool-benchmark-results.csv
|   |       mempool-heatmap.png
|   |       mempool-profiling.md
|   |       mempool-tx-samples.json
|   |       mev-frontrun-sim.js
|   |       node-mempool-compare.ipynb
|   |       README.md
|   |       relayer-latency-bench.js
|   |
|   +---regression
|   |       README.md
|   |
|   +---results
|   |       20250701-ai-vs-core.csv
|   |       20250701-ai-vs-core.md
|   |       20250701-benchmark-data.csv
|   |       20250701-benchmark-report.md
|   |       20250701-gas-vs-mempool.csv
|   |       20250701-gas-vs-mempool.md
|   |       20250701-latency-vs-plugin.csv
|   |       20250701-latency-vs-plugin.md
|   |       20250715-benchmark-data.csv
|   |       20250715-benchmark-report.md
|   |       20250730-benchmark-data.csv
|   |       20250730-benchmark-report.md
|   |       README.md
|   |       results-changelog.md
|   |
|   \---tools
|           bench-analyze.py
|           bench-cleanup.py
|           bench-config.json
|           bench-docs-export.sh
|           bench-mock-data-gen.py
|           bench-runner.js
|           bench-sample-script.sh
|           bench-toolkit.md
|           plot-benchmarks.ipynb
|           README.md
|           tool-release-notes.md
|
+---ci
|   |   .env.example
|   |   ci-config.json
|   |   ci-helpers.sh
|   |   ci-notes.md
|   |   ci-settings.json
|   |   ci-setup.ps1
|   |   common.sh
|   |   migration-history.md
|   |   README.md
|   |   tree_structure.txt
|   |
|   +---badges
|   |       ai-status.svg
|   |       ci-status.svg
|   |       contracts-status.svg
|   |       coverage.svg
|   |       dashboard-status.svg
|   |       e2e.svg
|   |       fork-smoke.svg
|   |       lint.svg
|   |       README.md
|   |       security-audit.svg
|   |
|   +---buildkite
|   |   |   pipeline.yml
|   |   |   README.md
|   |   |
|   |   +---agent-hooks
|   |   |       environment
|   |   |       post-command
|   |   |       pre-command
|   |   |       README.md
|   |   |
|   |   \---scripts
|   |           ai-bench.sh
|   |           badge-update.sh
|   |           build-image.sh
|   |           deploy.sh
|   |           notify-slack.sh
|   |           README.md
|   |           run-e2e.sh
|   |
|   +---circleci
|   |   |   config.yml
|   |   |   README.md
|   |   |
|   |   \---scripts
|   |           badge-update.sh
|   |           deploy.sh
|   |           install-deps.sh
|   |           notify-discord.sh
|   |           README.md
|   |           run-tests.sh
|   |
|   +---config
|   |       .secrets.example
|   |       ai.env.template
|   |       buildkite.env
|   |       ci.env.template
|   |       docker-compose.ci.yml
|   |       prod.env.template
|   |       README.md
|   |       staging.env.template
|   |       test.env.template
|   |       workflows.env
|   |
|   +---github
|   |   |   CODEOWNERS
|   |   |   dependabot.yml
|   |   |   issue-template.md
|   |   |   pr-template.md
|   |   |   README.md
|   |   |
|   |   \---actions
|   |           cache-hardhat-node.yml
|   |           deploy-contract-action.yml
|   |           notify-discord-action.yml
|   |           README.md
|   |           run-ai-inference-action.yml
|   |           setup-docker-action.yml
|   |           shared-env-vars.yml
|   |           upload-artifact-action.yml
|   |
|   +---gitlab
|   |   |   .gitlab-ci.yml
|   |   |   ai-train.gitlab-ci.yml
|   |   |   contract-deploy.gitlab-ci.yml
|   |   |   env.template
|   |   |   README.md
|   |   |
|   |   \---scripts
|   |           ai-bench.py
|   |           build.sh
|   |           coverage.sh
|   |           deploy.sh
|   |           lint.sh
|   |           notify.sh
|   |           patch-release.sh
|   |           README.md
|   |           test.sh
|   |
|   +---jenkins
|   |   |   credentials.xml
|   |   |   Jenkinsfile
|   |   |   Jenkinsfile.contracts
|   |   |   Jenkinsfile.deploy
|   |   |   README.md
|   |   |
|   |   +---pipeline-libs
|   |   |       ai-utils.groovy
|   |   |       notifications.groovy
|   |   |       README.md
|   |   |       shared-library.groovy
|   |   |
|   |   \---scripts
|   |           build-docker.sh
|   |           deploy-contracts.sh
|   |           lint.sh
|   |           notify-discord.groovy
|   |           notify-slack.groovy
|   |           notify-telegram.groovy
|   |           post-cleanup.groovy
|   |           README.md
|   |           run-ai-bench.py
|   |           run-tests.sh
|   |
|   +---legacy
|   |   |   ci-migration-notes.md
|   |   |   deprecated-gitlab-ci.yml
|   |   |   old-github-actions.yml
|   |   |   old-jenkinsfile
|   |   |   README.md
|   |   |
|   |   +---backup-pipelines
|   |   |       pipeline-2023.yml
|   |   |       pipeline-2024.yml
|   |   |       README.md
|   |   |
|   |   \---old-circleci
|   |           config-old.yml
|   |           README.md
|   |
|   +---notifications
|   |       discord-webhook.json
|   |       email-config.json
|   |       incident-alerts.json
|   |       opsgenie.json
|   |       pagerduty.json
|   |       README.md
|   |       slack-webhook.json
|   |       telegram.json
|   |       webhook-configs.json
|   |
|   +---scripts
|   |       ci-check-pr-labels.js
|   |       cleanup.sh
|   |       coverage.sh
|   |       deploy-all.sh
|   |       docker-cleanup.sh
|   |       env-diff.sh
|   |       fetch-artifacts.sh
|   |       install-deps.sh
|   |       lint-all.sh
|   |       merge-bot.sh
|   |       notify.sh
|   |       postbuild.sh
|   |       prebuild.sh
|   |       README.md
|   |       rollback.sh
|   |       run-badge-update.sh
|   |       secrets-loader.sh
|   |       setup-env.sh
|   |       test-all.sh
|   |
|   \---workflows
|           ai-deploy.yml
|           ai-tests.yml
|           audit.yml
|           cd.yml
|           ci.yml
|           codeql-analysis.yml
|           contracts-deploy.yml
|           contracts-test.yml
|           coverage.yml
|           dashboard-build.yml
|           dashboard-preview.yml
|           e2e.yml
|           fork-smoke.yml
|           lint.yml
|           mainnet-fork.yml
|           notify.yml
|           oracle-adapters.yml
|           patch-deploy.yml
|           plugin-marketplace.yml
|           README.md
|           regression.yml
|           release-tag.yml
|           test.yml
|
+---config
|   |   .env.example
|   |   agent-compatibility.json
|   |   audit-policy.json
|   |   config-docs.md
|   |   config-manifest.json
|   |   config-schema.json
|   |   config-schema.yaml
|   |   cross-ref.json
|   |   defaults.env
|   |   defaults.json
|   |   example.env
|   |   explainability-rules.yaml
|   |   gdpr-map.json
|   |   hotload-params.json
|   |   kyc-policy.json
|   |   README-bot-ops.md
|   |   README.md
|   |   roles.json
|   |   vault-ref.json
|   |   xai-params.json
|   |
|   +---.meta
|   |       README.md
|   |
|   +---ai
|   |       .meta
|   |       ai-ablation-matrix.json
|   |       ai-config.json
|   |       ai-feature-engineering.json
|   |       ai-pipeline-config.json
|   |       ai-scorer-config.json
|   |       ai-test-scenarios.json
|   |       ai-thresholds.json
|   |       ai-weights.json
|   |       README.md
|   |       retrain-policy.json
|   |
|   +---analytics
|   |       analytics-config.json
|   |       custom-metrics.json
|   |       dashboard-example.json
|   |       data-sources.json
|   |       event-hooks.json
|   |       README.md
|   |       trade-log-template.json
|   |
|   +---api-snapshots
|   |       README.md
|   |
|   +---chains
|   |       arbitrum.json
|   |       avalanche.json
|   |       bsc.json
|   |       chain-aliases.json
|   |       chains.json
|   |       chains.schema.json
|   |       ethereum.json
|   |       explorer-templates.json
|   |       optimism.json
|   |       polygon.json
|   |       README.md
|   |       rpc-endpoints.json
|   |       testnets.json
|   |
|   +---compliance
|   |       audit-rules.json
|   |       blacklisted-addresses.json
|   |       compliance-policies.json
|   |       jurisdiction-rules.json
|   |       monitoring.json
|   |       README.md
|   |       sanctions-list.json
|   |       whitelist.json
|   |
|   +---custom
|   |       README.md
|   |
|   +---dao
|   |       dao-core.json
|   |       dao-gov-rules.json
|   |       proposal-templates.json
|   |       README.md
|   |       roles.json
|   |       treasury-config.json
|   |       voting-strategy.json
|   |
|   +---dashboards
|   |       alerts.json
|   |       dashboard-presets.json
|   |       dashboard-roles.json
|   |       dashboards.json
|   |       demo-dashboard.json
|   |       panel-layouts.json
|   |       README.md
|   |       stats-widgets.json
|   |
|   +---deprecated
|   |       README.md
|   |
|   +---dexes
|   |       adapters.json
|   |       dex-abi-templates.json
|   |       dex-examples.json
|   |       dex-fee-params.json
|   |       dexes.json
|   |       pools.json
|   |       README.md
|   |       routers.json
|   |
|   +---digital-twin
|   |       chain-fork-templates.json
|   |       digital-twin-schema.json
|   |       preset-scenarios.json
|   |       README.md
|   |       simulation-config.json
|   |       twin-overrides.json
|   |
|   +---examples
|   |       ai-example.json
|   |       all-in-one-demo-config.json
|   |       analytics-example.json
|   |       chain-example.json
|   |       compliance-example.json
|   |       dao-example.json
|   |       dashboard-example.json
|   |       dex-example.json
|   |       digital-twin-example.json
|   |       insurance-example.json
|   |       notifications-example.json
|   |       README.md
|   |       risk-example.json
|   |       strat-example.json
|   |       tokens-example.json
|   |       versioning-example.json
|   |
|   +---insurance
|   |       collateral-config.json
|   |       coverage-rules.json
|   |       insurance-policies.json
|   |       insurance-providers.json
|   |       payout-logic.json
|   |       pricing-models.json
|   |       README.md
|   |
|   +---legacy
|   |       README.md
|   |
|   +---locales
|   |       README.md
|   |
|   +---migrations
|   |       README.md
|   |
|   +---notifications
|   |       alert-message-templates.json
|   |       escalation-policy.json
|   |       notification-providers.json
|   |       notification-routing.json
|   |       notification-thresholds.json
|   |       provider-integrations.json
|   |       README.md
|   |
|   +---overrides
|   |   |   README.md
|   |   |
|   |   +---dev
|   |   |       README.md
|   |   |
|   |   +---prod
|   |   |       README.md
|   |   |
|   |   +---staging
|   |   |       README.md
|   |   |
|   |   \---test
|   |           README.md
|   |
|   +---presets
|   |       ai-demo.json
|   |       ai-presets.json
|   |       compliance-demo.json
|   |       dashboards.json
|   |       digital-twin-presets.json
|   |       mainnet.json
|   |       README.md
|   |       strat-arb-batch-demo.json
|   |       testnet.json
|   |       user-quickstart.json
|   |
|   +---quickstart
|   |       README.md
|   |
|   +---risk
|   |       blacklist.json
|   |       liquidation-rules.json
|   |       README.md
|   |       risk-audit-log.json
|   |       risk-profiles.json
|   |       risk-thresholds.json
|   |       stress-test.json
|   |
|   +---runtime-patches
|   |       README.md
|   |
|   +---sample-templates
|   |       README.md
|   |
|   +---schema
|   |       README.md
|   |
|   +---secrets
|   |       README.md
|   |
|   +---strategies
|   |   |   arbitrage.json
|   |   |   liquidity.json
|   |   |   README.md
|   |   |   sandwich.json
|   |   |   stablecoin.json
|   |   |   strategy-schema.json
|   |   |
|   |   \---examples
|   |           demo-liquidity-strategy.json
|   |           example-arb-mainnet.json
|   |           example-arb-testnet.json
|   |           README.md
|   |
|   +---tokens
|   |       legacy-tokens.json
|   |       README.md
|   |       test-tokens.json
|   |       token-metadata.json
|   |       token-symbols.csv
|   |       tokens.json
|   |       tokens.schema.json
|   |
|   \---versioning
|           config-changelog.json
|           README.md
|           rollback.json
|           schema-migration-log.json
|           version-history.json
|
+---dashboard
|   |   README.md
|   |
|   +---admin
|   |       README.md
|   |
|   +---ai
|   |   |   ai-manifest.json
|   |   |   CHANGELOG.md
|   |   |   index.js
|   |   |   README.md
|   |   |
|   |   +---automation
|   |   |       AIAutoPilotPanel.jsx
|   |   |       AIBatchRunner.js
|   |   |       automation-demo.json
|   |   |       AutomationLogs.json
|   |   |       AutoStrategySelector.js
|   |   |       OperatorOverrideToggle.jsx
|   |   |       README.md
|   |   |
|   |   +---chat
|   |   |       AIChatUtils.js
|   |   |       ChatFeedbackPanel.jsx
|   |   |       ChatHistoryStore.js
|   |   |       ChatOperatorLog.json
|   |   |       LLMChatEngine.js
|   |   |       PromptTemplates.json
|   |   |       README.md
|   |   |
|   |   +---components
|   |   |       AIInsightWidget.jsx
|   |   |       AITradeScorer.jsx
|   |   |       AutomationToggle.jsx
|   |   |       DecisionPathCard.jsx
|   |   |       FeatureAttributionCard.jsx
|   |   |       FeedbackPanel.jsx
|   |   |       LLMChatBox.jsx
|   |   |       ModelAuditLogPanel.jsx
|   |   |       ModelStatusChip.jsx
|   |   |       ModelSwitcher.jsx
|   |   |       OperatorAIFeedbackPanel.jsx
|   |   |       README.md
|   |   |       ScoreKPIBlock.jsx
|   |   |       XAIHeatmapOverlay.jsx
|   |   |
|   |   +---config
|   |   |       ai-dashboard-config.json
|   |   |       ai-presets.json
|   |   |       chat-settings.json
|   |   |       feedback-config.json
|   |   |       model-switcher-presets.json
|   |   |       README.md
|   |   |       xai-overlays.json
|   |   |
|   |   +---demo
|   |   |       ai-dashboard-tour.md
|   |   |       ai-insight-demo.json
|   |   |       chat-demo.json
|   |   |       feedback-demo.json
|   |   |       README.md
|   |   |       xai-demo.json
|   |   |
|   |   +---explainability
|   |   |       ExplainabilityHistory.json
|   |   |       ExplainabilityUtils.js
|   |   |       FeatureImportanceChart.jsx
|   |   |       GlobalXAIStatsWidget.jsx
|   |   |       README.md
|   |   |       SaliencyMapPanel.jsx
|   |   |       xai-demo-data.json
|   |   |       XAIIncidentExplorer.jsx
|   |   |       XAIOverviewModal.jsx
|   |   |
|   |   +---feedback
|   |   |       feedback-demo.json
|   |   |       FeedbackAPI.js
|   |   |       FeedbackHistoryTable.jsx
|   |   |       FeedbackPanel.jsx
|   |   |       FeedbackSchema.json
|   |   |       README.md
|   |   |
|   |   +---hooks
|   |   |       README.md
|   |   |       useAIAutoPilot.js
|   |   |       useAIFeedback.js
|   |   |       useAIModel.js
|   |   |       useAIOperatorMode.js
|   |   |       useAIScoring.js
|   |   |       useLLMChat.js
|   |   |       useXAI.js
|   |   |
|   |   +---models
|   |   |   |   ai-models-list.json
|   |   |   |   default-model-config.json
|   |   |   |   model-audit-log.json
|   |   |   |   model-metadata.json
|   |   |   |   README.md
|   |   |   |
|   |   |   \---weights
|   |   |       |   ai-arb-v5.onnx
|   |   |       |   pattern-learner-v3.pt
|   |   |       |   README.md
|   |   |       |   xai-embedder-v1.bin
|   |   |       |
|   |   |       \---old-weights
|   |   |               ai-arb-v3.pt
|   |   |               ai-arb-v4.onnx
|   |   |               README.md
|   |   |
|   |   +---presets
|   |   |       ai-theme-presets.json
|   |   |       explainability-presets.json
|   |   |       model-switcher-presets.json
|   |   |       README.md
|   |   |
|   |   +---scoring
|   |   |       AIPredictionTable.jsx
|   |   |       AIScoreEngine.js
|   |   |       README.md
|   |   |       score-demo.json
|   |   |       ScoreEventLog.json
|   |   |       ScoreHeatmapPanel.jsx
|   |   |       ScorePresetConfig.json
|   |   |       ScoringUtils.js
|   |   |
|   |   +---tests
|   |   |       aiModelSelect.test.js
|   |   |       automationMode.test.js
|   |   |       FeedbackPanel.test.js
|   |   |       LLMChatPanel.test.js
|   |   |       OperatorAIFeedbackPanel.test.js
|   |   |       README.md
|   |   |       XAIWidget.test.js
|   |   |
|   |   \---utils
|   |           aiApiClient.js
|   |           aiDataAdapters.js
|   |           aiFileUtils.js
|   |           aiFormatters.js
|   |           aiMetrics.js
|   |           aiValidator.js
|   |           README.md
|   |
|   +---analytics
|   |   |   CHANGELOG.md
|   |   |   README.md
|   |   |
|   |   +---ai
|   |   |       ai-demo-results.json
|   |   |       AIDashboardAdapter.js
|   |   |       AIProfitPredictor.js
|   |   |       AnalyticsAIMetrics.jsx
|   |   |       LatencyAnomalyAI.js
|   |   |       OutlierDetectorAI.js
|   |   |       README.md
|   |   |       RegressionTrainer.js
|   |   |
|   |   +---charts
|   |   |       AnalyticsChartUtils.js
|   |   |       AnomalyScatterPlot.jsx
|   |   |       AreaChart.jsx
|   |   |       CandlestickChart.jsx
|   |   |       LineChart.jsx
|   |   |       OrderbookDepthChart.jsx
|   |   |       PieChart.jsx
|   |   |       README.md
|   |   |
|   |   +---components
|   |   |       AnalyticsAlertBanner.jsx
|   |   |       AnalyticsDashboard.jsx
|   |   |       GasCostChart.jsx
|   |   |       LatencyStatsPanel.jsx
|   |   |       OperatorStatsPanel.jsx
|   |   |       OutlierDetectionWidget.jsx
|   |   |       PerformanceBreakdown.jsx
|   |   |       PnLChart.jsx
|   |   |       README.md
|   |   |       RiskProfileChart.jsx
|   |   |       ROIHeatmap.jsx
|   |   |       TradeMetricsTable.jsx
|   |   |       VolumeTimeSeries.jsx
|   |   |
|   |   +---config
|   |   |       ai-analytics-presets.json
|   |   |       analytics-layout.json
|   |   |       anomaly-detection-config.json
|   |   |       custom-widgets-presets.json
|   |   |       dashboard-metrics.json
|   |   |       kpi-config.json
|   |   |       operator-view-presets.json
|   |   |       README.md
|   |   |       regression-settings.json
|   |   |       risk-indicators.json
|   |   |       theme-presets.json
|   |   |       timeseries-source.json
|   |   |
|   |   +---data
|   |   |       demo-anomalies.json
|   |   |       demo-gas-costs.csv
|   |   |       demo-pnl-data.csv
|   |   |       demo-trade-metrics.csv
|   |   |       outlier-events.csv
|   |   |       README.md
|   |   |       time-series-sample.csv
|   |   |
|   |   +---explainability
|   |   |       AnalyticsXAIOverlay.jsx
|   |   |       AnomalyExplanationPanel.jsx
|   |   |       explainability-config.json
|   |   |       README.md
|   |   |       RegressionExplainPanel.jsx
|   |   |
|   |   +---hooks
|   |   |       README.md
|   |   |       useAnalyticsData.js
|   |   |       useAnomalyScan.js
|   |   |       useArbStats.js
|   |   |       useGasTrends.js
|   |   |       useLatencyStats.js
|   |   |       useLivePnL.js
|   |   |       useVolumeTimeseries.js
|   |   |
|   |   +---integration
|   |   |       AnalyticsAPI.js
|   |   |       analyticsDataClient.js
|   |   |       AnalyticsWS.js
|   |   |       README.md
|   |   |       syncConfig.json
|   |   |       useAnalyticsSocket.js
|   |   |
|   |   +---pages
|   |   |       dashboard.js
|   |   |       gas-cost.js
|   |   |       pnl.js
|   |   |       README.md
|   |   |       regression.js
|   |   |       risk.js
|   |   |       roi.js
|   |   |       time-series.js
|   |   |       trade-metrics.js
|   |   |
|   |   +---panels
|   |   |       MainAnalyticsPanel.jsx
|   |   |       OperatorPerformancePanel.jsx
|   |   |       ProfitRegressionPanel.jsx
|   |   |       README.md
|   |   |       RiskAndROIOverview.jsx
|   |   |       TimeSeriesExplorerPanel.jsx
|   |   |       VolumeVsGasPanel.jsx
|   |   |
|   |   +---reports
|   |   |       custom-user-report-sample.pdf
|   |   |       daily-report-20250730.pdf
|   |   |       gas-analysis-report-20250701.csv
|   |   |       profit-loss-report-20250710.csv
|   |   |       README.md
|   |   |       regression-report-20250715.csv
|   |   |
|   |   +---state
|   |   |       analyticsPersistence.js
|   |   |       analyticsSelectors.js
|   |   |       analyticsStore.js
|   |   |       README.md
|   |   |
|   |   +---tests
|   |   |       AnalyticsAIMetrics.test.js
|   |   |       AnalyticsAPI.test.js
|   |   |       AnalyticsDashboard.test.js
|   |   |       GasCostChart.test.js
|   |   |       LatencyStatsPanel.test.js
|   |   |       OutlierDetectionWidget.test.js
|   |   |       README.md
|   |   |       ROIHeatmap.test.js
|   |   |       TradeMetricsTable.test.js
|   |   |
|   |   +---utils
|   |   |       anomalyUtils.js
|   |   |       calcROI.js
|   |   |       formatTradeData.js
|   |   |       kpiFormatters.js
|   |   |       pnlUtils.js
|   |   |       README.md
|   |   |       regressionUtils.js
|   |   |       timeSeriesUtils.js
|   |   |
|   |   \---widgets
|   |           ActiveRouteWidget.jsx
|   |           ArbitrageScoreWidget.jsx
|   |           GasTrendWidget.jsx
|   |           LatencyIndicatorWidget.jsx
|   |           LiveVolumeSparkline.jsx
|   |           MiniPnLWidget.jsx
|   |           README.md
|   |           TradeCountWidget.jsx
|   |
|   +---api
|   |   |   ai.js
|   |   |   arb.js
|   |   |   CHANGELOG.md
|   |   |   dev.js
|   |   |   extension.js
|   |   |   health.js
|   |   |   index.js
|   |   |   metrics.js
|   |   |   notifications.js
|   |   |   plugin.js
|   |   |   README.md
|   |   |   user.js
|   |   |   webhook.js
|   |   |
|   |   +---docs
|   |   |       api-error-codes.md
|   |   |       api-versioning.md
|   |   |       auth.md
|   |   |       integration.md
|   |   |       multi-tenancy.md
|   |   |       README.md
|   |   |       routes.md
|   |   |       schemas.md
|   |   |       sockets.md
|   |   |       update-history.md
|   |   |       webhooks.md
|   |   |
|   |   +---integration
|   |   |       aiAdapter.js
|   |   |       analyticsAdapter.js
|   |   |       backendAdapter.js
|   |   |       configAdapter.js
|   |   |       metricsAdapter.js
|   |   |       multiTenantAdapter.js
|   |   |       notificationAdapter.js
|   |   |       operatorAdapter.js
|   |   |       pluginAdapter.js
|   |   |       README.md
|   |   |       riskAdapter.js
|   |   |       sandboxAdapter.js
|   |   |       uploadAdapter.js
|   |   |       wsAdapter.js
|   |   |
|   |   +---middleware
|   |   |       analyticsThrottle.js
|   |   |       auth.js
|   |   |       cors.js
|   |   |       csrf.js
|   |   |       errorHandler.js
|   |   |       logger.js
|   |   |       multiTenantGuard.js
|   |   |       operatorGuard.js
|   |   |       rateLimit.js
|   |   |       README.md
|   |   |       validate.js
|   |   |
|   |   +---routes
|   |   |   |   ai.js
|   |   |   |   alerts.js
|   |   |   |   analytics.js
|   |   |   |   config.js
|   |   |   |   gas.js
|   |   |   |   graphql.js
|   |   |   |   health.js
|   |   |   |   index.js
|   |   |   |   metrics.js
|   |   |   |   multi-tenant.js
|   |   |   |   notifications.js
|   |   |   |   operator.js
|   |   |   |   overlays.js
|   |   |   |   plugins.js
|   |   |   |   pnl.js
|   |   |   |   presets.js
|   |   |   |   README.md
|   |   |   |   risk.js
|   |   |   |   sandbox.js
|   |   |   |   session.js
|   |   |   |   status.js
|   |   |   |   trades.js
|   |   |   |   uploads.js
|   |   |   |   user.js
|   |   |   |   websocket.js
|   |   |   |   xai.js
|   |   |   |
|   |   |   \---__mocks__
|   |   |           ai-inference.json
|   |   |           analytics.json
|   |   |           config.json
|   |   |           health.json
|   |   |           notifications.json
|   |   |           operator.json
|   |   |           overlays.json
|   |   |           presets.json
|   |   |           README.md
|   |   |           session.json
|   |   |           trades.json
|   |   |           user.json
|   |   |
|   |   +---schemas
|   |   |       ai-inference.schema.json
|   |   |       analytics.schema.json
|   |   |       config.schema.json
|   |   |       notification.schema.json
|   |   |       openapi.yaml
|   |   |       operator.schema.json
|   |   |       overlays.schema.json
|   |   |       plugin.schema.json
|   |   |       presets.schema.json
|   |   |       README.md
|   |   |       session.schema.json
|   |   |       trade.schema.json
|   |   |       upload.schema.json
|   |   |       user.schema.json
|   |   |       websocket.schema.json
|   |   |
|   |   +---sockets
|   |   |       ai-socket.js
|   |   |       alerts-socket.js
|   |   |       analytics-socket.js
|   |   |       config-socket.js
|   |   |       notification-socket.js
|   |   |       operator-socket.js
|   |   |       overlays-socket.js
|   |   |       plugin-socket.js
|   |   |       README.md
|   |   |       trade-socket.js
|   |   |       user-socket.js
|   |   |
|   |   +---tests
|   |   |   |   api-ai.test.js
|   |   |   |   api-analytics.test.js
|   |   |   |   api-config.test.js
|   |   |   |   api-error.test.js
|   |   |   |   api-health.test.js
|   |   |   |   api-metrics.test.js
|   |   |   |   api-multi-tenant.test.js
|   |   |   |   api-notifications.test.js
|   |   |   |   api-operator.test.js
|   |   |   |   api-presets.test.js
|   |   |   |   api-routes.test.js
|   |   |   |   api-sandbox.test.js
|   |   |   |   api-session.test.js
|   |   |   |   api-status.test.js
|   |   |   |   api-trades.test.js
|   |   |   |   api-uploads.test.js
|   |   |   |   api-websocket.test.js
|   |   |   |   api-xai.test.js
|   |   |   |   README.md
|   |   |   |
|   |   |   \---__mocks__
|   |   |           aiMock.js
|   |   |           analyticsMock.js
|   |   |           README.md
|   |   |           userSessionMock.js
|   |   |
|   |   \---utils
|   |           apiErrorCodes.js
|   |           apiMockUtils.js
|   |           apiResponse.js
|   |           parseQuery.js
|   |           queryValidator.js
|   |           rateLimiter.js
|   |           README.md
|   |           testUtils.js
|   |           uploadUtils.js
|   |           validateSchema.js
|   |           websocketUtils.js
|   |
|   +---ar
|   |   |   CHANGELOG.md
|   |   |   README.md
|   |   |
|   |   +---components
|   |   |       ARActionPromptPanel.jsx
|   |   |       ARCameraStreamView.jsx
|   |   |       ARConfigPanel.jsx
|   |   |       ARDashboardMenu.jsx
|   |   |       ARFeatureAttributionMap.jsx
|   |   |       ARGasPriceMeter.jsx
|   |   |       ARIncidentFeed.jsx
|   |   |       ARLatencyStatusWidget.jsx
|   |   |       ARLivePoolWidget.jsx
|   |   |       AROperatorCommandPanel.jsx
|   |   |       AROrderbook3D.jsx
|   |   |       AROverlayToggle.jsx
|   |   |       ARPnLHeatmap3D.jsx
|   |   |       ARRiskAlertOverlay.jsx
|   |   |       ARXAIInsightPanel.jsx
|   |   |       README.md
|   |   |
|   |   +---config
|   |   |       ar-context-presets.json
|   |   |       ar-device-mapping.json
|   |   |       ar-operator-presets.json
|   |   |       ar-overlays.json
|   |   |       ar-theme-presets.json
|   |   |       README.md
|   |   |
|   |   +---context
|   |   |       ARDeviceContext.js
|   |   |       AROverlayContext.js
|   |   |       ARPermissionContext.js
|   |   |       ARSessionContext.js
|   |   |       README.md
|   |   |
|   |   +---fixtures
|   |   |       ar-incident-demo.json
|   |   |       demo-ar-overlays.json
|   |   |       live-pool-demo.json
|   |   |       README.md
|   |   |       xr-demo-assets.json
|   |   |
|   |   +---hooks
|   |   |       README.md
|   |   |       useARCameraStream.js
|   |   |       useARIncidentFeed.js
|   |   |       useAROperatorMode.js
|   |   |       useAROverlay.js
|   |   |       useARSession.js
|   |   |       useXRScene.js
|   |   |
|   |   +---integration
|   |   |       ARBackendAdapter.js
|   |   |       ARIncidentFeedAdapter.js
|   |   |       ARLiveFeedAdapter.js
|   |   |       ARWebSocketAdapter.js
|   |   |       ARXAIAdapter.js
|   |   |       integration-config.json
|   |   |       README.md
|   |   |
|   |   +---modals
|   |   |       ARIncidentDetailModal.jsx
|   |   |       ARPermissionModal.jsx
|   |   |       ARSettingsModal.jsx
|   |   |       ARXAIExplainModal.jsx
|   |   |       README.md
|   |   |
|   |   +---overlays
|   |   |       ARAlertBannerOverlay.jsx
|   |   |       ARIncidentOverlay.jsx
|   |   |       ARLiveXAIOverlay.jsx
|   |   |       ARPerformanceOverlay.jsx
|   |   |       ARXAIAttributionOverlay.jsx
|   |   |       overlays-config.json
|   |   |       overlays-demo-data.json
|   |   |       overlays-preset.json
|   |   |       README.md
|   |   |
|   |   +---pages
|   |   |       incidents.js
|   |   |       index.js
|   |   |       live.js
|   |   |       operator.js
|   |   |       pools.js
|   |   |       README.md
|   |   |       settings.js
|   |   |
|   |   +---preview
|   |   |       ar-preview-demo.json
|   |   |       ARPreviewControls.jsx
|   |   |       ARPreviewPanel.jsx
|   |   |       README.md
|   |   |
|   |   +---tests
|   |   |       ARContext.test.js
|   |   |       ARIncidentFeed.test.js
|   |   |       ARIntegration.test.js
|   |   |       ARLivePoolWidget.test.js
|   |   |       AROverlayToggle.test.js
|   |   |       README.md
|   |   |       XRScene3D.test.js
|   |   |
|   |   +---uploads
|   |   |   |   ar-upload-manifest.json
|   |   |   |   README.md
|   |   |   |   user-ar-presets.json
|   |   |   |
|   |   |   \---custom-ar-assets
|   |   |           custom-overlay.glb
|   |   |           custom-pool.glb
|   |   |           README.md
|   |   |
|   |   +---utils
|   |   |       arDemoData.js
|   |   |       arDeviceUtils.js
|   |   |       arMetricsUtils.js
|   |   |       arOverlayUtils.js
|   |   |       arTestHelpers.js
|   |   |       README.md
|   |   |       xrSceneUtils.js
|   |   |
|   |   \---xr
|   |       |   README.md
|   |       |   xr-config.json
|   |       |   XRLiquidityMesh.jsx
|   |       |   XRModelViewer.jsx
|   |       |   XROrderbookDepth3D.jsx
|   |       |   XRScene3D.jsx
|   |       |   XRVolumeVisualization.jsx
|   |       |
|   |       \---XRAssets
|   |               dashboard.glb
|   |               metrics-cube.glb
|   |               pool.glb
|   |               README.md
|   |
|   +---backend
|   |       README.md
|   |
|   +---charts
|   |       README.md
|   |
|   +---components
|   |   |   README.md
|   |   |
|   |   +---ai
|   |   |       AIChatBubble.jsx
|   |   |       AIDecisionFlow.jsx
|   |   |       AIInsightPrompt.jsx
|   |   |       LLMChatBox.jsx
|   |   |       ModelConfidenceMeter.jsx
|   |   |       ModelSwitcherCard.jsx
|   |   |       README.md
|   |   |       SaliencyOverlay.jsx
|   |   |       XAIHeatmapPanel.jsx
|   |   |
|   |   +---atomic
|   |   |       Avatar.jsx
|   |   |       Badge.jsx
|   |   |       Button.jsx
|   |   |       Chip.jsx
|   |   |       ColorSwatch.jsx
|   |   |       Divider.jsx
|   |   |       Icon.jsx
|   |   |       Label.jsx
|   |   |       ProgressBar.jsx
|   |   |       README.md
|   |   |       Skeleton.jsx
|   |   |       Spinner.jsx
|   |   |       StatusIndicator.jsx
|   |   |       ToggleSwitch.jsx
|   |   |       Tooltip.jsx
|   |   |
|   |   +---charts
|   |   |       AreaChart.jsx
|   |   |       BarChart.jsx
|   |   |       CandlestickChart.jsx
|   |   |       ChartWrapper.jsx
|   |   |       DepthChart.jsx
|   |   |       HeatmapChart.jsx
|   |   |       LatencyTrendChart.jsx
|   |   |       LineChart.jsx
|   |   |       PieChart.jsx
|   |   |       README.md
|   |   |       TradePathChart.jsx
|   |   |       VolumeChart.jsx
|   |   |
|   |   +---dialogs
|   |   |       AIExplainDialog.jsx
|   |   |       ConfirmDialog.jsx
|   |   |       ErrorModal.jsx
|   |   |       OnboardingModal.jsx
|   |   |       OperatorCommandDialog.jsx
|   |   |       PluginDialog.jsx
|   |   |       README.md
|   |   |       ReportExportDialog.jsx
|   |   |       SettingsDialog.jsx
|   |   |
|   |   +---forms
|   |   |       CodeEditorInput.jsx
|   |   |       DatePicker.jsx
|   |   |       FileUploadInput.jsx
|   |   |       InputGroup.jsx
|   |   |       JSONEditor.jsx
|   |   |       MultiSelect.jsx
|   |   |       PasswordInput.jsx
|   |   |       RangeSlider.jsx
|   |   |       README.md
|   |   |       SearchInput.jsx
|   |   |       SelectInput.jsx
|   |   |       TextInput.jsx
|   |   |       ToggleGroup.jsx
|   |   |
|   |   +---layout
|   |   |       AppLayout.jsx
|   |   |       Breadcrumbs.jsx
|   |   |       DashboardGrid.jsx
|   |   |       Footer.jsx
|   |   |       PageWrapper.jsx
|   |   |       PanelCard.jsx
|   |   |       README.md
|   |   |       SectionHeader.jsx
|   |   |       Sidebar.jsx
|   |   |       SplitPaneLayout.jsx
|   |   |       Topbar.jsx
|   |   |
|   |   +---loaders
|   |   |       FullscreenLoader.jsx
|   |   |       InlineSpinner.jsx
|   |   |       README.md
|   |   |       WidgetLoader.jsx
|   |   |
|   |   +---notifications
|   |   |       InlineAlert.jsx
|   |   |       NotificationBanner.jsx
|   |   |       README.md
|   |   |       Snackbar.jsx
|   |   |       ToastContainer.jsx
|   |   |       WebhookAlert.jsx
|   |   |
|   |   +---operator
|   |   |       AuditTimeline.jsx
|   |   |       HealthStatusCard.jsx
|   |   |       IncidentFeed.jsx
|   |   |       IncidentSummaryPanel.jsx
|   |   |       KillSwitchButton.jsx
|   |   |       OperatorCommandBar.jsx
|   |   |       README.md
|   |   |       ShiftRosterPanel.jsx
|   |   |
|   |   +---overlays
|   |   |       AlertBanner.jsx
|   |   |       AROverlay.jsx
|   |   |       DebugOverlay.jsx
|   |   |       IncidentOverlay.jsx
|   |   |       README.md
|   |   |       RiskOverlay.jsx
|   |   |       TradePathOverlay.jsx
|   |   |       XAIOverlay.jsx
|   |   |
|   |   +---plugin
|   |   |       PluginCard.jsx
|   |   |       PluginConfigForm.jsx
|   |   |       PluginMarketplace.jsx
|   |   |       PluginPanel.jsx
|   |   |       PluginStatusIndicator.jsx
|   |   |       PluginToggle.jsx
|   |   |       README.md
|   |   |
|   |   +---sandbox
|   |   |       ExperimentalChartPanel.jsx
|   |   |       FeatureFlagToggle.jsx
|   |   |       LLMToolbox.jsx
|   |   |       PlaygroundPanel.jsx
|   |   |       README.md
|   |   |       WidgetDevTools.jsx
|   |   |
|   |   +---tables
|   |   |       AITable.jsx
|   |   |       AlertHistoryTable.jsx
|   |   |       DataTable.jsx
|   |   |       EditableTableCell.jsx
|   |   |       PoolTable.jsx
|   |   |       README.md
|   |   |       RiskMatrixTable.jsx
|   |   |       SortableTable.jsx
|   |   |       TablePagination.jsx
|   |   |       TradeTable.jsx
|   |   |
|   |   +---theme
|   |   |       ContrastModeSwitch.jsx
|   |   |       README.md
|   |   |       ThemePaletteGrid.jsx
|   |   |       ThemePreviewBox.jsx
|   |   |       ThemeSelector.jsx
|   |   |       ThemeToggle.jsx
|   |   |
|   |   +---utils
|   |   |       BlockTimer.jsx
|   |   |       CodeBlock.jsx
|   |   |       CopyToClipboard.jsx
|   |   |       GasBadge.jsx
|   |   |       JsonViewer.jsx
|   |   |       OperatorAvatar.jsx
|   |   |       README.md
|   |   |       StatusPill.jsx
|   |   |       TimeAgo.jsx
|   |   |       ValueChangeDelta.jsx
|   |   |
|   |   \---widgets
|   |           AIDecisionScoreCard.jsx
|   |           GasWidget.jsx
|   |           LatencyMeter.jsx
|   |           MEVActivityWidget.jsx
|   |           OperatorInsightsWidget.jsx
|   |           PnLWidget.jsx
|   |           PoolHealthWidget.jsx
|   |           README.md
|   |           RiskGaugeWidget.jsx
|   |           RoutePriorityMeter.jsx
|   |           TokenReputationScore.jsx
|   |           TradeDeltaWidget.jsx
|   |           TradeVolumeSparkline.jsx
|   |           WatchdogStatus.jsx
|   |
|   +---context
|   |       AIContext.js
|   |       AIProvider.jsx
|   |       AlertsContext.js
|   |       AlertsProvider.jsx
|   |       AppContext.js
|   |       AppProvider.jsx
|   |       AuthContext.js
|   |       AuthProvider.jsx
|   |       context.test.js
|   |       contextHelpers.js
|   |       index.js
|   |       LayoutContext.js
|   |       LayoutProvider.jsx
|   |       LocaleContext.js
|   |       LocaleProvider.jsx
|   |       ModalContext.js
|   |       ModalProvider.jsx
|   |       NotificationsContext.js
|   |       NotificationsProvider.jsx
|   |       OperatorContext.js
|   |       OperatorProvider.jsx
|   |       OperatorShiftContext.js
|   |       OperatorShiftProvider.jsx
|   |       OverlayContext.js
|   |       OverlayProvider.jsx
|   |       PluginContext.js
|   |       PluginProvider.jsx
|   |       README.md
|   |       SettingsContext.js
|   |       SettingsProvider.jsx
|   |       StateSyncContext.js
|   |       StateSyncProvider.jsx
|   |       ThemeContext.js
|   |       ThemeProvider.jsx
|   |       useAI.js
|   |       useAlerts.js
|   |       useApp.js
|   |       useAuth.js
|   |       useLayout.js
|   |       useLocale.js
|   |       useModal.js
|   |       useNotifications.js
|   |       useOperator.js
|   |       useOperatorShift.js
|   |       useOverlay.js
|   |       usePlugin.js
|   |       useSettings.js
|   |       useStateSync.js
|   |       useTheme.js
|   |       useWebsocket.js
|   |       useXAI.js
|   |       WebsocketContext.js
|   |       WebsocketProvider.jsx
|   |       XAIContext.js
|   |       XAIProvider.jsx
|   |
|   +---data
|   |   |   active-pools.json
|   |   |   agent-scores.json
|   |   |   ai-evaluations.json
|   |   |   compliance-log.json
|   |   |   fork-state-diff.json
|   |   |   incident-log.json
|   |   |   market-depth.json
|   |   |   operator-profiles.json
|   |   |   oracle-feed-cache.json
|   |   |   plugin-usage.json
|   |   |   profit-log.json
|   |   |   README.md
|   |   |   risk-events.json
|   |   |   route-cache.json
|   |   |   simulation-runs.json
|   |   |   state-history.log
|   |   |   token-metadata.json
|   |   |   trade-history.json
|   |   |
|   |   +---ai-feedback
|   |   |       feedback-20250701.json
|   |   |       feedback-20250715.json
|   |   |       feedback-20250730.json
|   |   |       model-update-requests.json
|   |   |       README.md
|   |   |
|   |   +---analytics
|   |   |       ai-inference-20250701.json
|   |   |       ai-inference-20250715.json
|   |   |       ai-inference-20250730.json
|   |   |       anomaly-events-20250730.json
|   |   |       pool-liquidity-report-20250701.json
|   |   |       pool-liquidity-report-20250715.json
|   |   |       pool-liquidity-report-20250730.json
|   |   |       README.md
|   |   |       trade-alpha-scores-20250701.json
|   |   |       trade-alpha-scores-20250715.json
|   |   |       trade-alpha-scores-20250730.json
|   |   |
|   |   +---audit-trails
|   |   |       audit-20250701.log
|   |   |       audit-20250715.log
|   |   |       audit-20250730.log
|   |   |       event-archive-20250701.json
|   |   |       event-archive-20250715.json
|   |   |       event-archive-20250730.json
|   |   |       README.md
|   |   |
|   |   +---compliance-archive
|   |   |       kyc-report-20250701.pdf
|   |   |       kyc-report-20250715.pdf
|   |   |       kyc-report-20250730.pdf
|   |   |       README.md
|   |   |       sanctions-check-20250701.json
|   |   |       sanctions-check-20250715.json
|   |   |       sanctions-check-20250730.json
|   |   |
|   |   +---export
|   |   |       ai-inference-export-20250701.json
|   |   |       dashboard-report-20250730.pdf
|   |   |       export-20250701.csv
|   |   |       export-20250715.csv
|   |   |       export-20250730.csv
|   |   |       README.md
|   |   |
|   |   +---forensics
|   |   |       exploit-dump-20250701.json
|   |   |       exploit-dump-20250715.json
|   |   |       exploit-dump-20250730.json
|   |   |       README.md
|   |   |       root-cause-analysis.md
|   |   |       trade-anomaly-20250730.json
|   |   |
|   |   +---logs
|   |   |       ai-agent-20250701.log
|   |   |       ai-agent-20250715.log
|   |   |       ai-agent-20250730.log
|   |   |       engine-20250701.log
|   |   |       engine-20250715.log
|   |   |       engine-20250730.log
|   |   |       error-20250701.log
|   |   |       error-20250715.log
|   |   |       error-20250730.log
|   |   |       README.md
|   |   |       rotation-policy.md
|   |   |       trades-20250701.log
|   |   |       trades-20250715.log
|   |   |       trades-20250730.log
|   |   |       watchdog-20250701.log
|   |   |       watchdog-20250715.log
|   |   |       watchdog-20250730.log
|   |   |
|   |   +---operator-audit
|   |   |       ai-review-20250715.json
|   |   |       nlp-feedback-20250730.json
|   |   |       operator-actions-20250701.json
|   |   |       operator-actions-20250715.json
|   |   |       operator-actions-20250730.json
|   |   |       README.md
|   |   |
|   |   +---simulation-snapshots
|   |   |       post-fork-sim-20250715.json
|   |   |       pre-fork-sim-20250715.json
|   |   |       README.md
|   |   |       risk-test-20250715.json
|   |   |       snapshot-20250701.json
|   |   |       snapshot-20250715.json
|   |   |       snapshot-20250730.json
|   |   |
|   |   +---snapshots
|   |   |       agents-20250701.json
|   |   |       agents-20250715.json
|   |   |       agents-20250730.json
|   |   |       latest-snapshot.json
|   |   |       pools-20250701.json
|   |   |       pools-20250715.json
|   |   |       pools-20250730.json
|   |   |       README.md
|   |   |       sim-20250701.json
|   |   |       sim-20250715.json
|   |   |       sim-20250730.json
|   |   |
|   |   \---synthetic-datasets
|   |           deep-arb-ai-trainset.csv
|   |           fake-arb-scenarios.json
|   |           README.md
|   |           sim-synthetic-events.json
|   |           synthetic-prices-20250701.csv
|   |           synthetic-prices-20250715.csv
|   |           synthetic-profits-20250730.csv
|   |
|   +---deploy
|   |   |   CHANGELOG.md
|   |   |   patterns.md
|   |   |   README.md
|   |   |
|   |   +---ansible
|   |   |   |   inventory.ini
|   |   |   |   playbook.yml
|   |   |   |   README.md
|   |   |   |   secrets.yml
|   |   |   |
|   |   |   +---group_vars
|   |   |   |       all.yml
|   |   |   |       prod.yml
|   |   |   |       README.md
|   |   |   |
|   |   |   +---roles
|   |   |   |   |   README.md
|   |   |   |   |
|   |   |   |   +---ai-modules
|   |   |   |   |   |   README.md
|   |   |   |   |   |
|   |   |   |   |   +---backend
|   |   |   |   |   |       README.md
|   |   |   |   |   |
|   |   |   |   |   +---dashboard
|   |   |   |   |   |       README.md
|   |   |   |   |   |
|   |   |   |   |   \---operator
|   |   |   |   |           README.md
|   |   |   |   |
|   |   |   |   +---backend
|   |   |   |   |       README.md
|   |   |   |   |
|   |   |   |   +---dashboard
|   |   |   |   |       README.md
|   |   |   |   |
|   |   |   |   \---operator
|   |   |   |           README.md
|   |   |   |
|   |   |   \---scripts
|   |   |           README.md
|   |   |           run-all.sh
|   |   |
|   |   +---audit
|   |   |       audit-checklist.md
|   |   |       cloud-posture.md
|   |   |       deploy-logs.md
|   |   |       README.md
|   |   |
|   |   +---docker
|   |   |       ai-modules.Dockerfile
|   |   |       backend.Dockerfile
|   |   |       base.Dockerfile
|   |   |       dashboard.Dockerfile
|   |   |       operator.Dockerfile
|   |   |       README.md
|   |   |
|   |   +---docker-compose
|   |   |       docker-compose.dev.yml
|   |   |       docker-compose.override.yml
|   |   |       docker-compose.prod.yml
|   |   |       docker-compose.yml
|   |   |       README.md
|   |   |
|   |   +---environments
|   |   |       .env.example
|   |   |       dev.env
|   |   |       local.env
|   |   |       mainnet-fork.env
|   |   |       preview.env
|   |   |       prod.env
|   |   |       README.md
|   |   |       staging.env
|   |   |       testnet.env
|   |   |       vault.env
|   |   |
|   |   +---helm
|   |   |   |   README.md
|   |   |   |
|   |   |   \---apex-protocol
|   |   |       |   Chart.yaml
|   |   |       |   NOTES.txt
|   |   |       |   README.md
|   |   |       |   values.yaml
|   |   |       |
|   |   |       \---templates
|   |   |               configmap.yaml
|   |   |               deployment.yaml
|   |   |               hpa.yaml
|   |   |               ingress.yaml
|   |   |               README.md
|   |   |               secrets.yaml
|   |   |               service.yaml
|   |   |
|   |   +---kubernetes
|   |   |   |   README.md
|   |   |   |
|   |   |   +---base
|   |   |   |       ai-modules-deployment.yaml
|   |   |   |       backend-deployment.yaml
|   |   |   |       configmap.yaml
|   |   |   |       dashboard-deployment.yaml
|   |   |   |       ingress.yaml
|   |   |   |       kustomization.yaml
|   |   |   |       namespace.yaml
|   |   |   |       operator-deployment.yaml
|   |   |   |       README.md
|   |   |   |       secrets.yaml
|   |   |   |       service.yaml
|   |   |   |       storage.yaml
|   |   |   |
|   |   |   +---overlays
|   |   |   |   |   README.md
|   |   |   |   |
|   |   |   |   +---dev
|   |   |   |   |       kustomization.yaml
|   |   |   |   |       README.md
|   |   |   |   |
|   |   |   |   +---local
|   |   |   |   |       kustomization.yaml
|   |   |   |   |       README.md
|   |   |   |   |
|   |   |   |   +---prod
|   |   |   |   |       kustomization.yaml
|   |   |   |   |       README.md
|   |   |   |   |
|   |   |   |   +---staging
|   |   |   |   |       kustomization.yaml
|   |   |   |   |       README.md
|   |   |   |   |
|   |   |   |   \---testnet
|   |   |   |           kustomization.yaml
|   |   |   |           README.md
|   |   |   |
|   |   |   \---scripts
|   |   |           cleanup.sh
|   |   |           deploy.sh
|   |   |           README.md
|   |   |
|   |   +---migration
|   |   |       001-init.sql
|   |   |       README.md
|   |   |
|   |   +---scripts
|   |   |       backup-db.sh
|   |   |       deploy-all.sh
|   |   |       healthcheck.sh
|   |   |       logs.sh
|   |   |       README.md
|   |   |       restore-db.sh
|   |   |       update-all.sh
|   |   |
|   |   +---secrets
|   |   |       dev.secrets.enc
|   |   |       example.secrets.yaml
|   |   |       prod.secrets.enc
|   |   |       README.md
|   |   |
|   |   \---terraform
|   |       |   main.tf
|   |       |   outputs.tf
|   |       |   provider.tf
|   |       |   README.md
|   |       |   secrets.auto.tfvars
|   |       |   variables.tf
|   |       |   versions.tf
|   |       |
|   |       +---modules
|   |       |   |   README.md
|   |       |   |
|   |       |   +---db
|   |       |   |       README.md
|   |       |   |
|   |       |   +---k8s
|   |       |   |       README.md
|   |       |   |
|   |       |   +---storage
|   |       |   |       README.md
|   |       |   |
|   |       |   \---vpc
|   |       |           README.md
|   |       |
|   |       \---scripts
|   |               apply.sh
|   |               plan.sh
|   |               README.md
|   |
|   +---docs
|   |   |   ai-integration.md
|   |   |   analytics.md
|   |   |   api.md
|   |   |   ar-guide.md
|   |   |   architecture.md
|   |   |   audit-trail.md
|   |   |   backend-api.md
|   |   |   backend-stack.md
|   |   |   CHANGELOG.md
|   |   |   charts.md
|   |   |   ci-cd.md
|   |   |   code-quality.md
|   |   |   compliance.md
|   |   |   context.md
|   |   |   contract-integration.md
|   |   |   data-pipeline.md
|   |   |   db-schema.md
|   |   |   design-system.md
|   |   |   event-handling.md
|   |   |   event-reference.md
|   |   |   extensions.md
|   |   |   failover-guide.md
|   |   |   faq.md
|   |   |   faqs.md
|   |   |   features.md
|   |   |   fork-testing.md
|   |   |   formal-verification.md
|   |   |   getting-started.md
|   |   |   incident-response.md
|   |   |   integration.md
|   |   |   localization.md
|   |   |   logging-monitoring.md
|   |   |   mainnet-deployment.md
|   |   |   mainnet-hardening.md
|   |   |   migration-guide.md
|   |   |   module-development.md
|   |   |   navigation.md
|   |   |   notification-guide.md
|   |   |   onboarding.md
|   |   |   operator-guide.md
|   |   |   operator-modes.md
|   |   |   operator-roles.md
|   |   |   overlays-ar-xai.md
|   |   |   pages-structure.md
|   |   |   plugin-architecture.md
|   |   |   plugin-system.md
|   |   |   privacy.md
|   |   |   quickstart.md
|   |   |   README.md
|   |   |   release-notes.md
|   |   |   risk-management.md
|   |   |   roadmap.md
|   |   |   security.md
|   |   |   simulation-workflow.md
|   |   |   state-management.md
|   |   |   style-guide.md
|   |   |   test-strategy.md
|   |   |   testing.md
|   |   |   theming.md
|   |   |   troubleshooting.md
|   |   |   upgradeability.md
|   |   |   uploads.md
|   |   |   user-guide.md
|   |   |   widgets.md
|   |   |   xai-guide.md
|   |   |
|   |   +---ai
|   |   |       ai-engine.md
|   |   |       ai-ml-pipeline.md
|   |   |       ai-models.md
|   |   |       ai-ops-guide.md
|   |   |       ai-testing-guide.md
|   |   |       ai-upgradeability.md
|   |   |       README.md
|   |   |
|   |   +---api
|   |   |       ai-engine-api.yaml
|   |   |       backend-api.yaml
|   |   |       dashboard-api.yaml
|   |   |       notification-api.yaml
|   |   |       plugin-api.yaml
|   |   |       README.md
|   |   |       simulation-api.yaml
|   |   |
|   |   +---audit
|   |   |       audit-log-spec.md
|   |   |       incident-review-checklist.md
|   |   |       operator-audit-demo.csv
|   |   |       README.md
|   |   |
|   |   +---compliance
|   |   |       aml-logs.md
|   |   |       compliance-audit.md
|   |   |       data-retention.md
|   |   |       kyc-flow.md
|   |   |       README.md
|   |   |       sanctions-workflow.md
|   |   |
|   |   +---dashboard
|   |   |       ai-dashboard.md
|   |   |       dashboard-api.md
|   |   |       dashboard-architecture.md
|   |   |       live-analytics-guide.md
|   |   |       notification-integration.md
|   |   |       overlays-integration.md
|   |   |       plugin-status-panel.md
|   |   |       README.md
|   |   |
|   |   +---diagrams
|   |   |       ai-integration.drawio
|   |   |       ai-xai-pipeline.svg
|   |   |       backend-architecture.drawio
|   |   |       ci-cd-pipeline.drawio
|   |   |       dashboard-architecture.png
|   |   |       data-pipeline.drawio
|   |   |       failover-diagram.drawio
|   |   |       fork-testing.drawio
|   |   |       incident-response.drawio
|   |   |       operator-dashboard.drawio
|   |   |       operator-flow.svg
|   |   |       plugin-system-sequence.png
|   |   |       plugin-system.drawio
|   |   |       README.md
|   |   |       risk-flow.drawio
|   |   |       simulation-workflow.drawio
|   |   |       state-context-flow.png
|   |   |
|   |   +---formal
|   |   |       ai-formal-verification.md
|   |   |       contract-formal-verification.md
|   |   |       formal-verification-report.md
|   |   |       invariants.md
|   |   |       model-specs.md
|   |   |       README.md
|   |   |
|   |   +---legacy
|   |   |       deprecated-architecture.md
|   |   |       legacy-api.md
|   |   |       legacy-upgrade-guide.md
|   |   |       old-release-notes.md
|   |   |       README.md
|   |   |
|   |   +---migration
|   |   |       ai-migration.md
|   |   |       backend-migration.md
|   |   |       contract-migration.md
|   |   |       db-migration.md
|   |   |       plugin-migration.md
|   |   |       README.md
|   |   |
|   |   +---onboarding
|   |   |       ai-module-onboarding.md
|   |   |       auditor-onboarding.md
|   |   |       developer-onboarding.md
|   |   |       faq-onboarding.md
|   |   |       operator-onboarding.md
|   |   |       plugin-onboarding.md
|   |   |       README.md
|   |   |
|   |   +---playbooks
|   |   |       disaster-recovery.md
|   |   |       incident-playbook.md
|   |   |       ops-handover.md
|   |   |       README.md
|   |   |       rollback-playbook.md
|   |   |       upgrade-playbook.md
|   |   |
|   |   +---risk
|   |   |       ai-risk.md
|   |   |       bridge-risk.md
|   |   |       incident-catalog.md
|   |   |       kill-switch.md
|   |   |       mev-risk.md
|   |   |       oracle-risk.md
|   |   |       pool-risk.md
|   |   |       README.md
|   |   |       risk-dashboard.md
|   |   |       trade-risk.md
|   |   |
|   |   +---samples
|   |   |       demo-user.csv
|   |   |       onboarding-example.md
|   |   |       plugin-stub.js
|   |   |       README.md
|   |   |       sample-config.json
|   |   |       sample-theme.json
|   |   |
|   |   \---templates
|   |           context-provider-template.js
|   |           operator-alert-template.md
|   |           plugin-template.js
|   |           README.md
|   |           widget-template.jsx
|   |
|   +---extensions
|   |   |   CHANGELOG.md
|   |   |   extension-api.md
|   |   |   extension-dev-guide.md
|   |   |   extension-security.md
|   |   |   manifest.json
|   |   |   README.md
|   |   |   registry.json
|   |   |
|   |   +---assets
|   |   |       extension-banner-sample.png
|   |   |       extension-icon-sample.svg
|   |   |       extension-preview-theme.css
|   |   |       README.md
|   |   |
|   |   +---community
|   |   |       CommunityDiscussionThread.jsx
|   |   |       CommunityExtensionManifest.json
|   |   |       CommunityGalleryPanel.jsx
|   |   |       ExtensionMarketplace.jsx
|   |   |       ExtensionSubmitForm.jsx
|   |   |       README.md
|   |   |       VotingWidget.jsx
|   |   |
|   |   +---core
|   |   |       CoreExtensionLoader.js
|   |   |       CoreExtensionSampleWidget.jsx
|   |   |       CoreExtensionsRegistry.json
|   |   |       README.md
|   |   |
|   |   +---demo
|   |   |       AnimationPlayground.jsx
|   |   |       DarkModeDemoWidget.jsx
|   |   |       DemoConfigPreset.json
|   |   |       MobileUXPreviewer.jsx
|   |   |       README.md
|   |   |       ThemeDemoPanel.jsx
|   |   |       UXFeedbackCollector.jsx
|   |   |
|   |   +---integration
|   |   |       AnalyticsIntegrationPanel.jsx
|   |   |       ARPluginIntegrationPanel.jsx
|   |   |       ChainlinkIntegrationWidget.jsx
|   |   |       DiscordBotIntegration.jsx
|   |   |       ExternalApiIntegrationWidget.jsx
|   |   |       IntegrationManifest.json
|   |   |       README.md
|   |   |       WebhookBridgeExtension.jsx
|   |   |       XAIExtensionAdapter.js
|   |   |
|   |   +---labs
|   |   |       AdvancedStrategyLab.jsx
|   |   |       AIPrototypePanel.jsx
|   |   |       ExperimentalWidgetGallery.jsx
|   |   |       ExperimentRegistry.json
|   |   |       LabsDemoConfig.json
|   |   |       LabsLauncherPanel.jsx
|   |   |       PatternExplorerLab.jsx
|   |   |       README.md
|   |   |
|   |   +---plugin
|   |   |       AdvancedPluginDemo.jsx
|   |   |       plugin-manifest.json
|   |   |       PluginConfigEditor.jsx
|   |   |       PluginExtensionTemplate.js
|   |   |       PluginQuickStartSample.jsx
|   |   |       PluginReadme.md
|   |   |       README.md
|   |   |
|   |   +---samples
|   |   |       extension-onboarding.md
|   |   |       extension-sample-api.js
|   |   |       extension-sample-config.json
|   |   |       extension-sample-doc.md
|   |   |       extension-sample-widget.jsx
|   |   |       README.md
|   |   |
|   |   +---tests
|   |   |       AnalyticsIntegrationPanel.test.js
|   |   |       CommunityGalleryPanel.test.js
|   |   |       DemoExtensionSandbox.test.js
|   |   |       ExtensionLoader.test.js
|   |   |       ExtensionValidator.test.js
|   |   |       LabsLauncherPanel.test.js
|   |   |       PluginQuickStartSample.test.js
|   |   |       README.md
|   |   |
|   |   \---utils
|   |           extensionDevHelpers.js
|   |           extensionHotReload.js
|   |           extensionPermissions.js
|   |           extensionSandbox.js
|   |           extensionValidator.js
|   |           README.md
|   |           registerExtension.js
|   |
|   +---fixtures
|   |   |   CHANGELOG.md
|   |   |   README.md
|   |   |
|   |   +---analytics
|   |   |       anomaly-events-demo.csv
|   |   |       gas-costs-demo.csv
|   |   |       latency-demo.csv
|   |   |       outlier-events-demo.json
|   |   |       pnl-demo.csv
|   |   |       README.md
|   |   |       risk-profile-demo.json
|   |   |       roi-demo.csv
|   |   |       trade-history-demo.csv
|   |   |
|   |   +---api
|   |   |       mock-ai-inference.json
|   |   |       mock-analytics-data.json
|   |   |       mock-arb-alerts.json
|   |   |       mock-health-status.json
|   |   |       mock-incident-events.json
|   |   |       mock-notifications.json
|   |   |       mock-operator-audit.json
|   |   |       mock-overlays.json
|   |   |       mock-pnl-data.json
|   |   |       mock-trade-metrics.json
|   |   |       mock-upload-results.json
|   |   |       mock-user-session.json
|   |   |       mock-websocket-events.json
|   |   |       README.md
|   |   |
|   |   +---ar
|   |   |       ar-incident-demo.json
|   |   |       ar-user-preset-demo.json
|   |   |       demo-ar-overlays.json
|   |   |       live-pool-demo.json
|   |   |       README.md
|   |   |       xr-demo-assets.json
|   |   |
|   |   +---demo
|   |   |       ai-widget-demo-data.json
|   |   |       dashboard-demo-metrics.json
|   |   |       gas-widget-demo.json
|   |   |       operator-demo-session.json
|   |   |       plugin-demo-config.json
|   |   |       pnl-widget-demo.json
|   |   |       README.md
|   |   |       sandbox-stories.json
|   |   |       trade-volume-demo.json
|   |   |       xai-overlay-demo.json
|   |   |
|   |   +---misc
|   |   |       deprecated-demo.json
|   |   |       migration-sample.json
|   |   |       README.md
|   |   |       seed-data.json
|   |   |       test-data.json
|   |   |
|   |   +---notifications
|   |   |       alert-demo.json
|   |   |       banner-demo.json
|   |   |       incident-toast-demo.json
|   |   |       operator-notification-demo.json
|   |   |       README.md
|   |   |       webhook-demo.json
|   |   |
|   |   +---operator
|   |   |       audit-timeline-demo.json
|   |   |       escalation-demo.json
|   |   |       incident-log-demo.json
|   |   |       kill-switch-events-demo.json
|   |   |       README.md
|   |   |       shift-demo-schedule.json
|   |   |
|   |   +---plugins
|   |   |       extension-gallery-demo.json
|   |   |       plugin-config-demo.json
|   |   |       plugin-marketplace-demo.json
|   |   |       README.md
|   |   |
|   |   +---test-utils
|   |   |       demo-api-client.js
|   |   |       fixtures.test.js
|   |   |       README.md
|   |   |       sample-mock-store.js
|   |   |
|   |   \---user
|   |           demo-locale-settings.json
|   |           demo-user-profile.json
|   |           onboarding-tour-demo.json
|   |           README.md
|   |           theme-preset-demo.json
|   |
|   +---hooks
|   |       hooks.test.js
|   |       index.js
|   |       README.md
|   |       useAI.js
|   |       useAIFeedback.js
|   |       useAIInsight.js
|   |       useAIScoring.js
|   |       useAlerts.js
|   |       useAnalyticsData.js
|   |       useApi.js
|   |       useAppState.js
|   |       useArbStats.js
|   |       useARCameraStream.js
|   |       useARIncidentFeed.js
|   |       useAROperatorMode.js
|   |       useAROverlay.js
|   |       useARSession.js
|   |       useAuth.js
|   |       useBanner.js
|   |       useBreadcrumbs.js
|   |       useClipboard.js
|   |       useDropzone.js
|   |       useExtensionRegistry.js
|   |       useFileUpload.js
|   |       useFocusTrap.js
|   |       useGasTrends.js
|   |       useHydrated.js
|   |       useLabsExperiment.js
|   |       useLatencyStats.js
|   |       useLayout.js
|   |       useLiveData.js
|   |       useLivePnL.js
|   |       useLocale.js
|   |       useLocalStorage.js
|   |       useModal.js
|   |       useModelAudit.js
|   |       useModelSwitcher.js
|   |       useNavigation.js
|   |       useNotifications.js
|   |       useOnboarding.js
|   |       useOperator.js
|   |       useOperatorShift.js
|   |       usePersistedState.js
|   |       usePlugin.js
|   |       useRiskRegression.js
|   |       useSession.js
|   |       useSettings.js
|   |       useStateSync.js
|   |       useStorybookState.js
|   |       useSWRApi.js
|   |       useTheme.js
|   |       useTimeAgo.js
|   |       useUserProfile.js
|   |       useVisibility.js
|   |       useVolumeTimeseries.js
|   |       useWebhookListener.js
|   |       useWebsocket.js
|   |       useWidgetTestHarness.js
|   |       useXAI.js
|   |       useXRScene.js
|   |
|   +---integration
|   |       AlertSyncAdapter.js
|   |       AnalyticsAdapter.js
|   |       ApiBridge.js
|   |       ArbScoringSync.js
|   |       ARControlBridge.js
|   |       ARStreamAdapter.js
|   |       BotMessageBridge.js
|   |       ChainDataBridge.js
|   |       DiscordBotConnector.js
|   |       ExtensionRegistrySync.js
|   |       HealthCheckDisplay.jsx
|   |       HealthCheckDisplay.test.jsx
|   |       InsightsBridge.js
|   |       integration.test.js
|   |       IntegrationCache.js
|   |       integrationConfig.json
|   |       IntegrationDebugOverlay.jsx
|   |       IntegrationDevPanel.jsx
|   |       IntegrationLatencyMeter.jsx
|   |       IntegrationLogger.js
|   |       IntegrationStatusCard.jsx
|   |       IntegrationToggleSwitch.jsx
|   |       integrationUtils.js
|   |       LabsStatusBridge.js
|   |       mockIntegrationData.json
|   |       OperatorSyncBridge.js
|   |       PluginSyncAdapter.js
|   |       PluginSyncAdapter.test.js
|   |       README.md
|   |       SSEBridge.js
|   |       SyncErrorBoundary.jsx
|   |       useIntegrationStatus.js
|   |       WebhookReceiver.js
|   |       WebsocketBridge.js
|   |       WebsocketBridge.test.js
|   |       XAIAdapter.js
|   |       XAIAdapter.test.js
|   |       XRCanvasSync.js
|   |
|   +---layouts
|   |       AppLayout.jsx
|   |       ARLayout.jsx
|   |       AuthLayout.jsx
|   |       DashboardGrid.jsx
|   |       Footer.jsx
|   |       MultiPaneLayout.jsx
|   |       OperatorLayout.jsx
|   |       PageWrapper.jsx
|   |       README.md
|   |       Sidebar.jsx
|   |       SplitPaneLayout.jsx
|   |       StickyMenuBar.jsx
|   |       Topbar.jsx
|   |
|   +---locales
|   |   |   add-new-language.md
|   |   |   ar.json
|   |   |   bn.json
|   |   |   CHANGELOG.md
|   |   |   check-missing-translations.js
|   |   |   compile-locale-bundle.js
|   |   |   currency-map.json
|   |   |   currency-utils.js
|   |   |   date-format-map.json
|   |   |   de.json
|   |   |   detect-user-locale.js
|   |   |   en.json
|   |   |   es.json
|   |   |   fallback.json
|   |   |   fr.json
|   |   |   hi.json
|   |   |   i18n-config.js
|   |   |   id.json
|   |   |   ja.json
|   |   |   keys-reference.json
|   |   |   locale-utils.js
|   |   |   locales.test.js
|   |   |   message-templates.json
|   |   |   number-format-map.json
|   |   |   pluralization-rules.json
|   |   |   pt.json
|   |   |   README.md
|   |   |   region-switcher.js
|   |   |   ru.json
|   |   |   supported-locales.json
|   |   |   ta.json
|   |   |   te.json
|   |   |   timeago-locales.js
|   |   |   timezone-map.json
|   |   |   translate-best-practices.md
|   |   |   update-locale-cdn.js
|   |   |   zh.json
|   |   |
|   |   \---custom
|   |           custom-strings-demo.json
|   |           onboarding-tour-hi.json
|   |           operator-flows-ta.json
|   |           README.md
|   |
|   +---mock
|   |   |   api-handlers.js
|   |   |   api-handlers.test.js
|   |   |   CHANGELOG.md
|   |   |   factories.test.js
|   |   |   faker-config.js
|   |   |   hot-reload-mocks.js
|   |   |   inject-mocks.js
|   |   |   mirage-readme.md
|   |   |   mirage-server.js
|   |   |   mirage-server.test.js
|   |   |   mock-server.js
|   |   |   mock-utils.js
|   |   |   mock.test.js
|   |   |   mockConfig.json
|   |   |   msw-readme.md
|   |   |   msw-server.js
|   |   |   README.md
|   |   |   scenario-presets.test.js
|   |   |   scenario-switcher.js
|   |   |   setup-mock-env.js
|   |   |   socket-mock-server.js
|   |   |
|   |   +---api-responses
|   |   |       mock-ai-inference.json
|   |   |       mock-analytics-data.json
|   |   |       mock-arb-alerts.json
|   |   |       mock-health-status.json
|   |   |       mock-incident-events.json
|   |   |       mock-notifications.json
|   |   |       mock-operator-audit.json
|   |   |       mock-overlays.json
|   |   |       mock-pnl-data.json
|   |   |       mock-trade-metrics.json
|   |   |       mock-upload-results.json
|   |   |       mock-user-session.json
|   |   |       mock-websocket-events.json
|   |   |       README.md
|   |   |
|   |   +---factories
|   |   |       aiInferenceFactory.js
|   |   |       analyticsFactory.js
|   |   |       incidentFactory.js
|   |   |       notificationFactory.js
|   |   |       poolFactory.js
|   |   |       README.md
|   |   |       tradeFactory.js
|   |   |       userFactory.js
|   |   |
|   |   \---scenario-presets
|   |           ai-demo-state.json
|   |           incident-demo-state.json
|   |           operator-demo-state.json
|   |           README.md
|   |           trade-surge-state.json
|   |
|   +---modals
|   |       AccountSwitchDialog.jsx
|   |       AIExplainDialog.jsx
|   |       AIFeedbackModal.jsx
|   |       AlertModal.jsx
|   |       ARPermissionModal.jsx
|   |       AuditReviewDialog.jsx
|   |       ConfirmDialog.jsx
|   |       CustomModal.jsx
|   |       DebugModal.jsx
|   |       DialogQueueProvider.jsx
|   |       ErrorModal.jsx
|   |       ExportDialog.jsx
|   |       ExtensionMarketplaceDialog.jsx
|   |       FileUploadModal.jsx
|   |       HelpDialog.jsx
|   |       IncidentDetailModal.jsx
|   |       index.js
|   |       InfoDialog.jsx
|   |       KillSwitchModal.jsx
|   |       LabsDialog.jsx
|   |       ModalHost.jsx
|   |       modals.test.js
|   |       ModelSwitcherDialog.jsx
|   |       NotificationModal.jsx
|   |       OnboardingModal.jsx
|   |       OperatorCommandDialog.jsx
|   |       OverlaySettingsDialog.jsx
|   |       PluginConfigDialog.jsx
|   |       PluginDialog.jsx
|   |       ProfileSettingsModal.jsx
|   |       README.md
|   |       SettingsDialog.jsx
|   |       ShiftChangeDialog.jsx
|   |       TourDialog.jsx
|   |       WelcomeDialog.jsx
|   |       XAIOverlayDialog.jsx
|   |
|   +---notifications
|   |   |   AIInsightAlert.jsx
|   |   |   AlertBadge.jsx
|   |   |   AlertCountdown.jsx
|   |   |   AlertStatusPill.jsx
|   |   |   CHANGELOG.md
|   |   |   EmailNotification.jsx
|   |   |   EscalationAlertBar.jsx
|   |   |   IncidentAlertBar.jsx
|   |   |   IncidentResponseToast.jsx
|   |   |   InlineAlert.jsx
|   |   |   mockNotificationServer.js
|   |   |   MultiChannelAlert.jsx
|   |   |   notification-best-practices.md
|   |   |   notificationApi.js
|   |   |   NotificationBanner.jsx
|   |   |   NotificationCenter.jsx
|   |   |   notificationDevPanel.jsx
|   |   |   NotificationPanel.jsx
|   |   |   notifications.test.js
|   |   |   NotificationsContext.js
|   |   |   NotificationsProvider.jsx
|   |   |   notificationStories.md
|   |   |   notificationTemplates.js
|   |   |   notificationUtils.js
|   |   |   OperatorAlert.jsx
|   |   |   PushNotificationPanel.jsx
|   |   |   README.md
|   |   |   Snackbar.jsx
|   |   |   ToastContainer.jsx
|   |   |   useNotifications.js
|   |   |   WebhookAlert.jsx
|   |   |
|   |   \---testData
|   |           demo-notifications.json
|   |           incident-alerts-demo.json
|   |           README.md
|   |
|   +---operator
|   |       README.md
|   |
|   +---overlays
|   |       AlertBanner.jsx
|   |       ARIncidentOverlay.jsx
|   |       AROverlay.jsx
|   |       ConnectionStatusOverlay.jsx
|   |       DebugOverlay.jsx
|   |       EscalationOverlay.jsx
|   |       IncidentBannerOverlay.jsx
|   |       IncidentOverlay.jsx
|   |       index.js
|   |       LatencyOverlay.jsx
|   |       OperatorCamOverlay.jsx
|   |       OperatorOverlay.jsx
|   |       OverlayConfigPanel.jsx
|   |       OverlayHotkeys.js
|   |       OverlayPortal.jsx
|   |       OverlayProvider.jsx
|   |       OverlayRoot.jsx
|   |       overlays.test.js
|   |       OverlaySettingsModal.jsx
|   |       OverlayToggleButton.jsx
|   |       OverlayTransition.js
|   |       overlayUtils.js
|   |       README.md
|   |       RiskOverlay.jsx
|   |       StatusOverlay.jsx
|   |       TradePathOverlay.jsx
|   |       XAIHeatmapOverlay.jsx
|   |       XAIOverlay.jsx
|   |
|   +---pages
|   |   |   404.js
|   |   |   500.js
|   |   |   account.js
|   |   |   ai.js
|   |   |   alerts.js
|   |   |   analytics.js
|   |   |   ar.js
|   |   |   assets.js
|   |   |   backup.js
|   |   |   cam.js
|   |   |   changelog.js
|   |   |   dashboard.js
|   |   |   dev.js
|   |   |   docs.js
|   |   |   download.js
|   |   |   edge.js
|   |   |   escalation.js
|   |   |   extensions.js
|   |   |   failover.js
|   |   |   gas.js
|   |   |   health.js
|   |   |   help.js
|   |   |   history.js
|   |   |   i18n.js
|   |   |   incidents.js
|   |   |   index.js
|   |   |   kill-switch.js
|   |   |   latency.js
|   |   |   legal.js
|   |   |   liquidity.js
|   |   |   login.js
|   |   |   logs.js
|   |   |   maintenance.js
|   |   |   marketplace.js
|   |   |   metrics.js
|   |   |   onboarding-tour.js
|   |   |   onboarding.js
|   |   |   operator.js
|   |   |   overlays.js
|   |   |   pattern-404.js
|   |   |   pattern-dashboard.js
|   |   |   pattern-modal.js
|   |   |   plugins.js
|   |   |   pnl.js
|   |   |   preview.js
|   |   |   privacy.js
|   |   |   profile.js
|   |   |   README.md
|   |   |   register.js
|   |   |   reset-password.js
|   |   |   risk.js
|   |   |   robots.txt
|   |   |   sandbox.js
|   |   |   settings.js
|   |   |   sitemap.xml
|   |   |   status.js
|   |   |   storybook.js
|   |   |   team.js
|   |   |   test.js
|   |   |   theme.js
|   |   |   trades.js
|   |   |   uploads.js
|   |   |   users.js
|   |   |   verify-email.js
|   |   |   wallets.js
|   |   |   welcome.js
|   |   |   xai.js
|   |   |   [...slug].js
|   |   |   _app.js
|   |   |_document.js
|   |   |   _error.js
|   |   |_middleware.js
|   |   |
|   |   \---api
|   |           ai.js
|   |           arb.js
|   |           dev.js
|   |           extension.js
|   |           health.js
|   |           index.js
|   |           metrics.js
|   |           notifications.js
|   |           plugin.js
|   |           README.md
|   |           user.js
|   |           webhook.js
|   |
|   +---plugins
|   |   |   atomic-swap-batched.ts
|   |   |   bridge-latency-sniper.ts
|   |   |   CHANGELOG.md
|   |   |   ExtensionPluginAdapter.js
|   |   |   flash-sandwich-mm.ts
|   |   |   hyper-bundle-engine.ts
|   |   |   index.js
|   |   |   MarketplaceQAStatus.jsx
|   |   |   MarketplaceSubmissionForm.jsx
|   |   |   micro-latency-arb-suite.ts
|   |   |   nft-gamefi-arb.ts
|   |   |   plugin-api.test.js
|   |   |   plugin-architecture.md
|   |   |   plugin-best-practices.md
|   |   |   plugin-marketplace.test.js
|   |   |   plugin-sandbox.test.js
|   |   |   plugin-schema.json
|   |   |   plugin-types.js
|   |   |   PluginAdapter.js
|   |   |   PluginAPI.js
|   |   |   PluginApiBridge.js
|   |   |   PluginAuditLog.js
|   |   |   PluginCard.jsx
|   |   |   PluginConfig.js
|   |   |   PluginConfigForm.jsx
|   |   |   PluginContext.js
|   |   |   PluginDataSync.js
|   |   |   PluginDetails.jsx
|   |   |   PluginDevToolsPanel.jsx
|   |   |   PluginDialog.jsx
|   |   |   PluginErrorBoundary.jsx
|   |   |   PluginEventBus.js
|   |   |   PluginFactory.js
|   |   |   PluginHotReload.js
|   |   |   PluginInstallDialog.jsx
|   |   |   PluginInterface.js
|   |   |   PluginLifecycle.js
|   |   |   PluginList.jsx
|   |   |   PluginLoader.js
|   |   |   PluginManager.jsx
|   |   |   PluginManifest.js
|   |   |   PluginMarketplace.jsx
|   |   |   PluginMetadata.js
|   |   |   PluginPanel.jsx
|   |   |   PluginPermissions.json
|   |   |   PluginProvider.jsx
|   |   |   PluginQuickStartSample.jsx
|   |   |   PluginReadme.md
|   |   |   PluginRegistry.json
|   |   |   plugins.test.js
|   |   |   PluginSandbox.jsx
|   |   |   PluginSandboxLauncher.js
|   |   |   PluginSecurityManager.js
|   |   |   PluginSettings.jsx
|   |   |   PluginStatusIndicator.jsx
|   |   |   PluginToggle.jsx
|   |   |   PluginValidator.js
|   |   |   PluginVersion.js
|   |   |   README.md
|   |   |
|   |   +---alpha-signal
|   |   |   |   ai-signal-orchestrator.js
|   |   |   |   alpha-nft-issuer.js
|   |   |   |   alpha-reputation.js
|   |   |   |   alpha-voting.js
|   |   |   |   micro-arb-detector.js
|   |   |   |   README.md
|   |   |   |   sandwich-detector.js
|   |   |   |   sniping-detector.js
|   |   |   |   trend-analyzer-v2.js
|   |   |   |   trend-analyzer.js
|   |   |   |   whale-signal.js
|   |   |   |
|   |   |   +---docs
|   |   |   |       alerts-integration.md
|   |   |   |       alpha-reputation-scores.md
|   |   |   |       alpha-signal-models.md
|   |   |   |       alpha-voting-protocol.md
|   |   |   |       arb-patterns.md
|   |   |   |       README.md
|   |   |   |
|   |   |   \---tests
|   |   |           ai-signal-orchestrator.test.js
|   |   |           alpha-nft-issuer.test.js
|   |   |           alpha-reputation.test.js
|   |   |           alpha-voting.test.js
|   |   |           micro-arb-detector.test.js
|   |   |           README.md
|   |   |           sandwich-detector.test.js
|   |   |           sniping-detector.test.js
|   |   |           trend-analyzer-v2.test.js
|   |   |           trend-analyzer.test.js
|   |   |           whale-signal.test.js
|   |   |
|   |   +---bridge-adapters
|   |   |   |   avalanche-adapter.js
|   |   |   |   axelar-adapter.js
|   |   |   |   circle-cctp-adapter.js
|   |   |   |   cross-twin-adapter.js
|   |   |   |   elliptic-adapter.js
|   |   |   |   layerzero-adapter.js
|   |   |   |   polygon-zkevm-adapter.js
|   |   |   |   range-cross-chain-adapter.js
|   |   |   |   README.md
|   |   |   |   relaychain-adapter.js
|   |   |   |   symbiosis-adapter.js
|   |   |   |   wormhole-adapter.js
|   |   |   |
|   |   |   +---docs
|   |   |   |       avalanche-guide.md
|   |   |   |       bridge-integrations.md
|   |   |   |       cross-chain-security.md
|   |   |   |       polygon-zkevm-guide.md
|   |   |   |       README.md
|   |   |   |       relaychain-integration.md
|   |   |   |
|   |   |   \---tests
|   |   |           avalanche-adapter.test.js
|   |   |           axelar-adapter.test.js
|   |   |           circle-cctp-adapter.test.js
|   |   |           cross-twin-adapter.test.js
|   |   |           elliptic-adapter.test.js
|   |   |           layerzero-adapter.test.js
|   |   |           polygon-zkevm-adapter.test.js
|   |   |           range-cross-chain-adapter.test.js
|   |   |           README.md
|   |   |           relaychain-adapter.test.js
|   |   |           symbiosis-adapter.test.js
|   |   |           wormhole-adapter.test.js
|   |   |
|   |   +---compliance
|   |   |   |   adverse-media-scanner.js
|   |   |   |   blacklist-module.js
|   |   |   |   dispute-module.js
|   |   |   |   forensics-module.js
|   |   |   |   jurisdiction-manager.js
|   |   |   |   kyc-aml-module.js
|   |   |   |   pep-checker.js
|   |   |   |   permission-validator.js
|   |   |   |   rbac-enforcer.js
|   |   |   |   README.md
|   |   |   |   sanctions-checker.js
|   |   |   |   whitelist-module.js
|   |   |   |
|   |   |   +---docs
|   |   |   |       compliance-checks.md
|   |   |   |       forensics-guide.md
|   |   |   |       governance-controls.md
|   |   |   |       kyc-flows.md
|   |   |   |       README.md
|   |   |   |       sanctions-lists.md
|   |   |   |
|   |   |   \---tests
|   |   |           adverse-media-scanner.test.js
|   |   |           blacklist-module.test.js
|   |   |           dispute-module.test.js
|   |   |           forensics-module.test.js
|   |   |           jurisdiction-manager.test.js
|   |   |           kyc-aml-module.test.js
|   |   |           pep-checker.test.js
|   |   |           permission-validator.test.js
|   |   |           rbac-enforcer.test.js
|   |   |           README.md
|   |   |           sanctions-checker.test.js
|   |   |           whitelist-module.test.js
|   |   |
|   |   +---dex-adapters
|   |   |   |   aggregator-adapter.js
|   |   |   |   balancer-adapter.js
|   |   |   |   cowswap-adapter.js
|   |   |   |   curve-adapter.js
|   |   |   |   dodo-adapter.js
|   |   |   |   fraxswap-adapter.js
|   |   |   |   kyber-adapter.js
|   |   |   |   maverick-adapter.js
|   |   |   |   orca-adapter.js
|   |   |   |   pancake-adapter.js
|   |   |   |   quickswap-adapter.js
|   |   |   |   README.md
|   |   |   |   sushi-adapter.js
|   |   |   |   synthetix-adapter.js
|   |   |   |   thorchain-adapter.js
|   |   |   |   traderjoe-adapter.js
|   |   |   |   uniswap-v3-adapter.js
|   |   |   |   vertex-adapter.js
|   |   |   |   woofi-adapter.js
|   |   |   |
|   |   |   +---docs
|   |   |   |       adapter-development.md
|   |   |   |       dex-architecture.md
|   |   |   |       gas-optimizations.md
|   |   |   |       integration-guide.md
|   |   |   |       README.md
|   |   |   |       slippage-models.md
|   |   |   |       supported-dexes.md
|   |   |   |
|   |   |   \---tests
|   |   |           aggregator-adapter.test.js
|   |   |           balancer-adapter.test.js
|   |   |           cowswap-adapter.test.js
|   |   |           curve-adapter.test.js
|   |   |           dodo-adapter.test.js
|   |   |           fraxswap-adapter.test.js
|   |   |           kyber-adapter.test.js
|   |   |           maverick-adapter.test.js
|   |   |           orca-adapter.test.js
|   |   |           pancake-adapter.test.js
|   |   |           quickswap-adapter.test.js
|   |   |           README.md
|   |   |           sushi-adapter.test.js
|   |   |           synthetix-adapter.test.js
|   |   |           thorchain-adapter.test.js
|   |   |           traderjoe-adapter.test.js
|   |   |           uniswap-v3-adapter.test.js
|   |   |           vertex-adapter.test.js
|   |   |           woofi-adapter.test.js
|   |   |
|   |   +---docs
|   |   |       adapter-api.md
|   |   |       alpha-patterns.md
|   |   |       fork-testing-guide.md
|   |   |       integration-scenarios.md
|   |   |       mev-risk-mitigation.md
|   |   |       plugin-development.md
|   |   |       plugins-architecture.md
|   |   |       README.md
|   |   |       registry-guide.md
|   |   |       smart-contract-integration.md
|   |   |
|   |   +---flashloan
|   |   |   |   aave-adapter.js
|   |   |   |   angle-adapter.js
|   |   |   |   compound-adapter.js
|   |   |   |   cream-adapter.js
|   |   |   |   dydx-adapter.js
|   |   |   |   flashbots-adapter.js
|   |   |   |   gearbox-adapter.js
|   |   |   |   makerdao-adapter.js
|   |   |   |   morpho-adapter.js
|   |   |   |   parasite-arb-adapter.js
|   |   |   |   radiant-adapter.js
|   |   |   |   README.md
|   |   |   |   stargate-adapter.js
|   |   |   |
|   |   |   +---docs
|   |   |   |       audit-log.md
|   |   |   |       flashloan-architecture.md
|   |   |   |       flashloan-risks.md
|   |   |   |       provider-integrations.md
|   |   |   |       README.md
|   |   |   |       upgrade-guide.md
|   |   |   |
|   |   |   \---tests
|   |   |           aave-adapter.test.js
|   |   |           angle-adapter.test.js
|   |   |           compound-adapter.test.js
|   |   |           cream-adapter.test.js
|   |   |           dydx-adapter.test.js
|   |   |           flashbots-adapter.test.js
|   |   |           gearbox-adapter.test.js
|   |   |           makerdao-adapter.test.js
|   |   |           morpho-adapter.test.js
|   |   |           parasite-arb-adapter.test.js
|   |   |           radiant-adapter.test.js
|   |   |           README.md
|   |   |           stargate-adapter.test.js
|   |   |
|   |   +---insurance
|   |   |   |   claim-auditor.js
|   |   |   |   claim-verifier.js
|   |   |   |   coverage-oracle.js
|   |   |   |   incident-monitor.js
|   |   |   |   insurance-pool-manager.js
|   |   |   |   payout-calculator.js
|   |   |   |   premium-calculator.js
|   |   |   |   README.md
|   |   |   |   risk-assessment-plugin.js
|   |   |   |   risk-modeler.js
|   |   |   |
|   |   |   +---docs
|   |   |   |       claim-workflow.md
|   |   |   |       insurance-architecture.md
|   |   |   |       pool-audits.md
|   |   |   |       README.md
|   |   |   |       risk-assessment-methods.md
|   |   |   |       risk-models.md
|   |   |   |
|   |   |   \---tests
|   |   |           claim-auditor.test.js
|   |   |           claim-verifier.test.js
|   |   |           coverage-oracle.test.js
|   |   |           incident-monitor.test.js
|   |   |           insurance-pool-manager.test.js
|   |   |           payout-calculator.test.js
|   |   |           premium-calculator.test.js
|   |   |           README.md
|   |   |           risk-assessment-plugin.test.js
|   |   |           risk-modeler.test.js
|   |   |
|   |   +---intent-solvers
|   |   |   |   auction-intent-solver.js
|   |   |   |   batch-intent-processor.js
|   |   |   |   cow-intent-solver.js
|   |   |   |   eco-intent-solver.js
|   |   |   |   intent-forker.js
|   |   |   |   intent-merger.js
|   |   |   |   keepers-intent-solver.js
|   |   |   |   README.md
|   |   |   |   rfq-intent-solver.js
|   |   |   |   sandwich-intent-solver.js
|   |   |   |   sniper-intent-solver.js
|   |   |   |   uniswapx-intent-solver.js
|   |   |   |
|   |   |   +---docs
|   |   |   |       auction-design.md
|   |   |   |       eco-intents.md
|   |   |   |       intent-architecture.md
|   |   |   |       intent-merging.md
|   |   |   |       README.md
|   |   |   |
|   |   |   \---tests
|   |   |           auction-intent-solver.test.js
|   |   |           batch-intent-processor.test.js
|   |   |           cow-intent-solver.test.js
|   |   |           eco-intent-solver.test.js
|   |   |           intent-forker.test.js
|   |   |           intent-merger.test.js
|   |   |           keepers-intent-solver.test.js
|   |   |           README.md
|   |   |           rfq-intent-solver.test.js
|   |   |           sandwich-intent-solver.test.js
|   |   |           sniper-intent-solver.test.js
|   |   |           uniswapx-intent-solver.test.js
|   |   |
|   |   +---internal
|   |   |       interface-definitions.ts
|   |   |       migration-tool.js
|   |   |       plugin-manager.ts
|   |   |       plugin-utils.js
|   |   |       plugins.json
|   |   |       README.md
|   |   |       registry.ts
|   |   |       test-utils.js
|   |   |
|   |   +---marketplace
|   |   |       governance-marketplace.js
|   |   |       module-marketplace-registry.json
|   |   |       module-marketplace.js
|   |   |       plugin-marketplace-registry.json
|   |   |       plugin-marketplace.js
|   |   |       README.md
|   |   |
|   |   +---model-marketplace
|   |   |       ai-model-marketplace-registry.json
|   |   |       ai-model-marketplace.js
|   |   |       ai-model-metadata.json
|   |   |       ai-model-proxy.js
|   |   |       ai-model-validator.js
|   |   |       README.md
|   |   |
|   |   +---oracles
|   |   |   |   ai-oracle.js
|   |   |   |   chainlink-oracle.js
|   |   |   |   compliance-oracle.js
|   |   |   |   external-data-oracle.js
|   |   |   |   fallback-oracle.js
|   |   |   |   liquidity-oracle.js
|   |   |   |   onchain-oracle.js
|   |   |   |   README.md
|   |   |   |   time-weighted-oracle.js
|   |   |   |   volatility-oracle.js
|   |   |   |   zero-knowledge-oracle.js
|   |   |   |
|   |   |   +---docs
|   |   |   |       data-sources.md
|   |   |   |       oracle-integrations.md
|   |   |   |       README.md
|   |   |   |       risk-mitigation.md
|   |   |   |       zk-proofs.md
|   |   |   |
|   |   |   \---tests
|   |   |           ai-oracle.test.js
|   |   |           chainlink-oracle.test.js
|   |   |           compliance-oracle.test.js
|   |   |           external-data-oracle.test.js
|   |   |           fallback-oracle.test.js
|   |   |           liquidity-oracle.test.js
|   |   |           onchain-oracle.test.js
|   |   |           README.md
|   |   |           time-weighted-oracle.test.js
|   |   |           volatility-oracle.test.js
|   |   |           zero-knowledge-oracle.test.js
|   |   |
|   |   +---samples
|   |   |       demo-plugin-index.js
|   |   |       demo-plugin-manifest.json
|   |   |       demo-plugin-ui.jsx
|   |   |       plugin-boilerplate.md
|   |   |       README.md
|   |   |
|   |   +---social-impact
|   |   |   |   carbon-offset-module.js
|   |   |   |   charity-oracle.js
|   |   |   |   csr-audit.js
|   |   |   |   donation-router.js
|   |   |   |   esg-allocator.js
|   |   |   |   grants-engine.js
|   |   |   |   green-bond-manager.js
|   |   |   |   impact-scoring.js
|   |   |   |   impact-voting.js
|   |   |   |   README.md
|   |   |   |
|   |   |   +---docs
|   |   |   |       charity-protocols.md
|   |   |   |       csr-programs.md
|   |   |   |       esg-logic.md
|   |   |   |       impact-scoring-models.md
|   |   |   |       README.md
|   |   |   |       social-impact-flows.md
|   |   |   |
|   |   |   \---tests
|   |   |           carbon-offset-module.test.js
|   |   |           charity-oracle.test.js
|   |   |           csr-audit.test.js
|   |   |           donation-router.test.js
|   |   |           esg-allocator.test.js
|   |   |           grants-engine.test.js
|   |   |           green-bond-manager.test.js
|   |   |           impact-scoring.test.js
|   |   |           impact-voting.test.js
|   |   |           README.md
|   |   |
|   |   +---template
|   |   |       adapter-template.js
|   |   |       model-template.js
|   |   |       plugin-template.js
|   |   |       README.md
|   |   |       template-config.json
|   |   |
|   |   \---tests
|   |           ai-model-marketplace.test.js
|   |           atomic-swap-batched.test.ts
|   |           bridge-latency-sniper.test.ts
|   |           flash-sandwich-mm.test.ts
|   |           governance-marketplace.test.js
|   |           hyper-bundle-engine.test.ts
|   |           micro-latency-arb-suite.test.ts
|   |           nft-gamefi-arb.test.ts
|   |           plugin-manager.test.js
|   |           plugins-integration.test.js
|   |           README.md
|   |           test-utils.js
|   |
|   +---presets
|   |   |   advanced-presets.json
|   |   |   ai-presets.json
|   |   |   backup-presets.json
|   |   |   CHANGELOG.md
|   |   |   custom-preset-guide.md
|   |   |   demo-presets.json
|   |   |   layout-presets.json
|   |   |   pattern-presets.json
|   |   |   patterns.md
|   |   |   presets-best-practices.md
|   |   |   presets.test.js
|   |   |   quickstart-presets.json
|   |   |   README.md
|   |   |   sample-presets.json
|   |   |   strategy-presets.json
|   |   |   theme-presets.json
|   |   |   ui-presets.json
|   |   |   user-presets.json
|   |   |
|   |   +---custom-presets
|   |   |       high-volatility-preset.json
|   |   |       minimal-view-preset.json
|   |   |       night-trading-preset.json
|   |   |       README.md
|   |   |       sample-operator-preset.json
|   |   |
|   |   \---templates
|   |           dev-preset.json
|   |           onboarding-preset.json
|   |           preset-template.json
|   |           README.md
|   |
|   +---preview
|   |       CHANGELOG.md
|   |       feature-flags.json
|   |       feature-flags.test.js
|   |       FeatureFlagPanel.jsx
|   |       FeatureFlagSwitch.jsx
|   |       preview-branches.json
|   |       preview-cleanup.js
|   |       preview-config.json
|   |       preview-demo-data.json
|   |       preview-deploy-hook.js
|   |       preview-env.js
|   |       preview-metadata.json
|   |       preview-status.json
|   |       preview-stories.md
|   |       preview.test.js
|   |       previewApi.js
|   |       PreviewBanner.jsx
|   |       PreviewChangelogModal.jsx
|   |       previewDeployHooks.js
|   |       PreviewDeploymentCard.jsx
|   |       previewDevPanel.jsx
|   |       PreviewPanel.jsx
|   |       PreviewReviewActions.jsx
|   |       PreviewStatusBar.jsx
|   |       PreviewToggleButton.jsx
|   |       previewUtils.js
|   |       README.md
|   |       useFeatureFlags.js
|   |       usePreviewStatus.js
|   |       webhook-handler.js
|   |
|   +---public
|   |   |   .htaccess
|   |   |   android-chrome-192x192.png
|   |   |   android-chrome-512x512.png
|   |   |   apple-touch-icon.png
|   |   |   browserconfig.xml
|   |   |   CHANGELOG.md
|   |   |   empty-state.svg
|   |   |   error-illustration.svg
|   |   |   favicon-16x16.png
|   |   |   favicon-32x32.png
|   |   |   favicon.ico
|   |   |   humans.txt
|   |   |   loading-spinner.svg
|   |   |   logo-dark.svg
|   |   |   logo-light.svg
|   |   |   logo-small.png
|   |   |   logo-square.png
|   |   |   logo.svg
|   |   |   manifest.json
|   |   |   manifest.webmanifest
|   |   |   mstile-150x150.png
|   |   |   og-image.png
|   |   |   placeholder.png
|   |   |   preview-banner.svg
|   |   |   privacy-badge.svg
|   |   |   README.md
|   |   |   robots.txt
|   |   |   safari-pinned-tab.svg
|   |   |   security-badge.svg
|   |   |   site.webmanifest
|   |   |   sitemap.xml
|   |   |   social-preview.jpg
|   |   |   tailwind.css
|   |   |   theme.css
|   |   |   twitter-card.png
|   |   |
|   |   +---backgrounds
|   |   |       dark-bg.png
|   |   |       dashboard-bg.svg
|   |   |       landing-bg.jpg
|   |   |       light-bg.png
|   |   |       README.md
|   |   |
|   |   +---banners
|   |   |       beta-banner.svg
|   |   |       incident-banner.svg
|   |   |       promo-banner.png
|   |   |       README.md
|   |   |
|   |   +---brand
|   |   |       alt-logo.svg
|   |   |       full-logo.svg
|   |   |       icon.svg
|   |   |       README.md
|   |   |       wordmark.svg
|   |   |
|   |   +---downloads
|   |   |       apex-protocol-whitepaper.pdf
|   |   |       quickstart.pdf
|   |   |       README.md
|   |   |       terms-and-conditions.pdf
|   |   |       user-guide.pdf
|   |   |
|   |   +---fonts
|   |   |       custom-icons.ttf
|   |   |       Inter-Bold.woff2
|   |   |       Inter-Regular.woff2
|   |   |       README.md
|   |   |       RobotoMono-Regular.woff2
|   |   |
|   |   +---icons
|   |   |       ai-bot.png
|   |   |       ai.svg
|   |   |       alert.svg
|   |   |       arb.svg
|   |   |       dark-mode.svg
|   |   |       gas.svg
|   |   |       latency.svg
|   |   |       operator.svg
|   |   |       plugin.svg
|   |   |       README.md
|   |   |       settings.svg
|   |   |       user.svg
|   |   |       wallet.svg
|   |   |
|   |   \---onboarding
|   |           ai-demo.svg
|   |           operator.svg
|   |           README.md
|   |           step1.svg
|   |           step2.svg
|   |           step3.svg
|   |           success.svg
|   |
|   +---sandbox
|   |   |   AIOpsPlayground.jsx
|   |   |   AISandbox.jsx
|   |   |   CHANGELOG.md
|   |   |   DataVizLab.jsx
|   |   |   demo-examples.md
|   |   |   ExtensionPlayground.jsx
|   |   |   IntegrationTestPanel.jsx
|   |   |   LayoutPlayground.jsx
|   |   |   OperatorTestPanel.jsx
|   |   |   OverlaySandbox.jsx
|   |   |   patterns.md
|   |   |   README.md
|   |   |   sandbox-best-practices.md
|   |   |   sandbox.test.js
|   |   |   sandboxApi.js
|   |   |   SandboxHome.jsx
|   |   |   sandboxHotReload.js
|   |   |   sandboxState.js
|   |   |   sandboxUtils.js
|   |   |   StorybookPanel.jsx
|   |   |   ThemeSandbox.jsx
|   |   |   WidgetPlayground.jsx
|   |   |
|   |   +---demo-patterns
|   |   |       ai-prompt-lab-demo.jsx
|   |   |       data-viz-demo.jsx
|   |   |       multi-widget-demo.jsx
|   |   |       operator-alert-demo.jsx
|   |   |       overlay-motion-demo.jsx
|   |   |       README.md
|   |   |       sandbox-patterns.md
|   |   |
|   |   \---presets
|   |           ai-demo-preset.json
|   |           README.md
|   |           theme-preset.json
|   |           widget-preset.json
|   |
|   +---scripts
|   |       README.md
|   |
|   +---settings
|   |       README.md
|   |
|   +---src
|   |       README.md
|   |
|   +---state
|   |   |   aiState.js
|   |   |   analyticsState.js
|   |   |   CHANGELOG.md
|   |   |   contextBridge.js
|   |   |   devtools.js
|   |   |   edgeState.js
|   |   |   layoutState.js
|   |   |   middleware.js
|   |   |   notificationsState.js
|   |   |   operatorState.js
|   |   |   overlayState.js
|   |   |   patterns.md
|   |   |   persistStore.js
|   |   |   pluginState.js
|   |   |   presetsState.js
|   |   |   README.md
|   |   |   riskState.js
|   |   |   selectors.js
|   |   |   snapshotUtils.js
|   |   |   ssrState.js
|   |   |   state-best-practices.md
|   |   |   state.test.js
|   |   |   stateEvents.js
|   |   |   stateHistory.js
|   |   |   stateMigration.js
|   |   |   stateSubscriptions.js
|   |   |   stateSync.js
|   |   |   stateUtils.js
|   |   |   store.js
|   |   |   themeState.js
|   |   |   tradesState.js
|   |   |   userState.js
|   |   |
|   |   \---demo
|   |           demo-state.json
|   |           demo-userState.js
|   |           README.md
|   |
|   +---stats
|   |       README.md
|   |
|   +---styles
|   |   |   ar.css
|   |   |   CHANGELOG.md
|   |   |   fonts.css
|   |   |   index.css
|   |   |   minimal.css
|   |   |   mixins.scss
|   |   |   night-mode.css
|   |   |   overrides.scss
|   |   |   patterns.md
|   |   |   print.css
|   |   |   README.md
|   |   |   responsive.css
|   |   |   scrollbar.css
|   |   |   tailwind.config.js
|   |   |   tailwind.css
|   |   |   theme.css
|   |   |   transitions.css
|   |   |   utility-classes.css
|   |   |   variables.scss
|   |   |
|   |   +---animations
|   |   |       bounce.css
|   |   |       expand.css
|   |   |       fade.css
|   |   |       overlay.css
|   |   |       README.md
|   |   |       slide.css
|   |   |       spinner.css
|   |   |
|   |   +---components
|   |   |       alert.css
|   |   |       avatar.css
|   |   |       badge.css
|   |   |       button.css
|   |   |       card.css
|   |   |       chart.css
|   |   |       form.css
|   |   |       loading.css
|   |   |       menu.css
|   |   |       modal.css
|   |   |       README.md
|   |   |       table.css
|   |   |       tabs.css
|   |   |       timeline.css
|   |   |       tooltip.css
|   |   |       widget.css
|   |   |
|   |   \---palette
|   |           accessibility.css
|   |           custom-tokens.css
|   |           dark.css
|   |           light.css
|   |           operator.css
|   |           README.md
|   |           solarized.css
|   |
|   +---testData
|   |       README.md
|   |
|   +---tests
|   |   |   CHANGELOG.md
|   |   |   patterns.md
|   |   |   README.md
|   |   |   test-best-practices.md
|   |   |
|   |   +---ai
|   |   |       ai-dashboard-integration.test.py
|   |   |       ai-module-smoke.test.py
|   |   |       alpha-score.test.py
|   |   |       profit-gradient.test.py
|   |   |       README.md
|   |   |       route-selection.test.py
|   |   |       volatility-model.test.py
|   |   |
|   |   +---chaos
|   |   |       incident-chaos.test.js
|   |   |       node-crash-recovery.test.js
|   |   |       README.md
|   |   |       system-chaos.test.js
|   |   |
|   |   +---components
|   |   |       Alert.test.jsx
|   |   |       Avatar.test.jsx
|   |   |       Badge.test.jsx
|   |   |       Button.test.jsx
|   |   |       Card.test.jsx
|   |   |       Chart.test.jsx
|   |   |       Form.test.jsx
|   |   |       Loading.test.jsx
|   |   |       Menu.test.jsx
|   |   |       Modal.test.jsx
|   |   |       README.md
|   |   |       Table.test.jsx
|   |   |       Tabs.test.jsx
|   |   |       Timeline.test.jsx
|   |   |       Tooltip.test.jsx
|   |   |       Widget.test.jsx
|   |   |
|   |   +---contracts
|   |   |       alpha-nft.test.js
|   |   |       batch-executor.test.js
|   |   |       digital-twin-bridge.test.js
|   |   |       dispute-resolution.test.js
|   |   |       flashloan-arbitrage.test.js
|   |   |       governance-module.test.js
|   |   |       insurance-pool.test.js
|   |   |       intent-solver.test.js
|   |   |       operator-nft.test.js
|   |   |       README.md
|   |   |       reputation-oracle.test.js
|   |   |       upgradable-proxy.test.js
|   |   |       zk-proof.test.js
|   |   |
|   |   +---coverage
|   |   |   |   ai-coverage.test.py
|   |   |   |   backend-coverage.test.js
|   |   |   |   contracts-coverage.test.js
|   |   |   |   coverage-report.html
|   |   |   |   coverage-summary.md
|   |   |   |   lcov.info
|   |   |   |   README.md
|   |   |   |   summary.json
|   |   |   |
|   |   |   \---.nyc_output
|   |   |           README.md
|   |   |
|   |   +---docs
|   |   |       ai-testing.md
|   |   |       chaos-testing.md
|   |   |       coverage-guide.md
|   |   |       fork-testing.md
|   |   |       legacy-cases.md
|   |   |       mainnet-e2e.md
|   |   |       README.md
|   |   |       snapshot-methods.md
|   |   |       test-strategy.md
|   |   |       test-troubleshooting.md
|   |   |
|   |   +---e2e
|   |   |       ai-e2e.test.py
|   |   |       ai-panel.e2e.js
|   |   |       dashboard-e2e.test.js
|   |   |       failover-e2e.test.js
|   |   |       live-trade.e2e.js
|   |   |       mainnet-e2e.test.js
|   |   |       mobile-responsive.e2e.js
|   |   |       onboarding.e2e.js
|   |   |       plugin-marketplace.e2e.js
|   |   |       preset-switch.e2e.js
|   |   |       README.md
|   |   |       regression-suite.e2e.js
|   |   |       theme-switch.e2e.js
|   |   |
|   |   +---fixtures
|   |   |       example-analytics.json
|   |   |       example-trades.json
|   |   |       README.md
|   |   |
|   |   +---flows
|   |   |       AuthFlow.test.js
|   |   |       NotificationFlow.test.js
|   |   |       OperatorIncidentFlow.test.js
|   |   |       PluginLifecycle.test.js
|   |   |       PresetSwitchFlow.test.js
|   |   |       README.md
|   |   |       TradeExecFlow.test.js
|   |   |
|   |   +---fork
|   |   |       block-drift-fork.test.js
|   |   |       mainnet-fork.test.js
|   |   |       mempool-chaos.test.js
|   |   |       README.md
|   |   |       zk-sim-fork.test.js
|   |   |
|   |   +---fuzz
|   |   |       ai-fuzz.test.py
|   |   |       fork-fuzz.test.js
|   |   |       fuzz-arb-paths.test.js
|   |   |       plugin-fuzz.test.js
|   |   |       README.md
|   |   |
|   |   +---integration
|   |   |       ai-integration.test.py
|   |   |       contracts-integration.test.js
|   |   |       engine-integration.test.js
|   |   |       overlays-integration.test.js
|   |   |       plugins-integration.test.js
|   |   |       README.md
|   |   |       storage-integration.test.js
|   |   |       utils-integration.test.js
|   |   |       watchdog-integration.test.js
|   |   |
|   |   +---legacy
|   |   |       legacy-tests-summary.md
|   |   |       migration-checks.test.js
|   |   |       README.md
|   |   |
|   |   +---migration
|   |   |       contract-migration.test.js
|   |   |       db-migration.test.js
|   |   |       plugin-migration.test.js
|   |   |       README.md
|   |   |
|   |   +---mocks
|   |   |       mock-api.js
|   |   |       mock-plugin.json
|   |   |       mock-theme.json
|   |   |       mock-user.json
|   |   |       README.md
|   |   |
|   |   +---pages
|   |   |       AiPage.test.jsx
|   |   |       IndexPage.test.jsx
|   |   |       NotFoundPage.test.jsx
|   |   |       OperatorPage.test.jsx
|   |   |       PluginsPage.test.jsx
|   |   |       README.md
|   |   |       SettingsPage.test.jsx
|   |   |       TradesPage.test.jsx
|   |   |
|   |   +---performance
|   |   |       ai-latency-benchmark.test.py
|   |   |       fork-benchmark.test.js
|   |   |       gas-benchmark.test.js
|   |   |       README.md
|   |   |
|   |   +---plugin
|   |   |       alpha-signal-plugins.test.js
|   |   |       bridge-adapters.test.js
|   |   |       compliance-plugins.test.js
|   |   |       dex-adapters.test.js
|   |   |       flashloan-adapters.test.js
|   |   |       insurance-plugins.test.js
|   |   |       intent-solvers.test.js
|   |   |       model-marketplace.test.js
|   |   |       oracles-adapters.test.js
|   |   |       plugin-marketplace.test.js
|   |   |       README.md
|   |   |       template-plugins.test.js
|   |   |
|   |   +---python
|   |   |       ai-agent-tests.py
|   |   |       legacy-ml-tests.py
|   |   |       model-integration-tests.py
|   |   |       README.md
|   |   |       strategy-selection-tests.py
|   |   |       token-score-tests.py
|   |   |
|   |   +---regression
|   |   |       darkmode-regression.test.js
|   |   |       failed-trade-replay.test.js
|   |   |       legacy-compat.test.js
|   |   |       patch-regression.test.js
|   |   |       README.md
|   |   |       snapshot-regression.test.js
|   |   |       snapshot.test.js
|   |   |       upgrade-regression.test.js
|   |   |       visual-regression.test.js
|   |   |
|   |   +---runner
|   |   |       foundry.toml
|   |   |       hardhat.config.js
|   |   |       pytest.ini
|   |   |       README.md
|   |   |       test-runner.config.js
|   |   |
|   |   +---snapshot
|   |   |       README.md
|   |   |       snapshot-audit.test.js
|   |   |       snapshot-compare.test.js
|   |   |
|   |   +---state
|   |   |       aiState.test.js
|   |   |       analyticsState.test.js
|   |   |       edgeState.test.js
|   |   |       layoutState.test.js
|   |   |       notificationsState.test.js
|   |   |       operatorState.test.js
|   |   |       overlayState.test.js
|   |   |       pluginState.test.js
|   |   |       presetsState.test.js
|   |   |       README.md
|   |   |       riskState.test.js
|   |   |       ssrState.test.js
|   |   |       stateHistory.test.js
|   |   |       stateUtils.test.js
|   |   |       store.test.js
|   |   |       themeState.test.js
|   |   |       tradesState.test.js
|   |   |       userState.test.js
|   |   |
|   |   +---unit
|   |   |       ai-unit.test.py
|   |   |       contracts-unit.test.js
|   |   |       core-unit.test.js
|   |   |       engine-unit.test.js
|   |   |       overlays-unit.test.js
|   |   |       plugins-unit.test.js
|   |   |       README.md
|   |   |       storage-unit.test.js
|   |   |       utils-unit.test.js
|   |   |       watchdog-unit.test.js
|   |   |
|   |   \---utils
|   |           analytics-utils.test.js
|   |           api-rate-limiter-utils.test.js
|   |           arb-throttler-utils.test.js
|   |           bridge-utils.test.js
|   |           cache-manager-utils.test.js
|   |           digital-twin-utils.test.js
|   |           error-handler-utils.test.js
|   |           fee-estimator-utils.test.js
|   |           gas-profiler-utils.test.js
|   |           job-queue-utils.test.js
|   |           key-management-utils.test.js
|   |           latency-profiler-utils.test.js
|   |           log-rotator-utils.test.js
|   |           migration-helper-utils.test.js
|   |           nonce-safety-utils.test.js
|   |           privacy-zk-utils.test.js
|   |           profit-gradient-filter-utils.test.js
|   |           README.md
|   |           sim-result-compressor.test.js
|   |           simulation-utils.test.js
|   |           social-graph-utils.test.js
|   |           stateful-cache-utils.test.js
|   |           tx-bundle-utils.test.js
|   |           volatility-watchdog-utils.test.js
|   |
|   +---theme
|   |   |   CHANGELOG.md
|   |   |   fontTokens.js
|   |   |   layout.js
|   |   |   radiusTokens.js
|   |   |   README.md
|   |   |   shadowTokens.js
|   |   |   spacingTokens.js
|   |   |   theme-patterns.md
|   |   |   theme.test.js
|   |   |   themeConfig.js
|   |   |   themeHydrate.js
|   |   |   themeMiddleware.js
|   |   |   themeMigration.js
|   |   |   themeProvider.jsx
|   |   |   themeRegistry.js
|   |   |   ThemeSwitcher.jsx
|   |   |   themeTokens.js
|   |   |   themeUtils.js
|   |   |   typography.js
|   |   |   useTheme.js
|   |   |
|   |   +---demo
|   |   |       README.md
|   |   |       theme-demo.js
|   |   |       theme-gallery.md
|   |   |
|   |   +---fonts
|   |   |       custom-fonts.js
|   |   |       Inter.js
|   |   |       README.md
|   |   |       RobotoMono.js
|   |   |
|   |   \---palettes
|   |           accessibility.js
|   |           custom.js
|   |           dark.js
|   |           light.js
|   |           operator.js
|   |           README.md
|   |           solarized.js
|   |
|   +---themes
|   |       README.md
|   |
|   +---uploads
|   |   |   CHANGELOG.md
|   |   |   README.md
|   |   |
|   |   +---csv
|   |   |       ai-train-data.csv
|   |   |       analytics-demo.csv
|   |   |       custom-upload.csv
|   |   |       README.md
|   |   |       trade-log.csv
|   |   |
|   |   +---exports
|   |   |       csv-export-2025-07-31.zip
|   |   |       full-backup-2025-07-31.zip
|   |   |       README.md
|   |   |
|   |   +---logs
|   |   |       ai-session-logs.log
|   |   |       README.md
|   |   |       upload-errors-2025-07-31.log
|   |   |
|   |   +---misc
|   |   |       ai-result-report.docx
|   |   |       onboarding-demo.pdf
|   |   |       README.md
|   |   |
|   |   +---model-weights
|   |   |       custom-plugin-model.bin
|   |   |       finGPT-7b.bin
|   |   |       glm-4.5.bin
|   |   |       investlm-13b.bin
|   |   |       README.md
|   |   |       xai-tiny.onnx
|   |   |
|   |   +---presets
|   |   |       custom-operator-preset.json
|   |   |       night-trading-preset.json
|   |   |       README.md
|   |   |       user-backup-2025-07-31.json
|   |   |
|   |   \---users
|   |       |   README.md
|   |       |
|   |       \---pavan_korukonda
|   |               avatar.png
|   |               custom-ai-data.csv
|   |               README.md
|   |               uploaded-preset.json
|   |
|   +---utils
|   |       aiUtils.js
|   |       analyticsUtils.js
|   |       animationUtils.js
|   |       apiUtils.js
|   |       arbUtils.js
|   |       CHANGELOG.md
|   |       constants.js
|   |       dashboardUtils.js
|   |       dataUtils.js
|   |       demoUtils.js
|   |       enums.js
|   |       errorUtils.js
|   |       ethUtils.js
|   |       formatters.js
|   |       hotReloadUtils.js
|   |       layoutUtils.js
|   |       logger.js
|   |       mevUtils.js
|   |       patterns.md
|   |       perfUtils.js
|   |       pluginUtils.js
|   |       README.md
|   |       sandboxUtils.js
|   |       storageUtils.js
|   |       testUtils.js
|   |       themeUtils.js
|   |       tokenUtils.js
|   |       typeHelpers.js
|   |       validators.js
|   |       wsUtils.js
|   |
|   +---widgets
|   |   |   AIInsightWidget.jsx
|   |   |   AlertBannerWidget.jsx
|   |   |   ArbOpportunityWidget.jsx
|   |   |   CHANGELOG.md
|   |   |   ChartWidget.jsx
|   |   |   CircuitBreakerWidget.jsx
|   |   |   CSVPreviewWidget.jsx
|   |   |   GasWidget.jsx
|   |   |   HeatmapWidget.jsx
|   |   |   IncidentAlertWidget.jsx
|   |   |   KillSwitchWidget.jsx
|   |   |   LatencyWidget.jsx
|   |   |   ModelStatusWidget.jsx
|   |   |   OperatorControlWidget.jsx
|   |   |   OperatorStatusWidget.jsx
|   |   |   PatternDetectionWidget.jsx
|   |   |   patterns.md
|   |   |   PnLWidget.jsx
|   |   |   PresetModeWidget.jsx
|   |   |   PresetUploadWidget.jsx
|   |   |   README.md
|   |   |   RiskWidget.jsx
|   |   |   SafeModeWidget.jsx
|   |   |   SnackbarWidget.jsx
|   |   |   SpeedModeWidget.jsx
|   |   |   StatusBadgeWidget.jsx
|   |   |   SwapRouteWidget.jsx
|   |   |   TimelineWidget.jsx
|   |   |   TokenListWidget.jsx
|   |   |   TradeStatsWidget.jsx
|   |   |   UploadWidget.jsx
|   |   |   WalletStatusWidget.jsx
|   |   |   WatchdogWidget.jsx
|   |   |   WidgetDemo.jsx
|   |   |   WidgetFrame.jsx
|   |   |   WidgetLoader.jsx
|   |   |   widgets.test.js
|   |   |   WidgetSandbox.jsx
|   |   |   WidgetSettings.jsx
|   |   |   WidgetTestPanel.jsx
|   |   |   XAIWidget.jsx
|   |   |
|   |   +---ext
|   |   |       CustomPartnerWidget.jsx
|   |   |       README.md
|   |   |
|   |   \---legacy
|   |           OldPnLWidget.jsx
|   |           README.md
|   |
|   \---xai
|       |   AttentionMap.jsx
|       |   CHANGELOG.md
|       |   ChartSaliencyOverlay.jsx
|       |   FeatureAttribution.jsx
|       |   patterns.md
|       |   PredictionExplanation.jsx
|       |   README.md
|       |   SaliencyMap.jsx
|       |   TokenInsight.jsx
|       |   WidgetXAIOverlay.jsx
|       |   xai-api.js
|       |   xai.test.js
|       |   xaiConfig.js
|       |   XAIDashboardOverlay.jsx
|       |   XAIExport.jsx
|       |   xaiHooks.js
|       |   XAIInspector.jsx
|       |   XAIOverlay.jsx
|       |   XAIStatusBar.jsx
|       |   xaiTokens.js
|       |   XAIToolbar.jsx
|       |   xaiUtils.js
|       |
|       +---demo
|       |       README.md
|       |       XAIOverlayDemo.md
|       |       XAIWidgetDemo.jsx
|       |
|       \---ext
|               PartnerXAIWidget.jsx
|               README.md
|
+---data
|   |   README.md
|   |
|   +---ai-feedback
|   |       ai-decision-trace.json
|   |       ai-feedback-format-history.md
|   |       ai-labeling-samples.json
|   |       ai-misclassification.csv
|   |       ai-model-evaluation.json
|   |       ai-operator-feedback.json
|   |       ai-review-log.json
|   |       README.md
|   |
|   +---analytics
|   |   |   README.md
|   |   |
|   |   +---ai-analysis
|   |   |       README.md
|   |   |
|   |   +---ai-explainer
|   |   |       README.md
|   |   |
|   |   +---anomaly
|   |   |       README.md
|   |   |
|   |   +---dashboards
|   |   |       README.md
|   |   |
|   |   +---performance
|   |   |       README.md
|   |   |
|   |   +---regression
|   |   |       README.md
|   |   |
|   |   +---timeseries
|   |   |       README.md
|   |   |
|   |   \---trade-metrics
|   |           README.md
|   |
|   +---audit-trails
|   |       asset-flows.json
|   |       change-log.json
|   |       contract-deploy.json
|   |       dashboard-audit.json
|   |       fork-event-log.json
|   |       login-audit.json
|   |       plugin-upgrade.json
|   |       privileged-actions.json
|   |       README.md
|   |       schema-upgrade.json
|   |       system-health-audit.json
|   |       withdrawal-log.json
|   |
|   +---backups
|   |   |   backup-meta.json
|   |   |   README.md
|   |   |
|   |   +---ai-model-weights
|   |   |       README.md
|   |   |
|   |   +---compliance-snapshots
|   |   |       README.md
|   |   |
|   |   +---config-dump
|   |   |       README.md
|   |   |
|   |   +---daily
|   |   |       README.md
|   |   |
|   |   +---db-dumps
|   |   |       README.md
|   |   |
|   |   +---monthly
|   |   |       README.md
|   |   |
|   |   \---weekly
|   |           README.md
|   |
|   +---compliance-archive
|   |       aml-logs.json
|   |       audit-export-20250701.csv
|   |       compliance-events.json
|   |       compliance-versioning.json
|   |       data-retention.log
|   |       gdpr-requests.json
|   |       jurisdiction-events.json
|   |       kyc-logs.json
|   |       README.md
|   |       regulatory-changelog.json
|   |       sanctions-checks.json
|   |
|   +---export
|   |       ai-feedback-export.csv
|   |       all-in-one-export.zip
|   |       analytics-export.csv
|   |       audit-trail-export.csv
|   |       compliance-export.csv
|   |       forensics-export.csv
|   |       full-db-export.zip
|   |       model-weights-export.csv
|   |       operator-export.csv
|   |       README.md
|   |       regulatory-export.csv
|   |       simulation-export.csv
|   |       trade-history.csv
|   |
|   +---forensics
|   |       chain-events.json
|   |       contract-events.json
|   |       exploit-detections.json
|   |       failed-tx.json
|   |       fork-drift.json
|   |       fraud-alerts.json
|   |       frontrun-attempts.json
|   |       mempool-capture.json
|   |       operator-forensics-notes.md
|   |       orphan-blocks.json
|   |       README.md
|   |       reorg-events.json
|   |       snapshot-audit.json
|   |       trace-report.json
|   |
|   +---logs
|   |   |   ai-inference.log
|   |   |   alerts.log
|   |   |   audit.log
|   |   |   backend.log
|   |   |   compliance.log
|   |   |   dashboard.log
|   |   |   error.log
|   |   |   fork-sim.log
|   |   |   notification.log
|   |   |   operator.log
|   |   |   perf-debug.log
|   |   |   plugin.log
|   |   |   README.md
|   |   |   request.log
|   |   |   session.log
|   |   |   slow-query.log
|   |   |   sql-query.log
|   |   |   trades.log
|   |   |   upgrades.log
|   |   |   user-action.log
|   |   |   webhook.log
|   |   |
|   |   \---legacy
|   |           dataset-format-history.md
|   |           deprecated-benchmarks.csv
|   |           legacy-format-spec.md
|   |           log-format-history.md
|   |           old-backend.log
|   |           old-operator.log
|   |           old-synthetic-dataset.csv
|   |           old-trade.log
|   |           README.md
|   |
|   +---model-weights
|   |   |   hashes.json
|   |   |   README.md
|   |   |   weights-metadata.json
|   |   |
|   |   +---archive
|   |   |       README.md
|   |   |
|   |   +---current
|   |   |       README.md
|   |   |
|   |   \---staging
|   |           README.md
|   |
|   +---operator
|   |       device-fingerprints.json
|   |       escalation-records.json
|   |       incidents.csv
|   |       operator-feedback.json
|   |       permission-changes.log
|   |       profile.json
|   |       README.md
|   |       session-history.csv
|   |       shift-roster.json
|   |
|   +---overlays
|   |       ar-xai-events.json
|   |       incident-overlays.json
|   |       legacy-overlays.json
|   |       overlays-session-log.json
|   |       README.md
|   |
|   +---simulation-results
|   |   |   README.md
|   |   |
|   |   +---ai-batch
|   |   |       README.md
|   |   |
|   |   +---mainnet-fork
|   |   |       README.md
|   |   |
|   |   +---regression
|   |   |       README.md
|   |   |
|   |   +---scenarios
|   |   |       README.md
|   |   |
|   |   \---shadow-fork
|   |           README.md
|   |
|   +---simulation-snapshots
|   |       ai-sim-snapshot-20250701.json
|   |       README.md
|   |       snapshot-20250701.json
|   |       snapshot-20250715.json
|   |       snapshot-20250730.json
|   |       state-format-history.md
|   |
|   \---synthetic-datasets
|       |   ai-benchmark-set.csv
|       |   dataset-log.json
|       |   demo-ml-sim.csv
|       |   fake-liquidity-pools.json
|       |   fork-events.csv
|       |   README.md
|       |   sandwich-attacks.csv
|       |   synthetic-arb.csv
|       |   synthetic-prices.csv
|       |   test-scenarios.json
|       |
|       \---legacy
|               dataset-format-history.md
|               deprecated-benchmarks.csv
|               old-synthetic-dataset.csv
|               README.md
|
+---deploy
|   |   CHANGELOG.md
|   |   patterns.md
|   |   README.md
|   |
|   +---ansible
|   |   |   inventory.ini
|   |   |   playbook.yml
|   |   |   README.md
|   |   |   secrets.yml
|   |   |
|   |   +---group_vars
|   |   |       all.yml
|   |   |       prod.yml
|   |   |       README.md
|   |   |
|   |   +---roles
|   |   |   |   README.md
|   |   |   |
|   |   |   +---ai-modules
|   |   |   |       README.md
|   |   |   |
|   |   |   +---backend
|   |   |   |       README.md
|   |   |   |
|   |   |   +---dashboard
|   |   |   |       README.md
|   |   |   |
|   |   |   \---operator
|   |   |           README.md
|   |   |
|   |   \---scripts
|   |           README.md
|   |           run-all.sh
|   |
|   +---audit
|   |       audit-checklist.md
|   |       cloud-posture.md
|   |       deploy-logs.md
|   |       README.md
|   |
|   +---docker
|   |       ai-modules.Dockerfile
|   |       backend.Dockerfile
|   |       base.Dockerfile
|   |       dashboard.Dockerfile
|   |       operator.Dockerfile
|   |       README.md
|   |
|   +---docker-compose
|   |       docker-compose.dev.yml
|   |       docker-compose.override.yml
|   |       docker-compose.prod.yml
|   |       docker-compose.yml
|   |       README.md
|   |
|   +---environments
|   |       dev.env
|   |       env.example
|   |       local.env
|   |       mainnet-fork.env
|   |       preview.env
|   |       prod.env
|   |       README.md
|   |       staging.env
|   |       testnet.env
|   |       vault.env
|   |
|   +---helm
|   |   |   README.md
|   |   |
|   |   \---apex-protocol
|   |       |   Chart.yaml
|   |       |   NOTES.txt
|   |       |   README.md
|   |       |   values.yaml
|   |       |
|   |       \---templates
|   |               configmap.yaml
|   |               deployment.yaml
|   |               hpa.yaml
|   |               ingress.yaml
|   |               README.md
|   |               secrets.yaml
|   |               service.yaml
|   |
|   +---kubernetes
|   |   |   README.md
|   |   |
|   |   +---base
|   |   |       ai-modules-deployment.yaml
|   |   |       backend-deployment.yaml
|   |   |       configmap.yaml
|   |   |       dashboard-deployment.yaml
|   |   |       ingress.yaml
|   |   |       kustomization.yaml
|   |   |       namespace.yaml
|   |   |       operator-deployment.yaml
|   |   |       README.md
|   |   |       secrets.yaml
|   |   |       service.yaml
|   |   |       storage.yaml
|   |   |
|   |   \---overlays
|   |       |   README.md
|   |       |
|   |       +---dev
|   |       |       kustomization.yaml
|   |       |       README.md
|   |       |
|   |       +---local
|   |       |       kustomization.yaml
|   |       |       README.md
|   |       |
|   |       +---prod
|   |       |       kustomization.yaml
|   |       |       README.md
|   |       |
|   |       +---scripts
|   |       |       cleanup.sh
|   |       |       deploy.sh
|   |       |       README.md
|   |       |
|   |       +---staging
|   |       |       kustomization.yaml
|   |       |       README.md
|   |       |
|   |       \---testnet
|   |               kustomization.yaml
|   |               README.md
|   |
|   +---migration
|   |       001-init.sql
|   |       README.md
|   |
|   +---scripts
|   |       backup-db.sh
|   |       deploy-all.sh
|   |       healthcheck.sh
|   |       logs.sh
|   |       README.md
|   |       restore-db.sh
|   |       update-all.sh
|   |
|   +---secrets
|   |       dev.secrets.enc
|   |       example.secrets.yaml
|   |       prod.secrets.enc
|   |       README.md
|   |
|   \---terraform
|       |   main.tf
|       |   outputs.tf
|       |   provider.tf
|       |   README.md
|       |   secrets.auto.tfvars
|       |   variables.tf
|       |   versions.tf
|       |
|       +---modules
|       |   |   README.md
|       |   |
|       |   +---db
|       |   |       README.md
|       |   |
|       |   +---k8s
|       |   |       README.md
|       |   |
|       |   +---storage
|       |   |       README.md
|       |   |
|       |   \---vpc
|       |           README.md
|       |
|       \---scripts
|               apply.sh
|               plan.sh
|               README.md
|
+---docs
|   |   api-reference.md
|   |   architecture.md
|   |   backend.md
|   |   bot.md
|   |   changelog.md
|   |   ci-cd.md
|   |   cli.md
|   |   compliance.md
|   |   components.md
|   |   contracts.md
|   |   contributors.md
|   |   dashboard.md
|   |   data-flow.md
|   |   design-system.md
|   |   developer-guide.md
|   |   engine.md
|   |   environment.md
|   |   faq.md
|   |   frontend.md
|   |   getting-started.md
|   |   guidebook.md
|   |   installation.md
|   |   integration.md
|   |   legal.md
|   |   operator-guide.md
|   |   overlays.md
|   |   patterns.md
|   |   performance.md
|   |   plugins.md
|   |   quick-reference.md
|   |   README-TEMPLATE.md
|   |   README-TEMPLATE.new.md
|   |   README.md
|   |   roadmap.md
|   |   security.md
|   |   simulation.md
|   |   storage.md
|   |   tests.md
|   |   threat-model.md
|   |   user-guide.md
|   |   wall-of-fame.md
|   |   whitepaper.md
|   |
|   +---adr
|   |       0001-foundation.md
|   |       0002-ai-design.md
|   |       0003-dashboard.md
|   |       0004-engine.md
|   |       0005-mev-protection.md
|   |       README.md
|   |
|   +---ai
|   |       architecture.md
|   |       finGPT.md
|   |       investlm.md
|   |       model-weights.md
|   |       notebooks.md
|   |       pattern-learner.md
|   |       README.md
|   |       roadmap.md
|   |       scoring.md
|   |       training.md
|   |
|   +---api
|   |       auth.md
|   |       endpoints.md
|   |       patterns.md
|   |       README.md
|   |       schemas.md
|   |
|   +---audit
|   |       bug-bounty.md
|   |       compliance-checklist.md
|   |       pentest-report.md
|   |       README.md
|   |       security-audit.md
|   |
|   +---dashboard
|   |       onboarding.md
|   |       overlays.md
|   |       pages.md
|   |       plugins.md
|   |       README.md
|   |       state.md
|   |       theme.md
|   |       utils.md
|   |       widgets.md
|   |
|   +---legal
|   |       compliance.md
|   |       disclaimers.md
|   |       license.md
|   |       README.md
|   |
|   +---onboarding
|   |       auditor-onboarding.md
|   |       dev-onboarding.md
|   |       faq.md
|   |       operator-onboarding.md
|   |       README.md
|   |
|   \---patterns
|           anti-patterns.md
|           api-patterns.md
|           code-patterns.md
|           dashboard-patterns.md
|           devops-patterns.md
|           infra-patterns.md
|           operator-patterns.md
|           README.md
|
+---examples
|   |   cli-examples.txt
|   |   cli-usage.md
|   |   dashboard-examples.md
|   |   mainnet-fork-sim.md
|   |   README.md
|   |   testnet-sim.md
|   |
|   +---ai-examples
|   |       finGPT-demo.ipynb
|   |       investlm-demo.ipynb
|   |       pattern-learner-demo.ipynb
|   |       README.md
|   |       trade-ai-demo.csv
|   |
|   +---audit-qa
|   |       audit-checklist-demo.md
|   |       README.md
|   |       simulated-bug-report.md
|   |
|   +---configs
|   |       ai-module-config.json
|   |       ci-example-config.json
|   |       dashboard-preset.json
|   |       local-arb-config.json
|   |       mainnet-arb-config.json
|   |       README.md
|   |       testnet-arb-config.json
|   |
|   +---dashboard-screenshots
|   |       ai-insight-widget.png
|   |       dashboard-ar-overlay.png
|   |       dashboard-home.png
|   |       dashboard-settings.png
|   |       dashboard-trades.png
|   |       README.md
|   |
|   +---fuzzing-examples
|   |       arb-fuzzing-seed.json
|   |       fuzz-results.log
|   |       README.md
|   |
|   +---onboarding
|   |       auditor-walkthrough.md
|   |       dev-walkthrough.md
|   |       faq.md
|   |       operator-walkthrough.md
|   |       README.md
|   |
|   +---plugin-samples
|   |       ai-operator-plugin.js
|   |       custom-arb-plugin.js
|   |       demo-dex-adapter.js
|   |       README.md
|   |
|   +---simulation-runs
|   |       cached-mempool-report.md
|   |       event-stream.log
|   |       profit-heatmap.csv
|   |       README.md
|   |       simulated-arb-day.json
|   |       trade-history-short.csv
|   |
|   \---trade-history-examples
|           arb-winners-2025.csv
|           README.md
|           test-trades-2024-01.csv
|
+---logs
|   |   README.md
|   |
|   +---ai-logs
|   |       ai-inference.log
|   |       ai-scoring.log
|   |       ai-training.log
|   |       model-updates.log
|   |       README.md
|   |
|   +---analytics-logs
|   |       market-analysis.log
|   |       profit-loss-report.log
|   |       README.md
|   |       trade-performance.log
|   |
|   +---application
|   |       api-requests.log
|   |       app-events.log
|   |       error-handling.log
|   |       README.md
|   |       user-interactions.log
|   |
|   +---audit-logs
|   |       audit-trail.log
|   |       compliance-check.log
|   |       README.md
|   |       regulatory-report.log
|   |
|   +---contract-logs
|   |       contract-calls.log
|   |       contract-deployment.log
|   |       contract-errors.log
|   |       contract-updates.log
|   |       README.md
|   |
|   +---debug-logs
|   |       debug-errors.log
|   |       debug-event-stream.log
|   |       debug-requests.log
|   |       README.md
|   |
|   +---event-logs
|   |       activity-logs.log
|   |       process-events.log
|   |       README.md
|   |       system-events.log
|   |
|   +---performance-logs
|   |       cpu-usage.log
|   |       gas-usage.log
|   |       memory-usage.log
|   |       network-usage.log
|   |       README.md
|   |
|   +---security-logs
|   |       access-logs.log
|   |       breach-detection.log
|   |       login-attempts.log
|   |       permission-errors.log
|   |       README.md
|   |
|   +---system-logs
|   |       crash-reports.log
|   |       error-codes.log
|   |       README.md
|   |       system-diagnostics.log
|   |       uptime-monitor.log
|   |
|   +---transaction-logs
|   |       README.md
|   |       tx-error.log
|   |       tx-history.log
|   |       tx-performance.log
|   |
|   \---user-logs
|           README.md
|           user-activity.log
|           user-error.log
|           user-login.log
|
+---manifest
|   |   manifest.csv
|   |   manifest.json
|   |   manifest.md
|   |   README.md
|   |   tree.txt
|   |
|   +---checksums
|   |       integrity-report.md
|   |       md5sums.txt
|   |       README.md
|   |       sha256sums.txt
|   |
|   +---diffs
|   |       diff-latest.md
|   |       diff-latest.txt
|   |       diff-summary.csv
|   |       README.md
|   |
|   +---generator
|   |       manifest-generator.js
|   |       README.md
|   |       update-manifest.sh
|   |
|   +---inventory
|   |       inventory.csv
|   |       inventory.json
|   |       inventory.md
|   |       README.md
|   |
|   +---metadata
|   |       changelog-map.md
|   |       file-metadata.json
|   |       labels.yaml
|   |       README.md
|   |       repo-meta.json
|   |
|   +---stats
|   |       README.md
|   |       stats.csv
|   |       stats.json
|   |       stats.md
|   |
|   +---templates
|   |       inventory-template.csv
|   |       manifest-template.md
|   |       README.md
|   |
|   \---validation
|           check-integrity.sh
|           manifest-validator.js
|           README.md
|
+---migrations
|   |   .keep
|   |   changelog.md
|   |   migration-history.json
|   |   README.md
|   |
|   +---backup
|   |       backup-after.sql
|   |       backup-before.sql
|   |       README.md
|   |       restore.sql
|   |
|   +---contract
|   |       001-deploy-core.js
|   |       002-upgrade-v1.1.js
|   |       003-add-arb-adapter.js
|   |       010-safe-mode-patch.js
|   |       README.md
|   |
|   +---data
|   |       001-seed-operators.json
|   |       002-demo-trades.json
|   |       003-legacy-import.js
|   |       README.md
|   |
|   +---flyway
|   |       flyway.conf
|   |       README.md
|   |       V1__init.sql
|   |
|   +---plugin
|   |       001-register-plugins.js
|   |       002-upgrade-plugins.js
|   |       README.md
|   |
|   +---prisma
|   |   |   README.md
|   |   |   schema.prisma
|   |   |
|   |   \---migrations
|   |           README.md
|   |
|   +---schema
|   |       001-init.sql
|   |       002-add-operator.sql
|   |       003-arb-session.sql
|   |       010-ai-events.sql
|   |       README.md
|   |
|   \---scripts
|           check-status.sh
|           migrate-dev.sh
|           README.md
|           revert-migrations.sh
|           run-migrations.sh
|
+---overlays
|   |   README.md
|   |
|   +---ar
|   |   |   ar.test.js
|   |   |   ARConfig.js
|   |   |   ARDebugPanel.jsx
|   |   |   ARDevTools.jsx
|   |   |   AROverlay.jsx
|   |   |   ARPluginHook.jsx
|   |   |   ARStatusBar.jsx
|   |   |   README.md
|   |   |
|   |   +---demo
|   |   |       ARDemoScreenshots.md
|   |   |       ARDemoWidget.jsx
|   |   |       README.md
|   |   |
|   |   \---ext
|   |           PartnerARWidget.jsx
|   |           README.md
|   |
|   +---debug
|   |   |   debug.test.js
|   |   |   DebugConfig.js
|   |   |   DebugEventStream.jsx
|   |   |   DebugOverlay.jsx
|   |   |   DebugTracePanel.jsx
|   |   |   README.md
|   |   |
|   |   \---demo
|   |           DebugDemo.md
|   |           README.md
|   |
|   +---experimental
|   |       .keep
|   |       ObsOverlay.jsx
|   |       OverlayLabs.md
|   |       README.md
|   |
|   +---extension
|   |       OverlayExtensionAPI.js
|   |       OverlayExtensionDemo.jsx
|   |       README.md
|   |
|   +---incident
|   |   |   incident.test.js
|   |   |   IncidentActionPanel.jsx
|   |   |   IncidentBanner.jsx
|   |   |   IncidentConfig.js
|   |   |   IncidentOverlay.jsx
|   |   |   IncidentTimeline.jsx
|   |   |   README.md
|   |   |
|   |   \---demo
|   |           IncidentDemo.md
|   |           README.md
|   |
|   +---operator
|   |   |   operator.test.js
|   |   |   OperatorBanner.jsx
|   |   |   OperatorConfig.js
|   |   |   OperatorOverlay.jsx
|   |   |   OperatorProfilePanel.jsx
|   |   |   OperatorQAOverlay.jsx
|   |   |   README.md
|   |   |
|   |   \---demo
|   |           OperatorDemo.md
|   |           README.md
|   |
|   +---test
|   |       OverlayTestSuite.js
|   |       README.md
|   |
|   \---xai
|       |   AttentionMap.jsx
|       |   CHANGELOG.md
|       |   ChartSaliencyOverlay.jsx
|       |   FeatureAttribution.jsx
|       |   patterns.md
|       |   PredictionExplanation.jsx
|       |   README.md
|       |   SaliencyMap.jsx
|       |   WidgetXAIOverlay.jsx
|       |   xai-api.js
|       |   xai.test.js
|       |   xaiConfig.js
|       |   XAIExport.jsx
|       |   xaiHooks.js
|       |   XAIInspector.jsx
|       |   XAIOverlay.jsx
|       |   XAIStatusBar.jsx
|       |   xaiTokens.js
|       |   XAIToolbar.jsx
|       |   xaiUtils.js
|       |
|       +---demo
|       |       README.md
|       |       XAIOverlayDemo.md
|       |       XAIWidgetDemo.jsx
|       |
|       \---ext
|               PartnerXAIWidget.jsx
|               README.md
|
+---presets
|   |   changelog.md
|   |   README.md
|   |
|   +---ai
|   |       ai-arb-demo.json
|   |       ai-scorer-preset.json
|   |       explainability-preset.json
|   |       finGPT-preset.json
|   |       investlm-preset.json
|   |       ml-test-preset.json
|   |       pattern-learner.json
|   |       README.md
|   |
|   +---analytics
|   |       daily-pnl-report.json
|   |       dashboard-analytics.json
|   |       gas-cost-analysis.json
|   |       README.md
|   |       volatility-alerts.json
|   |
|   +---dashboard
|   |       analytics-widgets.json
|   |       dark-mode.json
|   |       default-theme.json
|   |       minimal-layout.json
|   |       night-trader-ui.json
|   |       README.md
|   |
|   +---export
|   |       backup-2025-07-31.json
|   |       README.md
|   |
|   +---migration
|   |       migrate-preset-v1-v2.js
|   |       migrate-theme-v1-v2.js
|   |       README.md
|   |
|   +---operator
|   |       ai-operator-preset.json
|   |       alerts-ui.json
|   |       gas-saver.json
|   |       operator-safe-mode.json
|   |       README.md
|   |       reporting-preset.json
|   |       wallet-preset.json
|   |
|   +---quickstart
|   |       default-quickstart.json
|   |       demo-dryrun.json
|   |       eth-testnet.json
|   |       operator-quick-preset.json
|   |       polygon-testnet.json
|   |       README.md
|   |
|   +---strategies
|   |       aggressive-arb.json
|   |       fallback-arb.json
|   |       mev-defense.json
|   |       night-mode.json
|   |       polygon-top-dexes.json
|   |       README.md
|   |       strategy-pack-2025Q3.json
|   |       usdc-weth-dai.json
|   |
|   +---templates
|   |       ai-preset-template.json
|   |       dashboard-template.json
|   |       operator-template.json
|   |       preset-template.json
|   |       README.md
|   |
|   \---user-presets
|           backup-user-preset-2025-07.json
|           my-custom-arb.json
|           my-dashboard-theme.json
|           README.md
|           saved-strategy-preset.json
|
+---public
|   |   asset-manifest.json
|   |   browserconfig.xml
|   |   CNAME
|   |   favicon.ico
|   |   humans.txt
|   |   index.html
|   |   manifest.webmanifest
|   |   README.md
|   |   robots.txt
|   |   service-worker.js
|   |   site.webmanifest
|   |
|   +---brand
|   |       banner.png
|   |       icon.png
|   |       logo-192.png
|   |       logo-512.png
|   |       logo-dark.svg
|   |       logo-light.svg
|   |       logo.svg
|   |       README.md
|   |       symbol-only.svg
|   |       wordmark.svg
|   |
|   +---css
|   |       dark-theme.css
|   |       light-theme.css
|   |       main.css
|   |       overrides.css
|   |       README.md
|   |       theme-vars.css
|   |
|   +---extensions
|   |       extension-sample-bg.jpg
|   |       partner1-logo.svg
|   |       partner2-logo.png
|   |       README.md
|   |
|   +---fonts
|   |       Inter-Bold.woff2
|   |       Inter-Regular.woff2
|   |       JetBrainsMono-Bold.woff2
|   |       JetBrainsMono-Regular.woff2
|   |       README.md
|   |       RobotoMono-Regular.ttf
|   |
|   +---icons
|   |   |   README.md
|   |   |
|   |   +---badges
|   |   |       ai.svg
|   |   |       dev.svg
|   |   |       operator.svg
|   |   |       README.md
|   |   |       verified.svg
|   |   |
|   |   +---tokens
|   |   |       arb.svg
|   |   |       btc.svg
|   |   |       dai.svg
|   |   |       link.svg
|   |   |       matic.svg
|   |   |       README.md
|   |   |       usdc.svg
|   |   |       usdt.svg
|   |   |       weth.svg
|   |   |
|   |   \---ui
|   |           alert.svg
|   |           copy.svg
|   |           danger.svg
|   |           dashboard.svg
|   |           external.svg
|   |           info.svg
|   |           operator.svg
|   |           README.md
|   |           success.svg
|   |           wallet.svg
|   |           warning.svg
|   |
|   +---img
|   |       avatar-default.png
|   |       charts-sample.png
|   |       code-examples.png
|   |       dashboard-hero-dark.jpg
|   |       dashboard-hero.jpg
|   |       empty-state.svg
|   |       hero-bg.svg
|   |       mobile-ui.png
|   |       operators.png
|   |       README.md
|   |       trade-bg.svg
|   |
|   +---legal
|   |       cookies.html
|   |       legal-disclaimer.txt
|   |       privacy-policy.html
|   |       README.md
|   |       security.txt
|   |       terms-of-use.html
|   |
|   +---meta
|   |       analytics.js
|   |       meta-tags.html
|   |       og-image-dark.png
|   |       og-image.png
|   |       preview-card.png
|   |       README.md
|   |
|   +---static
|   |       api-reference.pdf
|   |       litepaper.pdf
|   |       press-kit.zip
|   |       README.md
|   |       whitepaper.pdf
|   |
|   +---svg
|   |       ai-insight.svg
|   |       dashboard-bg.svg
|   |       README.md
|   |       trade-flow.svg
|   |
|   \---themes
|           charts.json
|           dark.json
|           light.json
|           operator-night.json
|           README.md
|
+---research
|   |   README.md
|   |   roadmap.md
|   |
|   +---alphaNFT
|   |       alpha-nft-demo-contract.sol
|   |       alpha-nft-protocol.md
|   |       alpha-nft-sim.ipynb
|   |       README.md
|   |
|   +---compliance
|   |       ai-ethics.md
|   |       audit-trail-research.md
|   |       data-privacy-research.md
|   |       model-bias-analysis.md
|   |       README.md
|   |
|   +---datasets
|   |       ai-arb-examples.json
|   |       ai-labels.json
|   |       arb-benchmark.csv
|   |       mev-prediction-data.parquet
|   |       operator-actions.csv
|   |       price-history-2025.json
|   |       README.md
|   |       synthetic-pool-dataset.csv
|   |
|   +---docs
|   |       ai-arb-research-whitepaper.md
|   |       experimental-protocols.md
|   |       explainable-ai-xai.md
|   |       literature-review-2025.md
|   |       README.md
|   |       trading-sim-whitepaper.md
|   |
|   +---experiments
|   |       ai-arb-strategy.ipynb
|   |       ai-vs-human-arb-sim.md
|   |       cross-chain-arb-research.ipynb
|   |       finetune-experiments.ipynb
|   |       mev-simulation.ipynb
|   |       optimization-benchmarks.md
|   |       README.md
|   |       stealth-execution-lab.ipynb
|   |       trade-pattern-learning.ipynb
|   |
|   +---innovation
|   |       agent-autonomy-log.md
|   |       experimental-ideas-2025.md
|   |       hackathon-2025-log.md
|   |       proposal-ai-xai.md
|   |       proposal-rust-backend.md
|   |       README.md
|   |
|   +---logs
|   |       ai-experiment-error.log
|   |       data-pipeline-debug.log
|   |       README.md
|   |       research-run-log-2025-07-31.txt
|   |
|   +---notebooks
|   |       agent-cooperation.ipynb
|   |       ai-risk-score.ipynb
|   |       alpha-nft-experiments.ipynb
|   |       dashboard-insight-research.ipynb
|   |       ml-eda-arb-dataset.ipynb
|   |       profit-predictor-training.ipynb
|   |       quantum-sim-2025.ipynb
|   |       README.md
|   |       synthetic-data-gen.ipynb
|   |
|   +---quantum
|   |       quantum-arb-sim.md
|   |       quantum-experiment.ipynb
|   |       quantum-safe-protocols.md
|   |       README.md
|   |       toy-qiskit-demo.py
|   |
|   +---results
|   |       ai-experiment-leaderboard.md
|   |       cross-chain-arb-results.json
|   |       gas-usage-benchmark.csv
|   |       profit-predictor-results.csv
|   |       README.md
|   |       summary-2025Q3.md
|   |
|   \---swarm
|           collaborative-llm-training.ipynb
|           edge-ml-agent-research.md
|           README.md
|           swarm-arb-sim.ipynb
|
+---scripts
|   |   backup-data.sh
|   |   check-project-tree.js
|   |   check-status.sh
|   |   ci-build.sh
|   |   clean-logs.sh
|   |   deploy-contracts.js
|   |   fetch-external-data.js
|   |   generate-report.js
|   |   manifest-generator.js
|   |   migrate-dev.sh
|   |   monitor-prices.js
|   |   README.md
|   |   restore-data.sh
|   |   revert-migrations.sh
|   |   run-migrations.sh
|   |   run-simulation.js
|   |   simulate-arbitrage.js
|   |   start-bot.sh
|   |   testnet-deploy.js
|   |   update-manifest.sh
|   |   update-plugins.sh
|   |   verify-contract.js
|   |   wallet-balance-check.js
|   |
|   +---automation
|   |       clean-temp-files.sh
|   |       nightly-backup.sh
|   |       README.md
|   |       sync-docker-images.sh
|   |
|   +---operator
|   |       check-health.sh
|   |       log-rotation.sh
|   |       operator-alert.sh
|   |       README.md
|   |
|   +---playbook
|   |       emergency-shutdown.sh
|   |       liquidity-reset.sh
|   |       README.md
|   |       restart-bot.sh
|   |
|   +---quickstart
|   |       ci-build.sh
|   |       demo-run.sh
|   |       README.md
|   |       start-dev.sh
|   |       testnet-deploy.sh
|   |
|   +---setup
|   |       configure-env.sh
|   |       install-dependencies.sh
|   |       node-setup.sh
|   |       README.md
|   |       setup-venv.sh
|   |
|   +---tree
|   |       generate-tree.sh
|   |       README.md
|   |       update-manifest.sh
|   |       validate-manifest.sh
|   |
|   \---update
|           README.md
|           update-ai-models.sh
|           update-dex-lists.sh
|           upgrade-contracts.sh
|
+---storage
|   |   README.md
|   |
|   +---agent-snapshots
|   |       agent-state-2025-07-31.json
|   |       agent-state-2025-08-01.json
|   |       decision-heatmap.png
|   |       model-checkpoint-epoch50.bin
|   |       model-checkpoint-epoch75.bin
|   |       README.md
|   |       reward-curve.png
|   |       sim-snapshot-ai-trades-2025-07.json
|   |       training-metrics-2025-07.log
|   |
|   +---key-vault
|   |       README.md
|   |       recovery-instructions.md
|   |       vault-backup-2025-07-31.enc
|   |       vault-backup-2025-08-01.enc
|   |       vault-temp.json
|   |       vault.enc
|   |
|   +---secret-backups
|   |       api-keys-backup-2025-07.json.enc
|   |       config-secrets-2025-07.json.enc
|   |       operator-tokens.enc
|   |       pgp-keyring-backup.asc
|   |       README.md
|   |       rotation-log.md
|   |
|   +---strat-archives
|   |       arb-strat-v1-2025-07.json
|   |       arb-strat-v2-2025-08.json
|   |       fallback-strategy-v1.json
|   |       README.md
|   |       risk-profile-v2.json
|   |       strat-archive-2025-07-31.zip
|   |       strat-archive-2025-08-01.zip
|   |       strat-metadata.json
|   |
|   \---temp
|           autosave-agent.tmp
|           cache-temp.json
|           checksum-verification.log
|           partial-download.tmp
|           README.md
|           unzipped-strategy-preview.json
|           upload-queue.json
|           validator-temp-matrix.csv
|
+---tests
|   |   foundry.toml
|   |   hardhat.config.test.js
|   |   README.md
|   |   test-entrypoint.sh
|   |   test-runner.config.js
|   |
|   +---ai
|   |       README.md
|   |       test-agentModelOverfitting.py
|   |       test-aiRollUnderPredictor.py
|   |       test-decisionReplayValidator.py
|   |       test-latencyScorerModel.py
|   |       test-profitPredictorModel.py
|   |       test-simulatedTradeForecast.py
|   |       test-volatilityWatchdog.py
|   |
|   +---cli
|   |       README.md
|   |       test-botLaunchPrompt.js
|   |       test-configPresetLoad.js
|   |       test-hotkeyExitAndResume.js
|   |       test-interactiveSession.js
|   |       test-modeSelectorInput.js
|   |
|   +---contracts
|   |       arbExecutor.test.js
|   |       eventEmitters.test.js
|   |       fallbackRouterLogic.test.js
|   |       flashloanArb.test.js
|   |       proxyUpgradeFlow.test.js
|   |       README.md
|   |       strategyRegistry.test.js
|   |
|   +---coverage
|   |       README.md
|   |
|   +---e2e
|   |       README.md
|   |       test-botLaunchToProfit.js
|   |       test-botOperatorControl.js
|   |       test-profitWithdrawFlow.js
|   |       test-reentryRecoveryFlow.js
|   |       test-txnReversionSafeExit.js
|   |
|   +---error-snapshots
|   |       crash-2025-07-30.json
|   |       README.md
|   |
|   +---fuzz
|   |       fuzz-parameterLimits.sol
|   |       fuzz-reserveImbalance.py
|   |       fuzz-simulationIntegrity.js
|   |       fuzz-tokenSequence.py
|   |       fuzz-unusualPairRoutes.js
|   |       README.md
|   |
|   +---integration
|   |       README.md
|   |       test-aiOracleIntegration.js
|   |       test-alertWebhookIntegration.js
|   |       test-configPresetLinking.js
|   |       test-dashboardToEngine.js
|   |       test-dexArbFlow.js
|   |       test-eventSyncBus.js
|   |
|   +---mocks
|   |       mockBlockState.json
|   |       mockDEXPair.json
|   |       mockExecutionLogs.json
|   |       mockOracle.js
|   |       mockRouterResponse.json
|   |       mockTokenList.json
|   |       mockWalletConfig.json
|   |       README.md
|   |
|   +---regression
|   |       README.md
|   |       regression-dexDesyncBug.test.js
|   |       regression-outdatedOracleSkip.test.js
|   |       regression-pendingTxCrash.test.js
|   |       regression-simulationMismatch.test.js
|   |       regression-slippageCapFailure.test.js
|   |       regression-txRevertHistory.test.js
|   |
|   +---reports
|   |       lint-and-test-status.json
|   |       model-accuracy-report-2025-07.csv
|   |       README.md
|   |       test-coverage-summary.html
|   |       test-report-2025-07.xml
|   |
|   +---snapshot
|   |       data-snapshot-compare.test.py
|   |       profitSnapshotChecker.js
|   |       README.md
|   |       snapshotConsistencyChecker.js
|   |       snapshotTrainerStability.test.py
|   |       state-snapshot-restore.test.js
|   |
|   +---snapshots
|   |       arb-engine-snapshot.json
|   |       model-replay-checkpoint-75.json
|   |       README.md
|   |
|   +---unit
|   |       README.md
|   |       test-arbEngine.spec.js
|   |       test-gasOptimizer.spec.js
|   |       test-priceFetchCache.spec.js
|   |       test-profitCalc.spec.js
|   |       test-routerAdapter.spec.js
|   |       test-slippageController.spec.js
|   |       test-tokenReputation.spec.js
|   |       test-utils.spec.js
|   |       test-watchdogTrigger.spec.js
|   |
|   \---watchdog
|           README.md
|           test-autoRestartLoop.js
|           test-circuitBreakerTrip.js
|           test-highGasSpikeRejection.js
|           test-liquidityFailoverRoute.js
|           test-spikeDetection.js
|
+---third-party
|   |   README.md
|   |
|   +---adapters
|   |       betswirl-dice-adapter.ts
|   |       oneinch-split-router.ts
|   |       paraswap-router-integration.js
|   |       README.md
|   |       stargate-liquidity-bridge.ts
|   |       velodrome-v2-adapter.ts
|   |       zksync-router-mock.ts
|   |
|   +---bots
|   |       archer-relay-sim.js
|   |       bloxroute-tx-broadcaster.js
|   |       flashbots-tx-bundler.js
|   |       jito-relay-adapter.ts
|   |       README.md
|   |       starknet-bridge-simulator.js
|   |
|   +---compliance-hooks
|   |       audit-log-exporter.js
|   |       chainalysis-screening.ts
|   |       compliance-cache.json
|   |       README.md
|   |       safe-blocklist-fetcher.js
|   |       trmlabs-sanctions-check.js
|   |
|   +---connectors
|   |       balancer-v2-connector.js
|   |       camelot-arbitrum.js
|   |       kyber-dmm-connector.js
|   |       quickswap-connector.js
|   |       README.md
|   |       sushiswap-v2-connector.js
|   |       uniswap-v3-connector.js
|   |
|   +---oracles
|   |       chainlink-aggregator.ts
|   |       custom-infra-oracle.js
|   |       dia-oracle-wrapper.py
|   |       oracle-quorum-engine.ts
|   |       oracle-validator-utils.js
|   |       README.md
|   |       redstone-adapter.js
|   |
|   +---patches
|   |       aave-pool-interface-patch.sol
|   |       deploy-skip-check.patch.js
|   |       flashbots-bundler-override.js
|   |       patched-ethers-provider.ts
|   |       README.md
|   |       redstone-feed-fix.ts
|   |
|   +---schemas
|   |       ai-scorer-output-schema.json
|   |       dex-liquidity-pool-schema.json
|   |       dex-route-schema.json
|   |       flashloan-request-schema.json
|   |       mev-strategy-spec.json
|   |       oracle-feed-schema.json
|   |       README.md
|   |       token-schema.json
|   |
|   \---sdk
|           aave-v3-sdk.js
|           bloxroute-sdk-wrapper.js
|           chainlink-price-feed-sdk.js
|           ethers-ext.js
|           flashbots-provider.js
|           polygon-zkevm-sdk.ts
|           README.md
|
+---types
|   |   README.md
|   |
|   +---abi
|   |       ArbitrageExecutor.json
|   |       ERC20.json
|   |       FlashLoanArbitrage.json
|   |       OracleRegistry.json
|   |       README.md
|   |       TokenVault.json
|   |       UpgradeableBeacon.json
|   |
|   +---json
|   |       ai-score-example.json
|   |       default-config-template.json
|   |       flashloan-example.json
|   |       README.md
|   |       route-cache-template.json
|   |       test-oracle-response.json
|   |       watchdog-trigger-template.json
|   |
|   +---py
|   |       ai_prediction.py
|   |       arb_model.py
|   |       config_loader.py
|   |       flashloan_struct.py
|   |       oracle_feed.py
|   |       README.md
|   |       schema_validator.py
|   |
|   +---schema
|   |       ai-prediction.schema.json
|   |       dashboard-settings.schema.json
|   |       dex-route.schema.json
|   |       execution-report.schema.json
|   |       flashloan-request.schema.json
|   |       README.md
|   |       token.schema.json
|   |
|   +---ts
|   |       ai.types.ts
|   |       arb.types.ts
|   |       bridge.types.ts
|   |       config.types.ts
|   |       dashboard.types.ts
|   |       dex.types.ts
|   |       error.types.ts
|   |       flashloan.types.ts
|   |       oracle.types.ts
|   |       README.md
|   |       watchdog.types.ts
|   |
|   \---utils
|           abi-type-parser.ts
|           doc-generator.ts
|           interface-mapper.ts
|           normalize-types.ts
|           README.md
|           schema-validator.ts
|           ts-to-jsonschema.js
|
+---utils
|   |   README.md
|   |
|   +---converter
|   |       abiToSchema.js
|   |       jsonSchemaToTypes.js
|   |       jsonToAbi.js
|   |       README.md
|   |       tsToJsonSchema.js
|   |
|   +---devtools
|   |       dependencyChecker.js
|   |       fileTreePrinter.js
|   |       hotReloader.js
|   |       presetLoader.js
|   |       README.md
|   |       testSeedGenerator.js
|   |
|   +---formatter
|   |       executionSummaryPrinter.js
|   |       percentFormatter.js
|   |       README.md
|   |       timeFormatter.js
|   |       usdFormatter.js
|   |
|   +---gas
|   |       gasBoostPlanner.js
|   |       gasCostCalculator.js
|   |       gasEstimator.js
|   |       gasProfiler.js
|   |       mevBoostFeeScanner.js
|   |       README.md
|   |       smartGasPredictor.js
|   |
|   +---helpers
|   |       asyncQueue.js
|   |       deepClone.js
|   |       delay.js
|   |       flattenNestedJson.js
|   |       README.md
|   |       retryWithBackoff.js
|   |       throttle.js
|   |
|   +---logs
|   |       errorReporter.js
|   |       logFormatter.js
|   |       logParser.js
|   |       logReplayLoader.js
|   |       logToSQLite.js
|   |       README.md
|   |
|   +---math
|   |       arbProfitMargin.js
|   |       bnMath.js
|   |       pnlCalculator.js
|   |       README.md
|   |       safeDivision.js
|   |       slippageCalc.js
|   |
|   +---parser
|   |       abiDecoder.js
|   |       bytecodeAnalyzer.js
|   |       calldataCompressor.js
|   |       README.md
|   |       txTraceParser.js
|   |
|   +---sim
|   |       forkBlockFetcher.js
|   |       priceDeltaChecker.js
|   |       README.md
|   |       reserveImbalanceDetector.js
|   |       simRouteValidator.js
|   |       simSnapSaver.js
|   |       slippageGuard.js
|   |
|   +---validator
|   |       chainHealthChecker.js
|   |       configSanityChecker.js
|   |       envVarChecker.js
|   |       README.md
|   |       routeSanityValidator.js
|   |
|   \---watchers
|           errorSpikeWatcher.js
|           liquidityWatcher.js
|           mempoolWatcher.js
|           priceDriftWatcher.js
|           README.md
|
+---vendor
|   |   README.md
|   |
|   +---abi
|   |       aaveV3LendingPool.json
|   |       arbExecutor.json
|   |       balancerVault.json
|   |       chainlinkAggregator.json
|   |       flashloanArbitrage.json
|   |       quickswapRouter.json
|   |       README.md
|   |       uniswapV2Router.json
|   |       uniswapV3Pool.json
|   |
|   +---binaries
|   |       abi-parser.wasm
|   |       bytecode-sigtool.wasm
|   |       graph-cli.wasm
|   |       mev-trace-analyzer.exe
|   |       README.md
|   |       sqlite3.dll
|   |       sqlite3.so
|   |
|   +---contracts
|   |       AaveV3PoolInterface.sol
|   |       BalancerVaultInterface.sol
|   |       FlashLoanReceiverBase.sol
|   |       IERC20.sol
|   |       README.md
|   |       SafeERC20.sol
|   |       SafeMath.sol
|   |       UniswapV2Library.sol
|   |       UniV3TickMath.sol
|   |
|   +---datasets
|   |       aave-historical-flashloan.csv
|   |       chainlink-oracle-history.json
|   |       mev-inspector-dataset.json
|   |       profit-patterns.csv
|   |       README.md
|   |
|   +---dex-liquidity-snapshots
|   |       2025-07-27.json
|   |       2025-07-28.json
|   |       2025-07-29.json
|   |       latest.json
|   |       README.md
|   |
|   +---libs
|   |       ajv.bundle.js
|   |       ethers-v5.js
|   |       lodash.min.js
|   |       merkle-tools.min.js
|   |       moment-timezone.js
|   |       multicall.js
|   |       README.md
|   |
|   +---patches
|   |       aave-interface-fix.sol
|   |       ethers-provider-patch.js
|   |       jsonrpc-batch-fix.js
|   |       node-fetch-esm-patch.js
|   |       README.md
|   |       redstone-deviation-fix.js
|   |
|   \---scripts
|           export-datasets.py
|           fetch-mev-patterns.py
|           freeze-deps.sh
|           integrity-hash-check.sh
|           README.md
|           update-abi-cache.js
|
+---wall-of-fame
|   |   CONTRIBUTORS.md
|   |   README.md
|   |
|   +---badges
|   |       bug-slayer-badge.svg
|   |       docs-champion-badge.svg
|   |       early-contributor-badge.svg
|   |       innovation-badge.svg
|   |       mentor-badge.svg
|   |       qa-defender-badge.svg
|   |       README.md
|   |       reviewer-badge.svg
|   |       top-committer-badge.svg
|   |
|   +---recognition-events
|   |       awards-ceremony-2025.md
|   |       community-celebration-2025.md
|   |       contributor-appreciation-day-2025.md
|   |       github-recognition-week.md
|   |       README.md
|   |       team-retreat-hackathon.md
|   |
|   +---recognitions
|   |       ai-contribution-award.md
|   |       excellence-in-innovation.md
|   |       leadership-award.md
|   |       open-source-evangelist.md
|   |       outstanding-community-service.md
|   |       README.md
|   |
|   \---testimonials
|           ai-lead-reflection.md
|           alice-jones-testimonial.md
|           dev-ops-intern-testimonial.md
|           jane-smith-testimonial.md
|           john-doe-testimonial.md
|           README.md
|
\---watchdog
        autoRestart.js
        circuitBreaker.js
        eventMonitor.js
        executionGuard.js
        executionWindowLimiter.js
        failoverRouteManager.js
        gasSpikeWatcher.js
        integrationTestWatchdog.js
        killSwitch.js
        latencySpikeDetector.js
        liquidityDriftWatcher.js
        mempoolAnomalyDetector.js
        oracleSyncChecker.js
        README.md
        README.schema.json
        rpcHealthMonitor.js
        slippageDeviationGuard.js
        stuckTransactionScanner.js
        tradeFailureMonitor.js
        volatilityWatchdog.js
        watchdogConfig.json
        watchdogController.js
        watchdogHooks.js

```	ext
