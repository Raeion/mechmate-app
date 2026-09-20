import 'package:flutter/material.dart';

/// Bundled illustration with a steel fallback if the asset is missing.
class WorkshopImage extends StatelessWidget {
  const WorkshopImage({
    super.key,
    required this.asset,
    this.height,
    this.width,
    this.fit = BoxFit.cover,
    this.borderRadius,
    this.semanticLabel,
  });

  final String asset;
  final double? height;
  final double? width;
  final BoxFit fit;
  final BorderRadius? borderRadius;
  final String? semanticLabel;

  @override
  Widget build(BuildContext context) {
    final image = Image.asset(
      asset,
      height: height,
      width: width,
      fit: fit,
      semanticLabel: semanticLabel,
      errorBuilder: (context, error, stackTrace) {
        return ColoredBox(
          color: Theme.of(context).colorScheme.surfaceContainerHighest,
          child: Icon(
            Icons.build_circle_outlined,
            color: Theme.of(context).colorScheme.primary,
          ),
        );
      },
    );
    if (borderRadius == null) {
      return image;
    }
    return ClipRRect(borderRadius: borderRadius!, child: image);
  }
}
