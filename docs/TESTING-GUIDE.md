# APEX Testing Guide

> **Version:** 1.0.0 | **Last Updated:** July 25, 2026 | **Scope:** Unit, Integration, E2E, Contract, and Packaging Tests

---

## 1. Overview

APEX needs a layered test strategy because it combines desktop security boundaries, local persistence, AI provider abstraction, and blockchain execution flows. A single test style is not sufficient.

---

## 2. Test Pyramid

| Layer | Primary Tools | Purpose |
|------|---------------|---------|
| Unit | Vitest | pure logic, schema validation, utility behaviour |
| Integration | Vitest + test DB + mocked services | service boundaries, repositories, IPC handlers |
| E2E UI | Playwright + Electron | real user flows through packaged or near-packaged app |
| Contract/Chain | Hardhat | smart contracts, fork-based execution checks |
| Release smoke | CI packaging scripts | installer/build/update validation |

---

## 3. Repository Test Layout

Recommended structure:

```text
packages/
  desktop/
    src/
    electron/
    tests/
      unit/
      integration/
      e2e/
  ai/
    tests/
  strategies/
    tests/
  contracts/
    test/
```

---

## 4. Unit Testing with Vitest

### 4.1 Target Areas

- config validators
- provider adapters
- strategy profit calculations
- risk scoring functions
- repository mapping helpers
- cache eviction rules

### 4.2 Example

```ts
import { describe, it, expect } from 'vitest';
import { netProfit } from '../net-profit';

describe('netProfit', () => {
  it('subtracts gas and fees from gross profit', () => {
    expect(netProfit(100, 10, 5)).toBe(85);
  });
});
```

Unit tests should remain fast, deterministic, and free of external I/O whenever possible.

---

## 5. Integration Testing

### 5.1 Scope

Integration tests should validate interactions between modules, not just isolated functions.

Examples:

- IPC handler + validation schema + repository write
- provider adapter + response parser + cache layer
- strategy output + risk-engine approval flow
- settings save + encrypted storage path

### 5.2 Database Strategy

Use an isolated SQLite test database per suite or in-memory mode when possible.

Recommended rules:

- run migrations before each suite
- clean tables between tests
- seed deterministic fixture data

---

## 6. Testing IPC Handlers

Each IPC handler should be tested for:

- valid request returns typed success
- invalid payload returns `IPC_ERROR_VALIDATION`
- missing entity returns `IPC_ERROR_NOT_FOUND`
- handler never leaks secret-bearing fields

Mock Electron primitives where direct runtime dependency makes tests brittle, but keep at least one integration path close to the real handler wiring.

---

## 7. Testing AI Provider Adapters

### 7.1 Required Cases

- OpenAI-compatible request mapping
- Anthropic request mapping
- streaming chunk assembly
- tool call normalisation
- schema failure and repair retry
- fallback provider selection

### 7.2 Mocking Guidance

- mock HTTP responses with representative provider payloads
- include malformed and partial responses
- test rate-limit handling and retry backoff without real sleep where possible

---

## 8. Strategy and Risk Testing

Strategies should be tested with deterministic market fixtures.

Representative cases:

- profitable path accepted
- gross profit erased by fees
- insufficient liquidity path rejected
- stale market data rejected
- confidence/risk thresholds block marginal opportunity

Risk engine tests should cover exposure caps, drawdown halts, and circuit breaker triggers.

---

## 9. Playwright End-to-End Testing

### 9.1 Scope

Use Playwright to validate real user flows through the renderer and preload surface.

Critical flows:

- first launch
- provider setup
- settings persistence
- skill toggle
- trade history display
- error banner and degraded mode handling

### 9.2 Recommended Pattern

- launch Electron in test mode
- seed deterministic DB state
- interact through visible UI only
- collect screenshots on failure

### 9.3 Stability Rules

- avoid timing-based assertions where state-based assertions are possible
- disable nonessential animations in test mode if they create flakiness
- isolate tests from live external providers

---

## 10. Hardhat and Mainnet-Fork Testing

### 10.1 Contract Test Scope

- flash-loan receiver correctness
- swap execution correctness
- access control and pause paths
- profit distribution invariants

### 10.2 Mainnet-Fork Use Cases

- validate adapter logic against real ABIs and pool state
- simulate route execution under realistic liquidity conditions
- replay known opportunities and failures

Representative command pattern:

```bash
npx hardhat test
npx hardhat node --fork <RPC_URL>
```

Fork tests should be tagged separately because they are heavier and may rely on premium RPC access.

---

## 11. Coverage Expectations

| Layer | Target |
|------|--------|
| Unit | 80%+ on critical logic |
| Integration | 60%+ on service boundaries |
| E2E | 100% on critical operator flows |
| Contracts | full coverage on privileged and loss-bearing paths |

Coverage is not the goal by itself, but low coverage on financial or security-critical paths is unacceptable.

---

## 12. CI Strategy

### 12.1 Pull Request

Run:

- lint
- type check
- unit tests
- core integration tests

### 12.2 Main Branch / Merge

Run additionally:

- broader integration suite
- packaged-build smoke test
- desktop security assertions

### 12.3 Nightly / Scheduled

Run:

- Playwright suite
- mainnet-fork tests
- dependency vulnerability scan
- update-path smoke test

---

## 13. Fixtures and Test Data

Recommended fixture categories:

- provider configs
- wallet records with mock encrypted blobs
- synthetic opportunities and trades
- market snapshots
- chain adapter response fixtures
- malformed provider response fixtures

Keep fixtures minimal but realistic.

---

## 14. Regression Testing

Every production incident or major bug should yield:

- a minimal repro fixture
- a regression test
- a changelog entry if externally relevant

This is especially important for false-positive opportunities, unsafe risk approvals, and renderer/main boundary mistakes.

---

## 15. Release Validation

Before a release candidate is accepted:

- packaged Windows build launches
- DB migrations succeed on upgrade path
- update metadata is valid
- tray and window actions work
- no security flags regress in packaged Electron build

---

Testing in APEX is not only about correctness in isolated functions. It is the mechanism that prevents unsafe execution paths, broken desktop boundaries, and drift between documentation and implementation.

## Cross-references
- `SIMULATION-ENGINE.md`
- `BACKTESTING.md`
- `STRATEGIES.md`
- `AI-PIPELINE.md`
- `RUNTIME-OPERATIONS.md`
- `MONITORING-OBSERVABILITY.md`
