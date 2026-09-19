import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class AppTheme {
  static const Color steel = Color(0xFF1B2430);
  static const Color panel = Color(0xFF243044);
  static const Color amber = Color(0xFFE8A317);
  static const Color cream = Color(0xFFF4EFE6);

  static ThemeData dark() {
    final base = ColorScheme.fromSeed(
      seedColor: amber,
      brightness: Brightness.dark,
    );
    return ThemeData(
      useMaterial3: true,
      colorScheme: base.copyWith(
        surface: steel,
        primary: amber,
        onPrimary: const Color(0xFF1A1406),
        secondary: const Color(0xFF7FB3C8),
      ),
      scaffoldBackgroundColor: steel,
      cardTheme: CardThemeData(
        color: panel,
        elevation: 0,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(18)),
      ),
      appBarTheme: const AppBarTheme(
        backgroundColor: steel,
        foregroundColor: cream,
        elevation: 0,
        centerTitle: false,
        systemOverlayStyle: SystemUiOverlayStyle.light,
      ),
      textTheme: Typography.whiteMountainView.apply(
        bodyColor: cream,
        displayColor: cream,
      ),
      inputDecorationTheme: InputDecorationTheme(
        filled: true,
        fillColor: panel,
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(16),
          borderSide: BorderSide.none,
        ),
      ),
    );
  }
}
