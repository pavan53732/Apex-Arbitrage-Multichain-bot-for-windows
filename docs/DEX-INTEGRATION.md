# APEX DEX Integration Guide

> **Version:** 3.0.0 | **Last Updated:** July 25, 2026
> **Scope:** Adding a new DEX (decentralized exchange) adapter to APEX.

---

## 1. Overview

A DEX adapter gives APEX the ability to:
- Read pool reserves and prices
- Simulate swaps (quote)
- Build swap transactions
- (Optional) Execute swaps

APEX supports a growing list of DEXes. Each DEX type (AMM, order book,
concentrated liquidity) has its own adapter pattern.

---

## 2. Supported DEXes (v3.0)

| DEX | Type | Chains | Adapter |
|-----|------|--------|---------|
| Uniswap V2 | Constant product AMM | Most EVM | `uniswap-v2` |
| Uniswap V3 | Concentrated liquidity | Most EVM | `uniswap-v3` |
| SushiSwap | Constant product AMM | Most EVM | `sushiswap` |
| PancakeSwap V2 | Constant product AMM | BNB, ETH, others | `pancakeswap-v2` |
| PancakeSwap V3 | Concentrated liquidity | BNB, ETH, others | `pancakeswap-v3` |
| Curve (StableSwap) | Stable swap | Most EVM | `curve-stableswap` |
| Balancer V2 | Weighted AMM | Most EVM | `balancer-v2` |
| Maverick | Concentrated liquidity | ETH, Base, others | `maverick` |
| Trader Joe V2 | Liquidity book | Avalanche, others | `traderjoe-v2` |
| Velodrome | Solidly fork | Optimism | `velodrome` |
| Aerodrome | Solidly fork | Base | `aerodrome` |
| Camelot | Concentrated liquidity | Arbitrum | `camelot` |

---

## 3. Adding a New DEX

### 3.1 Prerequisites
- DEX is deployed on at least one supported chain
- You have the router and factory addresses for each chain
- You have the ABI (or can reconstruct it from verified source)
- DEX has been live for >30 days and has >$1M TVL (for safety)

### 3.2 Create the Adapter

Create `packages/dex-registry/src/dexes/<dex-id>.ts`:

```ts
import { defineDex } from '../types';

export const myDex = defineDex({
  // Identity
  dex_id: 'my-dex',
  name: 'MyDEX',
  type: 'amm',  // 'amm' | 'concentrated_liquidity' | 'order_book' | 'stable_swap' | 'weighted'
  version: '1',
  docs_url: 'https://docs.mydex.io',

  // Per-chain deployments
  deployments: [
    {
      chain_id: 1,
      factory: '0x...',
      router: '0x...',
      quoter: '0x...',        // V3-style quote; optional
      init_code_hash: '0x...', // for V2-style pool derivation
      fee_tiers: [100, 500, 3000, 10000], // in bps; for CL DEXs
      default_fee_tier: 3000,
    },
    {
      chain_id: 42161,
      factory: '0x...',
      // ...
    },
  ],

  // Capabilities
  capabilities: {
    quote: true,
    swap: true,
    multi_hop: true,
    fee_on_transfer: false,  // most DEXs; some do
    supports_eth_input: true, // can swap ETH without wrapping
  },

  // ABI fragments (just what we need)
  abi: {
    router: [...],     // minimal router ABI
    quoter: [...],     // quoter ABI (CL DEXs)
    factory: [...],    // factory ABI (pool lookup)
    pool: [...],       // pool ABI (reads)
  },
});
```

### 3.3 Implement the Adapter Logic

`packages/dex-registry/src/dexes/<dex-id>/quoter.ts`:
```ts
export async function quoteExactInputSingle(
  chain: ChainAdapter,
  dex: DexDefinition,
  deployment: DexDeployment,
  params: { tokenIn: string; tokenOut: string; amountIn: bigint; feeTier?: number }
): Promise<{ amountOut: bigint; gasEstimate: bigint }> {
  // Build call to quoter contract
  const quoter = new Contract(deployment.quoter, dex.abi.quoter, chain.getProvider());
  const result = await quoter.quoteExactInputSingle.staticCall({
    tokenIn: params.tokenIn,
    tokenOut: params.tokenOut,
    amountIn: params.amountIn,
    fee: params.feeTier ?? deployment.default_fee_tier,
    sqrtPriceLimitX96: 0,
  });
  return { amountOut: result[0], gasEstimate: result[2] };
}
```

Similarly implement:
- `quoteExactOutputSingle`
- `quoteExactInput` (multi-hop)
- `buildSwapTx` (returns unsigned tx)
- `getPools` (for analytics)

### 3.4 Register

Edit `packages/dex-registry/src/index.ts`:
```ts
import { myDex } from './dexes/my-dex';

export const supportedDexes = [
  // ... existing
  myDex,
];
```

Add the dex to each chain's `dexes` list in `packages/chains/src/chains/<chain>.ts`.

### 3.5 Test

```bash
npm run test -- --grep "my-dex"
```

Test cases:
- Quote single-hop (USDC → WETH)
- Quote multi-hop (USDC → WETH → DAI)
- Build swap tx (verify calldata encoding)
- Pool discovery (factory calls return valid pools)
- Fee tier discovery (CL DEXs)
- Slippage calculation

### 3.6 Live Quote Test

```bash
npm run scripts:test-quote -- --dex=my-dex --chain=1 --pair=USDC/WETH --amount=1000
```

Compares APEX's quote to the DEX's own UI/API (within 0.05% tolerance).

---

## 4. The DexAdapter Interface

```ts
interface DexAdapter {
  readonly definition: DexDefinition;

  // Pool discovery
  getPool(tokenA: string, tokenB: string, feeTier?: number): Promise<PoolInfo | null>;
  getPoolsForToken(token: string): Promise<PoolInfo[]>;

  // Quotes
  quoteExactInputSingle(input: QuoteInput): Promise<QuoteResult>;
  quoteExactOutputSingle(input: QuoteInput): Promise<QuoteResult>;
  quoteExactInput(path: string[], amountIn: bigint): Promise<QuoteResult>;

  // Build (unsigned) transactions
  buildSwapTx(input: SwapInput): Promise<UnsignedTransaction>;

  // Reads
  getReserves(pool: string): Promise<{ reserve0: bigint; reserve1: bigint }>;
  getPriceImpact(input: SwapInput): Promise<number>;  // 0-1
}
```

---

## 5. Pool Registry

APEX maintains a `pools` table with:
- `pool_address`, `chain_id`, `dex_id`
- `token0`, `token1`, `fee_tier` (if applicable)
- `tvl_usd`, `volume_24h_usd` (updated periodically)
- `last_updated`

Pool discovery happens lazily:
- When APEX first sees a pair on a chain, it queries the factory
- Pools are cached and refreshed every 6 hours
- Users can pin custom pools via **Settings → Pools → Add Pool**

---

## 6. Fee Tier Handling (Concentrated Liquidity)

For V3-style DEXs, fee tiers vary (commonly 0.01%, 0.05%, 0.3%, 1%).
APEX:
- Queries all fee tiers for a pair
- Picks the best quote
- Returns the chosen fee tier with the result

For multi-hop routing, the fee tier is per-hop.

---

## 7. Multi-hop Routing

`quoteExactInput` accepts a path like `[USDC, WETH, DAI]` and returns the
net output. Implementation differs by DEX type:

### 7.1 AMM (V2-style)
- No native multi-hop; iterate through pairs
- Or call router's `swapExactTokensForTokens` with the path encoded

### 7.2 Concentrated Liquidity (V3-style)
- Path is encoded with fee tiers: `[(USDC, 500), (WETH, 3000)]`
- Quoter handles routing

### 7.3 Smart Order Routing (Cross-DEX)
- APEX can split a trade across multiple DEXes
- Implementation: dynamic programming over the graph of pools
- Optimizes for best net output net of gas

---

## 8. Gas Optimization

- Cache `factory` and `router` contracts per chain
- Batch pool reads via Multicall3
- Reuse WebSocket connections
- Pre-warm pools in the `chain-health` skill

---

## 9. Safety Checks

Before adding a DEX to the registry, APEX's `contract-auditor` agent reviews:
- Is the contract verified on the explorer?
- Has it been live for >30 days?
- Has it been exploited?
- TVL stability (no flash-crashes)
- Audit status
- Owner privileges (can owner drain funds?)

Risks are graded A-F; only A and B are added by default. C+ require explicit
user opt-in (Settings → Advanced → "Allow experimental DEXes").

---

## 10. DEX-Specific Quirks

| DEX | Gotcha |
|-----|--------|
| Uniswap V3 | Non-standard decimal handling for some pairs |
| Curve | Many pool types (2-coin, 3-coin, 4-coin, metapools); ABI varies |
| Balancer | Weighted pools with up to 8 tokens; pricing is non-trivial |
| Solidly forks | ve(3,3) model; some pools have dynamic fees |
| Maverick | Bin-based distribution; more complex quotes |

Each requires careful adapter testing. See the test suite for examples.

---

## 11. Deprecation

If a DEX is exploited, abandoned, or supplanted:
1. Mark `deprecated: true` in the dex definition
2. UI shows a warning; users can keep using but are prompted to migrate
3. New opportunities from this DEX are excluded by default
4. After 90 days, removed from default list

---

## 12. Checklist for New DEX

- [ ] Adapter implemented and registered
- [ ] All chains with deployments added
- [ ] ABIs sourced from verified contracts
- [ ] Unit tests passing
- [ ] Mainnet fork tests passing
- [ ] Live quote test within 0.05% of reference
- [ ] Slippage protection verified
- [ ] Contract audited by APEX's `contract-auditor` agent
- [ ] Documentation updated (`DEX-INTEGRATION.md` §2)
- [ ] Released in next minor version with changelog entry

---

*Add DEXes carefully. Each new integration is a potential attack surface.*

## Cross-references
- `ROUTING-ENGINE.md`
- `MARKET-DATA.md`
- `CHAIN-INTEGRATION.md`
- `EXECUTION-ENGINE.md`
- `LIQUIDITY-ANALYSIS.md`
- `DEX-REGISTRY.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
