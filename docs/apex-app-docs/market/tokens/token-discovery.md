---
metadata_schema_version: 1.0
document_id: DOC-0331
title: Token Discovery
plane: Product Specification
domain: Market
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.1.0
canonical_source: docs/apex-app-docs/market/tokens/token-discovery.md
related_concepts:
  - CONCEPT-0331
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Market
type: REFERENCE
purpose: Token Discovery documentation.
scope: Reference documentation.
---

# Token Discovery

## Document type
Document type: [CONTRACT]

## Purpose
Defines token lookup, discovery sources, validation, enrichment, and registry synchronization.

## Discovery sources
- On-chain metadata and DEX pool listings.
- Token registry change events.
- Strategy and pair discovery requirements.

## Discovery rules
- Discovery runs on a defined cadence and on refresh triggers such as new pools or registry changes.
- A discovered token is validated before promotion: symbol, contract address, chain, and decimals.
- Enrichment adds metadata (name, display, wrapped/native relationship) from verified sources.
- Cache invalidation follows the refresh cadence; a cached token older than the window is refetched.
- Promoted tokens are synchronized into the token registry with a candidate-to-active transition.

## Validation gates
- A token without a verifiable contract address is rejected.
- A token with unknown decimals is rejected until verified.
- Chain association must resolve in the chain registry.
- Duplicate symbols across chains are allowed; identity is address plus chain.

## Enrichment
- Metadata is enriched only from verified sources; an unverified value is omitted, not guessed.
- Provenance is recorded for every enriched field.

## Refresh and cache
- A cached token older than the refresh window is refetched before use.
- Cache invalidation follows the refresh cadence and registry change events.

## Output
- Promoted tokens are synchronized into the token registry with a candidate-to-active transition.
- Discovery output is deterministic for the same inputs.
- Tokens rejected at validation are recorded with their reason.
- Discovery feeds pair discovery and opportunity detection with validated tokens only.
- Discovery configuration changes are validated before activation.
- Registry synchronization is idempotent; re-promotion is safe.
- A source outage is flagged; discovery continues from remaining sources.

## Cross-references
- `../core/market-data.md`
- `../core/market-intelligence.md`
- `../registries/token-registry.md`
- `./pair-discovery.md`

## Operational Contract

This document owns token discovery, validation, enrichment, and registry synchronization. Token identity is owned by the token registry; this document feeds it with validated candidates.

## Example
A discovered token is validated before being promoted into the token registry; a token with unknown decimals is rejected until verified.
