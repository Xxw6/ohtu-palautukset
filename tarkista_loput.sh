#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
cd osa2/nhl-statistics-1
uv sync
uv run coverage run -m pytest
uv run coverage report --fail-under=100
uv run python src/index.py
cd ../project-reader
uv sync
uv run python src/index.py
cd ../..
echo "VALMIS: NHL, testikattavuus ja TOML-lukija tarkistettu. Pushaa viela GitHubiin."
