'use strict';

const fs = require('fs');
const path = require('path');

const MAX_OPPORTUNITIES = 1000;
const MAX_TRADES = 1000;

/**
 * Simple JSON-file backed store. Use filePath ':memory:' for an in-memory
 * store (used by tests). The public surface is intentionally small so the
 * persistence backend can be swapped (e.g. for SQLite) without touching callers.
 */
class Store {
  constructor(filePath) {
    this.filePath = filePath;
    this.state = {
      opportunities: [],
      trades: [],
      portfolio: { balanceUsd: 0 },
      stats: {
        scans: 0,
        opportunitiesFound: 0,
        tradesExecuted: 0,
        totalProfitUsd: 0,
        balanceUsd: 0,
        running: false,
        startedAt: null,
        lastScanAt: null,
      },
    };
    if (this.filePath !== ':memory:') {
      this._ensureDir();
      this._load();
    }
  }

  _ensureDir() {
    const dir = path.dirname(this.filePath);
    if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
  }

  _load() {
    try {
      if (fs.existsSync(this.filePath)) {
        const raw = fs.readFileSync(this.filePath, 'utf8');
        const parsed = JSON.parse(raw);
        this.state = { ...this.state, ...parsed };
      }
    } catch (err) {
      // Corrupt or unreadable store: start fresh.
    }
  }

  _persist() {
    if (this.filePath === ':memory:') return;
    fs.writeFileSync(this.filePath, JSON.stringify(this.state, null, 2), 'utf8');
  }

  setBalance(balanceUsd) {
    this.state.portfolio.balanceUsd = balanceUsd;
    this.state.stats.balanceUsd = balanceUsd;
    this._persist();
  }

  getBalance() {
    return this.state.portfolio.balanceUsd;
  }

  addOpportunities(list) {
    if (!Array.isArray(list) || list.length === 0) return;
    const byId = new Map(this.state.opportunities.map((o) => [o.id, o]));
    for (const op of list) byId.set(op.id, op);
    this.state.opportunities = Array.from(byId.values())
      .sort((a, b) => b.timestamp - a.timestamp)
      .slice(0, MAX_OPPORTUNITIES);
    this.state.stats.opportunitiesFound += list.length;
    this.state.stats.lastScanAt = Date.now();
    this._persist();
  }

  getOpportunities() {
    return this.state.opportunities.slice();
  }

  recordTrade(trade) {
    this.state.trades.unshift(trade);
    if (this.state.trades.length > MAX_TRADES) this.state.trades.length = MAX_TRADES;
    this.state.stats.tradesExecuted += 1;
    this.state.stats.totalProfitUsd = Math.round((this.state.stats.totalProfitUsd + (trade.profitUsd || 0)) * 100) / 100;
    this._persist();
  }

  getTrades() {
    return this.state.trades.slice();
  }

  updateStats(partial) {
    Object.assign(this.state.stats, partial);
    this._persist();
  }

  getStats() {
    return { ...this.state.stats };
  }

  reset() {
    this.state = {
      opportunities: [],
      trades: [],
      portfolio: { balanceUsd: 0 },
      stats: {
        scans: 0,
        opportunitiesFound: 0,
        tradesExecuted: 0,
        totalProfitUsd: 0,
        balanceUsd: 0,
        running: false,
        startedAt: null,
        lastScanAt: null,
      },
    };
    this._persist();
  }
}

module.exports = Store;
