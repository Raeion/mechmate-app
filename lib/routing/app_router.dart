import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

import '../features/article/article_screen.dart';
import '../features/browse/browse_screen.dart';
import '../features/garage/garage_screen.dart';
import '../features/home/home_screen.dart';
import '../features/legal/legal_screen.dart';
import '../features/search/search_screen.dart';
import '../features/settings/settings_screen.dart';
import '../widgets/empty_state.dart';

GoRouter createRouter() {
  return GoRouter(
    errorBuilder: (context, state) {
      return Scaffold(
        appBar: AppBar(title: const Text('Mechmate')),
        body: EmptyState(
          title: 'That page is not here',
          message:
              'The link is missing or the catalog moved. Go home and search from there.',
          actionLabel: 'Home',
          onAction: () => context.go('/'),
        ),
      );
    },
    routes: [
      GoRoute(path: '/', builder: (context, state) => const HomeScreen()),
      GoRoute(
        path: '/garage',
        builder: (context, state) => const GarageScreen(),
      ),
      GoRoute(
        path: '/settings',
        builder: (context, state) => const SettingsScreen(),
      ),
      GoRoute(
        path: '/legal/:doc',
        builder: (context, state) =>
            LegalScreen(docId: state.pathParameters['doc']!),
      ),
      GoRoute(
        path: '/search',
        builder: (context, state) =>
            SearchScreen(initialQuery: state.uri.queryParameters['q'] ?? ''),
      ),
      GoRoute(
        path: '/browse/:kind/:id',
        builder: (context, state) => BrowseScreen(
          kind: state.pathParameters['kind']!,
          tagId: state.pathParameters['id']!,
        ),
      ),
      GoRoute(
        path: '/article/:id',
        builder: (context, state) =>
            ArticleScreen(articleId: state.pathParameters['id']!),
      ),
    ],
  );
}
