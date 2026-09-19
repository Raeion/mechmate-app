from catalog_common import COMMON_SAFETY_BAY, COMMON_SCAN, article, cause, source, spec, test

HILUX_FILTER_N70_1KD = [{"generationId": "hilux-n70", "engineId": "1kd-ftv"}]
HILUX_FILTER_N80_1GD = [{"generationId": "hilux-n80", "engineId": "1gd-ftv"}, {"generationId": "hilux-n80-48v", "engineId": "1gd-ftv"}]
HILUX_FILTER_N80_EARLY = [{"generationId": "hilux-n80", "engineId": "1gd-ftv", "yearFrom": 2015, "yearTo": 2020}]
HILUX_FILTER_48V = [{"generationId": "hilux-n80-48v", "requires48v": True}]
PRADO_1GD = [{"modelId": "prado", "engineId": "1gd-ftv"}]


def articles():
    return [
        article(
            id="hilux-1kd-injector-seat",
            title="1KD injector copper seat leak and oil pressurised by combustion",
            summary="Pre-2008 1KD-FTV Hilux injectors sit on copper washers that can relax. Combustion gas then pressurises the rocker cover, forces oil into the turbo drain, and kills the turbo.",
            severity="critical",
            locations=["engine-bay"],
            senses=["look", "performance", "sound"],
            systems=["fuel", "lubrication", "air-turbo"],
            symptoms=["Oil level rising", "White or blue haze after a boost run", "Turbo whistle then smoke", "Crankcase pressure at the oil cap"],
            safety=COMMON_SAFETY_BAY + ["Relieve rail pressure. Crack a return line into a bottle, not onto a hot turbo."],
            tools=COMMON_SCAN + ["Injector puller set", "New DLC or steel seats, not the original soft copper if the engine is still on copper"],
            causes=[
                cause(
                    1,
                    "Soft copper injector seats leaking combustion into the oil gallery",
                    "very-common on pre-2008 1KD",
                    "Toyota changed seat material after about 2007 because copper annealed and leaked.",
                    [
                        test(
                            "Crankcase pressure at idle and snap throttle",
                            "Warm the engine. Remove the oil cap. A light pulse is normal. A hard lift of the cap, oil mist, or a whistle from the filler means combustion is in the crankcase. Then pull injectors and inspect the seat face.",
                            "Cap sits still. Seat face is flat. No black combustion ring under the injector.",
                            "Cap lifts, oil is grey, or the seat is dished. Replace seats and retest compression on that cylinder.",
                        )
                    ],
                    [
                        "Pull the injector rail cover and mark injector order.",
                        "Extract injectors. If a copper seat stays in the head, pick it out. Do not drop copper into the chamber.",
                        "Fit the later hard seats. Lightly oil the new O-rings. Seat each injector square.",
                        "Replace the turbo if the drain was full of black oil and the compressor is scored.",
                        "Change oil and filter twice in the next 1000 km because combustion soot is in the sump.",
                    ],
                ),
                cause(
                    2,
                    "Leaking injector body or return T-piece",
                    "common at high km",
                    "A wet injector can look like a seat leak but the oil is diesel, not combustion.",
                    [
                        test(
                            "Wipe and idle",
                            "Clean the injector valley. Idle 10 minutes with a paper towel under the returns.",
                            "Towel stays dry. Fuel smell is absent.",
                            "Towel wets with clear diesel. Replace return seals or the injector.",
                        )
                    ],
                    ["Replace leak-off olives and any injector that weeps at the body. Retorque using the service sequence. Factory injector clamp torque is not published here. Tighten evenly until the injector is fully seated and does not rotate."],
                ),
            ],
            specs=[
                spec("Affected engines", "1KD-FTV roughly pre-2008 copper seats"),
                spec("Oil level rise", "Any rise between services is a fail. Diesel and combustion both raise the stick."),
            ],
            parts=["Injector seats (later DLC/steel type)", "Injector O-rings", "Oil and filter", "Turbo if contaminated"],
            sources=[
                source("Toyota Hilux common problems, Carify Australia", "https://www.carify.com.au/toyota/hilux/problems"),
                source("1KD-FTV field reliability notes", "https://craigjonesauto.com.au/toyota-hilux-common-problems-report/"),
            ],
            related=["hilux-1kd-oil-dilution", "hilux-turbo-actuator", "hilux-1kd-piston-crack"],
            filters=HILUX_FILTER_N70_1KD,
        ),
        article(
            id="hilux-1kd-oil-dilution",
            title="1KD oil level rising from diesel dilution",
            summary="Short trips and leaking injectors dump diesel into the 1KD sump. Oil looks thin, smells of fuel, and bearings suffer.",
            severity="high",
            locations=["engine-bay"],
            senses=["smell", "look", "performance"],
            systems=["lubrication", "fuel"],
            symptoms=["Oil above full", "Fuel smell on the dipstick", "Knock after a cold start that fades", "Fuel use up"],
            safety=COMMON_SAFETY_BAY,
            tools=["Dipstick comparison with new oil", "Oil sample bottle", "Scan tool for injector correction"],
            causes=[
                cause(
                    1,
                    "Injector dribble after shutdown",
                    "very-common",
                    "A leaking injector keeps feeding fuel into a hot cylinder. Fuel washes the bore and lands in the sump.",
                    [
                        test(
                            "Injector contribution and return quantity",
                            "Scan correction values. Pull returns into four bottles for 30 seconds at idle.",
                            "Corrections stay near zero. Return volumes are even.",
                            "One cylinder is rich or one return is flooding. Replace that injector as a set of seals first, then the injector.",
                        )
                    ],
                    [
                        "Drain the diluted oil. Do not drive with fuel-thin oil.",
                        "Repair the leaking injector.",
                        "Refill with the specified 5W-40 or 10W-40 diesel oil and a new filter.",
                        "Re-check the stick after 200 km. If it climbs again, the leak is still live.",
                    ],
                )
            ],
            specs=[spec("Action level", "Oil that smells of diesel or sits above the full mark is failed oil. Change it now.")],
            parts=["Oil and filter", "Injector or seals"],
            sources=[source("1KD reliability guide", "https://craigjonesauto.com.au/toyota-hilux-common-problems-report/")],
            related=["hilux-1kd-injector-seat"],
            filters=HILUX_FILTER_N70_1KD,
        ),
        article(
            id="hilux-1kd-piston-crack",
            title="1KD piston crown crack and sudden knock",
            summary="High-km 1KD engines can crack a piston, usually after over-fuelling, heavy towing, or a long history of oil dilution. You confirm it with a leak-down and a borescope, then you pull the sump or the head.",
            severity="critical",
            locations=["engine-bay"],
            senses=["sound", "performance"],
            systems=["engine-mechanical"],
            symptoms=["Sharp knock under load", "Misfire on one cylinder", "Metal in the filter", "White smoke that is fuel, not coolant"],
            safety=COMMON_SAFETY_BAY + ["If you hear a hard knock, shut down. Another minute can put a rod through the block."],
            tools=COMMON_SCAN + ["Compression and leak-down gauges", "Borescope"],
            causes=[
                cause(
                    1,
                    "Cracked piston on a 1KD that was over-fuelled or run with poor oil",
                    "known 1KD failure",
                    "The 1KD piston is the documented weak point when injectors over-fuel or oil cooling is poor.",
                    [
                        test(
                            "Leak-down and borescope",
                            "Warm engine. Leak-down each cylinder at TDC. Listen at the oil cap and the tailpipe. Scope the crown through the injector hole.",
                            "Leak-down under 15 percent. Crown is intact.",
                            "High leak into the crankcase and a visible crack or missing chunk. Plan a rebuild: pistons, rings, and bearings at minimum.",
                        )
                    ],
                    [
                        "Do not keep driving it to 'see if it clears'.",
                        "Drop the sump and inspect bearings. If the filter has glitter, budget a full rebuild.",
                        "Fit later pistons if a revised part is available for that serial. Measure bore wear before you reuse the block.",
                        "Fix the injector that caused the over-fuel before you start the rebuilt engine.",
                    ],
                )
            ],
            specs=[spec("Leak-down", "Treat over about 20 percent on one cylinder as a mechanical fail when the others are healthy.")],
            parts=["Piston kit", "Bearings", "Oil pump pickup screen"],
            sources=[source("Owner and workshop 1KD piston notes", "https://www.reddit.com/r/hilux/comments/11fyaya/which_hilux_motor_is_the_most_reliable_30l_1kdftv/")],
            related=["hilux-1kd-injector-seat", "engine-knock-on-accel"],
            filters=HILUX_FILTER_N70_1KD,
        ),
        article(
            id="hilux-1kd-egr-carbon",
            title="1KD and 1GD EGR and intake carbon",
            summary="Both Hilux diesels route soot through the EGR. The valve sticks and the intake runners cake up. You get P0401, a lazy pedal, and black smoke.",
            severity="medium",
            locations=["engine-bay"],
            senses=["performance", "look"],
            systems=["air-turbo", "exhaust-dpf"],
            symptoms=["P0401", "Flat mid-range", "Black smoke on a hard pull", "Rattle from the EGR on shutdown"],
            safety=COMMON_SAFETY_BAY + ["Do not use a flammable cleaner on an open intake while the engine can crank."],
            tools=COMMON_SCAN + ["Intake cleaner", "EGR gasket set", "Catch-can parts if you want to slow the return of oil mist"],
            causes=[
                cause(
                    1,
                    "EGR valve stuck open or closed with a blocked cooler",
                    "very-common",
                    "Soot plus oil mist from the breather turns to tar in the valve and the intake.",
                    [
                        test(
                            "Command the EGR and watch MAF / MAP",
                            "On a scan tool, command EGR. MAP and MAF should move. Then remove the valve and look through the cooler.",
                            "Valve moves smoothly. Cooler passages are open.",
                            "Valve is caked or the cooler is blocked. Clean or replace. Pressure-test the cooler in water if you suspect an internal leak.",
                        )
                    ],
                    [
                        "Remove the EGR valve and cooler. Walnut-blast or chemically clean the intake.",
                        "Replace gaskets. Do not reuse swollen EGR gaskets.",
                        "Fit a quality oil separator on the breather if the engine will keep doing short trips.",
                        "Clear codes and road-test. Confirm P0401 stays gone.",
                    ],
                )
            ],
            specs=[spec("Code", "P0401 is the usual insufficient EGR flow code on these engines.")],
            parts=["EGR valve", "EGR cooler", "Intake gaskets"],
            sources=[source("Hilux EGR carbon write-up", "https://www.carify.com.au/toyota/hilux/problems")],
            related=["hilux-n80-egr-cooler", "smoke-black-fuel"],
            filters=[{"modelId": "hilux"}, {"modelId": "prado"}],
        ),
        article(
            id="hilux-intercooler-hose",
            title="Split intercooler hose and fake turbo failure",
            summary="A split or popped intercooler hose on a Hilux dumps boost before the inlet. You get black smoke, a whistle, and no power. The turbo is often still healthy.",
            severity="medium",
            locations=["engine-bay", "front"],
            senses=["sound", "performance", "look"],
            systems=["air-turbo"],
            symptoms=["Sudden power loss", "Black smoke", "Hiss or whistle under boost", "Hose oily and split at a join"],
            safety=COMMON_SAFETY_BAY,
            tools=["Smoke machine or soapy water", "Clamp set", "Boost gauge or scan live data"],
            causes=[
                cause(
                    1,
                    "Split or slipped intercooler hose",
                    "very-common",
                    "Heat, oil mist, and aftermarket clamps let the cold-side hose open.",
                    [
                        test(
                            "Boost leak at the hose",
                            "Watch commanded versus actual boost. Then pressurise the cold side to about 15-20 psi with a smoke machine or a regulated air source. Stay below a pressure that can damage the charger.",
                            "Actual boost tracks request. No smoke at the joins.",
                            "Actual boost lags and smoke or soap bubbles at a join. Replace the hose and use quality constant-tension clamps.",
                        )
                    ],
                    [
                        "Replace the split hose. Do not tape it.",
                        "Clean oil out of the intercooler if it is wet. Oil in the core is a clue to a turbo or breather issue.",
                        "Road-test and confirm boost tracks request.",
                    ],
                )
            ],
            specs=[spec("Boost leak test", "Use a regulated source. Do not put shop-line pressure through a plastic tank.")],
            parts=["Intercooler hose", "Clamps"],
            sources=[source("Hilux turbo and intercooler hose notes", "https://craigjonesauto.com.au/toyota-hilux-common-problems-report/")],
            related=["hilux-turbo-actuator", "no-boost"],
            filters=[{"modelId": "hilux"}],
        ),
        article(
            id="hilux-turbo-actuator",
            title="Variable-nozzle turbo actuator and bearing wear",
            summary="Hilux diesels use a vacuum or electronic actuator on the VNT. A seized vane pack or a torn diaphragm gives lag, over-boost, or a whistle.",
            severity="high",
            locations=["engine-bay"],
            senses=["sound", "performance"],
            systems=["air-turbo"],
            symptoms=["Lag then a sudden kick", "Over-boost cut", "Metallic grit in the oil", "Blue smoke after a long downhill"],
            safety=COMMON_SAFETY_BAY + ["A charging turbo is hot and the compressor wheel will cut fingers."],
            tools=COMMON_SCAN + ["Hand vacuum pump", "Borescope for compressor blades"],
            causes=[
                cause(
                    1,
                    "Actuator diaphragm or vane pack stuck",
                    "common",
                    "Soot locks the vanes. The actuator rod then stops moving.",
                    [
                        test(
                            "Actuator stroke",
                            "On a vacuum actuator, pump 20 inHg and watch the rod. On an electronic actuator, command duty cycle with a scan tool.",
                            "Rod travels smoothly and boost request is met.",
                            "Rod is stuck or fluttering. Free the vanes or replace the turbo as a unit if the vanes are rusted solid.",
                        )
                    ],
                    [
                        "Replace a torn actuator first if the vanes still move by hand with the turbo off the engine.",
                        "If the shaft has play that lets the wheel kiss the housing, replace the turbo. Clean the oil feed and the drain.",
                        "Prime the oil feed before first fire.",
                    ],
                )
            ],
            parts=["Actuator", "Turbocharger", "Oil feed line"],
            sources=[source("Hilux turbo troubles", "https://craigjonesauto.com.au/toyota-hilux-common-problems-report/")],
            related=["hilux-intercooler-hose", "hilux-1kd-injector-seat"],
            filters=[{"modelId": "hilux"}],
        ),
        article(
            id="hilux-n80-dpf",
            title="N80 1GD DPF will not finish regeneration",
            summary="Early N80 2.8 diesels (about October 2015 to April 2020) failed to complete DPF regen. Toyota Australia faced a Federal Court class action covering Hilux, Fortuner and Prado. You diagnose soot load, delta-P, and the fifth injector before you buy a DPF.",
            severity="high",
            locations=["rear", "engine-bay"],
            senses=["look", "performance"],
            systems=["exhaust-dpf", "fuel"],
            symptoms=["DPF lamp", "White smoke on start", "Limp mode", "P2458 or P2463", "Fuel use up"],
            safety=COMMON_SAFETY_BAY + [
                "A regen can start while you work. Stay off dry grass. The DPF skin will burn you.",
                "Do not delete the DPF. That is illegal on an Australian road vehicle.",
            ],
            tools=COMMON_SCAN + ["Pyrometer", "Fifth injector quantity test bottles"],
            causes=[
                cause(
                    1,
                    "Aborted active regen and packed soot",
                    "very-common on 2015-2020 1GD",
                    "The early calibration and hardware could not finish a regen on short-trip or low-load work.",
                    [
                        test(
                            "Soot percent and differential pressure",
                            "Read DPF soot and differential pressure at idle and at 2500 rpm in park. Compare exhaust temp upstream of the DPF during a commanded regen.",
                            "Soot drops during a completed regen. Delta-P stays low when the filter is clean.",
                            "Soot stuck high, regen aborts, P2458 / P2463. Move to fifth injector and pressure sensor tests before replacing the can.",
                        )
                    ],
                    [
                        "If the truck has a manual DPF burn switch (2019-on many AU trucks), use it on a highway run, not in a workshop with rags under the tray.",
                        "Command a service regen only after you have confirmed oil is not diluted and coolant temp is in the normal range.",
                        "If soot will not leave and delta-P stays high after a completed regen, replace the DPF. Clean only if you can verify the substrate is intact.",
                        "Update ECU calibration if a later public campaign file applies to that VIN.",
                    ],
                ),
                cause(
                    2,
                    "Failed fifth injector",
                    "common on pre-2020 1GD",
                    "The 1GD uses a fifth injector in the exhaust to feed regen. When it dies, regen cannot raise temperature.",
                    [
                        test(
                            "Fifth injector command and rail contribution",
                            "Command the fifth injector. You should see a temp rise upstream of the DPF and a fuel quantity change. A dead injector throws a specific code and no temp rise.",
                            "Temp climbs and the injector clicks / flows.",
                            "No temp rise. Replace the fifth injector. Toyota revised later injectors with a cooling path.",
                        )
                    ],
                    ["Replace the fifth injector. Clear adaptions. Complete one monitored regen on a long run."],
                ),
            ],
            specs=[
                spec("Campaign window", "Federal Court matter covered roughly Oct 2015 to Apr 2020 1GD Hilux, Fortuner and Prado"),
                spec("Codes", "P2458 duration, P2463 soot accumulation are the usual pair"),
            ],
            parts=["DPF assembly", "Fifth injector", "Differential pressure sensor and pipes"],
            sources=[
                source("Hilux DPF class-action summary", "https://www.carify.com.au/toyota/hilux/problems"),
                source("N80 problems and fifth injector", "https://unsealed4x4.com.au/toyota-hilux-n80-common-problems/"),
                source("Toyota Australia HiLux spec table, V-Active and DPF burn switch", "https://media.adtorqueedge.com/new-cars/toyota-au/hilux/hilux-specs.pdf"),
            ],
            related=["hilux-n80-fifth-injector", "dpf-regen-loop", "prado-1gd-dpf"],
            filters=HILUX_FILTER_N80_EARLY + PRADO_1GD,
        ),
        article(
            id="hilux-n80-fifth-injector",
            title="1GD fifth injector failure",
            summary="The 1GD has four chamber injectors plus a fifth injector in the exhaust for DPF regen. Early units failed and filled the dash with lamps.",
            severity="high",
            locations=["under", "rear"],
            senses=["look", "performance"],
            systems=["fuel", "exhaust-dpf"],
            symptoms=["DPF and engine lamps together", "No temp rise during regen", "Fuel smell at the exhaust pipe join"],
            safety=COMMON_SAFETY_BAY,
            tools=COMMON_SCAN + ["Fifth injector service kit"],
            causes=[
                cause(
                    1,
                    "Fifth injector stuck closed or leaking into the pipe",
                    "common pre-2020",
                    "Toyota redesigned later injectors with better cooling after field failures.",
                    [
                        test(
                            "Command and leak-down of the fifth injector",
                            "Command the injector on a scan tool. Listen and watch upstream temp. Then inspect the pipe join for wet diesel.",
                            "Click plus a clear temp rise. Joint stays dry.",
                            "Silent injector or a wet joint. Replace with the revised part.",
                        )
                    ],
                    [
                        "Replace the injector. Do not reuse a swollen copper washer.",
                        "Clear the DPF codes and complete a regen.",
                        "If the DPF is already melted or cracked from failed regens, replace the DPF at the same time.",
                    ],
                )
            ],
            parts=["Fifth injector", "Gasket / washer"],
            sources=[source("Unsealed 4x4 N80 fifth injector", "https://unsealed4x4.com.au/toyota-hilux-n80-common-problems/")],
            related=["hilux-n80-dpf"],
            filters=HILUX_FILTER_N80_1GD,
        ),
        article(
            id="hilux-n80-egr-cooler",
            title="N80 EGR cooler leak into the intake",
            summary="A failed EGR cooler puts coolant into the intake. You see a falling coolant tank, white smoke, and a sweet smell without a head-gasket pressure test fail.",
            severity="high",
            locations=["engine-bay"],
            senses=["look", "smell", "performance"],
            systems=["cooling", "air-turbo"],
            symptoms=["Coolant loss with a dry radiator seam", "White smoke that smells sweet", "Milky film in the intake"],
            safety=COMMON_SAFETY_BAY + ["Never open a hot cooling system."],
            tools=["Cooling system pressure tester", "Borescope", "Combustion gas tester for the header tank"],
            causes=[
                cause(
                    1,
                    "EGR cooler internally cracked",
                    "common at higher km",
                    "Thermal cycling cracks the cooler. Coolant is ingested.",
                    [
                        test(
                            "Pressure test with EGR isolated",
                            "Pressure-test the cold system. Watch the intake and the EGR cooler housing. A combustion gas test of the header tank that stays negative while coolant still vanishes points at the cooler, not the head gasket.",
                            "System holds pressure. Intake is dry.",
                            "Coolant appears in the EGR or intake. Replace the cooler. Flush the intake.",
                        )
                    ],
                    [
                        "Replace the EGR cooler and gaskets.",
                        "Flush coolant. Refill and bleed until the rear heater is hot.",
                        "If the engine ingested a large volume, change oil in case coolant reached the sump.",
                    ],
                )
            ],
            parts=["EGR cooler", "Coolant"],
            sources=[source("N80 EGR cooler leaks", "https://unsealed4x4.com.au/toyota-hilux-n80-common-problems/")],
            related=["hilux-1kd-egr-carbon", "smoke-white-coolant"],
            filters=HILUX_FILTER_N80_1GD,
        ),
        article(
            id="hilux-n80-airbox-dust",
            title="N80 airbox dust ingress",
            summary="Early N80 airboxes can leak dust past the filter seal. The MAF reads wrong and the turbo ingests grit.",
            severity="medium",
            locations=["engine-bay"],
            senses=["look", "performance"],
            systems=["air-turbo"],
            symptoms=["Dust on the clean side of the filter", "MAF codes", "Gritty compressor blades"],
            safety=COMMON_SAFETY_BAY,
            tools=["Torch", "Replacement airbox seals or updated box"],
            causes=[
                cause(
                    1,
                    "Airbox lid or snorkel seal leak",
                    "common on early N80",
                    "A poor lid seal lets fine bull-dust bypass the paper.",
                    [
                        test(
                            "Clean-side inspection",
                            "Open the box. The outlet tube and MAF screen must be clean. Dust there means the seal failed.",
                            "Clean side is clean.",
                            "Dust past the filter. Replace the filter, reseal or replace the box, and inspect the compressor.",
                        )
                    ],
                    [
                        "Fit a new filter. Do not blow a dirty filter from the inside out in a way that punches holes.",
                        "Replace crushed seals. If a later airbox revision exists for that year, use it.",
                        "If the compressor is sand-blasted, replace the turbo before it sheds blades.",
                    ],
                )
            ],
            parts=["Air filter", "Airbox seal or box"],
            sources=[source("N80 airbox sealing", "https://unsealed4x4.com.au/toyota-hilux-n80-common-problems/")],
            related=["hilux-turbo-actuator"],
            filters=HILUX_FILTER_N80_1GD,
        ),
        article(
            id="hilux-n80-timing-chain",
            title="N80 1GD timing chain rattle on cold start",
            summary="Earlier 1GD engines can rattle the timing chain at cold start. Many keep running, but you still measure slack and oil pressure before you ignore it.",
            severity="medium",
            locations=["engine-bay"],
            senses=["sound"],
            systems=["engine-mechanical", "lubrication"],
            symptoms=["1 to 3 second rattle at cold start", "Rattle that lasts longer as km climb"],
            safety=COMMON_SAFETY_BAY,
            tools=["Mechanic stethoscope", "Oil pressure gauge", "Scan tool for cam/crank correlation"],
            causes=[
                cause(
                    1,
                    "Chain and tensioner wear",
                    "common on earlier N80",
                    "A short cold rattle is the known 1GD noise. A long rattle plus correlation codes is a chain job.",
                    [
                        test(
                            "Cold start recording and correlation",
                            "Record the first three seconds from the front cover. Read cam/crank correlation. Check cold oil pressure.",
                            "Rattle under three seconds, no correlation code, oil pressure in spec.",
                            "Rattle continues, correlation code stored, or low oil pressure. Replace chain, guides, and tensioner. Find why oil pressure was low.",
                        )
                    ],
                    [
                        "If the rattle is short and codes are clean, change oil to the specified grade and re-test on a cold morning.",
                        "If it fails the correlation or duration test, pull the cover and replace the chain kit.",
                        "Toyota has replaced some under goodwill. That does not change the test.",
                    ],
                )
            ],
            parts=["Timing chain kit", "Oil and filter"],
            sources=[source("N80 timing chain rattle", "https://unsealed4x4.com.au/toyota-hilux-n80-common-problems/")],
            related=["tick-at-idle"],
            filters=HILUX_FILTER_N80_1GD,
        ),
        article(
            id="hilux-n80-trans-cooler",
            title="N80 automatic overheat when towing",
            summary="The factory N80 auto cooler is small. Towing in heat raises ATF temp, glazes the clutch packs, and makes late or harsh shifts.",
            severity="medium",
            locations=["front", "under"],
            senses=["performance", "feel"],
            systems=["drivetrain", "cooling"],
            symptoms=["Harsh 3-4", "ATF smell", "Temp warning on a long climb", "Brown ATF"],
            safety=COMMON_SAFETY_BAY,
            tools=["Scan tool with ATF temp", "Infrared thermometer", "ATF warmer / cooler kit"],
            causes=[
                cause(
                    1,
                    "Inadequate factory cooler capacity",
                    "common on towing trucks",
                    "ATF over 100C for long periods cooks the fluid.",
                    [
                        test(
                            "ATF temp on a known climb",
                            "Tow or simulate load. Watch ATF temp versus coolant temp.",
                            "ATF stays in a stable band and shifts stay clean.",
                            "ATF climbs away from coolant and shifts flare. Fit a larger stacked-plate cooler in front of the radiator, in series, with a thermostat if you also need warm-up.",
                        )
                    ],
                    [
                        "Drain and refill ATF. Do not mix types. Use Toyota WS or the labelled spec only.",
                        "Add a remote cooler. Keep lines away from the exhaust.",
                        "If fluid is black and burned, budget a rebuild. Cooler install will not revive cooked clutches.",
                    ],
                )
            ],
            parts=["ATF", "Auxiliary cooler", "Lines and clamps"],
            sources=[source("N80 factory trans cooler notes", "https://unsealed4x4.com.au/toyota-hilux-n80-common-problems/")],
            related=["auto-hard-shift"],
            filters=HILUX_FILTER_N80_1GD,
        ),
        article(
            id="hilux-n80-door-drain",
            title="Early N80 missing door drain plugs and wet carpets",
            summary="Some early N80 doors were built without drain plugs. Water sits in the door, rusts the shell, and overflows onto the carpet.",
            severity="low",
            locations=["inside", "outside"],
            senses=["look", "smell"],
            systems=["body-electrical"],
            symptoms=["Wet carpet after rain", "Door that gurgles", "Window slow in one door"],
            safety=["Support the door. Disconnect the battery if you are near airbag looms in the door."],
            tools=["Trim tools", "Drain plugs or grommets", "Moisture meter"],
            causes=[
                cause(
                    1,
                    "Blocked or missing door drains",
                    "common on early N80",
                    "Water has nowhere to leave the door cavity.",
                    [
                        test(
                            "Hose test",
                            "Remove the door card. Pour a small amount of water into the cavity. It must exit at the bottom drains, not onto the carpet.",
                            "Water exits the drains.",
                            "Water sits or exits onto the sill. Open the drain holes and fit plugs that still drain.",
                        )
                    ],
                    [
                        "Clear the drain holes. Fit the missing plugs.",
                        "Dry the carpet and underlay. Treat rust in the door skin from the inside.",
                        "Check the speaker and module for water.",
                    ],
                )
            ],
            parts=["Door drain plugs", "Door film"],
            sources=[source("Early N80 door drain plugs", "https://unsealed4x4.com.au/toyota-hilux-n80-common-problems/")],
            related=["exterior-water-ingress"],
            filters=[{"generationId": "hilux-n80", "yearFrom": 2015, "yearTo": 2017}],
        ),
        article(
            id="hilux-thin-paint",
            title="Hilux stone chips and thin factory paint",
            summary="N80 paint is thin on leading edges. Chips rust if you leave bare metal. Treat it as body work, not a polish job.",
            severity="low",
            locations=["outside", "front"],
            senses=["look"],
            systems=["body-electrical"],
            symptoms=["Chips on bonnet and guards", "Brown dots at chip edges"],
            safety=["Use rust converter in a ventilated space."],
            tools=["400-800 wet paper", "Etch primer", "Colour-matched two-pack or a quality touch stick"],
            causes=[
                cause(
                    1,
                    "Thin film build on leading panels",
                    "common across N80 years",
                    "Factory film is easy to break with bull-dust and stones.",
                    [
                        test(
                            "Chip depth",
                            "If you see silver or brown, you are through the film. If it is only colour, you can wet-sand and polish.",
                            "Colour only, no rust.",
                            "Bare metal or rust. Clean, convert, prime, and paint.",
                        )
                    ],
                    [
                        "Clean the chip. Convert rust. Prime. Paint. Clear.",
                        "Fit a genuine-thickness wrap or a stone guard if the truck lives on gravel.",
                    ],
                )
            ],
            parts=["Touch paint", "Stone guard film"],
            sources=[source("N80 thin paint", "https://unsealed4x4.com.au/toyota-hilux-n80-common-problems/")],
            filters=[{"modelId": "hilux"}],
        ),
        article(
            id="hilux-vactive-no-assist",
            title="Hilux V-Active 48V assist missing",
            summary="AU HiLux V-Active (2024-on, continuing on 2026 higher grades) uses an 8.5 kW / 65 Nm belt motor-generator, a 48V pack, and a DC-DC. If assist and idle-stop die, test 12V and the belt before you condemn the pack.",
            severity="high",
            locations=["engine-bay", "electrical", "inside"],
            senses=["performance", "look"],
            systems=["mhev-48v", "body-electrical"],
            symptoms=["V-Active lamp", "No idle-stop", "Heavy steering-like take-off", "12V battery going flat"],
            safety=COMMON_SAFETY_BAY + [
                "Blue 48V cables can still injure. Isolate the 12V earth, open the 48V service connector if equipped, wait, then measure.",
            ],
            tools=COMMON_SCAN + ["12V load tester", "Clamp meter", "Belt tool for the aramid 48V belt"],
            causes=[
                cause(
                    1,
                    "12V battery or DC-DC not supporting the control module",
                    "very-common",
                    "The 48V controller thinks on 12V. A tired 12V pack disables assist and looks like a 48V failure.",
                    [
                        test(
                            "12V load test then DC-DC output",
                            "Load-test the 12V. Engine running, measure 12V at the jump posts. Then read 48V SOC and DC-DC command on a scan tool.",
                            "12V load-test passes. Running voltage is in the mid-14s if the DC-DC is charging.",
                            "12V fails load or stays at battery rest while 48V SOC is healthy. Replace 12V first, then test DC-DC.",
                        )
                    ],
                    [
                        "Replace a failed 12V with the specified AGM or EFB.",
                        "If 12V is good and DC-DC will not output, replace the DC-DC. These units are not repaired in the field.",
                        "Complete any required coding so the new converter talks to the 48V BMS.",
                    ],
                ),
                cause(
                    2,
                    "Belt slip on the motor-generator",
                    "common",
                    "The 48V belt carries motoring torque. A glazed belt slips and the system disables assist.",
                    [
                        test(
                            "Belt and restart quality",
                            "Inspect ribs, glaze, and tensioner travel. Command a restart and watch slip pids if available.",
                            "Belt is dry, ribs are sharp, restart is crisp.",
                            "Glaze, dust, or a lazy restart. Fit the specified aramid 48V belt. Do not twist it during install.",
                        )
                    ],
                    ["Replace belt and tensioner as a pair if the tensioner has a dead spot. Clear codes and road-test take-off."],
                ),
            ],
            specs=[
                spec("V-Active motor", "8.5 kW and 65 Nm on the belt generator (Toyota AU / EU figures)"),
                spec("Pack location", "Under the rear seat on many Hilux 48V trucks. Stay off the cooling vents."),
            ],
            parts=["12V battery", "48V belt", "DC-DC converter"],
            sources=[
                source("Toyota Europe Hilux Hybrid 48V newsroom", "https://newsroom.toyota.eu/new-hilux-hybrid-48v-enhances-an-invincible-icon/"),
                source("Drive: 2024 HiLux V-Active details", "https://www.drive.com.au/news/2024-toyota-hilux-mild-hybrid-tech-details/"),
                source("4x4 Australia 2026 HiLux V-Active", "https://www.4x4australia.com.au/news/2026-toyota-hilux-revealed"),
            ],
            related=["hilux-vactive-dcdc", "hilux-vactive-belt", "mhev-12v-first"],
            filters=HILUX_FILTER_48V,
        ),
        article(
            id="hilux-vactive-dcdc",
            title="V-Active DC-DC not charging the 12V",
            summary="The 48V pack feeds the 12V system through a DC-DC. A dead converter leaves a perfect 48V pack and a flat 12V.",
            severity="high",
            locations=["electrical"],
            senses=["look", "performance"],
            systems=["mhev-48v"],
            symptoms=["12V dies overnight", "No charging voltage with a good 48V SOC", "Cluster brown-out"],
            safety=COMMON_SAFETY_BAY,
            tools=["Multimeter", "Scan tool with DC-DC pids"],
            causes=[
                cause(
                    1,
                    "Failed DC-DC converter",
                    "common on 48V vehicles generally",
                    "Castrol and field reports list DC-DC failure as the usual reason a 48V car stops charging 12V.",
                    [
                        test(
                            "Compare 48V SOC to 12V running voltage",
                            "Engine running, 48V SOC above 40 percent. 12V should be charged by the converter.",
                            "12V rises into charge range.",
                            "12V stays at rest. Replace the DC-DC. Do not keep jump-starting. You will cook the 12V.",
                        )
                    ],
                    ["Replace the DC-DC. Code it. Load-test the 12V and replace it if it was repeatedly flattened."],
                )
            ],
            parts=["DC-DC converter", "12V battery"],
            sources=[source("Castrol 12V/48V service complications", "https://www.castrol.com/en_gb/united-kingdom/home/learn/castrol-fastscan/service-problems-and-diagnostic-complications-in-vehicles-equipped-with-12V-48V-electrical-installation.html")],
            related=["hilux-vactive-no-assist", "mhev-dcdc-fail"],
            filters=HILUX_FILTER_48V,
        ),
        article(
            id="hilux-vactive-belt",
            title="V-Active 48V belt chirp and failed restart",
            summary="The V-Active belt is a structural part of the hybrid assist. A cheap 12V-style belt will slip under motoring torque.",
            severity="medium",
            locations=["engine-bay"],
            senses=["sound", "performance"],
            systems=["mhev-48v", "air-turbo"],
            symptoms=["Chirp on idle-stop restart", "Glaze on ribs", "Assist cut after a wet start"],
            safety=COMMON_SAFETY_BAY,
            tools=["Belt tool", "Specified 48V belt"],
            causes=[
                cause(
                    1,
                    "Wrong belt or worn tensioner",
                    "common",
                    "48V belts are aramid-reinforced and have a service procedure. They cannot be bent back on themselves.",
                    [
                        test(
                            "Inspect and restart",
                            "Check part number, glaze, and tensioner sweep. Wet the belt lightly. A slip that appears only when wet is the belt.",
                            "Correct part, quiet restart.",
                            "Wrong part or glaze. Replace belt and check pulley alignment.",
                        )
                    ],
                    ["Fit the specified belt. Route it without twisting. Recheck after a heat cycle."],
                )
            ],
            parts=["48V aramid belt", "Tensioner"],
            sources=[source("Tomorrow's Technician 48V belt systems", "https://www.tomorrowstechnician.com/belt-drive-systems-for-audi-and-bmw-mild-hybrids/")],
            related=["hilux-vactive-no-assist", "squeal-cold-belt"],
            filters=HILUX_FILTER_48V,
        ),
    ]
