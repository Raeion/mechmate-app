# Vercel web deploy

Mechmate on the web is a **static Flutter build**. The catalog, garage, and search run in the browser. There is no Firebase, no API, and no environment variables.

## What Vercel hosts

- `flutter build web --release` output in `build/web`
- Bundled `assets/data/catalog.json` imported into local SQLite (Drift + `sqlite3.wasm`)
- Garage state in the browser profile (`SharedPreferences`)

## Project

- Team: Kindred Sky Projects (`raeions-projects`)
- Project name: `mechmate`
- Config: [../vercel.json](../vercel.json)
- Build script: [../tool/vercel-build.sh](../tool/vercel-build.sh)

SPA routes (`/settings`, `/article/:id`) rewrite to `index.html`. Cross-origin isolation headers let the WASM worker start.

## Deploy from a machine with Flutter and the Vercel CLI

```bash
flutter build web --release --no-wasm-dry-run --base-href /
npx vercel deploy --prod --yes --scope raeions-projects
```

Or let Vercel run [../tool/vercel-build.sh](../tool/vercel-build.sh). That script installs Flutter only if the build image does not already have it. Still no backend keys.

## Related

- [launch.md](launch.md)
- [legal/privacy.md](legal/privacy.md)
- [index.md](index.md)
- [manifest.md](manifest.md)
