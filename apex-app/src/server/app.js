'use strict';

const express = require('express');
const http = require('http');
const { WebSocketServer } = require('ws');

function createApp(ctx) {
  const { engine, store, config, priceSource } = ctx;
  const app = express();
  app.use(express.json());

  app.get('/health', (req, res) => {
    res.json({
      status: 'ok',
      uptime: process.uptime(),
      running: engine.isRunning(),
      source: config.pricing.source,
    });
  });

  app.get('/config', (req, res) => {
    res.json({
      venues: config.venues,
      tokens: config.tokens,
      engine: {
        scanIntervalMs: config.engine.scanIntervalMs,
        tradeSizeUsd: config.engine.tradeSizeUsd,
        minProfitPct: config.engine.minProfitPct,
        maxSlippagePct: config.engine.maxSlippagePct,
        autoExecute: config.engine.autoExecute,
      },
      portfolio: { baseToken: config.portfolio.baseToken, initialBalanceUsd: config.portfolio.initialBalanceUsd },
    });
  });

  app.get('/prices', async (req, res) => {
    let market = engine.latestMarket;
    if (!market) {
      try {
        market = await priceSource.fetchMarket();
        engine.latestMarket = market;
      } catch (err) {
        return res.status(503).json({ error: 'price_unavailable', message: err.message });
      }
    }
    res.json({
      timestamp: market.timestamp,
      source: market.source,
      venues: market.venues,
      prices: market.prices,
    });
  });

  app.get('/opportunities', (req, res) => {
    res.json({ count: store.getOpportunities().length, opportunities: store.getOpportunities() });
  });

  app.get('/trades', (req, res) => {
    res.json({ count: store.getTrades().length, trades: store.getTrades() });
  });

  app.get('/stats', (req, res) => {
    res.json(store.getStats());
  });

  app.post('/engine/start', (req, res) => {
    engine.start();
    res.status(202).json({ running: true });
  });

  app.post('/engine/stop', (req, res) => {
    engine.stop();
    res.status(202).json({ running: false });
  });

  app.post('/engine/scan', async (req, res) => {
    const { opportunities } = await engine.scanOnce();
    res.json({ count: opportunities.length, opportunities });
  });

  app.use((err, req, res, next) => {
    res.status(500).json({ error: 'internal_error', message: err.message });
  });

  return app;
}

function attachWebSocket(server, ctx) {
  const { engine, store } = ctx;
  const wss = new WebSocketServer({ server, path: '/stream' });

  function send(ws, type, payload) {
    if (ws.readyState === ws.OPEN) ws.send(JSON.stringify({ type, payload, ts: Date.now() }));
  }

  wss.on('connection', (ws) => {
    send(ws, 'snapshot', {
      stats: store.getStats(),
      opportunities: store.getOpportunities().slice(0, 50),
      running: engine.isRunning(),
    });
    const onOpp = (ops) => send(ws, 'opportunities', ops);
    const onTrade = (t) => send(ws, 'trade', t);
    const onStatus = (s) => send(ws, 'status', s);
    engine.on('opportunities', onOpp);
    engine.on('trade', onTrade);
    engine.on('status', onStatus);
    ws.on('close', () => {
      engine.off('opportunities', onOpp);
      engine.off('trade', onTrade);
      engine.off('status', onStatus);
    });
  });

  return wss;
}

function buildServer(ctx) {
  const app = createApp(ctx);
  const server = http.createServer(app);
  attachWebSocket(server, ctx);
  return server;
}

module.exports = { createApp, attachWebSocket, buildServer };
