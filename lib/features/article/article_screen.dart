import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../data/models/catalog_models.dart';
import '../../data/providers.dart';
import '../../widgets/empty_state.dart';
import '../../widgets/error_state.dart';
import '../../widgets/safety_banner.dart';

class ArticleScreen extends ConsumerWidget {
  const ArticleScreen({super.key, required this.articleId});

  final String articleId;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final catalog = ref.watch(catalogProvider);

    return catalog.when(
      loading: () =>
          const Scaffold(body: Center(child: CircularProgressIndicator())),
      error: (_, _) => Scaffold(
        body: ErrorState(
          message:
              'The local catalog failed to open. Restart the app and open the job again.',
          onRetry: () => ref.invalidate(catalogProvider),
        ),
      ),
      data: (repo) {
        final article = repo.article(articleId);
        if (article == null) {
          return Scaffold(
            appBar: AppBar(),
            body: EmptyState(
              title: 'Article missing',
              message: 'This job is not in the local catalog.',
              actionLabel: 'Home',
              onAction: () => context.go('/'),
            ),
          );
        }
        return _ArticleBody(article: article);
      },
    );
  }
}

class _ArticleBody extends ConsumerStatefulWidget {
  const _ArticleBody({required this.article});

  final Article article;

  @override
  ConsumerState<_ArticleBody> createState() => _ArticleBodyState();
}

class _ArticleBodyState extends ConsumerState<_ArticleBody> {
  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((_) async {
      final garage = await ref.read(garageProvider.future);
      await garage.setLastArticle(widget.article.id);
    });
  }

  @override
  Widget build(BuildContext context) {
    final article = widget.article;
    final catalog = ref.watch(catalogProvider).value;
    return Scaffold(
      appBar: AppBar(title: Text(article.title)),
      body: ListView(
        padding: const EdgeInsets.fromLTRB(16, 8, 16, 32),
        children: [
          Text(article.summary, style: Theme.of(context).textTheme.titleMedium),
          const SizedBox(height: 12),
          Wrap(
            spacing: 8,
            children: [
              Chip(label: Text(_severityLabel(article.severity))),
              for (final symptom in article.symptoms.take(4))
                Chip(label: Text(symptom)),
            ],
          ),
          const SizedBox(height: 16),
          SafetyBanner(items: article.safety),
          const SizedBox(height: 16),
          Text('Tools', style: Theme.of(context).textTheme.titleLarge),
          const SizedBox(height: 8),
          Card(
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  for (final tool in article.tools)
                    Padding(
                      padding: const EdgeInsets.only(bottom: 6),
                      child: Text('•  $tool'),
                    ),
                ],
              ),
            ),
          ),
          const SizedBox(height: 20),
          Text(
            'Ranked causes and the test that proves them',
            style: Theme.of(context).textTheme.titleLarge,
          ),
          const SizedBox(height: 8),
          for (final cause in article.causes) _CauseCard(cause: cause),
          if (article.specs.isNotEmpty) ...[
            const SizedBox(height: 12),
            Text(
              'Numbers you can use',
              style: Theme.of(context).textTheme.titleLarge,
            ),
            const SizedBox(height: 8),
            for (final spec in article.specs)
              ListTile(
                contentPadding: EdgeInsets.zero,
                title: Text(spec.name),
                subtitle: Text(
                  spec.note == null
                      ? spec.value
                      : '${spec.value}. ${spec.note}',
                ),
              ),
          ],
          if (article.parts.isNotEmpty) ...[
            const SizedBox(height: 8),
            Text('Parts', style: Theme.of(context).textTheme.titleLarge),
            const SizedBox(height: 8),
            for (final part in article.parts) Text('•  $part'),
          ],
          if (article.related.isNotEmpty) ...[
            const SizedBox(height: 16),
            Text('Related jobs', style: Theme.of(context).textTheme.titleLarge),
            const SizedBox(height: 8),
            Wrap(
              spacing: 8,
              children: [
                for (final id in article.related)
                  ActionChip(
                    label: Text(
                      catalog?.article(id)?.title ?? id.replaceAll('-', ' '),
                    ),
                    onPressed: () => context.push('/article/$id'),
                  ),
              ],
            ),
          ],
          if (article.sources.isNotEmpty) ...[
            const SizedBox(height: 16),
            Text('Sources', style: Theme.of(context).textTheme.titleLarge),
            const SizedBox(height: 8),
            for (final source in article.sources)
              Text('•  ${source.title} (${source.url})'),
          ],
        ],
      ),
    );
  }

  String _severityLabel(Severity severity) {
    return switch (severity) {
      Severity.low => 'Low risk if you stop at the test',
      Severity.medium => 'Medium. Confirm before replacing parts',
      Severity.high => 'High. Do not drive until the test passes',
      Severity.critical => 'Critical. Isolate and support the vehicle first',
    };
  }
}

class _CauseCard extends StatelessWidget {
  const _CauseCard({required this.cause});

  final Cause cause;

  @override
  Widget build(BuildContext context) {
    return Card(
      child: ExpansionTile(
        title: Text('${cause.rank}. ${cause.name}'),
        subtitle: Text('${cause.likelihood}  •  ${cause.why}'),
        childrenPadding: const EdgeInsets.fromLTRB(16, 0, 16, 16),
        children: [
          for (final test in cause.tests) ...[
            Align(
              alignment: Alignment.centerLeft,
              child: Text(
                'Test: ${test.name}',
                style: Theme.of(context).textTheme.titleSmall,
              ),
            ),
            const SizedBox(height: 4),
            Text(test.how),
            const SizedBox(height: 8),
            Text('Pass: ${test.pass}'),
            Text('Fail: ${test.fail}'),
            const SizedBox(height: 12),
          ],
          Text('Fix', style: Theme.of(context).textTheme.titleSmall),
          const SizedBox(height: 6),
          for (var index = 0; index < cause.fix.length; index++)
            Padding(
              padding: const EdgeInsets.only(bottom: 6),
              child: Text('${index + 1}. ${cause.fix[index]}'),
            ),
        ],
      ),
    );
  }
}
