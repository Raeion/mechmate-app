from catalog_common import COMMON_SAFETY_BAY, COMMON_SCAN, article, cause, source, spec, test

MHEV = [{"requires48v": True}]


def articles():
    return [
        article(
            id="mhev-12v-first",
            title="48V system diagnosis always starts at the 12V battery",
            summary="Mild-hybrid controllers, contactors, and DC-DC logic run on 12V. A weak 12V battery disables assist, idle-stop, and charging even when the 48V pack is healthy.",
            severity="high",
            locations=["electrical", "engine-bay"],
            senses=["look", "performance"],
            systems=["mhev-48v", "body-electrical"],
            symptoms=["Hybrid or battery lamp", "Idle-stop dead", "No assist", "Random electrical gremlins"],
            safety=COMMON_SAFETY_BAY,
            tools=["12V conductance or load tester", "Scan tool with 12V and 48V SOC"],
            causes=[
                cause(
                    1,
                    "12V below specification",
                    "very-common",
                    "Field procedure on Audi, BMW, Mercedes, and Toyota 48V systems is the same: prove the 12V before you price a 48V pack.",
                    [
                        test(
                            "Rest and load",
                            "Lights off, rest voltage after 30 minutes. Then a proper load or conductance test. Then running voltage.",
                            "Rest near 12.6V on a healthy flooded/AGM. Load-test pass. Running voltage shows charge.",
                            "Rest low or load-test fail. Replace the 12V. Retest 48V functions before ordering a pack.",
                        )
                    ],
                    [
                        "Replace the 12V with the specified type. Register it if the car needs IBS coding.",
                        "Clear 48V disable codes and road-test idle-stop and take-off assist.",
                    ],
                )
            ],
            specs=[spec("Rule", "Never condemn a 48V pack on a 12V that fails a load test.")],
            parts=["Specified 12V AGM or EFB"],
            sources=[
                source("48V diagnosis overview", "https://yourracingcar.com/diagnosing-and-repairing-48-volt-mild-hybrid-systems/"),
                source("Castrol 12V/48V service notes", "https://www.castrol.com/en_gb/united-kingdom/home/learn/castrol-fastscan/service-problems-and-diagnostic-complications-in-vehicles-equipped-with-12V-48V-electrical-installation.html"),
            ],
            related=["mhev-dcdc-fail", "hilux-vactive-no-assist"],
            filters=MHEV,
        ),
        article(
            id="mhev-dcdc-fail",
            title="48V DC-DC converter failure",
            summary="When the DC-DC dies, the 48V pack no longer supports the 12V network. The car may still run while it slowly kills the 12V battery.",
            severity="high",
            locations=["electrical"],
            senses=["look", "performance"],
            systems=["mhev-48v"],
            symptoms=["Repeated 12V failure", "No charge voltage", "Converter or battery codes"],
            safety=COMMON_SAFETY_BAY,
            tools=COMMON_SCAN + ["Multimeter"],
            causes=[
                cause(
                    1,
                    "Open or overheated DC-DC",
                    "common",
                    "Converters are replaced, not rebuilt, on most platforms.",
                    [
                        test(
                            "SOC versus 12V running voltage",
                            "48V SOC healthy, engine running. Measure 12V and read converter current.",
                            "Converter current is positive into the 12V.",
                            "Zero current and 12V at rest. Replace and code the converter.",
                        )
                    ],
                    ["Replace the DC-DC. Code the hardware. Replace a 12V that was deep-cycled."],
                )
            ],
            parts=["DC-DC converter"],
            sources=[source("AFM 48V battery system problems", "https://advancedfleetmanagementtube.com/en/the-problems-with-the-48v-battery-in-micro-hybrid-cars")],
            related=["mhev-12v-first"],
            filters=MHEV,
        ),
        article(
            id="mhev-bsg-overheat",
            title="Belt starter generator overheat or electronics failure",
            summary="Water-cooled 48V starter-generators, common on VW Group cars, fail when the coolant pump or the power board overheats. The lamp comes on and charging of the 48V pack stops.",
            severity="high",
            locations=["engine-bay", "electrical"],
            senses=["look", "performance"],
            systems=["mhev-48v", "cooling"],
            symptoms=["Battery lamp", "48V pack discharging to a cutoff", "Hot BSG after a short drive"],
            safety=COMMON_SAFETY_BAY + ["A water-cooled BSG shares coolant. Pressure-test before you open it."],
            tools=COMMON_SCAN + ["Infrared thermometer", "Cooling pressure tester"],
            causes=[
                cause(
                    1,
                    "BSG power electronics overheat from a weak coolant circuit",
                    "common on early water-cooled units",
                    "Published failure notes list high charge current and coolant leaks into the electronics.",
                    [
                        test(
                            "Coolant flow and BSG temp pid",
                            "Confirm the small pump runs when the BSG is generating. Compare housing temp to coolant temp.",
                            "Pump runs. Temps stay together.",
                            "Pump silent or housing far hotter than coolant. Replace the pump, then the BSG if it already took coolant.",
                        )
                    ],
                    [
                        "Repair the cooling circuit first.",
                        "Replace the BSG if boards are wet or codes show internal faults.",
                        "Update firmware and adapt the new unit to the engine and cooling variant.",
                    ],
                )
            ],
            parts=["BSG / starter-generator", "Electric coolant pump"],
            sources=[source("STS 48V starter-generator failures", "https://sts.parts/en/articles/how-to-install-and-code-a-48-v-starter-generator")],
            related=["mhev-belt-tensioner"],
            filters=MHEV,
        ),
        article(
            id="mhev-belt-tensioner",
            title="48V belt, pulley and tensioner failure",
            summary="A 48V belt carries motoring torque in both directions. Glaze, a weak tensioner, or the wrong belt kills restart quality and sets charging faults.",
            severity="medium",
            locations=["engine-bay"],
            senses=["sound", "performance"],
            systems=["mhev-48v"],
            symptoms=["Chirp on restart", "Idle-stop disabled after rain", "Belt dust on the cover"],
            safety=COMMON_SAFETY_BAY,
            tools=["Correct 48V belt", "Tensioner pin"],
            causes=[
                cause(
                    1,
                    "Glazed belt or dead tensioner",
                    "very-common",
                    "Audi-style systems often quote a belt inspection every oil service and a shorter replacement interval than a normal accessory belt.",
                    [
                        test(
                            "Inspect and measure slack",
                            "Look for glaze, cracks, and tensioner travel. Compare belt length and part number to the 48V spec, not a generic 12V belt.",
                            "Correct part, quiet, tensioner moves and returns.",
                            "Wrong part or dead tensioner. Replace both.",
                        )
                    ],
                    ["Fit the aramid belt without kinking. Align pulleys. Clear codes."],
                )
            ],
            parts=["48V belt", "Tensioner", "Idler"],
            sources=[source("Belt drive systems for Audi and BMW mild hybrids", "https://www.tomorrowstechnician.com/belt-drive-systems-for-audi-and-bmw-mild-hybrids/")],
            related=["hilux-vactive-belt", "squeal-cold-belt"],
            filters=MHEV,
        ),
        article(
            id="mhev-battery-cell",
            title="48V lithium pack weak cell",
            summary="A 48V pack needs a scan tool. You cannot carbon-pile it. Look at SOC, SOH, and cell balance. A cell that is more than about 0.2V off the pack mean is a failed module.",
            severity="high",
            locations=["electrical", "inside"],
            senses=["look", "performance"],
            systems=["mhev-48v"],
            symptoms=["Pack isolation or imbalance codes", "Assist dies after a short trip", "Low SOC that will not climb"],
            safety=COMMON_SAFETY_BAY + ["Do not pierce or jump a 48V lithium pack with a 12V packer."],
            tools=["Manufacturer scan tool", "Insulated gloves and a meter rated for the system"],
            causes=[
                cause(
                    1,
                    "Unbalanced or tired cell",
                    "common with age and heat",
                    "BMS opens contactors to protect the pack.",
                    [
                        test(
                            "Cell voltage spread",
                            "Read all cell or module voltages at rest.",
                            "Cells within a few tens of millivolts.",
                            "One cell or module more than about 0.2V off. Replace the pack or the failed module if the maker sells it.",
                        )
                    ],
                    [
                        "Replace the failed pack hardware.",
                        "Charge only with the specified procedure after install.",
                        "Confirm cooling vents or liquid cooling are clear so the new pack does not cook.",
                    ],
                )
            ],
            specs=[spec("Balance rule of thumb", "About 0.2V off the pack mean is a weak cell on many 13-cell 48V modules.")],
            parts=["48V battery or module"],
            sources=[source("Diagnosing 48V systems", "https://yourracingcar.com/diagnosing-and-repairing-48-volt-mild-hybrid-systems/")],
            related=["mhev-12v-first"],
            filters=MHEV,
        ),
        article(
            id="mercedes-eq-boost-messages",
            title="Mercedes EQ Boost 48V warning messages",
            summary="EQ Boost C-Class, E-Class, GLC and GLE cars sold in Australia use a 48V integrated starter generator. Messages about the 48V network usually start as a 12V or belt issue.",
            severity="medium",
            locations=["electrical", "inside"],
            senses=["look", "performance"],
            systems=["mhev-48v"],
            symptoms=["48V network message", "Idle-stop disabled", "Rough restart"],
            safety=COMMON_SAFETY_BAY,
            tools=COMMON_SCAN + ["Mercedes-capable scan tool"],
            causes=[
                cause(
                    1,
                    "12V IBS or 48V disable from a tired starter battery",
                    "very-common",
                    "Same logic as other MHEV platforms.",
                    [
                        test(
                            "XENTRY-style 12V and 48V SOC",
                            "Read IBS, 12V rest, 48V SOC, and generator status.",
                            "12V healthy and 48V enabled.",
                            "12V fail. Replace and register the battery, then retest.",
                        )
                    ],
                    ["Register the new 12V. Clear network faults. Confirm EQ Boost assist on take-off."],
                )
            ],
            sources=[source("Mercedes 48V / EQ Boost in AU luxury fleet", "https://www.carexpert.com.au/car-news/2025-audi-a5-and-s5-initial-details-for-australia")],
            related=["mhev-12v-first"],
            filters=[{"requires48v": True, "generationId": "c-class-w206"}, {"requires48v": True, "generationId": "e-class-w214"}, {"requires48v": True, "generationId": "glc-x254"}, {"requires48v": True, "generationId": "gle-v167"}],
        ),
        article(
            id="audi-mhev-restart",
            title="Audi 48V restart clunk and failed coasting",
            summary="Audi MHEV and Mild hybrid plus cars use a belt or integrated starter generator. A clunk on restart is often the belt or the 12V, not a failed engine mount.",
            severity="medium",
            locations=["engine-bay"],
            senses=["sound", "feel"],
            systems=["mhev-48v"],
            symptoms=["Clunk on idle-stop restart", "Coasting disabled", "Belt dust"],
            safety=COMMON_SAFETY_BAY,
            tools=COMMON_SCAN + ["Belt inspection"],
            causes=[
                cause(
                    1,
                    "Belt slip or 12V sag during the restart event",
                    "common",
                    "The generator motors the crank. A slipping belt or a sagging 12V makes the restart violent.",
                    [
                        test(
                            "Voltage sag and belt",
                            "Graph 12V during a stop-start event. Inspect the 48V belt.",
                            "12V stays above about 11.5V during the event. Belt is clean.",
                            "12V collapses or the belt is glazed. Fix those before replacing mounts.",
                        )
                    ],
                    ["Replace 12V or belt as the test shows. Then re-evaluate mounts if the clunk remains with a crisp restart."],
                )
            ],
            sources=[source("Audi 48V belt interval notes", "https://www.tomorrowstechnician.com/belt-drive-systems-for-audi-and-bmw-mild-hybrids/")],
            related=["mhev-belt-tensioner"],
            filters=[{"requires48v": True, "generationId": "a4-b9"}, {"requires48v": True, "generationId": "a5-b10"}, {"requires48v": True, "generationId": "q5-fy"}, {"requires48v": True, "generationId": "q7-4m"}],
        ),
        article(
            id="bmw-48v-aux-battery",
            title="BMW 48V auxiliary battery and charging complaints",
            summary="BMW 48V cars (3 Series, 5 Series, X5 and others in AU) store regen in a small lithium pack. A low SOC message after short winter trips is often use-case plus a tired 12V, not an instant pack replace.",
            severity="medium",
            locations=["electrical"],
            senses=["look", "performance"],
            systems=["mhev-48v"],
            symptoms=["Yellow battery icon", "Message to idle until the lamp goes out", "Assist missing"],
            safety=COMMON_SAFETY_BAY,
            tools=COMMON_SCAN,
            causes=[
                cause(
                    1,
                    "48V SOC below about 30 percent after short trips",
                    "common",
                    "Castrol notes a cluster message when the auxiliary pack drops below about 30 percent. Idle in a safe place until the lamp clears, then find why it will not stay charged.",
                    [
                        test(
                            "SOC after a 20 minute drive",
                            "Drive until fully warm. Read 48V SOC and 12V. Confirm the generator is actually charging.",
                            "SOC climbs and the lamp stays out.",
                            "SOC will not climb. Test belt, BSG, and cells.",
                        )
                    ],
                    [
                        "If the lamp clears after a long idle or drive, change the use pattern and retest the 12V.",
                        "If SOC never climbs, follow BSG and pack tests.",
                    ],
                )
            ],
            specs=[spec("Published warning threshold", "Auxiliary pack messages are described around 30 percent SOC on some 12V/48V cars.")],
            sources=[source("Castrol 48V charge warnings", "https://www.castrol.com/en_gb/united-kingdom/home/learn/castrol-fastscan/service-problems-and-diagnostic-complications-in-vehicles-equipped-with-12V-48V-electrical-installation.html")],
            related=["mhev-battery-cell"],
            filters=[{"requires48v": True, "generationId": "3-g20"}, {"requires48v": True, "generationId": "5-g60"}, {"requires48v": True, "generationId": "x5-g05"}],
        ),
    ]
