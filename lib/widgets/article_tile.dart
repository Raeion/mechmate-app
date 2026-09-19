import 'package:flutter/material.dart';

import '../data/models/catalog_models.dart';

class ArticleTile extends StatelessWidget {
  const ArticleTile({
    super.key,
    required this.article,
    required this.onTap,
  });

  final Article article;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    return Card(
      child: ListTile(
        contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
        title: Text(article.title),
        subtitle: Padding(
          padding: const EdgeInsets.only(top: 6),
          child: Text(
            article.summary,
            maxLines: 2,
            overflow: TextOverflow.ellipsis,
          ),
        ),
        trailing: _SeverityChip(severity: article.severity),
        onTap: onTap,
      ),
    );
  }
}

class _SeverityChip extends StatelessWidget {
  const _SeverityChip({required this.severity});

  final Severity severity;

  @override
  Widget build(BuildContext context) {
    final label = switch (severity) {
      Severity.low => 'Low',
      Severity.medium => 'Medium',
      Severity.high => 'High',
      Severity.critical => 'Critical',
    };
    return Chip(
      visualDensity: VisualDensity.compact,
      label: Text(label),
    );
  }
}
