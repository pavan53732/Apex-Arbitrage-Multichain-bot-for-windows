#!/bin/bash
set -e

echo "Creating patch release..."
npm version patch
git push --tags
echo "Patch release created"
