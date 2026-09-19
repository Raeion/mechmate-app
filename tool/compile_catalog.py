#!/usr/bin/env python3
"""Compile Mechmate YAML/Python sources into the bundled offline catalog."""

from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parent))

from articles_48v import articles as articles_48v
from articles_au import articles as articles_au
from articles_heritage import articles as articles_heritage
from articles_hilux import articles as articles_hilux
from articles_universal import articles as articles_universal
from catalog_taxonomy import TAXONOMY
from catalog_vehicles import ENGINES, GENERATIONS, MAKES, MODELS, VARIANTS


def _yaml_scalar(value):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value).replace('"', '\\"')
    return f'"{text}"'


def _dump_yaml(data, indent=0):
    pad = "  " * indent
    if isinstance(data, list):
        if not data:
            return f"{pad}[]\n"
        chunks = []
        for item in data:
            if isinstance(item, (dict, list)):
                chunks.append(f"{pad}-\n{_dump_yaml(item, indent + 1)}")
            else:
                chunks.append(f"{pad}- {_yaml_scalar(item)}\n")
        return "".join(chunks)
    if isinstance(data, dict):
        chunks = []
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                chunks.append(f"{pad}{key}:\n{_dump_yaml(value, indent + 1)}")
            else:
                chunks.append(f"{pad}{key}: {_yaml_scalar(value)}\n")
        return "".join(chunks)
    return f"{pad}{_yaml_scalar(data)}\n"


def build_catalog():
    articles = (
        articles_hilux()
        + articles_48v()
        + articles_universal()
        + articles_au()
        + articles_heritage()
    )
    ids = [item["id"] for item in articles]
    if len(ids) != len(set(ids)):
        raise SystemExit("Duplicate article ids")
    return {
        "version": "2026.09.17.2",
        "name": "Mechmate Australia-first catalog",
        "taxonomy": TAXONOMY,
        "makes": MAKES,
        "models": MODELS,
        "generations": GENERATIONS,
        "engines": ENGINES,
        "variants": VARIANTS,
        "articles": articles,
    }


def write_sqlite(catalog: dict, path: Path) -> None:
    if path.exists():
        path.unlink()
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.executescript(
        """
        CREATE TABLE makes (id TEXT PRIMARY KEY, name TEXT);
        CREATE TABLE models (id TEXT PRIMARY KEY, make_id TEXT, name TEXT, body_type TEXT);
        CREATE TABLE generations (
          id TEXT PRIMARY KEY, model_id TEXT, code TEXT, name TEXT, year_from INTEGER, year_to INTEGER
        );
        CREATE TABLE engines (
          id TEXT PRIMARY KEY, code TEXT, fuel TEXT, displacement_l TEXT, notes TEXT
        );
        CREATE TABLE variants (
          id TEXT PRIMARY KEY, generation_id TEXT, engine_id TEXT, drivetrain TEXT,
          is_48v INTEGER, voltage_label TEXT
        );
        CREATE TABLE taxonomy (
          id TEXT PRIMARY KEY, kind TEXT, title TEXT, subtitle TEXT, icon TEXT, sort_order INTEGER
        );
        CREATE TABLE articles (
          id TEXT PRIMARY KEY, title TEXT, summary TEXT, severity TEXT, body_json TEXT
        );
        CREATE TABLE article_tags (
          id INTEGER PRIMARY KEY AUTOINCREMENT, article_id TEXT, kind TEXT, tag_id TEXT
        );
        CREATE VIRTUAL TABLE articles_fts USING fts5(
          article_id UNINDEXED, title, summary, body, tokenize='unicode61'
        );
        """
    )
    cursor.executemany(
        "INSERT INTO makes VALUES (?, ?)",
        [(row["id"], row["name"]) for row in catalog["makes"]],
    )
    cursor.executemany(
        "INSERT INTO models VALUES (?, ?, ?, ?)",
        [(row["id"], row["makeId"], row["name"], row["bodyType"]) for row in catalog["models"]],
    )
    cursor.executemany(
        "INSERT INTO generations VALUES (?, ?, ?, ?, ?, ?)",
        [
            (
                row["id"],
                row["modelId"],
                row["code"],
                row["name"],
                row["yearFrom"],
                row["yearTo"],
            )
            for row in catalog["generations"]
        ],
    )
    cursor.executemany(
        "INSERT INTO engines VALUES (?, ?, ?, ?, ?)",
        [
            (row["id"], row["code"], row["fuel"], row["displacementL"], row.get("notes"))
            for row in catalog["engines"]
        ],
    )
    cursor.executemany(
        "INSERT INTO variants VALUES (?, ?, ?, ?, ?, ?)",
        [
            (
                row["id"],
                row["generationId"],
                row["engineId"],
                row["drivetrain"],
                1 if row.get("is48v") else 0,
                row.get("voltageLabel"),
            )
            for row in catalog["variants"]
        ],
    )
    cursor.executemany(
        "INSERT INTO taxonomy VALUES (?, ?, ?, ?, ?, ?)",
        [
            (
                row["id"],
                row["kind"],
                row["title"],
                row["subtitle"],
                row["icon"],
                row["sortOrder"],
            )
            for row in catalog["taxonomy"]
        ],
    )
    for article in catalog["articles"]:
        cursor.execute(
            "INSERT INTO articles VALUES (?, ?, ?, ?, ?)",
            (
                article["id"],
                article["title"],
                article["summary"],
                article["severity"],
                json.dumps(article),
            ),
        )
        for location in article["locations"]:
            cursor.execute(
                "INSERT INTO article_tags (article_id, kind, tag_id) VALUES (?, ?, ?)",
                (article["id"], "location", location),
            )
        for sense in article["senses"]:
            cursor.execute(
                "INSERT INTO article_tags (article_id, kind, tag_id) VALUES (?, ?, ?)",
                (article["id"], "sense", sense),
            )
        for system in article["systems"]:
            cursor.execute(
                "INSERT INTO article_tags (article_id, kind, tag_id) VALUES (?, ?, ?)",
                (article["id"], "system", system),
            )
        body = " ".join(
            [
                article["title"],
                article["summary"],
                " ".join(article["symptoms"]),
                " ".join(cause["name"] + " " + cause["why"] for cause in article["causes"]),
            ]
        )
        cursor.execute(
            "INSERT INTO articles_fts (article_id, title, summary, body) VALUES (?, ?, ?, ?)",
            (article["id"], article["title"], article["summary"], body),
        )
    connection.commit()
    connection.close()


def main() -> None:
    catalog = build_catalog()
    data_dir = ROOT / "data"
    articles_dir = data_dir / "articles"
    assets_dir = ROOT / "assets" / "data"
    data_dir.mkdir(exist_ok=True)
    articles_dir.mkdir(parents=True, exist_ok=True)
    assets_dir.mkdir(parents=True, exist_ok=True)

    (data_dir / "taxonomy.yaml").write_text(_dump_yaml(catalog["taxonomy"]), encoding="utf-8")
    (data_dir / "vehicles.yaml").write_text(
        _dump_yaml(
            {
                "makes": catalog["makes"],
                "models": catalog["models"],
                "generations": catalog["generations"],
                "engines": catalog["engines"],
                "variants": catalog["variants"],
            }
        ),
        encoding="utf-8",
    )
    groups = {
        "hilux.yaml": articles_hilux(),
        "forty_eight_volt.yaml": articles_48v(),
        "universal.yaml": articles_universal(),
        "australia.yaml": articles_au(),
        "heritage.yaml": articles_heritage(),
    }
    for name, rows in groups.items():
        (articles_dir / name).write_text(_dump_yaml(rows), encoding="utf-8")

    catalog_path = assets_dir / "catalog.json"
    catalog_path.write_text(json.dumps(catalog, indent=2), encoding="utf-8")
    write_sqlite(catalog, assets_dir / "mechmate.db")
    print(
        f"Wrote {len(catalog['articles'])} articles, "
        f"{len(catalog['models'])} models, {len(catalog['variants'])} variants"
    )


if __name__ == "__main__":
    main()
