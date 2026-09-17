# Heritage from the first MechMate apps

This Flutter catalog is a new origin at [Raeion/mechmate-app](https://github.com/Raeion/mechmate-app). The useful information came from the older private apps. Nothing was copied from keystores, Firebase configs, or workshop manuals.

## Repos inspected

| Repo | What it is | What we used |
| --- | --- | --- |
| [Raeion/MechMate](https://github.com/Raeion/MechMate) | Unity C# app, 2019. Tagline: "A mate for your Car" | Diagnostic graph names, home categories, voice |
| [Raeion/MechMate-Reborn](https://github.com/Raeion/MechMate-Reborn) | Angular 13 scaffold, 2022 | Almost nothing. Home is a placeholder dashboard. |

## What the Unity app already knew

`Assets/Scripts/DiagnosisManager.cs` and `Assets/VDH.asset` (Vehicle Diagnostic Hub) split the car into ten home paths:

1. Electrical
2. Noise
3. Fluid leak
4. Smell
5. Steering
6. Tyres
7. Vibration
8. Glass
9. Body interior
10. Body exterior

Steering already had a real tree:

- Pulling: tight caliper, brakes not bled, drum, flat tyre, alignment, wheel bearing
- Loose
- Tight: constant, every 180 degrees, low power, pump
- Vibrating

Vibration already split:

- When stationary (check pulleys)
- When braking
- While driving

Welcome copy was "Your mate in mech". First launch opened a disclaimer panel. Settings had light and dark. A no-internet popup admitted some features needed a connection.

## What we did with that

- Home shows those ten paths as "A mate for your Car" chips. They route into the Flutter taxonomy.
- Taxonomy gained `glass` (location) and `leak` (sense) so Fluid Leak and Glass are first-class again.
- New original articles in [../tool/articles_heritage.py](../tool/articles_heritage.py) cover leak colour, the steering tree, stationary and braking vibration, glass, smell, and body rust.
- First launch shows [../lib/widgets/mate_welcome.dart](../lib/widgets/mate_welcome.dart). After that the local catalog is enough. No internet warning.
- Dark workshop theme stays. Light mode from Unity is not restored in this pass.

## What we did not copy

- `MechMate.keystore`
- `google-services.json` and `GoogleService-Info.plist`
- Parse / Firebase login, Crashlytics, and the Flappy Bird easter egg
- Unity UI art, fonts, and paid plugin packs
- Any Haynes or factory manual text. The Unity graphs were node names, not procedures.

## Related

- [ia.md](ia.md)
- [manifest.md](manifest.md)
- [research/sources.md](research/sources.md)
- [index.md](index.md)
