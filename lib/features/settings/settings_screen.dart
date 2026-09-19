import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../app_info.dart';
import '../../data/providers.dart';
import '../../legal/legal_copy.dart';
import '../../widgets/error_state.dart';
import '../../widgets/mate_welcome.dart';

class SettingsScreen extends ConsumerWidget {
  const SettingsScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final catalog = ref.watch(catalogProvider);

    return Scaffold(
      appBar: AppBar(title: const Text('Settings')),
      body: ListView(
        padding: const EdgeInsets.fromLTRB(16, 8, 16, 32),
        children: [
          Text('About', style: Theme.of(context).textTheme.titleLarge),
          const SizedBox(height: 8),
          Card(
            child: ListTile(
              title: const Text(AppInfo.name),
              subtitle: Text(
                catalog.when(
                  data: (repo) =>
                      'App ${AppInfo.version}  •  Catalog ${repo.snapshot.version}',
                  loading: () =>
                      'App ${AppInfo.version}  •  Loading catalog',
                  error: (_, _) =>
                      'App ${AppInfo.version}  •  Catalog failed to open',
                ),
              ),
            ),
          ),
          const SizedBox(height: 8),
          const Card(
            child: ListTile(
              title: Text(AppInfo.tagline),
              subtitle: Text(
                'Offline workshop companion. Diagnose, test, and finish the job.',
              ),
            ),
          ),
          const SizedBox(height: 20),
          Text('Legal', style: Theme.of(context).textTheme.titleLarge),
          const SizedBox(height: 8),
          for (final doc in LegalDoc.values)
            Card(
              child: ListTile(
                title: Text(legalTitle(doc)),
                trailing: const Icon(Icons.chevron_right),
                onTap: () => context.push('/legal/${legalId(doc)}'),
              ),
            ),
          const SizedBox(height: 20),
          Text('Welcome', style: Theme.of(context).textTheme.titleLarge),
          const SizedBox(height: 8),
          Card(
            child: ListTile(
              title: const Text('Read the welcome again'),
              subtitle: const Text('Your mate in mech'),
              onTap: () async {
                final garage = await ref.read(garageProvider.future);
                if (!context.mounted) {
                  return;
                }
                await showDialog<void>(
                  context: context,
                  builder: (dialogContext) {
                    return MateWelcome(
                      onAccept: () async {
                        await garage.acceptDisclaimer();
                        if (dialogContext.mounted) {
                          Navigator.of(dialogContext).pop();
                        }
                      },
                    );
                  },
                );
              },
            ),
          ),
          catalog.maybeWhen(
            error: (_, _) => Padding(
              padding: const EdgeInsets.only(top: 20),
              child: ErrorState(
                message:
                    'The local catalog failed to open. Restart the app. If it keeps failing, reinstall so the bundled database can copy again.',
                onRetry: () => ref.invalidate(catalogProvider),
              ),
            ),
            orElse: () => const SizedBox.shrink(),
          ),
        ],
      ),
    );
  }
}
