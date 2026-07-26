# Strategies

## Document type
This document is an overview, reference, or index as noted below.

# Strategies

## Purpose
This document is the authoritative specification for every supported trading strategy and their implementation behavior.

## Ownership
- Owns strategy business logic, decision logic, lifecycle, runtime workflow, simulation binding, and performance metrics.
- AI may rank or explain strategies, but strategy authority remains here.

## Shared contract
Every strategy must define objective, overview, decision logic, market conditions, entry, exit, sizing, allocation, risk, slippage, gas, MEV, chain/DEX support, market data, AI interaction, runtime workflow, state machine, IPC, persistence, monitoring, backtesting, simulation, stress testing, failure handling, recovery, limitations, and extension points.

## Shared lifecycle
Discover -> Score -> Validate -> Size -> Approve -> Execute -> Monitor -> Exit -> Reconcile -> Learn.

## Common strategy requirements
- Deterministic decisioning for the same snapshot and config.
- Hard rejection on stale data, unsafe route, or risk breach.
- Persisted plan lineage for audit and replay.
- Monitoring and alerting on every failure class.
- Simulation and backtesting parity with live decision logic.

## Strategy template
### Business objective
### Strategy overview
### Mathematical model or decision logic
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
Exploit cross-venue price inefficiencies net of fees, gas, slippage, and MEV risk.

### Strategy overview
Arbitrage is implemented as a deterministic, policy-gated trading strategy with explicit entry/exit and lifecycle rules.

### Mathematical model or decision logic
Compare normalized quotes across venues and execute only when net edge is positive after all costs.

### Required market conditions
Cross-DEX, cross-pool, and cross-chain where enabled.

### Entry conditions
All hard gates pass and the opportunity remains fresh.

### Exit conditions
Exit on fill, invalidation, stop-loss, timeout, or risk breach.

### Position sizing methodology
Size by risk budget, liquidity, and expected net edge.

### Capital allocation rules
Allocate only within strategy budget and exposure limits.

### Risk controls
Route-level fill, price impact, fee, gas, latency, stale data.

### Stop-loss logic
Close or cancel when the configured loss or signal invalidation threshold is reached.

### Take-profit logic
Lock profit when the terminal execution outcome meets the strategy objective.

### Volatility handling
Reduce size, widen filters, or pause when volatility exceeds policy.

### Liquidity requirements
Only trade when depth supports target notional within impact limits.

### Slippage tolerance
Use route-specific maximum slippage and reject violations.

### Gas optimisation rules
Respect gas ceilings, fee replacement policy, and chain-specific fee guidance.

### MEV considerations
Use protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Primary on DEXs with deep liquidity and low latency routing.

### Supported DEXs
Configured DEXs only.

### Required market data
Reject on stale quotes, thin liquidity, or failed protection.

### AI interaction
AI may rank, explain, or summarize but cannot override hard strategy gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, timestamps, and final outcome records.

### Monitoring metrics
Candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Realized edge, fill success, and execution latency.

### Failure scenarios
Stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Recompute on quote drift and cancel if edge disappears.

### Known limitations
Performance depends on liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through documented interfaces.

## Triangular Arbitrage

### Business objective
Exploit in-venue circular pricing inefficiencies.

### Strategy overview
Triangular Arbitrage is implemented as a deterministic, policy-gated trading strategy with explicit entry/exit and lifecycle rules.

### Mathematical model or decision logic
Evaluate a three-leg cycle and compute closed-loop profit after costs.

### Required market conditions
Single venue with compatible asset triangle.

### Entry conditions
All hard gates pass and the opportunity remains fresh.

### Exit conditions
Exit on fill, invalidation, stop-loss, timeout, or risk breach.

### Position sizing methodology
Size by risk budget, liquidity, and expected net edge.

### Capital allocation rules
Allocate only within strategy budget and exposure limits.

### Risk controls
Fill risk, per-leg impact, stale leg rejection.

### Stop-loss logic
Close or cancel when the configured loss or signal invalidation threshold is reached.

### Take-profit logic
Lock profit when the terminal execution outcome meets the strategy objective.

### Volatility handling
Reduce size, widen filters, or pause when volatility exceeds policy.

### Liquidity requirements
Only trade when depth supports target notional within impact limits.

### Slippage tolerance
Use route-specific maximum slippage and reject violations.

### Gas optimisation rules
Respect gas ceilings, fee replacement policy, and chain-specific fee guidance.

### MEV considerations
Use protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Venue with reliable atomic or near-atomic routing.

### Supported DEXs
Configured DEXs only.

### Required market data
Leg-specific deltas, fees, gas, triangle topology.

### AI interaction
AI may rank, explain, or summarize but cannot override hard strategy gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, timestamps, and final outcome records.

### Monitoring metrics
Candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Realized edge, fill success, and execution latency.

### Failure scenarios
Stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Negative cycle detection and stale leg protection.

### Known limitations
Performance depends on liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through documented interfaces.

## Cross-DEX Arbitrage

### Business objective
Capture pricing differences across DEXs on the same chain.

### Strategy overview
Cross-DEX Arbitrage is implemented as a deterministic, policy-gated trading strategy with explicit entry/exit and lifecycle rules.

### Mathematical model or decision logic
Rank route pairs by spread minus gas and slippage.

### Required market conditions
Multiple DEX quotes and stable chain conditions.

### Entry conditions
All hard gates pass and the opportunity remains fresh.

### Exit conditions
Exit on fill, invalidation, stop-loss, timeout, or risk breach.

### Position sizing methodology
Size by risk budget, liquidity, and expected net edge.

### Capital allocation rules
Allocate only within strategy budget and exposure limits.

### Risk controls
Route drift, pool depth collapse, quote staleness.

### Stop-loss logic
Close or cancel when the configured loss or signal invalidation threshold is reached.

### Take-profit logic
Lock profit when the terminal execution outcome meets the strategy objective.

### Volatility handling
Reduce size, widen filters, or pause when volatility exceeds policy.

### Liquidity requirements
Only trade when depth supports target notional within impact limits.

### Slippage tolerance
Use route-specific maximum slippage and reject violations.

### Gas optimisation rules
Respect gas ceilings, fee replacement policy, and chain-specific fee guidance.

### MEV considerations
Use protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Supported chain DEX set only.

### Supported DEXs
Configured DEXs only.

### Required market data
DEX quotes, pool metadata, gas, route costs.

### AI interaction
AI may rank, explain, or summarize but cannot override hard strategy gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, timestamps, and final outcome records.

### Monitoring metrics
Candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Realized edge, fill success, and execution latency.

### Failure scenarios
Stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Route invalidation on quote drift.

### Known limitations
Performance depends on liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through documented interfaces.

## Cross-Chain Arbitrage

### Business objective
Exploit differences across chains when bridge and finality costs still leave positive edge.

### Strategy overview
Cross-Chain Arbitrage is implemented as a deterministic, policy-gated trading strategy with explicit entry/exit and lifecycle rules.

### Mathematical model or decision logic
Compare normalized cross-chain opportunity after bridge latency and settlement risk.

### Required market conditions
Stable chains, bridge availability, sufficient finality.

### Entry conditions
All hard gates pass and the opportunity remains fresh.

### Exit conditions
Exit on fill, invalidation, stop-loss, timeout, or risk breach.

### Position sizing methodology
Size by risk budget, liquidity, and expected net edge.

### Capital allocation rules
Allocate only within strategy budget and exposure limits.

### Risk controls
Reorg risk, bridge failure, finality delay.

### Stop-loss logic
Close or cancel when the configured loss or signal invalidation threshold is reached.

### Take-profit logic
Lock profit when the terminal execution outcome meets the strategy objective.

### Volatility handling
Reduce size, widen filters, or pause when volatility exceeds policy.

### Liquidity requirements
Only trade when depth supports target notional within impact limits.

### Slippage tolerance
Use route-specific maximum slippage and reject violations.

### Gas optimisation rules
Respect gas ceilings, fee replacement policy, and chain-specific fee guidance.

### MEV considerations
Use protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Supported chains and bridge routes only.

### Supported DEXs
Configured DEXs only.

### Required market data
Chain prices, bridge status, gas, finality score.

### AI interaction
AI may rank, explain, or summarize but cannot override hard strategy gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, timestamps, and final outcome records.

### Monitoring metrics
Candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Realized edge, fill success, and execution latency.

### Failure scenarios
Stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Revalidate on chain state change and bridge delay.

### Known limitations
Performance depends on liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through documented interfaces.

## Flash Loan Arbitrage

### Business objective
Use borrowed capital atomically to amplify arbitrage without pre-funding.

### Strategy overview
Flash Loan Arbitrage is implemented as a deterministic, policy-gated trading strategy with explicit entry/exit and lifecycle rules.

### Mathematical model or decision logic
Atomic borrow, execute, repay, and retain profit if all steps succeed.

### Required market conditions
Flash-loan provider, atomic execution path, ample liquidity.

### Entry conditions
All hard gates pass and the opportunity remains fresh.

### Exit conditions
Exit on fill, invalidation, stop-loss, timeout, or risk breach.

### Position sizing methodology
Size by risk budget, liquidity, and expected net edge.

### Capital allocation rules
Allocate only within strategy budget and exposure limits.

### Risk controls
Execution revert, insufficient repayment, gas spike.

### Stop-loss logic
Close or cancel when the configured loss or signal invalidation threshold is reached.

### Take-profit logic
Lock profit when the terminal execution outcome meets the strategy objective.

### Volatility handling
Reduce size, widen filters, or pause when volatility exceeds policy.

### Liquidity requirements
Only trade when depth supports target notional within impact limits.

### Slippage tolerance
Use route-specific maximum slippage and reject violations.

### Gas optimisation rules
Respect gas ceilings, fee replacement policy, and chain-specific fee guidance.

### MEV considerations
Use protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Chains and venues that support atomic execution.

### Supported DEXs
Configured DEXs only.

### Required market data
Borrow amount, route quotes, fee model.

### AI interaction
AI may rank, explain, or summarize but cannot override hard strategy gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, timestamps, and final outcome records.

### Monitoring metrics
Candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Realized edge, fill success, and execution latency.

### Failure scenarios
Stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Fallback to no-trade if atomic constraints fail.

### Known limitations
Performance depends on liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through documented interfaces.

## Statistical Arbitrage

### Business objective
Trade mean-reverting or spread-based dislocations.

### Strategy overview
Statistical Arbitrage is implemented as a deterministic, policy-gated trading strategy with explicit entry/exit and lifecycle rules.

### Mathematical model or decision logic
Use z-score, correlation, and spread stability to decide entry.

### Required market conditions
Stable historical relationship, bounded volatility.

### Entry conditions
All hard gates pass and the opportunity remains fresh.

### Exit conditions
Exit on fill, invalidation, stop-loss, timeout, or risk breach.

### Position sizing methodology
Size by risk budget, liquidity, and expected net edge.

### Capital allocation rules
Allocate only within strategy budget and exposure limits.

### Risk controls
Regime shift, correlation break, spread widening.

### Stop-loss logic
Close or cancel when the configured loss or signal invalidation threshold is reached.

### Take-profit logic
Lock profit when the terminal execution outcome meets the strategy objective.

### Volatility handling
Reduce size, widen filters, or pause when volatility exceeds policy.

### Liquidity requirements
Only trade when depth supports target notional within impact limits.

### Slippage tolerance
Use route-specific maximum slippage and reject violations.

### Gas optimisation rules
Respect gas ceilings, fee replacement policy, and chain-specific fee guidance.

### MEV considerations
Use protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Configured assets and venues only.

### Supported DEXs
Configured DEXs only.

### Required market data
Historical series, live spread, correlation features.

### AI interaction
AI may rank, explain, or summarize but cannot override hard strategy gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, timestamps, and final outcome records.

### Monitoring metrics
Candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Realized edge, fill success, and execution latency.

### Failure scenarios
Stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Exit when mean reversion occurs or relationship breaks.

### Known limitations
Performance depends on liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through documented interfaces.

## Grid Trading

### Business objective
Harvest oscillation inside a defined price band.

### Strategy overview
Grid Trading is implemented as a deterministic, policy-gated trading strategy with explicit entry/exit and lifecycle rules.

### Mathematical model or decision logic
Place deterministic buy/sell ladder around reference price.

### Required market conditions
Range-bound market, sufficient liquidity.

### Entry conditions
All hard gates pass and the opportunity remains fresh.

### Exit conditions
Exit on fill, invalidation, stop-loss, timeout, or risk breach.

### Position sizing methodology
Size by risk budget, liquidity, and expected net edge.

### Capital allocation rules
Allocate only within strategy budget and exposure limits.

### Risk controls
Band breakout, slippage, whipsaw.

### Stop-loss logic
Close or cancel when the configured loss or signal invalidation threshold is reached.

### Take-profit logic
Lock profit when the terminal execution outcome meets the strategy objective.

### Volatility handling
Reduce size, widen filters, or pause when volatility exceeds policy.

### Liquidity requirements
Only trade when depth supports target notional within impact limits.

### Slippage tolerance
Use route-specific maximum slippage and reject violations.

### Gas optimisation rules
Respect gas ceilings, fee replacement policy, and chain-specific fee guidance.

### MEV considerations
Use protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Supported chains/venues only.

### Supported DEXs
Configured DEXs only.

### Required market data
Reference price, volatility, depth.

### AI interaction
AI may rank, explain, or summarize but cannot override hard strategy gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, timestamps, and final outcome records.

### Monitoring metrics
Candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Realized edge, fill success, and execution latency.

### Failure scenarios
Stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Re-center on band shift.

### Known limitations
Performance depends on liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through documented interfaces.

## Scalping

### Business objective
Capture very short-lived inefficiencies.

### Strategy overview
Scalping is implemented as a deterministic, policy-gated trading strategy with explicit entry/exit and lifecycle rules.

### Mathematical model or decision logic
Use tight spread and momentum windows with rapid exits.

### Required market conditions
Fast market, low latency, tight spreads.

### Entry conditions
All hard gates pass and the opportunity remains fresh.

### Exit conditions
Exit on fill, invalidation, stop-loss, timeout, or risk breach.

### Position sizing methodology
Size by risk budget, liquidity, and expected net edge.

### Capital allocation rules
Allocate only within strategy budget and exposure limits.

### Risk controls
Spread widening, stale quotes, queue lag.

### Stop-loss logic
Close or cancel when the configured loss or signal invalidation threshold is reached.

### Take-profit logic
Lock profit when the terminal execution outcome meets the strategy objective.

### Volatility handling
Reduce size, widen filters, or pause when volatility exceeds policy.

### Liquidity requirements
Only trade when depth supports target notional within impact limits.

### Slippage tolerance
Use route-specific maximum slippage and reject violations.

### Gas optimisation rules
Respect gas ceilings, fee replacement policy, and chain-specific fee guidance.

### MEV considerations
Use protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Low-latency supported venues.

### Supported DEXs
Configured DEXs only.

### Required market data
Live order book, quote velocity, gas.

### AI interaction
AI may rank, explain, or summarize but cannot override hard strategy gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, timestamps, and final outcome records.

### Monitoring metrics
Candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Realized edge, fill success, and execution latency.

### Failure scenarios
Stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Immediate exit on signal decay.

### Known limitations
Performance depends on liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through documented interfaces.

## Momentum

### Business objective
Follow directional continuation when move strength is sufficient.

### Strategy overview
Momentum is implemented as a deterministic, policy-gated trading strategy with explicit entry/exit and lifecycle rules.

### Mathematical model or decision logic
Combine trend, volume, and acceleration signals.

### Required market conditions
Directional trend with confirming volume.

### Entry conditions
All hard gates pass and the opportunity remains fresh.

### Exit conditions
Exit on fill, invalidation, stop-loss, timeout, or risk breach.

### Position sizing methodology
Size by risk budget, liquidity, and expected net edge.

### Capital allocation rules
Allocate only within strategy budget and exposure limits.

### Risk controls
Trend reversal, volume fade, high churn.

### Stop-loss logic
Close or cancel when the configured loss or signal invalidation threshold is reached.

### Take-profit logic
Lock profit when the terminal execution outcome meets the strategy objective.

### Volatility handling
Reduce size, widen filters, or pause when volatility exceeds policy.

### Liquidity requirements
Only trade when depth supports target notional within impact limits.

### Slippage tolerance
Use route-specific maximum slippage and reject violations.

### Gas optimisation rules
Respect gas ceilings, fee replacement policy, and chain-specific fee guidance.

### MEV considerations
Use protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Supported markets only.

### Supported DEXs
Configured DEXs only.

### Required market data
Trend features, volume, spread.

### AI interaction
AI may rank, explain, or summarize but cannot override hard strategy gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, timestamps, and final outcome records.

### Monitoring metrics
Candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Realized edge, fill success, and execution latency.

### Failure scenarios
Stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Exit on reversal or stop-loss.

### Known limitations
Performance depends on liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through documented interfaces.

## Mean Reversion

### Business objective
Trade excursions back toward fair value.

### Strategy overview
Mean Reversion is implemented as a deterministic, policy-gated trading strategy with explicit entry/exit and lifecycle rules.

### Mathematical model or decision logic
Use deviation from moving average or fair value band.

### Required market conditions
Statistical deviation with stable baseline.

### Entry conditions
All hard gates pass and the opportunity remains fresh.

### Exit conditions
Exit on fill, invalidation, stop-loss, timeout, or risk breach.

### Position sizing methodology
Size by risk budget, liquidity, and expected net edge.

### Capital allocation rules
Allocate only within strategy budget and exposure limits.

### Risk controls
Breakout, regime change, drift.

### Stop-loss logic
Close or cancel when the configured loss or signal invalidation threshold is reached.

### Take-profit logic
Lock profit when the terminal execution outcome meets the strategy objective.

### Volatility handling
Reduce size, widen filters, or pause when volatility exceeds policy.

### Liquidity requirements
Only trade when depth supports target notional within impact limits.

### Slippage tolerance
Use route-specific maximum slippage and reject violations.

### Gas optimisation rules
Respect gas ceilings, fee replacement policy, and chain-specific fee guidance.

### MEV considerations
Use protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Supported markets only.

### Supported DEXs
Configured DEXs only.

### Required market data
Baseline, variance, z-score.

### AI interaction
AI may rank, explain, or summarize but cannot override hard strategy gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, timestamps, and final outcome records.

### Monitoring metrics
Candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Realized edge, fill success, and execution latency.

### Failure scenarios
Stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Exit at baseline or invalidation.

### Known limitations
Performance depends on liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through documented interfaces.

## Market Making

### Business objective
Quote both sides to capture spread while controlling inventory.

### Strategy overview
Market Making is implemented as a deterministic, policy-gated trading strategy with explicit entry/exit and lifecycle rules.

### Mathematical model or decision logic
Maintain inventory-aware bid/ask quotes around fair value.

### Required market conditions
Two-sided liquidity and bounded inventory risk.

### Entry conditions
All hard gates pass and the opportunity remains fresh.

### Exit conditions
Exit on fill, invalidation, stop-loss, timeout, or risk breach.

### Position sizing methodology
Size by risk budget, liquidity, and expected net edge.

### Capital allocation rules
Allocate only within strategy budget and exposure limits.

### Risk controls
Inventory imbalance, adverse selection, gap move.

### Stop-loss logic
Close or cancel when the configured loss or signal invalidation threshold is reached.

### Take-profit logic
Lock profit when the terminal execution outcome meets the strategy objective.

### Volatility handling
Reduce size, widen filters, or pause when volatility exceeds policy.

### Liquidity requirements
Only trade when depth supports target notional within impact limits.

### Slippage tolerance
Use route-specific maximum slippage and reject violations.

### Gas optimisation rules
Respect gas ceilings, fee replacement policy, and chain-specific fee guidance.

### MEV considerations
Use protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Venues that support quote refresh and cancellation.

### Supported DEXs
Configured DEXs only.

### Required market data
Order book, inventory, fee model.

### AI interaction
AI may rank, explain, or summarize but cannot override hard strategy gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, timestamps, and final outcome records.

### Monitoring metrics
Candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Realized edge, fill success, and execution latency.

### Failure scenarios
Stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Requote on inventory or market movement.

### Known limitations
Performance depends on liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through documented interfaces.

## Liquidity Provision

### Business objective
Supply liquidity for fee income while managing impermanent loss.

### Strategy overview
Liquidity Provision is implemented as a deterministic, policy-gated trading strategy with explicit entry/exit and lifecycle rules.

### Mathematical model or decision logic
Select pools based on yield, depth, and risk.

### Required market conditions
Eligible pools with sufficient volume and depth.

### Entry conditions
All hard gates pass and the opportunity remains fresh.

### Exit conditions
Exit on fill, invalidation, stop-loss, timeout, or risk breach.

### Position sizing methodology
Size by risk budget, liquidity, and expected net edge.

### Capital allocation rules
Allocate only within strategy budget and exposure limits.

### Risk controls
Impermanent loss, pool drain, adverse selection.

### Stop-loss logic
Close or cancel when the configured loss or signal invalidation threshold is reached.

### Take-profit logic
Lock profit when the terminal execution outcome meets the strategy objective.

### Volatility handling
Reduce size, widen filters, or pause when volatility exceeds policy.

### Liquidity requirements
Only trade when depth supports target notional within impact limits.

### Slippage tolerance
Use route-specific maximum slippage and reject violations.

### Gas optimisation rules
Respect gas ceilings, fee replacement policy, and chain-specific fee guidance.

### MEV considerations
Use protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Supported pools and chains only.

### Supported DEXs
Configured DEXs only.

### Required market data
Pool analytics, volatility, fees.

### AI interaction
AI may rank, explain, or summarize but cannot override hard strategy gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, timestamps, and final outcome records.

### Monitoring metrics
Candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Realized edge, fill success, and execution latency.

### Failure scenarios
Stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Withdraw or rebalance on risk breach.

### Known limitations
Performance depends on liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through documented interfaces.

## Yield Farming

### Business objective
Allocate capital to incentive programs where net yield is attractive.

### Strategy overview
Yield Farming is implemented as a deterministic, policy-gated trading strategy with explicit entry/exit and lifecycle rules.

### Mathematical model or decision logic
Compare emissions, lockups, and withdrawal penalties.

### Required market conditions
Valid incentive program and acceptable lockup.

### Entry conditions
All hard gates pass and the opportunity remains fresh.

### Exit conditions
Exit on fill, invalidation, stop-loss, timeout, or risk breach.

### Position sizing methodology
Size by risk budget, liquidity, and expected net edge.

### Capital allocation rules
Allocate only within strategy budget and exposure limits.

### Risk controls
Reward collapse, lockup risk, smart-contract risk.

### Stop-loss logic
Close or cancel when the configured loss or signal invalidation threshold is reached.

### Take-profit logic
Lock profit when the terminal execution outcome meets the strategy objective.

### Volatility handling
Reduce size, widen filters, or pause when volatility exceeds policy.

### Liquidity requirements
Only trade when depth supports target notional within impact limits.

### Slippage tolerance
Use route-specific maximum slippage and reject violations.

### Gas optimisation rules
Respect gas ceilings, fee replacement policy, and chain-specific fee guidance.

### MEV considerations
Use protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Supported chains and protocols only.

### Supported DEXs
Configured DEXs only.

### Required market data
Reward, lockup, APR, risk score.

### AI interaction
AI may rank, explain, or summarize but cannot override hard strategy gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, timestamps, and final outcome records.

### Monitoring metrics
Candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Realized edge, fill success, and execution latency.

### Failure scenarios
Stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Reallocate on program change or exit window.

### Known limitations
Performance depends on liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through documented interfaces.

## Dollar-Cost Averaging

### Business objective
Accumulate exposure over time with deterministic sizing.

### Strategy overview
Dollar-Cost Averaging is implemented as a deterministic, policy-gated trading strategy with explicit entry/exit and lifecycle rules.

### Mathematical model or decision logic
Execute fixed schedule-based orders.

### Required market conditions
Approved schedule and budget.

### Entry conditions
All hard gates pass and the opportunity remains fresh.

### Exit conditions
Exit on fill, invalidation, stop-loss, timeout, or risk breach.

### Position sizing methodology
Size by risk budget, liquidity, and expected net edge.

### Capital allocation rules
Allocate only within strategy budget and exposure limits.

### Risk controls
Unexpected volatility, risk halt.

### Stop-loss logic
Close or cancel when the configured loss or signal invalidation threshold is reached.

### Take-profit logic
Lock profit when the terminal execution outcome meets the strategy objective.

### Volatility handling
Reduce size, widen filters, or pause when volatility exceeds policy.

### Liquidity requirements
Only trade when depth supports target notional within impact limits.

### Slippage tolerance
Use route-specific maximum slippage and reject violations.

### Gas optimisation rules
Respect gas ceilings, fee replacement policy, and chain-specific fee guidance.

### MEV considerations
Use protected submission or reject routes with unacceptable MEV exposure.

### Supported chains
Supported chains/venues only.

### Supported DEXs
Configured DEXs only.

### Required market data
Schedule, price, risk state.

### AI interaction
AI may rank, explain, or summarize but cannot override hard strategy gates.

### Runtime workflow
Detect -> score -> validate -> size -> approve -> execute -> monitor -> reconcile.

### State machine
Idle -> Candidate -> Approved -> Submitted -> Filled | Failed | Cancelled -> Reconciled.

### IPC interactions
Opportunity, plan, order, transaction, and alert events.

### Database persistence
Persist scores, plans, fills, timestamps, and final outcome records.

### Monitoring metrics
Candidate rate, approval rate, fill rate, latency, slippage, and error rate.

### Alert thresholds
Alert on repeated invalidations, stale inputs, or repeated execution failures.

### Backtesting methodology
Replay historical input snapshots against the same deterministic rules.

### Simulation scenarios
Thin liquidity, gas spikes, failures, and adverse price movement.

### Stress testing
Increase latency, reduce depth, and inflate fees to verify abort logic.

### Performance metrics
Realized edge, fill success, and execution latency.

### Failure scenarios
Stale quotes, route failure, reorg, wallet failure, and rejection.

### Recovery behaviour
Continue per schedule unless halted.

### Known limitations
Performance depends on liquidity, latency, and venue reliability.

### Extension points
Add route scorers, signal filters, and AI ranking hooks only through documented interfaces.

## Cross-references
- `RISK-ENGINE.md`
- `AI-PIPELINE.md`
- `EXECUTION-ENGINE.md`
- `MARKET-INTELLIGENCE.md`
- `SIMULATION-ENGINE.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Required details
- Define per-strategy assumptions, inputs, outputs, and execution constraints.

## Strategy rules
- Define strategy inputs, outputs, assumptions, and execution constraints.
- Define per-strategy validation and failure behavior.
