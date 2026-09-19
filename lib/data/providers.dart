import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:shared_preferences/shared_preferences.dart';

import 'catalog_repository.dart';
import 'database/app_database.dart';
import 'garage_repository.dart';
import 'models/catalog_models.dart';

final sharedPreferencesProvider = FutureProvider<SharedPreferences>((
  ref,
) async {
  return SharedPreferences.getInstance();
});

final databaseProvider = Provider<AppDatabase>((ref) {
  final db = AppDatabase();
  ref.onDispose(db.close);
  return db;
});

final catalogProvider = FutureProvider<CatalogRepository>((ref) async {
  final db = ref.watch(databaseProvider);
  return CatalogRepository.open(db);
});

final garageProvider = FutureProvider<GarageRepository>((ref) async {
  final prefs = await ref.watch(sharedPreferencesProvider.future);
  return GarageRepository(prefs);
});

final activeVehicleProvider = FutureProvider<GarageVehicle?>((ref) async {
  final garage = await ref.watch(garageProvider.future);
  return garage.activeVehicle();
});
