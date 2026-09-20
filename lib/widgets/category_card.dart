import 'package:flutter/material.dart';

import '../data/models/catalog_models.dart';
import '../theme/workshop_art.dart';
import 'workshop_image.dart';

IconData iconForName(String name) {
  switch (name) {
    case 'cabin':
      return Icons.airline_seat_recline_normal;
    case 'body':
      return Icons.directions_car;
    case 'engine':
      return Icons.settings;
    case 'front':
      return Icons.arrow_upward;
    case 'rear':
      return Icons.arrow_downward;
    case 'under':
      return Icons.layers;
    case 'wheels':
      return Icons.tire_repair;
    case 'electrical':
      return Icons.electrical_services;
    case 'sound':
      return Icons.hearing;
    case 'look':
      return Icons.visibility;
    case 'performance':
      return Icons.speed;
    case 'smell':
      return Icons.air;
    case 'feel':
      return Icons.back_hand;
    case 'hybrid':
      return Icons.battery_charging_full;
    case 'exhaust':
      return Icons.cloud;
    case 'brakes':
      return Icons.do_not_step;
    case 'drivetrain':
      return Icons.settings_suggest;
    case 'cooling':
      return Icons.thermostat;
    case 'fuel':
      return Icons.local_gas_station;
    case 'glass':
      return Icons.crop_landscape;
    case 'leak':
      return Icons.water_drop;
    default:
      return Icons.build;
  }
}

class CategoryCard extends StatelessWidget {
  const CategoryCard({
    super.key,
    required this.item,
    required this.onTap,
    this.compact = false,
  });

  final TaxonomyItem item;
  final VoidCallback onTap;
  final bool compact;

  @override
  Widget build(BuildContext context) {
    final art = WorkshopArt.forTaxonomy(item.id);
    return Card(
      clipBehavior: Clip.antiAlias,
      child: InkWell(
        onTap: onTap,
        child: Semantics(
          button: true,
          label: item.title,
          hint: item.subtitle,
          child: SizedBox.expand(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                if (art != null)
                  Expanded(
                    flex: compact ? 3 : 4,
                    child: WorkshopImage(
                      asset: art,
                      fit: BoxFit.cover,
                      semanticLabel: item.title,
                    ),
                  ),
                Padding(
                  padding: EdgeInsets.fromLTRB(
                    compact ? 12 : 14,
                    compact ? 10 : 12,
                    compact ? 12 : 14,
                    compact ? 10 : 12,
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      if (art == null) ...[
                        Icon(
                          iconForName(item.icon),
                          color: Theme.of(context).colorScheme.primary,
                        ),
                        const SizedBox(height: 8),
                      ],
                      Text(
                        item.title,
                        maxLines: 2,
                        overflow: TextOverflow.ellipsis,
                        style: Theme.of(context).textTheme.titleMedium,
                      ),
                      const SizedBox(height: 4),
                      Text(
                        item.subtitle,
                        maxLines: compact ? 2 : 3,
                        overflow: TextOverflow.ellipsis,
                        style: Theme.of(context).textTheme.bodySmall,
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
