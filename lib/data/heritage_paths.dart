import 'models/catalog_models.dart';

/// Home tiles that match the original Unity MechMate VDH categories.
///
/// Names come from `Raeion/MechMate` `Assets/VDH.asset` and
/// `Assets/Scripts/DiagnosisManager.cs`. Routes point at the Flutter
/// taxonomy that now owns that work.
class MatePath {
  const MatePath({
    required this.title,
    required this.subtitle,
    required this.icon,
    required this.kind,
    required this.tagId,
  });

  final String title;
  final String subtitle;
  final String icon;
  final TagKind kind;
  final String tagId;

  String get route => '/browse/${kind.name}/$tagId';
}

const List<MatePath> originalMatePaths = [
  MatePath(
    title: 'Electrical',
    subtitle: 'Batteries, drain, lamps, loom heat',
    icon: 'electrical',
    kind: TagKind.location,
    tagId: 'electrical',
  ),
  MatePath(
    title: 'Noise',
    subtitle: 'Knock, tick, squeal, grind, hiss',
    icon: 'sound',
    kind: TagKind.sense,
    tagId: 'sound',
  ),
  MatePath(
    title: 'Fluid leak',
    subtitle: 'Colour, smell, then the circuit',
    icon: 'leak',
    kind: TagKind.sense,
    tagId: 'leak',
  ),
  MatePath(
    title: 'Smell',
    subtitle: 'Fuel, coolant, clutch, electrical',
    icon: 'smell',
    kind: TagKind.sense,
    tagId: 'smell',
  ),
  MatePath(
    title: 'Steering',
    subtitle: 'Pull, tight, loose, vibrating',
    icon: 'front',
    kind: TagKind.system,
    tagId: 'steering-suspension',
  ),
  MatePath(
    title: 'Tyres',
    subtitle: 'Wear, pull, pressure, bearings',
    icon: 'wheels',
    kind: TagKind.location,
    tagId: 'wheels',
  ),
  MatePath(
    title: 'Vibration',
    subtitle: 'Stationary, braking, driving',
    icon: 'feel',
    kind: TagKind.sense,
    tagId: 'feel',
  ),
  MatePath(
    title: 'Glass',
    subtitle: 'Windscreen leak, wipers, smear',
    icon: 'glass',
    kind: TagKind.location,
    tagId: 'glass',
  ),
  MatePath(
    title: 'Body interior',
    subtitle: 'Cabin rattles, HVAC, cluster',
    icon: 'cabin',
    kind: TagKind.location,
    tagId: 'inside',
  ),
  MatePath(
    title: 'Body exterior',
    subtitle: 'Paint, rust, lights, water in',
    icon: 'body',
    kind: TagKind.location,
    tagId: 'outside',
  ),
];
