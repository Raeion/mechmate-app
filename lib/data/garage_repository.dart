import 'dart:convert';

import 'package:shared_preferences/shared_preferences.dart';

import 'models/catalog_models.dart';

class GarageRepository {
  GarageRepository(this._prefs);

  final SharedPreferences _prefs;

  static const _vehiclesKey = 'garage_vehicles';
  static const _activeKey = 'garage_active';
  static const _lastArticleKey = 'last_article';
  static const _disclaimerKey = 'disclaimer_accepted';

  List<GarageVehicle> vehicles() {
    final raw = _prefs.getStringList(_vehiclesKey) ?? const [];
    return raw
        .map(
          (item) =>
              GarageVehicle.fromJson(jsonDecode(item) as Map<String, dynamic>),
        )
        .toList();
  }

  GarageVehicle? activeVehicle() {
    final id = _prefs.getString(_activeKey);
    if (id == null) {
      return null;
    }
    for (final vehicle in vehicles()) {
      if (vehicle.id == id) {
        return vehicle;
      }
    }
    return null;
  }

  Future<void> addVehicle(GarageVehicle vehicle) async {
    final next = [...vehicles(), vehicle];
    await _prefs.setStringList(
      _vehiclesKey,
      next.map((item) => jsonEncode(item.toJson())).toList(),
    );
    await _prefs.setString(_activeKey, vehicle.id);
  }

  Future<void> setActive(String id) async {
    await _prefs.setString(_activeKey, id);
  }

  Future<void> removeVehicle(String id) async {
    final next = vehicles().where((vehicle) => vehicle.id != id).toList();
    await _prefs.setStringList(
      _vehiclesKey,
      next.map((item) => jsonEncode(item.toJson())).toList(),
    );
    if (activeVehicle()?.id == id) {
      if (next.isEmpty) {
        await _prefs.remove(_activeKey);
      } else {
        await _prefs.setString(_activeKey, next.first.id);
      }
    }
  }

  String? lastArticleId() => _prefs.getString(_lastArticleKey);

  Future<void> setLastArticle(String id) async {
    await _prefs.setString(_lastArticleKey, id);
  }

  bool hasAcceptedDisclaimer() => _prefs.getBool(_disclaimerKey) ?? false;

  Future<void> acceptDisclaimer() async {
    await _prefs.setBool(_disclaimerKey, true);
  }
}
