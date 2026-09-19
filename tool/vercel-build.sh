#!/usr/bin/env bash
# Build the offline Flutter web bundle for Vercel. No Firebase or env vars.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if ! command -v flutter >/dev/null 2>&1; then
  FLUTTER_HOME="${FLUTTER_HOME:-$HOME/flutter}"
  if [ ! -x "$FLUTTER_HOME/bin/flutter" ]; then
    git clone https://github.com/flutter/flutter.git -b stable --depth 1 "$FLUTTER_HOME"
  fi
  export PATH="$FLUTTER_HOME/bin:$PATH"
fi

python3 tool/compile_catalog.py

flutter config --no-analytics --enable-web
flutter pub get

mkdir -p web
WASM="$(find "$HOME/.pub-cache" -name sqlite3.wasm -print -quit || true)"
WORKER="$(find "$HOME/.pub-cache" -name drift_worker.js -print -quit || true)"
if [ -n "$WASM" ]; then
  cp "$WASM" web/sqlite3.wasm
fi
if [ -n "$WORKER" ]; then
  cp "$WORKER" web/drift_worker.js
fi

dart run build_runner build --delete-conflicting-outputs
flutter build web --release --no-wasm-dry-run --base-href /
