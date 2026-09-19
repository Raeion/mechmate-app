import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import 'app_info.dart';
import 'routing/app_router.dart';
import 'theme/app_theme.dart';

class MechmateApp extends ConsumerWidget {
  MechmateApp({super.key});

  final _router = createRouter();

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return MaterialApp.router(
      title: AppInfo.name,
      debugShowCheckedModeBanner: false,
      theme: AppTheme.dark(),
      themeMode: ThemeMode.dark,
      routerConfig: _router,
    );
  }
}
