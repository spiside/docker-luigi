#!/usr/bin/env bash
set -e
PORT=${PORT:-8082}

./generate_config.py

luigid --port "$PORT"
