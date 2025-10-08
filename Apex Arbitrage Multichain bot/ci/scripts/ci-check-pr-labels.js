#!/usr/bin/env node
const labels = process.env.PR_LABELS?.split(',') || [];
const requiredLabels = ['reviewed', 'tested'];

const hasRequired = requiredLabels.every(label => labels.includes(label));

if (!hasRequired) {
  console.error('PR missing required labels:', requiredLabels);
  process.exit(1);
}

console.log('PR labels validated');
