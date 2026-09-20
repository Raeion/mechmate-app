import 'package:flutter/material.dart';

import '../theme/workshop_art.dart';
import 'workshop_image.dart';

/// First-run sheet. Voice comes from Unity MechMate:
/// "Your mate in mech" plus the disclaimer panel that opened on launch.
class MateWelcome extends StatelessWidget {
  const MateWelcome({super.key, required this.onAccept});

  final VoidCallback onAccept;

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    return AlertDialog(
      title: const Text('Your mate in mech'),
      content: SingleChildScrollView(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            const ClipRRect(
              borderRadius: BorderRadius.all(Radius.circular(16)),
              child: AspectRatio(
                aspectRatio: 4 / 3,
                child: WorkshopImage(
                  asset: WorkshopArt.welcome,
                  semanticLabel: 'Workshop bay',
                ),
              ),
            ),
            const SizedBox(height: 16),
            Text(
              'Welcome to Mechmate. This is a workshop companion. '
              'Lock out the job first, then run the tests and finish the repair. '
              'The first MechMate split cars by electrical, noise, leak, smell, '
              'steering, tyres, vibration, glass, and body. Those paths are still '
              'on the home screen. Stay clear of wet fuel, a hot DPF, and live 48V '
              'cables. The catalog keeps growing.',
              style: theme.textTheme.bodyMedium,
            ),
          ],
        ),
      ),
      actions: [FilledButton(onPressed: onAccept, child: const Text('Got it'))],
    );
  }
}
