import 'database/app_database.dart'
    hide Article, Make, Generation, Engine, VehicleVariant, Model, ArticleFilter;
import 'models/catalog_models.dart';

class CatalogRepository {
  CatalogRepository(this._db, this.snapshot);

  final AppDatabase _db;
  final CatalogSnapshot snapshot;

  static Future<CatalogRepository> open(AppDatabase db) async {
    await db.seedFromAssetIfNeeded();
    final snapshot = await db.loadSnapshot();
    return CatalogRepository(db, snapshot);
  }

  List<TaxonomyItem> locations() => snapshot.tagsOf(TagKind.location);
  List<TaxonomyItem> senses() => snapshot.tagsOf(TagKind.sense);
  List<TaxonomyItem> systems() => snapshot.tagsOf(TagKind.system);

  List<Article> articlesFor({
    required TagKind kind,
    required String tagId,
    GarageVehicle? vehicle,
  }) {
    return snapshot.articlesForTag(kind: kind, tagId: tagId, vehicle: vehicle);
  }

  Article? article(String id) => snapshot.articleById(id);

  Future<List<Article>> search(String query, {GarageVehicle? vehicle}) async {
    final ids = await _db.searchArticleIds(query);
    if (ids.isEmpty) {
      final needle = query.toLowerCase();
      return snapshot.articles.where((article) {
        if (!article.matchesVehicle(vehicle)) {
          return false;
        }
        return article.searchText.toLowerCase().contains(needle);
      }).toList();
    }
    final byId = {for (final article in snapshot.articles) article.id: article};
    return ids
        .map((id) => byId[id])
        .whereType<Article>()
        .where((article) => article.matchesVehicle(vehicle))
        .toList();
  }

  Make? makeById(String id) {
    for (final make in snapshot.makes) {
      if (make.id == id) {
        return make;
      }
    }
    return null;
  }

  VehicleModel? modelById(String id) {
    for (final model in snapshot.models) {
      if (model.id == id) {
        return model;
      }
    }
    return null;
  }

  Generation? generationById(String id) {
    for (final generation in snapshot.generations) {
      if (generation.id == id) {
        return generation;
      }
    }
    return null;
  }

  Engine? engineById(String id) {
    for (final engine in snapshot.engines) {
      if (engine.id == id) {
        return engine;
      }
    }
    return null;
  }

  List<VehicleVariant> variantsFor({
    required String generationId,
    required String engineId,
  }) {
    return snapshot.variants
        .where(
          (variant) =>
              variant.generationId == generationId &&
              variant.engineId == engineId,
        )
        .toList();
  }
}
