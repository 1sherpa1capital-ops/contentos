#!/bin/bash
# run-autoresearch.sh
# Runs autoresearch on customer-avatar then offer-builder

set -e

echo "=========================================="
echo "Contentos Autoresearch Runner"
echo "=========================================="
echo ""

# Run customer-avatar first
echo ">>> Running customer-avatar autoresearch..."
cd "$(dirname "$0")" && python3 autoresearch.py --skill customer-avatar --iterations 10

echo ""
echo ">>> Running offer-builder autoresearch..."
cd "$(dirname "$0")" && python3 autoresearch.py --skill offer-builder --iterations 10

echo ""
echo "=========================================="
echo "Autoresearch complete!"
echo "=========================================="
