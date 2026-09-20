/// Steel-and-amber workshop illustrations for browse tiles and empty states.
///
/// System chips stay as icons. Articles stay text-first so the catalog
/// does not grow a picture per job.
class WorkshopArt {
  static const String welcome = 'assets/illustrations/welcome.png';
  static const String emptyGarage = 'assets/illustrations/empty_garage.png';
  static const String emptySearch = 'assets/illustrations/empty_search.png';
  static const String emptyBrowse = 'assets/illustrations/empty_browse.png';
  static const String emptyNoHits = 'assets/illustrations/empty_no_hits.png';
  static const String errorCatalog = 'assets/illustrations/error_catalog.png';
  static const String vehicleActive = 'assets/illustrations/vehicle_active.png';

  static const Map<String, String> _taxonomy = {
    'inside': 'assets/illustrations/loc_inside.png',
    'outside': 'assets/illustrations/loc_outside.png',
    'engine-bay': 'assets/illustrations/loc_engine_bay.png',
    'front': 'assets/illustrations/loc_front.png',
    'rear': 'assets/illustrations/loc_rear.png',
    'under': 'assets/illustrations/loc_under.png',
    'wheels': 'assets/illustrations/loc_wheels.png',
    'electrical': 'assets/illustrations/loc_electrical.png',
    'glass': 'assets/illustrations/loc_glass.png',
    'sound': 'assets/illustrations/sense_sound.png',
    'look': 'assets/illustrations/sense_look.png',
    'leak': 'assets/illustrations/sense_leak.png',
    'performance': 'assets/illustrations/sense_performance.png',
    'smell': 'assets/illustrations/sense_smell.png',
    'feel': 'assets/illustrations/sense_feel.png',
    'engine-mechanical': 'assets/illustrations/loc_engine_bay.png',
    'fuel': 'assets/illustrations/loc_engine_bay.png',
    'air-turbo': 'assets/illustrations/loc_engine_bay.png',
    'exhaust-dpf': 'assets/illustrations/loc_rear.png',
    'cooling': 'assets/illustrations/loc_front.png',
    'lubrication': 'assets/illustrations/loc_under.png',
    'drivetrain': 'assets/illustrations/loc_under.png',
    'brakes': 'assets/illustrations/loc_wheels.png',
    'steering-suspension': 'assets/illustrations/loc_front.png',
    'hvac': 'assets/illustrations/loc_inside.png',
    'body-electrical': 'assets/illustrations/loc_electrical.png',
    'mhev-48v': 'assets/illustrations/loc_electrical.png',
  };

  static String? forTaxonomy(String id) => _taxonomy[id];

  static List<String> get allAssets => [
    welcome,
    emptyGarage,
    emptySearch,
    emptyBrowse,
    emptyNoHits,
    errorCatalog,
    vehicleActive,
    ...{..._taxonomy.values},
  ];
}
