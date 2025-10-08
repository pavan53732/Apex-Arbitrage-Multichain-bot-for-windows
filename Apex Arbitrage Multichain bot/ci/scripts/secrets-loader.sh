#!/bin/bash
set -e

echo "Loading secrets from vault..."
export $(cat .env.secrets | xargs)
echo "Secrets loaded successfully"
