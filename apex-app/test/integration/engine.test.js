'use strict';

const Store = require('../../src/storage/store');
const Engine = require('../../src/engine/engine');
const Executor = require('../../src/engine/executor');
const { MockSource, DEFAULT_MOCK_PRICES } = require('../../src/pricing/mockSource');

function makeConfig(overrides = {}) {
  return {
    engine: {
      scanIntervalMs: 1000,
      tradeSizeUsd: 1000,
      minProfitPct: 0.2,
      maxSlippagePct: 1.5,
      liquidityDepthUsd: 5_000_000,
      autoExecute: false,
    },
    portfolio: { baseToken: 'USDC', initialBalanceUsd: 10000 },
    venues: [
      { id: 'uniswap', name: 'Uniswap', feePct: 0.3, chain: 'ethereum' },
      { id: 'sushiswap', name: 'SushiSwap', feePct: 0.25, chain: 'ethereum' },
      { id: 'pancakeswap', name: 'PancakeSwap', feePct: 0.2, chain: 'bsc' },
      { id: 'quickswap', name: 'QuickSwap', feePct: 0.3, chain: 'polygon' },
      { id: 'curve', name: 'Curve', feePct: 0.04, chain: 'ethereum' },
      { id: 'traderjoe', name: 'Trader Joe', feePct: 0.3, chain: 'arbitrum' },
    ],
    ...overrides,
  };
}

describe('Engine integration', () => {
  let store, engine;

  beforeEach(() => {
    store = new Store(':memory:');
    const source = new MockSource(makeConfig(), DEFAULT_MOCK_PRICES);
    engine = new Engine({ priceSource: source, store, config: makeConfig() });
  });

  afterEach(() => {
    engine.stop();
  });

  test('scanOnce detects and stores opportunities', async () => {
    const { opportunities } = await engine.scanOnce();
    expect(opportunities.length).toBeGreaterThan(0);
    expect(store.getOpportunities().length).toBe(opportunities.length);
    expect(store.getStats().scans).toBe(1);
  });

  test('latestMarket is populated after a scan', async () => {
    await engine.scanOnce();
    expect(engine.latestMarket).not.toBeNull();
    expect(engine.latestMarket.prices.ETH).toBeDefined();
  });

  test('autoExecute simulates trades and grows the paper balance', async () => {
    const cfg = makeConfig({ engine: { ...makeConfig().engine, autoExecute: true } });
    const source = new MockSource(cfg, DEFAULT_MOCK_PRICES);
    const e = new Engine({ priceSource: source, store, config: cfg });
    const before = store.getBalance();
    await e.scanOnce();
    const trades = store.getTrades();
    expect(trades.length).toBeGreaterThan(0);
    expect(store.getBalance()).toBeGreaterThan(before);
    expect(store.getStats().totalProfitUsd).toBeGreaterThan(0);
    e.stop();
  });

  test('start/stop toggles running state and clears the timer', () => {
    expect(engine.isRunning()).toBe(false);
    engine.start();
    expect(engine.isRunning()).toBe(true);
    engine.stop();
    expect(engine.isRunning()).toBe(false);
  });

  test('emits opportunities event during scan', async () => {
    const received = [];
    engine.on('opportunities', (ops) => received.push(...ops));
    await engine.scanOnce();
    expect(received.length).toBeGreaterThan(0);
  });
});

describe('Executor', () => {
  test('simulate returns a trade and increases balance', () => {
    const executor = new Executor(makeConfig());
    const op = { type: 'direct', path: ['ETH'], profitPct: 1.5, tradeSizeUsd: 1000, expectedProfitUsd: 15, legs: [] };
    const res = executor.simulate(op, 10000);
    expect(res.ok).toBe(true);
    expect(res.trade.profitUsd).toBe(15);
    expect(res.newBalance).toBe(10015);
  });

  test('simulate rejects when balance is insufficient', () => {
    const executor = new Executor(makeConfig());
    const op = { type: 'direct', path: ['ETH'], profitPct: 1.5, tradeSizeUsd: 5000, expectedProfitUsd: 75, legs: [] };
    const res = executor.simulate(op, 1000);
    expect(res.ok).toBe(false);
    expect(res.reason).toBe('insufficient_balance');
  });
});
