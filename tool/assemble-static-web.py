#!/usr/bin/env python3
"""Assemble the prebuilt Flutter web tree on Vercel without a Flutter SDK."""

from __future__ import annotations

import base64
import pathlib
import shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
PARTS = ROOT / "tool" / "web-parts"
OUT = ROOT / "build" / "web"


def write_bytes(rel: str, data: bytes) -> None:
    dest = OUT / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)


def concat_parts(stem: str, dest_rel: str) -> None:
    directory = PARTS / stem
    if not directory.is_dir():
        return
    chunks = sorted(p for p in directory.iterdir() if p.is_file())
    write_bytes(dest_rel, b"".join(p.read_bytes() for p in chunks))


def decode_b64(rel: str) -> None:
    src = PARTS / f"{rel}.b64"
    if src.is_file():
        write_bytes(rel, base64.b64decode(src.read_text()))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    if (PARTS / "copy").is_dir():
        shutil.copytree(PARTS / "copy", OUT, dirs_exist_ok=True)
    concat_parts("main.dart.js", "main.dart.js")
    concat_parts("catalog.json", "assets/assets/data/catalog.json")
    concat_parts("drift_worker.js", "drift_worker.js")
    for rel in (
        "sqlite3.wasm",
        "favicon.png",
        "icons/Icon-192.png",
        "icons/Icon-512.png",
        "icons/Icon-maskable-192.png",
        "icons/Icon-maskable-512.png",
        "assets/fonts/MaterialIcons-Regular.otf",
        "assets/packages/cupertino_icons/assets/CupertinoIcons.ttf",
        "assets/AssetManifest.bin",
    ):
        decode_b64(rel)


if __name__ == "__main__":
    main()
