'use strict';

const levels = ['debug', 'info', 'warn', 'error'];
const currentLevel = process.env.APEX_LOG_LEVEL || 'info';

function shouldLog(level) {
  return levels.indexOf(level) >= levels.indexOf(currentLevel);
}

function format(level, args) {
  const ts = new Date().toISOString();
  return [`${ts} [${level.toUpperCase()}]`, ...args];
}

const logger = {
  debug(...args) { if (shouldLog('debug')) console.debug(...format('debug', args)); },
  info(...args) { if (shouldLog('info')) console.info(...format('info', args)); },
  warn(...args) { if (shouldLog('warn')) console.warn(...format('warn', args)); },
  error(...args) { if (shouldLog('error')) console.error(...format('error', args)); },
};

module.exports = logger;
