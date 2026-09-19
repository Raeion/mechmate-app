enum Severity { low, medium, high, critical }

enum TagKind { location, sense, system }

Severity severityFromString(String value) {
  switch (value) {
    case 'low':
      return Severity.low;
    case 'medium':
      return Severity.medium;
    case 'high':
      return Severity.high;
    case 'critical':
      return Severity.critical;
    default:
      throw ArgumentError('Unknown severity: $value');
  }
}

TagKind tagKindFromString(String value) {
  switch (value) {
    case 'location':
      return TagKind.location;
    case 'sense':
      return TagKind.sense;
    case 'system':
      return TagKind.system;
    default:
      throw ArgumentError('Unknown tag kind: $value');
  }
}

class TaxonomyItem {
  const TaxonomyItem({
    required this.id,
    required this.kind,
    required this.title,
    required this.subtitle,
    required this.icon,
    required this.sortOrder,
  });

  final String id;
  final TagKind kind;
  final String title;
  final String subtitle;
  final String icon;
  final int sortOrder;

  factory TaxonomyItem.fromJson(Map<String, dynamic> json) {
    return TaxonomyItem(
      id: json['id'] as String,
      kind: tagKindFromString(json['kind'] as String),
      title: json['title'] as String,
      subtitle: json['subtitle'] as String,
      icon: json['icon'] as String,
      sortOrder: json['sortOrder'] as int,
    );
  }
}

class Make {
  const Make({required this.id, required this.name});

  final String id;
  final String name;

  factory Make.fromJson(Map<String, dynamic> json) {
    return Make(id: json['id'] as String, name: json['name'] as String);
  }
}

class VehicleModel {
  const VehicleModel({
    required this.id,
    required this.makeId,
    required this.name,
    required this.bodyType,
  });

  final String id;
  final String makeId;
  final String name;
  final String bodyType;

  factory VehicleModel.fromJson(Map<String, dynamic> json) {
    return VehicleModel(
      id: json['id'] as String,
      makeId: json['makeId'] as String,
      name: json['name'] as String,
      bodyType: json['bodyType'] as String,
    );
  }
}

class Generation {
  const Generation({
    required this.id,
    required this.modelId,
    required this.code,
    required this.name,
    required this.yearFrom,
    this.yearTo,
  });

  final String id;
  final String modelId;
  final String code;
  final String name;
  final int yearFrom;
  final int? yearTo;

  factory Generation.fromJson(Map<String, dynamic> json) {
    return Generation(
      id: json['id'] as String,
      modelId: json['modelId'] as String,
      code: json['code'] as String,
      name: json['name'] as String,
      yearFrom: json['yearFrom'] as int,
      yearTo: json['yearTo'] as int?,
    );
  }

  String get yearLabel {
    final end = yearTo?.toString() ?? 'present';
    return '$yearFrom-$end';
  }
}

class Engine {
  const Engine({
    required this.id,
    required this.code,
    required this.fuel,
    required this.displacementL,
    this.notes,
  });

  final String id;
  final String code;
  final String fuel;
  final String displacementL;
  final String? notes;

  factory Engine.fromJson(Map<String, dynamic> json) {
    return Engine(
      id: json['id'] as String,
      code: json['code'] as String,
      fuel: json['fuel'] as String,
      displacementL: json['displacementL'] as String,
      notes: json['notes'] as String?,
    );
  }
}

class VehicleVariant {
  const VehicleVariant({
    required this.id,
    required this.generationId,
    required this.engineId,
    required this.drivetrain,
    required this.is48v,
    this.voltageLabel,
  });

  final String id;
  final String generationId;
  final String engineId;
  final String drivetrain;
  final bool is48v;
  final String? voltageLabel;

  factory VehicleVariant.fromJson(Map<String, dynamic> json) {
    return VehicleVariant(
      id: json['id'] as String,
      generationId: json['generationId'] as String,
      engineId: json['engineId'] as String,
      drivetrain: json['drivetrain'] as String,
      is48v: json['is48v'] as bool? ?? false,
      voltageLabel: json['voltageLabel'] as String?,
    );
  }
}

class ArticleFilter {
  const ArticleFilter({
    required this.articleId,
    this.generationId,
    this.engineId,
    this.modelId,
    this.yearFrom,
    this.yearTo,
    this.requires48v = false,
    this.universal = false,
  });

  final String articleId;
  final String? generationId;
  final String? engineId;
  final String? modelId;
  final int? yearFrom;
  final int? yearTo;
  final bool requires48v;
  final bool universal;

  factory ArticleFilter.fromJson(Map<String, dynamic> json) {
    return ArticleFilter(
      articleId: json['articleId'] as String,
      generationId: json['generationId'] as String?,
      engineId: json['engineId'] as String?,
      modelId: json['modelId'] as String?,
      yearFrom: json['yearFrom'] as int?,
      yearTo: json['yearTo'] as int?,
      requires48v: json['requires48v'] as bool? ?? false,
      universal: json['universal'] as bool? ?? false,
    );
  }

  bool matches({
    String? generationId,
    String? engineId,
    String? modelId,
    int? year,
    bool? is48v,
  }) {
    if (universal) {
      return true;
    }
    if (this.generationId != null &&
        generationId != null &&
        this.generationId != generationId) {
      return false;
    }
    if (this.engineId != null && engineId != null && this.engineId != engineId) {
      return false;
    }
    if (this.modelId != null && modelId != null && this.modelId != modelId) {
      return false;
    }
    if (year != null) {
      if (yearFrom != null && year < yearFrom!) {
        return false;
      }
      if (yearTo != null && year > yearTo!) {
        return false;
      }
    }
    if (requires48v && is48v != true) {
      return false;
    }
    return true;
  }
}

class DiagnosticTest {
  const DiagnosticTest({
    required this.name,
    required this.how,
    required this.pass,
    required this.fail,
  });

  final String name;
  final String how;
  final String pass;
  final String fail;

  factory DiagnosticTest.fromJson(Map<String, dynamic> json) {
    return DiagnosticTest(
      name: json['name'] as String,
      how: json['how'] as String,
      pass: json['pass'] as String,
      fail: json['fail'] as String,
    );
  }
}

class Cause {
  const Cause({
    required this.rank,
    required this.name,
    required this.likelihood,
    required this.why,
    required this.tests,
    required this.fix,
  });

  final int rank;
  final String name;
  final String likelihood;
  final String why;
  final List<DiagnosticTest> tests;
  final List<String> fix;

  factory Cause.fromJson(Map<String, dynamic> json) {
    return Cause(
      rank: json['rank'] as int,
      name: json['name'] as String,
      likelihood: json['likelihood'] as String,
      why: json['why'] as String,
      tests: (json['tests'] as List<dynamic>)
          .map((item) => DiagnosticTest.fromJson(item as Map<String, dynamic>))
          .toList(),
      fix: (json['fix'] as List<dynamic>).cast<String>(),
    );
  }
}

class Spec {
  const Spec({required this.name, required this.value, this.note});

  final String name;
  final String value;
  final String? note;

  factory Spec.fromJson(Map<String, dynamic> json) {
    return Spec(
      name: json['name'] as String,
      value: json['value'] as String,
      note: json['note'] as String?,
    );
  }
}

class Source {
  const Source({required this.title, required this.url});

  final String title;
  final String url;

  factory Source.fromJson(Map<String, dynamic> json) {
    return Source(title: json['title'] as String, url: json['url'] as String);
  }
}

class Article {
  const Article({
    required this.id,
    required this.title,
    required this.summary,
    required this.severity,
    required this.symptoms,
    required this.safety,
    required this.tools,
    required this.causes,
    required this.specs,
    required this.parts,
    required this.sources,
    required this.related,
    required this.locationIds,
    required this.senseIds,
    required this.systemIds,
    required this.filters,
  });

  final String id;
  final String title;
  final String summary;
  final Severity severity;
  final List<String> symptoms;
  final List<String> safety;
  final List<String> tools;
  final List<Cause> causes;
  final List<Spec> specs;
  final List<String> parts;
  final List<Source> sources;
  final List<String> related;
  final List<String> locationIds;
  final List<String> senseIds;
  final List<String> systemIds;
  final List<ArticleFilter> filters;

  factory Article.fromJson(Map<String, dynamic> json) {
    return Article(
      id: json['id'] as String,
      title: json['title'] as String,
      summary: json['summary'] as String,
      severity: severityFromString(json['severity'] as String),
      symptoms: (json['symptoms'] as List<dynamic>).cast<String>(),
      safety: (json['safety'] as List<dynamic>).cast<String>(),
      tools: (json['tools'] as List<dynamic>).cast<String>(),
      causes: (json['causes'] as List<dynamic>)
          .map((item) => Cause.fromJson(item as Map<String, dynamic>))
          .toList()
        ..sort((a, b) => a.rank.compareTo(b.rank)),
      specs: (json['specs'] as List<dynamic>? ?? [])
          .map((item) => Spec.fromJson(item as Map<String, dynamic>))
          .toList(),
      parts: (json['parts'] as List<dynamic>? ?? []).cast<String>(),
      sources: (json['sources'] as List<dynamic>? ?? [])
          .map((item) => Source.fromJson(item as Map<String, dynamic>))
          .toList(),
      related: (json['related'] as List<dynamic>? ?? []).cast<String>(),
      locationIds: (json['locations'] as List<dynamic>).cast<String>(),
      senseIds: (json['senses'] as List<dynamic>).cast<String>(),
      systemIds: (json['systems'] as List<dynamic>).cast<String>(),
      filters: (json['filters'] as List<dynamic>? ?? [])
          .map(
            (item) => ArticleFilter.fromJson({
              ...item as Map<String, dynamic>,
              'articleId': json['id'],
            }),
          )
          .toList(),
    );
  }

  bool matchesVehicle(GarageVehicle? vehicle) {
    if (vehicle == null) {
      return true;
    }
    if (filters.isEmpty) {
      return true;
    }
    return filters.any(
      (filter) => filter.matches(
        generationId: vehicle.generationId,
        engineId: vehicle.engineId,
        modelId: vehicle.modelId,
        year: vehicle.year,
        is48v: vehicle.is48v,
      ),
    );
  }

  String get searchText {
    final buffer = StringBuffer()
      ..write(title)
      ..write(' ')
      ..write(summary)
      ..write(' ')
      ..writeAll(symptoms, ' ')
      ..write(' ');
    for (final cause in causes) {
      buffer
        ..write(cause.name)
        ..write(' ')
        ..write(cause.why)
        ..write(' ');
    }
    return buffer.toString();
  }
}

class GarageVehicle {
  const GarageVehicle({
    required this.id,
    required this.makeId,
    required this.modelId,
    required this.generationId,
    required this.engineId,
    required this.year,
    required this.is48v,
    required this.label,
  });

  final String id;
  final String makeId;
  final String modelId;
  final String generationId;
  final String engineId;
  final int year;
  final bool is48v;
  final String label;

  Map<String, dynamic> toJson() => {
    'id': id,
    'makeId': makeId,
    'modelId': modelId,
    'generationId': generationId,
    'engineId': engineId,
    'year': year,
    'is48v': is48v,
    'label': label,
  };

  factory GarageVehicle.fromJson(Map<String, dynamic> json) {
    return GarageVehicle(
      id: json['id'] as String,
      makeId: json['makeId'] as String,
      modelId: json['modelId'] as String,
      generationId: json['generationId'] as String,
      engineId: json['engineId'] as String,
      year: json['year'] as int,
      is48v: json['is48v'] as bool? ?? false,
      label: json['label'] as String,
    );
  }
}

class CatalogSnapshot {
  const CatalogSnapshot({
    required this.version,
    required this.taxonomy,
    required this.makes,
    required this.models,
    required this.generations,
    required this.engines,
    required this.variants,
    required this.articles,
  });

  final String version;
  final List<TaxonomyItem> taxonomy;
  final List<Make> makes;
  final List<VehicleModel> models;
  final List<Generation> generations;
  final List<Engine> engines;
  final List<VehicleVariant> variants;
  final List<Article> articles;

  factory CatalogSnapshot.fromJson(Map<String, dynamic> json) {
    return CatalogSnapshot(
      version: json['version'] as String,
      taxonomy: (json['taxonomy'] as List<dynamic>)
          .map((item) => TaxonomyItem.fromJson(item as Map<String, dynamic>))
          .toList(),
      makes: (json['makes'] as List<dynamic>)
          .map((item) => Make.fromJson(item as Map<String, dynamic>))
          .toList(),
      models: (json['models'] as List<dynamic>)
          .map((item) => VehicleModel.fromJson(item as Map<String, dynamic>))
          .toList(),
      generations: (json['generations'] as List<dynamic>)
          .map((item) => Generation.fromJson(item as Map<String, dynamic>))
          .toList(),
      engines: (json['engines'] as List<dynamic>)
          .map((item) => Engine.fromJson(item as Map<String, dynamic>))
          .toList(),
      variants: (json['variants'] as List<dynamic>)
          .map((item) => VehicleVariant.fromJson(item as Map<String, dynamic>))
          .toList(),
      articles: (json['articles'] as List<dynamic>)
          .map((item) => Article.fromJson(item as Map<String, dynamic>))
          .toList(),
    );
  }

  List<TaxonomyItem> tagsOf(TagKind kind) {
    final items = taxonomy.where((item) => item.kind == kind).toList()
      ..sort((a, b) => a.sortOrder.compareTo(b.sortOrder));
    return items;
  }

  TaxonomyItem? tagById(String id) {
    for (final item in taxonomy) {
      if (item.id == id) {
        return item;
      }
    }
    return null;
  }

  Article? articleById(String id) {
    for (final article in articles) {
      if (article.id == id) {
        return article;
      }
    }
    return null;
  }

  List<Article> articlesForTag({
    required TagKind kind,
    required String tagId,
    GarageVehicle? vehicle,
  }) {
    return articles.where((article) {
      final ids = switch (kind) {
        TagKind.location => article.locationIds,
        TagKind.sense => article.senseIds,
        TagKind.system => article.systemIds,
      };
      if (!ids.contains(tagId)) {
        return false;
      }
      return article.matchesVehicle(vehicle);
    }).toList();
  }
}
