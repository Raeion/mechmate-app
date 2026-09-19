import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../data/models/catalog_models.dart';
import '../../data/providers.dart';
import '../../widgets/article_tile.dart';
import '../../widgets/empty_state.dart';
import '../../widgets/error_state.dart';

class SearchScreen extends ConsumerStatefulWidget {
  const SearchScreen({super.key, this.initialQuery = ''});

  final String initialQuery;

  @override
  ConsumerState<SearchScreen> createState() => _SearchScreenState();
}

class _SearchScreenState extends ConsumerState<SearchScreen> {
  late final TextEditingController _controller;
  List<Article> _results = const [];
  bool _loading = false;
  String? _error;

  @override
  void initState() {
    super.initState();
    _controller = TextEditingController(text: widget.initialQuery);
    if (widget.initialQuery.trim().isNotEmpty) {
      WidgetsBinding.instance.addPostFrameCallback((_) {
        _runSearch(widget.initialQuery);
      });
    }
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  Future<void> _runSearch(String query) async {
    setState(() {
      _loading = true;
      _error = null;
    });
    try {
      final repo = await ref.read(catalogProvider.future);
      final vehicle = await ref.read(activeVehicleProvider.future);
      final results = await repo.search(query, vehicle: vehicle);
      if (!mounted) {
        return;
      }
      setState(() {
        _results = results;
        _loading = false;
      });
    } catch (_) {
      if (!mounted) {
        return;
      }
      setState(() {
        _error =
            'Search failed. Try again. If it keeps failing, restart the app so the local catalog can open.';
        _loading = false;
      });
    }
  }

  Widget _body() {
    if (_error != null) {
      return ErrorState(
        message: _error!,
        onRetry: () => _runSearch(_controller.text),
      );
    }
    if (_controller.text.trim().isEmpty) {
      return const EmptyState(
        title: 'Search the bay',
        message:
            'Try a noise, a leak colour, a lamp, an engine code, or a part name.',
      );
    }
    if (_results.isEmpty) {
      return const EmptyState(
        title: 'No hits',
        message:
            'Try a shorter word, a system name, or browse by where the problem is.',
      );
    }
    return ListView.separated(
      itemCount: _results.length,
      separatorBuilder: (_, _) => const SizedBox(height: 8),
      itemBuilder: (context, index) {
        final article = _results[index];
        return ArticleTile(
          article: article,
          onTap: () => context.push('/article/${article.id}'),
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Search')),
      body: Padding(
        padding: const EdgeInsets.fromLTRB(16, 8, 16, 24),
        child: Column(
          children: [
            TextField(
              controller: _controller,
              autofocus: widget.initialQuery.isEmpty,
              textInputAction: TextInputAction.search,
              decoration: const InputDecoration(
                labelText: 'Search jobs',
                hintText: 'DPF, fifth injector, 48V belt, white smoke',
                prefixIcon: Icon(Icons.search),
              ),
              onSubmitted: _runSearch,
            ),
            const SizedBox(height: 16),
            if (_loading) const LinearProgressIndicator(),
            Expanded(child: _body()),
          ],
        ),
      ),
    );
  }
}
