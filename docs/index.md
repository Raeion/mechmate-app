# Mechmate documentation

Mechmate is an offline workshop companion. This folder is the map of what shipped, why it is shaped this way, and where the diagnostic data came from.

## Index

- [Manifest](manifest.md) of files, coverage, and generated artifacts
- [Information architecture](ia.md) for garage, where, sense, and system browse
- [Workshop illustrations](illustrations.md) for home tiles and empty states
- [Data model](data-model.md) for vehicles, articles, filters, and Drift
- [Research sources](research/sources.md) cited by the catalog
- [Heritage from the first MechMate apps](heritage.md)
- [Launch status](launch.md)
- [Vercel web deploy](vercel.md)
- [Changelog](changelog.md)
- [Store listing copy](store-listing.md)
- [Privacy](legal/privacy.md)
- [Terms of use](legal/terms.md)
- [Safety disclaimer](legal/disclaimer.md)

## Product rules

- The local database is the source of truth at runtime.
- YAML in `data/` plus the Python sources in `tool/` are the source of truth in git.
- Articles diagnose, test, and repair. They do not outsource the job.
- Illegal DPF or EGR deletes are not documented as repairs.
- Safety is a lock-out list, then the next step.

## Related repo files

- [../README.md](../README.md)
- [../tool/compile_catalog.py](../tool/compile_catalog.py)
- [../assets/data/catalog.json](../assets/data/catalog.json)
