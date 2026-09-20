# Changelog

## Workshop illustrations

Home tiles, welcome, garage, search, browse, and error states now use a steel-and-amber picture set. Articles stay text-first. See [illustrations.md](illustrations.md).

## Vercel web host

Static Flutter web deploy on the Kindred Sky Projects Vercel team. No Firebase and no environment variables. See [vercel.md](vercel.md).

Production assemble now writes `assets/AssetManifest.json` and a complete `assets/FontManifest.json`, and pulls the prebuilt JS/WASM from the live host so Hobby builds do not need a Flutter SDK. SPA rewrites skip `assets/` so Flutter no longer parses `index.html` as JSON.

## 1.0.0 launch polish

In-repo work that closed launch blockers before store submission.

- Settings, privacy, terms, and the safety disclaimer are readable offline
- Unknown routes and missing legal pages recover to home or Settings
- Catalog and search errors stay user-facing. Raw exception text is not shown
- Garage asks before a vehicle is removed
- Branded steel and amber mark in [../design/app-icon-1024.png](../design/app-icon-1024.png), with iOS, Android adaptive, and web sizes from [../tool/generate_icons.py](../tool/generate_icons.py)
- Play upload signing reads `android/key.properties` when you add a keystore. See [../android/key.properties.example](../android/key.properties.example)
- Debug banner is off. App and catalog versions sit in Settings

Human store steps remain in [launch.md](launch.md).

## Related

- [index.md](index.md)
- [manifest.md](manifest.md)
- [launch.md](launch.md)
- [store-listing.md](store-listing.md)
