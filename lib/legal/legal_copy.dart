enum LegalDoc { privacy, terms, disclaimer }

String legalTitle(LegalDoc doc) {
  switch (doc) {
    case LegalDoc.privacy:
      return 'Privacy';
    case LegalDoc.terms:
      return 'Terms of use';
    case LegalDoc.disclaimer:
      return 'Safety disclaimer';
  }
}

String legalBody(LegalDoc doc) {
  switch (doc) {
    case LegalDoc.privacy:
      return _privacy;
    case LegalDoc.terms:
      return _terms;
    case LegalDoc.disclaimer:
      return _disclaimer;
  }
}

LegalDoc legalDocFromId(String id) {
  switch (id) {
    case 'privacy':
      return LegalDoc.privacy;
    case 'terms':
      return LegalDoc.terms;
    case 'disclaimer':
      return LegalDoc.disclaimer;
    default:
      throw ArgumentError('Unknown legal document: $id');
  }
}

String legalId(LegalDoc doc) {
  switch (doc) {
    case LegalDoc.privacy:
      return 'privacy';
    case LegalDoc.terms:
      return 'terms';
    case LegalDoc.disclaimer:
      return 'disclaimer';
  }
}

const _privacy = '''
Mechmate is offline-first. After install, diagnosis runs from the catalog bundled in the app.

What stays on this device
Garage vehicles, the active vehicle, the last article you opened, and whether you accepted the welcome sheet are stored with SharedPreferences on this phone, tablet, or browser profile. The diagnostic database is a local SQLite file seeded from the bundled catalog.

What we do not collect
This build does not create an account. It does not send garage data, searches, or article views to a server. It does not include analytics, advertising, or crash-reporting SDKs. It does not sell personal information.

Web
On web, the same local store lives in this browser profile. Clearing site data removes the garage.

Children
Mechmate is not directed at children under 13.

Questions
If you host your own build, you are the operator of that copy. The public origin repo is github.com/Raeion/mechmate-app.
''';

const _terms = '''
Mechmate is a workshop companion. It ranks likely causes and gives tests and repairs. It is not a substitute for the official workshop procedure for your exact vehicle, and it is not a licensed mechanical inspection.

You decide whether a job is safe for you. If a step needs a tool, a hoist, or a skill you do not have, stop and get that capability. The app will not tell you to "take it to a mechanic." It will tell you how to finish the job. That does not make every job appropriate for every person.

Do not use Mechmate to defeat emissions equipment. DPF or EGR delete is not documented as a repair.

Factory torque and rail-pressure numbers that are not public are not invented here. Where a figure is missing, measure and follow the service sequence you have.

Catalog coverage is Australia-first and growing. A missing model overlay does not mean the universal articles are wrong. It means the model-specific notes are not written yet.

The software is provided as is. The authors are not liable for injury, damage, failed parts, or a vehicle that does not pass a roadworthy after you follow a procedure.
''';

const _disclaimer = '''
Lock out the job first. Park on level ground. Park brake on. Wheels chocked. Support the vehicle on rated stands. Never work under a jack only.

Fuel, brake fluid, and coolant are hazardous. Do not taste fluids. Keep ignition sources away from wet fuel.

A hot exhaust, turbo, or DPF can exceed 500C. Let it cool. Regeneration on dry grass is a fire risk.

On 48V V-Active and other mild hybrids, treat blue 48V cables as live until the service connector is open and you have measured 0V. Start electrical tests on the 12V battery and the DC-DC. Do not pull 48V connectors by guesswork.

If you see smoke from a loom, isolate the 12V earth. Do not keep powering a circuit that already smells of burnt plastic.

This disclaimer is also shown the first time you open the app. You can read it again from Settings.
''';
