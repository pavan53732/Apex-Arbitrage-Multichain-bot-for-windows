# Healthchecks

## Document type
This document is an overview, reference, or index as noted below.

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

## Checks
- Define healthcheck cadence, threshold, and fail-closed behavior.
- Include RPC, wallet, backend, UI bridge, and Windows network checks.

## Check rules
- Define actual checks, thresholds, cadence, and fail-closed behavior.
- Define alert and recovery outputs.
