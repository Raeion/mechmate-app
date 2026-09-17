import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../data/models/catalog_models.dart';
import '../../data/providers.dart';
import '../../widgets/category_card.dart';
import '../../widgets/empty_state.dart';
import '../../widgets/error_state.dart';

class HomeScreen extends ConsumerWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final catalog = ref.watch(catalogProvider);
    final vehicle = ref.watch(activeVehicleProvider);
    return catalog.when(
      loading: () => const Scaffold(body: Center(child: CircularProgressIndicator())),
      error: (error, _) => Scaffold(body: ErrorState(message: '$error', onRetry: () => ref.invalidate(catalogProvider))),
      data: (repo) {
        final locations = repo.locations();
        final senses = repo.senses();
        final systems = repo.systems();
        return Scaffold(
          appBar: AppBar(
            title: const Text('Mechmate'),
            actions: [IconButton(tooltip: 'Garage', onPressed: () => context.push('/garage'), icon: const Icon(Icons.garage_outlined))],
          ),
          body: ListView(
            padding: const EdgeInsets.fromLTRB(16, 8, 16, 32),
            children: [
              vehicle.when(
                loading: () => const SizedBox.shrink(),
                error: (_, _) => const SizedBox.shrink(),
                data: (active) => active == null
                    ? EmptyState(title: 'Add the car in the bay', message: 'Pick a make, model, year and engine so results stay relevant.', actionLabel: 'Open garage', onAction: () => context.push('/garage'))
                    : Card(child: ListTile(leading: const Icon(Icons.precision_manufacturing), title: Text(active.label), subtitle: Text(active.is48v ? '48V system selected.' : 'Filtering the catalog to this vehicle.'), trailing: const Icon(Icons.chevron_right), onTap: () => context.push('/garage'))),
              ),
              const SizedBox(height: 16),
              TextField(textInputAction: TextInputAction.search, decoration: const InputDecoration(hintText: 'Search a sound, leak, code, or part', prefixIcon: Icon(Icons.search)), onSubmitted: (value) => context.push('/search?q=${Uri.encodeQueryComponent(value)}')),
              const SizedBox(height: 16),
              Text('Where is it', style: Theme.of(context).textTheme.titleLarge),
              const SizedBox(height: 8),
              GridView.count(shrinkWrap: true, physics: const NeverScrollableScrollPhysics(), crossAxisCount: MediaQuery.sizeOf(context).width > 720 ? 4 : 2, childAspectRatio: 1.15, mainAxisSpacing: 10, crossAxisSpacing: 10, children: [for (final item in locations) CategoryCard(item: item, onTap: () => context.push('/browse/location/${item.id}'))]),
              const SizedBox(height: 20),
              Text('How it shows up', style: Theme.of(context).textTheme.titleLarge),
              const SizedBox(height: 8),
              SizedBox(height: 150, child: ListView.separated(scrollDirection: Axis.horizontal, itemCount: senses.length, separatorBuilder: (_, _) => const SizedBox(width: 10), itemBuilder: (context, index) { final item = senses[index]; return SizedBox(width: 180, child: CategoryCard(item: item, compact: true, onTap: () => context.push('/browse/sense/${item.id}'))); })),
              const SizedBox(height: 20),
              Text('Systems', style: Theme.of(context).textTheme.titleLarge),
              const SizedBox(height: 8),
              Wrap(spacing: 8, runSpacing: 8, children: [for (final item in systems) ActionChip(avatar: Icon(iconForName(item.icon), size: 18), label: Text(item.title), onPressed: () => context.push('/browse/system/${item.id}'))]),
            ],
          ),
        );
      },
    );
  }
}
