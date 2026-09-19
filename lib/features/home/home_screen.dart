import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../data/heritage_paths.dart';
import '../../data/models/catalog_models.dart';
import '../../data/providers.dart';
import '../../widgets/category_card.dart';
import '../../widgets/empty_state.dart';
import '../../widgets/error_state.dart';
import '../../widgets/mate_welcome.dart';

class HomeScreen extends ConsumerStatefulWidget {
  const HomeScreen({super.key});

  @override
  ConsumerState<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends ConsumerState<HomeScreen> {
  bool _welcomeScheduled = false;

  void _maybeShowWelcome() {
    if (_welcomeScheduled) {
      return;
    }
    _welcomeScheduled = true;
    WidgetsBinding.instance.addPostFrameCallback((_) async {
      if (!mounted) {
        return;
      }
      final garage = await ref.read(garageProvider.future);
      if (!mounted || garage.hasAcceptedDisclaimer()) {
        return;
      }
      await showDialog<void>(
        context: context,
        barrierDismissible: false,
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
    });
  }

  @override
  Widget build(BuildContext context) {
    final catalog = ref.watch(catalogProvider);
    final vehicle = ref.watch(activeVehicleProvider);

    return catalog.when(
      loading: () => const Scaffold(
        body: Center(child: CircularProgressIndicator()),
      ),
      error: (_, _) => Scaffold(
        body: ErrorState(
          message:
              'The local catalog failed to open. Restart the app. If it keeps failing, reinstall so the bundled database can copy again.',
          onRetry: () => ref.invalidate(catalogProvider),
        ),
      ),
      data: (repo) {
        _maybeShowWelcome();
        final locations = repo.locations();
        final senses = repo.senses();
        final systems = repo.systems();
        return Scaffold(
          appBar: AppBar(
            title: const Text('Mechmate'),
            actions: [
              IconButton(
                tooltip: 'Garage',
                onPressed: () => context.push('/garage'),
                icon: const Icon(Icons.garage_outlined),
              ),
              IconButton(
                tooltip: 'Settings',
                onPressed: () => context.push('/settings'),
                icon: const Icon(Icons.settings_outlined),
              ),
            ],
          ),
          body: ListView(
            padding: const EdgeInsets.fromLTRB(16, 8, 16, 32),
            children: [
              vehicle.when(
                loading: () => const SizedBox.shrink(),
                error: (_, _) => const SizedBox.shrink(),
                data: (active) => _GarageBanner(vehicle: active),
              ),
              const SizedBox(height: 12),
              ref.watch(garageProvider).when(
                loading: () => const SizedBox.shrink(),
                error: (_, _) => const SizedBox.shrink(),
                data: (store) {
                  final lastId = store.lastArticleId();
                  if (lastId == null) {
                    return const SizedBox.shrink();
                  }
                  final last = repo.article(lastId);
                  if (last == null) {
                    return const SizedBox.shrink();
                  }
                  return Card(
                    child: ListTile(
                      leading: const Icon(Icons.history),
                      title: const Text('Continue last job'),
                      subtitle: Text(last.title),
                      trailing: const Icon(Icons.chevron_right),
                      onTap: () => context.push('/article/${last.id}'),
                    ),
                  );
                },
              ),
              const SizedBox(height: 16),
              TextField(
                textInputAction: TextInputAction.search,
                decoration: const InputDecoration(
                  labelText: 'Search the catalog',
                  hintText: 'Search a sound, leak, code, or part',
                  prefixIcon: Icon(Icons.search),
                ),
                onSubmitted: (value) {
                  context.push('/search?q=${Uri.encodeQueryComponent(value)}');
                },
              ),
              const SizedBox(height: 12),
              Align(
                alignment: Alignment.centerLeft,
                child: TextButton.icon(
                  onPressed: () => context.push('/search'),
                  icon: const Icon(Icons.tune),
                  label: const Text('Open full search'),
                ),
              ),
              const SizedBox(height: 8),
              Text(
                'A mate for your Car',
                style: Theme.of(context).textTheme.titleLarge,
              ),
              const SizedBox(height: 4),
              Text(
                'The first MechMate split jobs these ten ways. Same paths, with tests and repairs now.',
                style: Theme.of(context).textTheme.bodyMedium,
              ),
              const SizedBox(height: 12),
              Wrap(
                spacing: 8,
                runSpacing: 8,
                children: [
                  for (final path in originalMatePaths)
                    ActionChip(
                      avatar: Icon(iconForName(path.icon), size: 18),
                      label: Text(path.title),
                      tooltip: path.subtitle,
                      onPressed: () => context.push(path.route),
                    ),
                ],
              ),
              const SizedBox(height: 20),
              Text('Where is it', style: Theme.of(context).textTheme.titleLarge),
              const SizedBox(height: 8),
              GridView.count(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                crossAxisCount: MediaQuery.sizeOf(context).width > 720 ? 4 : 2,
                childAspectRatio: 1.15,
                mainAxisSpacing: 10,
                crossAxisSpacing: 10,
                children: [
                  for (final item in locations)
                    CategoryCard(
                      item: item,
                      onTap: () => context.push('/browse/location/${item.id}'),
                    ),
                ],
              ),
              const SizedBox(height: 20),
              Text(
                'How it shows up',
                style: Theme.of(context).textTheme.titleLarge,
              ),
              const SizedBox(height: 8),
              SizedBox(
                height: 150,
                child: ListView.separated(
                  scrollDirection: Axis.horizontal,
                  itemCount: senses.length,
                  separatorBuilder: (_, _) => const SizedBox(width: 10),
                  itemBuilder: (context, index) {
                    final item = senses[index];
                    return SizedBox(
                      width: 180,
                      child: CategoryCard(
                        item: item,
                        compact: true,
                        onTap: () => context.push('/browse/sense/${item.id}'),
                      ),
                    );
                  },
                ),
              ),
              const SizedBox(height: 20),
              Text('Systems', style: Theme.of(context).textTheme.titleLarge),
              const SizedBox(height: 8),
              Wrap(
                spacing: 8,
                runSpacing: 8,
                children: [
                  for (final item in systems)
                    ActionChip(
                      avatar: Icon(iconForName(item.icon), size: 18),
                      label: Text(item.title),
                      onPressed: () =>
                          context.push('/browse/system/${item.id}'),
                    ),
                ],
              ),
            ],
          ),
        );
      },
    );
  }
}

class _GarageBanner extends StatelessWidget {
  const _GarageBanner({required this.vehicle});

  final GarageVehicle? vehicle;

  @override
  Widget build(BuildContext context) {
    if (vehicle == null) {
      return EmptyState(
        title: 'Add the car in the bay',
        message:
            'Pick a make, model, year and engine so results stay relevant. Hilux and 48V V-Active are first-class. Or start from a mate path below.',
        actionLabel: 'Open garage',
        onAction: () => context.push('/garage'),
      );
    }
    return Card(
      child: ListTile(
        leading: const Icon(Icons.precision_manufacturing),
        title: Text(vehicle!.label),
        subtitle: Text(
          vehicle!.is48v
              ? '48V system selected. Electrical tests start on the 12V battery.'
              : 'Filtering the catalog to this vehicle.',
        ),
        trailing: const Icon(Icons.chevron_right),
        onTap: () => context.push('/garage'),
      ),
    );
  }
}
