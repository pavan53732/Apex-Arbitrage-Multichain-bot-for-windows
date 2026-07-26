# Chain Integration

## Document type
This document is an overview, reference, or index as noted below.

# APEX Chain Integration Guide

> **Version:** 3.0.0 | **Last Updated:** July 25, 2026
> **Scope:** Adding a new EVM-compatible chain to APEX.

---

## 1. Overview

APEX is **chain-agnostic by design**. Every supported chain is an adapter
implementing a common interface. Adding a new chain is a focused, well-defined
process.

A chain adapter provides:
- RPC connection (HTTP + WebSocket)
- Block / gas / price queries
- Native token info
- Token registry (curated + on-demand)
- DEX registry (which DEXes are deployed on this chain)
- Bridge registry (which bridges serve this chain)
- Flash loan provider support (if available)
- Explorer URL builder
- Contract deployment addresses for APEX's own contracts

---

## 2. Supported Chains (v3.0)

| Chain | ID | Type | Status |
|-------|----|----|--------|
| Ethereum | 1 | L1 | ✅ Supported |
| BNB Chain | 56 | L1 | ✅ Supported |
| Polygon | 137 | Sidechain | ✅ Supported |
| Arbitrum | 42161 | Optimistic L2 | ✅ Supported |
| Optimism | 10 | Optimistic L2 | ✅ Supported |
| Base | 8453 | Optimistic L2 | ✅ Supported |
| Avalanche C-Chain | 43114 | L1 | 🟡 v3.1 |
| Sonic | 146 | L1 | 🟡 v3.1 |
| Linea | 59144 | ZK L2 | 🟡 v3.1 |
| zkSync Era | 324 | ZK L2 | 🟡 v3.1 |
| Scroll | 534352 | ZK L2 | 🟡 v3.1 |
| Mantle | 5000 | Optimistic L2 | 🟡 v3.1 |
| Gnosis | 100 | Sidechain | 🟡 v3.1 |
| Celo | 42220 | L1 | 🟡 v3.1 |

---

## 3. Adding a New Chain

### 3.1 Prerequisites
- Chain is EVM-compatible (any chain running an EVM fork works)
- You have at least one reliable public RPC URL (HTTP + WSS)
- You have the block explorer base URL
- You know the native token (symbol, decimals, coingecko ID)
- You know which DEXes / bridges are deployed

### 3.2 Create the Chain Definition

Create `packages/chains/src/chains/<chain-name>.ts`:

```ts
import { defineChain } from '../types';

export const myChain = defineChain({
  // Identity
  chain_id: 12345,
  name: 'My Chain',
  short_name: 'mychain',
  slug: 'mychain',
  is_testnet: false,
  family: 'evm',

  // Native token
  native_token: {
    symbol: 'MYC',
    name: 'My Chain Token',
    decimals: 18,
    coingecko_id: 'my-chain',
  },

  // RPC
  rpc_urls: {
    primary: 'https://rpc.mychain.io',
    fallback: ['https://rpc2.mychain.io', 'https://rpc3.mychain.io'],
    websocket: 'wss://ws.mychain.io',
  },

  // Block / gas
  block_time_ms: 2000,
  gas_token: 'MYC',  // usually the native token
  eip_1559: true,
  gas_oracle_url: 'https://gas.mychain.io/api/v1/gas',  // optional, falls back to eth_gasPrice

  // Explorer
  explorer: {
    name: 'MyScan',
    url: 'https://myscan.io',
    api_url: 'https://api.myscan.io/api',  // optional
    api_key_env: 'MYSCAN_API_KEY',         // optional, reads from env
  },

  // DEX registry
  dexe: ['uniswap-v3', 'sushiswap'],  // from packages/dex-registry

  // Bridge registry
  bridges: ['stargate', 'layerzero'],  // from packages/bridge-registry

  // Flash loan providers
  flash_loan_providers: ['aave-v3'],  // empty if none

  // APEX contract addresses (after deployment)
  contracts: {
    flash_loan_receiver: '0x...',
    swap_executor: '0x...',
    profit_distributor: '0x...',
  },

  // Token registry defaults
  common_tokens: [
    { symbol: 'USDC', address: '0x...', decimals: 6 },
    { symbol: 'USDT', address: '0x...', decimals: 6 },
    { symbol: 'WETH', address: '0x...', decimals: 18 },
  ],

  // Misc
  features: {
    eip_1559: true,
    eip_2930: true,
    eip_4844: false,
    multicall3: '0x...',  // if deployed
  },
});
```

### 3.3 Register the Chain

Edit `packages/chains/src/index.ts`:
```ts
import { myChain } from './chains/mychain';

export const supportedChains = [
  // ... existing
  myChain,
];
```

### 3.4 Verify

```bash
npm run test -- --grep "mychain"
```

The test suite includes:
- RPC connectivity check
- Block number fetch
- Gas estimation
- Token balance query
- Multicall3 call (if deployed)
- Explorer link generation

### 3.5 UI

The chain auto-appears in:
- Status bar (chain health)
- AI Configuration → chains dropdown
- Skills → chains filter
- Settings → chains page
- Opportunities view

No UI code changes needed.

---

## 4. The ChainAdapter Interface

Every chain implements `ChainAdapter` (`packages/chains/src/types.ts`):

```ts
interface ChainAdapter {
  // Identity
  readonly definition: ChainDefinition;

  // Connection
  getProvider(): JsonRpcProvider;
  getWebSocketProvider(): WebSocketProvider;
  isHealthy(): Promise<boolean>;
  getBlockNumber(): Promise<number>;

  // Gas
  getGasPrice(): Promise<bigint>;
  estimateGas(tx: TransactionRequest): Promise<bigint>;
  getEip1559Fees(): Promise<{ maxFeePerGas: bigint; maxPriorityFeePerGas: bigint }>;

  // Tokens
  getTokenBalance(token: string, holder: string): Promise<bigint>;
  getTokenInfo(address: string): Promise<TokenInfo>;
  getMulticall3Result(calls: MulticallCall[]): Promise<MulticallResult[]>;

  // DEX (delegated to packages/dex-registry)
  getDexes(): DexAdapter[];

  // Bridges (delegated to packages/bridge-registry)
  getBridges(): BridgeAdapter[];

  // Flash loans
  getFlashLoanProviders(): FlashLoanProvider[];

  // Explorer
  txUrl(hash: string): string;
  addressUrl(addr: string): string;
  tokenUrl(addr: string): string;

  // APEX contracts
  getApexContracts(): { flashLoanReceiver: string; swapExecutor: string; profitDistributor: string };
}
```

---

## 5. RPC Management

### 5.1 Health & Failover
- APEX monitors RPC latency every 30s
- On `eth_blockNumber` failure: mark unhealthy, try fallback
- If all fail: mark chain degraded; skills depending on this chain go into cooldown
- UI shows chain health in status bar

### 5.2 WebSocket Subscriptions
- One persistent WS per chain for newHeads
- Subscribed per-skill for events (Swaps, Transfers, etc.)
- Auto-reconnect with exponential backoff

### 5.3 Rate Limiting
- Per-RPC rate limiter (token bucket, configurable per chain)
- Default: 100 req/s
- Free public RPCs often have lower limits; APEX surfaces this in Diagnostics

### 5.4 Private RPCs
Users can add their own RPC URLs in **Settings → Chains → [chain] → Custom RPC**:
- Higher rate limits
- Higher reliability
- Used as primary if set; fallbacks kept for resilience

---

## 6. Token Registry

### 6.1 Built-in
Each chain ships with a curated list of `common_tokens` (USDC, USDT, WETH, etc.)

### 6.2 User-added
Users can add custom tokens via:
- **Settings → Chains → [chain] → Add Token** (manual entry)
- **Paste a token contract address** in the trade form (auto-fetched)

### 6.3 Auto-discovery
For some chains, APEX can scan the top pools and discover traded tokens:
**Settings → Chains → [chain] → Auto-discover tokens**

Discovered tokens are added to a `discovered_tokens` table, queryable, and
can be promoted to the user's personal list.

---

## 7. Flash Loan Providers

If the chain has Aave V3, Spark, or similar:
1. Add the provider to the chain's `flash_loan_providers` list
2. APEX automatically includes it in `flash-loan-arb` skill
3. Test the flash loan via `scripts/test-flash-loan.ts`

If no flash loan provider exists on the chain, the `flash-loan-arb` skill
is hidden for that chain.

---

## 8. Bridges

Cross-chain requires bridges. See `packages/bridge-registry`. Each bridge
adapter provides:
- Quote function
- Send function
- Status tracker
- Supported chains
- Supported tokens

To add a chain to a bridge:
1. Verify the bridge supports the chain
2. Add the chain ID to the bridge's `supported_chains`
3. Test a small transfer

---

## 9. Deploying APEX Contracts to a New Chain

APEX's on-chain contracts (FlashLoanReceiver, SwapExecutor, ProfitDistributor)
must be deployed to the new chain before execution skills work there.

Steps:
1. `cd packages/contracts`
2. `npx hardhat run scripts/deploy.ts --network mychain`
3. Note the deployed addresses
4. Update `packages/chains/src/chains/mychain.ts` with the addresses
5. Verify on explorer

For some chains, a multi-sig owns the contract upgradeability; follow the
governance process.

---

## 10. Testing

### 10.1 Unit Tests
- `packages/chains/test/<chain>.test.ts`
- Mocks the RPC provider
- Tests all interface methods

### 10.2 Integration Tests (Mainnet Fork)
```bash
FORK_RPC=<fork-rpc-url> npm run test:fork -- --chain=mychain
```
Forks the chain at a recent block, runs real skill executions, asserts
expected outcomes.

### 10.3 Live Testnet
For pre-mainnet:
- Deploy APEX contracts to testnet
- Add testnet RPC to chain definition (`is_testnet: true`)
- Run skills against small test trades

---

## 11. Monitoring

Per-chain metrics surfaced in **Dashboard → Chains**:
- Block height (and drift vs expected)
- Gas price (current, p50, p95)
- RPC latency (primary + fallbacks)
- Number of opportunities found (last 24h)
- Number of trades executed (last 24h)
- Total gas spent (last 24h)

---

## 12. Common Pitfalls

- **Wrong chain ID** — the `chain_id` is the EVM `CHAIN_ID` opcode value, not an arbitrary index
- **Wrong native token decimals** — most are 18, but some are not (e.g. Celo native)
- **Missing EIP-1559 support** — some L2s have non-standard fee markets; check carefully
- **Multicall3 not deployed** — if not, APEX falls back to sequential calls (slower but works)
- **Flash loan not available** — many L2s lack the major flash loan providers
- **Bridge liquidity** — having a bridge "supported" is not enough; check actual liquidity

---

## 13. Chain Deprecation

When a chain is no longer viable (low liquidity, abandoned, exploited):
1. Mark `deprecated: true` in the chain definition
2. UI shows a "Deprecated" badge
3. Existing skills continue to work (so users aren't surprised)
4. New skill enabling for the chain is disabled
5. After 90 days, chain is removed from default `supportedChains` list (users with the chain in their config keep it)

---

*Adding a chain should be a focused PR. Use the testnet first, then mainnet, then community announcement.*

## Cross-references
- `TRANSACTION-LIFECYCLE.md`
- `ROUTING-ENGINE.md`
- `WALLET-MANAGEMENT.md`
- `GAS-OPTIMISATION.md`
- `MONITORING-OBSERVABILITY.md`
- `DATABASE-SCHEMA.md`
- `CHAIN-REGISTRY.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
