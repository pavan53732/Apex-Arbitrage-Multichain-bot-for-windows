# Strategies

## Purpose
This document is the authoritative specification for every supported trading strategy and their implementation behavior.

## Strategy contract
Each strategy must define business objective, decision logic, market conditions, entry and exit criteria, sizing, allocation, risk, slippage, gas, MEV, chain/DEX support, market data dependencies, AI interaction, runtime flow, state machine, IPC events, persistence, monitoring, alerting, backtesting, simulation, stress testing, failure handling, recovery, performance metrics, limitations, and extension points.

## Shared lifecycle
Discover -> Score -> Validate -> Size -> Approve -> Execute -> Monitor -> Exit -> Reconcile -> Learn.

## Common strategy requirements
These requirements apply to every strategy below.
- Business objective and overview.
- Decision logic or model.
- Required market conditions.
- Entry and exit conditions.
- Position sizing and capital allocation.
- Risk controls, stop-loss, and take-profit.
- Volatility, liquidity, slippage, gas, and MEV policy.
- Supported chains, DEXs, and market data.
- AI interaction rules.
- Runtime workflow and state machine.
- IPC and persistence requirements.
- Monitoring, alerting, backtesting, simulation, and failure handling.
- Known limitations and extension points.

## Strategy template
### Business objective
### Strategy overview
### Decision logic
### Required market conditions
### Entry conditions
### Exit conditions
### Position sizing methodology
### Capital allocation rules
### Risk controls
### Stop-loss logic
### Take-profit logic
### Volatility handling
### Liquidity requirements
### Slippage tolerance
### Gas optimisation rules
### MEV considerations
### Supported chains
### Supported DEXs
### Required market data
### AI interaction
### Runtime workflow
### State machine
### IPC interactions
### Database persistence
### Monitoring metrics
### Alert thresholds
### Backtesting methodology
### Simulation scenarios
### Stress testing
### Performance metrics
### Failure scenarios
### Recovery behaviour
### Known limitations
### Extension points

## Arbitrage

### Business objective
Exploit price inefficiencies between venues after gas, slippage, and MEV costs.

### Strategy overview
Arbitrage uses deterministic rules and policy gates to transform market signals into execution intent.

### Decision logic
Use route quotes, latency, and liquidity depth to compute net edge.

### Required market conditions
Configured market conditions must satisfy freshness, liquidity, and venue availability thresholds.

### Entry conditions
All hard gates pass, the strategy is enabled, and the opportunity is not stale.

### Exit conditions
Exit on fill, invalidation, timeout, stop-loss, or risk breach.

### Position sizing methodology
Size by available capital, liquidity depth, expected edge, and risk budget.

### Capital allocation rules
Allocate only from the strategy budget and never exceed configured exposure limits.

### Risk controls
Apply max loss, freshness, concentration, drawdown, and execution controls.

### Stop-loss logic
Abort if the edge or signal quality falls below the configured threshold before execution.

### Take-profit logic
Take profit only on confirmed fills or realized settlement outcomes.

### Volatility handling
Reduce size or pause when volatility exceeds the accepted policy band.

### Liquidity requirements
Route only when the path depth can support target notional within impact limits.

### Slippage tolerance
Use the route-specific maximum slippage defined by the slippage model.

### Gas optimisation rules
Respect fee ceilings, replacement policy, and chain-specific gas guidance.

### MEV considerations
Prefer protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Configured chains only.

### Supported DEXs
Configured DEXs only.

### Required market data
Quotes, depth, gas, chain health, token metadata, and strategy-specific signals.

### AI interaction
AI may rank or explain but cannot bypass deterministic gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, and final outcome records.

### Monitoring metrics
Capture candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Include thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Measure realized edge, fill success, and execution latency.

### Failure scenarios
Handle stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Reconcile outcomes, update state, and pause when thresholds are exceeded.

### Known limitations
Strategy performance depends on market liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through the documented interfaces.

## Triangular Arbitrage

### Business objective
Capture conversion inefficiencies across three assets on a venue or chain.

### Strategy overview
Triangular Arbitrage uses deterministic rules and policy gates to transform market signals into execution intent.

### Decision logic
Evaluate three-leg closed-loop edge after fees and impact.

### Required market conditions
Configured market conditions must satisfy freshness, liquidity, and venue availability thresholds.

### Entry conditions
All hard gates pass, the strategy is enabled, and the opportunity is not stale.

### Exit conditions
Exit on fill, invalidation, timeout, stop-loss, or risk breach.

### Position sizing methodology
Size by available capital, liquidity depth, expected edge, and risk budget.

### Capital allocation rules
Allocate only from the strategy budget and never exceed configured exposure limits.

### Risk controls
Apply max loss, freshness, concentration, drawdown, and execution controls.

### Stop-loss logic
Abort if the edge or signal quality falls below the configured threshold before execution.

### Take-profit logic
Take profit only on confirmed fills or realized settlement outcomes.

### Volatility handling
Reduce size or pause when volatility exceeds the accepted policy band.

### Liquidity requirements
Route only when the path depth can support target notional within impact limits.

### Slippage tolerance
Use the route-specific maximum slippage defined by the slippage model.

### Gas optimisation rules
Respect fee ceilings, replacement policy, and chain-specific gas guidance.

### MEV considerations
Prefer protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Configured chains only.

### Supported DEXs
Configured DEXs only.

### Required market data
Quotes, depth, gas, chain health, token metadata, and strategy-specific signals.

### AI interaction
AI may rank or explain but cannot bypass deterministic gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, and final outcome records.

### Monitoring metrics
Capture candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Include thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Measure realized edge, fill success, and execution latency.

### Failure scenarios
Handle stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Reconcile outcomes, update state, and pause when thresholds are exceeded.

### Known limitations
Strategy performance depends on market liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through the documented interfaces.

## Cross-DEX Arbitrage

### Business objective
Capture spread across DEX venues.

### Strategy overview
Cross-DEX Arbitrage uses deterministic rules and policy gates to transform market signals into execution intent.

### Decision logic
Compare normalized quotes across routers and pools.

### Required market conditions
Configured market conditions must satisfy freshness, liquidity, and venue availability thresholds.

### Entry conditions
All hard gates pass, the strategy is enabled, and the opportunity is not stale.

### Exit conditions
Exit on fill, invalidation, timeout, stop-loss, or risk breach.

### Position sizing methodology
Size by available capital, liquidity depth, expected edge, and risk budget.

### Capital allocation rules
Allocate only from the strategy budget and never exceed configured exposure limits.

### Risk controls
Apply max loss, freshness, concentration, drawdown, and execution controls.

### Stop-loss logic
Abort if the edge or signal quality falls below the configured threshold before execution.

### Take-profit logic
Take profit only on confirmed fills or realized settlement outcomes.

### Volatility handling
Reduce size or pause when volatility exceeds the accepted policy band.

### Liquidity requirements
Route only when the path depth can support target notional within impact limits.

### Slippage tolerance
Use the route-specific maximum slippage defined by the slippage model.

### Gas optimisation rules
Respect fee ceilings, replacement policy, and chain-specific gas guidance.

### MEV considerations
Prefer protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Configured chains only.

### Supported DEXs
Configured DEXs only.

### Required market data
Quotes, depth, gas, chain health, token metadata, and strategy-specific signals.

### AI interaction
AI may rank or explain but cannot bypass deterministic gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, and final outcome records.

### Monitoring metrics
Capture candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Include thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Measure realized edge, fill success, and execution latency.

### Failure scenarios
Handle stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Reconcile outcomes, update state, and pause when thresholds are exceeded.

### Known limitations
Strategy performance depends on market liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through the documented interfaces.

## Cross-Chain Arbitrage

### Business objective
Capture spread across chains using supported bridges or native settlement paths.

### Strategy overview
Cross-Chain Arbitrage uses deterministic rules and policy gates to transform market signals into execution intent.

### Decision logic
Compare normalized cross-chain opportunity net of bridge, gas, and finality costs.

### Required market conditions
Configured market conditions must satisfy freshness, liquidity, and venue availability thresholds.

### Entry conditions
All hard gates pass, the strategy is enabled, and the opportunity is not stale.

### Exit conditions
Exit on fill, invalidation, timeout, stop-loss, or risk breach.

### Position sizing methodology
Size by available capital, liquidity depth, expected edge, and risk budget.

### Capital allocation rules
Allocate only from the strategy budget and never exceed configured exposure limits.

### Risk controls
Apply max loss, freshness, concentration, drawdown, and execution controls.

### Stop-loss logic
Abort if the edge or signal quality falls below the configured threshold before execution.

### Take-profit logic
Take profit only on confirmed fills or realized settlement outcomes.

### Volatility handling
Reduce size or pause when volatility exceeds the accepted policy band.

### Liquidity requirements
Route only when the path depth can support target notional within impact limits.

### Slippage tolerance
Use the route-specific maximum slippage defined by the slippage model.

### Gas optimisation rules
Respect fee ceilings, replacement policy, and chain-specific gas guidance.

### MEV considerations
Prefer protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Configured chains only.

### Supported DEXs
Configured DEXs only.

### Required market data
Quotes, depth, gas, chain health, token metadata, and strategy-specific signals.

### AI interaction
AI may rank or explain but cannot bypass deterministic gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, and final outcome records.

### Monitoring metrics
Capture candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Include thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Measure realized edge, fill success, and execution latency.

### Failure scenarios
Handle stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Reconcile outcomes, update state, and pause when thresholds are exceeded.

### Known limitations
Strategy performance depends on market liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through the documented interfaces.

## Flash Loan Arbitrage

### Business objective
Use borrowed capital to capture atomic arbitrage without pre-funded balance risk.

### Strategy overview
Flash Loan Arbitrage uses deterministic rules and policy gates to transform market signals into execution intent.

### Decision logic
Evaluate atomic borrow/repay feasibility, fee coverage, and route safety.

### Required market conditions
Configured market conditions must satisfy freshness, liquidity, and venue availability thresholds.

### Entry conditions
All hard gates pass, the strategy is enabled, and the opportunity is not stale.

### Exit conditions
Exit on fill, invalidation, timeout, stop-loss, or risk breach.

### Position sizing methodology
Size by available capital, liquidity depth, expected edge, and risk budget.

### Capital allocation rules
Allocate only from the strategy budget and never exceed configured exposure limits.

### Risk controls
Apply max loss, freshness, concentration, drawdown, and execution controls.

### Stop-loss logic
Abort if the edge or signal quality falls below the configured threshold before execution.

### Take-profit logic
Take profit only on confirmed fills or realized settlement outcomes.

### Volatility handling
Reduce size or pause when volatility exceeds the accepted policy band.

### Liquidity requirements
Route only when the path depth can support target notional within impact limits.

### Slippage tolerance
Use the route-specific maximum slippage defined by the slippage model.

### Gas optimisation rules
Respect fee ceilings, replacement policy, and chain-specific gas guidance.

### MEV considerations
Prefer protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Configured chains only.

### Supported DEXs
Configured DEXs only.

### Required market data
Quotes, depth, gas, chain health, token metadata, and strategy-specific signals.

### AI interaction
AI may rank or explain but cannot bypass deterministic gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, and final outcome records.

### Monitoring metrics
Capture candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Include thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Measure realized edge, fill success, and execution latency.

### Failure scenarios
Handle stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Reconcile outcomes, update state, and pause when thresholds are exceeded.

### Known limitations
Strategy performance depends on market liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through the documented interfaces.

## Statistical Arbitrage

### Business objective
Capture relative mispricing using mean reversion or spread models.

### Strategy overview
Statistical Arbitrage uses deterministic rules and policy gates to transform market signals into execution intent.

### Decision logic
Use historical spread z-score, volatility, and correlation to detect signal strength.

### Required market conditions
Configured market conditions must satisfy freshness, liquidity, and venue availability thresholds.

### Entry conditions
All hard gates pass, the strategy is enabled, and the opportunity is not stale.

### Exit conditions
Exit on fill, invalidation, timeout, stop-loss, or risk breach.

### Position sizing methodology
Size by available capital, liquidity depth, expected edge, and risk budget.

### Capital allocation rules
Allocate only from the strategy budget and never exceed configured exposure limits.

### Risk controls
Apply max loss, freshness, concentration, drawdown, and execution controls.

### Stop-loss logic
Abort if the edge or signal quality falls below the configured threshold before execution.

### Take-profit logic
Take profit only on confirmed fills or realized settlement outcomes.

### Volatility handling
Reduce size or pause when volatility exceeds the accepted policy band.

### Liquidity requirements
Route only when the path depth can support target notional within impact limits.

### Slippage tolerance
Use the route-specific maximum slippage defined by the slippage model.

### Gas optimisation rules
Respect fee ceilings, replacement policy, and chain-specific gas guidance.

### MEV considerations
Prefer protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Configured chains only.

### Supported DEXs
Configured DEXs only.

### Required market data
Quotes, depth, gas, chain health, token metadata, and strategy-specific signals.

### AI interaction
AI may rank or explain but cannot bypass deterministic gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, and final outcome records.

### Monitoring metrics
Capture candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Include thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Measure realized edge, fill success, and execution latency.

### Failure scenarios
Handle stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Reconcile outcomes, update state, and pause when thresholds are exceeded.

### Known limitations
Strategy performance depends on market liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through the documented interfaces.

## Grid Trading

### Business objective
Harvest oscillation inside a defined price band.

### Strategy overview
Grid Trading uses deterministic rules and policy gates to transform market signals into execution intent.

### Decision logic
Place symmetrical ladder orders around a reference price and rebalance on fills.

### Required market conditions
Configured market conditions must satisfy freshness, liquidity, and venue availability thresholds.

### Entry conditions
All hard gates pass, the strategy is enabled, and the opportunity is not stale.

### Exit conditions
Exit on fill, invalidation, timeout, stop-loss, or risk breach.

### Position sizing methodology
Size by available capital, liquidity depth, expected edge, and risk budget.

### Capital allocation rules
Allocate only from the strategy budget and never exceed configured exposure limits.

### Risk controls
Apply max loss, freshness, concentration, drawdown, and execution controls.

### Stop-loss logic
Abort if the edge or signal quality falls below the configured threshold before execution.

### Take-profit logic
Take profit only on confirmed fills or realized settlement outcomes.

### Volatility handling
Reduce size or pause when volatility exceeds the accepted policy band.

### Liquidity requirements
Route only when the path depth can support target notional within impact limits.

### Slippage tolerance
Use the route-specific maximum slippage defined by the slippage model.

### Gas optimisation rules
Respect fee ceilings, replacement policy, and chain-specific gas guidance.

### MEV considerations
Prefer protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Configured chains only.

### Supported DEXs
Configured DEXs only.

### Required market data
Quotes, depth, gas, chain health, token metadata, and strategy-specific signals.

### AI interaction
AI may rank or explain but cannot bypass deterministic gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, and final outcome records.

### Monitoring metrics
Capture candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Include thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Measure realized edge, fill success, and execution latency.

### Failure scenarios
Handle stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Reconcile outcomes, update state, and pause when thresholds are exceeded.

### Known limitations
Strategy performance depends on market liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through the documented interfaces.

## Scalping

### Business objective
Capture small intraday inefficiencies with very tight hold times.

### Strategy overview
Scalping uses deterministic rules and policy gates to transform market signals into execution intent.

### Decision logic
Use short-lived momentum and spread signals with aggressive freshness gates.

### Required market conditions
Configured market conditions must satisfy freshness, liquidity, and venue availability thresholds.

### Entry conditions
All hard gates pass, the strategy is enabled, and the opportunity is not stale.

### Exit conditions
Exit on fill, invalidation, timeout, stop-loss, or risk breach.

### Position sizing methodology
Size by available capital, liquidity depth, expected edge, and risk budget.

### Capital allocation rules
Allocate only from the strategy budget and never exceed configured exposure limits.

### Risk controls
Apply max loss, freshness, concentration, drawdown, and execution controls.

### Stop-loss logic
Abort if the edge or signal quality falls below the configured threshold before execution.

### Take-profit logic
Take profit only on confirmed fills or realized settlement outcomes.

### Volatility handling
Reduce size or pause when volatility exceeds the accepted policy band.

### Liquidity requirements
Route only when the path depth can support target notional within impact limits.

### Slippage tolerance
Use the route-specific maximum slippage defined by the slippage model.

### Gas optimisation rules
Respect fee ceilings, replacement policy, and chain-specific gas guidance.

### MEV considerations
Prefer protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Configured chains only.

### Supported DEXs
Configured DEXs only.

### Required market data
Quotes, depth, gas, chain health, token metadata, and strategy-specific signals.

### AI interaction
AI may rank or explain but cannot bypass deterministic gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, and final outcome records.

### Monitoring metrics
Capture candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Include thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Measure realized edge, fill success, and execution latency.

### Failure scenarios
Handle stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Reconcile outcomes, update state, and pause when thresholds are exceeded.

### Known limitations
Strategy performance depends on market liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through the documented interfaces.

## Momentum

### Business objective
Follow directional continuation when trend strength is strong.

### Strategy overview
Momentum uses deterministic rules and policy gates to transform market signals into execution intent.

### Decision logic
Use trend confirmation, volume expansion, and volatility filters.

### Required market conditions
Configured market conditions must satisfy freshness, liquidity, and venue availability thresholds.

### Entry conditions
All hard gates pass, the strategy is enabled, and the opportunity is not stale.

### Exit conditions
Exit on fill, invalidation, timeout, stop-loss, or risk breach.

### Position sizing methodology
Size by available capital, liquidity depth, expected edge, and risk budget.

### Capital allocation rules
Allocate only from the strategy budget and never exceed configured exposure limits.

### Risk controls
Apply max loss, freshness, concentration, drawdown, and execution controls.

### Stop-loss logic
Abort if the edge or signal quality falls below the configured threshold before execution.

### Take-profit logic
Take profit only on confirmed fills or realized settlement outcomes.

### Volatility handling
Reduce size or pause when volatility exceeds the accepted policy band.

### Liquidity requirements
Route only when the path depth can support target notional within impact limits.

### Slippage tolerance
Use the route-specific maximum slippage defined by the slippage model.

### Gas optimisation rules
Respect fee ceilings, replacement policy, and chain-specific gas guidance.

### MEV considerations
Prefer protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Configured chains only.

### Supported DEXs
Configured DEXs only.

### Required market data
Quotes, depth, gas, chain health, token metadata, and strategy-specific signals.

### AI interaction
AI may rank or explain but cannot bypass deterministic gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, and final outcome records.

### Monitoring metrics
Capture candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Include thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Measure realized edge, fill success, and execution latency.

### Failure scenarios
Handle stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Reconcile outcomes, update state, and pause when thresholds are exceeded.

### Known limitations
Strategy performance depends on market liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through the documented interfaces.

## Mean Reversion

### Business objective
Trade price excursions back toward a statistical baseline.

### Strategy overview
Mean Reversion uses deterministic rules and policy gates to transform market signals into execution intent.

### Decision logic
Use deviation from moving average or fair value bands.

### Required market conditions
Configured market conditions must satisfy freshness, liquidity, and venue availability thresholds.

### Entry conditions
All hard gates pass, the strategy is enabled, and the opportunity is not stale.

### Exit conditions
Exit on fill, invalidation, timeout, stop-loss, or risk breach.

### Position sizing methodology
Size by available capital, liquidity depth, expected edge, and risk budget.

### Capital allocation rules
Allocate only from the strategy budget and never exceed configured exposure limits.

### Risk controls
Apply max loss, freshness, concentration, drawdown, and execution controls.

### Stop-loss logic
Abort if the edge or signal quality falls below the configured threshold before execution.

### Take-profit logic
Take profit only on confirmed fills or realized settlement outcomes.

### Volatility handling
Reduce size or pause when volatility exceeds the accepted policy band.

### Liquidity requirements
Route only when the path depth can support target notional within impact limits.

### Slippage tolerance
Use the route-specific maximum slippage defined by the slippage model.

### Gas optimisation rules
Respect fee ceilings, replacement policy, and chain-specific gas guidance.

### MEV considerations
Prefer protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Configured chains only.

### Supported DEXs
Configured DEXs only.

### Required market data
Quotes, depth, gas, chain health, token metadata, and strategy-specific signals.

### AI interaction
AI may rank or explain but cannot bypass deterministic gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, and final outcome records.

### Monitoring metrics
Capture candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Include thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Measure realized edge, fill success, and execution latency.

### Failure scenarios
Handle stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Reconcile outcomes, update state, and pause when thresholds are exceeded.

### Known limitations
Strategy performance depends on market liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through the documented interfaces.

## Market Making

### Business objective
Quote both sides to capture spread while controlling inventory.

### Strategy overview
Market Making uses deterministic rules and policy gates to transform market signals into execution intent.

### Decision logic
Use inventory-aware bid/ask placement around fair value.

### Required market conditions
Configured market conditions must satisfy freshness, liquidity, and venue availability thresholds.

### Entry conditions
All hard gates pass, the strategy is enabled, and the opportunity is not stale.

### Exit conditions
Exit on fill, invalidation, timeout, stop-loss, or risk breach.

### Position sizing methodology
Size by available capital, liquidity depth, expected edge, and risk budget.

### Capital allocation rules
Allocate only from the strategy budget and never exceed configured exposure limits.

### Risk controls
Apply max loss, freshness, concentration, drawdown, and execution controls.

### Stop-loss logic
Abort if the edge or signal quality falls below the configured threshold before execution.

### Take-profit logic
Take profit only on confirmed fills or realized settlement outcomes.

### Volatility handling
Reduce size or pause when volatility exceeds the accepted policy band.

### Liquidity requirements
Route only when the path depth can support target notional within impact limits.

### Slippage tolerance
Use the route-specific maximum slippage defined by the slippage model.

### Gas optimisation rules
Respect fee ceilings, replacement policy, and chain-specific gas guidance.

### MEV considerations
Prefer protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Configured chains only.

### Supported DEXs
Configured DEXs only.

### Required market data
Quotes, depth, gas, chain health, token metadata, and strategy-specific signals.

### AI interaction
AI may rank or explain but cannot bypass deterministic gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, and final outcome records.

### Monitoring metrics
Capture candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Include thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Measure realized edge, fill success, and execution latency.

### Failure scenarios
Handle stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Reconcile outcomes, update state, and pause when thresholds are exceeded.

### Known limitations
Strategy performance depends on market liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through the documented interfaces.

## Liquidity Provision

### Business objective
Supply liquidity to earn fees while managing impermanent loss.

### Strategy overview
Liquidity Provision uses deterministic rules and policy gates to transform market signals into execution intent.

### Decision logic
Select pools by fee yield, depth, and expected adverse selection.

### Required market conditions
Configured market conditions must satisfy freshness, liquidity, and venue availability thresholds.

### Entry conditions
All hard gates pass, the strategy is enabled, and the opportunity is not stale.

### Exit conditions
Exit on fill, invalidation, timeout, stop-loss, or risk breach.

### Position sizing methodology
Size by available capital, liquidity depth, expected edge, and risk budget.

### Capital allocation rules
Allocate only from the strategy budget and never exceed configured exposure limits.

### Risk controls
Apply max loss, freshness, concentration, drawdown, and execution controls.

### Stop-loss logic
Abort if the edge or signal quality falls below the configured threshold before execution.

### Take-profit logic
Take profit only on confirmed fills or realized settlement outcomes.

### Volatility handling
Reduce size or pause when volatility exceeds the accepted policy band.

### Liquidity requirements
Route only when the path depth can support target notional within impact limits.

### Slippage tolerance
Use the route-specific maximum slippage defined by the slippage model.

### Gas optimisation rules
Respect fee ceilings, replacement policy, and chain-specific gas guidance.

### MEV considerations
Prefer protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Configured chains only.

### Supported DEXs
Configured DEXs only.

### Required market data
Quotes, depth, gas, chain health, token metadata, and strategy-specific signals.

### AI interaction
AI may rank or explain but cannot bypass deterministic gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, and final outcome records.

### Monitoring metrics
Capture candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Include thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Measure realized edge, fill success, and execution latency.

### Failure scenarios
Handle stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Reconcile outcomes, update state, and pause when thresholds are exceeded.

### Known limitations
Strategy performance depends on market liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through the documented interfaces.

## Yield Farming

### Business objective
Allocate capital to incentives where expected net yield exceeds risk-adjusted threshold.

### Strategy overview
Yield Farming uses deterministic rules and policy gates to transform market signals into execution intent.

### Decision logic
Compare reward emissions, lockup terms, and withdrawal penalties.

### Required market conditions
Configured market conditions must satisfy freshness, liquidity, and venue availability thresholds.

### Entry conditions
All hard gates pass, the strategy is enabled, and the opportunity is not stale.

### Exit conditions
Exit on fill, invalidation, timeout, stop-loss, or risk breach.

### Position sizing methodology
Size by available capital, liquidity depth, expected edge, and risk budget.

### Capital allocation rules
Allocate only from the strategy budget and never exceed configured exposure limits.

### Risk controls
Apply max loss, freshness, concentration, drawdown, and execution controls.

### Stop-loss logic
Abort if the edge or signal quality falls below the configured threshold before execution.

### Take-profit logic
Take profit only on confirmed fills or realized settlement outcomes.

### Volatility handling
Reduce size or pause when volatility exceeds the accepted policy band.

### Liquidity requirements
Route only when the path depth can support target notional within impact limits.

### Slippage tolerance
Use the route-specific maximum slippage defined by the slippage model.

### Gas optimisation rules
Respect fee ceilings, replacement policy, and chain-specific gas guidance.

### MEV considerations
Prefer protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Configured chains only.

### Supported DEXs
Configured DEXs only.

### Required market data
Quotes, depth, gas, chain health, token metadata, and strategy-specific signals.

### AI interaction
AI may rank or explain but cannot bypass deterministic gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, and final outcome records.

### Monitoring metrics
Capture candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Include thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Measure realized edge, fill success, and execution latency.

### Failure scenarios
Handle stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Reconcile outcomes, update state, and pause when thresholds are exceeded.

### Known limitations
Strategy performance depends on market liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through the documented interfaces.

## Dollar-Cost Averaging

### Business objective
Accumulate exposure over time with deterministic sizing.

### Strategy overview
Dollar-Cost Averaging uses deterministic rules and policy gates to transform market signals into execution intent.

### Decision logic
Allocate fixed schedule-based orders irrespective of short-term noise.

### Required market conditions
Configured market conditions must satisfy freshness, liquidity, and venue availability thresholds.

### Entry conditions
All hard gates pass, the strategy is enabled, and the opportunity is not stale.

### Exit conditions
Exit on fill, invalidation, timeout, stop-loss, or risk breach.

### Position sizing methodology
Size by available capital, liquidity depth, expected edge, and risk budget.

### Capital allocation rules
Allocate only from the strategy budget and never exceed configured exposure limits.

### Risk controls
Apply max loss, freshness, concentration, drawdown, and execution controls.

### Stop-loss logic
Abort if the edge or signal quality falls below the configured threshold before execution.

### Take-profit logic
Take profit only on confirmed fills or realized settlement outcomes.

### Volatility handling
Reduce size or pause when volatility exceeds the accepted policy band.

### Liquidity requirements
Route only when the path depth can support target notional within impact limits.

### Slippage tolerance
Use the route-specific maximum slippage defined by the slippage model.

### Gas optimisation rules
Respect fee ceilings, replacement policy, and chain-specific gas guidance.

### MEV considerations
Prefer protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Configured chains only.

### Supported DEXs
Configured DEXs only.

### Required market data
Quotes, depth, gas, chain health, token metadata, and strategy-specific signals.

### AI interaction
AI may rank or explain but cannot bypass deterministic gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, and final outcome records.

### Monitoring metrics
Capture candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Include thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Measure realized edge, fill success, and execution latency.

### Failure scenarios
Handle stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Reconcile outcomes, update state, and pause when thresholds are exceeded.

### Known limitations
Strategy performance depends on market liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through the documented interfaces.

## Cross-references
- `RISK-ENGINE.md`
- `AI-PIPELINE.md`
- `EXECUTION-ENGINE.md`
- `MARKET-INTELLIGENCE.md`
