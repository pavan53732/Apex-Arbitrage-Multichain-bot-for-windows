# Rpc Manager

## Document type
This document is an overview, reference, or index as noted below.

# RPC Manager

## Purpose
Authoritative owner for rpc manager.

## Scope
Cross-cutting platform governance.

## Responsibilities
Define ownership, contracts, lifecycle, validation, and cross-references.

## Cross-references
- `APEX-OS.md`
- `ARCHITECTURE.md`

## Operational Contract
Defines provider pool management, health, rotation, failover, latency, routing, and rate-limit handling.

## Example
A slow RPC endpoint is rotated out after repeated latency breaches.

## Required details
- Define endpoint config, websocket support, retry, and proxy handling.
- Define failover and custom RPC registration.

## RPC contract
- Define endpoint registration, websocket support, retry policy, and proxy handling.
- Define failover, health scoring, and custom endpoint validation.
