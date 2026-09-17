# Manifest

Last compiled catalog version: `2026.09.17.2`

## Application

| Path | Role |
| --- | --- |
| [../lib/main.dart](../lib/main.dart) | ProviderScope entry |
| [../lib/app.dart](../lib/app.dart) | MaterialApp.router |
| [../lib/theme/app_theme.dart](../lib/theme/app_theme.dart) | Dark workshop theme |
| [../lib/routing/app_router.dart](../lib/routing/app_router.dart) | Home, garage, search, browse, article |
| [../lib/data/database/app_database.dart](../lib/data/database/app_database.dart) | Drift schema, FTS5, JSON seed import |
| [../lib/data/catalog_repository.dart](../lib/data/catalog_repository.dart) | Query API over the snapshot |
| [../lib/data/garage_repository.dart](../lib/data/garage_repository.dart) | Saved vehicles, offline |
| [../lib/features/home/home_screen.dart](../lib/features/home/home_screen.dart) | Category launch plus original mate paths |
| [../lib/data/heritage_paths.dart](../lib/data/heritage_paths.dart) | Unity VDH tiles mapped to Flutter routes |
| [../lib/widgets/mate_welcome.dart](../lib/widgets/mate_welcome.dart) | First-run "Your mate in mech" sheet |
| [../lib/features/garage/garage_screen.dart](../lib/features/garage/garage_screen.dart) | Vehicle picker including 48V |
| [../lib/features/browse/browse_screen.dart](../lib/features/browse/browse_screen.dart) | Filtered article lists |
| [../lib/features/article/article_screen.dart](../lib/features/article/article_screen.dart) | Test-then-fix reader |
| [../lib/features/search/search_screen.dart](../lib/features/search/search_screen.dart) | FTS plus fallback text search |

## Catalog sources

| Path | Role |
| --- | --- |
| [../tool/catalog_taxonomy.py](../tool/catalog_taxonomy.py) | Location, sense, system tags |
| [../tool/catalog_vehicles.py](../tool/catalog_vehicles.py) | Makes, models, generations, engines, variants |
| [../tool/articles_hilux.py](../tool/articles_hilux.py) | Hilux N50/N70/N80/V-Active articles |
| [../tool/articles_48v.py](../tool/articles_48v.py) | Shared 48V / MHEV chapter |
| [../tool/articles_universal.py](../tool/articles_universal.py) | Cross-vehicle systems |
| [../tool/articles_au.py](../tool/articles_au.py) | Ranger, D-Max, Prado, and other AU volume models |
| [../tool/articles_heritage.py](../tool/articles_heritage.py) | Unity graph coverage: leak, steering tree, vibration, glass, smell |
| [../tool/compile_catalog.py](../tool/compile_catalog.py) | Writes YAML, JSON, and SQLite |

## Generated artifacts

| Path | Role |
| --- | --- |
| [../data/taxonomy.yaml](../data/taxonomy.yaml) | Human-readable taxonomy |
| [../data/vehicles.yaml](../data/vehicles.yaml) | Human-readable vehicle tree |
| [../data/articles/hilux.yaml](../data/articles/hilux.yaml) | Hilux article export |
| [../data/articles/forty_eight_volt.yaml](../data/articles/forty_eight_volt.yaml) | 48V article export |
| [../data/articles/universal.yaml](../data/articles/universal.yaml) | Universal article export |
| [../data/articles/australia.yaml](../data/articles/australia.yaml) | AU overlay export |
| [../data/articles/heritage.yaml](../data/articles/heritage.yaml) | Heritage article export |
| [../assets/data/catalog.json](../assets/data/catalog.json) | Bundled seed the app imports |
| [../assets/data/mechmate.db](../assets/data/mechmate.db) | Compiled SQLite snapshot in the repo |

## Coverage snapshot

- 106 diagnostic articles (93 plus 13 heritage jobs from the Unity graphs)
- 15 makes
- 43 models
- Hilux generations: N50, N70, N80, N80 V-Active 48V
- 48V / MHEV variants on Hilux V-Active, Mercedes EQ Boost, BMW, Audi, and VW eTSI
- Universal systems apply even when a model overlay does not exist yet

## Tests

| Path | Role |
| --- | --- |
| [../test/catalog_matching_test.dart](../test/catalog_matching_test.dart) | Vehicle filters, 48V gating, taxonomy |
| [../test/widget_test.dart](../test/widget_test.dart) | Empty state, safety banner, mate welcome |

## Heritage notes

See [heritage.md](heritage.md). The Unity keystore and Firebase files were not copied.
