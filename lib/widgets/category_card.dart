import 'package:flutter/material.dart';

import '../data/models/catalog_models.dart';

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
    return Card(
      clipBehavior: Clip.antiAlias,
      child: InkWell(
        onTap: onTap,
        child: Semantics(
          button: true,
          label: item.title,
          hint: item.subtitle,
          child: Padding(
            padding: EdgeInsets.all(compact ? 14 : 16),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Icon(
                  iconForName(item.icon),
                  color: Theme.of(context).colorScheme.primary,
                ),
                const Spacer(),
                Text(
                  item.title,
                  style: Theme.of(context).textTheme.titleMedium,
                ),
                const SizedBox(height: 4),
                Text(
                  item.subtitle,
                  maxLines: 2,
                  overflow: TextOverflow.ellipsis,
                  style: Theme.of(context).textTheme.bodySmall,
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
