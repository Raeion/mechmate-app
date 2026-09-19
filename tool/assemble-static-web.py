#!/usr/bin/env python3
"""Assemble the prebuilt Flutter web tree on Vercel without a Flutter SDK."""

from __future__ import annotations

import base64
import gzip
import hashlib
import json
import pathlib
import shutil
import subprocess
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
PARTS = ROOT / "tool" / "web-parts"
OUT = ROOT / "build" / "web"


def write_bytes(rel: str, data: bytes) -> None:
    dest = OUT / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)


def concat_parts(stem: str, dest_rel: str, decompress: bool = False) -> None:
    directory = PARTS / stem
    if not directory.is_dir():
        return
    chunks = sorted(p for p in directory.iterdir() if p.is_file())
    data = b"".join(p.read_bytes() for p in chunks)
    if decompress:
        data = gzip.decompress(data)
    write_bytes(dest_rel, data)


def decode_b64(rel: str) -> None:
    src = PARTS / f"{rel}.b64"
    if src.is_file():
        write_bytes(rel, base64.b64decode(src.read_text()))


def write_asset_manifest_json() -> None:
    dest = OUT / "assets" / "AssetManifest.json"
    payload = json.dumps(
        {
            "assets/data/catalog.json": ["assets/data/catalog.json"],
            "packages/cupertino_icons/assets/CupertinoIcons.ttf": [
                "packages/cupertino_icons/assets/CupertinoIcons.ttf"
            ],
        },
        separators=(",", ":"),
    )
    if dest.is_file():
        existing = dest.read_text(encoding="utf-8", errors="replace")
        if existing.lstrip().startswith("{") and "assets/data/catalog.json" in existing:
            return
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(payload, encoding="utf-8")


def compile_catalog() -> None:
    script = ROOT / "tool" / "compile_catalog.py"
    if not script.is_file():
        return
    subprocess.check_call([sys.executable, str(script)], cwd=ROOT)
    generated = ROOT / "assets" / "data" / "catalog.json"
    if generated.is_file():
        write_bytes("assets/assets/data/catalog.json", generated.read_bytes())


def download_remote_files() -> None:
    manifest_path = PARTS / "remote-files.json"
    if not manifest_path.is_file():
        return
    manifest = json.loads(manifest_path.read_text())
    for rel, meta in manifest.items():
        dest = OUT / rel
        if dest.is_file() and dest.stat().st_size > 0:
            print(f"skip remote {rel}: already assembled")
            continue
        url = meta["url"]
        expected = meta["sha1"]
        try:
            request = urllib.request.Request(
                url,
                headers={"User-Agent": "mechmate-assemble/1.0"},
            )
            payload = urllib.request.urlopen(request, timeout=120).read()
        except Exception as exc:
            if dest.is_file():
                print(f"skip remote {rel}: {exc}")
                continue
            raise SystemExit(f"remote download fail {rel}: {exc}") from exc
        if meta.get("gzip") or payload[:2] == b"\x1f\x8b":
            payload = gzip.decompress(payload)
        got = hashlib.sha1(payload).hexdigest()
        if got != expected:
            if dest.is_file():
                print(f"skip remote {rel}: checksum {got} != {expected}")
                continue
            raise SystemExit(f"remote checksum fail {rel}: {got} != {expected}")
        write_bytes(rel, payload)
        print(f"downloaded {rel} ({len(payload)} bytes)")


def verify_checksums() -> None:
    manifest = PARTS / "checksums.json"
    if not manifest.is_file():
        return
    expected = json.loads(manifest.read_text())
    errors: list[str] = []
    for rel, sha in expected.items():
        path = OUT / rel
        if not path.is_file():
            errors.append(f"missing {rel}")
            continue
        got = hashlib.sha1(path.read_bytes()).hexdigest()
        if got != sha:
            errors.append(f"{rel} {got} != {sha}")
    if errors:
        raise SystemExit("checksum fail:\n" + "\n".join(errors))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    if (PARTS / "copy").is_dir():
        shutil.copytree(PARTS / "copy", OUT, dirs_exist_ok=True)
    concat_parts("main.dart.js", "main.dart.js")
    concat_parts("main.dart.js.gz", "main.dart.js", decompress=True)
    concat_parts("catalog.json", "assets/assets/data/catalog.json")
    concat_parts("drift_worker.js", "drift_worker.js")
    concat_parts("notices", "assets/NOTICES")
    concat_parts("sqlite3.wasm.gz", "sqlite3.wasm", decompress=True)
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
    download_remote_files()
    icon_192 = OUT / "icons" / "Icon-192.png"
    icon_512 = OUT / "icons" / "Icon-512.png"
    if icon_192.is_file():
        write_bytes("icons/Icon-maskable-192.png", icon_192.read_bytes())
    if icon_512.is_file():
        write_bytes("icons/Icon-maskable-512.png", icon_512.read_bytes())
    if not (OUT / "assets/assets/data/catalog.json").is_file():
        compile_catalog()
    if not (OUT / "assets/NOTICES").is_file():
        write_bytes("assets/NOTICES", b"Mechmate Flutter licenses\n")
    write_asset_manifest_json()
    verify_checksums()


if __name__ == "__main__":
    main()
