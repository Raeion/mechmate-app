import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

import '../../legal/legal_copy.dart';
import '../../widgets/empty_state.dart';

class LegalScreen extends StatelessWidget {
  const LegalScreen({super.key, required this.docId});

  final String docId;

  @override
  Widget build(BuildContext context) {
    late final LegalDoc doc;
    try {
      doc = legalDocFromId(docId);
    } on ArgumentError {
      return Scaffold(
        appBar: AppBar(title: const Text('Missing')),
        body: EmptyState(
          title: 'That legal page is not here',
          message: 'Privacy, terms, and the safety disclaimer live in Settings.',
          actionLabel: 'Settings',
          onAction: () => context.go('/settings'),
        ),
      );
    }

    return Scaffold(
      appBar: AppBar(title: Text(legalTitle(doc))),
      body: ListView(
        padding: const EdgeInsets.fromLTRB(16, 8, 16, 32),
        children: [
          SelectableText(
            legalBody(doc).trim(),
            style: Theme.of(context).textTheme.bodyLarge,
          ),
        ],
      ),
    );
  }
}
