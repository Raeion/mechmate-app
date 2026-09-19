import 'dart:convert';

import 'package:drift/drift.dart';
import 'package:drift_flutter/drift_flutter.dart';
import 'package:flutter/services.dart';

import '../models/catalog_models.dart' as catalog;

part 'app_database.g.dart';

class Makes extends Table {
  TextColumn get id => text()();
  TextColumn get name => text()();

  @override
  Set<Column<Object>> get primaryKey => {id};
}

class Models extends Table {
  TextColumn get id => text()();
  TextColumn get makeId => text()();
  TextColumn get name => text()();
  TextColumn get bodyType => text()();

  @override
  Set<Column<Object>> get primaryKey => {id};
}

class Generations extends Table {
  TextColumn get id => text()();
  TextColumn get modelId => text()();
  TextColumn get code => text()();
  TextColumn get name => text()();
  IntColumn get yearFrom => integer()();
  IntColumn get yearTo => integer().nullable()();

  @override
  Set<Column<Object>> get primaryKey => {id};
}

class Engines extends Table {
  TextColumn get id => text()();
  TextColumn get code => text()();
  TextColumn get fuel => text()();
  TextColumn get displacementL => text()();
  TextColumn get notes => text().nullable()();

  @override
  Set<Column<Object>> get primaryKey => {id};
}

class VehicleVariants extends Table {
  TextColumn get id => text()();
  TextColumn get generationId => text()();
  TextColumn get engineId => text()();
  TextColumn get drivetrain => text()();
  BoolColumn get is48v => boolean().withDefault(const Constant(false))();
  TextColumn get voltageLabel => text().nullable()();

  @override
  Set<Column<Object>> get primaryKey => {id};
}

class Articles extends Table {
  TextColumn get id => text()();
  TextColumn get title => text()();
  TextColumn get summary => text()();
  TextColumn get severity => text()();
  TextColumn get bodyJson => text()();

  @override
  Set<Column<Object>> get primaryKey => {id};
}

class ArticleTags extends Table {
  IntColumn get id => integer().autoIncrement()();
  TextColumn get articleId => text()();
  TextColumn get kind => text()();
  TextColumn get tagId => text()();
}

class ArticleFilters extends Table {
  IntColumn get id => integer().autoIncrement()();
  TextColumn get articleId => text()();
  TextColumn get generationId => text().nullable()();
  TextColumn get engineId => text().nullable()();
  TextColumn get modelId => text().nullable()();
  IntColumn get yearFrom => integer().nullable()();
  IntColumn get yearTo => integer().nullable()();
  BoolColumn get requires48v => boolean().withDefault(const Constant(false))();
  BoolColumn get universal => boolean().withDefault(const Constant(false))();
}

class Taxonomy extends Table {
  TextColumn get id => text()();
  TextColumn get kind => text()();
  TextColumn get title => text()();
  TextColumn get subtitle => text()();
  TextColumn get icon => text()();
  IntColumn get sortOrder => integer()();

  @override
  Set<Column<Object>> get primaryKey => {id};
}

class MetaEntries extends Table {
  TextColumn get key => text()();
  TextColumn get value => text()();

  @override
  Set<Column<Object>> get primaryKey => {key};
}

@DriftDatabase(
  tables: [
    Makes,
    Models,
    Generations,
    Engines,
    VehicleVariants,
    Articles,
    ArticleTags,
    ArticleFilters,
    Taxonomy,
    MetaEntries,
  ],
)
class AppDatabase extends _$AppDatabase {
  AppDatabase() : super(_openConnection());

  AppDatabase.forTesting(super.e);

  @override
  int get schemaVersion => 1;

  @override
  MigrationStrategy get migration {
    return MigrationStrategy(
      onCreate: (Migrator migrator) async {
        await migrator.createAll();
        await customStatement('''
CREATE VIRTUAL TABLE IF NOT EXISTS articles_fts USING fts5(
  article_id UNINDEXED,
  title,
  summary,
  body,
  tokenize = 'unicode61'
);
''');
      },
    );
  }

  static QueryExecutor _openConnection() {
    return driftDatabase(
      name: 'mechmate',
      web: DriftWebOptions(
        sqlite3Wasm: Uri.parse('sqlite3.wasm'),
        driftWorker: Uri.parse('drift_worker.js'),
      ),
    );
  }

  Future<void> seedFromAssetIfNeeded() async {
    final existing = await (select(
      metaEntries,
    )..where((row) => row.key.equals('catalog_version'))).getSingleOrNull();
    final raw = await rootBundle.loadString('assets/data/catalog.json');
    final json = jsonDecode(raw) as Map<String, dynamic>;
    final version = json['version'] as String;
    if (existing?.value == version) {
      return;
    }
    await _replaceCatalog(json, version);
  }

  Future<void> seedFromJson(Map<String, dynamic> json) async {
    await _replaceCatalog(json, json['version'] as String);
  }

  Future<void> _replaceCatalog(
    Map<String, dynamic> json,
    String version,
  ) async {
    await transaction(() async {
      await customStatement('DELETE FROM articles_fts');
      await delete(articleFilters).go();
      await delete(articleTags).go();
      await delete(articles).go();
      await delete(vehicleVariants).go();
      await delete(engines).go();
      await delete(generations).go();
      await delete(models).go();
      await delete(makes).go();
      await delete(taxonomy).go();
      await delete(metaEntries).go();

      await batch((batch) {
        batch.insertAll(
          makes,
          (json['makes'] as List<dynamic>).map((item) {
            final row = item as Map<String, dynamic>;
            return MakesCompanion.insert(
              id: row['id'] as String,
              name: row['name'] as String,
            );
          }),
        );
        batch.insertAll(
          models,
          (json['models'] as List<dynamic>).map((item) {
            final row = item as Map<String, dynamic>;
            return ModelsCompanion.insert(
              id: row['id'] as String,
              makeId: row['makeId'] as String,
              name: row['name'] as String,
              bodyType: row['bodyType'] as String,
            );
          }),
        );
        batch.insertAll(
          generations,
          (json['generations'] as List<dynamic>).map((item) {
            final row = item as Map<String, dynamic>;
            return GenerationsCompanion.insert(
              id: row['id'] as String,
              modelId: row['modelId'] as String,
              code: row['code'] as String,
              name: row['name'] as String,
              yearFrom: row['yearFrom'] as int,
              yearTo: Value(row['yearTo'] as int?),
            );
          }),
        );
        batch.insertAll(
          engines,
          (json['engines'] as List<dynamic>).map((item) {
            final row = item as Map<String, dynamic>;
            return EnginesCompanion.insert(
              id: row['id'] as String,
              code: row['code'] as String,
              fuel: row['fuel'] as String,
              displacementL: row['displacementL'] as String,
              notes: Value(row['notes'] as String?),
            );
          }),
        );
        batch.insertAll(
          vehicleVariants,
          (json['variants'] as List<dynamic>).map((item) {
            final row = item as Map<String, dynamic>;
            return VehicleVariantsCompanion.insert(
              id: row['id'] as String,
              generationId: row['generationId'] as String,
              engineId: row['engineId'] as String,
              drivetrain: row['drivetrain'] as String,
              is48v: Value(row['is48v'] as bool? ?? false),
              voltageLabel: Value(row['voltageLabel'] as String?),
            );
          }),
        );
        batch.insertAll(
          taxonomy,
          (json['taxonomy'] as List<dynamic>).map((item) {
            final row = item as Map<String, dynamic>;
            return TaxonomyCompanion.insert(
              id: row['id'] as String,
              kind: row['kind'] as String,
              title: row['title'] as String,
              subtitle: row['subtitle'] as String,
              icon: row['icon'] as String,
              sortOrder: row['sortOrder'] as int,
            );
          }),
        );
      });

      for (final item in json['articles'] as List<dynamic>) {
        final article = item as Map<String, dynamic>;
        final id = article['id'] as String;
        await into(articles).insert(
          ArticlesCompanion.insert(
            id: id,
            title: article['title'] as String,
            summary: article['summary'] as String,
            severity: article['severity'] as String,
            bodyJson: jsonEncode(article),
          ),
        );
        for (final location in article['locations'] as List<dynamic>) {
          await into(articleTags).insert(
            ArticleTagsCompanion.insert(
              articleId: id,
              kind: 'location',
              tagId: location as String,
            ),
          );
        }
        for (final sense in article['senses'] as List<dynamic>) {
          await into(articleTags).insert(
            ArticleTagsCompanion.insert(
              articleId: id,
              kind: 'sense',
              tagId: sense as String,
            ),
          );
        }
        for (final system in article['systems'] as List<dynamic>) {
          await into(articleTags).insert(
            ArticleTagsCompanion.insert(
              articleId: id,
              kind: 'system',
              tagId: system as String,
            ),
          );
        }
        final filters = article['filters'] as List<dynamic>? ?? const [];
        if (filters.isEmpty) {
          await into(articleFilters).insert(
            ArticleFiltersCompanion.insert(articleId: id, universal: const Value(true)),
          );
        } else {
          for (final filter in filters) {
            final row = filter as Map<String, dynamic>;
            await into(articleFilters).insert(
              ArticleFiltersCompanion.insert(
                articleId: id,
                generationId: Value(row['generationId'] as String?),
                engineId: Value(row['engineId'] as String?),
                modelId: Value(row['modelId'] as String?),
                yearFrom: Value(row['yearFrom'] as int?),
                yearTo: Value(row['yearTo'] as int?),
                requires48v: Value(row['requires48v'] as bool? ?? false),
                universal: Value(row['universal'] as bool? ?? false),
              ),
            );
          }
        }
        final searchBody = catalog.Article.fromJson(article).searchText;
        await customStatement(
          'INSERT INTO articles_fts (article_id, title, summary, body) VALUES (?, ?, ?, ?)',
          [id, article['title'], article['summary'], searchBody],
        );
      }

      await into(metaEntries).insert(
        MetaEntriesCompanion.insert(key: 'catalog_version', value: version),
      );
    });
  }

  Future<catalog.CatalogSnapshot> loadSnapshot() async {
    final makeRows = await select(makes).get();
    final modelRows = await select(models).get();
    final generationRows = await select(generations).get();
    final engineRows = await select(engines).get();
    final variantRows = await select(vehicleVariants).get();
    final taxonomyRows = await select(taxonomy).get();
    final articleRows = await select(articles).get();
    final versionRow = await (select(
      metaEntries,
    )..where((row) => row.key.equals('catalog_version'))).getSingleOrNull();

    return catalog.CatalogSnapshot(
      version: versionRow?.value ?? 'unknown',
      taxonomy: taxonomyRows
          .map(
            (row) => catalog.TaxonomyItem(
              id: row.id,
              kind: catalog.tagKindFromString(row.kind),
              title: row.title,
              subtitle: row.subtitle,
              icon: row.icon,
              sortOrder: row.sortOrder,
            ),
          )
          .toList(),
      makes: makeRows
          .map((row) => catalog.Make(id: row.id, name: row.name))
          .toList(),
      models: modelRows
          .map(
            (row) => catalog.VehicleModel(
              id: row.id,
              makeId: row.makeId,
              name: row.name,
              bodyType: row.bodyType,
            ),
          )
          .toList(),
      generations: generationRows
          .map(
            (row) => catalog.Generation(
              id: row.id,
              modelId: row.modelId,
              code: row.code,
              name: row.name,
              yearFrom: row.yearFrom,
              yearTo: row.yearTo,
            ),
          )
          .toList(),
      engines: engineRows
          .map(
            (row) => catalog.Engine(
              id: row.id,
              code: row.code,
              fuel: row.fuel,
              displacementL: row.displacementL,
              notes: row.notes,
            ),
          )
          .toList(),
      variants: variantRows
          .map(
            (row) => catalog.VehicleVariant(
              id: row.id,
              generationId: row.generationId,
              engineId: row.engineId,
              drivetrain: row.drivetrain,
              is48v: row.is48v,
              voltageLabel: row.voltageLabel,
            ),
          )
          .toList(),
      articles: articleRows
          .map(
            (row) => catalog.Article.fromJson(
              jsonDecode(row.bodyJson) as Map<String, dynamic>,
            ),
          )
          .toList(),
    );
  }

  Future<List<String>> searchArticleIds(String query) async {
    final trimmed = query.trim();
    if (trimmed.isEmpty) {
      return const [];
    }
    final tokens = trimmed
        .split(RegExp(r'\s+'))
        .where((token) => token.isNotEmpty)
        .map((token) => '"${token.replaceAll('"', '')}"*')
        .join(' AND ');
    if (tokens.isEmpty) {
      return const [];
    }
    final rows = await customSelect(
      'SELECT article_id FROM articles_fts WHERE articles_fts MATCH ? ORDER BY rank',
      variables: [Variable.withString(tokens)],
    ).get();
    return rows.map((row) => row.read<String>('article_id')).toList();
  }
}
