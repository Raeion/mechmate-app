import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../data/models/catalog_models.dart';
import '../../data/providers.dart';
import '../../widgets/article_tile.dart';
import '../../widgets/empty_state.dart';
import '../../widgets/error_state.dart';

class BrowseScreen extends ConsumerWidget {
  const BrowseScreen({super.key, required this.kind, required this.tagId});

  final String kind;
  final String tagId;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final catalog = ref.watch(catalogProvider);
    final vehicle = ref.watch(activeVehicleProvider);

    return catalog.when(
      loading: () =>
          const Scaffold(body: Center(child: CircularProgressIndicator())),
      error: (_, _) => Scaffold(
        appBar: AppBar(),
        body: ErrorState(
          message:
              'The local catalog failed to open. Restart the app and try this category again.',
          onRetry: () => ref.invalidate(catalogProvider),
        ),
      ),
      data: (repo) {
        final tagKind = tagKindFromString(kind);
        final tag = repo.snapshot.tagById(tagId);
        final articles = repo.articlesFor(
          kind: tagKind,
          tagId: tagId,
          vehicle: vehicle.value,
        );
        return Scaffold(
          appBar: AppBar(title: Text(tag?.title ?? tagId)),
          body: articles.isEmpty
              ? EmptyState(
                  title: 'No matching jobs',
                  message: vehicle.value == null
                      ? 'Nothing is tagged here yet.'
                      : 'Nothing matches ${vehicle.value!.label} in this category. Clear the garage filter or pick a related system.',
                  actionLabel: 'Change vehicle',
                  onAction: () => context.push('/garage'),
                )
              : ListView.separated(
                  padding: const EdgeInsets.fromLTRB(16, 8, 16, 32),
                  itemCount: articles.length + 1,
                  separatorBuilder: (_, _) => const SizedBox(height: 8),
                  itemBuilder: (context, index) {
                    if (index == 0) {
                      return Text(
                        tag?.subtitle ?? '',
                        style: Theme.of(context).textTheme.bodyMedium,
                      );
                    }
                    final article = articles[index - 1];
                    return ArticleTile(
                      article: article,
                      onTap: () => context.push('/article/${article.id}'),
                    );
                  },
                ),
        );
      },
    );
  }
}
