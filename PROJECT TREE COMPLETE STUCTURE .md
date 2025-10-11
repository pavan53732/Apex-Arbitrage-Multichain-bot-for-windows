
Apex Arbitrage Multichain bot/



ª   .dockerignore
ª   .editorconfig
ª   .env
ª   .env.example
ª   .eslintrc
ª   .flake8
ª   .gitignore
ª   .prettierrc
ª   .stylelintrc
ª   ai-feedback.sqlite
ª   ai-training.sqlite
ª   analytics.sqlite
ª   api_reference.md
ª   audit-trail.sqlite
ª   backup-meta.json
ª   Bot Blue Print.md
ª   CHANGELOG.md
ª   CODE_OF_CONDUCT.md
ª   compliance.sqlite
ª   CONTRIBUTING.md
ª   Dashboard.md
ª   docker-compose.yml
ª   forensics.sqlite
ª   HEALTHCHECK.md
ª   LEGAL.md
ª   LICENSE
ª   logs.sqlite
ª   Makefile
ª   manifest.csv
ª   manifest.json
ª   manifest.md
ª   operator-guide.md
ª   package.json
ª   PROJECT FILES AND FOLDERS DETAILS .MD
ª   PROJECT TREE COMPLETE STUCTURE .md
ª   README.md
ª   requirements.txt
ª   roadmap.md
ª   SECURITY.md
ª   tsconfig.json
ª   wall-of-fame.md
ª   
+---.devcontainer
ª       devcontainer.json
ª       Dockerfile
ª       env.example
ª       extensions.json
ª       postCreateCommand.sh
ª       README.md
ª       requirements.txt
ª       settings.json
ª       
+---.github
ª   ª   CODEOWNERS
ª   ª   dependabot.yml
ª   ª   FUNDING.yml
ª   ª   README.md
ª   ª   SECURITY.md
ª   ª   support.md
ª   ª   
ª   +---ISSUE_TEMPLATE
ª   ª       bug_report.md
ª   ª       feature_request.md
ª   ª       general_question.md
ª   ª       README.md
ª   ª       
ª   +---PULL_REQUEST_TEMPLATE
ª   ª       pull_request.md
ª   ª       README.md
ª   ª       
ª   +---workflows
ª           ci.yml
ª           deploy.yml
ª           lint.yml
ª           monitor.yml
ª           README.md
ª           sync-fork.yml
ª           test.yml
ª           
+---.husky
ª       commit-msg
ª       commitlint.config.js
ª       lint-staged.config.js
ª       pre-commit
ª       pre-push
ª       README.md
ª       
+---.vscode
ª       extensions.json
ª       launch.json
ª       README.md
ª       settings.json
ª       tasks.json
ª       
+---ai-modules
ª   ª   Ai modules.txt
ª   ª   ai-engine.js
ª   ª   aiConfig.json
ª   ª   decisionMaker.js
ª   ª   modelRouter.js
ª   ª   patternLearner.js
ª   ª   README.md
ª   ª   scoreArbOpportunity.js
ª   ª   tokenReputationIndex.py
ª   ª   tradeOutcomeLogger.js
ª   ª   
ª   +---datasets
ª   ª       ai-decision-corpus.json
ª   ª       features.csv
ª   ª       profitLabels.json
ª   ª       README.md
ª   ª       trade-history.csv
ª   ª       
ª   +---features
ª   ª       featureExtractor.js
ª   ª       gasFeeSpikeFeature.js
ª   ª       latencyProfileFeature.js
ª   ª       priceDeltaFeature.js
ª   ª       README.md
ª   ª       
ª   +---integration
ª   ª       aiBridgeAdapter.js
ª   ª       aiHooks.js
ª   ª       aiLogFormatter.js
ª   ª       aiWebhookReceiver.js
ª   ª       README.md
ª   ª       
ª   +---models
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---modelWeights
ª   ª   ª       decisionNet-v1.pt
ª   ª   ª       patternNet-v2.onnx
ª   ª   ª       README.md
ª   ª   ª       scorerModel.json
ª   ª   ª       volatilityClassifier.pkl
ª   ª   ª       
ª   ª   +---trainingOutputs
ª   ª           accuracy-report.txt
ª   ª           README.md
ª   ª           token-risk-score-histogram.png
ª   ª           trade-learning-curve.png
ª   ª           
ª   +---notebooks
ª   ª       latency-vs-profit.ipynb
ª   ª       model-training-logistics.ipynb
ª   ª       README.md
ª   ª       risk-surface-analysis.ipynb
ª   ª       trade-pattern-exploration.ipynb
ª   ª       
ª   +---simulation
ª   ª       aiReplayValidator.js
ª   ª       analyzeAIErrorCases.js
ª   ª       README.md
ª   ª       simulateAITrade.js
ª   ª       
ª   +---tests
ª   ª       README.md
ª   ª       testFeatureExtractor.test.js
ª   ª       testModelRouter.test.js
ª   ª       testPatternLearner.test.js
ª   ª       testScoreArbOpportunity.test.js
ª   ª       
ª   +---train
ª           config.yaml
ª           evaluate.py
ª           preprocess.py
ª           README.md
ª           train.py
ª           trainFineTune.py
ª           
+---archive
ª   ª   archive.txt
ª   ª   README.md
ª   ª   
ª   +---archived-tests
ª   ª   ª   aiScoring-legacy.test.js
ª   ª   ª   README.md
ª   ª   ª   testLegacyFlashloan.js
ª   ª   ª   tradeSamples-v1.json
ª   ª   ª   
ª   ª   +---archived-output-logs
ª   ª           ai-trace-legacy.log
ª   ª           README.md
ª   ª           trade-diffs-old.json
ª   ª           tx-failure-snapshots.log
ª   ª           
ª   +---deprecated-modules
ª   ª   ª   flashloan-logic-legacy.sol
ª   ª   ª   legacy-arbEngine-v1.js
ª   ª   ª   old-ai-model.py
ª   ª   ª   README.md
ª   ª   ª   route-cache-old.js
ª   ª   ª   
ª   ª   +---ui-backup-2023-12
ª   ª           app.js
ª   ª           index.html
ª   ª           main.css
ª   ª           README.md
ª   ª           
ª   +---docs
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---api-diffs
ª   ª   ª       contracts-diff-v1-v2.md
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---compliance-logs
ª   ª   ª       audit-2023Q2.md
ª   ª   ª       audit-2024-GDPR-report.md
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---deprecation-notices
ª   ª   ª       deprecated-flashloan-2023.md
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---incident-reports
ª   ª   ª       incident-2023-07-22.md
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---migration-notes
ª   ª   ª       migration-v2.0.md
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---old-adrs
ª   ª   ª       adr-001-example.md
ª   ª   ª       adr-002-example.md
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---onboarding
ª   ª   ª       onboarding-v1.md
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---playbooks
ª   ª           failover-v1.sh
ª   ª           README.md
ª   ª           runbook-legacy.md
ª   ª           
ª   +---migrations-logs
ª   ª       db-schema-v1.sql
ª   ª       migration-2024-12-20.log
ª   ª       migration-2025-06-01.log
ª   ª       migration-2025-07-15.log
ª   ª       migration-failures.log
ª   ª       migration-summary.csv
ª   ª       README.md
ª   ª       
ª   +---old-configs
ª   ª       chains-v1.json
ª   ª       dexes-legacy.json
ª   ª       flashloanParams-v1.json
ª   ª       README.md
ª   ª       risk-profiles-archive.json
ª   ª       strategy-params-legacy.yaml
ª   ª       tokens-old.json
ª   ª       
ª   +---previous-releases
ª           README.md
ª           release-notes-v1.md
ª           release-v1.0.zip
ª           release-v1.1-beta.zip
ª           release-v1.2-integrity.sha256
ª           release-v1.2.zip
ª           
+---backend
ª   ª   .eslintrc
ª   ª   .flake8
ª   ª   .gitignore
ª   ª   .prettierrc
ª   ª   .stylelintrc
ª   ª   api_reference.md
ª   ª   CHANGELOG.md
ª   ª   CONTRIBUTING.md
ª   ª   docker-compose.yml
ª   ª   Dockerfile
ª   ª   jest.config.js
ª   ª   LICENSE
ª   ª   Makefile
ª   ª   operator-guide.md
ª   ª   package.json
ª   ª   pyproject.toml
ª   ª   README.md
ª   ª   requirements.txt
ª   ª   SECURITY.md
ª   ª   tsconfig.json
ª   ª   
ª   +---backup
ª   ª       README.md
ª   ª       
ª   +---contracts
ª   ª   ª   AlphaNFT.sol
ª   ª   ª   ArbitrageExecutor.sol
ª   ª   ª   DigitalTwinBridge.sol
ª   ª   ª   DisputeResolution.sol
ª   ª   ª   Events.sol
ª   ª   ª   FlashLoanArbitrage.sol
ª   ª   ª   GovernanceModule.sol
ª   ª   ª   InsurancePool.sol
ª   ª   ª   IntentSolver.sol
ª   ª   ª   OperatorNFT.sol
ª   ª   ª   QuantumReadyModule.sol
ª   ª   ª   README.md
ª   ª   ª   ReputationOracle.sol
ª   ª   ª   SocialImpactDistributor.sol
ª   ª   ª   UpgradableProxy.sol
ª   ª   ª   
ª   ª   +---docs
ª   ª   ª       ai-agent-integration.md
ª   ª   ª       audits.md
ª   ª   ª       contract-architecture.md
ª   ª   ª       coverage-report.md
ª   ª   ª       cross-chain-bridges.md
ª   ª   ª       digital-twin-architecture.md
ª   ª   ª       events-reference.md
ª   ª   ª       formal-verification.md
ª   ª   ª       governance-design.md
ª   ª   ª       insurance-mechanisms.md
ª   ª   ª       interface-specs.md
ª   ª   ª       plugin-architecture.md
ª   ª   ª       quantum-resilience.md
ª   ª   ª       README.md
ª   ª   ª       test-playbooks.md
ª   ª   ª       upgradeability.md
ª   ª   ª       
ª   ª   +---interfaces
ª   ª   ª       IAIAgentInterface.sol
ª   ª   ª       IAIOracle.sol
ª   ª   ª       IAlphaNFT.sol
ª   ª   ª       IAlphaSignal.sol
ª   ª   ª       IBridge.sol
ª   ª   ª       ICompliance.sol
ª   ª   ª       IDEXAdapter.sol
ª   ª   ª       IDigitalTwinBridge.sol
ª   ª   ª       IERC20.sol
ª   ª   ª       IFlashLoanProvider.sol
ª   ª   ª       IForkSimulation.sol
ª   ª   ª       IGovernance.sol
ª   ª   ª       IInsurance.sol
ª   ª   ª       IIntentSolver.sol
ª   ª   ª       IOperatorNFT.sol
ª   ª   ª       IOracle.sol
ª   ª   ª       IPluginMarket.sol
ª   ª   ª       IReputationOracle.sol
ª   ª   ª       IRewardDistributor.sol
ª   ª   ª       ISocialImpact.sol
ª   ª   ª       IUpgradeBeacon.sol
ª   ª   ª       IZKVerifier.sol
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---scripts
ª   ª   ª       alpha-nft-mint.js
ª   ª   ª       deploy.js
ª   ª   ª       digital-twin-runner.js
ª   ª   ª       fork-test.js
ª   ª   ª       governance-init.js
ª   ª   ª       README.md
ª   ª   ª       simulate-arb.js
ª   ª   ª       snapshot.js
ª   ª   ª       upgrade.js
ª   ª   ª       verify.js
ª   ª   ª       
ª   ª   +---src
ª   ª       ª   README.md
ª   ª       ª   
ª   ª       +---executors
ª   ª       ª       alpha-signal-executor.sol
ª   ª       ª       arb-executor.sol
ª   ª       ª       batch-executor.sol
ª   ª       ª       digital-twin-executor.sol
ª   ª       ª       governance-executor.sol
ª   ª       ª       insurance-executor.sol
ª   ª       ª       liquidation-executor.sol
ª   ª       ª       plugin-executor.sol
ª   ª       ª       README.md
ª   ª       ª       sandbox-executor.sol
ª   ª       ª       
ª   ª       +---governance
ª   ª       ª       dispute-manager.sol
ª   ª       ª       fork-voting.sol
ª   ª       ª       governance-token.sol
ª   ª       ª       proposal-registry.sol
ª   ª       ª       README.md
ª   ª       ª       timelock.sol
ª   ª       ª       voting.sol
ª   ª       ª       
ª   ª       +---interfaces
ª   ª       ª       IAIAgentInterface.sol
ª   ª       ª       IAlphaFeed.sol
ª   ª       ª       IArbScore.sol
ª   ª       ª       IAudit.sol
ª   ª       ª       IExecutionModule.sol
ª   ª       ª       IIncident.sol
ª   ª       ª       IRewardVault.sol
ª   ª       ª       IUpgradeBeacon.sol
ª   ª       ª       README.md
ª   ª       ª       
ª   ª       +---onchain-governance
ª   ª       ª       council.sol
ª   ª       ª       dao.sol
ª   ª       ª       fork-consensus.sol
ª   ª       ª       proposal-factory.sol
ª   ª       ª       README.md
ª   ª       ª       upgrade-voting.sol
ª   ª       ª       
ª   ª       +---proofs
ª   ª       ª       ai-audit.sol
ª   ª       ª       audit-proof.sol
ª   ª       ª       fraud-proof.sol
ª   ª       ª       quantum-proof.sol
ª   ª       ª       README.md
ª   ª       ª       replay-attack-guard.sol
ª   ª       ª       zk-proof.sol
ª   ª       ª       zk-snark-utils.sol
ª   ª       ª       
ª   ª       +---registries
ª   ª       ª       address-registry.sol
ª   ª       ª       asset-registry.sol
ª   ª       ª       module-registry.sol
ª   ª       ª       nft-registry.sol
ª   ª       ª       operator-registry.sol
ª   ª       ª       plugin-registry.sol
ª   ª       ª       README.md
ª   ª       ª       
ª   ª       +---test
ª   ª               alpha-nft.test.js
ª   ª               batch-executor.test.js
ª   ª               digital-twin-bridge.test.js
ª   ª               dispute-resolution.test.js
ª   ª               flashloan-arbitrage.test.js
ª   ª               governance-module.test.js
ª   ª               insurance-pool.test.js
ª   ª               intent-solver.test.js
ª   ª               operator-nft.test.js
ª   ª               README.md
ª   ª               reputation-oracle.test.js
ª   ª               upgradable-proxy.test.js
ª   ª               zk-proof.test.js
ª   ª               
ª   +---core
ª   ª   ª   agent-orchestrator.js
ª   ª   ª   ai-controller.js
ª   ª   ª   alpha-signal-broadcaster.js
ª   ª   ª   automated-risk-manager.js
ª   ª   ª   bridge-scanner.js
ª   ª   ª   bundle-composer.js
ª   ª   ª   cross-market-adapter.js
ª   ª   ª   digital-twin-simulator.js
ª   ª   ª   execute-arbitrage.js
ª   ª   ª   failover-engine.js
ª   ª   ª   gas-optimizer.js
ª   ª   ª   incident-response-core.js
ª   ª   ª   index.js
ª   ª   ª   liquidity-scanner.js
ª   ª   ª   mev-defender.js
ª   ª   ª   module-sandbox.js
ª   ª   ª   monitor-prices.js
ª   ª   ª   parallel-sim-runner.js
ª   ª   ª   profit-safeguard.js
ª   ª   ª   prompt-sync-input.js
ª   ª   ª   README.md
ª   ª   ª   shadow-bot-manager.js
ª   ª   ª   simulate-trade.js
ª   ª   ª   
ª   ª   +---data
ª   ª   ª   ª   active-pools.json
ª   ª   ª   ª   README.md
ª   ª   ª   ª   route-cache.json
ª   ª   ª   ª   state-history.log
ª   ª   ª   ª   
ª   ª   ª   +---simulation-snapshots
ª   ª   ª           README.md
ª   ª   ª           snapshot-20250701.json
ª   ª   ª           snapshot-20250715.json
ª   ª   ª           snapshot-20250730.json
ª   ª   ª           
ª   ª   +---docs
ª   ª   ª       architecture.md
ª   ª   ª       core-flowcharts.md
ª   ª   ª       migration-notes.md
ª   ª   ª       quickstart.md
ª   ª   ª       README.md
ª   ª   ª       troubleshooting.md
ª   ª   ª       
ª   ª   +---hooks
ª   ª   ª       README.md
ª   ª   ª       use-alerts-hook.js
ª   ª   ª       use-bundle-status.js
ª   ª   ª       use-rollback-hook.js
ª   ª   ª       use-simulation-hook.js
ª   ª   ª       
ª   ª   +---tests
ª   ª   ª   ª   bundle-composer.test.js
ª   ª   ª   ª   core-unit.test.js
ª   ª   ª   ª   digital-twin-simulator.test.js
ª   ª   ª   ª   failover-engine.test.js
ª   ª   ª   ª   incident-response-core.test.js
ª   ª   ª   ª   README.md
ª   ª   ª   ª   
ª   ª   ª   +---hooks
ª   ª   ª           README.md
ª   ª   ª           use-alerts-hook.test.js
ª   ª   ª           use-bundle-status.test.js
ª   ª   ª           use-rollback-hook.test.js
ª   ª   ª           use-simulation-hook.test.js
ª   ª   ª           
ª   ª   +---utils
ª   ª           api-rate-limiter.js
ª   ª           context-propagator.js
ª   ª           error-reporter.js
ª   ª           job-queue.js
ª   ª           logger.js
ª   ª           nonce-manager.js
ª   ª           README.md
ª   ª           stateful-cache.js
ª   ª           
ª   +---coverage
ª   ª       README.md
ª   ª       
ª   +---data
ª   ª   ª   active-pools.json
ª   ª   ª   agent-scores.json
ª   ª   ª   ai-evaluations.json
ª   ª   ª   compliance-log.json
ª   ª   ª   fork-state-diff.json
ª   ª   ª   incident-log.json
ª   ª   ª   market-depth.json
ª   ª   ª   operator-profiles.json
ª   ª   ª   oracle-feed-cache.json
ª   ª   ª   plugin-usage.json
ª   ª   ª   profit-log.json
ª   ª   ª   README.md
ª   ª   ª   risk-events.json
ª   ª   ª   route-cache.json
ª   ª   ª   simulation-runs.json
ª   ª   ª   state-history.log
ª   ª   ª   token-metadata.json
ª   ª   ª   trade-history.json
ª   ª   ª   
ª   ª   +---ai-feedback
ª   ª   ª       feedback-20250701.json
ª   ª   ª       feedback-20250715.json
ª   ª   ª       feedback-20250730.json
ª   ª   ª       model-update-requests.json
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---analytics
ª   ª   ª       ai-inference-20250701.json
ª   ª   ª       ai-inference-20250715.json
ª   ª   ª       ai-inference-20250730.json
ª   ª   ª       anomaly-events-20250730.json
ª   ª   ª       pool-liquidity-report-20250701.json
ª   ª   ª       pool-liquidity-report-20250715.json
ª   ª   ª       pool-liquidity-report-20250730.json
ª   ª   ª       README.md
ª   ª   ª       trade-alpha-scores-20250701.json
ª   ª   ª       trade-alpha-scores-20250715.json
ª   ª   ª       trade-alpha-scores-20250730.json
ª   ª   ª       
ª   ª   +---audit-trails
ª   ª   ª       audit-20250701.log
ª   ª   ª       audit-20250715.log
ª   ª   ª       audit-20250730.log
ª   ª   ª       event-archive-20250701.json
ª   ª   ª       event-archive-20250715.json
ª   ª   ª       event-archive-20250730.json
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---compliance-archive
ª   ª   ª       kyc-report-20250701.pdf
ª   ª   ª       kyc-report-20250715.pdf
ª   ª   ª       kyc-report-20250730.pdf
ª   ª   ª       README.md
ª   ª   ª       sanctions-check-20250701.json
ª   ª   ª       sanctions-check-20250715.json
ª   ª   ª       sanctions-check-20250730.json
ª   ª   ª       
ª   ª   +---export
ª   ª   ª       ai-inference-export-20250701.json
ª   ª   ª       dashboard-report-20250730.pdf
ª   ª   ª       export-20250701.csv
ª   ª   ª       export-20250715.csv
ª   ª   ª       export-20250730.csv
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---forensics
ª   ª   ª       exploit-dump-20250701.json
ª   ª   ª       exploit-dump-20250715.json
ª   ª   ª       exploit-dump-20250730.json
ª   ª   ª       README.md
ª   ª   ª       root-cause-analysis.md
ª   ª   ª       trade-anomaly-20250730.json
ª   ª   ª       
ª   ª   +---logs
ª   ª   ª       ai-agent-20250701.log
ª   ª   ª       ai-agent-20250715.log
ª   ª   ª       ai-agent-20250730.log
ª   ª   ª       engine-20250701.log
ª   ª   ª       engine-20250715.log
ª   ª   ª       engine-20250730.log
ª   ª   ª       error-20250701.log
ª   ª   ª       error-20250715.log
ª   ª   ª       error-20250730.log
ª   ª   ª       README.md
ª   ª   ª       rotation-policy.md
ª   ª   ª       trades-20250701.log
ª   ª   ª       trades-20250715.log
ª   ª   ª       trades-20250730.log
ª   ª   ª       watchdog-20250701.log
ª   ª   ª       watchdog-20250715.log
ª   ª   ª       watchdog-20250730.log
ª   ª   ª       
ª   ª   +---operator-audit
ª   ª   ª       ai-review-20250715.json
ª   ª   ª       nlp-feedback-20250730.json
ª   ª   ª       operator-actions-20250701.json
ª   ª   ª       operator-actions-20250715.json
ª   ª   ª       operator-actions-20250730.json
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---simulation-snapshots
ª   ª   ª       post-fork-sim-20250715.json
ª   ª   ª       pre-fork-sim-20250715.json
ª   ª   ª       README.md
ª   ª   ª       risk-test-20250715.json
ª   ª   ª       snapshot-20250701.json
ª   ª   ª       snapshot-20250715.json
ª   ª   ª       snapshot-20250730.json
ª   ª   ª       
ª   ª   +---snapshots
ª   ª   ª       agents-20250701.json
ª   ª   ª       agents-20250715.json
ª   ª   ª       agents-20250730.json
ª   ª   ª       latest-snapshot.json
ª   ª   ª       pools-20250701.json
ª   ª   ª       pools-20250715.json
ª   ª   ª       pools-20250730.json
ª   ª   ª       README.md
ª   ª   ª       sim-20250701.json
ª   ª   ª       sim-20250715.json
ª   ª   ª       sim-20250730.json
ª   ª   ª       
ª   ª   +---synthetic-datasets
ª   ª           deep-arb-ai-trainset.csv
ª   ª           fake-arb-scenarios.json
ª   ª           README.md
ª   ª           sim-synthetic-events.json
ª   ª           synthetic-prices-20250701.csv
ª   ª           synthetic-prices-20250715.csv
ª   ª           synthetic-profits-20250730.csv
ª   ª           
ª   +---docs
ª   ª   ª   ai-integration.md
ª   ª   ª   architecture.md
ª   ª   ª   backend-api.md
ª   ª   ª   backend-stack.md
ª   ª   ª   ci-cd.md
ª   ª   ª   code-quality.md
ª   ª   ª   compliance.md
ª   ª   ª   contract-integration.md
ª   ª   ª   data-pipeline.md
ª   ª   ª   db-schema.md
ª   ª   ª   event-handling.md
ª   ª   ª   event-reference.md
ª   ª   ª   failover-guide.md
ª   ª   ª   faq.md
ª   ª   ª   fork-testing.md
ª   ª   ª   formal-verification.md
ª   ª   ª   incident-response.md
ª   ª   ª   logging-monitoring.md
ª   ª   ª   mainnet-deployment.md
ª   ª   ª   mainnet-hardening.md
ª   ª   ª   module-development.md
ª   ª   ª   notification-guide.md
ª   ª   ª   operator-guide.md
ª   ª   ª   operator-roles.md
ª   ª   ª   plugin-architecture.md
ª   ª   ª   quickstart.md
ª   ª   ª   README.md
ª   ª   ª   release-notes.md
ª   ª   ª   risk-management.md
ª   ª   ª   roadmap.md
ª   ª   ª   security.md
ª   ª   ª   simulation-workflow.md
ª   ª   ª   test-strategy.md
ª   ª   ª   upgradeability.md
ª   ª   ª   
ª   ª   +---ai
ª   ª   ª       ai-engine.md
ª   ª   ª       ai-ml-pipeline.md
ª   ª   ª       ai-models.md
ª   ª   ª       ai-ops-guide.md
ª   ª   ª       ai-testing-guide.md
ª   ª   ª       ai-upgradeability.md
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---api
ª   ª   ª       ai-engine-api.yaml
ª   ª   ª       backend-api.yaml
ª   ª   ª       dashboard-api.yaml
ª   ª   ª       notification-api.yaml
ª   ª   ª       plugin-api.yaml
ª   ª   ª       README.md
ª   ª   ª       simulation-api.yaml
ª   ª   ª       
ª   ª   +---compliance
ª   ª   ª       aml-logs.md
ª   ª   ª       compliance-audit.md
ª   ª   ª       data-retention.md
ª   ª   ª       kyc-flow.md
ª   ª   ª       README.md
ª   ª   ª       sanctions-workflow.md
ª   ª   ª       
ª   ª   +---dashboard
ª   ª   ª       ai-dashboard.md
ª   ª   ª       dashboard-api.md
ª   ª   ª       dashboard-architecture.md
ª   ª   ª       live-analytics-guide.md
ª   ª   ª       notification-integration.md
ª   ª   ª       overlays-integration.md
ª   ª   ª       plugin-status-panel.md
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---diagrams
ª   ª   ª       ai-integration.drawio
ª   ª   ª       backend-architecture.drawio
ª   ª   ª       ci-cd-pipeline.drawio
ª   ª   ª       data-pipeline.drawio
ª   ª   ª       failover-diagram.drawio
ª   ª   ª       fork-testing.drawio
ª   ª   ª       incident-response.drawio
ª   ª   ª       operator-dashboard.drawio
ª   ª   ª       plugin-system.drawio
ª   ª   ª       README.md
ª   ª   ª       risk-flow.drawio
ª   ª   ª       simulation-workflow.drawio
ª   ª   ª       
ª   ª   +---formal
ª   ª   ª       ai-formal-verification.md
ª   ª   ª       contract-formal-verification.md
ª   ª   ª       formal-verification-report.md
ª   ª   ª       invariants.md
ª   ª   ª       model-specs.md
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---legacy
ª   ª   ª       deprecated-architecture.md
ª   ª   ª       legacy-api.md
ª   ª   ª       legacy-upgrade-guide.md
ª   ª   ª       old-release-notes.md
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---migration
ª   ª   ª       ai-migration.md
ª   ª   ª       backend-migration.md
ª   ª   ª       contract-migration.md
ª   ª   ª       db-migration.md
ª   ª   ª       plugin-migration.md
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---onboarding
ª   ª   ª       ai-module-onboarding.md
ª   ª   ª       auditor-onboarding.md
ª   ª   ª       developer-onboarding.md
ª   ª   ª       faq-onboarding.md
ª   ª   ª       operator-onboarding.md
ª   ª   ª       plugin-onboarding.md
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---playbooks
ª   ª   ª       disaster-recovery.md
ª   ª   ª       incident-playbook.md
ª   ª   ª       ops-handover.md
ª   ª   ª       README.md
ª   ª   ª       rollback-playbook.md
ª   ª   ª       upgrade-playbook.md
ª   ª   ª       
ª   ª   +---risk
ª   ª           ai-risk.md
ª   ª           bridge-risk.md
ª   ª           incident-catalog.md
ª   ª           kill-switch.md
ª   ª           mev-risk.md
ª   ª           oracle-risk.md
ª   ª           pool-risk.md
ª   ª           README.md
ª   ª           risk-dashboard.md
ª   ª           trade-risk.md
ª   ª           
ª   +---engine
ª   ª   ª   adaptive-fee-controller.js
ª   ª   ª   alpha-marketplace-engine.js
ª   ª   ª   analytics-reporter.js
ª   ª   ª   auto-strategy-composer.js
ª   ª   ª   block-profiler.js
ª   ª   ª   bundle-simulator.js
ª   ª   ª   circuit-breaker.js
ª   ª   ª   digital-twin-exec.js
ª   ª   ª   dynamic-route-manager.js
ª   ª   ª   economic-dao-governance-engine.js
ª   ª   ª   flashloan-engine.js
ª   ª   ª   fork-sync-validator.js
ª   ª   ª   liquidity-shard-manager.js
ª   ª   ª   loan-sizer.js
ª   ª   ª   mev-aware-router.js
ª   ª   ª   multi-modal-inference-engine.js
ª   ª   ª   nlp-inference-engine.js
ª   ª   ª   profit-curve-estimator.js
ª   ª   ª   queue-optimizer.js
ª   ª   ª   README.md
ª   ª   ª   result-compressor.js
ª   ª   ª   risk-mitigator.js
ª   ª   ª   state-restorer.js
ª   ª   ª   temporal-scheduler.js
ª   ª   ª   trade-batch-manager.js
ª   ª   ª   trade-throttler.js
ª   ª   ª   volatility-guard.js
ª   ª   ª   
ª   ª   +---data
ª   ª   ª   ª   README.md
ª   ª   ª   ª   
ª   ª   ª   +---analytics
ª   ª   ª   ª       engine-analytics-20250701.json
ª   ª   ª   ª       engine-analytics-20250715.json
ª   ª   ª   ª       engine-analytics-20250730.json
ª   ª   ª   ª       README.md
ª   ª   ª   ª       
ª   ª   ª   +---batch-logs
ª   ª   ª   ª       batch-20250701.log
ª   ª   ª   ª       batch-20250715.log
ª   ª   ª   ª       batch-20250730.log
ª   ª   ª   ª       README.md
ª   ª   ª   ª       
ª   ª   ª   +---sim-results
ª   ª   ª   ª       README.md
ª   ª   ª   ª       sim-20250701.json
ª   ª   ª   ª       sim-20250715.json
ª   ª   ª   ª       sim-20250730.json
ª   ª   ª   ª       
ª   ª   ª   +---snapshots
ª   ª   ª           README.md
ª   ª   ª           state-20250701.json
ª   ª   ª           state-20250715.json
ª   ª   ª           state-20250730.json
ª   ª   ª           
ª   ª   +---docs
ª   ª   ª       benchmarking.md
ª   ª   ª       change-log.md
ª   ª   ª       flashloan-engines.md
ª   ª   ª       formal-verification.md
ª   ª   ª       integration-guide.md
ª   ª   ª       performance-tuning.md
ª   ª   ª       README.md
ª   ª   ª       workflows.md
ª   ª   ª       
ª   ª   +---hooks
ª   ª   ª       README.md
ª   ª   ª       use-alerts-hook.js
ª   ª   ª       use-execution-hook.js
ª   ª   ª       use-mev-detection-hook.js
ª   ª   ª       use-rollback-hook.js
ª   ª   ª       
ª   ª   +---jobs
ª   ª   ª       auto-report-uploader.js
ª   ª   ª       README.md
ª   ª   ª       result-cleaner.js
ª   ª   ª       scheduled-job-runner.js
ª   ª   ª       
ª   ª   +---modules
ª   ª   ª       arbitrage-scanner.js
ª   ª   ª       execution-timer.js
ª   ª   ª       historical-sim-analyzer.js
ª   ª   ª       liquidity-impact-analyzer.js
ª   ª   ª       opportunity-indexer.js
ª   ª   ª       README.md
ª   ª   ª       risk-histogram.js
ª   ª   ª       slippage-simulator.js
ª   ª   ª       strategy-verifier.js
ª   ª   ª       
ª   ª   +---tests
ª   ª   ª   ª   bundle-simulator.test.js
ª   ª   ª   ª   engine-integration.test.js
ª   ª   ª   ª   fork-sync-validator.test.js
ª   ª   ª   ª   liquidity-shard-manager.test.js
ª   ª   ª   ª   profit-curve-estimator.test.js
ª   ª   ª   ª   README.md
ª   ª   ª   ª   
ª   ª   ª   +---modules
ª   ª   ª           arbitrage-scanner.test.js
ª   ª   ª           execution-timer.test.js
ª   ª   ª           liquidity-impact-analyzer.test.js
ª   ª   ª           README.md
ª   ª   ª           slippage-simulator.test.js
ª   ª   ª           strategy-verifier.test.js
ª   ª   ª           
ª   ª   +---utils
ª   ª           api-rate-limiter.js
ª   ª           bundle-utils.js
ª   ª           error-reporter.js
ª   ª           fee-estimator.js
ª   ª           logger.js
ª   ª           nonce-manager.js
ª   ª           queue-utils.js
ª   ª           README.md
ª   ª           stateful-cache.js
ª   ª           
ª   +---examples
ª   ª   ª   ai-sim-report.md
ª   ª   ª   cli-usage.txt
ª   ª   ª   config-presets.md
ª   ª   ª   dashboard-tour.md
ª   ª   ª   dryrun-results.md
ª   ª   ª   experiment-log.md
ª   ª   ª   mainnet-replay.md
ª   ª   ª   operator-demo.md
ª   ª   ª   param-quickstart.md
ª   ª   ª   plugin-demo.md
ª   ª   ª   README.md
ª   ª   ª   sim-arb-day.json
ª   ª   ª   strategy-walkthrough.md
ª   ª   ª   
ª   ª   +---ai-tuning
ª   ª   ª       ai-ablation-study-20250701.md
ª   ª   ª       ai-config-tuning-20250701.json
ª   ª   ª       ai-hyperparam-search-20250701.json
ª   ª   ª       ai-loss-curve-20250701.png
ª   ª   ª       model-selection-demo-20250701.md
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---configs
ª   ª   ª       ai-module.example.json
ª   ª   ª       chains.example.json
ª   ª   ª       dashboard.example.json
ª   ª   ª       README.md
ª   ª   ª       routers.example.json
ª   ª   ª       sample-mode-presets.json
ª   ª   ª       tokens.example.json
ª   ª   ª       
ª   ª   +---dashboard-screenshots
ª   ª   ª       ai-arb-explorer.png
ª   ª   ª       dashboard-main.png
ª   ª   ª       failover-popup.png
ª   ª   ª       fork-testing-ui.png
ª   ª   ª       governance-panel.png
ª   ª   ª       incident-popup.png
ª   ª   ª       overlays-active.png
ª   ª   ª       pool-heatmap.png
ª   ª   ª       profit-log-chart.png
ª   ª   ª       README.md
ª   ª   ª       risk-dashboard.png
ª   ª   ª       watchdog-alerts.png
ª   ª   ª       
ª   ª   +---legacy
ª   ª   ª       deprecated-sim-output.json
ª   ª   ª       legacy-arb-demo.json
ª   ª   ª       legacy-config.json
ª   ª   ª       legacy-dashboard.png
ª   ª   ª       old-cli-usage.txt
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---mainnet-tx-samples
ª   ª   ª       batch-tx-mainnet-20250701.json
ª   ª   ª       batch-tx-mainnet-20250730.json
ª   ª   ª       README.md
ª   ª   ª       tx-arb-loss-2.json
ª   ª   ª       tx-arb-profit-1.json
ª   ª   ª       tx-fork-diverge-5.json
ª   ª   ª       tx-mev-front-4.json
ª   ª   ª       tx-revert-3.json
ª   ª   ª       
ª   ª   +---research-demos
ª   ª   ª       ai-scorer-demo.md
ª   ª   ª       alpha-patterns-demo.md
ª   ª   ª       fork-testing-demo.md
ª   ª   ª       gas-cost-demo.md
ª   ª   ª       plugin-benchmark-demo.md
ª   ª   ª       profit-gradient-demo.md
ª   ª   ª       README.md
ª   ª   ª       volatility-profile-demo.md
ª   ª   ª       
ª   ª   +---sim-outputs
ª   ª           ai-feedback-20250701.json
ª   ª           ai-trade-outputs-20250701.json
ª   ª           dryrun-output-20250701.log
ª   ª           dryrun-output-20250730.log
ª   ª           README.md
ª   ª           sim-run-20250701.json
ª   ª           sim-run-20250715.json
ª   ª           sim-run-20250730.json
ª   ª           
ª   +---legacy
ª   ª       README.md
ª   ª       
ª   +---migrations
ª   ª   ª   migration-manifest.json
ª   ª   ª   README.md
ª   ª   ª   VERSIONS.md
ª   ª   ª   
ª   ª   +---ai
ª   ª   ª   ª   README.md
ª   ª   ª   ª   v1.0-load-base-model.py
ª   ª   ª   ª   v1.1-finetune-volatility.py
ª   ª   ª   ª   v1.2-update-weights.py
ª   ª   ª   ª   v1.3-score-thresholds.json
ª   ª   ª   ª   v1.4-dashboard-pipeline.py
ª   ª   ª   ª   
ª   ª   ª   +---rollback
ª   ª   ª           README.md
ª   ª   ª           v1.1-rollback.py
ª   ª   ª           v1.2-rollback.py
ª   ª   ª           v1.3-rollback.json
ª   ª   ª           
ª   ª   +---config
ª   ª   ª   ª   README.md
ª   ª   ª   ª   v1.0-defaults.json
ª   ª   ª   ª   v1.1-risk-profiles.json
ª   ª   ª   ª   v1.2-hotload-profiles.json
ª   ª   ª   ª   v1.3-operator-roles.json
ª   ª   ª   ª   v1.4-alert-thresholds.json
ª   ª   ª   ª   
ª   ª   ª   +---rollback
ª   ª   ª           README.md
ª   ª   ª           v1.1-rollback.json
ª   ª   ª           v1.2-rollback.json
ª   ª   ª           v1.3-rollback.json
ª   ª   ª           v1.4-rollback.json
ª   ª   ª           
ª   ª   +---contracts
ª   ª   ª   ª   README.md
ª   ª   ª   ª   v1.0-core-deploy.js
ª   ª   ª   ª   v1.1-governance-module.js
ª   ª   ª   ª   v1.2-insurance-pool.js
ª   ª   ª   ª   v1.3-alpha-nft.js
ª   ª   ª   ª   v1.4-intent-solver.js
ª   ª   ª   ª   v1.5-zk-proof.js
ª   ª   ª   ª   
ª   ª   ª   +---rollback
ª   ª   ª           README.md
ª   ª   ª           v1.1-revert-governance.js
ª   ª   ª           v1.2-revert-insurance.js
ª   ª   ª           v1.3-revert-alpha-nft.js
ª   ª   ª           v1.4-revert-intent-solver.js
ª   ª   ª           v1.5-revert-zk-proof.js
ª   ª   ª           
ª   ª   +---db
ª   ª   ª   ª   README.md
ª   ª   ª   ª   v1.0-init-schema.sql
ª   ª   ª   ª   v1.1-ai-feedback-schema.sql
ª   ª   ª   ª   v1.2-event-log-enhancements.sql
ª   ª   ª   ª   v1.3-metrics-dashboard.sql
ª   ª   ª   ª   v1.4-kill-switch-schema.sql
ª   ª   ª   ª   v1.5-plugin-registry.sql
ª   ª   ª   ª   
ª   ª   ª   +---rollback
ª   ª   ª           README.md
ª   ª   ª           v1.1-rollback.sql
ª   ª   ª           v1.2-rollback.sql
ª   ª   ª           v1.3-rollback.sql
ª   ª   ª           v1.4-rollback.sql
ª   ª   ª           v1.5-rollback.sql
ª   ª   ª           
ª   ª   +---legacy
ª   ª   ª       deprecated-contracts.js
ª   ª   ª       legacy-ai-weights.json
ª   ª   ª       legacy-db-schema.sql
ª   ª   ª       legacy-plugin-registry.json
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---operator
ª   ª   ª   ª   README.md
ª   ª   ª   ª   v1.0-onboarding.json
ª   ª   ª   ª   v1.1-policy-update.md
ª   ª   ª   ª   v1.2-key-rotation.json
ª   ª   ª   ª   v1.3-handover-script.js
ª   ª   ª   ª   
ª   ª   ª   +---rollback
ª   ª   ª           README.md
ª   ª   ª           v1.1-rollback.md
ª   ª   ª           v1.2-rollback.json
ª   ª   ª           v1.3-rollback.js
ª   ª   ª           
ª   ª   +---plugin
ª   ª   ª   ª   README.md
ª   ª   ª   ª   v1.0-register-core-plugins.js
ª   ª   ª   ª   v1.1-dex-fallbacks.js
ª   ª   ª   ª   v1.2-ai-indexer.js
ª   ª   ª   ª   v1.3-failover-switch.js
ª   ª   ª   ª   v1.4-governance-marketplace.js
ª   ª   ª   ª   
ª   ª   ª   +---rollback
ª   ª   ª           README.md
ª   ª   ª           v1.1-rollback.js
ª   ª   ª           v1.2-rollback.js
ª   ª   ª           v1.3-rollback.js
ª   ª   ª           v1.4-rollback.js
ª   ª   ª           
ª   ª   +---scripts
ª   ª           migrate-ai.py
ª   ª           migrate-all.js
ª   ª           migrate-config.js
ª   ª           migrate-contracts.js
ª   ª           migrate-db.js
ª   ª           migrate-operator.js
ª   ª           migrate-plugin.js
ª   ª           migration-audit-log.json
ª   ª           README.md
ª   ª           rollback-all.js
ª   ª           
ª   +---notebooks
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---ai
ª   ª   ª       ablation-studies.ipynb
ª   ª   ª       agent-explainability.ipynb
ª   ª   ª       ai-dashboard-demo.ipynb
ª   ª   ª       ai-evaluation-report.ipynb
ª   ª   ª       ai-hyperparam-search.ipynb
ª   ª   ª       alpha-replay-analysis.ipynb
ª   ª   ª       feature-engineering.ipynb
ª   ª   ª       federated-learning.ipynb
ª   ª   ª       legacy-models-benchmark.ipynb
ª   ª   ª       model-training.ipynb
ª   ª   ª       pattern-discovery.ipynb
ª   ª   ª       README.md
ª   ª   ª       reinforcement-learning.ipynb
ª   ª   ª       volatility-modeling.ipynb
ª   ª   ª       
ª   ª   +---analytics
ª   ª   ª       alpha-signal-analytics.ipynb
ª   ª   ª       dashboard-integration-demo.ipynb
ª   ª   ª       model-drift-monitoring.ipynb
ª   ª   ª       performance-tuning.ipynb
ª   ª   ª       README.md
ª   ª   ª       trade-metrics.ipynb
ª   ª   ª       
ª   ª   +---data-demo
ª   ª   ª       export-demo.ipynb
ª   ª   ª       live-feed-demo.ipynb
ª   ª   ª       quick-exploration.ipynb
ª   ª   ª       README.md
ª   ª   ª       real-vs-sim-plots.ipynb
ª   ª   ª       
ª   ª   +---economics
ª   ª   ª       funding-rate-models.ipynb
ª   ª   ª       incentive-analysis.ipynb
ª   ª   ª       insurance-models.ipynb
ª   ª   ª       liquidity-curve-analysis.ipynb
ª   ª   ª       market-sentiment.ipynb
ª   ª   ª       protocol-tvl-charts.ipynb
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---explainability
ª   ª   ª       incident-xai-audit.ipynb
ª   ª   ª       local-vs-global-xai.ipynb
ª   ª   ª       operator-xai-panel-demo.ipynb
ª   ª   ª       README.md
ª   ª   ª       saliency-map-demo.ipynb
ª   ª   ª       XAI-overview.ipynb
ª   ª   ª       
ª   ª   +---legacy
ª   ª   ª       deprecated-ai-models.ipynb
ª   ª   ª       legacy-alpha-analysis.ipynb
ª   ª   ª       legacy-engine-demo.ipynb
ª   ª   ª       legacy-ops-walkthrough.ipynb
ª   ª   ª       old-research-log.ipynb
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---MEV
ª   ª   ª       block-timing.ipynb
ª   ª   ª       frontrun-detection.ipynb
ª   ª   ª       JIT-arb-analysis.ipynb
ª   ª   ª       MEV-research-demo.ipynb
ª   ª   ª       MEV-simulation.ipynb
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---operator
ª   ª   ª       alert-incident-demo.ipynb
ª   ª   ª       audit-log-explorer.ipynb
ª   ª   ª       compliance-demo.ipynb
ª   ª   ª       governance-interaction.ipynb
ª   ª   ª       README.md
ª   ª   ª       workflow-demo.ipynb
ª   ª   ª       
ª   ª   +---simulation
ª   ª   ª       arb-simulation.ipynb
ª   ª   ª       batch-execution.ipynb
ª   ª   ª       fork-testing.ipynb
ª   ª   ª       latency-benchmark.ipynb
ª   ª   ª       README.md
ª   ª   ª       scenario-testing.ipynb
ª   ª   ª       shadow-sim-demo.ipynb
ª   ª   ª       sim-vs-real-analysis.ipynb
ª   ª   ª       simulation-outputs-demo.ipynb
ª   ª   ª       synthetic-dataset-gen.ipynb
ª   ª   ª       volatility-stress-test.ipynb
ª   ª   ª       
ª   ª   +---strategy
ª   ª           adaptive-risk.ipynb
ª   ª           dynamic-loan-sizing.ipynb
ª   ª           intent-based-routing.ipynb
ª   ª           MEV-defense-testing.ipynb
ª   ª           multi-token-arb.ipynb
ª   ª           profit-gradient-analysis.ipynb
ª   ª           README.md
ª   ª           real-vs-sim-comparison.ipynb
ª   ª           route-discovery.ipynb
ª   ª           
ª   +---onboarding
ª   ª       README.md
ª   ª       
ª   +---operator
ª   ª       README.md
ª   ª       
ª   +---overlays
ª   ª   ª   ai-action-overlay.js
ª   ª   ª   ai-audit-trail-overlay.js
ª   ª   ª   ai-debug-overlay.js
ª   ª   ª   ai-insight-panel.js
ª   ª   ª   alert-toast-overlay.js
ª   ª   ª   arbitration-overlay.js
ª   ª   ª   dashboard-overlay.js
ª   ª   ª   event-stream-overlay.js
ª   ª   ª   incident-response-overlay.js
ª   ª   ª   market-sentiment-overlay.js
ª   ª   ª   operator-health-overlay.js
ª   ª   ª   oracle-divergence-overlay.js
ª   ª   ª   plugin-status-overlay.js
ª   ª   ª   profit-loss-overlay.js
ª   ª   ª   README.md
ª   ª   ª   risk-control-overlay.js
ª   ª   ª   simulation-overlay.js
ª   ª   ª   social-impact-overlay.js
ª   ª   ª   tx-history-overlay.js
ª   ª   ª   xai-inspector.js
ª   ª   ª   
ª   ª   +---ar
ª   ª   ª   ª   ar-ai-analytics.js
ª   ª   ª   ª   ar-entrypoint.js
ª   ª   ª   ª   ar-incident-mapper.js
ª   ª   ª   ª   ar-market-overlay.js
ª   ª   ª   ª   ar-operator-analytics.js
ª   ª   ª   ª   ar-xai-visualizer.js
ª   ª   ª   ª   README.md
ª   ª   ª   ª   
ª   ª   ª   +---overlay-3d-assets
ª   ª   ª           3d-bot-avatar.glb
ª   ª   ª           3d-dashboard.glb
ª   ª   ª           3d-explain-graph.glb
ª   ª   ª           3d-gas-meter.glb
ª   ª   ª           3d-health-bar.glb
ª   ª   ª           3d-mev-shield.glb
ª   ª   ª           3d-token.glb
ª   ª   ª           README.md
ª   ª   ª           
ª   ª   +---docs
ª   ª   ª       alerting-tuning.md
ª   ª   ª       ar-integration-guide.md
ª   ª   ª       dashboard-integration.md
ª   ª   ª       incident-overlays.md
ª   ª   ª       overlays-architecture.md
ª   ª   ª       README.md
ª   ª   ª       widget-development.md
ª   ª   ª       xai-explainability.md
ª   ª   ª       
ª   ª   +---tests
ª   ª   ª   ª   ai-action-overlay.test.js
ª   ª   ª   ª   ai-audit-trail-overlay.test.js
ª   ª   ª   ª   ai-debug-overlay.test.js
ª   ª   ª   ª   ai-insight-panel.test.js
ª   ª   ª   ª   arbitration-overlay.test.js
ª   ª   ª   ª   dashboard-overlay.test.js
ª   ª   ª   ª   event-stream-overlay.test.js
ª   ª   ª   ª   incident-response-overlay.test.js
ª   ª   ª   ª   market-sentiment-overlay.test.js
ª   ª   ª   ª   oracle-divergence-overlay.test.js
ª   ª   ª   ª   plugin-status-overlay.test.js
ª   ª   ª   ª   profit-loss-overlay.test.js
ª   ª   ª   ª   README.md
ª   ª   ª   ª   risk-control-overlay.test.js
ª   ª   ª   ª   simulation-overlay.test.js
ª   ª   ª   ª   social-impact-overlay.test.js
ª   ª   ª   ª   xai-inspector.test.js
ª   ª   ª   ª   
ª   ª   ª   +---ar
ª   ª   ª   ª       ar-entrypoint.test.js
ª   ª   ª   ª       ar-incident-mapper.test.js
ª   ª   ª   ª       ar-xai-visualizer.test.js
ª   ª   ª   ª       README.md
ª   ª   ª   ª       
ª   ª   ª   +---widgets
ª   ª   ª           mev-risk-widget.test.js
ª   ª   ª           quick-arb-widget.test.js
ª   ª   ª           README.md
ª   ª   ª           wallet-health-widget.test.js
ª   ª   ª           
ª   ª   +---widgets
ª   ª           ai-status-widget.js
ª   ª           alpha-feed-widget.js
ª   ª           gas-trend-widget.js
ª   ª           governance-vote-widget.js
ª   ª           mev-risk-widget.js
ª   ª           oracle-deviation-widget.js
ª   ª           quick-arb-widget.js
ª   ª           README.md
ª   ª           time-sync-widget.js
ª   ª           tx-rollback-widget.js
ª   ª           wallet-health-widget.js
ª   ª           
ª   +---plugins
ª   ª   ª   atomic-swap-batched.ts
ª   ª   ª   bridge-latency-sniper.ts
ª   ª   ª   flash-sandwich-mm.ts
ª   ª   ª   hyper-bundle-engine.ts
ª   ª   ª   micro-latency-arb-suite.ts
ª   ª   ª   nft-gamefi-arb.ts
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---alpha-signal
ª   ª   ª   ª   ai-signal-orchestrator.js
ª   ª   ª   ª   alpha-nft-issuer.js
ª   ª   ª   ª   alpha-reputation.js
ª   ª   ª   ª   alpha-voting.js
ª   ª   ª   ª   micro-arb-detector.js
ª   ª   ª   ª   README.md
ª   ª   ª   ª   sandwich-detector.js
ª   ª   ª   ª   sniping-detector.js
ª   ª   ª   ª   trend-analyzer-v2.js
ª   ª   ª   ª   trend-analyzer.js
ª   ª   ª   ª   whale-signal.js
ª   ª   ª   ª   
ª   ª   ª   +---docs
ª   ª   ª   ª       alerts-integration.md
ª   ª   ª   ª       alpha-reputation-scores.md
ª   ª   ª   ª       alpha-signal-models.md
ª   ª   ª   ª       alpha-voting-protocol.md
ª   ª   ª   ª       arb-patterns.md
ª   ª   ª   ª       README.md
ª   ª   ª   ª       
ª   ª   ª   +---tests
ª   ª   ª           ai-signal-orchestrator.test.js
ª   ª   ª           alpha-nft-issuer.test.js
ª   ª   ª           alpha-reputation.test.js
ª   ª   ª           alpha-voting.test.js
ª   ª   ª           micro-arb-detector.test.js
ª   ª   ª           README.md
ª   ª   ª           sandwich-detector.test.js
ª   ª   ª           sniping-detector.test.js
ª   ª   ª           trend-analyzer-v2.test.js
ª   ª   ª           trend-analyzer.test.js
ª   ª   ª           whale-signal.test.js
ª   ª   ª           
ª   ª   +---bridge-adapters
ª   ª   ª   ª   avalanche-adapter.js
ª   ª   ª   ª   axelar-adapter.js
ª   ª   ª   ª   circle-cctp-adapter.js
ª   ª   ª   ª   cross-twin-adapter.js
ª   ª   ª   ª   elliptic-adapter.js
ª   ª   ª   ª   layerzero-adapter.js
ª   ª   ª   ª   polygon-zkevm-adapter.js
ª   ª   ª   ª   range-cross-chain-adapter.js
ª   ª   ª   ª   README.md
ª   ª   ª   ª   relaychain-adapter.js
ª   ª   ª   ª   symbiosis-adapter.js
ª   ª   ª   ª   wormhole-adapter.js
ª   ª   ª   ª   
ª   ª   ª   +---docs
ª   ª   ª   ª       avalanche-guide.md
ª   ª   ª   ª       bridge-integrations.md
ª   ª   ª   ª       cross-chain-security.md
ª   ª   ª   ª       polygon-zkevm-guide.md
ª   ª   ª   ª       README.md
ª   ª   ª   ª       relaychain-integration.md
ª   ª   ª   ª       
ª   ª   ª   +---tests
ª   ª   ª           avalanche-adapter.test.js
ª   ª   ª           axelar-adapter.test.js
ª   ª   ª           circle-cctp-adapter.test.js
ª   ª   ª           cross-twin-adapter.test.js
ª   ª   ª           elliptic-adapter.test.js
ª   ª   ª           layerzero-adapter.test.js
ª   ª   ª           polygon-zkevm-adapter.test.js
ª   ª   ª           range-cross-chain-adapter.test.js
ª   ª   ª           README.md
ª   ª   ª           relaychain-adapter.test.js
ª   ª   ª           symbiosis-adapter.test.js
ª   ª   ª           wormhole-adapter.test.js
ª   ª   ª           
ª   ª   +---compliance
ª   ª   ª   ª   adverse-media-scanner.js
ª   ª   ª   ª   blacklist-module.js
ª   ª   ª   ª   dispute-module.js
ª   ª   ª   ª   forensics-module.js
ª   ª   ª   ª   jurisdiction-manager.js
ª   ª   ª   ª   kyc-aml-module.js
ª   ª   ª   ª   pep-checker.js
ª   ª   ª   ª   permission-validator.js
ª   ª   ª   ª   rbac-enforcer.js
ª   ª   ª   ª   README.md
ª   ª   ª   ª   sanctions-checker.js
ª   ª   ª   ª   whitelist-module.js
ª   ª   ª   ª   
ª   ª   ª   +---docs
ª   ª   ª   ª       compliance-checks.md
ª   ª   ª   ª       forensics-guide.md
ª   ª   ª   ª       governance-controls.md
ª   ª   ª   ª       kyc-flows.md
ª   ª   ª   ª       README.md
ª   ª   ª   ª       sanctions-lists.md
ª   ª   ª   ª       
ª   ª   ª   +---tests
ª   ª   ª           adverse-media-scanner.test.js
ª   ª   ª           blacklist-module.test.js
ª   ª   ª           dispute-module.test.js
ª   ª   ª           forensics-module.test.js
ª   ª   ª           jurisdiction-manager.test.js
ª   ª   ª           kyc-aml-module.test.js
ª   ª   ª           pep-checker.test.js
ª   ª   ª           permission-validator.test.js
ª   ª   ª           rbac-enforcer.test.js
ª   ª   ª           README.md
ª   ª   ª           sanctions-checker.test.js
ª   ª   ª           whitelist-module.test.js
ª   ª   ª           
ª   ª   +---dex-adapters
ª   ª   ª   ª   aggregator-adapter.js
ª   ª   ª   ª   balancer-adapter.js
ª   ª   ª   ª   cowswap-adapter.js
ª   ª   ª   ª   curve-adapter.js
ª   ª   ª   ª   dodo-adapter.js
ª   ª   ª   ª   fraxswap-adapter.js
ª   ª   ª   ª   kyber-adapter.js
ª   ª   ª   ª   maverick-adapter.js
ª   ª   ª   ª   orca-adapter.js
ª   ª   ª   ª   pancake-adapter.js
ª   ª   ª   ª   quickswap-adapter.js
ª   ª   ª   ª   README.md
ª   ª   ª   ª   sushi-adapter.js
ª   ª   ª   ª   synthetix-adapter.js
ª   ª   ª   ª   thorchain-adapter.js
ª   ª   ª   ª   traderjoe-adapter.js
ª   ª   ª   ª   uniswap-v3-adapter.js
ª   ª   ª   ª   vertex-adapter.js
ª   ª   ª   ª   woofi-adapter.js
ª   ª   ª   ª   
ª   ª   ª   +---docs
ª   ª   ª   ª       adapter-development.md
ª   ª   ª   ª       dex-architecture.md
ª   ª   ª   ª       gas-optimizations.md
ª   ª   ª   ª       integration-guide.md
ª   ª   ª   ª       README.md
ª   ª   ª   ª       slippage-models.md
ª   ª   ª   ª       supported-dexes.md
ª   ª   ª   ª       
ª   ª   ª   +---tests
ª   ª   ª           aggregator-adapter.test.js
ª   ª   ª           balancer-adapter.test.js
ª   ª   ª           cowswap-adapter.test.js
ª   ª   ª           curve-adapter.test.js
ª   ª   ª           dodo-adapter.test.js
ª   ª   ª           fraxswap-adapter.test.js
ª   ª   ª           kyber-adapter.test.js
ª   ª   ª           maverick-adapter.test.js
ª   ª   ª           orca-adapter.test.js
ª   ª   ª           pancake-adapter.test.js
ª   ª   ª           quickswap-adapter.test.js
ª   ª   ª           README.md
ª   ª   ª           sushi-adapter.test.js
ª   ª   ª           synthetix-adapter.test.js
ª   ª   ª           thorchain-adapter.test.js
ª   ª   ª           traderjoe-adapter.test.js
ª   ª   ª           uniswap-v3-adapter.test.js
ª   ª   ª           vertex-adapter.test.js
ª   ª   ª           woofi-adapter.test.js
ª   ª   ª           
ª   ª   +---docs
ª   ª   ª       adapter-api.md
ª   ª   ª       alpha-patterns.md
ª   ª   ª       fork-testing-guide.md
ª   ª   ª       integration-scenarios.md
ª   ª   ª       mev-risk-mitigation.md
ª   ª   ª       plugin-development.md
ª   ª   ª       plugins-architecture.md
ª   ª   ª       README.md
ª   ª   ª       registry-guide.md
ª   ª   ª       smart-contract-integration.md
ª   ª   ª       
ª   ª   +---flashloan
ª   ª   ª   ª   aave-adapter.js
ª   ª   ª   ª   angle-adapter.js
ª   ª   ª   ª   compound-adapter.js
ª   ª   ª   ª   cream-adapter.js
ª   ª   ª   ª   dydx-adapter.js
ª   ª   ª   ª   flashbots-adapter.js
ª   ª   ª   ª   gearbox-adapter.js
ª   ª   ª   ª   makerdao-adapter.js
ª   ª   ª   ª   morpho-adapter.js
ª   ª   ª   ª   parasite-arb-adapter.js
ª   ª   ª   ª   radiant-adapter.js
ª   ª   ª   ª   README.md
ª   ª   ª   ª   stargate-adapter.js
ª   ª   ª   ª   
ª   ª   ª   +---docs
ª   ª   ª   ª       audit-log.md
ª   ª   ª   ª       flashloan-architecture.md
ª   ª   ª   ª       flashloan-risks.md
ª   ª   ª   ª       provider-integrations.md
ª   ª   ª   ª       README.md
ª   ª   ª   ª       upgrade-guide.md
ª   ª   ª   ª       
ª   ª   ª   +---tests
ª   ª   ª           aave-adapter.test.js
ª   ª   ª           angle-adapter.test.js
ª   ª   ª           compound-adapter.test.js
ª   ª   ª           cream-adapter.test.js
ª   ª   ª           dydx-adapter.test.js
ª   ª   ª           flashbots-adapter.test.js
ª   ª   ª           gearbox-adapter.test.js
ª   ª   ª           makerdao-adapter.test.js
ª   ª   ª           morpho-adapter.test.js
ª   ª   ª           parasite-arb-adapter.test.js
ª   ª   ª           radiant-adapter.test.js
ª   ª   ª           README.md
ª   ª   ª           stargate-adapter.test.js
ª   ª   ª           
ª   ª   +---insurance
ª   ª   ª   ª   claim-auditor.js
ª   ª   ª   ª   claim-verifier.js
ª   ª   ª   ª   coverage-oracle.js
ª   ª   ª   ª   incident-monitor.js
ª   ª   ª   ª   insurance-pool-manager.js
ª   ª   ª   ª   payout-calculator.js
ª   ª   ª   ª   premium-calculator.js
ª   ª   ª   ª   README.md
ª   ª   ª   ª   risk-assessment-plugin.js
ª   ª   ª   ª   risk-modeler.js
ª   ª   ª   ª   
ª   ª   ª   +---docs
ª   ª   ª   ª       claim-workflow.md
ª   ª   ª   ª       insurance-architecture.md
ª   ª   ª   ª       pool-audits.md
ª   ª   ª   ª       README.md
ª   ª   ª   ª       risk-assessment-methods.md
ª   ª   ª   ª       risk-models.md
ª   ª   ª   ª       
ª   ª   ª   +---tests
ª   ª   ª           claim-auditor.test.js
ª   ª   ª           claim-verifier.test.js
ª   ª   ª           coverage-oracle.test.js
ª   ª   ª           incident-monitor.test.js
ª   ª   ª           insurance-pool-manager.test.js
ª   ª   ª           payout-calculator.test.js
ª   ª   ª           premium-calculator.test.js
ª   ª   ª           README.md
ª   ª   ª           risk-assessment-plugin.test.js
ª   ª   ª           risk-modeler.test.js
ª   ª   ª           
ª   ª   +---intent-solvers
ª   ª   ª   ª   auction-intent-solver.js
ª   ª   ª   ª   batch-intent-processor.js
ª   ª   ª   ª   cow-intent-solver.js
ª   ª   ª   ª   eco-intent-solver.js
ª   ª   ª   ª   intent-forker.js
ª   ª   ª   ª   intent-merger.js
ª   ª   ª   ª   keepers-intent-solver.js
ª   ª   ª   ª   README.md
ª   ª   ª   ª   rfq-intent-solver.js
ª   ª   ª   ª   sandwich-intent-solver.js
ª   ª   ª   ª   sniper-intent-solver.js
ª   ª   ª   ª   uniswapx-intent-solver.js
ª   ª   ª   ª   
ª   ª   ª   +---docs
ª   ª   ª   ª       auction-design.md
ª   ª   ª   ª       eco-intents.md
ª   ª   ª   ª       intent-architecture.md
ª   ª   ª   ª       intent-merging.md
ª   ª   ª   ª       README.md
ª   ª   ª   ª       
ª   ª   ª   +---tests
ª   ª   ª           auction-intent-solver.test.js
ª   ª   ª           batch-intent-processor.test.js
ª   ª   ª           cow-intent-solver.test.js
ª   ª   ª           eco-intent-solver.test.js
ª   ª   ª           intent-forker.test.js
ª   ª   ª           intent-merger.test.js
ª   ª   ª           keepers-intent-solver.test.js
ª   ª   ª           README.md
ª   ª   ª           rfq-intent-solver.test.js
ª   ª   ª           sandwich-intent-solver.test.js
ª   ª   ª           sniper-intent-solver.test.js
ª   ª   ª           uniswapx-intent-solver.test.js
ª   ª   ª           
ª   ª   +---internal
ª   ª   ª       interface-definitions.ts
ª   ª   ª       migration-tool.js
ª   ª   ª       plugin-manager.ts
ª   ª   ª       plugin-utils.js
ª   ª   ª       plugins.json
ª   ª   ª       README.md
ª   ª   ª       registry.ts
ª   ª   ª       test-utils.js
ª   ª   ª       
ª   ª   +---marketplace
ª   ª   ª       governance-marketplace.js
ª   ª   ª       module-marketplace-registry.json
ª   ª   ª       module-marketplace.js
ª   ª   ª       plugin-marketplace-registry.json
ª   ª   ª       plugin-marketplace.js
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---model-marketplace
ª   ª   ª       ai-model-marketplace-registry.json
ª   ª   ª       ai-model-marketplace.js
ª   ª   ª       ai-model-metadata.json
ª   ª   ª       ai-model-proxy.js
ª   ª   ª       ai-model-validator.js
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---oracles
ª   ª   ª   ª   ai-oracle.js
ª   ª   ª   ª   chainlink-oracle.js
ª   ª   ª   ª   compliance-oracle.js
ª   ª   ª   ª   external-data-oracle.js
ª   ª   ª   ª   fallback-oracle.js
ª   ª   ª   ª   liquidity-oracle.js
ª   ª   ª   ª   onchain-oracle.js
ª   ª   ª   ª   README.md
ª   ª   ª   ª   time-weighted-oracle.js
ª   ª   ª   ª   volatility-oracle.js
ª   ª   ª   ª   zero-knowledge-oracle.js
ª   ª   ª   ª   
ª   ª   ª   +---docs
ª   ª   ª   ª       data-sources.md
ª   ª   ª   ª       oracle-integrations.md
ª   ª   ª   ª       README.md
ª   ª   ª   ª       risk-mitigation.md
ª   ª   ª   ª       zk-proofs.md
ª   ª   ª   ª       
ª   ª   ª   +---tests
ª   ª   ª           ai-oracle.test.js
ª   ª   ª           chainlink-oracle.test.js
ª   ª   ª           compliance-oracle.test.js
ª   ª   ª           external-data-oracle.test.js
ª   ª   ª           fallback-oracle.test.js
ª   ª   ª           liquidity-oracle.test.js
ª   ª   ª           onchain-oracle.test.js
ª   ª   ª           README.md
ª   ª   ª           time-weighted-oracle.test.js
ª   ª   ª           volatility-oracle.test.js
ª   ª   ª           zero-knowledge-oracle.test.js
ª   ª   ª           
ª   ª   +---social-impact
ª   ª   ª   ª   carbon-offset-module.js
ª   ª   ª   ª   charity-oracle.js
ª   ª   ª   ª   csr-audit.js
ª   ª   ª   ª   donation-router.js
ª   ª   ª   ª   esg-allocator.js
ª   ª   ª   ª   grants-engine.js
ª   ª   ª   ª   green-bond-manager.js
ª   ª   ª   ª   impact-scoring.js
ª   ª   ª   ª   impact-voting.js
ª   ª   ª   ª   README.md
ª   ª   ª   ª   
ª   ª   ª   +---docs
ª   ª   ª   ª       charity-protocols.md
ª   ª   ª   ª       csr-programs.md
ª   ª   ª   ª       esg-logic.md
ª   ª   ª   ª       impact-scoring-models.md
ª   ª   ª   ª       README.md
ª   ª   ª   ª       social-impact-flows.md
ª   ª   ª   ª       
ª   ª   ª   +---tests
ª   ª   ª           carbon-offset-module.test.js
ª   ª   ª           charity-oracle.test.js
ª   ª   ª           csr-audit.test.js
ª   ª   ª           donation-router.test.js
ª   ª   ª           esg-allocator.test.js
ª   ª   ª           grants-engine.test.js
ª   ª   ª           green-bond-manager.test.js
ª   ª   ª           impact-scoring.test.js
ª   ª   ª           impact-voting.test.js
ª   ª   ª           README.md
ª   ª   ª           
ª   ª   +---template
ª   ª   ª       adapter-template.js
ª   ª   ª       model-template.js
ª   ª   ª       plugin-template.js
ª   ª   ª       README.md
ª   ª   ª       template-config.json
ª   ª   ª       
ª   ª   +---tests
ª   ª           ai-model-marketplace.test.js
ª   ª           atomic-swap-batched.test.ts
ª   ª           bridge-latency-sniper.test.ts
ª   ª           flash-sandwich-mm.test.ts
ª   ª           governance-marketplace.test.js
ª   ª           hyper-bundle-engine.test.ts
ª   ª           micro-latency-arb-suite.test.ts
ª   ª           nft-gamefi-arb.test.ts
ª   ª           plugin-manager.test.js
ª   ª           plugins-integration.test.js
ª   ª           README.md
ª   ª           test-utils.js
ª   ª           
ª   +---research
ª   ª   ª   ai-experiments.md
ª   ª   ª   economic-module-report.md
ª   ª   ª   experiment-index.md
ª   ª   ª   explainability-report.md
ª   ª   ª   innovation-log.md
ª   ª   ª   quantum-research-notes.md
ª   ª   ª   README.md
ª   ª   ª   regulatory-mapping-exploration.md
ª   ª   ª   swarm-learning-overview.md
ª   ª   ª   threat-models-research.md
ª   ª   ª   
ª   ª   +---adversarial
ª   ª   ª       adversarial-attacks.ipynb
ª   ª   ª       ai-robustness-analysis.ipynb
ª   ª   ª       cross-chain-sim-attack.ipynb
ª   ª   ª       MEV-defender-test.ipynb
ª   ª   ª       protocol-fuzz-testing.ipynb
ª   ª   ª       README.md
ª   ª   ª       recovery-strategies.ipynb
ª   ª   ª       
ª   ª   +---alphaNFT
ª   ª   ª       alphaNFT-attack-defense.ipynb
ª   ª   ª       alphaNFT-game-theory.ipynb
ª   ª   ª       alphaNFT-minting-analysis.ipynb
ª   ª   ª       alphaNFT-protocol-experiments.ipynb
ª   ª   ª       operator-nft-governance.ipynb
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---demos
ª   ª   ª       ai-interactive-sim.ipynb
ª   ª   ª       contract-governance-demo.ipynb
ª   ª   ª       dashboard-xai-demo.ipynb
ª   ª   ª       failover-event-demo.ipynb
ª   ª   ª       intent-arbitrage-demo.ipynb
ª   ª   ª       plugin-hotload-demo.ipynb
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---economics
ª   ª   ª       agent-incentives-model.ipynb
ª   ª   ª       insurance-experiment.ipynb
ª   ª   ª       liquidity-experiment.ipynb
ª   ª   ª       market-simulation-study.ipynb
ª   ª   ª       protocol-fee-analysis.ipynb
ª   ª   ª       README.md
ª   ª   ª       social-impact-analysis.ipynb
ª   ª   ª       
ª   ª   +---federated
ª   ª   ª       attack-resilience-test.ipynb
ª   ª   ª       federated-setup-demo.ipynb
ª   ª   ª       incentive-alignment.ipynb
ª   ª   ª       model-aggregation-experiments.ipynb
ª   ª   ª       node-participation-metrics.ipynb
ª   ª   ª       privacy-eval.ipynb
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---legacy
ª   ª   ª       deprecated-research-log.md
ª   ª   ª       legacy-economic-models.ipynb
ª   ª   ª       legacy-experiment-index.md
ª   ª   ª       old-xai-notebook.ipynb
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---quantum
ª   ª   ª       quantum-bridge-sim.ipynb
ª   ª   ª       quantum-experiment-notes.md
ª   ª   ª       quantum-pool-defense.ipynb
ª   ª   ª       quantum-rng-prototype.ipynb
ª   ª   ª       quantum-xai-visual.ipynb
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---swarm
ª   ª   ª       async-learning-demo.ipynb
ª   ª   ª       chain-consensus-models.ipynb
ª   ª   ª       model-update-broadcast.ipynb
ª   ª   ª       README.md
ª   ª   ª       swarm-node-behavior.ipynb
ª   ª   ª       
ª   ª   +---xai
ª   ª           ai-decision-graph.ipynb
ª   ª           live-explainability-case.ipynb
ª   ª           model-introspection-demo.ipynb
ª   ª           operator-interpretability.ipynb
ª   ª           README.md
ª   ª           xai-attack-defense.ipynb
ª   ª           xai-dashboard-demo.ipynb
ª   ª           
ª   +---storage
ª   ª   ª   access-log.json
ª   ª   ª   agent-metadata.json
ª   ª   ª   backup-secrets.enc
ª   ª   ª   keyvault.json
ª   ª   ª   legacy-wallet.json
ª   ª   ª   operator-nft-log.json
ª   ª   ª   operator-nfts.json
ª   ª   ª   README.md
ª   ª   ª   validator-registry.json
ª   ª   ª   
ª   ª   +---ai-agent-memory
ª   ª   ª   ª   ai-session-context.json
ª   ª   ª   ª   memory-20250701.json
ª   ª   ª   ª   memory-20250715.json
ª   ª   ª   ª   memory-20250730.json
ª   ª   ª   ª   README.md
ª   ª   ª   ª   
ª   ª   ª   +---memory-checkpoints
ª   ª   ª           checkpoint-1.json
ª   ª   ª           checkpoint-2.json
ª   ª   ª           checkpoint-3.json
ª   ª   ª           README.md
ª   ª   ª           
ª   ª   +---ai-agent-snapshots
ª   ª   ª   ª   ai-agent-memory-v1.json
ª   ª   ª   ª   ai-agent-memory-v2.json
ª   ª   ª   ª   ai-agent-snapshot-20250701.json
ª   ª   ª   ª   ai-agent-snapshot-20250715.json
ª   ª   ª   ª   ai-agent-snapshot-20250730.json
ª   ª   ª   ª   README.md
ª   ª   ª   ª   
ª   ª   ª   +---ai-session-logs
ª   ª   ª           README.md
ª   ª   ª           session-log-20250701.json
ª   ª   ª           session-log-20250715.json
ª   ª   ª           session-log-20250730.json
ª   ª   ª           
ª   ª   +---api-auth
ª   ª   ª       api-access-log.json
ª   ª   ª       api-key-metadata.json
ª   ª   ª       oauth-credentials.json
ª   ª   ª       README.md
ª   ª   ª       session-tokens-20250730.json
ª   ª   ª       
ª   ª   +---backup
ª   ª   ª       ai-memory-backup-20250701.json
ª   ª   ª       backup-20250701.zip
ª   ª   ª       backup-20250715.zip
ª   ª   ª       backup-20250730.zip
ª   ª   ª       config-backup-20250701.json
ª   ª   ª       contracts-backup-20250701.json
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---config-snapshots
ª   ª   ª       config-20250701.json
ª   ª   ª       config-20250715.json
ª   ª   ª       config-20250730.json
ª   ª   ª       config-latest.json
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---forensic-archive
ª   ª   ª       ai-anomaly-logs.json
ª   ª   ª       full-trace-20250730.json
ª   ª   ª       incident-evidence-20250701.zip
ª   ª   ª       incident-evidence-20250715.zip
ª   ª   ª       incident-evidence-20250730.zip
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---keys
ª   ª   ª       ai-agent-key.pem
ª   ª   ª       encryption-key.pem
ª   ª   ª       legacy-wallet.json
ª   ª   ª       mnemonic.txt
ª   ª   ª       operator-key.pem
ª   ª   ª       README.md
ª   ª   ª       signing-key.pem
ª   ª   ª       
ª   ª   +---model-weight-snapshots
ª   ª   ª       ai-governance.weights
ª   ª   ª       digital-twin.weights
ª   ª   ª       federated.weights
ª   ª   ª       README.md
ª   ª   ª       scorer.weights
ª   ª   ª       session-weights-20250701.json
ª   ª   ª       session-weights-latest.json
ª   ª   ª       volatility.weights
ª   ª   ª       
ª   ª   +---plugin-vaults
ª   ª   ª       compliance-adapter-vault.json
ª   ª   ª       dex-adapter-vault.json
ª   ª   ª       flashloan-adapter-vault.json
ª   ª   ª       oracle-adapter-vault.json
ª   ª   ª       plugin-auth-metadata.json
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---recovery-playbooks
ª   ª   ª       cold-storage-guide.md
ª   ª   ª       incident-response.md
ª   ª   ª       README.md
ª   ª   ª       restore-procedure.md
ª   ª   ª       
ª   ª   +---snapshots
ª   ª   ª       operator-balances-20250730.json
ª   ª   ª       README.md
ª   ª   ª       session-context-20250730.json
ª   ª   ª       snapshot-20250701.json
ª   ª   ª       snapshot-20250715.json
ª   ª   ª       snapshot-20250730.json
ª   ª   ª       snapshot-latest.json
ª   ª   ª       wallet-balances-20250730.json
ª   ª   ª       
ª   ª   +---strat-archive
ª   ª   ª       archived-strategies.md
ª   ª   ª       legacy-strategy.json
ª   ª   ª       README.md
ª   ª   ª       strategy-metadata.json
ª   ª   ª       strategy-v1.json
ª   ª   ª       strategy-v2.json
ª   ª   ª       
ª   ª   +---test
ª   ª           ai-agent-memory.test.js
ª   ª           backup-restore.test.js
ª   ª           config-snapshots.test.js
ª   ª           keyvault-security.test.js
ª   ª           plugin-vaults.test.js
ª   ª           README.md
ª   ª           storage-access.test.js
ª   ª           strat-archive.test.js
ª   ª           
ª   +---tests
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---ai
ª   ª   ª       ai-dashboard-integration.test.py
ª   ª   ª       ai-module-smoke.test.py
ª   ª   ª       alpha-score.test.py
ª   ª   ª       profit-gradient.test.py
ª   ª   ª       README.md
ª   ª   ª       route-selection.test.py
ª   ª   ª       volatility-model.test.py
ª   ª   ª       
ª   ª   +---chaos
ª   ª   ª       incident-chaos.test.js
ª   ª   ª       node-crash-recovery.test.js
ª   ª   ª       README.md
ª   ª   ª       system-chaos.test.js
ª   ª   ª       
ª   ª   +---contracts
ª   ª   ª       alpha-nft.test.js
ª   ª   ª       batch-executor.test.js
ª   ª   ª       digital-twin-bridge.test.js
ª   ª   ª       dispute-resolution.test.js
ª   ª   ª       flashloan-arbitrage.test.js
ª   ª   ª       governance-module.test.js
ª   ª   ª       insurance-pool.test.js
ª   ª   ª       intent-solver.test.js
ª   ª   ª       operator-nft.test.js
ª   ª   ª       README.md
ª   ª   ª       reputation-oracle.test.js
ª   ª   ª       upgradable-proxy.test.js
ª   ª   ª       zk-proof.test.js
ª   ª   ª       
ª   ª   +---coverage
ª   ª   ª   ª   ai-coverage.test.py
ª   ª   ª   ª   backend-coverage.test.js
ª   ª   ª   ª   contracts-coverage.test.js
ª   ª   ª   ª   coverage-report.html
ª   ª   ª   ª   coverage-summary.md
ª   ª   ª   ª   README.md
ª   ª   ª   ª   
ª   ª   ª   +---.nyc_output
ª   ª   ª           README.md
ª   ª   ª           
ª   ª   +---docs
ª   ª   ª       ai-testing.md
ª   ª   ª       chaos-testing.md
ª   ª   ª       coverage-guide.md
ª   ª   ª       fork-testing.md
ª   ª   ª       legacy-cases.md
ª   ª   ª       mainnet-e2e.md
ª   ª   ª       README.md
ª   ª   ª       snapshot-methods.md
ª   ª   ª       test-strategy.md
ª   ª   ª       test-troubleshooting.md
ª   ª   ª       
ª   ª   +---e2e
ª   ª   ª       ai-e2e.test.py
ª   ª   ª       dashboard-e2e.test.js
ª   ª   ª       failover-e2e.test.js
ª   ª   ª       mainnet-e2e.test.js
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---fork
ª   ª   ª       block-drift-fork.test.js
ª   ª   ª       mainnet-fork.test.js
ª   ª   ª       mempool-chaos.test.js
ª   ª   ª       README.md
ª   ª   ª       zk-sim-fork.test.js
ª   ª   ª       
ª   ª   +---fuzz
ª   ª   ª       ai-fuzz.test.py
ª   ª   ª       fork-fuzz.test.js
ª   ª   ª       fuzz-arb-paths.test.js
ª   ª   ª       plugin-fuzz.test.js
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---integration
ª   ª   ª       ai-integration.test.py
ª   ª   ª       contracts-integration.test.js
ª   ª   ª       engine-integration.test.js
ª   ª   ª       overlays-integration.test.js
ª   ª   ª       plugins-integration.test.js
ª   ª   ª       README.md
ª   ª   ª       storage-integration.test.js
ª   ª   ª       utils-integration.test.js
ª   ª   ª       watchdog-integration.test.js
ª   ª   ª       
ª   ª   +---legacy
ª   ª   ª       legacy-tests-summary.md
ª   ª   ª       migration-checks.test.js
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---migration
ª   ª   ª       contract-migration.test.js
ª   ª   ª       db-migration.test.js
ª   ª   ª       plugin-migration.test.js
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---performance
ª   ª   ª       ai-latency-benchmark.test.py
ª   ª   ª       fork-benchmark.test.js
ª   ª   ª       gas-benchmark.test.js
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---plugin
ª   ª   ª       alpha-signal-plugins.test.js
ª   ª   ª       bridge-adapters.test.js
ª   ª   ª       compliance-plugins.test.js
ª   ª   ª       dex-adapters.test.js
ª   ª   ª       flashloan-adapters.test.js
ª   ª   ª       insurance-plugins.test.js
ª   ª   ª       intent-solvers.test.js
ª   ª   ª       model-marketplace.test.js
ª   ª   ª       oracles-adapters.test.js
ª   ª   ª       plugin-marketplace.test.js
ª   ª   ª       README.md
ª   ª   ª       template-plugins.test.js
ª   ª   ª       
ª   ª   +---python
ª   ª   ª       ai-agent-tests.py
ª   ª   ª       legacy-ml-tests.py
ª   ª   ª       model-integration-tests.py
ª   ª   ª       README.md
ª   ª   ª       strategy-selection-tests.py
ª   ª   ª       token-score-tests.py
ª   ª   ª       
ª   ª   +---regression
ª   ª   ª       failed-trade-replay.test.js
ª   ª   ª       patch-regression.test.js
ª   ª   ª       README.md
ª   ª   ª       snapshot-regression.test.js
ª   ª   ª       upgrade-regression.test.js
ª   ª   ª       
ª   ª   +---runner
ª   ª   ª       foundry.toml
ª   ª   ª       hardhat.config.js
ª   ª   ª       pytest.ini
ª   ª   ª       README.md
ª   ª   ª       test-runner.config.js
ª   ª   ª       
ª   ª   +---snapshot
ª   ª   ª       README.md
ª   ª   ª       snapshot-audit.test.js
ª   ª   ª       snapshot-compare.test.js
ª   ª   ª       
ª   ª   +---unit
ª   ª   ª       ai-unit.test.py
ª   ª   ª       contracts-unit.test.js
ª   ª   ª       core-unit.test.js
ª   ª   ª       engine-unit.test.js
ª   ª   ª       overlays-unit.test.js
ª   ª   ª       plugins-unit.test.js
ª   ª   ª       README.md
ª   ª   ª       storage-unit.test.js
ª   ª   ª       utils-unit.test.js
ª   ª   ª       watchdog-unit.test.js
ª   ª   ª       
ª   ª   +---utils
ª   ª           analytics-utils.test.js
ª   ª           api-rate-limiter-utils.test.js
ª   ª           arb-throttler-utils.test.js
ª   ª           bridge-utils.test.js
ª   ª           cache-manager-utils.test.js
ª   ª           digital-twin-utils.test.js
ª   ª           error-handler-utils.test.js
ª   ª           fee-estimator-utils.test.js
ª   ª           gas-profiler-utils.test.js
ª   ª           job-queue-utils.test.js
ª   ª           key-management-utils.test.js
ª   ª           latency-profiler-utils.test.js
ª   ª           log-rotator-utils.test.js
ª   ª           migration-helper-utils.test.js
ª   ª           nonce-safety-utils.test.js
ª   ª           privacy-zk-utils.test.js
ª   ª           profit-gradient-filter-utils.test.js
ª   ª           README.md
ª   ª           sim-result-compressor.test.js
ª   ª           simulation-utils.test.js
ª   ª           social-graph-utils.test.js
ª   ª           stateful-cache-utils.test.js
ª   ª           tx-bundle-utils.test.js
ª   ª           volatility-watchdog-utils.test.js
ª   ª           
ª   +---utils
ª   ª   ª   ai-sandbox.js
ª   ª   ª   analytics.js
ª   ª   ª   api-rate-limiter.js
ª   ª   ª   arb-throttler.js
ª   ª   ª   bridge-utils.js
ª   ª   ª   browser-tools.js
ª   ª   ª   cache-manager.js
ª   ª   ª   cli-utils.js
ª   ª   ª   context-propagator.js
ª   ª   ª   cryptography-utils.js
ª   ª   ª   digital-twin.js
ª   ª   ª   env-loader.js
ª   ª   ª   error-handler.js
ª   ª   ª   error-reporter.js
ª   ª   ª   esg-impact-utils.js
ª   ª   ª   fee-estimator.js
ª   ª   ª   fork-sync-validator.js
ª   ª   ª   gas-profiler.js
ª   ª   ª   incident-helper.js
ª   ª   ª   job-queue.js
ª   ª   ª   json-schema-validator.js
ª   ª   ª   key-management.js
ª   ª   ª   latency-profiler.js
ª   ª   ª   license-checker.js
ª   ª   ª   log-rotator.js
ª   ª   ª   migration-helper.js
ª   ª   ª   nonce-safety.js
ª   ª   ª   notification.js
ª   ª   ª   plugin-loader.js
ª   ª   ª   privacy-zk-utils.js
ª   ª   ª   profit-gradient-filter.js
ª   ª   ª   README.md
ª   ª   ª   sim-result-compressor.js
ª   ª   ª   simulation.js
ª   ª   ª   snapshot-manager.js
ª   ª   ª   social-graph-utils.js
ª   ª   ª   stateful-cache.js
ª   ª   ª   token-reputation-index.py
ª   ª   ª   trade-history.js
ª   ª   ª   tx-bundle-utils.js
ª   ª   ª   volatility-watchdog.js
ª   ª   ª   webhook-helper.js
ª   ª   ª   
ª   ª   +---docs
ª   ª   ª       api-rate-limiter.md
ª   ª   ª       error-handling.md
ª   ª   ª       migration-helper-guide.md
ª   ª   ª       plugin-loader-guide.md
ª   ª   ª       privacy-zk-utils.md
ª   ª   ª       README.md
ª   ª   ª       snapshot-manager.md
ª   ª   ª       usage-examples.md
ª   ª   ª       utils-overview.md
ª   ª   ª       
ª   ª   +---test
ª   ª           ai-sandbox.test.js
ª   ª           analytics.test.js
ª   ª           browser-tools.test.js
ª   ª           cache-manager.test.js
ª   ª           digital-twin.test.js
ª   ª           error-handler.test.js
ª   ª           fee-estimator.test.js
ª   ª           job-queue.test.js
ª   ª           migration-helper.test.js
ª   ª           nonce-safety.test.js
ª   ª           privacy-zk-utils.test.js
ª   ª           README.md
ª   ª           simulation.test.js
ª   ª           token-reputation-index.test.py
ª   ª           webhook-helper.test.js
ª   ª           
ª   +---watchdog
ª       ª   auto-restart.js
ª       ª   block-watchdog.js
ª       ª   circuit-breaker.js
ª       ª   event-listener.js
ª       ª   failover-manager.js
ª       ª   gas-spike-watchdog.js
ª       ª   incident-response-core.js
ª       ª   mev-alerts.js
ª       ª   notification-manager.js
ª       ª   README.md
ª       ª   revert-reason-logger.js
ª       ª   risk-trigger-handler.js
ª       ª   threshold-config.json
ª       ª   trade-kill-switch.js
ª       ª   watchdog-daemon.js
ª       ª   
ª       +---data
ª       ª   ª   event-history.log
ª       ª   ª   health-metrics.json
ª       ª   ª   last-restart.log
ª       ª   ª   README.md
ª       ª   ª   risk-alerts.json
ª       ª   ª   
ª       ª   +---incidents
ª       ª           incident-20250701.json
ª       ª           incident-20250715.json
ª       ª           incident-20250730.json
ª       ª           README.md
ª       ª           
ª       +---docs
ª       ª       failover-and-ha.md
ª       ª       forensics.md
ª       ª       incident-response-guide.md
ª       ª       notification-channels.md
ª       ª       README.md
ª       ª       testing-checklists.md
ª       ª       thresholds-and-tuning.md
ª       ª       watchdog-architecture.md
ª       ª       
ª       +---hooks
ª       ª       README.md
ª       ª       use-auto-recover.js
ª       ª       use-event-trigger.js
ª       ª       use-health-check.js
ª       ª       use-latency-monitor.js
ª       ª       use-risk-hook.js
ª       ª       
ª       +---tests
ª       ª   ª   auto-restart.test.js
ª       ª   ª   block-watchdog.test.js
ª       ª   ª   circuit-breaker.test.js
ª       ª   ª   event-listener.test.js
ª       ª   ª   failover-manager.test.js
ª       ª   ª   gas-spike-watchdog.test.js
ª       ª   ª   incident-response-core.test.js
ª       ª   ª   mev-alerts.test.js
ª       ª   ª   notification-manager.test.js
ª       ª   ª   README.md
ª       ª   ª   revert-reason-logger.test.js
ª       ª   ª   risk-trigger-handler.test.js
ª       ª   ª   trade-kill-switch.test.js
ª       ª   ª   watchdog-daemon.test.js
ª       ª   ª   
ª       ª   +---hooks
ª       ª   ª       README.md
ª       ª   ª       use-auto-recover.test.js
ª       ª   ª       use-event-trigger.test.js
ª       ª   ª       use-health-check.test.js
ª       ª   ª       use-latency-monitor.test.js
ª       ª   ª       use-risk-hook.test.js
ª       ª   ª       
ª       ª   +---utils
ª       ª           block-latency-calc.test.js
ª       ª           dashboard-sync.test.js
ª       ª           error-aggregator.test.js
ª       ª           health-score.test.js
ª       ª           incident-archive.test.js
ª       ª           notification-helper.test.js
ª       ª           persistent-state.test.js
ª       ª           README.md
ª       ª           
ª       +---utils
ª               block-latency-calc.js
ª               dashboard-sync.js
ª               error-aggregator.js
ª               health-score.js
ª               incident-archive.js
ª               notification-helper.js
ª               persistent-state.js
ª               README.md
ª               
+---benchmarks
ª   ª   benchmarks-config.json
ª   ª   benchmarks-notes.md
ª   ª   cpu-profile.log
ª   ª   mempool-bench.js
ª   ª   performance-matrix.md
ª   ª   profiling-report.md
ª   ª   quick-bench.js
ª   ª   README.md
ª   ª   results.csv
ª   ª   sample-batch.json
ª   ª   test-batch.js
ª   ª   
ª   +---ai
ª   ª       adversarial-ai-bench.py
ª   ª       ai-bench-compare.ipynb
ª   ª       ai-benchmark-methodology.md
ª   ª       ai-benchmark-results.csv
ª   ª       ai-benchmark-scenarios.md
ª   ª       ai-fork-bench.py
ª   ª       ai-inference-traces.log
ª   ª       ai-integration-bench.py
ª   ª       ai-memory-profile.json
ª   ª       ai-models-tested.md
ª   ª       ai-perf-metrics.json
ª   ª       ai-scalability-demo.ipynb
ª   ª       README.md
ª   ª       
ª   +---configs
ª   ª       ai-benchmark-config.json
ª   ª       cpu-benchmarks-config.json
ª   ª       gas-benchmark-config.json
ª   ª       latency-benchmarks-config.json
ª   ª       mempool-benchmark-config.json
ª   ª       plugins-bench-config.json
ª   ª       README.md
ª   ª       test-matrix-20250701.json
ª   ª       toolchain-config.json
ª   ª       
ª   +---cpu
ª   ª       ai-module-cpu-bench.py
ª   ª       core-engine-cpu-bench.js
ª   ª       cpu-baseline.json
ª   ª       cpu-benchmark-compare.ipynb
ª   ª       cpu-benchmark-results.csv
ª   ª       cpu-benchmarks.md
ª   ª       cpu-methodology.md
ª   ª       cpu-usage-traces.log
ª   ª       plugin-cpu-bench.js
ª   ª       README.md
ª   ª       
ª   +---datasets
ª   ª       ai-benchmark-set-20250715.csv
ª   ª       arbsim-batch-20250701.csv
ª   ª       benchmark-dataset-sample.csv
ª   ª       benchmark-output-sample.json
ª   ª       datasets-changelog.md
ª   ª       gas-batch-20250701.csv
ª   ª       gas-benchmark-set-20250701.csv
ª   ª       input-data-template.json
ª   ª       mempool-benchmark-set-20250701.csv
ª   ª       mempool-events-20250701.json
ª   ª       plugin-batch-20250701.csv
ª   ª       README.md
ª   ª       regression-batch-20250701.csv
ª   ª       test-batch-20250701.csv
ª   ª       test-data-20250701.csv
ª   ª       test-data-20250715.csv
ª   ª       test-data-20250730.csv
ª   ª       
ª   +---docs
ª   ª       README.md
ª   ª       
ª   +---gas
ª   ª       ai-gas-bench.py
ª   ª       contracts-gas-bench.js
ª   ª       gas-benchmark-compare.ipynb
ª   ª       gas-benchmark-methodology.md
ª   ª       gas-benchmark-results.csv
ª   ª       gas-benchmark-traces.log
ª   ª       gas-benchmark.md
ª   ª       gas-cost-analysis.json
ª   ª       plugin-gas-bench.js
ª   ª       README.md
ª   ª       routes-gas-bench.js
ª   ª       
ª   +---latency
ª   ª       ai-latency-bench.py
ª   ª       dashboard-latency-bench.js
ª   ª       latency-bench-compare.ipynb
ª   ª       latency-benchmark-methodology.md
ª   ª       latency-benchmarks.md
ª   ª       latency-profiles.log
ª   ª       latency-results.csv
ª   ª       network-latency-bench.js
ª   ª       plugin-latency-bench.js
ª   ª       README.md
ª   ª       
ª   +---mempool
ª   ª       block-reorg-events.log
ª   ª       mempool-benchmark-methodology.md
ª   ª       mempool-benchmark-results.csv
ª   ª       mempool-heatmap.png
ª   ª       mempool-profiling.md
ª   ª       mempool-tx-samples.json
ª   ª       mev-frontrun-sim.js
ª   ª       node-mempool-compare.ipynb
ª   ª       README.md
ª   ª       relayer-latency-bench.js
ª   ª       
ª   +---regression
ª   ª       README.md
ª   ª       
ª   +---results
ª   ª       20250701-ai-vs-core.csv
ª   ª       20250701-ai-vs-core.md
ª   ª       20250701-benchmark-data.csv
ª   ª       20250701-benchmark-report.md
ª   ª       20250701-gas-vs-mempool.csv
ª   ª       20250701-gas-vs-mempool.md
ª   ª       20250701-latency-vs-plugin.csv
ª   ª       20250701-latency-vs-plugin.md
ª   ª       20250715-benchmark-data.csv
ª   ª       20250715-benchmark-report.md
ª   ª       20250730-benchmark-data.csv
ª   ª       20250730-benchmark-report.md
ª   ª       README.md
ª   ª       results-changelog.md
ª   ª       
ª   +---tools
ª           bench-analyze.py
ª           bench-cleanup.py
ª           bench-config.json
ª           bench-docs-export.sh
ª           bench-mock-data-gen.py
ª           bench-runner.js
ª           bench-sample-script.sh
ª           bench-toolkit.md
ª           plot-benchmarks.ipynb
ª           README.md
ª           tool-release-notes.md
ª           
+---ci
ª   ª   .env.example
ª   ª   ci-config.json
ª   ª   ci-helpers.sh
ª   ª   ci-notes.md
ª   ª   ci-settings.json
ª   ª   ci-setup.ps1
ª   ª   common.sh
ª   ª   migration-history.md
ª   ª   README.md
ª   ª   tree_structure.txt
ª   ª   
ª   +---badges
ª   ª       ai-status.svg
ª   ª       ci-status.svg
ª   ª       coverage.svg
ª   ª       e2e.svg
ª   ª       lint.svg
ª   ª       README.md
ª   ª       
ª   +---buildkite
ª   ª   ª   pipeline.yml
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---agent-hooks
ª   ª   ª       environment
ª   ª   ª       post-command
ª   ª   ª       pre-command
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---scripts
ª   ª           ai-bench.sh
ª   ª           build-image.sh
ª   ª           deploy.sh
ª   ª           README.md
ª   ª           run-e2e.sh
ª   ª           
ª   +---circleci
ª   ª   ª   config.yml
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---scripts
ª   ª           deploy.sh
ª   ª           install-deps.sh
ª   ª           notify-discord.sh
ª   ª           README.md
ª   ª           run-tests.sh
ª   ª           
ª   +---config
ª   ª       ai.env.template
ª   ª       ci.env.template
ª   ª       docker-compose.ci.yml
ª   ª       prod.env.template
ª   ª       README.md
ª   ª       staging.env.template
ª   ª       test.env.template
ª   ª       
ª   +---github
ª   ª   ª   CODEOWNERS
ª   ª   ª   dependabot.yml
ª   ª   ª   issue-template.md
ª   ª   ª   pr-template.md
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---actions
ª   ª           cache-hardhat-node.yml
ª   ª           deploy-contract-action.yml
ª   ª           notify-discord-action.yml
ª   ª           README.md
ª   ª           run-ai-inference-action.yml
ª   ª           setup-docker-action.yml
ª   ª           
ª   +---gitlab
ª   ª   ª   .gitlab-ci.yml
ª   ª   ª   ai-train.gitlab-ci.yml
ª   ª   ª   contract-deploy.gitlab-ci.yml
ª   ª   ª   env.template
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---scripts
ª   ª           build.sh
ª   ª           deploy.sh
ª   ª           lint.sh
ª   ª           notify.sh
ª   ª           README.md
ª   ª           test.sh
ª   ª           
ª   +---jenkins
ª   ª   ª   credentials.xml
ª   ª   ª   Jenkinsfile
ª   ª   ª   Jenkinsfile.contracts
ª   ª   ª   Jenkinsfile.deploy
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---pipeline-libs
ª   ª   ª       ai-utils.groovy
ª   ª   ª       README.md
ª   ª   ª       shared-library.groovy
ª   ª   ª       
ª   ª   +---scripts
ª   ª           build-docker.sh
ª   ª           notify-slack.groovy
ª   ª           post-cleanup.groovy
ª   ª           README.md
ª   ª           run-tests.sh
ª   ª           
ª   +---legacy
ª   ª       ci-migration-notes.md
ª   ª       deprecated-gitlab-ci.yml
ª   ª       old-github-actions.yml
ª   ª       old-jenkinsfile
ª   ª       README.md
ª   ª       
ª   +---notifications
ª   ª       discord-webhook.json
ª   ª       email-config.json
ª   ª       opsgenie.json
ª   ª       pagerduty.json
ª   ª       README.md
ª   ª       slack-webhook.json
ª   ª       
ª   +---scripts
ª   ª       cleanup.sh
ª   ª       coverage.sh
ª   ª       deploy-all.sh
ª   ª       docker-cleanup.sh
ª   ª       install-deps.sh
ª   ª       lint-all.sh
ª   ª       merge-bot.sh
ª   ª       notify.sh
ª   ª       postbuild.sh
ª   ª       prebuild.sh
ª   ª       README.md
ª   ª       rollback.sh
ª   ª       setup-env.sh
ª   ª       test-all.sh
ª   ª       
ª   +---workflows
ª           ai-deploy.yml
ª           ai-tests.yml
ª           audit.yml
ª           cd.yml
ª           ci.yml
ª           codeql-analysis.yml
ª           contracts-deploy.yml
ª           contracts-test.yml
ª           coverage.yml
ª           dashboard-build.yml
ª           dashboard-preview.yml
ª           e2e.yml
ª           fork-smoke.yml
ª           lint.yml
ª           mainnet-fork.yml
ª           notify.yml
ª           oracle-adapters.yml
ª           patch-deploy.yml
ª           plugin-marketplace.yml
ª           README.md
ª           regression.yml
ª           release-tag.yml
ª           test.yml
ª           
+---config
ª   ª   .env.example
ª   ª   agent-compatibility.json
ª   ª   audit-policy.json
ª   ª   config-docs.md
ª   ª   config-manifest.json
ª   ª   config-schema.json
ª   ª   config-schema.yaml
ª   ª   cross-ref.json
ª   ª   defaults.env
ª   ª   defaults.json
ª   ª   example.env
ª   ª   explainability-rules.yaml
ª   ª   gdpr-map.json
ª   ª   hotload-params.json
ª   ª   kyc-policy.json
ª   ª   README-bot-ops.md
ª   ª   README.md
ª   ª   roles.json
ª   ª   vault-ref.json
ª   ª   xai-params.json
ª   ª   
ª   +---.meta
ª   ª       README.md
ª   ª       
ª   +---ai
ª   ª       .meta
ª   ª       ai-ablation-matrix.json
ª   ª       ai-config.json
ª   ª       ai-feature-engineering.json
ª   ª       ai-pipeline-config.json
ª   ª       ai-scorer-config.json
ª   ª       ai-test-scenarios.json
ª   ª       ai-thresholds.json
ª   ª       ai-weights.json
ª   ª       README.md
ª   ª       retrain-policy.json
ª   ª       
ª   +---analytics
ª   ª       analytics-config.json
ª   ª       custom-metrics.json
ª   ª       dashboard-example.json
ª   ª       data-sources.json
ª   ª       event-hooks.json
ª   ª       README.md
ª   ª       trade-log-template.json
ª   ª       
ª   +---api-snapshots
ª   ª       README.md
ª   ª       
ª   +---chains
ª   ª       arbitrum.json
ª   ª       avalanche.json
ª   ª       bsc.json
ª   ª       chain-aliases.json
ª   ª       chains.json
ª   ª       chains.schema.json
ª   ª       ethereum.json
ª   ª       explorer-templates.json
ª   ª       optimism.json
ª   ª       polygon.json
ª   ª       README.md
ª   ª       rpc-endpoints.json
ª   ª       testnets.json
ª   ª       
ª   +---compliance
ª   ª       audit-rules.json
ª   ª       blacklisted-addresses.json
ª   ª       compliance-policies.json
ª   ª       jurisdiction-rules.json
ª   ª       monitoring.json
ª   ª       README.md
ª   ª       sanctions-list.json
ª   ª       whitelist.json
ª   ª       
ª   +---custom
ª   ª       README.md
ª   ª       
ª   +---dao
ª   ª       README.md
ª   ª       
ª   +---dashboards
ª   ª       README.md
ª   ª       
ª   +---deprecated
ª   ª       README.md
ª   ª       
ª   +---dexes
ª   ª       README.md
ª   ª       
ª   +---digital-twin
ª   ª       README.md
ª   ª       
ª   +---examples
ª   ª       README.md
ª   ª       
ª   +---insurance
ª   ª       README.md
ª   ª       
ª   +---legacy
ª   ª       README.md
ª   ª       
ª   +---locales
ª   ª       README.md
ª   ª       
ª   +---migrations
ª   ª       README.md
ª   ª       
ª   +---notifications
ª   ª       README.md
ª   ª       
ª   +---overrides
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---dev
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---prod
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---staging
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---test
ª   ª           README.md
ª   ª           
ª   +---presets
ª   ª       README.md
ª   ª       
ª   +---quickstart
ª   ª       README.md
ª   ª       
ª   +---risk
ª   ª       README.md
ª   ª       
ª   +---runtime-patches
ª   ª       README.md
ª   ª       
ª   +---sample-templates
ª   ª       README.md
ª   ª       
ª   +---schema
ª   ª       README.md
ª   ª       
ª   +---secrets
ª   ª       README.md
ª   ª       
ª   +---strategies
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---examples
ª   ª           README.md
ª   ª           
ª   +---tokens
ª   ª       README.md
ª   ª       
ª   +---versioning
ª           README.md
ª           
+---dashboard
ª   ª   README.md
ª   ª   
ª   +---admin
ª   ª       README.md
ª   ª       
ª   +---ai
ª   ª   ª   ai-manifest.json
ª   ª   ª   CHANGELOG.md
ª   ª   ª   index.js
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---automation
ª   ª   ª       AIAutoPilotPanel.jsx
ª   ª   ª       AIBatchRunner.js
ª   ª   ª       automation-demo.json
ª   ª   ª       AutomationLogs.json
ª   ª   ª       AutoStrategySelector.js
ª   ª   ª       OperatorOverrideToggle.jsx
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---chat
ª   ª   ª       AIChatUtils.js
ª   ª   ª       ChatFeedbackPanel.jsx
ª   ª   ª       ChatHistoryStore.js
ª   ª   ª       ChatOperatorLog.json
ª   ª   ª       LLMChatEngine.js
ª   ª   ª       PromptTemplates.json
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---components
ª   ª   ª       AIInsightWidget.jsx
ª   ª   ª       AITradeScorer.jsx
ª   ª   ª       AutomationToggle.jsx
ª   ª   ª       DecisionPathCard.jsx
ª   ª   ª       FeatureAttributionCard.jsx
ª   ª   ª       FeedbackPanel.jsx
ª   ª   ª       LLMChatBox.jsx
ª   ª   ª       ModelAuditLogPanel.jsx
ª   ª   ª       ModelStatusChip.jsx
ª   ª   ª       ModelSwitcher.jsx
ª   ª   ª       OperatorAIFeedbackPanel.jsx
ª   ª   ª       README.md
ª   ª   ª       ScoreKPIBlock.jsx
ª   ª   ª       XAIHeatmapOverlay.jsx
ª   ª   ª       
ª   ª   +---config
ª   ª   ª       ai-dashboard-config.json
ª   ª   ª       ai-presets.json
ª   ª   ª       chat-settings.json
ª   ª   ª       feedback-config.json
ª   ª   ª       model-switcher-presets.json
ª   ª   ª       README.md
ª   ª   ª       xai-overlays.json
ª   ª   ª       
ª   ª   +---demo
ª   ª   ª       ai-dashboard-tour.md
ª   ª   ª       ai-insight-demo.json
ª   ª   ª       chat-demo.json
ª   ª   ª       feedback-demo.json
ª   ª   ª       README.md
ª   ª   ª       xai-demo.json
ª   ª   ª       
ª   ª   +---explainability
ª   ª   ª       ExplainabilityHistory.json
ª   ª   ª       ExplainabilityUtils.js
ª   ª   ª       FeatureImportanceChart.jsx
ª   ª   ª       GlobalXAIStatsWidget.jsx
ª   ª   ª       README.md
ª   ª   ª       SaliencyMapPanel.jsx
ª   ª   ª       xai-demo-data.json
ª   ª   ª       XAIIncidentExplorer.jsx
ª   ª   ª       XAIOverviewModal.jsx
ª   ª   ª       
ª   ª   +---feedback
ª   ª   ª       feedback-demo.json
ª   ª   ª       FeedbackAPI.js
ª   ª   ª       FeedbackHistoryTable.jsx
ª   ª   ª       FeedbackPanel.jsx
ª   ª   ª       FeedbackSchema.json
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---hooks
ª   ª   ª       README.md
ª   ª   ª       useAIAutoPilot.js
ª   ª   ª       useAIFeedback.js
ª   ª   ª       useAIModel.js
ª   ª   ª       useAIOperatorMode.js
ª   ª   ª       useAIScoring.js
ª   ª   ª       useLLMChat.js
ª   ª   ª       useXAI.js
ª   ª   ª       
ª   ª   +---models
ª   ª   ª   ª   ai-models-list.json
ª   ª   ª   ª   default-model-config.json
ª   ª   ª   ª   model-audit-log.json
ª   ª   ª   ª   model-metadata.json
ª   ª   ª   ª   README.md
ª   ª   ª   ª   
ª   ª   ª   +---weights
ª   ª   ª       ª   ai-arb-v5.onnx
ª   ª   ª       ª   pattern-learner-v3.pt
ª   ª   ª       ª   README.md
ª   ª   ª       ª   xai-embedder-v1.bin
ª   ª   ª       ª   
ª   ª   ª       +---old-weights
ª   ª   ª               ai-arb-v3.pt
ª   ª   ª               ai-arb-v4.onnx
ª   ª   ª               README.md
ª   ª   ª               
ª   ª   +---presets
ª   ª   ª       ai-theme-presets.json
ª   ª   ª       explainability-presets.json
ª   ª   ª       model-switcher-presets.json
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---scoring
ª   ª   ª       AIPredictionTable.jsx
ª   ª   ª       AIScoreEngine.js
ª   ª   ª       README.md
ª   ª   ª       score-demo.json
ª   ª   ª       ScoreEventLog.json
ª   ª   ª       ScoreHeatmapPanel.jsx
ª   ª   ª       ScorePresetConfig.json
ª   ª   ª       ScoringUtils.js
ª   ª   ª       
ª   ª   +---tests
ª   ª   ª       aiModelSelect.test.js
ª   ª   ª       automationMode.test.js
ª   ª   ª       FeedbackPanel.test.js
ª   ª   ª       LLMChatPanel.test.js
ª   ª   ª       OperatorAIFeedbackPanel.test.js
ª   ª   ª       README.md
ª   ª   ª       XAIWidget.test.js
ª   ª   ª       
ª   ª   +---utils
ª   ª           aiApiClient.js
ª   ª           aiDataAdapters.js
ª   ª           aiFileUtils.js
ª   ª           aiFormatters.js
ª   ª           aiMetrics.js
ª   ª           aiValidator.js
ª   ª           README.md
ª   ª           
ª   +---analytics
ª   ª   ª   CHANGELOG.md
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---ai
ª   ª   ª       ai-demo-results.json
ª   ª   ª       AIDashboardAdapter.js
ª   ª   ª       AIProfitPredictor.js
ª   ª   ª       AnalyticsAIMetrics.jsx
ª   ª   ª       LatencyAnomalyAI.js
ª   ª   ª       OutlierDetectorAI.js
ª   ª   ª       README.md
ª   ª   ª       RegressionTrainer.js
ª   ª   ª       
ª   ª   +---charts
ª   ª   ª       AnalyticsChartUtils.js
ª   ª   ª       AnomalyScatterPlot.jsx
ª   ª   ª       AreaChart.jsx
ª   ª   ª       CandlestickChart.jsx
ª   ª   ª       LineChart.jsx
ª   ª   ª       OrderbookDepthChart.jsx
ª   ª   ª       PieChart.jsx
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---components
ª   ª   ª       AnalyticsAlertBanner.jsx
ª   ª   ª       AnalyticsDashboard.jsx
ª   ª   ª       GasCostChart.jsx
ª   ª   ª       LatencyStatsPanel.jsx
ª   ª   ª       OperatorStatsPanel.jsx
ª   ª   ª       OutlierDetectionWidget.jsx
ª   ª   ª       PerformanceBreakdown.jsx
ª   ª   ª       PnLChart.jsx
ª   ª   ª       README.md
ª   ª   ª       RiskProfileChart.jsx
ª   ª   ª       ROIHeatmap.jsx
ª   ª   ª       TradeMetricsTable.jsx
ª   ª   ª       VolumeTimeSeries.jsx
ª   ª   ª       
ª   ª   +---config
ª   ª   ª       ai-analytics-presets.json
ª   ª   ª       analytics-layout.json
ª   ª   ª       anomaly-detection-config.json
ª   ª   ª       custom-widgets-presets.json
ª   ª   ª       dashboard-metrics.json
ª   ª   ª       kpi-config.json
ª   ª   ª       operator-view-presets.json
ª   ª   ª       README.md
ª   ª   ª       regression-settings.json
ª   ª   ª       risk-indicators.json
ª   ª   ª       theme-presets.json
ª   ª   ª       timeseries-source.json
ª   ª   ª       
ª   ª   +---data
ª   ª   ª       demo-anomalies.json
ª   ª   ª       demo-gas-costs.csv
ª   ª   ª       demo-pnl-data.csv
ª   ª   ª       demo-trade-metrics.csv
ª   ª   ª       outlier-events.csv
ª   ª   ª       README.md
ª   ª   ª       time-series-sample.csv
ª   ª   ª       
ª   ª   +---explainability
ª   ª   ª       AnalyticsXAIOverlay.jsx
ª   ª   ª       AnomalyExplanationPanel.jsx
ª   ª   ª       explainability-config.json
ª   ª   ª       README.md
ª   ª   ª       RegressionExplainPanel.jsx
ª   ª   ª       
ª   ª   +---hooks
ª   ª   ª       README.md
ª   ª   ª       useAnalyticsData.js
ª   ª   ª       useAnomalyScan.js
ª   ª   ª       useArbStats.js
ª   ª   ª       useGasTrends.js
ª   ª   ª       useLatencyStats.js
ª   ª   ª       useLivePnL.js
ª   ª   ª       useVolumeTimeseries.js
ª   ª   ª       
ª   ª   +---integration
ª   ª   ª       AnalyticsAPI.js
ª   ª   ª       analyticsDataClient.js
ª   ª   ª       AnalyticsWS.js
ª   ª   ª       README.md
ª   ª   ª       syncConfig.json
ª   ª   ª       useAnalyticsSocket.js
ª   ª   ª       
ª   ª   +---pages
ª   ª   ª       dashboard.js
ª   ª   ª       gas-cost.js
ª   ª   ª       pnl.js
ª   ª   ª       README.md
ª   ª   ª       regression.js
ª   ª   ª       risk.js
ª   ª   ª       roi.js
ª   ª   ª       time-series.js
ª   ª   ª       trade-metrics.js
ª   ª   ª       
ª   ª   +---panels
ª   ª   ª       MainAnalyticsPanel.jsx
ª   ª   ª       OperatorPerformancePanel.jsx
ª   ª   ª       ProfitRegressionPanel.jsx
ª   ª   ª       README.md
ª   ª   ª       RiskAndROIOverview.jsx
ª   ª   ª       TimeSeriesExplorerPanel.jsx
ª   ª   ª       VolumeVsGasPanel.jsx
ª   ª   ª       
ª   ª   +---reports
ª   ª   ª       custom-user-report-sample.pdf
ª   ª   ª       daily-report-20250730.pdf
ª   ª   ª       gas-analysis-report-20250701.csv
ª   ª   ª       profit-loss-report-20250710.csv
ª   ª   ª       README.md
ª   ª   ª       regression-report-20250715.csv
ª   ª   ª       
ª   ª   +---state
ª   ª   ª       analyticsPersistence.js
ª   ª   ª       analyticsSelectors.js
ª   ª   ª       analyticsStore.js
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---tests
ª   ª   ª       AnalyticsAIMetrics.test.js
ª   ª   ª       AnalyticsAPI.test.js
ª   ª   ª       AnalyticsDashboard.test.js
ª   ª   ª       GasCostChart.test.js
ª   ª   ª       LatencyStatsPanel.test.js
ª   ª   ª       OutlierDetectionWidget.test.js
ª   ª   ª       README.md
ª   ª   ª       ROIHeatmap.test.js
ª   ª   ª       TradeMetricsTable.test.js
ª   ª   ª       
ª   ª   +---utils
ª   ª   ª       anomalyUtils.js
ª   ª   ª       calcROI.js
ª   ª   ª       formatTradeData.js
ª   ª   ª       kpiFormatters.js
ª   ª   ª       pnlUtils.js
ª   ª   ª       README.md
ª   ª   ª       regressionUtils.js
ª   ª   ª       timeSeriesUtils.js
ª   ª   ª       
ª   ª   +---widgets
ª   ª           ActiveRouteWidget.jsx
ª   ª           ArbitrageScoreWidget.jsx
ª   ª           GasTrendWidget.jsx
ª   ª           LatencyIndicatorWidget.jsx
ª   ª           LiveVolumeSparkline.jsx
ª   ª           MiniPnLWidget.jsx
ª   ª           README.md
ª   ª           TradeCountWidget.jsx
ª   ª           
ª   +---api
ª   ª   ª   ai.js
ª   ª   ª   arb.js
ª   ª   ª   CHANGELOG.md
ª   ª   ª   dev.js
ª   ª   ª   extension.js
ª   ª   ª   health.js
ª   ª   ª   index.js
ª   ª   ª   metrics.js
ª   ª   ª   notifications.js
ª   ª   ª   plugin.js
ª   ª   ª   README.md
ª   ª   ª   user.js
ª   ª   ª   webhook.js
ª   ª   ª   
ª   ª   +---docs
ª   ª   ª       api-error-codes.md
ª   ª   ª       api-versioning.md
ª   ª   ª       auth.md
ª   ª   ª       integration.md
ª   ª   ª       multi-tenancy.md
ª   ª   ª       README.md
ª   ª   ª       routes.md
ª   ª   ª       schemas.md
ª   ª   ª       sockets.md
ª   ª   ª       update-history.md
ª   ª   ª       webhooks.md
ª   ª   ª       
ª   ª   +---integration
ª   ª   ª       aiAdapter.js
ª   ª   ª       analyticsAdapter.js
ª   ª   ª       backendAdapter.js
ª   ª   ª       configAdapter.js
ª   ª   ª       metricsAdapter.js
ª   ª   ª       multiTenantAdapter.js
ª   ª   ª       notificationAdapter.js
ª   ª   ª       operatorAdapter.js
ª   ª   ª       pluginAdapter.js
ª   ª   ª       README.md
ª   ª   ª       riskAdapter.js
ª   ª   ª       sandboxAdapter.js
ª   ª   ª       uploadAdapter.js
ª   ª   ª       wsAdapter.js
ª   ª   ª       
ª   ª   +---middleware
ª   ª   ª       analyticsThrottle.js
ª   ª   ª       auth.js
ª   ª   ª       cors.js
ª   ª   ª       csrf.js
ª   ª   ª       errorHandler.js
ª   ª   ª       logger.js
ª   ª   ª       multiTenantGuard.js
ª   ª   ª       operatorGuard.js
ª   ª   ª       rateLimit.js
ª   ª   ª       README.md
ª   ª   ª       validate.js
ª   ª   ª       
ª   ª   +---routes
ª   ª   ª   ª   ai.js
ª   ª   ª   ª   alerts.js
ª   ª   ª   ª   analytics.js
ª   ª   ª   ª   config.js
ª   ª   ª   ª   gas.js
ª   ª   ª   ª   graphql.js
ª   ª   ª   ª   health.js
ª   ª   ª   ª   index.js
ª   ª   ª   ª   metrics.js
ª   ª   ª   ª   multi-tenant.js
ª   ª   ª   ª   notifications.js
ª   ª   ª   ª   operator.js
ª   ª   ª   ª   overlays.js
ª   ª   ª   ª   plugins.js
ª   ª   ª   ª   pnl.js
ª   ª   ª   ª   presets.js
ª   ª   ª   ª   README.md
ª   ª   ª   ª   risk.js
ª   ª   ª   ª   sandbox.js
ª   ª   ª   ª   session.js
ª   ª   ª   ª   status.js
ª   ª   ª   ª   trades.js
ª   ª   ª   ª   uploads.js
ª   ª   ª   ª   user.js
ª   ª   ª   ª   websocket.js
ª   ª   ª   ª   xai.js
ª   ª   ª   ª   
ª   ª   ª   +---__mocks__
ª   ª   ª           ai-inference.json
ª   ª   ª           analytics.json
ª   ª   ª           config.json
ª   ª   ª           health.json
ª   ª   ª           notifications.json
ª   ª   ª           operator.json
ª   ª   ª           overlays.json
ª   ª   ª           presets.json
ª   ª   ª           README.md
ª   ª   ª           session.json
ª   ª   ª           trades.json
ª   ª   ª           user.json
ª   ª   ª           
ª   ª   +---schemas
ª   ª   ª       ai-inference.schema.json
ª   ª   ª       analytics.schema.json
ª   ª   ª       config.schema.json
ª   ª   ª       notification.schema.json
ª   ª   ª       openapi.yaml
ª   ª   ª       operator.schema.json
ª   ª   ª       overlays.schema.json
ª   ª   ª       plugin.schema.json
ª   ª   ª       presets.schema.json
ª   ª   ª       README.md
ª   ª   ª       session.schema.json
ª   ª   ª       trade.schema.json
ª   ª   ª       upload.schema.json
ª   ª   ª       user.schema.json
ª   ª   ª       websocket.schema.json
ª   ª   ª       
ª   ª   +---sockets
ª   ª   ª       ai-socket.js
ª   ª   ª       alerts-socket.js
ª   ª   ª       analytics-socket.js
ª   ª   ª       config-socket.js
ª   ª   ª       notification-socket.js
ª   ª   ª       operator-socket.js
ª   ª   ª       overlays-socket.js
ª   ª   ª       plugin-socket.js
ª   ª   ª       README.md
ª   ª   ª       trade-socket.js
ª   ª   ª       user-socket.js
ª   ª   ª       
ª   ª   +---tests
ª   ª   ª   ª   api-ai.test.js
ª   ª   ª   ª   api-analytics.test.js
ª   ª   ª   ª   api-config.test.js
ª   ª   ª   ª   api-error.test.js
ª   ª   ª   ª   api-health.test.js
ª   ª   ª   ª   api-metrics.test.js
ª   ª   ª   ª   api-multi-tenant.test.js
ª   ª   ª   ª   api-notifications.test.js
ª   ª   ª   ª   api-operator.test.js
ª   ª   ª   ª   api-presets.test.js
ª   ª   ª   ª   api-routes.test.js
ª   ª   ª   ª   api-sandbox.test.js
ª   ª   ª   ª   api-session.test.js
ª   ª   ª   ª   api-status.test.js
ª   ª   ª   ª   api-trades.test.js
ª   ª   ª   ª   api-uploads.test.js
ª   ª   ª   ª   api-websocket.test.js
ª   ª   ª   ª   api-xai.test.js
ª   ª   ª   ª   README.md
ª   ª   ª   ª   
ª   ª   ª   +---__mocks__
ª   ª   ª           aiMock.js
ª   ª   ª           analyticsMock.js
ª   ª   ª           README.md
ª   ª   ª           userSessionMock.js
ª   ª   ª           
ª   ª   +---utils
ª   ª           apiErrorCodes.js
ª   ª           apiMockUtils.js
ª   ª           apiResponse.js
ª   ª           parseQuery.js
ª   ª           queryValidator.js
ª   ª           rateLimiter.js
ª   ª           README.md
ª   ª           testUtils.js
ª   ª           uploadUtils.js
ª   ª           validateSchema.js
ª   ª           websocketUtils.js
ª   ª           
ª   +---ar
ª   ª       README.md
ª   ª       
ª   +---backend
ª   ª       README.md
ª   ª       
ª   +---charts
ª   ª       README.md
ª   ª       
ª   +---components
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---ai
ª   ª   ª       AIChatBubble.jsx
ª   ª   ª       AIDecisionFlow.jsx
ª   ª   ª       AIInsightPrompt.jsx
ª   ª   ª       LLMChatBox.jsx
ª   ª   ª       ModelConfidenceMeter.jsx
ª   ª   ª       ModelSwitcherCard.jsx
ª   ª   ª       README.md
ª   ª   ª       SaliencyOverlay.jsx
ª   ª   ª       XAIHeatmapPanel.jsx
ª   ª   ª       
ª   ª   +---atomic
ª   ª   ª       Avatar.jsx
ª   ª   ª       Badge.jsx
ª   ª   ª       Button.jsx
ª   ª   ª       Chip.jsx
ª   ª   ª       ColorSwatch.jsx
ª   ª   ª       Divider.jsx
ª   ª   ª       Icon.jsx
ª   ª   ª       Label.jsx
ª   ª   ª       ProgressBar.jsx
ª   ª   ª       README.md
ª   ª   ª       Skeleton.jsx
ª   ª   ª       Spinner.jsx
ª   ª   ª       StatusIndicator.jsx
ª   ª   ª       ToggleSwitch.jsx
ª   ª   ª       Tooltip.jsx
ª   ª   ª       
ª   ª   +---charts
ª   ª   ª       AreaChart.jsx
ª   ª   ª       BarChart.jsx
ª   ª   ª       CandlestickChart.jsx
ª   ª   ª       ChartWrapper.jsx
ª   ª   ª       DepthChart.jsx
ª   ª   ª       HeatmapChart.jsx
ª   ª   ª       LatencyTrendChart.jsx
ª   ª   ª       LineChart.jsx
ª   ª   ª       PieChart.jsx
ª   ª   ª       README.md
ª   ª   ª       TradePathChart.jsx
ª   ª   ª       VolumeChart.jsx
ª   ª   ª       
ª   ª   +---dialogs
ª   ª   ª       AIExplainDialog.jsx
ª   ª   ª       ConfirmDialog.jsx
ª   ª   ª       ErrorModal.jsx
ª   ª   ª       OnboardingModal.jsx
ª   ª   ª       OperatorCommandDialog.jsx
ª   ª   ª       PluginDialog.jsx
ª   ª   ª       README.md
ª   ª   ª       ReportExportDialog.jsx
ª   ª   ª       SettingsDialog.jsx
ª   ª   ª       
ª   ª   +---forms
ª   ª   ª       CodeEditorInput.jsx
ª   ª   ª       DatePicker.jsx
ª   ª   ª       FileUploadInput.jsx
ª   ª   ª       InputGroup.jsx
ª   ª   ª       JSONEditor.jsx
ª   ª   ª       MultiSelect.jsx
ª   ª   ª       PasswordInput.jsx
ª   ª   ª       RangeSlider.jsx
ª   ª   ª       README.md
ª   ª   ª       SearchInput.jsx
ª   ª   ª       SelectInput.jsx
ª   ª   ª       TextInput.jsx
ª   ª   ª       ToggleGroup.jsx
ª   ª   ª       
ª   ª   +---layout
ª   ª   ª       AppLayout.jsx
ª   ª   ª       Breadcrumbs.jsx
ª   ª   ª       DashboardGrid.jsx
ª   ª   ª       Footer.jsx
ª   ª   ª       PageWrapper.jsx
ª   ª   ª       PanelCard.jsx
ª   ª   ª       README.md
ª   ª   ª       SectionHeader.jsx
ª   ª   ª       Sidebar.jsx
ª   ª   ª       SplitPaneLayout.jsx
ª   ª   ª       Topbar.jsx
ª   ª   ª       
ª   ª   +---loaders
ª   ª   ª       FullscreenLoader.jsx
ª   ª   ª       InlineSpinner.jsx
ª   ª   ª       README.md
ª   ª   ª       WidgetLoader.jsx
ª   ª   ª       
ª   ª   +---notifications
ª   ª   ª       InlineAlert.jsx
ª   ª   ª       NotificationBanner.jsx
ª   ª   ª       README.md
ª   ª   ª       Snackbar.jsx
ª   ª   ª       ToastContainer.jsx
ª   ª   ª       WebhookAlert.jsx
ª   ª   ª       
ª   ª   +---operator
ª   ª   ª       AuditTimeline.jsx
ª   ª   ª       HealthStatusCard.jsx
ª   ª   ª       IncidentFeed.jsx
ª   ª   ª       IncidentSummaryPanel.jsx
ª   ª   ª       KillSwitchButton.jsx
ª   ª   ª       OperatorCommandBar.jsx
ª   ª   ª       README.md
ª   ª   ª       ShiftRosterPanel.jsx
ª   ª   ª       
ª   ª   +---overlays
ª   ª   ª       AlertBanner.jsx
ª   ª   ª       AROverlay.jsx
ª   ª   ª       DebugOverlay.jsx
ª   ª   ª       IncidentOverlay.jsx
ª   ª   ª       README.md
ª   ª   ª       RiskOverlay.jsx
ª   ª   ª       TradePathOverlay.jsx
ª   ª   ª       XAIOverlay.jsx
ª   ª   ª       
ª   ª   +---plugin
ª   ª   ª       PluginCard.jsx
ª   ª   ª       PluginConfigForm.jsx
ª   ª   ª       PluginMarketplace.jsx
ª   ª   ª       PluginPanel.jsx
ª   ª   ª       PluginStatusIndicator.jsx
ª   ª   ª       PluginToggle.jsx
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---sandbox
ª   ª   ª       ExperimentalChartPanel.jsx
ª   ª   ª       FeatureFlagToggle.jsx
ª   ª   ª       LLMToolbox.jsx
ª   ª   ª       PlaygroundPanel.jsx
ª   ª   ª       README.md
ª   ª   ª       WidgetDevTools.jsx
ª   ª   ª       
ª   ª   +---tables
ª   ª   ª       AITable.jsx
ª   ª   ª       AlertHistoryTable.jsx
ª   ª   ª       DataTable.jsx
ª   ª   ª       EditableTableCell.jsx
ª   ª   ª       PoolTable.jsx
ª   ª   ª       README.md
ª   ª   ª       RiskMatrixTable.jsx
ª   ª   ª       SortableTable.jsx
ª   ª   ª       TablePagination.jsx
ª   ª   ª       TradeTable.jsx
ª   ª   ª       
ª   ª   +---theme
ª   ª   ª       ContrastModeSwitch.jsx
ª   ª   ª       README.md
ª   ª   ª       ThemePaletteGrid.jsx
ª   ª   ª       ThemePreviewBox.jsx
ª   ª   ª       ThemeSelector.jsx
ª   ª   ª       ThemeToggle.jsx
ª   ª   ª       
ª   ª   +---utils
ª   ª   ª       BlockTimer.jsx
ª   ª   ª       CodeBlock.jsx
ª   ª   ª       CopyToClipboard.jsx
ª   ª   ª       GasBadge.jsx
ª   ª   ª       JsonViewer.jsx
ª   ª   ª       OperatorAvatar.jsx
ª   ª   ª       README.md
ª   ª   ª       StatusPill.jsx
ª   ª   ª       TimeAgo.jsx
ª   ª   ª       ValueChangeDelta.jsx
ª   ª   ª       
ª   ª   +---widgets
ª   ª           AIDecisionScoreCard.jsx
ª   ª           GasWidget.jsx
ª   ª           LatencyMeter.jsx
ª   ª           MEVActivityWidget.jsx
ª   ª           OperatorInsightsWidget.jsx
ª   ª           PnLWidget.jsx
ª   ª           PoolHealthWidget.jsx
ª   ª           README.md
ª   ª           RiskGaugeWidget.jsx
ª   ª           RoutePriorityMeter.jsx
ª   ª           TokenReputationScore.jsx
ª   ª           TradeDeltaWidget.jsx
ª   ª           TradeVolumeSparkline.jsx
ª   ª           WatchdogStatus.jsx
ª   ª           
ª   +---context
ª   ª       AIContext.js
ª   ª       AIProvider.jsx
ª   ª       AlertsContext.js
ª   ª       AlertsProvider.jsx
ª   ª       AppContext.js
ª   ª       AppProvider.jsx
ª   ª       AuthContext.js
ª   ª       AuthProvider.jsx
ª   ª       context.test.js
ª   ª       contextHelpers.js
ª   ª       index.js
ª   ª       LayoutContext.js
ª   ª       LayoutProvider.jsx
ª   ª       LocaleContext.js
ª   ª       LocaleProvider.jsx
ª   ª       ModalContext.js
ª   ª       ModalProvider.jsx
ª   ª       NotificationsContext.js
ª   ª       NotificationsProvider.jsx
ª   ª       OperatorContext.js
ª   ª       OperatorProvider.jsx
ª   ª       OperatorShiftContext.js
ª   ª       OperatorShiftProvider.jsx
ª   ª       OverlayContext.js
ª   ª       OverlayProvider.jsx
ª   ª       PluginContext.js
ª   ª       PluginProvider.jsx
ª   ª       README.md
ª   ª       SettingsContext.js
ª   ª       SettingsProvider.jsx
ª   ª       StateSyncContext.js
ª   ª       StateSyncProvider.jsx
ª   ª       ThemeContext.js
ª   ª       ThemeProvider.jsx
ª   ª       useAI.js
ª   ª       useAlerts.js
ª   ª       useApp.js
ª   ª       useAuth.js
ª   ª       useLayout.js
ª   ª       useLocale.js
ª   ª       useModal.js
ª   ª       useNotifications.js
ª   ª       useOperator.js
ª   ª       useOperatorShift.js
ª   ª       useOverlay.js
ª   ª       usePlugin.js
ª   ª       useSettings.js
ª   ª       useStateSync.js
ª   ª       useTheme.js
ª   ª       useWebsocket.js
ª   ª       useXAI.js
ª   ª       WebsocketContext.js
ª   ª       WebsocketProvider.jsx
ª   ª       XAIContext.js
ª   ª       XAIProvider.jsx
ª   ª       
ª   +---data
ª   ª   ª   active-pools.json
ª   ª   ª   agent-scores.json
ª   ª   ª   ai-evaluations.json
ª   ª   ª   compliance-log.json
ª   ª   ª   fork-state-diff.json
ª   ª   ª   incident-log.json
ª   ª   ª   market-depth.json
ª   ª   ª   operator-profiles.json
ª   ª   ª   oracle-feed-cache.json
ª   ª   ª   plugin-usage.json
ª   ª   ª   profit-log.json
ª   ª   ª   README.md
ª   ª   ª   risk-events.json
ª   ª   ª   route-cache.json
ª   ª   ª   simulation-runs.json
ª   ª   ª   state-history.log
ª   ª   ª   token-metadata.json
ª   ª   ª   trade-history.json
ª   ª   ª   
ª   ª   +---ai-feedback
ª   ª   ª       feedback-20250701.json
ª   ª   ª       feedback-20250715.json
ª   ª   ª       feedback-20250730.json
ª   ª   ª       model-update-requests.json
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---analytics
ª   ª   ª       ai-inference-20250701.json
ª   ª   ª       ai-inference-20250715.json
ª   ª   ª       ai-inference-20250730.json
ª   ª   ª       anomaly-events-20250730.json
ª   ª   ª       pool-liquidity-report-20250701.json
ª   ª   ª       pool-liquidity-report-20250715.json
ª   ª   ª       pool-liquidity-report-20250730.json
ª   ª   ª       README.md
ª   ª   ª       trade-alpha-scores-20250701.json
ª   ª   ª       trade-alpha-scores-20250715.json
ª   ª   ª       trade-alpha-scores-20250730.json
ª   ª   ª       
ª   ª   +---audit-trails
ª   ª   ª       audit-20250701.log
ª   ª   ª       audit-20250715.log
ª   ª   ª       audit-20250730.log
ª   ª   ª       event-archive-20250701.json
ª   ª   ª       event-archive-20250715.json
ª   ª   ª       event-archive-20250730.json
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---compliance-archive
ª   ª   ª       kyc-report-20250701.pdf
ª   ª   ª       kyc-report-20250715.pdf
ª   ª   ª       kyc-report-20250730.pdf
ª   ª   ª       README.md
ª   ª   ª       sanctions-check-20250701.json
ª   ª   ª       sanctions-check-20250715.json
ª   ª   ª       sanctions-check-20250730.json
ª   ª   ª       
ª   ª   +---export
ª   ª   ª       ai-inference-export-20250701.json
ª   ª   ª       dashboard-report-20250730.pdf
ª   ª   ª       export-20250701.csv
ª   ª   ª       export-20250715.csv
ª   ª   ª       export-20250730.csv
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---forensics
ª   ª   ª       exploit-dump-20250701.json
ª   ª   ª       exploit-dump-20250715.json
ª   ª   ª       exploit-dump-20250730.json
ª   ª   ª       README.md
ª   ª   ª       root-cause-analysis.md
ª   ª   ª       trade-anomaly-20250730.json
ª   ª   ª       
ª   ª   +---logs
ª   ª   ª       ai-agent-20250701.log
ª   ª   ª       ai-agent-20250715.log
ª   ª   ª       ai-agent-20250730.log
ª   ª   ª       engine-20250701.log
ª   ª   ª       engine-20250715.log
ª   ª   ª       engine-20250730.log
ª   ª   ª       error-20250701.log
ª   ª   ª       error-20250715.log
ª   ª   ª       error-20250730.log
ª   ª   ª       README.md
ª   ª   ª       rotation-policy.md
ª   ª   ª       trades-20250701.log
ª   ª   ª       trades-20250715.log
ª   ª   ª       trades-20250730.log
ª   ª   ª       watchdog-20250701.log
ª   ª   ª       watchdog-20250715.log
ª   ª   ª       watchdog-20250730.log
ª   ª   ª       
ª   ª   +---operator-audit
ª   ª   ª       ai-review-20250715.json
ª   ª   ª       nlp-feedback-20250730.json
ª   ª   ª       operator-actions-20250701.json
ª   ª   ª       operator-actions-20250715.json
ª   ª   ª       operator-actions-20250730.json
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---simulation-snapshots
ª   ª   ª       post-fork-sim-20250715.json
ª   ª   ª       pre-fork-sim-20250715.json
ª   ª   ª       README.md
ª   ª   ª       risk-test-20250715.json
ª   ª   ª       snapshot-20250701.json
ª   ª   ª       snapshot-20250715.json
ª   ª   ª       snapshot-20250730.json
ª   ª   ª       
ª   ª   +---snapshots
ª   ª   ª       agents-20250701.json
ª   ª   ª       agents-20250715.json
ª   ª   ª       agents-20250730.json
ª   ª   ª       latest-snapshot.json
ª   ª   ª       pools-20250701.json
ª   ª   ª       pools-20250715.json
ª   ª   ª       pools-20250730.json
ª   ª   ª       README.md
ª   ª   ª       sim-20250701.json
ª   ª   ª       sim-20250715.json
ª   ª   ª       sim-20250730.json
ª   ª   ª       
ª   ª   +---synthetic-datasets
ª   ª           deep-arb-ai-trainset.csv
ª   ª           fake-arb-scenarios.json
ª   ª           README.md
ª   ª           sim-synthetic-events.json
ª   ª           synthetic-prices-20250701.csv
ª   ª           synthetic-prices-20250715.csv
ª   ª           synthetic-profits-20250730.csv
ª   ª           
ª   +---deploy
ª   ª   ª   CHANGELOG.md
ª   ª   ª   patterns.md
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---ansible
ª   ª   ª   ª   inventory.ini
ª   ª   ª   ª   playbook.yml
ª   ª   ª   ª   README.md
ª   ª   ª   ª   secrets.yml
ª   ª   ª   ª   
ª   ª   ª   +---group_vars
ª   ª   ª   ª       all.yml
ª   ª   ª   ª       prod.yml
ª   ª   ª   ª       README.md
ª   ª   ª   ª       
ª   ª   ª   +---roles
ª   ª   ª   ª   ª   README.md
ª   ª   ª   ª   ª   
ª   ª   ª   ª   +---ai-modules
ª   ª   ª   ª   ª   ª   README.md
ª   ª   ª   ª   ª   ª   
ª   ª   ª   ª   ª   +---backend
ª   ª   ª   ª   ª   ª       README.md
ª   ª   ª   ª   ª   ª       
ª   ª   ª   ª   ª   +---dashboard
ª   ª   ª   ª   ª   ª       README.md
ª   ª   ª   ª   ª   ª       
ª   ª   ª   ª   ª   +---operator
ª   ª   ª   ª   ª           README.md
ª   ª   ª   ª   ª           
ª   ª   ª   ª   +---backend
ª   ª   ª   ª   ª       README.md
ª   ª   ª   ª   ª       
ª   ª   ª   ª   +---dashboard
ª   ª   ª   ª   ª       README.md
ª   ª   ª   ª   ª       
ª   ª   ª   ª   +---operator
ª   ª   ª   ª           README.md
ª   ª   ª   ª           
ª   ª   ª   +---scripts
ª   ª   ª           README.md
ª   ª   ª           run-all.sh
ª   ª   ª           
ª   ª   +---audit
ª   ª   ª       audit-checklist.md
ª   ª   ª       cloud-posture.md
ª   ª   ª       deploy-logs.md
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---docker
ª   ª   ª       ai-modules.Dockerfile
ª   ª   ª       backend.Dockerfile
ª   ª   ª       base.Dockerfile
ª   ª   ª       dashboard.Dockerfile
ª   ª   ª       operator.Dockerfile
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---docker-compose
ª   ª   ª       docker-compose.dev.yml
ª   ª   ª       docker-compose.override.yml
ª   ª   ª       docker-compose.prod.yml
ª   ª   ª       docker-compose.yml
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---environments
ª   ª   ª       .env.example
ª   ª   ª       dev.env
ª   ª   ª       local.env
ª   ª   ª       mainnet-fork.env
ª   ª   ª       preview.env
ª   ª   ª       prod.env
ª   ª   ª       README.md
ª   ª   ª       staging.env
ª   ª   ª       testnet.env
ª   ª   ª       vault.env
ª   ª   ª       
ª   ª   +---helm
ª   ª   ª   ª   README.md
ª   ª   ª   ª   
ª   ª   ª   +---apex-protocol
ª   ª   ª       ª   Chart.yaml
ª   ª   ª       ª   NOTES.txt
ª   ª   ª       ª   README.md
ª   ª   ª       ª   values.yaml
ª   ª   ª       ª   
ª   ª   ª       +---templates
ª   ª   ª               configmap.yaml
ª   ª   ª               deployment.yaml
ª   ª   ª               hpa.yaml
ª   ª   ª               ingress.yaml
ª   ª   ª               README.md
ª   ª   ª               secrets.yaml
ª   ª   ª               service.yaml
ª   ª   ª               
ª   ª   +---kubernetes
ª   ª   ª   ª   README.md
ª   ª   ª   ª   
ª   ª   ª   +---base
ª   ª   ª   ª       ai-modules-deployment.yaml
ª   ª   ª   ª       backend-deployment.yaml
ª   ª   ª   ª       configmap.yaml
ª   ª   ª   ª       dashboard-deployment.yaml
ª   ª   ª   ª       ingress.yaml
ª   ª   ª   ª       kustomization.yaml
ª   ª   ª   ª       namespace.yaml
ª   ª   ª   ª       operator-deployment.yaml
ª   ª   ª   ª       README.md
ª   ª   ª   ª       secrets.yaml
ª   ª   ª   ª       service.yaml
ª   ª   ª   ª       storage.yaml
ª   ª   ª   ª       
ª   ª   ª   +---overlays
ª   ª   ª   ª   ª   README.md
ª   ª   ª   ª   ª   
ª   ª   ª   ª   +---dev
ª   ª   ª   ª   ª       kustomization.yaml
ª   ª   ª   ª   ª       README.md
ª   ª   ª   ª   ª       
ª   ª   ª   ª   +---local
ª   ª   ª   ª   ª       kustomization.yaml
ª   ª   ª   ª   ª       README.md
ª   ª   ª   ª   ª       
ª   ª   ª   ª   +---prod
ª   ª   ª   ª   ª       kustomization.yaml
ª   ª   ª   ª   ª       README.md
ª   ª   ª   ª   ª       
ª   ª   ª   ª   +---staging
ª   ª   ª   ª   ª       kustomization.yaml
ª   ª   ª   ª   ª       README.md
ª   ª   ª   ª   ª       
ª   ª   ª   ª   +---testnet
ª   ª   ª   ª           kustomization.yaml
ª   ª   ª   ª           README.md
ª   ª   ª   ª           
ª   ª   ª   +---scripts
ª   ª   ª           cleanup.sh
ª   ª   ª           deploy.sh
ª   ª   ª           README.md
ª   ª   ª           
ª   ª   +---migration
ª   ª   ª       001-init.sql
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---scripts
ª   ª   ª       backup-db.sh
ª   ª   ª       deploy-all.sh
ª   ª   ª       healthcheck.sh
ª   ª   ª       logs.sh
ª   ª   ª       README.md
ª   ª   ª       restore-db.sh
ª   ª   ª       update-all.sh
ª   ª   ª       
ª   ª   +---secrets
ª   ª   ª       dev.secrets.enc
ª   ª   ª       example.secrets.yaml
ª   ª   ª       prod.secrets.enc
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---terraform
ª   ª       ª   main.tf
ª   ª       ª   outputs.tf
ª   ª       ª   provider.tf
ª   ª       ª   README.md
ª   ª       ª   secrets.auto.tfvars
ª   ª       ª   variables.tf
ª   ª       ª   versions.tf
ª   ª       ª   
ª   ª       +---modules
ª   ª       ª   ª   README.md
ª   ª       ª   ª   
ª   ª       ª   +---db
ª   ª       ª   ª       README.md
ª   ª       ª   ª       
ª   ª       ª   +---k8s
ª   ª       ª   ª       README.md
ª   ª       ª   ª       
ª   ª       ª   +---storage
ª   ª       ª   ª       README.md
ª   ª       ª   ª       
ª   ª       ª   +---vpc
ª   ª       ª           README.md
ª   ª       ª           
ª   ª       +---scripts
ª   ª               apply.sh
ª   ª               plan.sh
ª   ª               README.md
ª   ª               
ª   +---docs
ª   ª   ª   ai-integration.md
ª   ª   ª   analytics.md
ª   ª   ª   api.md
ª   ª   ª   ar-guide.md
ª   ª   ª   architecture.md
ª   ª   ª   audit-trail.md
ª   ª   ª   backend-api.md
ª   ª   ª   backend-stack.md
ª   ª   ª   CHANGELOG.md
ª   ª   ª   charts.md
ª   ª   ª   ci-cd.md
ª   ª   ª   code-quality.md
ª   ª   ª   compliance.md
ª   ª   ª   context.md
ª   ª   ª   contract-integration.md
ª   ª   ª   data-pipeline.md
ª   ª   ª   db-schema.md
ª   ª   ª   design-system.md
ª   ª   ª   event-handling.md
ª   ª   ª   event-reference.md
ª   ª   ª   extensions.md
ª   ª   ª   failover-guide.md
ª   ª   ª   faq.md
ª   ª   ª   faqs.md
ª   ª   ª   features.md
ª   ª   ª   fork-testing.md
ª   ª   ª   formal-verification.md
ª   ª   ª   getting-started.md
ª   ª   ª   incident-response.md
ª   ª   ª   integration.md
ª   ª   ª   localization.md
ª   ª   ª   logging-monitoring.md
ª   ª   ª   mainnet-deployment.md
ª   ª   ª   mainnet-hardening.md
ª   ª   ª   migration-guide.md
ª   ª   ª   module-development.md
ª   ª   ª   navigation.md
ª   ª   ª   notification-guide.md
ª   ª   ª   onboarding.md
ª   ª   ª   operator-guide.md
ª   ª   ª   operator-modes.md
ª   ª   ª   operator-roles.md
ª   ª   ª   overlays-ar-xai.md
ª   ª   ª   pages-structure.md
ª   ª   ª   plugin-architecture.md
ª   ª   ª   plugin-system.md
ª   ª   ª   privacy.md
ª   ª   ª   quickstart.md
ª   ª   ª   README.md
ª   ª   ª   release-notes.md
ª   ª   ª   risk-management.md
ª   ª   ª   roadmap.md
ª   ª   ª   security.md
ª   ª   ª   simulation-workflow.md
ª   ª   ª   state-management.md
ª   ª   ª   style-guide.md
ª   ª   ª   test-strategy.md
ª   ª   ª   testing.md
ª   ª   ª   theming.md
ª   ª   ª   troubleshooting.md
ª   ª   ª   upgradeability.md
ª   ª   ª   uploads.md
ª   ª   ª   user-guide.md
ª   ª   ª   widgets.md
ª   ª   ª   xai-guide.md
ª   ª   ª   
ª   ª   +---ai
ª   ª   ª       ai-engine.md
ª   ª   ª       ai-ml-pipeline.md
ª   ª   ª       ai-models.md
ª   ª   ª       ai-ops-guide.md
ª   ª   ª       ai-testing-guide.md
ª   ª   ª       ai-upgradeability.md
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---api
ª   ª   ª       ai-engine-api.yaml
ª   ª   ª       backend-api.yaml
ª   ª   ª       dashboard-api.yaml
ª   ª   ª       notification-api.yaml
ª   ª   ª       plugin-api.yaml
ª   ª   ª       README.md
ª   ª   ª       simulation-api.yaml
ª   ª   ª       
ª   ª   +---audit
ª   ª   ª       audit-log-spec.md
ª   ª   ª       incident-review-checklist.md
ª   ª   ª       operator-audit-demo.csv
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---compliance
ª   ª   ª       aml-logs.md
ª   ª   ª       compliance-audit.md
ª   ª   ª       data-retention.md
ª   ª   ª       kyc-flow.md
ª   ª   ª       README.md
ª   ª   ª       sanctions-workflow.md
ª   ª   ª       
ª   ª   +---dashboard
ª   ª   ª       ai-dashboard.md
ª   ª   ª       dashboard-api.md
ª   ª   ª       dashboard-architecture.md
ª   ª   ª       live-analytics-guide.md
ª   ª   ª       notification-integration.md
ª   ª   ª       overlays-integration.md
ª   ª   ª       plugin-status-panel.md
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---diagrams
ª   ª   ª       ai-integration.drawio
ª   ª   ª       ai-xai-pipeline.svg
ª   ª   ª       backend-architecture.drawio
ª   ª   ª       ci-cd-pipeline.drawio
ª   ª   ª       dashboard-architecture.png
ª   ª   ª       data-pipeline.drawio
ª   ª   ª       failover-diagram.drawio
ª   ª   ª       fork-testing.drawio
ª   ª   ª       incident-response.drawio
ª   ª   ª       operator-dashboard.drawio
ª   ª   ª       operator-flow.svg
ª   ª   ª       plugin-system-sequence.png
ª   ª   ª       plugin-system.drawio
ª   ª   ª       README.md
ª   ª   ª       risk-flow.drawio
ª   ª   ª       simulation-workflow.drawio
ª   ª   ª       state-context-flow.png
ª   ª   ª       
ª   ª   +---formal
ª   ª   ª       ai-formal-verification.md
ª   ª   ª       contract-formal-verification.md
ª   ª   ª       formal-verification-report.md
ª   ª   ª       invariants.md
ª   ª   ª       model-specs.md
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---legacy
ª   ª   ª       deprecated-architecture.md
ª   ª   ª       legacy-api.md
ª   ª   ª       legacy-upgrade-guide.md
ª   ª   ª       old-release-notes.md
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---migration
ª   ª   ª       ai-migration.md
ª   ª   ª       backend-migration.md
ª   ª   ª       contract-migration.md
ª   ª   ª       db-migration.md
ª   ª   ª       plugin-migration.md
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---onboarding
ª   ª   ª       ai-module-onboarding.md
ª   ª   ª       auditor-onboarding.md
ª   ª   ª       developer-onboarding.md
ª   ª   ª       faq-onboarding.md
ª   ª   ª       operator-onboarding.md
ª   ª   ª       plugin-onboarding.md
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---playbooks
ª   ª   ª       disaster-recovery.md
ª   ª   ª       incident-playbook.md
ª   ª   ª       ops-handover.md
ª   ª   ª       README.md
ª   ª   ª       rollback-playbook.md
ª   ª   ª       upgrade-playbook.md
ª   ª   ª       
ª   ª   +---risk
ª   ª   ª       ai-risk.md
ª   ª   ª       bridge-risk.md
ª   ª   ª       incident-catalog.md
ª   ª   ª       kill-switch.md
ª   ª   ª       mev-risk.md
ª   ª   ª       oracle-risk.md
ª   ª   ª       pool-risk.md
ª   ª   ª       README.md
ª   ª   ª       risk-dashboard.md
ª   ª   ª       trade-risk.md
ª   ª   ª       
ª   ª   +---samples
ª   ª   ª       demo-user.csv
ª   ª   ª       onboarding-example.md
ª   ª   ª       plugin-stub.js
ª   ª   ª       README.md
ª   ª   ª       sample-config.json
ª   ª   ª       sample-theme.json
ª   ª   ª       
ª   ª   +---templates
ª   ª           context-provider-template.js
ª   ª           operator-alert-template.md
ª   ª           plugin-template.js
ª   ª           README.md
ª   ª           widget-template.jsx
ª   ª           
ª   +---extensions
ª   ª   ª   CHANGELOG.md
ª   ª   ª   extension-api.md
ª   ª   ª   extension-dev-guide.md
ª   ª   ª   extension-security.md
ª   ª   ª   manifest.json
ª   ª   ª   README.md
ª   ª   ª   registry.json
ª   ª   ª   
ª   ª   +---assets
ª   ª   ª       extension-banner-sample.png
ª   ª   ª       extension-icon-sample.svg
ª   ª   ª       extension-preview-theme.css
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---community
ª   ª   ª       CommunityDiscussionThread.jsx
ª   ª   ª       CommunityExtensionManifest.json
ª   ª   ª       CommunityGalleryPanel.jsx
ª   ª   ª       ExtensionMarketplace.jsx
ª   ª   ª       ExtensionSubmitForm.jsx
ª   ª   ª       README.md
ª   ª   ª       VotingWidget.jsx
ª   ª   ª       
ª   ª   +---core
ª   ª   ª       CoreExtensionLoader.js
ª   ª   ª       CoreExtensionSampleWidget.jsx
ª   ª   ª       CoreExtensionsRegistry.json
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---demo
ª   ª   ª       AnimationPlayground.jsx
ª   ª   ª       DarkModeDemoWidget.jsx
ª   ª   ª       DemoConfigPreset.json
ª   ª   ª       MobileUXPreviewer.jsx
ª   ª   ª       README.md
ª   ª   ª       ThemeDemoPanel.jsx
ª   ª   ª       UXFeedbackCollector.jsx
ª   ª   ª       
ª   ª   +---integration
ª   ª   ª       AnalyticsIntegrationPanel.jsx
ª   ª   ª       ARPluginIntegrationPanel.jsx
ª   ª   ª       ChainlinkIntegrationWidget.jsx
ª   ª   ª       DiscordBotIntegration.jsx
ª   ª   ª       ExternalApiIntegrationWidget.jsx
ª   ª   ª       IntegrationManifest.json
ª   ª   ª       README.md
ª   ª   ª       WebhookBridgeExtension.jsx
ª   ª   ª       XAIExtensionAdapter.js
ª   ª   ª       
ª   ª   +---labs
ª   ª   ª       AdvancedStrategyLab.jsx
ª   ª   ª       AIPrototypePanel.jsx
ª   ª   ª       ExperimentalWidgetGallery.jsx
ª   ª   ª       ExperimentRegistry.json
ª   ª   ª       LabsDemoConfig.json
ª   ª   ª       LabsLauncherPanel.jsx
ª   ª   ª       PatternExplorerLab.jsx
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---plugin
ª   ª   ª       AdvancedPluginDemo.jsx
ª   ª   ª       plugin-manifest.json
ª   ª   ª       PluginConfigEditor.jsx
ª   ª   ª       PluginExtensionTemplate.js
ª   ª   ª       PluginQuickStartSample.jsx
ª   ª   ª       PluginReadme.md
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---samples
ª   ª   ª       extension-onboarding.md
ª   ª   ª       extension-sample-api.js
ª   ª   ª       extension-sample-config.json
ª   ª   ª       extension-sample-doc.md
ª   ª   ª       extension-sample-widget.jsx
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---tests
ª   ª   ª       AnalyticsIntegrationPanel.test.js
ª   ª   ª       CommunityGalleryPanel.test.js
ª   ª   ª       DemoExtensionSandbox.test.js
ª   ª   ª       ExtensionLoader.test.js
ª   ª   ª       ExtensionValidator.test.js
ª   ª   ª       LabsLauncherPanel.test.js
ª   ª   ª       PluginQuickStartSample.test.js
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---utils
ª   ª           extensionDevHelpers.js
ª   ª           extensionHotReload.js
ª   ª           extensionPermissions.js
ª   ª           extensionSandbox.js
ª   ª           extensionValidator.js
ª   ª           README.md
ª   ª           registerExtension.js
ª   ª           
ª   +---fixtures
ª   ª   ª   CHANGELOG.md
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---analytics
ª   ª   ª       anomaly-events-demo.csv
ª   ª   ª       gas-costs-demo.csv
ª   ª   ª       latency-demo.csv
ª   ª   ª       outlier-events-demo.json
ª   ª   ª       pnl-demo.csv
ª   ª   ª       README.md
ª   ª   ª       risk-profile-demo.json
ª   ª   ª       roi-demo.csv
ª   ª   ª       trade-history-demo.csv
ª   ª   ª       
ª   ª   +---api
ª   ª   ª       mock-ai-inference.json
ª   ª   ª       mock-analytics-data.json
ª   ª   ª       mock-arb-alerts.json
ª   ª   ª       mock-health-status.json
ª   ª   ª       mock-incident-events.json
ª   ª   ª       mock-notifications.json
ª   ª   ª       mock-operator-audit.json
ª   ª   ª       mock-overlays.json
ª   ª   ª       mock-pnl-data.json
ª   ª   ª       mock-trade-metrics.json
ª   ª   ª       mock-upload-results.json
ª   ª   ª       mock-user-session.json
ª   ª   ª       mock-websocket-events.json
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---ar
ª   ª   ª       ar-incident-demo.json
ª   ª   ª       ar-user-preset-demo.json
ª   ª   ª       demo-ar-overlays.json
ª   ª   ª       live-pool-demo.json
ª   ª   ª       README.md
ª   ª   ª       xr-demo-assets.json
ª   ª   ª       
ª   ª   +---demo
ª   ª   ª       ai-widget-demo-data.json
ª   ª   ª       dashboard-demo-metrics.json
ª   ª   ª       gas-widget-demo.json
ª   ª   ª       operator-demo-session.json
ª   ª   ª       plugin-demo-config.json
ª   ª   ª       pnl-widget-demo.json
ª   ª   ª       README.md
ª   ª   ª       sandbox-stories.json
ª   ª   ª       trade-volume-demo.json
ª   ª   ª       xai-overlay-demo.json
ª   ª   ª       
ª   ª   +---misc
ª   ª   ª       deprecated-demo.json
ª   ª   ª       migration-sample.json
ª   ª   ª       README.md
ª   ª   ª       seed-data.json
ª   ª   ª       test-data.json
ª   ª   ª       
ª   ª   +---notifications
ª   ª   ª       alert-demo.json
ª   ª   ª       banner-demo.json
ª   ª   ª       incident-toast-demo.json
ª   ª   ª       operator-notification-demo.json
ª   ª   ª       README.md
ª   ª   ª       webhook-demo.json
ª   ª   ª       
ª   ª   +---operator
ª   ª   ª       audit-timeline-demo.json
ª   ª   ª       escalation-demo.json
ª   ª   ª       incident-log-demo.json
ª   ª   ª       kill-switch-events-demo.json
ª   ª   ª       README.md
ª   ª   ª       shift-demo-schedule.json
ª   ª   ª       
ª   ª   +---plugins
ª   ª   ª       extension-gallery-demo.json
ª   ª   ª       plugin-config-demo.json
ª   ª   ª       plugin-marketplace-demo.json
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---test-utils
ª   ª   ª       demo-api-client.js
ª   ª   ª       fixtures.test.js
ª   ª   ª       README.md
ª   ª   ª       sample-mock-store.js
ª   ª   ª       
ª   ª   +---user
ª   ª           demo-locale-settings.json
ª   ª           demo-user-profile.json
ª   ª           onboarding-tour-demo.json
ª   ª           README.md
ª   ª           theme-preset-demo.json
ª   ª           
ª   +---hooks
ª   ª       hooks.test.js
ª   ª       index.js
ª   ª       README.md
ª   ª       useAI.js
ª   ª       useAIFeedback.js
ª   ª       useAIInsight.js
ª   ª       useAIScoring.js
ª   ª       useAlerts.js
ª   ª       useAnalyticsData.js
ª   ª       useApi.js
ª   ª       useAppState.js
ª   ª       useArbStats.js
ª   ª       useARCameraStream.js
ª   ª       useARIncidentFeed.js
ª   ª       useAROperatorMode.js
ª   ª       useAROverlay.js
ª   ª       useARSession.js
ª   ª       useAuth.js
ª   ª       useBanner.js
ª   ª       useBreadcrumbs.js
ª   ª       useClipboard.js
ª   ª       useDropzone.js
ª   ª       useExtensionRegistry.js
ª   ª       useFileUpload.js
ª   ª       useFocusTrap.js
ª   ª       useGasTrends.js
ª   ª       useHydrated.js
ª   ª       useLabsExperiment.js
ª   ª       useLatencyStats.js
ª   ª       useLayout.js
ª   ª       useLiveData.js
ª   ª       useLivePnL.js
ª   ª       useLocale.js
ª   ª       useLocalStorage.js
ª   ª       useModal.js
ª   ª       useModelAudit.js
ª   ª       useModelSwitcher.js
ª   ª       useNavigation.js
ª   ª       useNotifications.js
ª   ª       useOnboarding.js
ª   ª       useOperator.js
ª   ª       useOperatorShift.js
ª   ª       usePersistedState.js
ª   ª       usePlugin.js
ª   ª       useRiskRegression.js
ª   ª       useSession.js
ª   ª       useSettings.js
ª   ª       useStateSync.js
ª   ª       useStorybookState.js
ª   ª       useSWRApi.js
ª   ª       useTheme.js
ª   ª       useTimeAgo.js
ª   ª       useUserProfile.js
ª   ª       useVisibility.js
ª   ª       useVolumeTimeseries.js
ª   ª       useWebhookListener.js
ª   ª       useWebsocket.js
ª   ª       useWidgetTestHarness.js
ª   ª       useXAI.js
ª   ª       useXRScene.js
ª   ª       
ª   +---integration
ª   ª       AlertSyncAdapter.js
ª   ª       AnalyticsAdapter.js
ª   ª       ApiBridge.js
ª   ª       ArbScoringSync.js
ª   ª       ARControlBridge.js
ª   ª       ARStreamAdapter.js
ª   ª       BotMessageBridge.js
ª   ª       ChainDataBridge.js
ª   ª       DiscordBotConnector.js
ª   ª       ExtensionRegistrySync.js
ª   ª       HealthCheckDisplay.jsx
ª   ª       HealthCheckDisplay.test.jsx
ª   ª       InsightsBridge.js
ª   ª       integration.test.js
ª   ª       IntegrationCache.js
ª   ª       integrationConfig.json
ª   ª       IntegrationDebugOverlay.jsx
ª   ª       IntegrationDevPanel.jsx
ª   ª       IntegrationLatencyMeter.jsx
ª   ª       IntegrationLogger.js
ª   ª       IntegrationStatusCard.jsx
ª   ª       IntegrationToggleSwitch.jsx
ª   ª       integrationUtils.js
ª   ª       LabsStatusBridge.js
ª   ª       mockIntegrationData.json
ª   ª       OperatorSyncBridge.js
ª   ª       PluginSyncAdapter.js
ª   ª       PluginSyncAdapter.test.js
ª   ª       README.md
ª   ª       SSEBridge.js
ª   ª       SyncErrorBoundary.jsx
ª   ª       useIntegrationStatus.js
ª   ª       WebhookReceiver.js
ª   ª       WebsocketBridge.js
ª   ª       WebsocketBridge.test.js
ª   ª       XAIAdapter.js
ª   ª       XAIAdapter.test.js
ª   ª       XRCanvasSync.js
ª   ª       
ª   +---layouts
ª   ª       README.md
ª   ª       
ª   +---locales
ª   ª       README.md
ª   ª       
ª   +---mock
ª   ª   ª   api-handlers.js
ª   ª   ª   api-handlers.test.js
ª   ª   ª   CHANGELOG.md
ª   ª   ª   factories.test.js
ª   ª   ª   faker-config.js
ª   ª   ª   hot-reload-mocks.js
ª   ª   ª   inject-mocks.js
ª   ª   ª   mirage-readme.md
ª   ª   ª   mirage-server.js
ª   ª   ª   mirage-server.test.js
ª   ª   ª   mock-server.js
ª   ª   ª   mock-utils.js
ª   ª   ª   mock.test.js
ª   ª   ª   mockConfig.json
ª   ª   ª   msw-readme.md
ª   ª   ª   msw-server.js
ª   ª   ª   README.md
ª   ª   ª   scenario-presets.test.js
ª   ª   ª   scenario-switcher.js
ª   ª   ª   setup-mock-env.js
ª   ª   ª   socket-mock-server.js
ª   ª   ª   
ª   ª   +---api-responses
ª   ª   ª       mock-ai-inference.json
ª   ª   ª       mock-analytics-data.json
ª   ª   ª       mock-arb-alerts.json
ª   ª   ª       mock-health-status.json
ª   ª   ª       mock-incident-events.json
ª   ª   ª       mock-notifications.json
ª   ª   ª       mock-operator-audit.json
ª   ª   ª       mock-overlays.json
ª   ª   ª       mock-pnl-data.json
ª   ª   ª       mock-trade-metrics.json
ª   ª   ª       mock-upload-results.json
ª   ª   ª       mock-user-session.json
ª   ª   ª       mock-websocket-events.json
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---factories
ª   ª   ª       aiInferenceFactory.js
ª   ª   ª       analyticsFactory.js
ª   ª   ª       incidentFactory.js
ª   ª   ª       notificationFactory.js
ª   ª   ª       poolFactory.js
ª   ª   ª       README.md
ª   ª   ª       tradeFactory.js
ª   ª   ª       userFactory.js
ª   ª   ª       
ª   ª   +---scenario-presets
ª   ª           ai-demo-state.json
ª   ª           incident-demo-state.json
ª   ª           operator-demo-state.json
ª   ª           README.md
ª   ª           trade-surge-state.json
ª   ª           
ª   +---modals
ª   ª       AccountSwitchDialog.jsx
ª   ª       AIExplainDialog.jsx
ª   ª       AIFeedbackModal.jsx
ª   ª       AlertModal.jsx
ª   ª       ARPermissionModal.jsx
ª   ª       AuditReviewDialog.jsx
ª   ª       ConfirmDialog.jsx
ª   ª       CustomModal.jsx
ª   ª       DebugModal.jsx
ª   ª       DialogQueueProvider.jsx
ª   ª       ErrorModal.jsx
ª   ª       ExportDialog.jsx
ª   ª       ExtensionMarketplaceDialog.jsx
ª   ª       FileUploadModal.jsx
ª   ª       HelpDialog.jsx
ª   ª       IncidentDetailModal.jsx
ª   ª       index.js
ª   ª       InfoDialog.jsx
ª   ª       KillSwitchModal.jsx
ª   ª       LabsDialog.jsx
ª   ª       ModalHost.jsx
ª   ª       modals.test.js
ª   ª       ModelSwitcherDialog.jsx
ª   ª       NotificationModal.jsx
ª   ª       OnboardingModal.jsx
ª   ª       OperatorCommandDialog.jsx
ª   ª       OverlaySettingsDialog.jsx
ª   ª       PluginConfigDialog.jsx
ª   ª       PluginDialog.jsx
ª   ª       ProfileSettingsModal.jsx
ª   ª       README.md
ª   ª       SettingsDialog.jsx
ª   ª       ShiftChangeDialog.jsx
ª   ª       TourDialog.jsx
ª   ª       WelcomeDialog.jsx
ª   ª       XAIOverlayDialog.jsx
ª   ª       
ª   +---notifications
ª   ª   ª   AIInsightAlert.jsx
ª   ª   ª   AlertBadge.jsx
ª   ª   ª   AlertCountdown.jsx
ª   ª   ª   AlertStatusPill.jsx
ª   ª   ª   CHANGELOG.md
ª   ª   ª   EmailNotification.jsx
ª   ª   ª   EscalationAlertBar.jsx
ª   ª   ª   IncidentAlertBar.jsx
ª   ª   ª   IncidentResponseToast.jsx
ª   ª   ª   InlineAlert.jsx
ª   ª   ª   mockNotificationServer.js
ª   ª   ª   MultiChannelAlert.jsx
ª   ª   ª   notification-best-practices.md
ª   ª   ª   notificationApi.js
ª   ª   ª   NotificationBanner.jsx
ª   ª   ª   NotificationCenter.jsx
ª   ª   ª   notificationDevPanel.jsx
ª   ª   ª   NotificationPanel.jsx
ª   ª   ª   notifications.test.js
ª   ª   ª   NotificationsContext.js
ª   ª   ª   NotificationsProvider.jsx
ª   ª   ª   notificationStories.md
ª   ª   ª   notificationTemplates.js
ª   ª   ª   notificationUtils.js
ª   ª   ª   OperatorAlert.jsx
ª   ª   ª   PushNotificationPanel.jsx
ª   ª   ª   README.md
ª   ª   ª   Snackbar.jsx
ª   ª   ª   ToastContainer.jsx
ª   ª   ª   useNotifications.js
ª   ª   ª   WebhookAlert.jsx
ª   ª   ª   
ª   ª   +---testData
ª   ª           demo-notifications.json
ª   ª           incident-alerts-demo.json
ª   ª           README.md
ª   ª           
ª   +---operator
ª   ª       README.md
ª   ª       
ª   +---overlays
ª   ª       AlertBanner.jsx
ª   ª       ARIncidentOverlay.jsx
ª   ª       AROverlay.jsx
ª   ª       ConnectionStatusOverlay.jsx
ª   ª       DebugOverlay.jsx
ª   ª       EscalationOverlay.jsx
ª   ª       IncidentBannerOverlay.jsx
ª   ª       IncidentOverlay.jsx
ª   ª       index.js
ª   ª       LatencyOverlay.jsx
ª   ª       OperatorCamOverlay.jsx
ª   ª       OperatorOverlay.jsx
ª   ª       OverlayConfigPanel.jsx
ª   ª       OverlayHotkeys.js
ª   ª       OverlayPortal.jsx
ª   ª       OverlayProvider.jsx
ª   ª       OverlayRoot.jsx
ª   ª       overlays.test.js
ª   ª       OverlaySettingsModal.jsx
ª   ª       OverlayToggleButton.jsx
ª   ª       OverlayTransition.js
ª   ª       overlayUtils.js
ª   ª       README.md
ª   ª       RiskOverlay.jsx
ª   ª       StatusOverlay.jsx
ª   ª       TradePathOverlay.jsx
ª   ª       XAIHeatmapOverlay.jsx
ª   ª       XAIOverlay.jsx
ª   ª       
ª   +---pages
ª   ª   ª   404.js
ª   ª   ª   500.js
ª   ª   ª   account.js
ª   ª   ª   ai.js
ª   ª   ª   alerts.js
ª   ª   ª   analytics.js
ª   ª   ª   ar.js
ª   ª   ª   assets.js
ª   ª   ª   backup.js
ª   ª   ª   cam.js
ª   ª   ª   changelog.js
ª   ª   ª   dashboard.js
ª   ª   ª   dev.js
ª   ª   ª   docs.js
ª   ª   ª   download.js
ª   ª   ª   edge.js
ª   ª   ª   escalation.js
ª   ª   ª   extensions.js
ª   ª   ª   failover.js
ª   ª   ª   gas.js
ª   ª   ª   health.js
ª   ª   ª   help.js
ª   ª   ª   history.js
ª   ª   ª   i18n.js
ª   ª   ª   incidents.js
ª   ª   ª   index.js
ª   ª   ª   kill-switch.js
ª   ª   ª   latency.js
ª   ª   ª   legal.js
ª   ª   ª   liquidity.js
ª   ª   ª   login.js
ª   ª   ª   logs.js
ª   ª   ª   maintenance.js
ª   ª   ª   marketplace.js
ª   ª   ª   metrics.js
ª   ª   ª   onboarding-tour.js
ª   ª   ª   onboarding.js
ª   ª   ª   operator.js
ª   ª   ª   overlays.js
ª   ª   ª   pattern-404.js
ª   ª   ª   pattern-dashboard.js
ª   ª   ª   pattern-modal.js
ª   ª   ª   plugins.js
ª   ª   ª   pnl.js
ª   ª   ª   preview.js
ª   ª   ª   privacy.js
ª   ª   ª   profile.js
ª   ª   ª   README.md
ª   ª   ª   register.js
ª   ª   ª   reset-password.js
ª   ª   ª   risk.js
ª   ª   ª   robots.txt
ª   ª   ª   sandbox.js
ª   ª   ª   settings.js
ª   ª   ª   sitemap.xml
ª   ª   ª   status.js
ª   ª   ª   storybook.js
ª   ª   ª   team.js
ª   ª   ª   test.js
ª   ª   ª   theme.js
ª   ª   ª   trades.js
ª   ª   ª   uploads.js
ª   ª   ª   users.js
ª   ª   ª   verify-email.js
ª   ª   ª   wallets.js
ª   ª   ª   welcome.js
ª   ª   ª   xai.js
ª   ª   ª   [...slug].js
ª   ª   ª   _app.js
ª   ª   ª   _document.js
ª   ª   ª   _error.js
ª   ª   ª   _middleware.js
ª   ª   ª   
ª   ª   +---api
ª   ª           ai.js
ª   ª           arb.js
ª   ª           dev.js
ª   ª           extension.js
ª   ª           health.js
ª   ª           index.js
ª   ª           metrics.js
ª   ª           notifications.js
ª   ª           plugin.js
ª   ª           README.md
ª   ª           user.js
ª   ª           webhook.js
ª   ª           
ª   +---plugins
ª   ª   ª   atomic-swap-batched.ts
ª   ª   ª   bridge-latency-sniper.ts
ª   ª   ª   CHANGELOG.md
ª   ª   ª   ExtensionPluginAdapter.js
ª   ª   ª   flash-sandwich-mm.ts
ª   ª   ª   hyper-bundle-engine.ts
ª   ª   ª   index.js
ª   ª   ª   MarketplaceQAStatus.jsx
ª   ª   ª   MarketplaceSubmissionForm.jsx
ª   ª   ª   micro-latency-arb-suite.ts
ª   ª   ª   nft-gamefi-arb.ts
ª   ª   ª   plugin-api.test.js
ª   ª   ª   plugin-architecture.md
ª   ª   ª   plugin-best-practices.md
ª   ª   ª   plugin-marketplace.test.js
ª   ª   ª   plugin-sandbox.test.js
ª   ª   ª   plugin-schema.json
ª   ª   ª   plugin-types.js
ª   ª   ª   PluginAdapter.js
ª   ª   ª   PluginAPI.js
ª   ª   ª   PluginApiBridge.js
ª   ª   ª   PluginAuditLog.js
ª   ª   ª   PluginCard.jsx
ª   ª   ª   PluginConfig.js
ª   ª   ª   PluginConfigForm.jsx
ª   ª   ª   PluginContext.js
ª   ª   ª   PluginDataSync.js
ª   ª   ª   PluginDetails.jsx
ª   ª   ª   PluginDevToolsPanel.jsx
ª   ª   ª   PluginDialog.jsx
ª   ª   ª   PluginErrorBoundary.jsx
ª   ª   ª   PluginEventBus.js
ª   ª   ª   PluginFactory.js
ª   ª   ª   PluginHotReload.js
ª   ª   ª   PluginInstallDialog.jsx
ª   ª   ª   PluginInterface.js
ª   ª   ª   PluginLifecycle.js
ª   ª   ª   PluginList.jsx
ª   ª   ª   PluginLoader.js
ª   ª   ª   PluginManager.jsx
ª   ª   ª   PluginManifest.js
ª   ª   ª   PluginMarketplace.jsx
ª   ª   ª   PluginMetadata.js
ª   ª   ª   PluginPanel.jsx
ª   ª   ª   PluginPermissions.json
ª   ª   ª   PluginProvider.jsx
ª   ª   ª   PluginQuickStartSample.jsx
ª   ª   ª   PluginReadme.md
ª   ª   ª   PluginRegistry.json
ª   ª   ª   plugins.test.js
ª   ª   ª   PluginSandbox.jsx
ª   ª   ª   PluginSandboxLauncher.js
ª   ª   ª   PluginSecurityManager.js
ª   ª   ª   PluginSettings.jsx
ª   ª   ª   PluginStatusIndicator.jsx
ª   ª   ª   PluginToggle.jsx
ª   ª   ª   PluginValidator.js
ª   ª   ª   PluginVersion.js
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---alpha-signal
ª   ª   ª   ª   ai-signal-orchestrator.js
ª   ª   ª   ª   alpha-nft-issuer.js
ª   ª   ª   ª   alpha-reputation.js
ª   ª   ª   ª   alpha-voting.js
ª   ª   ª   ª   micro-arb-detector.js
ª   ª   ª   ª   README.md
ª   ª   ª   ª   sandwich-detector.js
ª   ª   ª   ª   sniping-detector.js
ª   ª   ª   ª   trend-analyzer-v2.js
ª   ª   ª   ª   trend-analyzer.js
ª   ª   ª   ª   whale-signal.js
ª   ª   ª   ª   
ª   ª   ª   +---docs
ª   ª   ª   ª       alerts-integration.md
ª   ª   ª   ª       alpha-reputation-scores.md
ª   ª   ª   ª       alpha-signal-models.md
ª   ª   ª   ª       alpha-voting-protocol.md
ª   ª   ª   ª       arb-patterns.md
ª   ª   ª   ª       README.md
ª   ª   ª   ª       
ª   ª   ª   +---tests
ª   ª   ª           ai-signal-orchestrator.test.js
ª   ª   ª           alpha-nft-issuer.test.js
ª   ª   ª           alpha-reputation.test.js
ª   ª   ª           alpha-voting.test.js
ª   ª   ª           micro-arb-detector.test.js
ª   ª   ª           README.md
ª   ª   ª           sandwich-detector.test.js
ª   ª   ª           sniping-detector.test.js
ª   ª   ª           trend-analyzer-v2.test.js
ª   ª   ª           trend-analyzer.test.js
ª   ª   ª           whale-signal.test.js
ª   ª   ª           
ª   ª   +---bridge-adapters
ª   ª   ª   ª   avalanche-adapter.js
ª   ª   ª   ª   axelar-adapter.js
ª   ª   ª   ª   circle-cctp-adapter.js
ª   ª   ª   ª   cross-twin-adapter.js
ª   ª   ª   ª   elliptic-adapter.js
ª   ª   ª   ª   layerzero-adapter.js
ª   ª   ª   ª   polygon-zkevm-adapter.js
ª   ª   ª   ª   range-cross-chain-adapter.js
ª   ª   ª   ª   README.md
ª   ª   ª   ª   relaychain-adapter.js
ª   ª   ª   ª   symbiosis-adapter.js
ª   ª   ª   ª   wormhole-adapter.js
ª   ª   ª   ª   
ª   ª   ª   +---docs
ª   ª   ª   ª       avalanche-guide.md
ª   ª   ª   ª       bridge-integrations.md
ª   ª   ª   ª       cross-chain-security.md
ª   ª   ª   ª       polygon-zkevm-guide.md
ª   ª   ª   ª       README.md
ª   ª   ª   ª       relaychain-integration.md
ª   ª   ª   ª       
ª   ª   ª   +---tests
ª   ª   ª           avalanche-adapter.test.js
ª   ª   ª           axelar-adapter.test.js
ª   ª   ª           circle-cctp-adapter.test.js
ª   ª   ª           cross-twin-adapter.test.js
ª   ª   ª           elliptic-adapter.test.js
ª   ª   ª           layerzero-adapter.test.js
ª   ª   ª           polygon-zkevm-adapter.test.js
ª   ª   ª           range-cross-chain-adapter.test.js
ª   ª   ª           README.md
ª   ª   ª           relaychain-adapter.test.js
ª   ª   ª           symbiosis-adapter.test.js
ª   ª   ª           wormhole-adapter.test.js
ª   ª   ª           
ª   ª   +---compliance
ª   ª   ª   ª   adverse-media-scanner.js
ª   ª   ª   ª   blacklist-module.js
ª   ª   ª   ª   dispute-module.js
ª   ª   ª   ª   forensics-module.js
ª   ª   ª   ª   jurisdiction-manager.js
ª   ª   ª   ª   kyc-aml-module.js
ª   ª   ª   ª   pep-checker.js
ª   ª   ª   ª   permission-validator.js
ª   ª   ª   ª   rbac-enforcer.js
ª   ª   ª   ª   README.md
ª   ª   ª   ª   sanctions-checker.js
ª   ª   ª   ª   whitelist-module.js
ª   ª   ª   ª   
ª   ª   ª   +---docs
ª   ª   ª   ª       compliance-checks.md
ª   ª   ª   ª       forensics-guide.md
ª   ª   ª   ª       governance-controls.md
ª   ª   ª   ª       kyc-flows.md
ª   ª   ª   ª       README.md
ª   ª   ª   ª       sanctions-lists.md
ª   ª   ª   ª       
ª   ª   ª   +---tests
ª   ª   ª           adverse-media-scanner.test.js
ª   ª   ª           blacklist-module.test.js
ª   ª   ª           dispute-module.test.js
ª   ª   ª           forensics-module.test.js
ª   ª   ª           jurisdiction-manager.test.js
ª   ª   ª           kyc-aml-module.test.js
ª   ª   ª           pep-checker.test.js
ª   ª   ª           permission-validator.test.js
ª   ª   ª           rbac-enforcer.test.js
ª   ª   ª           README.md
ª   ª   ª           sanctions-checker.test.js
ª   ª   ª           whitelist-module.test.js
ª   ª   ª           
ª   ª   +---dex-adapters
ª   ª   ª   ª   aggregator-adapter.js
ª   ª   ª   ª   balancer-adapter.js
ª   ª   ª   ª   cowswap-adapter.js
ª   ª   ª   ª   curve-adapter.js
ª   ª   ª   ª   dodo-adapter.js
ª   ª   ª   ª   fraxswap-adapter.js
ª   ª   ª   ª   kyber-adapter.js
ª   ª   ª   ª   maverick-adapter.js
ª   ª   ª   ª   orca-adapter.js
ª   ª   ª   ª   pancake-adapter.js
ª   ª   ª   ª   quickswap-adapter.js
ª   ª   ª   ª   README.md
ª   ª   ª   ª   sushi-adapter.js
ª   ª   ª   ª   synthetix-adapter.js
ª   ª   ª   ª   thorchain-adapter.js
ª   ª   ª   ª   traderjoe-adapter.js
ª   ª   ª   ª   uniswap-v3-adapter.js
ª   ª   ª   ª   vertex-adapter.js
ª   ª   ª   ª   woofi-adapter.js
ª   ª   ª   ª   
ª   ª   ª   +---docs
ª   ª   ª   ª       adapter-development.md
ª   ª   ª   ª       dex-architecture.md
ª   ª   ª   ª       gas-optimizations.md
ª   ª   ª   ª       integration-guide.md
ª   ª   ª   ª       README.md
ª   ª   ª   ª       slippage-models.md
ª   ª   ª   ª       supported-dexes.md
ª   ª   ª   ª       
ª   ª   ª   +---tests
ª   ª   ª           aggregator-adapter.test.js
ª   ª   ª           balancer-adapter.test.js
ª   ª   ª           cowswap-adapter.test.js
ª   ª   ª           curve-adapter.test.js
ª   ª   ª           dodo-adapter.test.js
ª   ª   ª           fraxswap-adapter.test.js
ª   ª   ª           kyber-adapter.test.js
ª   ª   ª           maverick-adapter.test.js
ª   ª   ª           orca-adapter.test.js
ª   ª   ª           pancake-adapter.test.js
ª   ª   ª           quickswap-adapter.test.js
ª   ª   ª           README.md
ª   ª   ª           sushi-adapter.test.js
ª   ª   ª           synthetix-adapter.test.js
ª   ª   ª           thorchain-adapter.test.js
ª   ª   ª           traderjoe-adapter.test.js
ª   ª   ª           uniswap-v3-adapter.test.js
ª   ª   ª           vertex-adapter.test.js
ª   ª   ª           woofi-adapter.test.js
ª   ª   ª           
ª   ª   +---docs
ª   ª   ª       adapter-api.md
ª   ª   ª       alpha-patterns.md
ª   ª   ª       fork-testing-guide.md
ª   ª   ª       integration-scenarios.md
ª   ª   ª       mev-risk-mitigation.md
ª   ª   ª       plugin-development.md
ª   ª   ª       plugins-architecture.md
ª   ª   ª       README.md
ª   ª   ª       registry-guide.md
ª   ª   ª       smart-contract-integration.md
ª   ª   ª       
ª   ª   +---flashloan
ª   ª   ª   ª   aave-adapter.js
ª   ª   ª   ª   angle-adapter.js
ª   ª   ª   ª   compound-adapter.js
ª   ª   ª   ª   cream-adapter.js
ª   ª   ª   ª   dydx-adapter.js
ª   ª   ª   ª   flashbots-adapter.js
ª   ª   ª   ª   gearbox-adapter.js
ª   ª   ª   ª   makerdao-adapter.js
ª   ª   ª   ª   morpho-adapter.js
ª   ª   ª   ª   parasite-arb-adapter.js
ª   ª   ª   ª   radiant-adapter.js
ª   ª   ª   ª   README.md
ª   ª   ª   ª   stargate-adapter.js
ª   ª   ª   ª   
ª   ª   ª   +---docs
ª   ª   ª   ª       audit-log.md
ª   ª   ª   ª       flashloan-architecture.md
ª   ª   ª   ª       flashloan-risks.md
ª   ª   ª   ª       provider-integrations.md
ª   ª   ª   ª       README.md
ª   ª   ª   ª       upgrade-guide.md
ª   ª   ª   ª       
ª   ª   ª   +---tests
ª   ª   ª           aave-adapter.test.js
ª   ª   ª           angle-adapter.test.js
ª   ª   ª           compound-adapter.test.js
ª   ª   ª           cream-adapter.test.js
ª   ª   ª           dydx-adapter.test.js
ª   ª   ª           flashbots-adapter.test.js
ª   ª   ª           gearbox-adapter.test.js
ª   ª   ª           makerdao-adapter.test.js
ª   ª   ª           morpho-adapter.test.js
ª   ª   ª           parasite-arb-adapter.test.js
ª   ª   ª           radiant-adapter.test.js
ª   ª   ª           README.md
ª   ª   ª           stargate-adapter.test.js
ª   ª   ª           
ª   ª   +---insurance
ª   ª   ª   ª   claim-auditor.js
ª   ª   ª   ª   claim-verifier.js
ª   ª   ª   ª   coverage-oracle.js
ª   ª   ª   ª   incident-monitor.js
ª   ª   ª   ª   insurance-pool-manager.js
ª   ª   ª   ª   payout-calculator.js
ª   ª   ª   ª   premium-calculator.js
ª   ª   ª   ª   README.md
ª   ª   ª   ª   risk-assessment-plugin.js
ª   ª   ª   ª   risk-modeler.js
ª   ª   ª   ª   
ª   ª   ª   +---docs
ª   ª   ª   ª       claim-workflow.md
ª   ª   ª   ª       insurance-architecture.md
ª   ª   ª   ª       pool-audits.md
ª   ª   ª   ª       README.md
ª   ª   ª   ª       risk-assessment-methods.md
ª   ª   ª   ª       risk-models.md
ª   ª   ª   ª       
ª   ª   ª   +---tests
ª   ª   ª           claim-auditor.test.js
ª   ª   ª           claim-verifier.test.js
ª   ª   ª           coverage-oracle.test.js
ª   ª   ª           incident-monitor.test.js
ª   ª   ª           insurance-pool-manager.test.js
ª   ª   ª           payout-calculator.test.js
ª   ª   ª           premium-calculator.test.js
ª   ª   ª           README.md
ª   ª   ª           risk-assessment-plugin.test.js
ª   ª   ª           risk-modeler.test.js
ª   ª   ª           
ª   ª   +---intent-solvers
ª   ª   ª   ª   auction-intent-solver.js
ª   ª   ª   ª   batch-intent-processor.js
ª   ª   ª   ª   cow-intent-solver.js
ª   ª   ª   ª   eco-intent-solver.js
ª   ª   ª   ª   intent-forker.js
ª   ª   ª   ª   intent-merger.js
ª   ª   ª   ª   keepers-intent-solver.js
ª   ª   ª   ª   README.md
ª   ª   ª   ª   rfq-intent-solver.js
ª   ª   ª   ª   sandwich-intent-solver.js
ª   ª   ª   ª   sniper-intent-solver.js
ª   ª   ª   ª   uniswapx-intent-solver.js
ª   ª   ª   ª   
ª   ª   ª   +---docs
ª   ª   ª   ª       auction-design.md
ª   ª   ª   ª       eco-intents.md
ª   ª   ª   ª       intent-architecture.md
ª   ª   ª   ª       intent-merging.md
ª   ª   ª   ª       README.md
ª   ª   ª   ª       
ª   ª   ª   +---tests
ª   ª   ª           auction-intent-solver.test.js
ª   ª   ª           batch-intent-processor.test.js
ª   ª   ª           cow-intent-solver.test.js
ª   ª   ª           eco-intent-solver.test.js
ª   ª   ª           intent-forker.test.js
ª   ª   ª           intent-merger.test.js
ª   ª   ª           keepers-intent-solver.test.js
ª   ª   ª           README.md
ª   ª   ª           rfq-intent-solver.test.js
ª   ª   ª           sandwich-intent-solver.test.js
ª   ª   ª           sniper-intent-solver.test.js
ª   ª   ª           uniswapx-intent-solver.test.js
ª   ª   ª           
ª   ª   +---internal
ª   ª   ª       interface-definitions.ts
ª   ª   ª       migration-tool.js
ª   ª   ª       plugin-manager.ts
ª   ª   ª       plugin-utils.js
ª   ª   ª       plugins.json
ª   ª   ª       README.md
ª   ª   ª       registry.ts
ª   ª   ª       test-utils.js
ª   ª   ª       
ª   ª   +---marketplace
ª   ª   ª       governance-marketplace.js
ª   ª   ª       module-marketplace-registry.json
ª   ª   ª       module-marketplace.js
ª   ª   ª       plugin-marketplace-registry.json
ª   ª   ª       plugin-marketplace.js
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---model-marketplace
ª   ª   ª       ai-model-marketplace-registry.json
ª   ª   ª       ai-model-marketplace.js
ª   ª   ª       ai-model-metadata.json
ª   ª   ª       ai-model-proxy.js
ª   ª   ª       ai-model-validator.js
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---oracles
ª   ª   ª   ª   ai-oracle.js
ª   ª   ª   ª   chainlink-oracle.js
ª   ª   ª   ª   compliance-oracle.js
ª   ª   ª   ª   external-data-oracle.js
ª   ª   ª   ª   fallback-oracle.js
ª   ª   ª   ª   liquidity-oracle.js
ª   ª   ª   ª   onchain-oracle.js
ª   ª   ª   ª   README.md
ª   ª   ª   ª   time-weighted-oracle.js
ª   ª   ª   ª   volatility-oracle.js
ª   ª   ª   ª   zero-knowledge-oracle.js
ª   ª   ª   ª   
ª   ª   ª   +---docs
ª   ª   ª   ª       data-sources.md
ª   ª   ª   ª       oracle-integrations.md
ª   ª   ª   ª       README.md
ª   ª   ª   ª       risk-mitigation.md
ª   ª   ª   ª       zk-proofs.md
ª   ª   ª   ª       
ª   ª   ª   +---tests
ª   ª   ª           ai-oracle.test.js
ª   ª   ª           chainlink-oracle.test.js
ª   ª   ª           compliance-oracle.test.js
ª   ª   ª           external-data-oracle.test.js
ª   ª   ª           fallback-oracle.test.js
ª   ª   ª           liquidity-oracle.test.js
ª   ª   ª           onchain-oracle.test.js
ª   ª   ª           README.md
ª   ª   ª           time-weighted-oracle.test.js
ª   ª   ª           volatility-oracle.test.js
ª   ª   ª           zero-knowledge-oracle.test.js
ª   ª   ª           
ª   ª   +---samples
ª   ª   ª       demo-plugin-index.js
ª   ª   ª       demo-plugin-manifest.json
ª   ª   ª       demo-plugin-ui.jsx
ª   ª   ª       plugin-boilerplate.md
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---social-impact
ª   ª   ª   ª   carbon-offset-module.js
ª   ª   ª   ª   charity-oracle.js
ª   ª   ª   ª   csr-audit.js
ª   ª   ª   ª   donation-router.js
ª   ª   ª   ª   esg-allocator.js
ª   ª   ª   ª   grants-engine.js
ª   ª   ª   ª   green-bond-manager.js
ª   ª   ª   ª   impact-scoring.js
ª   ª   ª   ª   impact-voting.js
ª   ª   ª   ª   README.md
ª   ª   ª   ª   
ª   ª   ª   +---docs
ª   ª   ª   ª       charity-protocols.md
ª   ª   ª   ª       csr-programs.md
ª   ª   ª   ª       esg-logic.md
ª   ª   ª   ª       impact-scoring-models.md
ª   ª   ª   ª       README.md
ª   ª   ª   ª       social-impact-flows.md
ª   ª   ª   ª       
ª   ª   ª   +---tests
ª   ª   ª           carbon-offset-module.test.js
ª   ª   ª           charity-oracle.test.js
ª   ª   ª           csr-audit.test.js
ª   ª   ª           donation-router.test.js
ª   ª   ª           esg-allocator.test.js
ª   ª   ª           grants-engine.test.js
ª   ª   ª           green-bond-manager.test.js
ª   ª   ª           impact-scoring.test.js
ª   ª   ª           impact-voting.test.js
ª   ª   ª           README.md
ª   ª   ª           
ª   ª   +---template
ª   ª   ª       adapter-template.js
ª   ª   ª       model-template.js
ª   ª   ª       plugin-template.js
ª   ª   ª       README.md
ª   ª   ª       template-config.json
ª   ª   ª       
ª   ª   +---tests
ª   ª           ai-model-marketplace.test.js
ª   ª           atomic-swap-batched.test.ts
ª   ª           bridge-latency-sniper.test.ts
ª   ª           flash-sandwich-mm.test.ts
ª   ª           governance-marketplace.test.js
ª   ª           hyper-bundle-engine.test.ts
ª   ª           micro-latency-arb-suite.test.ts
ª   ª           nft-gamefi-arb.test.ts
ª   ª           plugin-manager.test.js
ª   ª           plugins-integration.test.js
ª   ª           README.md
ª   ª           test-utils.js
ª   ª           
ª   +---presets
ª   ª   ª   advanced-presets.json
ª   ª   ª   ai-presets.json
ª   ª   ª   backup-presets.json
ª   ª   ª   CHANGELOG.md
ª   ª   ª   custom-preset-guide.md
ª   ª   ª   demo-presets.json
ª   ª   ª   layout-presets.json
ª   ª   ª   pattern-presets.json
ª   ª   ª   patterns.md
ª   ª   ª   presets-best-practices.md
ª   ª   ª   presets.test.js
ª   ª   ª   quickstart-presets.json
ª   ª   ª   README.md
ª   ª   ª   sample-presets.json
ª   ª   ª   strategy-presets.json
ª   ª   ª   theme-presets.json
ª   ª   ª   ui-presets.json
ª   ª   ª   user-presets.json
ª   ª   ª   
ª   ª   +---custom-presets
ª   ª   ª       high-volatility-preset.json
ª   ª   ª       minimal-view-preset.json
ª   ª   ª       night-trading-preset.json
ª   ª   ª       README.md
ª   ª   ª       sample-operator-preset.json
ª   ª   ª       
ª   ª   +---templates
ª   ª           dev-preset.json
ª   ª           onboarding-preset.json
ª   ª           preset-template.json
ª   ª           README.md
ª   ª           
ª   +---preview
ª   ª       CHANGELOG.md
ª   ª       feature-flags.json
ª   ª       feature-flags.test.js
ª   ª       FeatureFlagPanel.jsx
ª   ª       FeatureFlagSwitch.jsx
ª   ª       preview-branches.json
ª   ª       preview-cleanup.js
ª   ª       preview-config.json
ª   ª       preview-demo-data.json
ª   ª       preview-deploy-hook.js
ª   ª       preview-env.js
ª   ª       preview-metadata.json
ª   ª       preview-status.json
ª   ª       preview-stories.md
ª   ª       preview.test.js
ª   ª       previewApi.js
ª   ª       PreviewBanner.jsx
ª   ª       PreviewChangelogModal.jsx
ª   ª       previewDeployHooks.js
ª   ª       PreviewDeploymentCard.jsx
ª   ª       previewDevPanel.jsx
ª   ª       PreviewPanel.jsx
ª   ª       PreviewReviewActions.jsx
ª   ª       PreviewStatusBar.jsx
ª   ª       PreviewToggleButton.jsx
ª   ª       previewUtils.js
ª   ª       README.md
ª   ª       useFeatureFlags.js
ª   ª       usePreviewStatus.js
ª   ª       webhook-handler.js
ª   ª       
ª   +---public
ª   ª   ª   .htaccess
ª   ª   ª   android-chrome-192x192.png
ª   ª   ª   android-chrome-512x512.png
ª   ª   ª   apple-touch-icon.png
ª   ª   ª   browserconfig.xml
ª   ª   ª   CHANGELOG.md
ª   ª   ª   empty-state.svg
ª   ª   ª   error-illustration.svg
ª   ª   ª   favicon-16x16.png
ª   ª   ª   favicon-32x32.png
ª   ª   ª   favicon.ico
ª   ª   ª   humans.txt
ª   ª   ª   loading-spinner.svg
ª   ª   ª   logo-dark.svg
ª   ª   ª   logo-light.svg
ª   ª   ª   logo-small.png
ª   ª   ª   logo-square.png
ª   ª   ª   logo.svg
ª   ª   ª   manifest.json
ª   ª   ª   manifest.webmanifest
ª   ª   ª   mstile-150x150.png
ª   ª   ª   og-image.png
ª   ª   ª   placeholder.png
ª   ª   ª   preview-banner.svg
ª   ª   ª   privacy-badge.svg
ª   ª   ª   README.md
ª   ª   ª   robots.txt
ª   ª   ª   safari-pinned-tab.svg
ª   ª   ª   security-badge.svg
ª   ª   ª   site.webmanifest
ª   ª   ª   sitemap.xml
ª   ª   ª   social-preview.jpg
ª   ª   ª   tailwind.css
ª   ª   ª   theme.css
ª   ª   ª   twitter-card.png
ª   ª   ª   
ª   ª   +---backgrounds
ª   ª   ª       dark-bg.png
ª   ª   ª       dashboard-bg.svg
ª   ª   ª       landing-bg.jpg
ª   ª   ª       light-bg.png
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---banners
ª   ª   ª       beta-banner.svg
ª   ª   ª       incident-banner.svg
ª   ª   ª       promo-banner.png
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---brand
ª   ª   ª       alt-logo.svg
ª   ª   ª       full-logo.svg
ª   ª   ª       icon.svg
ª   ª   ª       README.md
ª   ª   ª       wordmark.svg
ª   ª   ª       
ª   ª   +---downloads
ª   ª   ª       apex-protocol-whitepaper.pdf
ª   ª   ª       quickstart.pdf
ª   ª   ª       README.md
ª   ª   ª       terms-and-conditions.pdf
ª   ª   ª       user-guide.pdf
ª   ª   ª       
ª   ª   +---fonts
ª   ª   ª       custom-icons.ttf
ª   ª   ª       Inter-Bold.woff2
ª   ª   ª       Inter-Regular.woff2
ª   ª   ª       README.md
ª   ª   ª       RobotoMono-Regular.woff2
ª   ª   ª       
ª   ª   +---icons
ª   ª   ª       ai-bot.png
ª   ª   ª       ai.svg
ª   ª   ª       alert.svg
ª   ª   ª       arb.svg
ª   ª   ª       dark-mode.svg
ª   ª   ª       gas.svg
ª   ª   ª       latency.svg
ª   ª   ª       operator.svg
ª   ª   ª       plugin.svg
ª   ª   ª       README.md
ª   ª   ª       settings.svg
ª   ª   ª       user.svg
ª   ª   ª       wallet.svg
ª   ª   ª       
ª   ª   +---onboarding
ª   ª           ai-demo.svg
ª   ª           operator.svg
ª   ª           README.md
ª   ª           step1.svg
ª   ª           step2.svg
ª   ª           success.svg
ª   ª           
ª   +---sandbox
ª   ª   ª   AIOpsPlayground.jsx
ª   ª   ª   AISandbox.jsx
ª   ª   ª   CHANGELOG.md
ª   ª   ª   DataVizLab.jsx
ª   ª   ª   demo-examples.md
ª   ª   ª   ExtensionPlayground.jsx
ª   ª   ª   IntegrationTestPanel.jsx
ª   ª   ª   LayoutPlayground.jsx
ª   ª   ª   OperatorTestPanel.jsx
ª   ª   ª   OverlaySandbox.jsx
ª   ª   ª   patterns.md
ª   ª   ª   README.md
ª   ª   ª   sandbox-best-practices.md
ª   ª   ª   sandbox.test.js
ª   ª   ª   sandboxApi.js
ª   ª   ª   SandboxHome.jsx
ª   ª   ª   sandboxHotReload.js
ª   ª   ª   sandboxState.js
ª   ª   ª   sandboxUtils.js
ª   ª   ª   StorybookPanel.jsx
ª   ª   ª   ThemeSandbox.jsx
ª   ª   ª   WidgetPlayground.jsx
ª   ª   ª   
ª   ª   +---demo-patterns
ª   ª   ª       ai-prompt-lab-demo.jsx
ª   ª   ª       data-viz-demo.jsx
ª   ª   ª       multi-widget-demo.jsx
ª   ª   ª       operator-alert-demo.jsx
ª   ª   ª       overlay-motion-demo.jsx
ª   ª   ª       README.md
ª   ª   ª       sandbox-patterns.md
ª   ª   ª       
ª   ª   +---presets
ª   ª           ai-demo-preset.json
ª   ª           README.md
ª   ª           theme-preset.json
ª   ª           widget-preset.json
ª   ª           
ª   +---scripts
ª   ª       README.md
ª   ª       
ª   +---settings
ª   ª       README.md
ª   ª       
ª   +---src
ª   ª       README.md
ª   ª       
ª   +---state
ª   ª   ª   aiState.js
ª   ª   ª   analyticsState.js
ª   ª   ª   CHANGELOG.md
ª   ª   ª   contextBridge.js
ª   ª   ª   devtools.js
ª   ª   ª   edgeState.js
ª   ª   ª   layoutState.js
ª   ª   ª   middleware.js
ª   ª   ª   notificationsState.js
ª   ª   ª   operatorState.js
ª   ª   ª   overlayState.js
ª   ª   ª   patterns.md
ª   ª   ª   persistStore.js
ª   ª   ª   pluginState.js
ª   ª   ª   presetsState.js
ª   ª   ª   README.md
ª   ª   ª   riskState.js
ª   ª   ª   selectors.js
ª   ª   ª   snapshotUtils.js
ª   ª   ª   ssrState.js
ª   ª   ª   state-best-practices.md
ª   ª   ª   state.test.js
ª   ª   ª   stateEvents.js
ª   ª   ª   stateHistory.js
ª   ª   ª   stateMigration.js
ª   ª   ª   stateSubscriptions.js
ª   ª   ª   stateSync.js
ª   ª   ª   stateUtils.js
ª   ª   ª   store.js
ª   ª   ª   themeState.js
ª   ª   ª   tradesState.js
ª   ª   ª   userState.js
ª   ª   ª   
ª   ª   +---demo
ª   ª           demo-state.json
ª   ª           demo-userState.js
ª   ª           README.md
ª   ª           
ª   +---stats
ª   ª       README.md
ª   ª       
ª   +---styles
ª   ª   ª   ar.css
ª   ª   ª   CHANGELOG.md
ª   ª   ª   fonts.css
ª   ª   ª   index.css
ª   ª   ª   minimal.css
ª   ª   ª   mixins.scss
ª   ª   ª   night-mode.css
ª   ª   ª   overrides.scss
ª   ª   ª   patterns.md
ª   ª   ª   print.css
ª   ª   ª   README.md
ª   ª   ª   responsive.css
ª   ª   ª   scrollbar.css
ª   ª   ª   tailwind.config.js
ª   ª   ª   tailwind.css
ª   ª   ª   theme.css
ª   ª   ª   transitions.css
ª   ª   ª   utility-classes.css
ª   ª   ª   variables.scss
ª   ª   ª   
ª   ª   +---animations
ª   ª   ª       bounce.css
ª   ª   ª       expand.css
ª   ª   ª       fade.css
ª   ª   ª       overlay.css
ª   ª   ª       README.md
ª   ª   ª       slide.css
ª   ª   ª       spinner.css
ª   ª   ª       
ª   ª   +---components
ª   ª   ª       alert.css
ª   ª   ª       avatar.css
ª   ª   ª       badge.css
ª   ª   ª       button.css
ª   ª   ª       card.css
ª   ª   ª       chart.css
ª   ª   ª       form.css
ª   ª   ª       loading.css
ª   ª   ª       menu.css
ª   ª   ª       modal.css
ª   ª   ª       README.md
ª   ª   ª       table.css
ª   ª   ª       tabs.css
ª   ª   ª       timeline.css
ª   ª   ª       tooltip.css
ª   ª   ª       widget.css
ª   ª   ª       
ª   ª   +---palette
ª   ª           accessibility.css
ª   ª           custom-tokens.css
ª   ª           dark.css
ª   ª           light.css
ª   ª           operator.css
ª   ª           README.md
ª   ª           solarized.css
ª   ª           
ª   +---testData
ª   ª       README.md
ª   ª       
ª   +---tests
ª   ª   ª   CHANGELOG.md
ª   ª   ª   patterns.md
ª   ª   ª   README.md
ª   ª   ª   test-best-practices.md
ª   ª   ª   
ª   ª   +---ai
ª   ª   ª       ai-dashboard-integration.test.py
ª   ª   ª       ai-module-smoke.test.py
ª   ª   ª       alpha-score.test.py
ª   ª   ª       profit-gradient.test.py
ª   ª   ª       README.md
ª   ª   ª       route-selection.test.py
ª   ª   ª       volatility-model.test.py
ª   ª   ª       
ª   ª   +---chaos
ª   ª   ª       incident-chaos.test.js
ª   ª   ª       node-crash-recovery.test.js
ª   ª   ª       README.md
ª   ª   ª       system-chaos.test.js
ª   ª   ª       
ª   ª   +---components
ª   ª   ª       Alert.test.jsx
ª   ª   ª       Avatar.test.jsx
ª   ª   ª       Badge.test.jsx
ª   ª   ª       Button.test.jsx
ª   ª   ª       Card.test.jsx
ª   ª   ª       Chart.test.jsx
ª   ª   ª       Form.test.jsx
ª   ª   ª       Loading.test.jsx
ª   ª   ª       Menu.test.jsx
ª   ª   ª       Modal.test.jsx
ª   ª   ª       README.md
ª   ª   ª       Table.test.jsx
ª   ª   ª       Tabs.test.jsx
ª   ª   ª       Timeline.test.jsx
ª   ª   ª       Tooltip.test.jsx
ª   ª   ª       Widget.test.jsx
ª   ª   ª       
ª   ª   +---contracts
ª   ª   ª       alpha-nft.test.js
ª   ª   ª       batch-executor.test.js
ª   ª   ª       digital-twin-bridge.test.js
ª   ª   ª       dispute-resolution.test.js
ª   ª   ª       flashloan-arbitrage.test.js
ª   ª   ª       governance-module.test.js
ª   ª   ª       insurance-pool.test.js
ª   ª   ª       intent-solver.test.js
ª   ª   ª       operator-nft.test.js
ª   ª   ª       README.md
ª   ª   ª       reputation-oracle.test.js
ª   ª   ª       upgradable-proxy.test.js
ª   ª   ª       zk-proof.test.js
ª   ª   ª       
ª   ª   +---coverage
ª   ª   ª   ª   ai-coverage.test.py
ª   ª   ª   ª   backend-coverage.test.js
ª   ª   ª   ª   contracts-coverage.test.js
ª   ª   ª   ª   coverage-report.html
ª   ª   ª   ª   coverage-summary.md
ª   ª   ª   ª   lcov.info
ª   ª   ª   ª   README.md
ª   ª   ª   ª   summary.json
ª   ª   ª   ª   
ª   ª   ª   +---.nyc_output
ª   ª   ª           README.md
ª   ª   ª           
ª   ª   +---docs
ª   ª   ª       ai-testing.md
ª   ª   ª       chaos-testing.md
ª   ª   ª       coverage-guide.md
ª   ª   ª       fork-testing.md
ª   ª   ª       legacy-cases.md
ª   ª   ª       mainnet-e2e.md
ª   ª   ª       README.md
ª   ª   ª       snapshot-methods.md
ª   ª   ª       test-strategy.md
ª   ª   ª       test-troubleshooting.md
ª   ª   ª       
ª   ª   +---e2e
ª   ª   ª       ai-e2e.test.py
ª   ª   ª       ai-panel.e2e.js
ª   ª   ª       dashboard-e2e.test.js
ª   ª   ª       failover-e2e.test.js
ª   ª   ª       live-trade.e2e.js
ª   ª   ª       mainnet-e2e.test.js
ª   ª   ª       mobile-responsive.e2e.js
ª   ª   ª       onboarding.e2e.js
ª   ª   ª       plugin-marketplace.e2e.js
ª   ª   ª       preset-switch.e2e.js
ª   ª   ª       README.md
ª   ª   ª       regression-suite.e2e.js
ª   ª   ª       theme-switch.e2e.js
ª   ª   ª       
ª   ª   +---fixtures
ª   ª   ª       example-analytics.json
ª   ª   ª       example-trades.json
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---flows
ª   ª   ª       AuthFlow.test.js
ª   ª   ª       NotificationFlow.test.js
ª   ª   ª       OperatorIncidentFlow.test.js
ª   ª   ª       PluginLifecycle.test.js
ª   ª   ª       PresetSwitchFlow.test.js
ª   ª   ª       README.md
ª   ª   ª       TradeExecFlow.test.js
ª   ª   ª       
ª   ª   +---fork
ª   ª   ª       block-drift-fork.test.js
ª   ª   ª       mainnet-fork.test.js
ª   ª   ª       mempool-chaos.test.js
ª   ª   ª       README.md
ª   ª   ª       zk-sim-fork.test.js
ª   ª   ª       
ª   ª   +---fuzz
ª   ª   ª       ai-fuzz.test.py
ª   ª   ª       fork-fuzz.test.js
ª   ª   ª       fuzz-arb-paths.test.js
ª   ª   ª       plugin-fuzz.test.js
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---integration
ª   ª   ª       ai-integration.test.py
ª   ª   ª       contracts-integration.test.js
ª   ª   ª       engine-integration.test.js
ª   ª   ª       overlays-integration.test.js
ª   ª   ª       plugins-integration.test.js
ª   ª   ª       README.md
ª   ª   ª       storage-integration.test.js
ª   ª   ª       utils-integration.test.js
ª   ª   ª       watchdog-integration.test.js
ª   ª   ª       
ª   ª   +---legacy
ª   ª   ª       legacy-tests-summary.md
ª   ª   ª       migration-checks.test.js
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---migration
ª   ª   ª       contract-migration.test.js
ª   ª   ª       db-migration.test.js
ª   ª   ª       plugin-migration.test.js
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---mocks
ª   ª   ª       mock-api.js
ª   ª   ª       mock-plugin.json
ª   ª   ª       mock-theme.json
ª   ª   ª       mock-user.json
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---pages
ª   ª   ª       AiPage.test.jsx
ª   ª   ª       IndexPage.test.jsx
ª   ª   ª       NotFoundPage.test.jsx
ª   ª   ª       OperatorPage.test.jsx
ª   ª   ª       PluginsPage.test.jsx
ª   ª   ª       README.md
ª   ª   ª       SettingsPage.test.jsx
ª   ª   ª       TradesPage.test.jsx
ª   ª   ª       
ª   ª   +---performance
ª   ª   ª       ai-latency-benchmark.test.py
ª   ª   ª       fork-benchmark.test.js
ª   ª   ª       gas-benchmark.test.js
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---plugin
ª   ª   ª       alpha-signal-plugins.test.js
ª   ª   ª       bridge-adapters.test.js
ª   ª   ª       compliance-plugins.test.js
ª   ª   ª       dex-adapters.test.js
ª   ª   ª       flashloan-adapters.test.js
ª   ª   ª       insurance-plugins.test.js
ª   ª   ª       intent-solvers.test.js
ª   ª   ª       model-marketplace.test.js
ª   ª   ª       oracles-adapters.test.js
ª   ª   ª       plugin-marketplace.test.js
ª   ª   ª       README.md
ª   ª   ª       template-plugins.test.js
ª   ª   ª       
ª   ª   +---python
ª   ª   ª       ai-agent-tests.py
ª   ª   ª       legacy-ml-tests.py
ª   ª   ª       model-integration-tests.py
ª   ª   ª       README.md
ª   ª   ª       strategy-selection-tests.py
ª   ª   ª       token-score-tests.py
ª   ª   ª       
ª   ª   +---regression
ª   ª   ª       darkmode-regression.test.js
ª   ª   ª       failed-trade-replay.test.js
ª   ª   ª       legacy-compat.test.js
ª   ª   ª       patch-regression.test.js
ª   ª   ª       README.md
ª   ª   ª       snapshot-regression.test.js
ª   ª   ª       snapshot.test.js
ª   ª   ª       upgrade-regression.test.js
ª   ª   ª       visual-regression.test.js
ª   ª   ª       
ª   ª   +---runner
ª   ª   ª       foundry.toml
ª   ª   ª       hardhat.config.js
ª   ª   ª       pytest.ini
ª   ª   ª       README.md
ª   ª   ª       test-runner.config.js
ª   ª   ª       
ª   ª   +---snapshot
ª   ª   ª       README.md
ª   ª   ª       snapshot-audit.test.js
ª   ª   ª       snapshot-compare.test.js
ª   ª   ª       
ª   ª   +---state
ª   ª   ª       aiState.test.js
ª   ª   ª       analyticsState.test.js
ª   ª   ª       edgeState.test.js
ª   ª   ª       layoutState.test.js
ª   ª   ª       notificationsState.test.js
ª   ª   ª       operatorState.test.js
ª   ª   ª       overlayState.test.js
ª   ª   ª       pluginState.test.js
ª   ª   ª       presetsState.test.js
ª   ª   ª       README.md
ª   ª   ª       riskState.test.js
ª   ª   ª       ssrState.test.js
ª   ª   ª       stateHistory.test.js
ª   ª   ª       stateUtils.test.js
ª   ª   ª       store.test.js
ª   ª   ª       themeState.test.js
ª   ª   ª       tradesState.test.js
ª   ª   ª       userState.test.js
ª   ª   ª       
ª   ª   +---unit
ª   ª   ª       ai-unit.test.py
ª   ª   ª       contracts-unit.test.js
ª   ª   ª       core-unit.test.js
ª   ª   ª       engine-unit.test.js
ª   ª   ª       overlays-unit.test.js
ª   ª   ª       plugins-unit.test.js
ª   ª   ª       README.md
ª   ª   ª       storage-unit.test.js
ª   ª   ª       utils-unit.test.js
ª   ª   ª       watchdog-unit.test.js
ª   ª   ª       
ª   ª   +---utils
ª   ª           analytics-utils.test.js
ª   ª           api-rate-limiter-utils.test.js
ª   ª           arb-throttler-utils.test.js
ª   ª           bridge-utils.test.js
ª   ª           cache-manager-utils.test.js
ª   ª           digital-twin-utils.test.js
ª   ª           error-handler-utils.test.js
ª   ª           fee-estimator-utils.test.js
ª   ª           gas-profiler-utils.test.js
ª   ª           job-queue-utils.test.js
ª   ª           key-management-utils.test.js
ª   ª           latency-profiler-utils.test.js
ª   ª           log-rotator-utils.test.js
ª   ª           migration-helper-utils.test.js
ª   ª           nonce-safety-utils.test.js
ª   ª           privacy-zk-utils.test.js
ª   ª           profit-gradient-filter-utils.test.js
ª   ª           README.md
ª   ª           sim-result-compressor.test.js
ª   ª           simulation-utils.test.js
ª   ª           social-graph-utils.test.js
ª   ª           stateful-cache-utils.test.js
ª   ª           tx-bundle-utils.test.js
ª   ª           volatility-watchdog-utils.test.js
ª   ª           
ª   +---theme
ª   ª   ª   CHANGELOG.md
ª   ª   ª   fontTokens.js
ª   ª   ª   layout.js
ª   ª   ª   radiusTokens.js
ª   ª   ª   README.md
ª   ª   ª   shadowTokens.js
ª   ª   ª   spacingTokens.js
ª   ª   ª   theme-patterns.md
ª   ª   ª   theme.test.js
ª   ª   ª   themeConfig.js
ª   ª   ª   themeHydrate.js
ª   ª   ª   themeMiddleware.js
ª   ª   ª   themeMigration.js
ª   ª   ª   themeProvider.jsx
ª   ª   ª   themeRegistry.js
ª   ª   ª   ThemeSwitcher.jsx
ª   ª   ª   themeTokens.js
ª   ª   ª   themeUtils.js
ª   ª   ª   typography.js
ª   ª   ª   useTheme.js
ª   ª   ª   
ª   ª   +---demo
ª   ª   ª       README.md
ª   ª   ª       theme-demo.js
ª   ª   ª       theme-gallery.md
ª   ª   ª       
ª   ª   +---fonts
ª   ª   ª       custom-fonts.js
ª   ª   ª       Inter.js
ª   ª   ª       README.md
ª   ª   ª       RobotoMono.js
ª   ª   ª       
ª   ª   +---palettes
ª   ª           accessibility.js
ª   ª           custom.js
ª   ª           dark.js
ª   ª           light.js
ª   ª           operator.js
ª   ª           README.md
ª   ª           solarized.js
ª   ª           
ª   +---themes
ª   ª       README.md
ª   ª       
ª   +---uploads
ª   ª       README.md
ª   ª       
ª   +---utils
ª   ª       aiUtils.js
ª   ª       analyticsUtils.js
ª   ª       animationUtils.js
ª   ª       apiUtils.js
ª   ª       arbUtils.js
ª   ª       CHANGELOG.md
ª   ª       constants.js
ª   ª       dashboardUtils.js
ª   ª       dataUtils.js
ª   ª       demoUtils.js
ª   ª       enums.js
ª   ª       errorUtils.js
ª   ª       ethUtils.js
ª   ª       formatters.js
ª   ª       hotReloadUtils.js
ª   ª       layoutUtils.js
ª   ª       logger.js
ª   ª       mevUtils.js
ª   ª       patterns.md
ª   ª       perfUtils.js
ª   ª       pluginUtils.js
ª   ª       README.md
ª   ª       sandboxUtils.js
ª   ª       storageUtils.js
ª   ª       testUtils.js
ª   ª       themeUtils.js
ª   ª       tokenUtils.js
ª   ª       typeHelpers.js
ª   ª       validators.js
ª   ª       wsUtils.js
ª   ª       
ª   +---widgets
ª   ª   ª   AIInsightWidget.jsx
ª   ª   ª   AlertBannerWidget.jsx
ª   ª   ª   ArbOpportunityWidget.jsx
ª   ª   ª   CHANGELOG.md
ª   ª   ª   ChartWidget.jsx
ª   ª   ª   CircuitBreakerWidget.jsx
ª   ª   ª   CSVPreviewWidget.jsx
ª   ª   ª   GasWidget.jsx
ª   ª   ª   HeatmapWidget.jsx
ª   ª   ª   IncidentAlertWidget.jsx
ª   ª   ª   KillSwitchWidget.jsx
ª   ª   ª   LatencyWidget.jsx
ª   ª   ª   ModelStatusWidget.jsx
ª   ª   ª   OperatorControlWidget.jsx
ª   ª   ª   OperatorStatusWidget.jsx
ª   ª   ª   PatternDetectionWidget.jsx
ª   ª   ª   patterns.md
ª   ª   ª   PnLWidget.jsx
ª   ª   ª   PresetModeWidget.jsx
ª   ª   ª   PresetUploadWidget.jsx
ª   ª   ª   README.md
ª   ª   ª   RiskWidget.jsx
ª   ª   ª   SafeModeWidget.jsx
ª   ª   ª   SnackbarWidget.jsx
ª   ª   ª   SpeedModeWidget.jsx
ª   ª   ª   StatusBadgeWidget.jsx
ª   ª   ª   SwapRouteWidget.jsx
ª   ª   ª   TimelineWidget.jsx
ª   ª   ª   TokenListWidget.jsx
ª   ª   ª   TradeStatsWidget.jsx
ª   ª   ª   UploadWidget.jsx
ª   ª   ª   WalletStatusWidget.jsx
ª   ª   ª   WatchdogWidget.jsx
ª   ª   ª   WidgetDemo.jsx
ª   ª   ª   WidgetFrame.jsx
ª   ª   ª   WidgetLoader.jsx
ª   ª   ª   widgets.test.js
ª   ª   ª   WidgetSandbox.jsx
ª   ª   ª   WidgetSettings.jsx
ª   ª   ª   WidgetTestPanel.jsx
ª   ª   ª   XAIWidget.jsx
ª   ª   ª   
ª   ª   +---ext
ª   ª   ª       CustomPartnerWidget.jsx
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---legacy
ª   ª           OldPnLWidget.jsx
ª   ª           README.md
ª   ª           
ª   +---xai
ª       ª   AttentionMap.jsx
ª       ª   CHANGELOG.md
ª       ª   ChartSaliencyOverlay.jsx
ª       ª   FeatureAttribution.jsx
ª       ª   patterns.md
ª       ª   PredictionExplanation.jsx
ª       ª   README.md
ª       ª   SaliencyMap.jsx
ª       ª   TokenInsight.jsx
ª       ª   WidgetXAIOverlay.jsx
ª       ª   xai-api.js
ª       ª   xai.test.js
ª       ª   xaiConfig.js
ª       ª   XAIDashboardOverlay.jsx
ª       ª   XAIExport.jsx
ª       ª   xaiHooks.js
ª       ª   XAIInspector.jsx
ª       ª   XAIOverlay.jsx
ª       ª   XAIStatusBar.jsx
ª       ª   xaiTokens.js
ª       ª   XAIToolbar.jsx
ª       ª   xaiUtils.js
ª       ª   
ª       +---demo
ª       ª       README.md
ª       ª       XAIOverlayDemo.md
ª       ª       XAIWidgetDemo.jsx
ª       ª       
ª       +---ext
ª               PartnerXAIWidget.jsx
ª               README.md
ª               
+---data
ª   ª   README.md
ª   ª   
ª   +---ai-feedback
ª   ª       ai-decision-trace.json
ª   ª       ai-feedback-format-history.md
ª   ª       ai-labeling-samples.json
ª   ª       ai-misclassification.csv
ª   ª       ai-model-evaluation.json
ª   ª       ai-operator-feedback.json
ª   ª       ai-review-log.json
ª   ª       README.md
ª   ª       
ª   +---analytics
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---ai-analysis
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---ai-explainer
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---anomaly
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---dashboards
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---performance
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---regression
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---timeseries
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---trade-metrics
ª   ª           README.md
ª   ª           
ª   +---audit-trails
ª   ª       asset-flows.json
ª   ª       change-log.json
ª   ª       contract-deploy.json
ª   ª       dashboard-audit.json
ª   ª       fork-event-log.json
ª   ª       login-audit.json
ª   ª       plugin-upgrade.json
ª   ª       privileged-actions.json
ª   ª       README.md
ª   ª       schema-upgrade.json
ª   ª       system-health-audit.json
ª   ª       withdrawal-log.json
ª   ª       
ª   +---backups
ª   ª   ª   backup-meta.json
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---ai-model-weights
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---compliance-snapshots
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---config-dump
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---daily
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---db-dumps
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---monthly
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---weekly
ª   ª           README.md
ª   ª           
ª   +---compliance-archive
ª   ª       aml-logs.json
ª   ª       audit-export-20250701.csv
ª   ª       compliance-events.json
ª   ª       compliance-versioning.json
ª   ª       data-retention.log
ª   ª       gdpr-requests.json
ª   ª       jurisdiction-events.json
ª   ª       kyc-logs.json
ª   ª       README.md
ª   ª       regulatory-changelog.json
ª   ª       sanctions-checks.json
ª   ª       
ª   +---export
ª   ª       ai-feedback-export.csv
ª   ª       all-in-one-export.zip
ª   ª       analytics-export.csv
ª   ª       audit-trail-export.csv
ª   ª       compliance-export.csv
ª   ª       forensics-export.csv
ª   ª       full-db-export.zip
ª   ª       model-weights-export.csv
ª   ª       operator-export.csv
ª   ª       README.md
ª   ª       regulatory-export.csv
ª   ª       simulation-export.csv
ª   ª       trade-history.csv
ª   ª       
ª   +---forensics
ª   ª       chain-events.json
ª   ª       contract-events.json
ª   ª       exploit-detections.json
ª   ª       failed-tx.json
ª   ª       fork-drift.json
ª   ª       fraud-alerts.json
ª   ª       frontrun-attempts.json
ª   ª       mempool-capture.json
ª   ª       operator-forensics-notes.md
ª   ª       orphan-blocks.json
ª   ª       README.md
ª   ª       reorg-events.json
ª   ª       snapshot-audit.json
ª   ª       trace-report.json
ª   ª       
ª   +---logs
ª   ª   ª   ai-inference.log
ª   ª   ª   alerts.log
ª   ª   ª   audit.log
ª   ª   ª   backend.log
ª   ª   ª   compliance.log
ª   ª   ª   dashboard.log
ª   ª   ª   error.log
ª   ª   ª   fork-sim.log
ª   ª   ª   notification.log
ª   ª   ª   operator.log
ª   ª   ª   perf-debug.log
ª   ª   ª   plugin.log
ª   ª   ª   README.md
ª   ª   ª   request.log
ª   ª   ª   session.log
ª   ª   ª   slow-query.log
ª   ª   ª   sql-query.log
ª   ª   ª   trades.log
ª   ª   ª   upgrades.log
ª   ª   ª   user-action.log
ª   ª   ª   webhook.log
ª   ª   ª   
ª   ª   +---legacy
ª   ª           dataset-format-history.md
ª   ª           deprecated-benchmarks.csv
ª   ª           legacy-format-spec.md
ª   ª           log-format-history.md
ª   ª           old-backend.log
ª   ª           old-operator.log
ª   ª           old-synthetic-dataset.csv
ª   ª           old-trade.log
ª   ª           README.md
ª   ª           
ª   +---model-weights
ª   ª   ª   hashes.json
ª   ª   ª   README.md
ª   ª   ª   weights-metadata.json
ª   ª   ª   
ª   ª   +---archive
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---current
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---staging
ª   ª           README.md
ª   ª           
ª   +---operator
ª   ª       device-fingerprints.json
ª   ª       escalation-records.json
ª   ª       incidents.csv
ª   ª       operator-feedback.json
ª   ª       permission-changes.log
ª   ª       profile.json
ª   ª       README.md
ª   ª       session-history.csv
ª   ª       shift-roster.json
ª   ª       
ª   +---overlays
ª   ª       ar-xai-events.json
ª   ª       incident-overlays.json
ª   ª       legacy-overlays.json
ª   ª       overlays-session-log.json
ª   ª       README.md
ª   ª       
ª   +---simulation-results
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---ai-batch
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---mainnet-fork
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---regression
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---scenarios
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---shadow-fork
ª   ª           README.md
ª   ª           
ª   +---simulation-snapshots
ª   ª       ai-sim-snapshot-20250701.json
ª   ª       README.md
ª   ª       snapshot-20250701.json
ª   ª       snapshot-20250715.json
ª   ª       snapshot-20250730.json
ª   ª       state-format-history.md
ª   ª       
ª   +---synthetic-datasets
ª       ª   ai-benchmark-set.csv
ª       ª   dataset-log.json
ª       ª   demo-ml-sim.csv
ª       ª   fake-liquidity-pools.json
ª       ª   fork-events.csv
ª       ª   README.md
ª       ª   sandwich-attacks.csv
ª       ª   synthetic-arb.csv
ª       ª   synthetic-prices.csv
ª       ª   test-scenarios.json
ª       ª   
ª       +---legacy
ª               dataset-format-history.md
ª               deprecated-benchmarks.csv
ª               old-synthetic-dataset.csv
ª               README.md
ª               
+---deploy
ª   ª   CHANGELOG.md
ª   ª   patterns.md
ª   ª   README.md
ª   ª   
ª   +---ansible
ª   ª   ª   inventory.ini
ª   ª   ª   playbook.yml
ª   ª   ª   README.md
ª   ª   ª   secrets.yml
ª   ª   ª   
ª   ª   +---group_vars
ª   ª   ª       all.yml
ª   ª   ª       prod.yml
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---roles
ª   ª   ª   ª   README.md
ª   ª   ª   ª   
ª   ª   ª   +---ai-modules
ª   ª   ª   ª       README.md
ª   ª   ª   ª       
ª   ª   ª   +---backend
ª   ª   ª   ª       README.md
ª   ª   ª   ª       
ª   ª   ª   +---dashboard
ª   ª   ª   ª       README.md
ª   ª   ª   ª       
ª   ª   ª   +---operator
ª   ª   ª           README.md
ª   ª   ª           
ª   ª   +---scripts
ª   ª           README.md
ª   ª           run-all.sh
ª   ª           
ª   +---audit
ª   ª       audit-checklist.md
ª   ª       cloud-posture.md
ª   ª       deploy-logs.md
ª   ª       README.md
ª   ª       
ª   +---docker
ª   ª       ai-modules.Dockerfile
ª   ª       backend.Dockerfile
ª   ª       base.Dockerfile
ª   ª       dashboard.Dockerfile
ª   ª       operator.Dockerfile
ª   ª       README.md
ª   ª       
ª   +---docker-compose
ª   ª       docker-compose.dev.yml
ª   ª       docker-compose.override.yml
ª   ª       docker-compose.prod.yml
ª   ª       docker-compose.yml
ª   ª       README.md
ª   ª       
ª   +---environments
ª   ª       dev.env
ª   ª       env.example
ª   ª       local.env
ª   ª       mainnet-fork.env
ª   ª       preview.env
ª   ª       prod.env
ª   ª       README.md
ª   ª       staging.env
ª   ª       testnet.env
ª   ª       vault.env
ª   ª       
ª   +---helm
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---apex-protocol
ª   ª       ª   Chart.yaml
ª   ª       ª   NOTES.txt
ª   ª       ª   README.md
ª   ª       ª   values.yaml
ª   ª       ª   
ª   ª       +---templates
ª   ª               configmap.yaml
ª   ª               deployment.yaml
ª   ª               hpa.yaml
ª   ª               ingress.yaml
ª   ª               README.md
ª   ª               secrets.yaml
ª   ª               service.yaml
ª   ª               
ª   +---kubernetes
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---base
ª   ª   ª       ai-modules-deployment.yaml
ª   ª   ª       backend-deployment.yaml
ª   ª   ª       configmap.yaml
ª   ª   ª       dashboard-deployment.yaml
ª   ª   ª       ingress.yaml
ª   ª   ª       kustomization.yaml
ª   ª   ª       namespace.yaml
ª   ª   ª       operator-deployment.yaml
ª   ª   ª       README.md
ª   ª   ª       secrets.yaml
ª   ª   ª       service.yaml
ª   ª   ª       storage.yaml
ª   ª   ª       
ª   ª   +---overlays
ª   ª       ª   README.md
ª   ª       ª   
ª   ª       +---dev
ª   ª       ª       kustomization.yaml
ª   ª       ª       README.md
ª   ª       ª       
ª   ª       +---local
ª   ª       ª       kustomization.yaml
ª   ª       ª       README.md
ª   ª       ª       
ª   ª       +---prod
ª   ª       ª       kustomization.yaml
ª   ª       ª       README.md
ª   ª       ª       
ª   ª       +---scripts
ª   ª       ª       cleanup.sh
ª   ª       ª       deploy.sh
ª   ª       ª       README.md
ª   ª       ª       
ª   ª       +---staging
ª   ª       ª       kustomization.yaml
ª   ª       ª       README.md
ª   ª       ª       
ª   ª       +---testnet
ª   ª               kustomization.yaml
ª   ª               README.md
ª   ª               
ª   +---migration
ª   ª       001-init.sql
ª   ª       README.md
ª   ª       
ª   +---scripts
ª   ª       backup-db.sh
ª   ª       deploy-all.sh
ª   ª       healthcheck.sh
ª   ª       logs.sh
ª   ª       README.md
ª   ª       restore-db.sh
ª   ª       update-all.sh
ª   ª       
ª   +---secrets
ª   ª       dev.secrets.enc
ª   ª       example.secrets.yaml
ª   ª       prod.secrets.enc
ª   ª       README.md
ª   ª       
ª   +---terraform
ª       ª   main.tf
ª       ª   outputs.tf
ª       ª   provider.tf
ª       ª   README.md
ª       ª   secrets.auto.tfvars
ª       ª   variables.tf
ª       ª   versions.tf
ª       ª   
ª       +---modules
ª       ª   ª   README.md
ª       ª   ª   
ª       ª   +---db
ª       ª   ª       README.md
ª       ª   ª       
ª       ª   +---k8s
ª       ª   ª       README.md
ª       ª   ª       
ª       ª   +---storage
ª       ª   ª       README.md
ª       ª   ª       
ª       ª   +---vpc
ª       ª           README.md
ª       ª           
ª       +---scripts
ª               apply.sh
ª               plan.sh
ª               README.md
ª               
+---docs
ª   ª   api-reference.md
ª   ª   architecture.md
ª   ª   backend.md
ª   ª   bot.md
ª   ª   changelog.md
ª   ª   ci-cd.md
ª   ª   cli.md
ª   ª   compliance.md
ª   ª   components.md
ª   ª   contracts.md
ª   ª   contributors.md
ª   ª   dashboard.md
ª   ª   data-flow.md
ª   ª   design-system.md
ª   ª   developer-guide.md
ª   ª   engine.md
ª   ª   environment.md
ª   ª   faq.md
ª   ª   frontend.md
ª   ª   getting-started.md
ª   ª   guidebook.md
ª   ª   installation.md
ª   ª   integration.md
ª   ª   legal.md
ª   ª   operator-guide.md
ª   ª   overlays.md
ª   ª   patterns.md
ª   ª   performance.md
ª   ª   plugins.md
ª   ª   quick-reference.md
ª   ª   README.md
ª   ª   roadmap.md
ª   ª   security.md
ª   ª   simulation.md
ª   ª   storage.md
ª   ª   tests.md
ª   ª   threat-model.md
ª   ª   user-guide.md
ª   ª   wall-of-fame.md
ª   ª   whitepaper.md
ª   ª   
ª   +---adr
ª   ª       0001-foundation.md
ª   ª       0002-ai-design.md
ª   ª       0003-dashboard.md
ª   ª       0004-engine.md
ª   ª       0005-mev-protection.md
ª   ª       README.md
ª   ª       
ª   +---ai
ª   ª       architecture.md
ª   ª       finGPT.md
ª   ª       investlm.md
ª   ª       model-weights.md
ª   ª       notebooks.md
ª   ª       pattern-learner.md
ª   ª       README.md
ª   ª       roadmap.md
ª   ª       scoring.md
ª   ª       training.md
ª   ª       
ª   +---api
ª   ª       auth.md
ª   ª       endpoints.md
ª   ª       patterns.md
ª   ª       README.md
ª   ª       schemas.md
ª   ª       
ª   +---audit
ª   ª       bug-bounty.md
ª   ª       compliance-checklist.md
ª   ª       pentest-report.md
ª   ª       README.md
ª   ª       security-audit.md
ª   ª       
ª   +---dashboard
ª   ª       onboarding.md
ª   ª       overlays.md
ª   ª       pages.md
ª   ª       plugins.md
ª   ª       README.md
ª   ª       state.md
ª   ª       theme.md
ª   ª       utils.md
ª   ª       widgets.md
ª   ª       
ª   +---legal
ª   ª       compliance.md
ª   ª       disclaimers.md
ª   ª       license.md
ª   ª       README.md
ª   ª       
ª   +---onboarding
ª   ª       auditor-onboarding.md
ª   ª       dev-onboarding.md
ª   ª       faq.md
ª   ª       operator-onboarding.md
ª   ª       README.md
ª   ª       
ª   +---patterns
ª           anti-patterns.md
ª           api-patterns.md
ª           code-patterns.md
ª           dashboard-patterns.md
ª           devops-patterns.md
ª           infra-patterns.md
ª           operator-patterns.md
ª           README.md
ª           
+---examples
ª   ª   cli-examples.txt
ª   ª   cli-usage.md
ª   ª   dashboard-examples.md
ª   ª   mainnet-fork-sim.md
ª   ª   README.md
ª   ª   testnet-sim.md
ª   ª   
ª   +---ai-examples
ª   ª       finGPT-demo.ipynb
ª   ª       investlm-demo.ipynb
ª   ª       pattern-learner-demo.ipynb
ª   ª       README.md
ª   ª       trade-ai-demo.csv
ª   ª       
ª   +---audit-qa
ª   ª       audit-checklist-demo.md
ª   ª       README.md
ª   ª       simulated-bug-report.md
ª   ª       
ª   +---configs
ª   ª       ai-module-config.json
ª   ª       ci-example-config.json
ª   ª       dashboard-preset.json
ª   ª       local-arb-config.json
ª   ª       mainnet-arb-config.json
ª   ª       README.md
ª   ª       testnet-arb-config.json
ª   ª       
ª   +---dashboard-screenshots
ª   ª       ai-insight-widget.png
ª   ª       dashboard-ar-overlay.png
ª   ª       dashboard-home.png
ª   ª       dashboard-settings.png
ª   ª       dashboard-trades.png
ª   ª       README.md
ª   ª       
ª   +---fuzzing-examples
ª   ª       arb-fuzzing-seed.json
ª   ª       fuzz-results.log
ª   ª       README.md
ª   ª       
ª   +---onboarding
ª   ª       auditor-walkthrough.md
ª   ª       dev-walkthrough.md
ª   ª       faq.md
ª   ª       operator-walkthrough.md
ª   ª       README.md
ª   ª       
ª   +---plugin-samples
ª   ª       ai-operator-plugin.js
ª   ª       custom-arb-plugin.js
ª   ª       demo-dex-adapter.js
ª   ª       README.md
ª   ª       
ª   +---simulation-runs
ª   ª       cached-mempool-report.md
ª   ª       event-stream.log
ª   ª       profit-heatmap.csv
ª   ª       README.md
ª   ª       simulated-arb-day.json
ª   ª       trade-history-short.csv
ª   ª       
ª   +---trade-history-examples
ª           arb-winners-2025.csv
ª           README.md
ª           test-trades-2024-01.csv
ª           
+---logs
ª   ª   README.md
ª   ª   
ª   +---ai-logs
ª   ª       ai-inference.log
ª   ª       ai-scoring.log
ª   ª       ai-training.log
ª   ª       model-updates.log
ª   ª       README.md
ª   ª       
ª   +---analytics-logs
ª   ª       market-analysis.log
ª   ª       profit-loss-report.log
ª   ª       README.md
ª   ª       trade-performance.log
ª   ª       
ª   +---application
ª   ª       api-requests.log
ª   ª       app-events.log
ª   ª       error-handling.log
ª   ª       README.md
ª   ª       user-interactions.log
ª   ª       
ª   +---audit-logs
ª   ª       audit-trail.log
ª   ª       compliance-check.log
ª   ª       README.md
ª   ª       regulatory-report.log
ª   ª       
ª   +---contract-logs
ª   ª       contract-calls.log
ª   ª       contract-deployment.log
ª   ª       contract-errors.log
ª   ª       contract-updates.log
ª   ª       README.md
ª   ª       
ª   +---debug-logs
ª   ª       debug-errors.log
ª   ª       debug-event-stream.log
ª   ª       debug-requests.log
ª   ª       README.md
ª   ª       
ª   +---event-logs
ª   ª       activity-logs.log
ª   ª       process-events.log
ª   ª       README.md
ª   ª       system-events.log
ª   ª       
ª   +---performance-logs
ª   ª       cpu-usage.log
ª   ª       gas-usage.log
ª   ª       memory-usage.log
ª   ª       network-usage.log
ª   ª       README.md
ª   ª       
ª   +---security-logs
ª   ª       access-logs.log
ª   ª       breach-detection.log
ª   ª       login-attempts.log
ª   ª       permission-errors.log
ª   ª       README.md
ª   ª       
ª   +---system-logs
ª   ª       crash-reports.log
ª   ª       error-codes.log
ª   ª       README.md
ª   ª       system-diagnostics.log
ª   ª       uptime-monitor.log
ª   ª       
ª   +---transaction-logs
ª   ª       README.md
ª   ª       tx-error.log
ª   ª       tx-history.log
ª   ª       tx-performance.log
ª   ª       
ª   +---user-logs
ª           README.md
ª           user-activity.log
ª           user-error.log
ª           user-login.log
ª           
+---manifest
ª   ª   manifest.csv
ª   ª   manifest.json
ª   ª   manifest.md
ª   ª   README.md
ª   ª   tree.txt
ª   ª   
ª   +---checksums
ª   ª       integrity-report.md
ª   ª       md5sums.txt
ª   ª       README.md
ª   ª       sha256sums.txt
ª   ª       
ª   +---diffs
ª   ª       diff-latest.md
ª   ª       diff-latest.txt
ª   ª       diff-summary.csv
ª   ª       README.md
ª   ª       
ª   +---generator
ª   ª       manifest-generator.js
ª   ª       README.md
ª   ª       update-manifest.sh
ª   ª       
ª   +---inventory
ª   ª       inventory.csv
ª   ª       inventory.json
ª   ª       inventory.md
ª   ª       README.md
ª   ª       
ª   +---metadata
ª   ª       changelog-map.md
ª   ª       file-metadata.json
ª   ª       labels.yaml
ª   ª       README.md
ª   ª       repo-meta.json
ª   ª       
ª   +---stats
ª   ª       README.md
ª   ª       stats.csv
ª   ª       stats.json
ª   ª       stats.md
ª   ª       
ª   +---templates
ª   ª       inventory-template.csv
ª   ª       manifest-template.md
ª   ª       README.md
ª   ª       
ª   +---validation
ª           check-integrity.sh
ª           manifest-validator.js
ª           README.md
ª           
+---migrations
ª   ª   .keep
ª   ª   changelog.md
ª   ª   migration-history.json
ª   ª   README.md
ª   ª   
ª   +---backup
ª   ª       backup-after.sql
ª   ª       backup-before.sql
ª   ª       README.md
ª   ª       restore.sql
ª   ª       
ª   +---contract
ª   ª       001-deploy-core.js
ª   ª       002-upgrade-v1.1.js
ª   ª       003-add-arb-adapter.js
ª   ª       010-safe-mode-patch.js
ª   ª       README.md
ª   ª       
ª   +---data
ª   ª       001-seed-operators.json
ª   ª       002-demo-trades.json
ª   ª       003-legacy-import.js
ª   ª       README.md
ª   ª       
ª   +---flyway
ª   ª       flyway.conf
ª   ª       README.md
ª   ª       V1__init.sql
ª   ª       
ª   +---plugin
ª   ª       001-register-plugins.js
ª   ª       002-upgrade-plugins.js
ª   ª       README.md
ª   ª       
ª   +---prisma
ª   ª   ª   README.md
ª   ª   ª   schema.prisma
ª   ª   ª   
ª   ª   +---migrations
ª   ª           README.md
ª   ª           
ª   +---schema
ª   ª       001-init.sql
ª   ª       002-add-operator.sql
ª   ª       003-arb-session.sql
ª   ª       010-ai-events.sql
ª   ª       README.md
ª   ª       
ª   +---scripts
ª           check-status.sh
ª           migrate-dev.sh
ª           README.md
ª           revert-migrations.sh
ª           run-migrations.sh
ª           
+---overlays
ª   ª   README.md
ª   ª   
ª   +---ar
ª   ª   ª   ar.test.js
ª   ª   ª   ARConfig.js
ª   ª   ª   ARDebugPanel.jsx
ª   ª   ª   ARDevTools.jsx
ª   ª   ª   AROverlay.jsx
ª   ª   ª   ARPluginHook.jsx
ª   ª   ª   ARStatusBar.jsx
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---demo
ª   ª   ª       ARDemoScreenshots.md
ª   ª   ª       ARDemoWidget.jsx
ª   ª   ª       README.md
ª   ª   ª       
ª   ª   +---ext
ª   ª           PartnerARWidget.jsx
ª   ª           README.md
ª   ª           
ª   +---debug
ª   ª   ª   debug.test.js
ª   ª   ª   DebugConfig.js
ª   ª   ª   DebugEventStream.jsx
ª   ª   ª   DebugOverlay.jsx
ª   ª   ª   DebugTracePanel.jsx
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---demo
ª   ª           DebugDemo.md
ª   ª           README.md
ª   ª           
ª   +---experimental
ª   ª       .keep
ª   ª       ObsOverlay.jsx
ª   ª       OverlayLabs.md
ª   ª       README.md
ª   ª       
ª   +---extension
ª   ª       OverlayExtensionAPI.js
ª   ª       OverlayExtensionDemo.jsx
ª   ª       README.md
ª   ª       
ª   +---incident
ª   ª   ª   incident.test.js
ª   ª   ª   IncidentActionPanel.jsx
ª   ª   ª   IncidentBanner.jsx
ª   ª   ª   IncidentConfig.js
ª   ª   ª   IncidentOverlay.jsx
ª   ª   ª   IncidentTimeline.jsx
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---demo
ª   ª           IncidentDemo.md
ª   ª           README.md
ª   ª           
ª   +---operator
ª   ª   ª   operator.test.js
ª   ª   ª   OperatorBanner.jsx
ª   ª   ª   OperatorConfig.js
ª   ª   ª   OperatorOverlay.jsx
ª   ª   ª   OperatorProfilePanel.jsx
ª   ª   ª   OperatorQAOverlay.jsx
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---demo
ª   ª           OperatorDemo.md
ª   ª           README.md
ª   ª           
ª   +---test
ª   ª       OverlayTestSuite.js
ª   ª       README.md
ª   ª       
ª   +---xai
ª       ª   AttentionMap.jsx
ª       ª   CHANGELOG.md
ª       ª   ChartSaliencyOverlay.jsx
ª       ª   FeatureAttribution.jsx
ª       ª   patterns.md
ª       ª   PredictionExplanation.jsx
ª       ª   README.md
ª       ª   SaliencyMap.jsx
ª       ª   WidgetXAIOverlay.jsx
ª       ª   xai-api.js
ª       ª   xai.test.js
ª       ª   xaiConfig.js
ª       ª   XAIExport.jsx
ª       ª   xaiHooks.js
ª       ª   XAIInspector.jsx
ª       ª   XAIOverlay.jsx
ª       ª   XAIStatusBar.jsx
ª       ª   xaiTokens.js
ª       ª   XAIToolbar.jsx
ª       ª   xaiUtils.js
ª       ª   
ª       +---demo
ª       ª       README.md
ª       ª       XAIOverlayDemo.md
ª       ª       XAIWidgetDemo.jsx
ª       ª       
ª       +---ext
ª               PartnerXAIWidget.jsx
ª               README.md
ª               
+---presets
ª   ª   changelog.md
ª   ª   README.md
ª   ª   
ª   +---ai
ª   ª       ai-arb-demo.json
ª   ª       ai-scorer-preset.json
ª   ª       explainability-preset.json
ª   ª       finGPT-preset.json
ª   ª       investlm-preset.json
ª   ª       ml-test-preset.json
ª   ª       pattern-learner.json
ª   ª       README.md
ª   ª       
ª   +---analytics
ª   ª       daily-pnl-report.json
ª   ª       dashboard-analytics.json
ª   ª       gas-cost-analysis.json
ª   ª       README.md
ª   ª       volatility-alerts.json
ª   ª       
ª   +---dashboard
ª   ª       analytics-widgets.json
ª   ª       dark-mode.json
ª   ª       default-theme.json
ª   ª       minimal-layout.json
ª   ª       night-trader-ui.json
ª   ª       README.md
ª   ª       
ª   +---export
ª   ª       backup-2025-07-31.json
ª   ª       README.md
ª   ª       
ª   +---migration
ª   ª       migrate-preset-v1-v2.js
ª   ª       migrate-theme-v1-v2.js
ª   ª       README.md
ª   ª       
ª   +---operator
ª   ª       ai-operator-preset.json
ª   ª       alerts-ui.json
ª   ª       gas-saver.json
ª   ª       operator-safe-mode.json
ª   ª       README.md
ª   ª       reporting-preset.json
ª   ª       wallet-preset.json
ª   ª       
ª   +---quickstart
ª   ª       default-quickstart.json
ª   ª       demo-dryrun.json
ª   ª       eth-testnet.json
ª   ª       operator-quick-preset.json
ª   ª       polygon-testnet.json
ª   ª       README.md
ª   ª       
ª   +---strategies
ª   ª       aggressive-arb.json
ª   ª       fallback-arb.json
ª   ª       mev-defense.json
ª   ª       night-mode.json
ª   ª       polygon-top-dexes.json
ª   ª       README.md
ª   ª       strategy-pack-2025Q3.json
ª   ª       usdc-weth-dai.json
ª   ª       
ª   +---templates
ª   ª       ai-preset-template.json
ª   ª       dashboard-template.json
ª   ª       operator-template.json
ª   ª       preset-template.json
ª   ª       README.md
ª   ª       
ª   +---user-presets
ª           backup-user-preset-2025-07.json
ª           my-custom-arb.json
ª           my-dashboard-theme.json
ª           README.md
ª           saved-strategy-preset.json
ª           
+---public
ª   ª   asset-manifest.json
ª   ª   browserconfig.xml
ª   ª   CNAME
ª   ª   favicon.ico
ª   ª   humans.txt
ª   ª   index.html
ª   ª   manifest.webmanifest
ª   ª   README.md
ª   ª   robots.txt
ª   ª   service-worker.js
ª   ª   site.webmanifest
ª   ª   
ª   +---brand
ª   ª       banner.png
ª   ª       icon.png
ª   ª       logo-192.png
ª   ª       logo-512.png
ª   ª       logo-dark.svg
ª   ª       logo-light.svg
ª   ª       logo.svg
ª   ª       README.md
ª   ª       symbol-only.svg
ª   ª       wordmark.svg
ª   ª       
ª   +---css
ª   ª       dark-theme.css
ª   ª       light-theme.css
ª   ª       main.css
ª   ª       overrides.css
ª   ª       README.md
ª   ª       theme-vars.css
ª   ª       
ª   +---extensions
ª   ª       extension-sample-bg.jpg
ª   ª       partner1-logo.svg
ª   ª       partner2-logo.png
ª   ª       README.md
ª   ª       
ª   +---fonts
ª   ª       Inter-Bold.woff2
ª   ª       Inter-Regular.woff2
ª   ª       JetBrainsMono-Bold.woff2
ª   ª       JetBrainsMono-Regular.woff2
ª   ª       README.md
ª   ª       RobotoMono-Regular.ttf
ª   ª       
ª   +---icons
ª   ª   ª   README.md
ª   ª   ª   
ª   ª   +---badges
ª   ª   ª       ai.svg
ª   ª   ª       dev.svg
ª   ª   ª       operator.svg
ª   ª   ª       README.md
ª   ª   ª       verified.svg
ª   ª   ª       
ª   ª   +---tokens
ª   ª   ª       arb.svg
ª   ª   ª       btc.svg
ª   ª   ª       dai.svg
ª   ª   ª       link.svg
ª   ª   ª       matic.svg
ª   ª   ª       README.md
ª   ª   ª       usdc.svg
ª   ª   ª       usdt.svg
ª   ª   ª       weth.svg
ª   ª   ª       
ª   ª   +---ui
ª   ª           alert.svg
ª   ª           copy.svg
ª   ª           danger.svg
ª   ª           dashboard.svg
ª   ª           external.svg
ª   ª           info.svg
ª   ª           operator.svg
ª   ª           README.md
ª   ª           success.svg
ª   ª           wallet.svg
ª   ª           warning.svg
ª   ª           
ª   +---img
ª   ª       avatar-default.png
ª   ª       charts-sample.png
ª   ª       code-examples.png
ª   ª       dashboard-hero-dark.jpg
ª   ª       dashboard-hero.jpg
ª   ª       empty-state.svg
ª   ª       hero-bg.svg
ª   ª       mobile-ui.png
ª   ª       operators.png
ª   ª       README.md
ª   ª       trade-bg.svg
ª   ª       
ª   +---legal
ª   ª       cookies.html
ª   ª       legal-disclaimer.txt
ª   ª       privacy-policy.html
ª   ª       README.md
ª   ª       security.txt
ª   ª       terms-of-use.html
ª   ª       
ª   +---meta
ª   ª       analytics.js
ª   ª       meta-tags.html
ª   ª       og-image-dark.png
ª   ª       og-image.png
ª   ª       preview-card.png
ª   ª       README.md
ª   ª       
ª   +---static
ª   ª       api-reference.pdf
ª   ª       litepaper.pdf
ª   ª       press-kit.zip
ª   ª       README.md
ª   ª       whitepaper.pdf
ª   ª       
ª   +---svg
ª   ª       ai-insight.svg
ª   ª       dashboard-bg.svg
ª   ª       README.md
ª   ª       trade-flow.svg
ª   ª       
ª   +---themes
ª           charts.json
ª           dark.json
ª           light.json
ª           operator-night.json
ª           README.md
ª           
+---research
ª   ª   README.md
ª   ª   roadmap.md
ª   ª   
ª   +---alphaNFT
ª   ª       alpha-nft-demo-contract.sol
ª   ª       alpha-nft-protocol.md
ª   ª       alpha-nft-sim.ipynb
ª   ª       README.md
ª   ª       
ª   +---compliance
ª   ª       ai-ethics.md
ª   ª       audit-trail-research.md
ª   ª       data-privacy-research.md
ª   ª       model-bias-analysis.md
ª   ª       README.md
ª   ª       
ª   +---datasets
ª   ª       ai-arb-examples.json
ª   ª       ai-labels.json
ª   ª       arb-benchmark.csv
ª   ª       mev-prediction-data.parquet
ª   ª       operator-actions.csv
ª   ª       price-history-2025.json
ª   ª       README.md
ª   ª       synthetic-pool-dataset.csv
ª   ª       
ª   +---docs
ª   ª       ai-arb-research-whitepaper.md
ª   ª       experimental-protocols.md
ª   ª       explainable-ai-xai.md
ª   ª       literature-review-2025.md
ª   ª       README.md
ª   ª       trading-sim-whitepaper.md
ª   ª       
ª   +---experiments
ª   ª       ai-arb-strategy.ipynb
ª   ª       ai-vs-human-arb-sim.md
ª   ª       cross-chain-arb-research.ipynb
ª   ª       finetune-experiments.ipynb
ª   ª       mev-simulation.ipynb
ª   ª       optimization-benchmarks.md
ª   ª       README.md
ª   ª       stealth-execution-lab.ipynb
ª   ª       trade-pattern-learning.ipynb
ª   ª       
ª   +---innovation
ª   ª       agent-autonomy-log.md
ª   ª       experimental-ideas-2025.md
ª   ª       hackathon-2025-log.md
ª   ª       proposal-ai-xai.md
ª   ª       proposal-rust-backend.md
ª   ª       README.md
ª   ª       
ª   +---logs
ª   ª       ai-experiment-error.log
ª   ª       data-pipeline-debug.log
ª   ª       README.md
ª   ª       research-run-log-2025-07-31.txt
ª   ª       
ª   +---notebooks
ª   ª       agent-cooperation.ipynb
ª   ª       ai-risk-score.ipynb
ª   ª       alpha-nft-experiments.ipynb
ª   ª       dashboard-insight-research.ipynb
ª   ª       ml-eda-arb-dataset.ipynb
ª   ª       profit-predictor-training.ipynb
ª   ª       quantum-sim-2025.ipynb
ª   ª       README.md
ª   ª       synthetic-data-gen.ipynb
ª   ª       
ª   +---quantum
ª   ª       quantum-arb-sim.md
ª   ª       quantum-experiment.ipynb
ª   ª       quantum-safe-protocols.md
ª   ª       README.md
ª   ª       toy-qiskit-demo.py
ª   ª       
ª   +---results
ª   ª       ai-experiment-leaderboard.md
ª   ª       cross-chain-arb-results.json
ª   ª       gas-usage-benchmark.csv
ª   ª       profit-predictor-results.csv
ª   ª       README.md
ª   ª       summary-2025Q3.md
ª   ª       
ª   +---swarm
ª           collaborative-llm-training.ipynb
ª           edge-ml-agent-research.md
ª           README.md
ª           swarm-arb-sim.ipynb
ª           
+---scripts
ª   ª   backup-data.sh
ª   ª   check-status.sh
ª   ª   ci-build.sh
ª   ª   clean-logs.sh
ª   ª   deploy-contracts.js
ª   ª   fetch-external-data.js
ª   ª   generate-report.js
ª   ª   manifest-generator.js
ª   ª   migrate-dev.sh
ª   ª   monitor-prices.js
ª   ª   README.md
ª   ª   restore-data.sh
ª   ª   revert-migrations.sh
ª   ª   run-migrations.sh
ª   ª   run-simulation.js
ª   ª   simulate-arbitrage.js
ª   ª   start-bot.sh
ª   ª   testnet-deploy.js
ª   ª   update-manifest.sh
ª   ª   update-plugins.sh
ª   ª   verify-contract.js
ª   ª   wallet-balance-check.js
ª   ª   
ª   +---automation
ª   ª       clean-temp-files.sh
ª   ª       nightly-backup.sh
ª   ª       README.md
ª   ª       sync-docker-images.sh
ª   ª       
ª   +---operator
ª   ª       check-health.sh
ª   ª       log-rotation.sh
ª   ª       operator-alert.sh
ª   ª       README.md
ª   ª       
ª   +---playbook
ª   ª       emergency-shutdown.sh
ª   ª       liquidity-reset.sh
ª   ª       README.md
ª   ª       restart-bot.sh
ª   ª       
ª   +---quickstart
ª   ª       ci-build.sh
ª   ª       demo-run.sh
ª   ª       README.md
ª   ª       start-dev.sh
ª   ª       testnet-deploy.sh
ª   ª       
ª   +---setup
ª   ª       configure-env.sh
ª   ª       install-dependencies.sh
ª   ª       node-setup.sh
ª   ª       README.md
ª   ª       setup-venv.sh
ª   ª       
ª   +---tree
ª   ª       generate-tree.sh
ª   ª       README.md
ª   ª       update-manifest.sh
ª   ª       validate-manifest.sh
ª   ª       
ª   +---update
ª           README.md
ª           update-ai-models.sh
ª           update-dex-lists.sh
ª           upgrade-contracts.sh
ª           
+---storage
ª   ª   README.md
ª   ª   
ª   +---agent-snapshots
ª   ª       agent-state-2025-07-31.json
ª   ª       agent-state-2025-08-01.json
ª   ª       decision-heatmap.png
ª   ª       model-checkpoint-epoch50.bin
ª   ª       model-checkpoint-epoch75.bin
ª   ª       README.md
ª   ª       reward-curve.png
ª   ª       sim-snapshot-ai-trades-2025-07.json
ª   ª       training-metrics-2025-07.log
ª   ª       
ª   +---key-vault
ª   ª       README.md
ª   ª       recovery-instructions.md
ª   ª       vault-backup-2025-07-31.enc
ª   ª       vault-backup-2025-08-01.enc
ª   ª       vault-temp.json
ª   ª       vault.enc
ª   ª       
ª   +---secret-backups
ª   ª       api-keys-backup-2025-07.json.enc
ª   ª       config-secrets-2025-07.json.enc
ª   ª       operator-tokens.enc
ª   ª       pgp-keyring-backup.asc
ª   ª       README.md
ª   ª       rotation-log.md
ª   ª       
ª   +---strat-archives
ª   ª       arb-strat-v1-2025-07.json
ª   ª       arb-strat-v2-2025-08.json
ª   ª       fallback-strategy-v1.json
ª   ª       README.md
ª   ª       risk-profile-v2.json
ª   ª       strat-archive-2025-07-31.zip
ª   ª       strat-archive-2025-08-01.zip
ª   ª       strat-metadata.json
ª   ª       
ª   +---temp
ª           autosave-agent.tmp
ª           cache-temp.json
ª           checksum-verification.log
ª           partial-download.tmp
ª           README.md
ª           unzipped-strategy-preview.json
ª           upload-queue.json
ª           validator-temp-matrix.csv
ª           
+---tests
ª   ª   foundry.toml
ª   ª   hardhat.config.test.js
ª   ª   README.md
ª   ª   test-entrypoint.sh
ª   ª   test-runner.config.js
ª   ª   
ª   +---ai
ª   ª       README.md
ª   ª       test-agentModelOverfitting.py
ª   ª       test-aiRollUnderPredictor.py
ª   ª       test-decisionReplayValidator.py
ª   ª       test-latencyScorerModel.py
ª   ª       test-profitPredictorModel.py
ª   ª       test-simulatedTradeForecast.py
ª   ª       test-volatilityWatchdog.py
ª   ª       
ª   +---cli
ª   ª       README.md
ª   ª       test-botLaunchPrompt.js
ª   ª       test-configPresetLoad.js
ª   ª       test-hotkeyExitAndResume.js
ª   ª       test-interactiveSession.js
ª   ª       test-modeSelectorInput.js
ª   ª       
ª   +---contracts
ª   ª       arbExecutor.test.js
ª   ª       eventEmitters.test.js
ª   ª       fallbackRouterLogic.test.js
ª   ª       flashloanArb.test.js
ª   ª       proxyUpgradeFlow.test.js
ª   ª       README.md
ª   ª       strategyRegistry.test.js
ª   ª       
ª   +---coverage
ª   ª       README.md
ª   ª       
ª   +---e2e
ª   ª       README.md
ª   ª       test-botLaunchToProfit.js
ª   ª       test-botOperatorControl.js
ª   ª       test-profitWithdrawFlow.js
ª   ª       test-reentryRecoveryFlow.js
ª   ª       test-txnReversionSafeExit.js
ª   ª       
ª   +---error-snapshots
ª   ª       crash-2025-07-30.json
ª   ª       README.md
ª   ª       
ª   +---fuzz
ª   ª       fuzz-parameterLimits.sol
ª   ª       fuzz-reserveImbalance.py
ª   ª       fuzz-simulationIntegrity.js
ª   ª       fuzz-tokenSequence.py
ª   ª       fuzz-unusualPairRoutes.js
ª   ª       README.md
ª   ª       
ª   +---integration
ª   ª       README.md
ª   ª       test-aiOracleIntegration.js
ª   ª       test-alertWebhookIntegration.js
ª   ª       test-configPresetLinking.js
ª   ª       test-dashboardToEngine.js
ª   ª       test-dexArbFlow.js
ª   ª       test-eventSyncBus.js
ª   ª       
ª   +---mocks
ª   ª       mockBlockState.json
ª   ª       mockDEXPair.json
ª   ª       mockExecutionLogs.json
ª   ª       mockOracle.js
ª   ª       mockRouterResponse.json
ª   ª       mockTokenList.json
ª   ª       mockWalletConfig.json
ª   ª       README.md
ª   ª       
ª   +---regression
ª   ª       README.md
ª   ª       regression-dexDesyncBug.test.js
ª   ª       regression-outdatedOracleSkip.test.js
ª   ª       regression-pendingTxCrash.test.js
ª   ª       regression-simulationMismatch.test.js
ª   ª       regression-slippageCapFailure.test.js
ª   ª       regression-txRevertHistory.test.js
ª   ª       
ª   +---reports
ª   ª       lint-and-test-status.json
ª   ª       model-accuracy-report-2025-07.csv
ª   ª       README.md
ª   ª       test-coverage-summary.html
ª   ª       test-report-2025-07.xml
ª   ª       
ª   +---snapshot
ª   ª       data-snapshot-compare.test.py
ª   ª       profitSnapshotChecker.js
ª   ª       README.md
ª   ª       snapshotConsistencyChecker.js
ª   ª       snapshotTrainerStability.test.py
ª   ª       state-snapshot-restore.test.js
ª   ª       
ª   +---snapshots
ª   ª       arb-engine-snapshot.json
ª   ª       model-replay-checkpoint-75.json
ª   ª       README.md
ª   ª       
ª   +---unit
ª   ª       README.md
ª   ª       test-arbEngine.spec.js
ª   ª       test-gasOptimizer.spec.js
ª   ª       test-priceFetchCache.spec.js
ª   ª       test-profitCalc.spec.js
ª   ª       test-routerAdapter.spec.js
ª   ª       test-slippageController.spec.js
ª   ª       test-tokenReputation.spec.js
ª   ª       test-utils.spec.js
ª   ª       test-watchdogTrigger.spec.js
ª   ª       
ª   +---watchdog
ª           README.md
ª           test-autoRestartLoop.js
ª           test-circuitBreakerTrip.js
ª           test-highGasSpikeRejection.js
ª           test-liquidityFailoverRoute.js
ª           test-spikeDetection.js
ª           
+---third-party
ª   ª   README.md
ª   ª   
ª   +---adapters
ª   ª       betswirl-dice-adapter.ts
ª   ª       oneinch-split-router.ts
ª   ª       paraswap-router-integration.js
ª   ª       README.md
ª   ª       stargate-liquidity-bridge.ts
ª   ª       velodrome-v2-adapter.ts
ª   ª       zksync-router-mock.ts
ª   ª       
ª   +---bots
ª   ª       archer-relay-sim.js
ª   ª       bloxroute-tx-broadcaster.js
ª   ª       flashbots-tx-bundler.js
ª   ª       jito-relay-adapter.ts
ª   ª       README.md
ª   ª       starknet-bridge-simulator.js
ª   ª       
ª   +---compliance-hooks
ª   ª       audit-log-exporter.js
ª   ª       chainalysis-screening.ts
ª   ª       compliance-cache.json
ª   ª       README.md
ª   ª       safe-blocklist-fetcher.js
ª   ª       trmlabs-sanctions-check.js
ª   ª       
ª   +---connectors
ª   ª       balancer-v2-connector.js
ª   ª       camelot-arbitrum.js
ª   ª       kyber-dmm-connector.js
ª   ª       quickswap-connector.js
ª   ª       README.md
ª   ª       sushiswap-v2-connector.js
ª   ª       uniswap-v3-connector.js
ª   ª       
ª   +---oracles
ª   ª       chainlink-aggregator.ts
ª   ª       custom-infra-oracle.js
ª   ª       dia-oracle-wrapper.py
ª   ª       oracle-quorum-engine.ts
ª   ª       oracle-validator-utils.js
ª   ª       README.md
ª   ª       redstone-adapter.js
ª   ª       
ª   +---patches
ª   ª       aave-pool-interface-patch.sol
ª   ª       deploy-skip-check.patch.js
ª   ª       flashbots-bundler-override.js
ª   ª       patched-ethers-provider.ts
ª   ª       README.md
ª   ª       redstone-feed-fix.ts
ª   ª       
ª   +---schemas
ª   ª       ai-scorer-output-schema.json
ª   ª       dex-liquidity-pool-schema.json
ª   ª       dex-route-schema.json
ª   ª       flashloan-request-schema.json
ª   ª       mev-strategy-spec.json
ª   ª       oracle-feed-schema.json
ª   ª       README.md
ª   ª       token-schema.json
ª   ª       
ª   +---sdk
ª           aave-v3-sdk.js
ª           bloxroute-sdk-wrapper.js
ª           chainlink-price-feed-sdk.js
ª           ethers-ext.js
ª           flashbots-provider.js
ª           polygon-zkevm-sdk.ts
ª           README.md
ª           
+---types
ª   ª   README.md
ª   ª   
ª   +---abi
ª   ª       ArbitrageExecutor.json
ª   ª       ERC20.json
ª   ª       FlashLoanArbitrage.json
ª   ª       OracleRegistry.json
ª   ª       README.md
ª   ª       TokenVault.json
ª   ª       UpgradeableBeacon.json
ª   ª       
ª   +---json
ª   ª       ai-score-example.json
ª   ª       default-config-template.json
ª   ª       flashloan-example.json
ª   ª       README.md
ª   ª       route-cache-template.json
ª   ª       test-oracle-response.json
ª   ª       watchdog-trigger-template.json
ª   ª       
ª   +---py
ª   ª       ai_prediction.py
ª   ª       arb_model.py
ª   ª       config_loader.py
ª   ª       flashloan_struct.py
ª   ª       oracle_feed.py
ª   ª       README.md
ª   ª       schema_validator.py
ª   ª       
ª   +---schema
ª   ª       ai-prediction.schema.json
ª   ª       dashboard-settings.schema.json
ª   ª       dex-route.schema.json
ª   ª       execution-report.schema.json
ª   ª       flashloan-request.schema.json
ª   ª       README.md
ª   ª       token.schema.json
ª   ª       
ª   +---ts
ª   ª       ai.types.ts
ª   ª       arb.types.ts
ª   ª       bridge.types.ts
ª   ª       config.types.ts
ª   ª       dashboard.types.ts
ª   ª       dex.types.ts
ª   ª       error.types.ts
ª   ª       flashloan.types.ts
ª   ª       oracle.types.ts
ª   ª       README.md
ª   ª       watchdog.types.ts
ª   ª       
ª   +---utils
ª           abi-type-parser.ts
ª           doc-generator.ts
ª           interface-mapper.ts
ª           normalize-types.ts
ª           README.md
ª           schema-validator.ts
ª           ts-to-jsonschema.js
ª           
+---utils
ª   ª   README.md
ª   ª   
ª   +---converter
ª   ª       abiToSchema.js
ª   ª       jsonSchemaToTypes.js
ª   ª       jsonToAbi.js
ª   ª       README.md
ª   ª       tsToJsonSchema.js
ª   ª       
ª   +---devtools
ª   ª       dependencyChecker.js
ª   ª       fileTreePrinter.js
ª   ª       hotReloader.js
ª   ª       presetLoader.js
ª   ª       README.md
ª   ª       testSeedGenerator.js
ª   ª       
ª   +---formatter
ª   ª       executionSummaryPrinter.js
ª   ª       percentFormatter.js
ª   ª       README.md
ª   ª       timeFormatter.js
ª   ª       usdFormatter.js
ª   ª       
ª   +---gas
ª   ª       gasBoostPlanner.js
ª   ª       gasCostCalculator.js
ª   ª       gasEstimator.js
ª   ª       gasProfiler.js
ª   ª       mevBoostFeeScanner.js
ª   ª       README.md
ª   ª       smartGasPredictor.js
ª   ª       
ª   +---helpers
ª   ª       asyncQueue.js
ª   ª       deepClone.js
ª   ª       delay.js
ª   ª       flattenNestedJson.js
ª   ª       README.md
ª   ª       retryWithBackoff.js
ª   ª       throttle.js
ª   ª       
ª   +---logs
ª   ª       errorReporter.js
ª   ª       logFormatter.js
ª   ª       logParser.js
ª   ª       logReplayLoader.js
ª   ª       logToSQLite.js
ª   ª       README.md
ª   ª       
ª   +---math
ª   ª       arbProfitMargin.js
ª   ª       bnMath.js
ª   ª       pnlCalculator.js
ª   ª       README.md
ª   ª       safeDivision.js
ª   ª       slippageCalc.js
ª   ª       
ª   +---parser
ª   ª       abiDecoder.js
ª   ª       bytecodeAnalyzer.js
ª   ª       calldataCompressor.js
ª   ª       README.md
ª   ª       txTraceParser.js
ª   ª       
ª   +---sim
ª   ª       forkBlockFetcher.js
ª   ª       priceDeltaChecker.js
ª   ª       README.md
ª   ª       reserveImbalanceDetector.js
ª   ª       simRouteValidator.js
ª   ª       simSnapSaver.js
ª   ª       slippageGuard.js
ª   ª       
ª   +---validator
ª   ª       chainHealthChecker.js
ª   ª       configSanityChecker.js
ª   ª       envVarChecker.js
ª   ª       README.md
ª   ª       routeSanityValidator.js
ª   ª       
ª   +---watchers
ª           errorSpikeWatcher.js
ª           liquidityWatcher.js
ª           mempoolWatcher.js
ª           priceDriftWatcher.js
ª           README.md
ª           
+---vendor
ª   ª   README.md
ª   ª   
ª   +---abi
ª   ª       aaveV3LendingPool.json
ª   ª       arbExecutor.json
ª   ª       balancerVault.json
ª   ª       chainlinkAggregator.json
ª   ª       flashloanArbitrage.json
ª   ª       quickswapRouter.json
ª   ª       README.md
ª   ª       uniswapV2Router.json
ª   ª       uniswapV3Pool.json
ª   ª       
ª   +---binaries
ª   ª       abi-parser.wasm
ª   ª       bytecode-sigtool.wasm
ª   ª       graph-cli.wasm
ª   ª       mev-trace-analyzer.exe
ª   ª       README.md
ª   ª       sqlite3.dll
ª   ª       sqlite3.so
ª   ª       
ª   +---contracts
ª   ª       AaveV3PoolInterface.sol
ª   ª       BalancerVaultInterface.sol
ª   ª       FlashLoanReceiverBase.sol
ª   ª       IERC20.sol
ª   ª       README.md
ª   ª       SafeERC20.sol
ª   ª       SafeMath.sol
ª   ª       UniswapV2Library.sol
ª   ª       UniV3TickMath.sol
ª   ª       
ª   +---datasets
ª   ª       aave-historical-flashloan.csv
ª   ª       chainlink-oracle-history.json
ª   ª       mev-inspector-dataset.json
ª   ª       profit-patterns.csv
ª   ª       README.md
ª   ª       
ª   +---dex-liquidity-snapshots
ª   ª       2025-07-27.json
ª   ª       2025-07-28.json
ª   ª       2025-07-29.json
ª   ª       latest.json
ª   ª       README.md
ª   ª       
ª   +---libs
ª   ª       ajv.bundle.js
ª   ª       ethers-v5.js
ª   ª       lodash.min.js
ª   ª       merkle-tools.min.js
ª   ª       moment-timezone.js
ª   ª       multicall.js
ª   ª       README.md
ª   ª       
ª   +---patches
ª   ª       aave-interface-fix.sol
ª   ª       ethers-provider-patch.js
ª   ª       jsonrpc-batch-fix.js
ª   ª       node-fetch-esm-patch.js
ª   ª       README.md
ª   ª       redstone-deviation-fix.js
ª   ª       
ª   +---scripts
ª           export-datasets.py
ª           fetch-mev-patterns.py
ª           freeze-deps.sh
ª           integrity-hash-check.sh
ª           README.md
ª           update-abi-cache.js
ª           
+---wall-of-fame
ª   ª   CONTRIBUTORS.md
ª   ª   README.md
ª   ª   
ª   +---badges
ª   ª       bug-slayer-badge.svg
ª   ª       docs-champion-badge.svg
ª   ª       early-contributor-badge.svg
ª   ª       innovation-badge.svg
ª   ª       mentor-badge.svg
ª   ª       qa-defender-badge.svg
ª   ª       README.md
ª   ª       reviewer-badge.svg
ª   ª       top-committer-badge.svg
ª   ª       
ª   +---recognition-events
ª   ª       awards-ceremony-2025.md
ª   ª       community-celebration-2025.md
ª   ª       contributor-appreciation-day-2025.md
ª   ª       github-recognition-week.md
ª   ª       README.md
ª   ª       team-retreat-hackathon.md
ª   ª       
ª   +---recognitions
ª   ª       ai-contribution-award.md
ª   ª       excellence-in-innovation.md
ª   ª       leadership-award.md
ª   ª       open-source-evangelist.md
ª   ª       outstanding-community-service.md
ª   ª       README.md
ª   ª       
ª   +---testimonials
ª           ai-lead-reflection.md
ª           alice-jones-testimonial.md
ª           dev-ops-intern-testimonial.md
ª           jane-smith-testimonial.md
ª           john-doe-testimonial.md
ª           README.md
ª           
+---watchdog
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
        
