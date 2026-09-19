import 'package:flutter/material.dart';

class SafetyBanner extends StatelessWidget {
  const SafetyBanner({super.key, required this.items});

  final List<String> items;

  @override
  Widget build(BuildContext context) {
    return Card(
      color: const Color(0xFF3B2A12),
      child: Semantics(
        container: true,
        label: 'Lock out the job first',
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                'Lock out the job first',
                style: Theme.of(context).textTheme.titleMedium,
              ),
              const SizedBox(height: 8),
              for (final item in items)
                Padding(
                  padding: const EdgeInsets.only(bottom: 6),
                  child: Row(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const Text('•  '),
                      Expanded(child: Text(item)),
                    ],
                  ),
                ),
            ],
          ),
        ),
      ),
    );
  }
}
