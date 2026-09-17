# Mechmate

Mechmate is an offline-first Flutter app for iOS, Android, and web. A mate for your Car: pick a vehicle, describe what you hear, see, or feel, and get ranked causes with tests and repairs.

Copy never says "take it to a mechanic." Safety steps stay in the procedure, then the app tells you how to finish the job.

The public origin repo is [https://github.com/Raeion/mechmate-app](https://github.com/Raeion/mechmate-app). The older private `Raeion/MechMate` C# project already used that name on GitHub, so this Flutter rebuild lives here.

## What is in version 1

- Garage with Australia-first vehicles, including every Hilux generation in the catalog and 48V V-Active / MHEV badges
- Browse by where (cabin, body, engine bay, front, rear, undercarriage, wheels, electrical, glass)
- Browse by how it shows up (sound, look, performance, smell, feel, leak)
- Browse by system, including a dedicated 48V V-Active / MHEV chapter
- Offline search over the bundled catalog
- The original ten Unity mate paths on home (electrical, noise, leak, smell, steering, tyres, vibration, glass, body in, body out)
- 106 original diagnostic articles compiled into `assets/data/catalog.json` and `assets/data/mechmate.db`

## Documentation

- [docs/index.md](docs/index.md)
- [docs/manifest.md](docs/manifest.md)
- [docs/data-model.md](docs/data-model.md)
- [docs/ia.md](docs/ia.md)
- [docs/research/sources.md](docs/research/sources.md)
- [docs/heritage.md](docs/heritage.md)

## Run locally

```bash
flutter pub get
python3 tool/compile_catalog.py
flutter run
```

Web needs the Drift worker files already in `web/sqlite3.wasm` and `web/drift_worker.js`.

```bash
flutter run -d chrome
```

## Tests

```bash
flutter analyze
flutter test
```

## Rebuild the catalog

Edit Python sources under `tool/` (taxonomy, vehicles, articles), then:

```bash
python3 tool/compile_catalog.py
```

That refreshes:

- `data/taxonomy.yaml`
- `data/vehicles.yaml`
- `data/articles/*.yaml`
- `assets/data/catalog.json`
- `assets/data/mechmate.db`

The app imports `catalog.json` into a local Drift / SQLite database on first launch and after a catalog version change. No network is required after install.

## Technical debt

- Catalog updates ship with the app until a signed content-pack channel exists.
- Drift web WASM files must stay in step with the Drift and sqlite3 package versions.
- Factory torque figures that are not public are not invented. Those steps tell you to measure and to use the service sequence you have, not a guessed newton-metre value.
