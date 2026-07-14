'use strict';

const fs = require('fs');
const path = require('path');

const DEFAULT_CONFIG_PATH = path.join(__dirname, '..', 'config', 'default.json');

function loadConfig(configPath) {
  const file = configPath || process.env.APEX_CONFIG || DEFAULT_CONFIG_PATH;
  const raw = fs.readFileSync(file, 'utf8');
  const config = JSON.parse(raw);

  // Environment overrides
  if (process.env.APEX_PORT) config.server.port = Number(process.env.APEX_PORT);
  if (process.env.APEX_PRICE_SOURCE) config.pricing.source = process.env.APEX_PRICE_SOURCE;
  if (process.env.APEX_AUTO_EXECUTE) config.engine.autoExecute = process.env.APEX_AUTO_EXECUTE === 'true';
  if (process.env.APEX_ENGINE_ENABLED) config.engine.enabled = process.env.APEX_ENGINE_ENABLED === 'true';

  return config;
}

module.exports = { loadConfig, DEFAULT_CONFIG_PATH };
