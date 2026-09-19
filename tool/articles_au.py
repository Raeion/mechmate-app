from catalog_common import COMMON_SAFETY_BAY, COMMON_SCAN, article, cause, source, spec, test


def articles():
    return [
        article(
            id="ranger-20-biturbo-coolant",
            title="Ranger / Everest 2.0 bi-turbo coolant loss",
            summary="The 2.0 bi-turbo used in PX and Next-Gen Ranger and Everest has a known habit of coolant loss from the degas bottle, EGR, or the complex pipework around the twins. Pressure-test before you buy a head gasket.",
            severity="high",
            locations=["engine-bay", "front"],
            senses=["look", "performance"],
            systems=["cooling"],
            symptoms=["Degas bottle dropping", "White film", "Overheat on a climb"],
            safety=COMMON_SAFETY_BAY,
            tools=["Pressure tester", "UV dye", "Combustion tester"],
            causes=[
                cause(
                    1,
                    "Pipe, cooler, or EGR leak before a head fault",
                    "common",
                    "These engines have a lot of coolant hose. The first job is a cold pressure test with a light.",
                    [
                        test(
                            "Cold pressure test",
                            "Hold system pressure and watch every pipe, the EGR, and the oil cooler area.",
                            "Holds. Combustion test negative.",
                            "Weep at a pipe or cooler: replace that part. Combustion positive: head path.",
                        )
                    ],
                    ["Replace the leaking pipe or cooler. Bleed thoroughly. The bi-turbo is sensitive to leftover air."],
                )
            ],
            related=["engine-overheat"],
            filters=[{"engineId": "bi-turbo-20"}],
            sources=[source("Ford Ranger 2.0 bi-turbo is a high-volume AU powertrain", "https://www.carexpert.com.au")],
        ),
        article(
            id="ranger-10r80-shift",
            title="Ranger 10R80 harsh shifts",
            summary="The 10-speed used in later Rangers can bang on a 1-2 or 2-3 when adaptive values are lost or the fluid is tired. Check level at the specified temp. Do not keep 'adapting' a burnt box.",
            severity="medium",
            locations=["under"],
            senses=["feel"],
            systems=["drivetrain"],
            symptoms=["Bang on light throttle", "Flare", "Limp"],
            safety=COMMON_SAFETY_BAY,
            tools=["Scan ATF temp", "Ford-capable scan tool"],
            causes=[
                cause(
                    1,
                    "Fluid level, adaptive values, or a solenoid",
                    "common",
                    "Level is temperature-specific on this box.",
                    [
                        test(
                            "Level at spec temp then adaptions",
                            "Bring ATF to the published temp window. Set level. Read solenoid performance.",
                            "Level correct, fluid clean, adaptions complete smoothly.",
                            "Burnt fluid or a solenoid that will not adapt. Service or rebuild as the fluid tells you.",
                        )
                    ],
                    ["Correct the level. Run the adaptive drive cycle. Replace fluid only with the specified Mercon type."],
                )
            ],
            related=["auto-hard-shift"],
            filters=[{"generationId": "ranger-px"}, {"generationId": "ranger-p703"}, {"generationId": "everest-ub"}],
        ),
        article(
            id="ranger-dpf",
            title="Ranger DPF limp on short trips",
            summary="Ranger diesels soot up on suburban duty the same way a Hilux does. Read soot and complete a legal regen. Do not delete.",
            severity="high",
            locations=["rear"],
            senses=["look", "performance"],
            systems=["exhaust-dpf"],
            symptoms=["DPF lamp", "Limp", "Fuel use up"],
            safety=COMMON_SAFETY_BAY,
            tools=COMMON_SCAN,
            causes=[
                cause(
                    1,
                    "Incomplete regen",
                    "very-common",
                    "Same physics as the Hilux 1GD, different hardware.",
                    [
                        test(
                            "Soot and a commanded regen",
                            "Read soot. Command a service regen after you confirm oil is not fuel-diluted.",
                            "Soot drops.",
                            "Soot stuck. Inspect pressure pipes and the injector / glow strategy that feeds regen.",
                        )
                    ],
                    ["Complete the regen. Replace a melted DPF. Fix the short-trip pattern or the oil dilution."],
                )
            ],
            related=["dpf-regen-loop"],
            filters=[{"modelId": "ranger"}, {"modelId": "everest"}],
        ),
        article(
            id="dmax-egr-dpf",
            title="Isuzu D-Max 4JJ1 EGR and DPF pairing",
            summary="The 4JJ1 is tough. It still packs an EGR cooler and a DPF. A blocked cooler plus a looping DPF is the usual late-model complaint.",
            severity="medium",
            locations=["engine-bay", "rear"],
            senses=["performance", "look"],
            systems=["exhaust-dpf", "cooling"],
            symptoms=["P0401 family", "DPF lamp", "Coolant smell"],
            safety=COMMON_SAFETY_BAY,
            tools=COMMON_SCAN + ["Cooling pressure tester"],
            causes=[
                cause(
                    1,
                    "EGR cooler soot or a leak, then a DPF that cannot get hot",
                    "common",
                    "Fix the EGR path so the DPF can actually regen.",
                    [
                        test(
                            "EGR command and coolant hold",
                            "Command EGR. Pressure-test cooling.",
                            "EGR moves and cooling holds.",
                            "Stuck EGR or a cooler leak. Repair, then regen the DPF.",
                        )
                    ],
                    ["Clean or replace the EGR cooler. Complete a regen. Do not delete either part."],
                )
            ],
            related=["dpf-regen-loop", "hilux-n80-egr-cooler"],
            filters=[{"engineId": "4jj1"}],
        ),
        article(
            id="triton-egr-cooler",
            title="Triton 4N15 EGR cooler and soot",
            summary="MQ/MR Tritons build soot in the EGR and can leak coolant through the cooler. The test is the same as the Hilux cooler: pressure and a dry intake.",
            severity="high",
            locations=["engine-bay"],
            senses=["look", "smell"],
            systems=["cooling", "air-turbo"],
            symptoms=["Coolant loss", "White smoke", "Idle stumble"],
            safety=COMMON_SAFETY_BAY,
            tools=["Pressure tester", "Borescope"],
            causes=[
                cause(
                    1,
                    "EGR cooler",
                    "common at higher km",
                    "Thermal cycle cracks the core.",
                    [
                        test(
                            "Pressure test into the intake",
                            "Pressurise cold. Watch the EGR and intake.",
                            "Dry.",
                            "Coolant in the intake. Replace the cooler and flush.",
                        )
                    ],
                    ["Replace the cooler. Change oil if coolant reached the sump."],
                )
            ],
            related=["hilux-n80-egr-cooler"],
            filters=[{"engineId": "4n15"}, {"engineId": "4n16"}],
        ),
        article(
            id="navara-ys23-chain",
            title="Navara YS23 timing chain noise",
            summary="NP300 2.3 diesels can rattle a chain. Confirm with cam/crank correlation and oil pressure, same method as the 1GD.",
            severity="medium",
            locations=["engine-bay"],
            senses=["sound"],
            systems=["engine-mechanical"],
            symptoms=["Cold rattle", "Correlation codes"],
            safety=COMMON_SAFETY_BAY,
            tools=COMMON_SCAN + ["Oil pressure gauge"],
            causes=[
                cause(
                    1,
                    "Chain kit wear",
                    "known",
                    "A short rattle with clean codes is a watch. A long rattle with codes is a kit.",
                    [
                        test(
                            "Correlation and duration",
                            "Record the start. Read codes. Check oil pressure.",
                            "Short rattle, no codes, pressure good.",
                            "Long rattle or codes. Replace the chain kit.",
                        )
                    ],
                    ["Fit a full kit. Find why oil pressure was low if it was."],
                )
            ],
            related=["hilux-n80-timing-chain"],
            filters=[{"engineId": "ys23"}],
        ),
        article(
            id="prado-1gd-dpf",
            title="Prado 150 1GD DPF and fifth injector",
            summary="The Prado 150 2.8 shares the early 1GD DPF hardware with the Hilux. The Federal Court window included Prado. Use the Hilux tests.",
            severity="high",
            locations=["rear"],
            senses=["look", "performance"],
            systems=["exhaust-dpf"],
            symptoms=["DPF lamp", "White smoke", "Limp"],
            safety=COMMON_SAFETY_BAY,
            tools=COMMON_SCAN,
            causes=[
                cause(
                    1,
                    "Same 1GD regen hardware",
                    "common 2015-2020",
                    "Fifth injector and soot load first.",
                    [
                        test(
                            "Soot, delta-P, fifth injector temp rise",
                            "Identical to the Hilux N80 DPF article.",
                            "Regen completes.",
                            "No temp rise or soot stuck. Fifth injector or DPF.",
                        )
                    ],
                    ["Follow the Hilux N80 DPF and fifth injector repairs."],
                )
            ],
            related=["hilux-n80-dpf", "hilux-n80-fifth-injector"],
            filters=[{"modelId": "prado", "engineId": "1gd-ftv"}],
            sources=[source("Class action coverage included Prado", "https://www.carify.com.au/toyota/hilux/problems")],
        ),
        article(
            id="prado-4wd-actuator",
            title="Prado 4WD actuator and centre diff",
            summary="A flashing 4WD lamp on a Prado is often the transfer actuator or a sensor, not a broken chain in the t-case.",
            severity="medium",
            locations=["under"],
            senses=["look", "performance"],
            systems=["drivetrain"],
            symptoms=["4WD lamp flash", "No 4L", "Grinding if forced"],
            safety=["Stop if you hear grind. You are crossing gears."],
            tools=COMMON_SCAN + ["Multimeter"],
            causes=[
                cause(
                    1,
                    "Actuator or position sensor",
                    "common",
                    "Command 4L on a scan tool and watch the position pid.",
                    [
                        test(
                            "Position versus command",
                            "Command. The position pid should arrive and stay.",
                            "Position matches.",
                            "Motor current with no position change: actuator. No current: wiring or module.",
                        )
                    ],
                    ["Replace the actuator or repair the loom. Recalibrate if the procedure exists for that year."],
                )
            ],
            related=["4wd-wont-engage"],
            filters=[{"modelId": "prado"}],
        ),
        article(
            id="lc200-injector",
            title="LandCruiser 200 1VD injector balance",
            summary="A 1VD that knocks on one bank or smokes on a cold start often has an injector that is out of quantity. Read correction values before you pull a head.",
            severity="high",
            locations=["engine-bay"],
            senses=["sound", "look"],
            systems=["fuel"],
            symptoms=["Cold knock", "Black smoke on one bank", "Rough idle"],
            safety=COMMON_SAFETY_BAY,
            tools=COMMON_SCAN + ["Return quantity bottles"],
            causes=[
                cause(
                    1,
                    "Injector quantity drift",
                    "common at high km",
                    "Corrections that sit at the rail limit are a failed injector.",
                    [
                        test(
                            "Correction and return",
                            "Read all eight corrections. Bottle the returns.",
                            "Corrections near zero, returns even.",
                            "One injector at the limit. Replace it and code the new QR if required.",
                        )
                    ],
                    ["Replace the failed injector. Change oil if it has been over-fuelling into the sump."],
                )
            ],
            filters=[{"engineId": "1vd-ftv"}],
        ),
        article(
            id="lc70-clutch",
            title="70 Series clutch on a 1VD",
            summary="A 70 Series that smells and flares on a steep climb has a clutch, not a 'need more power' problem. Confirm hydraulics, then replace the kit and check the rear main.",
            severity="medium",
            locations=["under"],
            senses=["performance", "smell"],
            systems=["drivetrain"],
            symptoms=["Flare", "Burnt smell", "High biting point"],
            safety=COMMON_SAFETY_BAY,
            tools=["Helper", "Clutch kit"],
            causes=[
                cause(
                    1,
                    "Worn clutch or a wet disc",
                    "common on 70s that tow",
                    "The rear main on a 1VD can wet the disc.",
                    [
                        test(
                            "Flare test and a look at the bell",
                            "Same as the universal clutch article, then inspect the 1VD rear main area.",
                            "No flare, dry bell.",
                            "Flare or a wet bell. Clutch kit plus rear main if wet.",
                        )
                    ],
                    ["Replace the clutch kit. Fix the rear main if it is leaking. Set free play."],
                )
            ],
            related=["clutch-slip"],
            filters=[{"generationId": "lc-70"}],
        ),
        article(
            id="cx5-diesel-dpf",
            title="Mazda CX-5 diesel DPF (AU)",
            summary="Australian CX-5 diesels soot on short trips. The Skyactiv-D wants a hot run. Read soot and complete a regen. Watch oil dilution after many incomplete events.",
            severity="medium",
            locations=["rear"],
            senses=["performance"],
            systems=["exhaust-dpf", "lubrication"],
            symptoms=["DPF lamp", "Oil level rise", "Limp"],
            safety=COMMON_SAFETY_BAY,
            tools=COMMON_SCAN,
            causes=[
                cause(
                    1,
                    "Incomplete regen and possible oil dilution",
                    "common",
                    "Check the stick every time you regen.",
                    [
                        test(
                            "Soot and oil level",
                            "Read soot. Check oil level and smell.",
                            "Soot drops, oil stays at the mark.",
                            "Oil rising: change it and find why regen keeps failing.",
                        )
                    ],
                    ["Complete a regen. Change diluted oil. Replace a packed DPF."],
                )
            ],
            related=["dpf-regen-loop"],
            filters=[{"generationId": "cx5-kf"}],
        ),
        article(
            id="tucson-gdi-carbon",
            title="Hyundai / Kia GDI intake carbon",
            summary="Direct-injection 2.4s in Tucson, Sportage and i30 grow carbon on the valves because fuel never washes them. A walnut blast restores airflow.",
            severity="medium",
            locations=["engine-bay"],
            senses=["performance"],
            systems=["air-turbo", "engine-mechanical"],
            symptoms=["Cold misfire", "Rough idle", "Lost mid-range"],
            safety=COMMON_SAFETY_BAY,
            tools=["Walnut blaster or a chemical method that does not destroy cats", "Borescope"],
            causes=[
                cause(
                    1,
                    "Valve-back carbon",
                    "very-common on GDI",
                    "Scope the valves. Do not guess.",
                    [
                        test(
                            "Borescope",
                            "Look at the intake valves.",
                            "Valves are wet and clean.",
                            "Dry black crust. Walnut-blast. Replace a PCV that is oiling the intake.",
                        )
                    ],
                    ["Blast the valves. Repair the breather. Use a catch strategy if the owner does short trips."],
                )
            ],
            filters=[{"engineId": "g4kj"}],
        ),
        article(
            id="outlander-awd-coupling",
            title="Outlander AWD coupling overheat or no rear drive",
            summary="The rear coupling on an Outlander or similar Mitsubishi AWD overheats when the wrong fluid is used or the clutch pack is worn. It then leaves the car in front-drive only.",
            severity="medium",
            locations=["under"],
            senses=["performance"],
            systems=["drivetrain"],
            symptoms=["AWD lamp", "Rear wheels do not help in gravel", "Fluid burnt"],
            safety=COMMON_SAFETY_BAY,
            tools=["Correct coupling fluid", "Scan AWD temps"],
            causes=[
                cause(
                    1,
                    "Wrong fluid or a worn pack",
                    "common",
                    "These couplings are fluid-specific.",
                    [
                        test(
                            "Fluid type and a slip test",
                            "Confirm the last fluid. On stands, see if the rear shaft is driven when AWD is commanded.",
                            "Correct fluid, rear shaft driven.",
                            "Burnt or wrong fluid. Service if the pack still holds. Replace the coupling if it does not.",
                        )
                    ],
                    ["Service with the specified fluid only. Replace a coupling that still slips."],
                )
            ],
            filters=[{"modelId": "outlander"}, {"modelId": "pajero-sport"}],
        ),
        article(
            id="forester-head-gasket-watch",
            title="Subaru boxer coolant watch",
            summary="Modern Foresters are better than the old EJ head-gasket cars, but a boxer that loses coolant with no external leak still gets a combustion test. Do not just keep filling it.",
            severity="high",
            locations=["engine-bay"],
            senses=["look", "performance"],
            systems=["cooling", "engine-mechanical"],
            symptoms=["Coolant loss", "May overheat on a climb", "Milky oil if it is late"],
            safety=COMMON_SAFETY_BAY,
            tools=["Combustion tester", "Pressure tester"],
            causes=[
                cause(
                    1,
                    "Internal coolant leak",
                    "watch on boxers",
                    "A negative external pressure test plus a positive combustion test is a gasket.",
                    [
                        test(
                            "External hold versus combustion",
                            "Pressure-test. Combustion-test the tank.",
                            "Holds and combustion negative.",
                            "Combustion positive. Plan heads and gaskets. Check the block for warp.",
                        )
                    ],
                    ["Heads off. Skim. New gaskets. Correct torque sequence. Do not reuse stretched head bolts if they are torque-to-yield."],
                )
            ],
            filters=[{"engineId": "fb25"}],
        ),
        article(
            id="golf-water-pump",
            title="Golf EA888 water pump and thermostat housing",
            summary="EA888 Golfs leak from the plastic pump/stat housing. Coolant on the belt side is the tell. Replace the housing before the belt eats coolant.",
            severity="medium",
            locations=["engine-bay"],
            senses=["look"],
            systems=["cooling"],
            symptoms=["Pink or purple crust at the pump", "Low level", "Belt wet"],
            safety=COMMON_SAFETY_BAY,
            tools=["Housing kit", "Coolant of the VW spec"],
            causes=[
                cause(
                    1,
                    "Plastic housing weep",
                    "very-common",
                    "The weep is usually at the pump seal or the stat joint.",
                    [
                        test(
                            "Cold pressure with a light on the housing",
                            "Pressurise. Watch the housing, not just the radiator.",
                            "Dry.",
                            "Weep at the housing. Replace the pump/stat unit.",
                        )
                    ],
                    ["Replace the housing kit. Bleed. Replace a belt that was soaked."],
                )
            ],
            filters=[{"engineId": "ea888"}, {"engineId": "ea888-mhev"}],
        ),
        article(
            id="hiace-egr",
            title="HiAce 1GD EGR and DPF on delivery duty",
            summary="A HiAce on suburban parcels never gets a regen. Treat it as a 1GD with worse duty. Read soot weekly if it is a fleet van.",
            severity="medium",
            locations=["rear", "engine-bay"],
            senses=["performance"],
            systems=["exhaust-dpf"],
            symptoms=["DPF lamp", "Limp on the freeway ramp"],
            safety=COMMON_SAFETY_BAY,
            tools=COMMON_SCAN,
            causes=[
                cause(
                    1,
                    "Duty cycle plus 1GD hardware",
                    "common",
                    "Use the Hilux 1GD tests.",
                    [
                        test(
                            "Soot and a highway regen",
                            "Read soot. Run a legal regen.",
                            "Soot drops.",
                            "Stuck soot. Fifth injector / DPF path.",
                        )
                    ],
                    ["Schedule a weekly hot run on a fleet van. Repair hardware that fails the Hilux tests."],
                )
            ],
            related=["hilux-n80-dpf"],
            filters=[{"generationId": "hiace-h300"}],
        ),
        article(
            id="amarok-v6-egr",
            title="Amarok 3.0 V6 EGR and intake soot",
            summary="The T9 3.0 V6 Amarok builds EGR soot and can throw boost and EGR codes together. Clean the intake and test the cooler for coolant.",
            severity="medium",
            locations=["engine-bay"],
            senses=["performance"],
            systems=["air-turbo", "cooling"],
            symptoms=["EGR codes", "Lost power", "Coolant loss"],
            safety=COMMON_SAFETY_BAY,
            tools=COMMON_SCAN + ["Intake clean kit"],
            causes=[
                cause(
                    1,
                    "EGR soot or cooler leak",
                    "common",
                    "Same cooler test as the Hilux, more plumbing.",
                    [
                        test(
                            "Command EGR and pressure-test",
                            "Watch MAP. Pressure-test cooling.",
                            "EGR moves, cooling holds.",
                            "Stuck or leaking. Clean or replace.",
                        )
                    ],
                    ["Clean the intake. Replace a leaking cooler."],
                )
            ],
            filters=[{"engineId": "t9-40"}],
        ),
        article(
            id="rav4-hybrid-12v",
            title="RAV4 / Camry / Kluger full hybrid 12V death",
            summary="These are high-voltage hybrids, not 48V. They still have a 12V that runs the contactors. A dead 12V makes a 'dead hybrid' that will not even click. Load-test the 12V first.",
            severity="high",
            locations=["electrical"],
            senses=["look"],
            systems=["body-electrical"],
            symptoms=["Ready will not come up", "Click from the back then silence", "12V lamp"],
            safety=["Orange cables are high voltage. Do not open the HV pack. The 12V is still your first test."],
            tools=["12V load tester"],
            causes=[
                cause(
                    1,
                    "12V too low to close contactors",
                    "very-common",
                    "A 12V that fails a load test will not let Ready come up.",
                    [
                        test(
                            "12V load test",
                            "Load-test. Then try Ready.",
                            "12V passes and Ready comes up.",
                            "12V fails. Replace the 12V. Then look at the DC-DC if it dies again.",
                        )
                    ],
                    ["Replace the 12V. If it dies again with a running Ready light, test the hybrid DC-DC output to the 12V."],
                )
            ],
            filters=[{"engineId": "a25a-fxs"}, {"engineId": "2zr-fxe"}],
        ),
        article(
            id="mg-15t-timing-chain-watch",
            title="MG ZS / HS 1.5T chain and coolant watch",
            summary="These cheap-to-buy SUVs still need a real diagnosis. A rattle on start is a chain. Coolant loss is a housing or a gasket. Measure. Do not just keep filling.",
            severity="medium",
            locations=["engine-bay"],
            senses=["sound", "look"],
            systems=["engine-mechanical", "cooling"],
            symptoms=["Start rattle", "Coolant drop"],
            safety=COMMON_SAFETY_BAY,
            tools=["Scan correlation", "Pressure tester"],
            causes=[
                cause(
                    1,
                    "Chain rattle or a coolant housing",
                    "watch",
                    "Split the two complaints.",
                    [
                        test(
                            "Correlation then a cooling pressure test",
                            "If it rattles, read cam/crank. If it loses coolant, pressure-test.",
                            "No codes, system holds.",
                            "Correlation fail: chain kit. Weep: housing or gasket.",
                        )
                    ],
                    ["Repair the failed system. Use the specified coolant. Do not mix types."],
                )
            ],
            filters=[{"engineId": "mg-15t"}],
        ),
        article(
            id="bt50-shared-ranger",
            title="BT-50 UP/UR shared Ranger 3.2 faults",
            summary="The UP/UR BT-50 is a Ranger PX underneath. Use the 3.2 P5AT fuel-filter, DPF, and cooling tests. The TF BT-50 is an Isuzu: use the 4JJ1 article.",
            severity="medium",
            locations=["engine-bay"],
            senses=["performance"],
            systems=["fuel", "exhaust-dpf"],
            symptoms=["Power loss under load", "DPF lamp"],
            safety=COMMON_SAFETY_BAY,
            tools=COMMON_SCAN,
            causes=[
                cause(
                    1,
                    "Shared platform faults",
                    "common",
                    "Identify UP/UR versus TF first.",
                    [
                        test(
                            "Which generation",
                            "UP/UR has a 3.2 five-cylinder. TF has an Isuzu 3.0.",
                            "You have identified the platform.",
                            "If you treat a TF like a Ranger you will order the wrong filter and the wrong DPF parts.",
                        )
                    ],
                    ["UP/UR: follow Ranger fuel-filter and DPF articles. TF: follow D-Max 4JJ1."],
                )
            ],
            related=["fuel-filter-diesel-clog", "dmax-egr-dpf", "ranger-dpf"],
            filters=[{"modelId": "bt50"}],
        ),
    ]
