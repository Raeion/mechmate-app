import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:mechmate/theme/app_theme.dart';
import 'package:mechmate/widgets/empty_state.dart';
import 'package:mechmate/widgets/mate_welcome.dart';
import 'package:mechmate/widgets/safety_banner.dart';

void main() {
  testWidgets('empty state shows the action', (tester) async {
    var tapped = false;
    await tester.pumpWidget(
      MaterialApp(
        theme: AppTheme.dark(),
        home: Scaffold(
          body: EmptyState(
            title: 'No vehicle selected',
            message: 'Add a Hilux to filter the catalog.',
            actionLabel: 'Open garage',
            onAction: () => tapped = true,
          ),
        ),
      ),
    );
    expect(find.text('No vehicle selected'), findsOneWidget);
    await tester.tap(find.text('Open garage'));
    expect(tapped, isTrue);
  });

  testWidgets('safety banner lists lock-out steps', (tester) async {
    await tester.pumpWidget(
      MaterialApp(
        theme: AppTheme.dark(),
        home: const Scaffold(
          body: SafetyBanner(
            items: ['Support the vehicle on rated stands.'],
          ),
        ),
      ),
    );
    expect(find.text('Lock out the job first'), findsOneWidget);
    expect(find.text('Support the vehicle on rated stands.'), findsOneWidget);
  });

  testWidgets('mate welcome uses the original voice', (tester) async {
    var accepted = false;
    await tester.pumpWidget(
      MaterialApp(
        theme: AppTheme.dark(),
        home: MateWelcome(onAccept: () => accepted = true),
      ),
    );
    expect(find.text('Your mate in mech'), findsOneWidget);
    expect(find.textContaining('A mate for your Car'), findsNothing);
    await tester.tap(find.text('Got it'));
    expect(accepted, isTrue);
  });
}
