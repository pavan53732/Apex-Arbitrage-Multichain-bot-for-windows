# Healthchecks

## Purpose
Defines the concrete health checks that prove the system is ready to trade.

## Health checks
- RPC connectivity.
- Exchange connectivity.
- Wallet readiness.
- Service availability.
- UI/backend bridge health.
- Windows network and proxy health.

## Failure handling
- Any critical failure must block autonomous trading.
- Health failures must publish alerts and recovery actions.

## Required details
- Define concrete checks and thresholds.
