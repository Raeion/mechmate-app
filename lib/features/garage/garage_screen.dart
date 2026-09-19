import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../data/models/catalog_models.dart';
import '../../data/providers.dart';
import '../../widgets/empty_state.dart';
import '../../widgets/error_state.dart';

class GarageScreen extends ConsumerWidget {
  const GarageScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final catalog = ref.watch(catalogProvider);
    final garage = ref.watch(garageProvider);

    return catalog.when(
      loading: () =>
          const Scaffold(body: Center(child: CircularProgressIndicator())),
      error: (_, _) => Scaffold(
        body: ErrorState(
          message:
              'The local catalog failed to open. Restart the app. If it keeps failing, reinstall so the bundled database can copy again.',
          onRetry: () => ref.invalidate(catalogProvider),
        ),
      ),
      data: (repo) {
        return garage.when(
          loading: () =>
              const Scaffold(body: Center(child: CircularProgressIndicator())),
          error: (_, _) => Scaffold(
            body: ErrorState(
              message:
                  'The garage list failed to open. Restart the app and try again.',
              onRetry: () => ref.invalidate(garageProvider),
            ),
          ),
          data: (store) {
            final vehicles = store.vehicles();
            final active = store.activeVehicle();
            return Scaffold(
              appBar: AppBar(title: const Text('Garage')),
              floatingActionButton: FloatingActionButton.extended(
                onPressed: () => _openEditor(context, ref),
                icon: const Icon(Icons.add),
                label: const Text('Add vehicle'),
              ),
              body: vehicles.isEmpty
                  ? EmptyState(
                      title: 'No vehicle selected',
                      message:
                          'Add a Hilux, Ranger, Prado, or any catalogued AU vehicle. 48V variants show a V-Active or MHEV badge.',
                      actionLabel: 'Add vehicle',
                      onAction: () => _openEditor(context, ref),
                    )
                  : ListView(
                      padding: const EdgeInsets.fromLTRB(16, 8, 16, 100),
                      children: [
                        for (final vehicle in vehicles)
                          Card(
                            child: ListTile(
                              leading: Icon(
                                active?.id == vehicle.id
                                    ? Icons.radio_button_checked
                                    : Icons.radio_button_off,
                              ),
                              title: Text(vehicle.label),
                              subtitle: Text(
                                vehicle.is48v
                                    ? '48V mild hybrid. Test 12V and DC-DC before the pack.'
                                    : '12V architecture',
                              ),
                              onTap: () async {
                                await store.setActive(vehicle.id);
                                ref.invalidate(garageProvider);
                                ref.invalidate(activeVehicleProvider);
                              },
                              trailing: IconButton(
                                tooltip: 'Remove',
                                onPressed: () async {
                                  final confirmed = await showDialog<bool>(
                                    context: context,
                                    builder: (dialogContext) {
                                      return AlertDialog(
                                        title: const Text('Remove vehicle'),
                                        content: Text(
                                          'Remove ${vehicle.label} from the garage? The catalog stays on the device.',
                                        ),
                                        actions: [
                                          TextButton(
                                            onPressed: () => Navigator.of(
                                              dialogContext,
                                            ).pop(false),
                                            child: const Text('Keep'),
                                          ),
                                          FilledButton(
                                            onPressed: () => Navigator.of(
                                              dialogContext,
                                            ).pop(true),
                                            child: const Text('Remove'),
                                          ),
                                        ],
                                      );
                                    },
                                  );
                                  if (confirmed != true) {
                                    return;
                                  }
                                  await store.removeVehicle(vehicle.id);
                                  ref.invalidate(garageProvider);
                                  ref.invalidate(activeVehicleProvider);
                                },
                                icon: const Icon(Icons.delete_outline),
                              ),
                            ),
                          ),
                      ],
                    ),
            );
          },
        );
      },
    );
  }

  Future<void> _openEditor(BuildContext context, WidgetRef ref) async {
    await showModalBottomSheet<void>(
      context: context,
      isScrollControlled: true,
      builder: (context) => const _VehicleEditor(),
    );
    ref.invalidate(garageProvider);
    ref.invalidate(activeVehicleProvider);
  }
}

class _VehicleEditor extends ConsumerStatefulWidget {
  const _VehicleEditor();

  @override
  ConsumerState<_VehicleEditor> createState() => _VehicleEditorState();
}

class _VehicleEditorState extends ConsumerState<_VehicleEditor> {
  String? _makeId;
  String? _modelId;
  String? _generationId;
  String? _engineId;
  int? _year;
  bool _is48v = false;

  @override
  Widget build(BuildContext context) {
    final catalog = ref.watch(catalogProvider).value;
    if (catalog == null) {
      return const Padding(
        padding: EdgeInsets.all(24),
        child: CircularProgressIndicator(),
      );
    }
    final snapshot = catalog.snapshot;
    final models = snapshot.models
        .where((model) => _makeId == null || model.makeId == _makeId)
        .toList();
    final generations = snapshot.generations
        .where((generation) => generation.modelId == _modelId)
        .toList();
    final engineIds = snapshot.variants
        .where((variant) => variant.generationId == _generationId)
        .map((variant) => variant.engineId)
        .toSet();
    final engines = snapshot.engines
        .where((engine) => engineIds.contains(engine.id))
        .toList();
    final years = _yearOptions();
    final variants = _generationId == null || _engineId == null
        ? const <VehicleVariant>[]
        : catalog.variantsFor(
            generationId: _generationId!,
            engineId: _engineId!,
          );
    final has48v = variants.any((variant) => variant.is48v);

    return Padding(
      padding: EdgeInsets.fromLTRB(
        16,
        16,
        16,
        16 + MediaQuery.viewInsetsOf(context).bottom,
      ),
      child: SingleChildScrollView(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Text('Add a vehicle', style: Theme.of(context).textTheme.titleLarge),
            const SizedBox(height: 16),
            DropdownButtonFormField<String>(
              // ignore: deprecated_member_use
              value: _makeId,
              decoration: const InputDecoration(labelText: 'Make'),
              items: [
                for (final make in snapshot.makes)
                  DropdownMenuItem(value: make.id, child: Text(make.name)),
              ],
              onChanged: (value) {
                setState(() {
                  _makeId = value;
                  _modelId = null;
                  _generationId = null;
                  _engineId = null;
                  _year = null;
                  _is48v = false;
                });
              },
            ),
            const SizedBox(height: 12),
            DropdownButtonFormField<String>(
              // ignore: deprecated_member_use
              value: _modelId,
              decoration: const InputDecoration(labelText: 'Model'),
              items: [
                for (final model in models)
                  DropdownMenuItem(value: model.id, child: Text(model.name)),
              ],
              onChanged: _makeId == null
                  ? null
                  : (value) {
                      setState(() {
                        _modelId = value;
                        _generationId = null;
                        _engineId = null;
                        _year = null;
                        _is48v = false;
                      });
                    },
            ),
            const SizedBox(height: 12),
            DropdownButtonFormField<String>(
              // ignore: deprecated_member_use
              value: _generationId,
              decoration: const InputDecoration(labelText: 'Generation'),
              items: [
                for (final generation in generations)
                  DropdownMenuItem(
                    value: generation.id,
                    child: Text(
                      '${generation.name} ${generation.yearLabel}',
                    ),
                  ),
              ],
              onChanged: _modelId == null
                  ? null
                  : (value) {
                      setState(() {
                        _generationId = value;
                        _engineId = null;
                        _year = null;
                        _is48v = false;
                      });
                    },
            ),
            const SizedBox(height: 12),
            DropdownButtonFormField<String>(
              // ignore: deprecated_member_use
              value: _engineId,
              decoration: const InputDecoration(labelText: 'Engine'),
              items: [
                for (final engine in engines)
                  DropdownMenuItem(
                    value: engine.id,
                    child: Text(
                      '${engine.code} ${engine.displacementL} ${engine.fuel}',
                    ),
                  ),
              ],
              onChanged: _generationId == null
                  ? null
                  : (value) {
                      setState(() {
                        _engineId = value;
                        _is48v = false;
                      });
                    },
            ),
            const SizedBox(height: 12),
            DropdownButtonFormField<int>(
              // ignore: deprecated_member_use
              value: _year,
              decoration: const InputDecoration(labelText: 'Year'),
              items: [
                for (final year in years)
                  DropdownMenuItem(value: year, child: Text('$year')),
              ],
              onChanged: _generationId == null
                  ? null
                  : (value) => setState(() => _year = value),
            ),
            if (has48v) ...[
              const SizedBox(height: 8),
              SwitchListTile(
                contentPadding: EdgeInsets.zero,
                title: const Text('48V V-Active / MHEV'),
                subtitle: const Text(
                  'Belt motor-generator and DC-DC. Always load-test the 12V battery first.',
                ),
                value: _is48v,
                onChanged: (value) => setState(() => _is48v = value),
              ),
            ],
            const SizedBox(height: 16),
            FilledButton(
              onPressed: _canSave
                  ? () async {
                      final garage = await ref.read(garageProvider.future);
                      final make = catalog.makeById(_makeId!)!.name;
                      final model = catalog.modelById(_modelId!)!.name;
                      final engine = catalog.engineById(_engineId!)!.code;
                      final label =
                          '$make $model $_year $engine${_is48v ? ' 48V' : ''}';
                      await garage.addVehicle(
                        GarageVehicle(
                          id: DateTime.now().millisecondsSinceEpoch.toString(),
                          makeId: _makeId!,
                          modelId: _modelId!,
                          generationId: _generationId!,
                          engineId: _engineId!,
                          year: _year!,
                          is48v: _is48v,
                          label: label,
                        ),
                      );
                      if (context.mounted) {
                        Navigator.of(context).pop();
                      }
                    }
                  : null,
              child: const Text('Save to garage'),
            ),
          ],
        ),
      ),
    );
  }

  bool get _canSave =>
      _makeId != null &&
      _modelId != null &&
      _generationId != null &&
      _engineId != null &&
      _year != null;

  List<int> _yearOptions() {
    final catalog = ref.read(catalogProvider).value;
    if (catalog == null || _generationId == null) {
      return const [];
    }
    final generation = catalog.generationById(_generationId!);
    if (generation == null) {
      return const [];
    }
    final end = generation.yearTo ?? DateTime.now().year;
    return [for (var year = generation.yearFrom; year <= end; year++) year];
  }
}
