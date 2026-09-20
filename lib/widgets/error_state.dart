import 'package:flutter/material.dart';

import '../theme/workshop_art.dart';
import 'workshop_image.dart';

class ErrorState extends StatelessWidget {
  const ErrorState({super.key, required this.message, this.onRetry});

  final String message;
  final VoidCallback? onRetry;

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Padding(
        padding: const EdgeInsets.all(24),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            const WorkshopImage(
              asset: WorkshopArt.errorCatalog,
              height: 140,
              width: 140,
              borderRadius: BorderRadius.all(Radius.circular(20)),
              semanticLabel: 'Catalog failed to open',
            ),
            const SizedBox(height: 12),
            Text(message, textAlign: TextAlign.center),
            if (onRetry != null) ...[
              const SizedBox(height: 16),
              FilledButton(onPressed: onRetry, child: const Text('Try again')),
            ],
          ],
        ),
      ),
    );
  }
}
