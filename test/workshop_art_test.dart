import 'package:flutter_test/flutter_test.dart';
import 'package:mechmate/theme/workshop_art.dart';

void main() {
  test('every location and sense tile has its own illustration', () {
    const locations = [
      'inside',
      'outside',
      'engine-bay',
      'front',
      'rear',
      'under',
      'wheels',
      'electrical',
      'glass',
    ];
    const senses = ['sound', 'look', 'leak', 'performance', 'smell', 'feel'];
    for (final id in [...locations, ...senses]) {
      expect(WorkshopArt.forTaxonomy(id), isNotNull, reason: id);
    }
  });

  test('system browse reuses a related location picture', () {
    expect(
      WorkshopArt.forTaxonomy('mhev-48v'),
      WorkshopArt.forTaxonomy('electrical'),
    );
    expect(
      WorkshopArt.forTaxonomy('exhaust-dpf'),
      WorkshopArt.forTaxonomy('rear'),
    );
  });

  test('unknown tags stay icon-only', () {
    expect(WorkshopArt.forTaxonomy('not-a-tag'), isNull);
  });
}
