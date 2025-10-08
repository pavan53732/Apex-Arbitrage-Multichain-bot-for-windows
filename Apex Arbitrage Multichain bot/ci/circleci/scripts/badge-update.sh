#!/bin/bash
set -e

echo "Updating CI badges..."
node ci/scripts/run-badge-update.sh
echo "Badges updated"
