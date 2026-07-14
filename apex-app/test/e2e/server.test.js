'use strict';

const request = require('supertest');
const WebSocket = require('ws');
const { createApp, buildServer } = require('../../src/server/app');
const Store = require('../../src/storage/store');
const Engine = require('../../src/engine/engine');
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
    server: { port: 0, host: '127.0.0.1' },
    pricing: { source: 'mock', mock: { jitterPct: 0.4 } },
    venues: [
      { id: 'uniswap', name: 'Uniswap', feePct: 0.3, chain: 'ethereum' },
      { id: 'sushiswap', name: 'SushiSwap', feePct: 0.25, chain: 'ethereum' },
      { id: 'pancakeswap', name: 'PancakeSwap', feePct: 0.2, chain: 'bsc' },
      { id: 'quickswap', name: 'QuickSwap', feePct: 0.3, chain: 'polygon' },
      { id: 'curve', name: 'Curve', feePct: 0.04, chain: 'ethereum' },
      { id: 'traderjoe', name: 'Trader Joe', feePct: 0.3, chain: 'arbitrum' },
    ],
    tokens: [
      { symbol: 'ETH', name: 'Ethereum', coingeckoId: 'ethereum' },
      { symbol: 'BTC', name: 'Bitcoin', coingeckoId: 'bitcoin' },
      { symbol: 'USDC', name: 'USD Coin', coingeckoId: 'usd-coin' },
      { symbol: 'USDT', name: 'Tether', coingeckoId: 'tether' },
      { symbol: 'DAI', name: 'Dai', coingeckoId: 'dai' },
      { symbol: 'WBTC', name: 'Wrapped Bitcoin', coingeckoId: 'wrapped-bitcoin' },
      { symbol: 'MATIC', name: 'Polygon', coingeckoId: 'matic-network' },
      { symbol: 'ARB', name: 'Arbitrum', coingeckoId: 'arbitrum' },
    ],
    ...overrides,
  };
}

function makeCtx() {
  const config = makeConfig();
  const store = new Store(':memory:');
  const source = new MockSource(config, DEFAULT_MOCK_PRICES);
  const engine = new Engine({ priceSource: source, store, config });
  return { engine, store, config, priceSource: source };
}

describe('HTTP API (end-to-end)', () => {
  let ctx, app;
  beforeAll(() => {
    ctx = makeCtx();
    app = createApp(ctx);
  });
  afterAll(() => ctx.engine.stop());

  test('GET /health reports ok', async () => {
    const res = await request(app).get('/health');
    expect(res.status).toBe(200);
    expect(res.body.status).toBe('ok');
  });

  test('GET /config exposes venues and tokens', async () => {
    const res = await request(app).get('/config');
    expect(res.status).toBe(200);
    expect(res.body.venues.length).toBeGreaterThan(0);
    expect(res.body.tokens.find((t) => t.symbol === 'ETH')).toBeDefined();
  });

  test('POST /engine/scan detects opportunities and persists them', async () => {
    const res = await request(app).post('/engine/scan');
    expect(res.status).toBe(200);
    expect(res.body.count).toBeGreaterThan(0);

    const opp = await request(app).get('/opportunities');
    expect(opp.body.count).toBeGreaterThan(0);

    const stats = await request(app).get('/stats');
    expect(stats.body.scans).toBeGreaterThanOrEqual(1);
  });

  test('GET /prices returns a market snapshot', async () => {
    const res = await request(app).get('/prices');
    expect(res.status).toBe(200);
    expect(res.body.prices.ETH).toBeDefined();
    expect(Object.keys(res.body.prices.ETH).length).toBeGreaterThan(0);
  });

  test('POST /engine/start and /stop toggle running state', async () => {
    const start = await request(app).post('/engine/start');
    expect(start.status).toBe(202);
    expect(start.body.running).toBe(true);

    const stop = await request(app).post('/engine/stop');
    expect(stop.status).toBe(202);
    expect(stop.body.running).toBe(false);
  });
});

describe('WebSocket live stream (end-to-end)', () => {
  let server, ctx, port, ws;
  beforeAll((done) => {
    ctx = makeCtx();
    server = buildServer(ctx);
    server.listen(0, '127.0.0.1', () => {
      port = server.address().port;
      done();
    });
  });
  afterAll((done) => {
    ctx.engine.stop();
    server.close(() => done());
  });

  test('client receives opportunities over the stream', (done) => {
    ws = new WebSocket(`ws://127.0.0.1:${port}/stream`);
    let got = false;
    ws.on('open', () => {
      ctx.engine.scanOnce().catch(done);
    });
    ws.on('message', (data) => {
      const msg = JSON.parse(data.toString());
      if (msg.type === 'opportunities' && msg.payload.length > 0) {
        got = true;
        ws.close();
        done();
      }
    });
    ws.on('error', done);
    setTimeout(() => {
      if (!got) {
        ws.close();
        done(new Error('no opportunities message received'));
      }
    }, 5000);
  });
});
