#!/bin/bash
set -e

echo "Comparing environment configurations..."
diff -u config/test.env.template config/prod.env.template || true
echo "Environment diff complete"
