# Workshop illustrations

Mechmate uses a small steel-and-amber picture set on the screens people land on first. Pictures are decoration. The catalog text stays the source of truth.

## What we illustrated

| Screen | Asset | Why |
| --- | --- | --- |
| Welcome | [../assets/illustrations/welcome.png](../assets/illustrations/welcome.png) | First-run sheet needs a workshop, not a blank dialog |
| Empty garage | [../assets/illustrations/empty_garage.png](../assets/illustrations/empty_garage.png) | Home banner and garage empty state |
| Active vehicle | [../assets/illustrations/vehicle_active.png](../assets/illustrations/vehicle_active.png) | Garage list and the selected-vehicle banner |
| Search empty | [../assets/illustrations/empty_search.png](../assets/illustrations/empty_search.png) | Open search with no query |
| Search no hits | [../assets/illustrations/empty_no_hits.png](../assets/illustrations/empty_no_hits.png) | Query returned nothing |
| Browse empty | [../assets/illustrations/empty_browse.png](../assets/illustrations/empty_browse.png) | Category filter has no jobs |
| Catalog error | [../assets/illustrations/error_catalog.png](../assets/illustrations/error_catalog.png) | Local database failed to open |
| Where tiles | `loc_*.png` | Home "Where is it" grid |
| Sense tiles | `sense_*.png` | Home "How it shows up" row |

Lookup lives in [../lib/theme/workshop_art.dart](../lib/theme/workshop_art.dart). Cards use [../lib/widgets/category_card.dart](../lib/widgets/category_card.dart).

## What we did not illustrate

- One picture per diagnostic article. That would be 100-plus assets and would rot next to the YAML.
- System chips on Home. Those stay icon chips. Browse for a system reuses a related location picture.
- Store launcher marks. Those stay [app-icon-1024.png](../design/app-icon-1024.png) and the generated platform icons.

## Palette

Steel `#1B2430`, panel `#243044`, amber `#E8A317`, cream `#F4EFE6`. Same tokens as [../lib/theme/app_theme.dart](../lib/theme/app_theme.dart).

## Related

- [index.md](index.md)
- [manifest.md](manifest.md)
- [ia.md](ia.md)
- [changelog.md](changelog.md)
