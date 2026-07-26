# Strategies

## Purpose
This document is the authoritative implementation specification for every supported trading strategy.

## Shared strategy contract
Every strategy must define business objective, market conditions, entry and exit conditions, position sizing, capital allocation, risk controls, stop-loss, take-profit, volatility handling, liquidity requirements, slippage tolerance, gas optimisation, MEV considerations, supported chains, supported DEXs, required market data, AI interaction, runtime workflow, state machine, IPC interactions, database persistence, monitoring metrics, alert thresholds, backtesting, simulation, stress testing, performance metrics, failure scenarios, recovery behavior, known limitations, and extension points.

## Shared lifecycle
Discover -> Evaluate -> Validate -> Size -> Approve -> Execute -> Monitor -> Exit -> Reconcile -> Learn.

## Arbitrage
Business objective: capture temporary price inefficiencies after fees and risk buffers.
Strategy overview: compare equivalent markets across venues and execute paired actions when net edge remains positive.
Mathematical model: net edge = spread - gas - fees - slippage - risk buffer.
Required market conditions: stale or divergent quotes with enough liquidity to fill both legs.
Entry conditions: positive net edge above threshold, route freshness valid, and risk approval granted.
Exit conditions: both legs filled, edge invalidated, timeout, or risk breach.
Position sizing: size to minimum of leg liquidity, wallet capacity, and risk cap.
Capital allocation: reserve capital for fees and execution buffers.
Risk controls: no trade if quote age, liquidity, or volatility exceed limits.
Stop-loss logic: cancel if fill drift exceeds tolerance or edge collapses below threshold.
Take-profit logic: realized on completed hedged pair fill.
Volatility handling: reduce size or reject during fast market moves.
Liquidity requirements: both legs must satisfy minimum depth and fill probability.
Slippage tolerance: explicit maximum delta per leg.
Gas optimisation rules: prefer routes with lower total cost and bounded confirmation delay.
MEV considerations: use protection when route is exposed to sandwich risk.
Supported chains: chain list is configuration driven.
Supported DEXs: configured routeable venues only.
Required market data: price, liquidity, gas, freshness, and route health.
AI interaction: AI may rank candidates but cannot bypass deterministic thresholds.
Runtime workflow: detect -> score -> size -> approve -> execute -> reconcile.
State machine: Candidate -> Approved -> Executing -> Filled -> Reconciled or Rejected or Failed.
IPC interactions: strategy.candidate, strategy.approve.request, strategy.result, strategy.reconcile.
Database persistence: candidate record, execution record, metrics, and outcome.
Monitoring metrics: edge, hit rate, fill rate, gas cost, slippage, latency, and PnL.
Alert thresholds: edge collapse, repeated rejects, or settlement failure.
Backtesting methodology: replay historical quotes and measure realized net edge after costs.
Simulation scenarios: quote divergence, gas spike, partial fill, reorg, stale data.
Stress testing: volatility shock, liquidity shock, and latency injection.
Performance metrics: Sharpe-like return on capital, fill rate, and average net profit.
Failure scenarios: stale quotes, route failure, partial fill, and nonce contention.
Recovery behavior: reconcile or cancel open legs and prevent duplicate re-entry.
Known limitations: dependent on liquidity and finality; not guaranteed in fragmented markets.
Extension points: multi-hop routes, cross-chain extensions, and AI ranking layers.

## Triangular Arbitrage
Business objective: capture mispricing across three convertable legs within one venue or route set.
Strategy overview: cycle through three assets and exploit non-equilibrium exchange rates.
Mathematical model: cycle return = product(exchange rates) - cost basis.
Required market conditions: stable enough quote topology and sufficient depth across all legs.
Entry conditions: cycle return above threshold with fresh quotes.
Exit conditions: completed cycle, return decay, or route invalidation.
Position sizing: limited by weakest leg liquidity.
Capital allocation: keep reserve for fee and slippage uncertainty.
Risk controls: reject if any leg freshness or depth is insufficient.
Stop-loss logic: cancel if the cycle cannot complete within time or risk limits.
Take-profit logic: realized when loop completes profitably.
Volatility handling: reduce exposure when leg volatility widens.
Liquidity requirements: each hop must support minimum depth.
Slippage tolerance: cap per-hop and cumulative slippage.
Gas optimisation rules: select the cheapest valid route that still clears profit.
MEV considerations: route exposure must be minimized.
Supported chains: configured venue chain only unless explicitly cross-chain capable.
Supported DEXs: configured triangular route venues.
Required market data: leg quotes, fees, liquidity, and freshness.
AI interaction: AI can suggest candidates but not approve them.
Runtime workflow: discover cycle -> score -> approve -> execute -> reconcile.
State machine: Candidate -> Approved -> Executing -> Completed or Rejected or Failed.
IPC interactions: strategy.candidate, strategy.reconcile, strategy.fail.
Database persistence: cycle candidate, leg outcomes, and net profit.
Monitoring metrics: cycle return, fill rate, latency, and net PnL.
Alert thresholds: repeated invalid cycles or negative realized edge.
Backtesting methodology: historical cycle replay.
Simulation scenarios: hop failure, quote drift, gas shock, and partial completion.
Stress testing: correlated price movement and latency injection.
Performance metrics: realized cycle profit and completion ratio.
Failure scenarios: one-leg failure, stale quote, and gas spike.
Recovery behavior: revert or reconcile unbalanced leg outcomes.
Known limitations: sensitive to quote freshness and fee drift.
Extension points: cross-chain cycle extension and AI ranking.

## Cross-DEX Arbitrage
Business objective: exploit price differences across DEXs on the same chain.
Strategy overview: compare routes and execute when the net spread exceeds execution cost.
Mathematical model: net profit = spread - gas - slippage - fees.
Required market conditions: competing venues with meaningful depth.
Entry conditions: validated spread and route availability.
Exit conditions: leg completion or invalidation.
Position sizing: bounded by deepest available route liquidity.
Capital allocation: keep fee buffer and safety reserve.
Risk controls: abort on route degradation or depth loss.
Stop-loss logic: cancel on spread collapse or adverse slippage.
Take-profit logic: realized on hedged completion.
Volatility handling: require larger spread during high volatility.
Liquidity requirements: minimum depth on both venues.
Slippage tolerance: explicit route tolerance.
Gas optimisation rules: use gas-aware route ranking.
MEV considerations: protection required for exposed routes.
Supported chains: chain-specific DEX set.
Supported DEXs: venue whitelist from configuration.
Required market data: venue quotes, depth, gas, and freshness.
AI interaction: AI may prioritize venue pairs.
Runtime workflow: detect -> validate -> size -> execute -> reconcile.
State machine, IPC, database, monitoring, alerting, backtesting, simulation, stress, failure, recovery, limitations, extension points follow the shared strategy contract.

## Cross-Chain Arbitrage
Business objective: capture cross-chain price dislocations.
Strategy overview: compare assets across chains and account for bridge latency and finality.
Mathematical model: net profit = spread - bridge cost - gas - slippage - delay risk.
Required market conditions: sufficient cross-chain liquidity and stable bridge health.
Entry conditions: positive net edge with bridge and chain health acceptance.
Exit conditions: successful settlement or cancellation before risk expires.
Position sizing: conservative due to settlement risk.
Capital allocation: reserve capital for bridge and timeout risk.
Risk controls: stricter finality and delay thresholds.
Stop-loss logic: abort if bridge or finality risk increases.
Take-profit logic: settled cross-chain profit realization.
Volatility handling: reduce size under high volatility or chain instability.
Liquidity requirements: both source and destination chains need viable liquidity.
Slippage tolerance: per-chain and bridge-aware tolerance.
Gas optimisation rules: optimize both source and destination fees.
MEV considerations: consider exposure on both chains.
Supported chains: configurable chain pair set.
Supported DEXs: chain-local venue whitelist.
Required market data: cross-chain price, bridge state, gas, and finality.
AI interaction: AI may rank but not override finality rules.
Runtime workflow: detect -> bridge-check -> size -> execute -> reconcile.
Known limitations: dependent on bridge and finality assumptions.

## Flash Loan Arbitrage
Business objective: use atomic borrowed capital to capture transient inefficiencies.
Strategy overview: borrow, trade, repay, and retain only atomic profit.
Mathematical model: profit = output - repayment - fees - gas.
Required market conditions: atomic execution support and sufficient spread.
Entry conditions: guaranteed repayment path and profitable atomic route.
Exit conditions: atomic completion or full revert.
Position sizing: constrained by flash loan limits and route liquidity.
Capital allocation: no persistent capital commitment beyond fees.
Risk controls: hard revert on any unmet repayment condition.
Stop-loss logic: transaction reverts atomically.
Take-profit logic: atomic residual profit only.
Volatility handling: can be aggressive only when atomic path remains valid.
Liquidity requirements: route must absorb loan size.
Slippage tolerance: strict atomic limit.
Gas optimisation rules: prioritize successful atomic completion.
MEV considerations: protect bundle exposure.
Supported chains: chains with flash-loan support.
Supported DEXs: venues compatible with atomic bundles.
Required market data: route depth, repayment cost, and gas.
AI interaction: AI may suggest opportunities but not authorize unsafe bundles.
Runtime workflow: detect -> validate -> bundle -> execute -> settle.
Known limitations: only works on supported atomic environments.

## Statistical Arbitrage
Business objective: profit from mean-reverting or statistically anomalous spread behavior.
Strategy overview: model deviation from historical norms and act on statistically significant divergence.
Mathematical model: z-score or equivalent deviation model.
Required market conditions: stable historical distribution and sufficient sample quality.
Entry conditions: deviation above calibrated threshold with liquidity support.
Exit conditions: reversion, threshold breach, or model invalidation.
Position sizing: proportional to confidence and bounded by risk.
Capital allocation: diversified across signals.
Risk controls: regime shift detection and drawdown caps.
Stop-loss logic: exit if deviation worsens or model regime changes.
Take-profit logic: exit on reversion or target convergence.
Volatility handling: model volatility-adjusted thresholds.
Liquidity requirements: enough depth for entry and exit.
Slippage tolerance: scaled to market volatility.
Gas optimisation rules: include cost in expectancy calculation.
MEV considerations: protection when routes are predictable.
Supported chains/DEXs: configured market universe.
Required market data: historical series, spreads, liquidity, and volatility.
AI interaction: AI may adjust ranking features but not thresholds.
Runtime workflow: detect -> score -> size -> execute -> monitor -> exit.
Known limitations: regime shifts reduce model reliability.

## Grid Trading
Business objective: monetize oscillation within a bounded price range.
Strategy overview: deploy layered buy/sell bands around a center price.
Mathematical model: banded mean-reversion grid.
Required market conditions: bounded range and sufficient liquidity.
Entry conditions: range validation and capital availability.
Exit conditions: range break, target profit, or manual stop.
Position sizing: evenly partitioned or weighted by volatility.
Capital allocation: allocate across grid levels with reserve cash.
Risk controls: range break protection and max inventory cap.
Stop-loss logic: exit on breakout beyond tolerance.
Take-profit logic: incremental profit per completed band cycle.
Volatility handling: widen grid or pause when volatility rises.
Liquidity requirements: every band must be executable.
Slippage tolerance: per band tolerance.
Gas optimisation rules: batch actions where possible.
MEV considerations: lower priority than core safety but still accounted for.
Supported chains/DEXs: configurable venue set.
Required market data: band center, volatility, depth, and fees.
AI interaction: AI may tune bands within policy.
Runtime workflow: configure -> activate -> monitor -> rebalance -> exit.
Known limitations: poor fit for strong trends.

## Scalping
Business objective: harvest short-lived micro-edges with rapid turnover.
Strategy overview: enter and exit quickly on tiny favorable deltas.
Mathematical model: micro-edge after costs and latency.
Required market conditions: low latency, tight spreads, and deep route availability.
Entry conditions: edge above threshold with stable route.
Exit conditions: tiny target reached, edge evaporates, or time limit hit.
Position sizing: small and latency-bounded.
Capital allocation: preserve rapid redeployment capital.
Risk controls: strict timeouts and exposure caps.
Stop-loss logic: immediate exit on adverse move.
Take-profit logic: micro-profit target.
Volatility handling: only operate when execution latency is acceptable.
Liquidity requirements: consistent fill probability.
Slippage tolerance: very tight.
Gas optimisation rules: prioritize execution speed and net gain.
MEV considerations: strong protection recommended.
Supported chains/DEXs: low-latency approved venues.
Required market data: microstructure, spread, latency, and gas.
AI interaction: AI may flag candidates but not relax risk.
Runtime workflow: detect -> validate -> execute -> exit.
Known limitations: highly sensitive to latency and fees.

## Momentum
Business objective: capture continuation after directional confirmation.
Strategy overview: trade with trend when momentum remains positive.
Mathematical model: trend confirmation + volume confirmation.
Required market conditions: directional move and supporting participation.
Entry conditions: momentum and trend confirmation.
Exit conditions: momentum decay, reversal, or target hit.
Position sizing: scaled to trend strength and volatility.
Capital allocation: favor confirmed regimes.
Risk controls: trend failure and drawdown limit.
Stop-loss logic: exit on trend reversal.
Take-profit logic: exit on target or momentum exhaustion.
Volatility handling: adapt size to trend volatility.
Liquidity requirements: enough depth for orderly exits.
Slippage tolerance: moderate and trend-aware.
Gas optimisation rules: incorporate trade horizon into fee sensitivity.
MEV considerations: route predictability may require protection.
Supported chains/DEXs: configured market universe.
Required market data: trend, volume, volatility, and liquidity.
AI interaction: AI may rank trend strength.
Runtime workflow: detect -> confirm -> size -> execute -> monitor -> exit.
Known limitations: prone to whipsaws.

## Mean Reversion
Business objective: exploit returns toward a mean after overextension.
Strategy overview: fade extreme deviations when the market is reverting.
Mathematical model: deviation from baseline mean or band.
Required market conditions: identifiable mean and stable distribution.
Entry conditions: overextension with reversion confirmation.
Exit conditions: reversion achieved or invalidation.
Position sizing: confidence and volatility adjusted.
Capital allocation: distributed across signals and reserve kept for adverse moves.
Risk controls: regime shift and trend-break detection.
Stop-loss logic: exit if deviation continues to expand.
Take-profit logic: exit near mean or target zone.
Volatility handling: widen thresholds in volatile regimes.
Liquidity requirements: enough depth to exit cleanly.
Slippage tolerance: bounded by expected reversion profit.
Gas optimisation rules: must remain profitable net of fees.
MEV considerations: protection when predictable.
Supported chains/DEXs: configured universe.
Required market data: mean, deviation, volatility, liquidity.
AI interaction: AI may tune signal weights.
Runtime workflow: detect -> score -> size -> execute -> monitor -> exit.
Known limitations: weak in persistent trends.

## Market Making
Business objective: provide liquidity and earn spread or incentive revenue.
Strategy overview: maintain two-sided quotes while managing inventory risk.
Mathematical model: spread plus inventory risk management.
Required market conditions: stable enough pricing and volume.
Entry conditions: quote conditions and inventory room satisfied.
Exit conditions: inventory limit, risk breach, or program stop.
Position sizing: quote size derived from inventory policy.
Capital allocation: reserve inventory and hedge capacity.
Risk controls: inventory caps and adverse selection controls.
Stop-loss logic: unwind when inventory risk exceeds tolerance.
Take-profit logic: spread capture and incentive realization.
Volatility handling: widen quotes or pause during turbulence.
Liquidity requirements: consistent quote competitiveness.
Slippage tolerance: quote-refresh aware.
Gas optimisation rules: quote update cost must remain acceptable.
MEV considerations: high exposure to adverse selection; protection may be required.
Supported chains/DEXs: configured market making venues.
Required market data: depth, spread, volatility, and order flow.
AI interaction: AI may forecast inventory risk.
Runtime workflow: quote -> monitor -> adjust -> hedge -> exit.
Known limitations: adverse selection and inventory imbalance.

## Liquidity Provision
Business objective: earn incentives and fees by supplying capital to pools.
Strategy overview: allocate capital to pools with acceptable reward and risk profile.
Mathematical model: expected return minus impermanent loss and gas.
Required market conditions: adequate pool demand and incentive yield.
Entry conditions: pool health, reward, and risk threshold satisfied.
Exit conditions: reward decay, risk increase, or target achieved.
Position sizing: based on pool depth, IL exposure, and capital budget.
Capital allocation: diversified across pools.
Risk controls: impermanent loss, pool health, and protocol risk limits.
Stop-loss logic: exit on adverse pool conditions or risk limit breach.
Take-profit logic: yield accumulation and rebalancing profit.
Volatility handling: reduce size in unstable regimes.
Liquidity requirements: pool must remain deep enough for intended capital.
Slippage tolerance: pool entry and exit bounds.
Gas optimisation rules: include add/remove-liquidity costs.
MEV considerations: pool actions may be exposed to MEV.
Supported chains/DEXs: configured pool venues.
Required market data: pool fees, depth, incentives, and volatility.
AI interaction: AI may rank pools by reward-to-risk.
Runtime workflow: evaluate -> allocate -> monitor -> rebalance -> exit.
Known limitations: impermanent loss and protocol risk.

## Yield Farming
Business objective: maximize reward yield from protocol incentives.
Strategy overview: deploy capital to yield-bearing mechanisms subject to risk gating.
Mathematical model: reward yield minus protocol and gas costs.
Required market conditions: attractive incentives and acceptable protocol risk.
Entry conditions: reward threshold and safety checks pass.
Exit conditions: reward decay, incentive end, or risk change.
Position sizing: incentive and risk adjusted.
Capital allocation: limited by protocol and strategy cap.
Risk controls: exploit, contract, and reward volatility risk checks.
Stop-loss logic: exit on protocol or reward deterioration.
Take-profit logic: reward realization and compounding policy.
Volatility handling: reduce allocation when underlying assets become unstable.
Liquidity requirements: underlying assets must remain redeemable within policy.
Slippage tolerance: bounded by entry/exit cost.
Gas optimisation rules: only deploy when net expected yield is positive after fees.
MEV considerations: if deployed via predictable paths, protection may be needed.
Supported chains/DEXs: configured protocol universe.
Required market data: reward rates, protocol risk, liquidity, and volatility.
AI interaction: AI may suggest allocations only within policy.
Runtime workflow: evaluate -> allocate -> monitor -> harvest -> exit.
Known limitations: incentive decay and protocol risk.

## Dollar-Cost Averaging
Business objective: accumulate exposure steadily over time.
Strategy overview: place periodic trades regardless of short-term noise.
Mathematical model: scheduled purchase logic.
Required market conditions: valid budget and enabled schedule.
Entry conditions: schedule trigger and safety checks pass.
Exit conditions: schedule end, manual stop, or risk halt.
Position sizing: fixed amount or policy-driven amount per interval.
Capital allocation: reserved by schedule.
Risk controls: budget cap and market-halt logic.
Stop-loss logic: pause on severe risk events.
Take-profit logic: not primary; realized via later portfolio appreciation.
Volatility handling: schedule may continue while sizing is constant or adapted by policy.
Liquidity requirements: enough liquidity to place scheduled trade.
Slippage tolerance: standard tolerance configured per asset.
Gas optimisation rules: align with predictable schedule windows.
MEV considerations: lower than high-frequency strategies but still relevant.
Supported chains/DEXs: configured buying venues.
Required market data: price, liquidity, and schedule data.
AI interaction: AI may suggest timing adjustments, but schedule policy prevails.
Runtime workflow: schedule -> trigger -> buy -> record -> repeat.
Known limitations: not designed for short-term alpha.

## Swing Trading
Business objective: capture medium-horizon directional moves.
Strategy overview: hold positions for multiple sessions while trend persists.
Mathematical model: trend and regime model.
Required market conditions: directional bias and acceptable volatility.
Entry conditions: trend confirmation and risk approval.
Exit conditions: target, reversal, or holding-period breach.
Position sizing: based on confidence and volatility.
Capital allocation: limit per trade and portfolio exposure.
Risk controls: regime shift and drawdown controls.
Stop-loss logic: exit on trend invalidation.
Take-profit logic: target or trailing exit.
Volatility handling: adjust size or hold period.
Liquidity requirements: enough depth for planned exit.
Slippage tolerance: moderate.
Gas optimisation rules: ensure holding horizon still justifies transaction cost.
MEV considerations: route predictability considered.
Supported chains/DEXs: configured venue set.
Required market data: trend, volatility, and liquidity.
AI interaction: AI may rank momentum quality.
Runtime workflow: screen -> enter -> monitor -> exit.
Known limitations: exposes capital to regime shifts.

## AI-assisted Strategies
Business objective: use AI to improve ranking, feature weighting, or candidate selection without bypassing deterministic policy.
Strategy overview: AI acts as a decision aid, not an authority.
Mathematical model: AI score combined with deterministic risk filters.
Required market conditions: valid candidate pool and available model context.
Entry conditions: candidate passes hard risk rules and AI score exceeds threshold.
Exit conditions: model rejection, risk change, or candidate expiry.
Position sizing: policy capped regardless of AI confidence.
Capital allocation: always constrained by deterministic limits.
Risk controls: AI cannot override safety or wallet rules.
Stop-loss logic: same as underlying strategy plus AI confidence decay.
Take-profit logic: same as underlying strategy.
Volatility handling: AI may reduce confidence under turbulence.
Liquidity requirements: same as underlying strategy.
Slippage tolerance: same as underlying strategy.
Gas optimisation rules: same as underlying strategy.
MEV considerations: same as underlying strategy.
Supported chains/DEXs: same as underlying strategy.
Required market data: all strategy inputs plus model context.
AI interaction: direct but non-authoritative.
Runtime workflow: detect -> score -> validate -> act or reject.
Known limitations: model drift and explainability constraints.

## Hybrid Strategies
Business objective: combine multiple strategy archetypes under one controlled policy.
Strategy overview: compose sub-strategies with explicit precedence and conflict rules.
Mathematical model: weighted or rule-based composition.
Required market conditions: depends on underlying components.
Entry conditions: all mandatory sub-strategy gates must pass.
Exit conditions: any stop condition from a controlling sub-strategy or overall risk policy.
Position sizing: the tighter of sub-strategy sizes and global caps.
Capital allocation: partitioned by component policy.
Risk controls: conflict resolution and portfolio exposure caps.
Stop-loss logic: immediate if any required risk gate fails.
Take-profit logic: aggregate or component-based realization.
Volatility handling: strategy-specific controls combined conservatively.
Liquidity requirements: all active components must be executable.
Slippage tolerance: most conservative applicable threshold.
Gas optimisation rules: route based on combined cost model.
MEV considerations: according to the most exposed component.
Supported chains/DEXs: union of component-approved venues.
Required market data: union of component inputs.
AI interaction: AI may tune weights only within bounds.
Runtime workflow: evaluate components -> resolve conflict -> execute -> monitor -> unwind.
Known limitations: complexity and explainability decrease as composition grows.
