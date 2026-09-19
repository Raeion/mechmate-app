from catalog_common import COMMON_SAFETY_BAY, COMMON_SCAN, article, cause, source, spec, test

U = [{"universal": True}]


def articles():
    return [
        article(
            id="engine-no-crank",
            title="No crank: silence or a single click",
            summary="Prove power at the starter solenoid, voltage drop on the earth, and the park/neutral or clutch switch before you buy a starter.",
            severity="high",
            locations=["engine-bay", "electrical"],
            senses=["sound", "performance"],
            systems=["body-electrical"],
            symptoms=["Key or button does nothing", "Single click", "Dash lights dim"],
            safety=COMMON_SAFETY_BAY + ["Keep clear of the starter pinion. It can engage unexpectedly."],
            tools=["Multimeter", "Jumper lead for a solenoid click test", "Load tester"],
            causes=[
                cause(
                    1,
                    "12V battery or voltage drop",
                    "very-common",
                    "A battery that shows 12.4V at rest can still collapse under starter load.",
                    [
                        test(
                            "Voltage at the starter during the crank request",
                            "Measure at the battery, then at the starter B+ and earth during the request.",
                            "Battery stays above about 10V and the starter sees almost the same.",
                            "Battery collapses or you lose more than about 0.5V in the cables. Charge-test the battery. Repair the earth or B+.",
                        )
                    ],
                    ["Replace a failed battery. Clean and remake the earth. Then retest the starter."],
                ),
                cause(
                    2,
                    "Starter solenoid or motor",
                    "common",
                    "A click with good voltage at the solenoid is a starter.",
                    [
                        test(
                            "Solenoid feed",
                            "Confirm 12V on the trigger wire during the request. If the trigger is live and B+ is live, the starter is the part.",
                            "Starter cranks.",
                            "Trigger and B+ are live and it still only clicks. Replace the starter.",
                        )
                    ],
                    ["Replace the starter. On 48V cars the engine restart may be the BSG. Do not confuse a 12V starter with a 48V generator."],
                ),
            ],
            related=["charging-system-low", "mhev-12v-first"],
            filters=U,
        ),
        article(
            id="engine-crank-no-start",
            title="Cranks but will not fire",
            summary="Split the job into spark or glow, fuel, and compression. A diesel that cranks freely with a wet exhaust is not a battery job.",
            severity="high",
            locations=["engine-bay"],
            senses=["performance", "smell"],
            systems=["fuel", "engine-mechanical"],
            symptoms=["Long crank", "Fires then dies", "Fuel smell", "No smoke at all on a diesel"],
            safety=COMMON_SAFETY_BAY + ["Do not crank until the starter cooks. Rest it."],
            tools=COMMON_SCAN + ["Fuel pressure gauge or scan rail pressure", "Glow current probe"],
            causes=[
                cause(
                    1,
                    "No rail pressure or no injector pulse",
                    "common",
                    "A dead lift pump, a clogged diesel filter, or a rail sensor that reads zero will keep it silent.",
                    [
                        test(
                            "Rail pressure while cranking",
                            "Watch rail pressure and RPM while cranking. A modern diesel needs a minimum rail figure before it will inject.",
                            "Rail climbs into the start range and injectors tick.",
                            "Rail stays near zero. Test the lift pump, filter, and high-pressure pump supply.",
                        )
                    ],
                    ["Replace a clogged filter first. Confirm the lift pump. Only then condemn the high-pressure pump."],
                ),
                cause(
                    2,
                    "No glow on a cold diesel",
                    "common in winter",
                    "A failed glow module leaves a cold 1KD or 1GD cranking forever.",
                    [
                        test(
                            "Glow current",
                            "Clamp the glow feed during the preheat lamp. You should see a large current that tapers.",
                            "Current present.",
                            "No current. Test fuses, module, and each glow plug resistance.",
                        )
                    ],
                    ["Replace failed glow plugs as a set if they are old. Replace the module if it does not drive them."],
                ),
            ],
            related=["fuel-filter-diesel-clog", "glow-plug-cold-start"],
            filters=U,
        ),
        article(
            id="engine-overheat",
            title="Temperature climbs and will not settle",
            summary="Confirm the gauge, then the cap, the fans, the thermostat, and a combustion leak. Do not keep driving a climbing gauge.",
            severity="critical",
            locations=["engine-bay", "front"],
            senses=["look", "performance"],
            systems=["cooling"],
            symptoms=["Gauge in the hot zone", "Fan silent", "Heater goes cold", "Sweet steam"],
            safety=COMMON_SAFETY_BAY + ["Never open a hot cap. A scald from a 4x4 header tank is a hospital job."],
            tools=["Infrared thermometer", "Pressure tester", "Combustion gas tester", "Multimeter on fan relays"],
            causes=[
                cause(
                    1,
                    "Fan not commanded or thermostat stuck shut",
                    "very-common",
                    "A stuck thermostat keeps coolant in the engine. A dead fan lets it climb in traffic.",
                    [
                        test(
                            "Cap temps and fan command",
                            "Compare radiator inlet and outlet with an infrared gun. Command the fans.",
                            "Outlet is cooler than inlet when the stat is open. Fans run on command.",
                            "Both tanks are cold while the head is hot: stat shut. Fans silent with a command: relay, fuse, or fan.",
                        )
                    ],
                    ["Replace the thermostat and bleed. Replace fans or relays as tested. Refill with the labelled coolant only."],
                ),
                cause(
                    2,
                    "Head gasket or cracked head putting combustion into the jacket",
                    "less common but critical",
                    "Combustion pressurises the tank and pushes coolant out.",
                    [
                        test(
                            "Combustion gas in the header tank",
                            "Cold system. Combustion tester on the tank. Then a cylinder leak-down if it fails.",
                            "Tester stays the fresh-fluid colour.",
                            "Tester changes. Plan head work. Do not just keep filling the tank.",
                        )
                    ],
                    ["Find the leaking cylinder. Skim and pressure-test the head. Replace the gasket set. Do not reuse a warped head."],
                ),
            ],
            related=["thermostat-stuck", "cooling-fan-dead", "smoke-white-coolant"],
            filters=U,
        ),
        article(
            id="thermostat-stuck",
            title="Thermostat stuck open or shut",
            summary="Stuck shut overheats. Stuck open never reaches temperature, wastes fuel, and leaves a diesel in a regen-unfriendly state.",
            severity="medium",
            locations=["engine-bay"],
            senses=["performance", "look"],
            systems=["cooling"],
            symptoms=["Never warms", "Or climbs immediately", "Heater poor"],
            safety=COMMON_SAFETY_BAY,
            tools=["Infrared thermometer", "Scan coolant temp"],
            causes=[
                cause(
                    1,
                    "Failed thermostat",
                    "common",
                    "The wax motor dies open or shut.",
                    [
                        test(
                            "Warm-up curve",
                            "From cold, watch coolant temp and the two composite radiator tanks.",
                            "Temp climbs steadily. Upper hose stays cool until the stat opens, then both tanks are hot.",
                            "Upper hose hot immediately (stuck open) or engine hot and radiator cold (stuck shut).",
                        )
                    ],
                    ["Replace the thermostat and the gasket. Bleed until no more air spit from the bleed."],
                )
            ],
            filters=U,
        ),
        article(
            id="cooling-fan-dead",
            title="Electric cooling fans do not run",
            summary="Prove power, earth, and the command. A fused fan on a Hilux or Ranger in traffic will overheat with a healthy water pump.",
            severity="high",
            locations=["front"],
            senses=["look", "performance"],
            systems=["cooling", "body-electrical"],
            symptoms=["Overheat only in traffic", "Fans silent when commanded"],
            safety=COMMON_SAFETY_BAY + ["Fans can start without warning. Keep fingers out of the shroud."],
            tools=["Multimeter", "Scan tool to command fans"],
            causes=[
                cause(
                    1,
                    "Fuse, relay, or fan motor",
                    "common",
                    "The control module only provides a command. The current is in the relay circuit.",
                    [
                        test(
                            "Command then power at the fan",
                            "Command high speed. Measure B+ and earth at the fan plug.",
                            "Fans run.",
                            "Power and earth present and the fan is silent: replace the fan. No power: fuse, relay, or wiring.",
                        )
                    ],
                    ["Replace the failed part. Confirm both fans if the car has two."],
                )
            ],
            filters=U,
        ),
        article(
            id="charging-system-low",
            title="Battery light or low running voltage",
            summary="On a 12V car this is the alternator, belt, or a voltage drop. On a 48V car this is often the DC-DC. Measure before you guess.",
            severity="high",
            locations=["engine-bay", "electrical"],
            senses=["look"],
            systems=["body-electrical", "mhev-48v"],
            symptoms=["Battery lamp", "Dim lights at idle", "12V dying"],
            safety=COMMON_SAFETY_BAY,
            tools=["Multimeter", "Clamp meter"],
            causes=[
                cause(
                    1,
                    "Alternator or DC-DC not charging",
                    "very-common",
                    "Identify the architecture first.",
                    [
                        test(
                            "Running voltage and current",
                            "Engine running, loads on. 12V should rise. Clamp the B+ and confirm output.",
                            "Voltage in charge range and current positive.",
                            "No charge. On 12V cars test the belt and alternator. On 48V cars go to the DC-DC article.",
                        )
                    ],
                    ["Replace the charging device that failed the current test. Do not replace a battery that is only the victim unless it fails a load test after charging."],
                )
            ],
            related=["mhev-dcdc-fail"],
            filters=U,
        ),
        article(
            id="electrical-12v-drain",
            title="Battery goes flat overnight",
            summary="A parasitic drain is measured in milliamps after modules sleep. Pull fuses in order while you watch the clamp.",
            severity="medium",
            locations=["electrical"],
            senses=["look"],
            systems=["body-electrical"],
            symptoms=["Dead every morning", "No lamp left on"],
            safety=["Do not pull airbag fuses with the wheel off-centre and the battery live if the procedure says otherwise. Isolate first."],
            tools=["DC clamp or a meter in series", "Fuse puller"],
            causes=[
                cause(
                    1,
                    "Module that will not sleep",
                    "common",
                    "A glovebox USB, a dashcam, or a stuck relay keeps a bus awake.",
                    [
                        test(
                            "Sleep current",
                            "Close the car. Wait the published sleep time (often 10-30 minutes). Measure draw.",
                            "Draw in the tens of milliamps on a healthy late model, higher if a tracker is fitted but still stable.",
                            "Draw in the hundreds of milliamps. Pull fuses until it drops. That circuit is the job.",
                        )
                    ],
                    ["Repair the stuck module or accessory on that fuse. Recheck sleep current."],
                )
            ],
            filters=U,
        ),
        article(
            id="fuel-filter-diesel-clog",
            title="Diesel fuel filter restriction",
            summary="A clogged filter looks like a dying high-pressure pump: rail pressure drops under load, the pedal goes flat, then it recovers at idle.",
            severity="medium",
            locations=["engine-bay", "under"],
            senses=["performance"],
            systems=["fuel"],
            symptoms=["Power loss under load", "Rail pressure falls only when you ask for fuel", "Hard cold start"],
            safety=COMMON_SAFETY_BAY + ["Catch diesel. It is slippery on a concrete floor."],
            tools=["Scan rail pressure", "New filter of the correct type"],
            causes=[
                cause(
                    1,
                    "Restricted filter or water in the bowl",
                    "very-common",
                    "Australian diesel and farm tanks leave water and wax.",
                    [
                        test(
                            "Rail pressure under load versus idle",
                            "Log rail actual versus requested on a hill.",
                            "Actual tracks request.",
                            "Actual falls only under load. Replace the filter and drain water. Retest before you buy a pump.",
                        )
                    ],
                    ["Replace the filter. Prime until the starter does not crank the air out for 20 seconds. Dispose of diesel legally."],
                )
            ],
            filters=U,
        ),
        article(
            id="glow-plug-cold-start",
            title="Cold diesel start and glow plugs",
            summary="One open glow plug can make a 1KD or 4JJ1 crank for 10 seconds on a 5C morning. Measure resistance and current. Do not keep feeding it ether.",
            severity="medium",
            locations=["engine-bay"],
            senses=["performance"],
            systems=["fuel", "engine-mechanical"],
            symptoms=["Long cold crank", "White fuel smoke then it fires", "Preheat lamp behaviour odd"],
            safety=COMMON_SAFETY_BAY + ["No ether on a glow-plugged diesel. You can punch a piston."],
            tools=["Ohmmeter", "Current clamp"],
            causes=[
                cause(
                    1,
                    "Open glow plug or dead module",
                    "common",
                    "Plugs go open-circuit with age.",
                    [
                        test(
                            "Resistance and current",
                            "Each plug should be a low ohm value and should draw current during preheat.",
                            "Even current on all plugs.",
                            "One plug open. Replace the set if they are original. Test the module if none of them are driven.",
                        )
                    ],
                    ["Replace failed plugs with the specified voltage type. Anti-seize on threads only if the maker allows it. Do not over-torque a glow plug into an aluminium head."],
                )
            ],
            filters=U,
        ),
        article(
            id="smoke-white-coolant",
            title="White smoke that smells sweet",
            summary="Sweet white smoke is coolant. Fuel white smoke on a cold diesel smells different and clears. Do not confuse them.",
            severity="high",
            locations=["rear", "engine-bay"],
            senses=["look", "smell"],
            systems=["cooling", "engine-mechanical"],
            symptoms=["Persistent white smoke when warm", "Coolant loss", "Sweet smell"],
            safety=COMMON_SAFETY_BAY,
            tools=["Combustion tester", "Borescope", "Cooling pressure tester"],
            causes=[
                cause(
                    1,
                    "Coolant in the chamber",
                    "common when an EGR cooler or head gasket fails",
                    "An EGR cooler leak can do this with a head that still holds leak-down.",
                    [
                        test(
                            "Coolant loss versus leak-down",
                            "Pressure-test the cold system. Leak-down each cylinder. Inspect the EGR cooler.",
                            "System holds. Leak-down even. Cooler dry.",
                            "Coolant vanishes. Follow the EGR cooler or head-gasket path that the tests indicate.",
                        )
                    ],
                    ["Repair the part that failed the test. Do not just keep adding coolant."],
                )
            ],
            related=["hilux-n80-egr-cooler", "engine-overheat"],
            filters=U,
        ),
        article(
            id="smoke-blue-oil",
            title="Blue smoke from oil",
            summary="Blue smoke is oil. After a long downhill it is often turbo drain or valve guides. On a cold idle it can be rings.",
            severity="medium",
            locations=["rear", "engine-bay"],
            senses=["look"],
            systems=["lubrication", "air-turbo"],
            symptoms=["Blue haze after overrun", "Oil use", "Oily tailpipe"],
            safety=COMMON_SAFETY_BAY,
            tools=["Borescope", "Compression tester"],
            causes=[
                cause(
                    1,
                    "Turbo seal or ring wear",
                    "common",
                    "Oil in the intercooler points at the turbo. Wet plugs on one side can be guides.",
                    [
                        test(
                            "Intercooler and compression",
                            "Pull the cold-side hose. Then compression or leak-down.",
                            "Intercooler dry and compression even.",
                            "Wet intercooler: turbo. Low compression: rings or valves.",
                        )
                    ],
                    ["Replace the turbo if the charger is feeding oil. Rebuild the bottom end if compression is gone."],
                )
            ],
            related=["hilux-turbo-actuator"],
            filters=U,
        ),
        article(
            id="smoke-black-fuel",
            title="Black smoke from unburnt diesel",
            summary="Black smoke is fuel that did not see enough air. Boost leaks, a dirty air filter, a stuck EGR, or a rich injector are the list.",
            severity="medium",
            locations=["rear", "engine-bay"],
            senses=["look", "performance"],
            systems=["air-turbo", "fuel"],
            symptoms=["Black smoke on a hard pull", "Fuel smell", "Power still there or flat"],
            safety=COMMON_SAFETY_BAY,
            tools=["Boost leak tester", "Scan MAF / MAP"],
            causes=[
                cause(
                    1,
                    "Not enough air",
                    "very-common",
                    "A split intercooler hose is the classic Hilux version of this.",
                    [
                        test(
                            "MAP versus MAF and a boost leak test",
                            "Log both. Then pressurise the cold side.",
                            "Air mass matches boost. No leak.",
                            "Boost leak or a MAF that reads low. Fix the air path first, not the injectors.",
                        )
                    ],
                    ["Repair the leak or replace the filter. Only then look at injector quantity."],
                )
            ],
            related=["hilux-intercooler-hose", "hilux-1kd-egr-carbon"],
            filters=U,
        ),
        article(
            id="knock-on-accel",
            title="Knock that appears under load",
            summary="A load knock is mechanical or diesel combustion. A tick that stays at idle is usually valvetrain or an injector. Split them before you pull a sump.",
            severity="critical",
            locations=["engine-bay"],
            senses=["sound", "performance"],
            systems=["engine-mechanical", "fuel"],
            symptoms=["Knock on a pull", "Quiet at idle", "Maybe a misfire"],
            safety=COMMON_SAFETY_BAY + ["A hard knock: shut down."],
            tools=["Stethoscope", "Leak-down", "Injector cut-out on a scan tool"],
            causes=[
                cause(
                    1,
                    "Bearing, piston, or a detonating cylinder",
                    "serious",
                    "If cutting one injector out kills the knock, that cylinder is the crime scene.",
                    [
                        test(
                            "Injector cut-out and leak-down",
                            "Cut injectors one at a time under a light load if it is safe. Then leak-down.",
                            "No change on any cylinder and leak-down is even: look at a heat shield or a loose pulley.",
                            "Knock vanishes on one cylinder. Leak-down or a borescope that cylinder.",
                        )
                    ],
                    ["Repair the failed mechanical part. Do not keep loading a knocking engine."],
                )
            ],
            related=["hilux-1kd-piston-crack"],
            filters=U,
        ),
        article(
            id="tick-at-idle",
            title="Tick at idle that may fade when warm",
            summary="A light tick can be an injector, a lash adjuster, or a heat shield. A heavy tick that grows is a rod. Use a stethoscope, not your phone in the cab.",
            severity="medium",
            locations=["engine-bay"],
            senses=["sound"],
            systems=["engine-mechanical", "fuel"],
            symptoms=["Tick in time with idle", "May change with oil temp"],
            safety=COMMON_SAFETY_BAY,
            tools=["Stethoscope", "Oil pressure gauge"],
            causes=[
                cause(
                    1,
                    "Injector tick versus bottom-end tick",
                    "common",
                    "Injectors tick at the head. Rods tick at the block.",
                    [
                        test(
                            "Stethoscope map and oil pressure",
                            "Compare head, block, and a heat shield. Read hot oil pressure.",
                            "Tick is at the injector body or a shield. Oil pressure is healthy.",
                            "Tick is at the block and oil pressure is low. Stop. That is a bearing job.",
                        )
                    ],
                    ["Repair the source you mapped. Do not ignore a block tick with low oil pressure."],
                )
            ],
            related=["hilux-n80-timing-chain"],
            filters=U,
        ),
        article(
            id="squeal-cold-belt",
            title="Belt squeal on cold start",
            summary="A 12V accessory belt squeals when it is glazed or the tensioner is weak. A 48V belt squeal is a hybrid fault, not a nuisance.",
            severity="low",
            locations=["engine-bay"],
            senses=["sound"],
            systems=["mhev-48v", "body-electrical"],
            symptoms=["Squeal for a few seconds when cold", "Chirp in the rain"],
            safety=COMMON_SAFETY_BAY,
            tools=["Belt dressing is not a fix. Use inspection and the correct belt."],
            causes=[
                cause(
                    1,
                    "Glazed belt or weak tensioner",
                    "very-common",
                    "Dressing hides the noise for a week.",
                    [
                        test(
                            "Inspect ribs and tensioner",
                            "Look for glaze and cracks. Move the tensioner through its travel.",
                            "Belt is matte, tensioner is smooth.",
                            "Glaze or a sticky tensioner. Replace them.",
                        )
                    ],
                    ["Fit the specified belt. On 48V cars use the aramid belt only."],
                )
            ],
            related=["mhev-belt-tensioner"],
            filters=U,
        ),
        article(
            id="grind-brakes",
            title="Grind or shudder when braking",
            summary="A grind is pad steel on a rotor. A shudder is a rotor thickness or runout problem, or a seized slide pin.",
            severity="high",
            locations=["wheels", "front"],
            senses=["sound", "feel"],
            systems=["brakes"],
            symptoms=["Grind", "Steering shimmy under the pedal", "Pull"],
            safety=["Do the job on stands. A falling Hilux is not a learning experience."],
            tools=["Micrometer", "Dial indicator", "Brake cleaner", "Slide-pin grease specified for rubber boots"],
            causes=[
                cause(
                    1,
                    "Pads to the backing plate or a rotor below minimum",
                    "very-common",
                    "You can hear steel. Measure anyway.",
                    [
                        test(
                            "Thickness and pad material",
                            "Measure rotor thickness and look at the pad friction material.",
                            "Rotor above the stamped minimum. Pad material still present.",
                            "Steel showing or rotor under minimum. Replace pads and rotors as an axle set.",
                        )
                    ],
                    [
                        "Replace pads and rotors together on that axle.",
                        "Service slide pins. A seized pin will eat the new set.",
                        "Bed the pads with a series of moderate stops. Do not heat-soak them from a highway then sit.",
                    ],
                )
            ],
            filters=U,
        ),
        article(
            id="hiss-vacuum",
            title="Hiss from the engine bay",
            summary="A hiss that changes with RPM is a vacuum or boost leak. A hiss that stays after shutdown is a cooling system leak.",
            severity="medium",
            locations=["engine-bay"],
            senses=["sound", "performance"],
            systems=["air-turbo", "cooling"],
            symptoms=["Hiss", "Idle wander", "Maybe a leak stain"],
            safety=COMMON_SAFETY_BAY,
            tools=["Smoke machine", "Paper towel"],
            causes=[
                cause(
                    1,
                    "Hose or gasket leak",
                    "common",
                    "Smoke finds it faster than your ear.",
                    [
                        test(
                            "Smoke at idle vacuum or a regulated cold-side pressurise",
                            "Pick vacuum or boost based on whether the noise is at idle or under load.",
                            "No smoke.",
                            "Smoke at a hose, a brake booster, or an EGR gasket. Replace that seal.",
                        )
                    ],
                    ["Replace the leaking hose or gasket. Recheck idle and fuel trims."],
                )
            ],
            related=["hilux-intercooler-hose"],
            filters=U,
        ),
        article(
            id="boom-driveshaft",
            title="Boom or vibration that arrives with speed",
            summary="A boom that tracks road speed is a shaft, a joint, or a tyre. A boom that tracks engine speed is a mount or a damper.",
            severity="medium",
            locations=["under", "wheels"],
            senses=["sound", "feel", "performance"],
            systems=["drivetrain", "steering-suspension"],
            symptoms=["Boom at a set km/h", "Seat vibration", "Maybe a clunk on take-off"],
            safety=COMMON_SAFETY_BAY,
            tools=["Road speed versus RPM notes", "Mark the shaft and tyres"],
            causes=[
                cause(
                    1,
                    "Driveshaft joint or imbalance",
                    "common on utes",
                    "A dry U-joint or a missing balance weight will boom.",
                    [
                        test(
                            "Neutral coast at the boom speed",
                            "If the boom stays in neutral at that road speed, it is rotating with the wheels or shaft. Then inspect joints and tyre balance.",
                            "Joints are tight, tyres are balanced, shaft weights are present.",
                            "Joint has play or a tyre has a broken belt. Repair that first.",
                        )
                    ],
                    ["Replace the failed joint or the tyre. Balance the shaft if a weight is gone."],
                )
            ],
            filters=U,
        ),
        article(
            id="limp-mode",
            title="Limp mode and a dead pedal",
            summary="Limp is a stored fault, not a personality trait. Read the code before you replace a turbo. On a late diesel it is often DPF, boost, or rail.",
            severity="high",
            locations=["inside", "engine-bay"],
            senses=["performance", "look"],
            systems=["exhaust-dpf", "air-turbo", "fuel"],
            symptoms=["Power capped", "Lamp on", "Boost request ignored"],
            safety=COMMON_SAFETY_BAY,
            tools=COMMON_SCAN,
            causes=[
                cause(
                    1,
                    "The code that set limp",
                    "always",
                    "Guessing wastes parts.",
                    [
                        test(
                            "Read and graph the related pid",
                            "Note the code. Graph the sensor it names under a light load.",
                            "Pid matches a mechanical test.",
                            "Pid is implausible. Repair that circuit or part, then clear limp.",
                        )
                    ],
                    ["Fix the cause. Clearing the code without a repair brings limp back on the next drive cycle."],
                )
            ],
            related=["hilux-n80-dpf", "no-boost"],
            filters=U,
        ),
        article(
            id="no-boost",
            title="No boost, long turbo lag",
            summary="Prove the request, the actuator, and the hoses. A silent wastegate or a split hose explains most 'dead turbo' jobs.",
            severity="medium",
            locations=["engine-bay"],
            senses=["performance"],
            systems=["air-turbo"],
            symptoms=["Flat until high RPM", "Whoosh or hiss", "Black smoke"],
            safety=COMMON_SAFETY_BAY,
            tools=["Scan boost", "Smoke machine"],
            causes=[
                cause(
                    1,
                    "Leak or actuator",
                    "very-common",
                    "Same sequence as the Hilux intercooler article, on any turbo car.",
                    [
                        test(
                            "Requested versus actual boost",
                            "Log both. Then leak-test.",
                            "Actual tracks request.",
                            "Actual stays low. Find the leak or free the actuator.",
                        )
                    ],
                    ["Repair the leak or the actuator. Retest on the same road."],
                )
            ],
            related=["hilux-intercooler-hose", "hilux-turbo-actuator"],
            filters=U,
        ),
        article(
            id="high-fuel-use",
            title="Fuel use stepped up and stayed up",
            summary="A sudden step is a leak, a sensor, a dragging brake, or a DPF that is regenerating too often. A slow creep is tyres, alignment, or a dirty intake.",
            severity="low",
            locations=["under", "wheels"],
            senses=["performance"],
            systems=["fuel", "brakes", "exhaust-dpf"],
            symptoms=["L/100 km worse than the last tank", "Maybe a smell of fuel"],
            safety=COMMON_SAFETY_BAY,
            tools=["Scan regen counters", "IR gun on brakes", "Fuel-pressure / leak inspection"],
            causes=[
                cause(
                    1,
                    "Frequent regen, dragging brake, or a leak",
                    "common",
                    "Split sudden versus slow.",
                    [
                        test(
                            "Regen count, brake temps, and a cold-engine sniff",
                            "Compare DPF regen frequency. After a short drive, compare wheel temps. Sniff the rail and the tank.",
                            "Regen interval is normal. Wheel temps even. No fuel smell.",
                            "Regens stacked: DPF path. One wheel much hotter: brake. Fuel smell: leak.",
                        )
                    ],
                    ["Follow the path that failed. Do not just reset an average MPG display."],
                )
            ],
            related=["dpf-regen-loop", "grind-brakes"],
            filters=U,
        ),
        article(
            id="vibration-at-speed",
            title="Vibration that starts at a set speed",
            summary="If it is road-speed specific, spin the wheels and the shaft. If it is engine-speed specific, look at mounts and the 48V belt.",
            severity="medium",
            locations=["wheels", "under"],
            senses=["feel", "performance"],
            systems=["steering-suspension", "drivetrain"],
            symptoms=["Shake in the seat or wheel", "Arrives at a repeatable km/h"],
            safety=COMMON_SAFETY_BAY,
            tools=["Balance figures", "Runout gauge"],
            causes=[
                cause(
                    1,
                    "Tyre, hub, or shaft",
                    "very-common",
                    "A broken belt in a tyre will vibrate even with a perfect balance weight.",
                    [
                        test(
                            "Swap or lift",
                            "If you can, swap front tyres rear. If the shake moves, it is the tyre. Then check hub play and shaft joints.",
                            "No play, tyres round, joints tight.",
                            "A tyre with a broken belt or a hub with play. Replace that part.",
                        )
                    ],
                    ["Replace the failed rotating part. Do not keep adding wheel weights to a broken belt."],
                )
            ],
            related=["boom-driveshaft", "wheel-bearing-growl", "vibration-stationary", "vibration-when-braking"],
            filters=U,
        ),
        article(
            id="pull-to-one-side",
            title="Car pulls to one side",
            summary="A pull that changes with braking is a brake. A pull that is always there is alignment, a tyre, or a seized caliper slide.",
            severity="medium",
            locations=["front", "wheels"],
            senses=["feel"],
            systems=["brakes", "steering-suspension"],
            symptoms=["Constant pull", "Or pull only under the pedal"],
            safety=COMMON_SAFETY_BAY,
            tools=["IR gun", "Alignment rack or at least a tape on toe if you know the method", "Tread depth gauge"],
            causes=[
                cause(
                    1,
                    "Brake drag or tyre/alignment",
                    "common",
                    "Heat tells you a dragging brake in one lap of the block.",
                    [
                        test(
                            "Wheel temps and tread",
                            "Drive 5 km. Compare rotor temps. Then look at inner versus outer tread.",
                            "Temps even. Tread even.",
                            "One rotor hot: service that caliper. Inner shoulder worn: alignment and bushes.",
                        )
                    ],
                    ["Free the caliper or set alignment. Replace a tyre that is already worn to the cords."],
                )
            ],
            related=["steering-pull-after-brakes", "steering-loose-play", "tyre-inner-shoulder-wear"],
            filters=U,
        ),
        article(
            id="dpf-regen-loop",
            title="DPF keeps asking for a regen",
            summary="A healthy DPF regenerates on a hot highway run. A looping DPF has a sensor, a fifth injector, short-trip soot, or a melted substrate. Measure soot and delta-P. Do not cut the can off.",
            severity="high",
            locations=["rear", "under"],
            senses=["look", "performance"],
            systems=["exhaust-dpf"],
            symptoms=["DPF lamp returns within a day", "Fuel use up", "Limp"],
            safety=COMMON_SAFETY_BAY + ["Regen is a fire risk on grass. Illegal delete is not a repair."],
            tools=COMMON_SCAN + ["Pyrometer"],
            causes=[
                cause(
                    1,
                    "Incomplete regen or a failed pressure sensor",
                    "very-common on AU diesels",
                    "Short trips never get the DPF hot. A blocked pressure pipe fakes a full can.",
                    [
                        test(
                            "Soot, delta-P, and a commanded regen",
                            "Read soot and both pressure pipes. Blow the pipes. Then a service regen on a dyno or a long road.",
                            "Soot drops and delta-P is low when clean.",
                            "Soot never drops or delta-P is implausible. Repair the sensor or replace a packed DPF.",
                        )
                    ],
                    ["Clear the pipes. Complete a legal regen. Replace a melted DPF. Fix the oil or injector problem that packed it."],
                )
            ],
            related=["hilux-n80-dpf", "ranger-dpf"],
            filters=U,
        ),
        article(
            id="front-brake-shudder",
            title="Steering shimmy under the brake pedal",
            summary="This is almost never 'warped rotors' from heat alone. It is thickness variation, runout from a dirty hub, or a pad that transferred unevenly.",
            severity="medium",
            locations=["front", "wheels"],
            senses=["feel"],
            systems=["brakes"],
            symptoms=["Shimmy at 80 km/h under light brake"],
            safety=COMMON_SAFETY_BAY,
            tools=["Micrometer", "Dial indicator on the hub"],
            causes=[
                cause(
                    1,
                    "DTV or hub runout",
                    "very-common",
                    "A speck of rust under a new rotor prints runout into the new discs.",
                    [
                        test(
                            "Hub and rotor runout",
                            "Clean the hub to bare metal. Measure rotor runout assembled.",
                            "Runout within the service limit and thickness variation is tiny.",
                            "Runout high. Index the rotor on the hub. If it follows the hub, the hub is bent.",
                        )
                    ],
                    ["Clean the hub. Fit new rotors and pads. Torque wheel nuts in a star with a torque wrench, not a rattle gun only."],
                )
            ],
            related=["grind-brakes"],
            filters=U,
        ),
        article(
            id="wheel-bearing-growl",
            title="Growl that changes in a corner",
            summary="A wheel bearing growl gets louder with a load in one direction. A tyre noise does not.",
            severity="medium",
            locations=["wheels"],
            senses=["sound", "feel"],
            systems=["steering-suspension"],
            symptoms=["Growl 60-100 km/h", "Changes when you lean the car left or right"],
            safety=COMMON_SAFETY_BAY,
            tools=["Road test", "Dial indicator for hub play"],
            causes=[
                cause(
                    1,
                    "Failed hub bearing",
                    "common on utes with offset wheels",
                    "Load the opposite corner to the growl to confirm.",
                    [
                        test(
                            "Corner load and play",
                            "On a quiet road, change lanes. Then check hub play on the stand.",
                            "No play and the growl does not change with load: look at tyres.",
                            "Play or a growl that swaps with load. Replace the hub unit.",
                        )
                    ],
                    ["Replace the hub. Torque the axle nut to the published method if it is a unit hub. Do not guess a stake-nut torque."],
                )
            ],
            filters=U,
        ),
        article(
            id="cv-boot-torn",
            title="Torn CV boot",
            summary="A torn boot is a joint death sentence once the grease is gone and water is in. Replace the boot immediately or the joint soon.",
            severity="medium",
            locations=["wheels", "under"],
            senses=["look"],
            systems=["drivetrain"],
            symptoms=["Grease sprayed in the wheel arch", "Click on full lock if the joint is already dry"],
            safety=COMMON_SAFETY_BAY,
            tools=["Boot kit or a new axle", "Grease of the specified type"],
            causes=[
                cause(
                    1,
                    "Split boot",
                    "very-common on 4x4s",
                    "If the grease is still in and the water is not, a boot kit is enough.",
                    [
                        test(
                            "Inspect the joint",
                            "Peel the boot. Look for rust and pitting.",
                            "Grease still present, no rust.",
                            "Rust or pitting. Replace the axle.",
                        )
                    ],
                    ["Fit a boot kit on a clean joint. Replace the axle if it is already clicking."],
                )
            ],
            filters=U,
        ),
        article(
            id="clutch-slip",
            title="Clutch slip on a manual",
            summary="If RPM rises and road speed does not, the clutch is done. Confirm the hydraulic system is not holding the bearing on.",
            severity="medium",
            locations=["under"],
            senses=["performance", "smell"],
            systems=["drivetrain"],
            symptoms=["RPM flares in a high gear", "Burnt smell", "High pedal"],
            safety=COMMON_SAFETY_BAY,
            tools=["Helper to watch RPM versus GPS speed"],
            causes=[
                cause(
                    1,
                    "Worn friction or oil on the disc",
                    "common on towed manuals",
                    "A rear main leak oils the disc.",
                    [
                        test(
                            "Stall-style check in a safe place and a look at the bellhousing",
                            "In a high gear at low speed, apply a firm throttle. If RPM runs away, it is slipping. Then look for oil at the bell.",
                            "RPM and road speed stay locked.",
                            "RPM runs away. Replace the clutch kit. Repair a rear main if it is wet.",
                        )
                    ],
                    ["Replace cover, disc, and bearing as a kit. Resurface or replace the flywheel as the face demands."],
                )
            ],
            filters=U,
        ),
        article(
            id="auto-hard-shift",
            title="Automatic harsh or late shifts",
            summary="Check ATF level and colour, then temps, then solenoids. A cooked cooler on a Hilux or Ranger will feel like a failing gearbox before the clutches are gone.",
            severity="medium",
            locations=["under"],
            senses=["feel", "performance"],
            systems=["drivetrain"],
            symptoms=["Bang into gear", "Late upshift", "Burnt ATF"],
            safety=COMMON_SAFETY_BAY,
            tools=["Scan ATF temp and shift pids", "ATF of the exact spec"],
            causes=[
                cause(
                    1,
                    "Fluid, heat, or a solenoid",
                    "common",
                    "Brown fluid is already a chemical failure.",
                    [
                        test(
                            "Level, colour, and temp",
                            "Level on a level surface at the specified temp. Smell and colour. Log temp on a climb.",
                            "Fluid is red or the specified colour, level correct, temp stable.",
                            "Burnt or overheated. Service change if it is not black. Rebuild if it is black and full of clutch material.",
                        )
                    ],
                    ["Service the fluid if it is salvageable. Add cooler capacity on a tow vehicle. Diagnose solenoids if fluid is healthy and shifts are still wrong."],
                )
            ],
            related=["hilux-n80-trans-cooler", "ranger-10r80-shift"],
            filters=U,
        ),
        article(
            id="4wd-wont-engage",
            title="4WD will not take",
            summary="On a part-time dual-cab, prove the actuator, the vacuum or motor, and the hubs before you rebuild a transfer case.",
            severity="medium",
            locations=["under", "front"],
            senses=["performance"],
            systems=["drivetrain"],
            symptoms=["Light flashes then dies", "No front shaft spin", "Bind on full lock in 4H on tarmac if it engaged late"],
            safety=["Do not force 4H on a dry high-grip road. You will wind up the front driveline."],
            tools=["Scan 4WD module", "Multimeter on the actuator", "Stands to watch the front shaft"],
            causes=[
                cause(
                    1,
                    "Actuator or hub",
                    "common",
                    "A seized front actuator is the usual dual-cab fault.",
                    [
                        test(
                            "Command and watch the front shaft",
                            "Raise the front safely. Command 4H. The front shaft should turn when you spin a front wheel in a way the design allows, or you should see the actuator move.",
                            "Actuator moves and the front end is locked as designed.",
                            "Actuator silent or hubs rusted. Replace that part.",
                        )
                    ],
                    ["Replace the actuator or service the hubs. Recheck vacuum lines if the system is vacuum-based."],
                )
            ],
            related=["prado-4wd-actuator"],
            filters=U,
        ),
        article(
            id="cabin-hvac-no-cold",
            title="Air conditioning blows warm",
            summary="In Australia you need a refrigerant licence to recover and charge. You can still find the clutch, the condenser fans, and the leak before anyone connects gauges.",
            severity="low",
            locations=["inside", "front"],
            senses=["feel", "look"],
            systems=["hvac"],
            symptoms=["Warm air", "Clutch not clicking", "Fans silent"],
            safety=["Do not vent refrigerant. Recover with licensed equipment."],
            tools=["Sight glass or pressure gauges if you are licensed", "Multimeter on the clutch"],
            causes=[
                cause(
                    1,
                    "No clutch or no airflow through the condenser",
                    "very-common",
                    "A silent clutch is low pressure, a fuse, or a failed coil. A running clutch with a blocked condenser still blows warm.",
                    [
                        test(
                            "Clutch command and condenser fans",
                            "Command A/C. The clutch should click and the condenser fans should run.",
                            "Clutch and fans run. Then do a leak test with licensed gear.",
                            "Clutch silent: check pressure switch circuit and coil. Fans silent: repair fans first.",
                        )
                    ],
                    ["Repair the electrical or fan fault. If the system is empty, leak-test, repair the leak, then charge to the under-bonnet gram spec with licensed gear."],
                )
            ],
            filters=U,
        ),
        article(
            id="cabin-musty-smell",
            title="Musty smell from the vents",
            summary="That smell is a wet evaporator and a blocked drain. Clean the drain and treat the core. Do not just spray perfume.",
            severity="low",
            locations=["inside"],
            senses=["smell"],
            systems=["hvac"],
            symptoms=["Wet-sock smell on A/C start", "Wet passenger carpet"],
            safety=["Do not pour random bleach through a drain that exits onto a loom."],
            tools=["Drain wire", "Evaporator-safe cleaner"],
            causes=[
                cause(
                    1,
                    "Blocked evaporator drain",
                    "very-common",
                    "Water sits on the core and grows biofilm.",
                    [
                        test(
                            "Drain flow",
                            "Run A/C. Water should drip from the drain, not onto the carpet.",
                            "Steady drip outside.",
                            "No drip and a wet carpet. Clear the drain. Dry the carpet.",
                        )
                    ],
                    ["Clear the drain. Treat the core with a product meant for evaporators. Replace a cabin filter that is wet."],
                )
            ],
            filters=U,
        ),
        article(
            id="cabin-airbag-lamp",
            title="Airbag lamp stays on",
            summary="Read the code. The usual dual-cab faults are a clock-spring or a seat-plug that was left half-clicked after a seat-out job. Do not guess a module.",
            severity="high",
            locations=["inside"],
            senses=["look"],
            systems=["body-electrical"],
            symptoms=["Airbag lamp", "Maybe a horn or angle-sensor issue if it is the clock-spring"],
            safety=["Battery earth off and wait before you unplug a yellow connector. Do not probe airbag squibs with a meter on ohms across the bag."],
            tools=["Scan tool that reads SRS"],
            causes=[
                cause(
                    1,
                    "Clock-spring or a seat connector",
                    "common",
                    "The code names the circuit.",
                    [
                        test(
                            "SRS code and connector inspection",
                            "Read the code. Inspect the named connector. Wiggle test only with the battery isolated if the procedure allows.",
                            "Connectors fully latched and the code stays gone after a clear.",
                            "Code returns. Replace the named part (clock-spring, buckle switch, or module) after the wiring proves out.",
                        )
                    ],
                    ["Repair the circuit the code names. Clear and confirm the lamp stays out through an ignition cycle."],
                )
            ],
            filters=U,
        ),
        article(
            id="cabin-window-wont-move",
            title="Window will not drop",
            summary="Prove voltage at the motor, then the regulator. A dual-cab door full of water kills regulators.",
            severity="low",
            locations=["inside", "outside"],
            senses=["sound", "look"],
            systems=["body-electrical"],
            symptoms=["Click but no move", "Or silence"],
            safety=["Support the glass so it cannot drop into the door."],
            tools=["Multimeter", "Door card tools"],
            causes=[
                cause(
                    1,
                    "Motor or regulator",
                    "common",
                    "Voltage at the motor plus a click is a regulator. Silence and no voltage is a switch or loom.",
                    [
                        test(
                            "Voltage at the motor",
                            "Command down. Measure at the motor plug.",
                            "Voltage present and the glass moves.",
                            "Voltage present and no move: regulator or motor. No voltage: switch, fuse, or a broken door loom.",
                        )
                    ],
                    ["Replace the regulator as a unit if the cables are frayed. Repair the loom if it is broken at the hinge."],
                )
            ],
            related=["hilux-n80-door-drain"],
            filters=U,
        ),
        article(
            id="exterior-light-out",
            title="Exterior lamp out",
            summary="LED trucks still have earths and modules. A single lamp out is a globe or a connector. A whole side out is an earth.",
            severity="low",
            locations=["outside", "front", "rear"],
            senses=["look"],
            systems=["body-electrical"],
            symptoms=["One lamp dark", "Or a whole corner dark"],
            safety=["Do not stare into an HID or LED projector."],
            tools=["Multimeter", "Replacement globe of the correct type"],
            causes=[
                cause(
                    1,
                    "Globe, connector, or earth",
                    "very-common",
                    "Green crust in a Hilux rear plug is a standard find.",
                    [
                        test(
                            "Power and earth at the lamp",
                            "Measure both. Wiggle the plug.",
                            "Power and earth present.",
                            "No earth: repair the earth. No power: fuse or switch. Both present: replace the lamp.",
                        )
                    ],
                    ["Repair the corrosion. Dielectric grease after it is clean. Replace the globe or LED module."],
                )
            ],
            filters=U,
        ),
        article(
            id="exterior-water-ingress",
            title="Water in the cabin after rain",
            summary="Find the path with a hose, not with guesswork. Door drains, a windscreen, a roof aerial, and a blocked plenum are the usual four.",
            severity="medium",
            locations=["inside", "outside", "glass"],
            senses=["look", "smell", "leak"],
            systems=["body-electrical"],
            symptoms=["Wet carpet", "Fogged windows", "Musty smell"],
            safety=["Dry the cabin so you do not grow a health problem in the underlay."],
            tools=["Hose", "UV dye optional", "Moisture meter"],
            causes=[
                cause(
                    1,
                    "Drain or seal",
                    "common",
                    "A helper inside with a torch beats tearing the dash first.",
                    [
                        test(
                            "Sectioned hose test",
                            "Wet the screen, then the plenum, then each door, then the tailgate. Stop when the helper sees water.",
                            "No water inside.",
                            "Water appears. Repair that seal or drain.",
                        )
                    ],
                    ["Clear drains. Reseal the glass or aerial. Dry the underlay in the sun or with a dehumidifier."],
                )
            ],
            related=["hilux-n80-door-drain"],
            filters=U,
        ),
        article(
            id="rear-leaf-sag",
            title="Leaf spring sag and a rear that sits low",
            summary="A ute that sits tail-low with no load has tired leaves or a broken leaf. Measure arch, then look for a cracked main leaf.",
            severity="medium",
            locations=["rear", "under"],
            senses=["look", "feel"],
            systems=["steering-suspension"],
            symptoms=["Tray rake", "Bump-steer", "Broken leaf visible"],
            safety=COMMON_SAFETY_BAY,
            tools=["Tape measure", "Spring compressor only if the design needs it"],
            causes=[
                cause(
                    1,
                    "Tired or broken leaf",
                    "very-common on work utes",
                    "A helper leaf that has shifted is also a fail.",
                    [
                        test(
                            "Arch and a visual",
                            "Measure hub to guard on both sides with the truck empty and on level ground.",
                            "Arch even and no cracked leaves.",
                            "One side down or a cracked leaf. Replace the pack as a pair.",
                        )
                    ],
                    ["Replace leaf packs in pairs. Replace tired bushes and U-bolts. Torque U-bolts after the first loaded trip."],
                )
            ],
            filters=U,
        ),
        article(
            id="rear-diff-whine",
            title="Differential whine that follows road speed",
            summary="A whine that changes on and off the throttle is mesh. Low oil or the wrong oil starts it. A smash after a clunk is a bearing or a spider gear.",
            severity="high",
            locations=["rear", "under"],
            senses=["sound"],
            systems=["drivetrain"],
            symptoms=["Whine 60-100 km/h", "Changes on and off throttle"],
            safety=COMMON_SAFETY_BAY,
            tools=["Correct hypoid oil", "Stethoscope on a stand"],
            causes=[
                cause(
                    1,
                    "Low or wrong oil, then worn mesh",
                    "common on towed utes",
                    "A front diff stain on a Hilux is the inspection note. The rear is the same chemistry.",
                    [
                        test(
                            "Level and colour, then a road test",
                            "Fill to the plug. Smell for burnt. Then confirm the whine is road-speed based.",
                            "Oil is full and clean and the whine is gone.",
                            "Oil was low or the whine stays. Rebuild or replace the carrier. Set backlash and preload with a clock gauge.",
                        )
                    ],
                    ["Correct the oil first. If the whine remains, set up a new gear set. Do not just keep filling a roaring diff."],
                )
            ],
            filters=U,
        ),
        article(
            id="tyre-inner-shoulder-wear",
            title="Inner shoulder wear",
            summary="Inner wear on a dual-cab is negative camber from sagged bushes or a lift that was never aligned. It is not 'just cheap tyres'.",
            severity="medium",
            locations=["wheels"],
            senses=["look"],
            systems=["steering-suspension"],
            symptoms=["Inner edge bald", "Feathered tread"],
            safety=["A tyre worn to cords is a blow-out risk. Park it."],
            tools=["Tread depth", "Alignment report"],
            causes=[
                cause(
                    1,
                    "Alignment or worn bushes",
                    "very-common",
                    "Check bushes before you pay for an alignment that cannot hold.",
                    [
                        test(
                            "Bush play and an alignment print",
                            "Lever the control arms. Then align.",
                            "Bushes tight and alignment in spec.",
                            "Play in bushes or camber out. Replace bushes, then align.",
                        )
                    ],
                    ["Replace bushes. Align. Replace tyres that are already to the cords."],
                )
            ],
            filters=U,
        ),
        article(
            id="power-steering-assist-loss",
            title="Steering suddenly heavy",
            summary="Hydraulic systems need fluid and a belt. EPAS needs a live module and a clean torque sensor. 48V cars can lose assist when the 12V sags.",
            severity="high",
            locations=["front", "engine-bay"],
            senses=["feel"],
            systems=["steering-suspension", "mhev-48v"],
            symptoms=["Heavy steering", "Whine on a hydraulic pump", "EPAS lamp"],
            safety=COMMON_SAFETY_BAY,
            tools=["Fluid level", "Scan EPAS", "12V test"],
            causes=[
                cause(
                    1,
                    "Fluid, belt, or a dead EPAS supply",
                    "common",
                    "Identify hydraulic versus electric first.",
                    [
                        test(
                            "Type check",
                            "Hydraulic: level and belt. Electric: 12V at the rack and a scan.",
                            "Fluid full / 12V present and no codes.",
                            "Empty reservoir or a dead 12V feed. Repair that. On 48V cars also run the 12V-first article.",
                        )
                    ],
                    ["Repair the supply. Bleed a hydraulic rack. Do not hold a hydraulic pump on full lock until it boils."],
                )
            ],
            related=["mhev-12v-first"],
            filters=U,
        ),
        article(
            id="brake-fluid-low",
            title="Brake fluid low and a long pedal",
            summary="A falling reservoir is pads worn or a leak. Topping it up without finding which one is how you hide a hose leak.",
            severity="critical",
            locations=["wheels", "front"],
            senses=["feel", "look", "leak"],
            systems=["brakes"],
            symptoms=["Long pedal", "Level below MIN", "Wet caliper or line"],
            safety=["A leaking brake system is a no-drive until it holds a pedal."],
            tools=["Torch", "New DOT 4 or the labelled spec"],
            causes=[
                cause(
                    1,
                    "Pad wear or a hydraulic leak",
                    "critical",
                    "Pads down will drop the level. A wet caliper is a leak.",
                    [
                        test(
                            "Level versus pad thickness and a wet search",
                            "If pads are thin and everything is dry, the level drop is normal wear. If pads are fat and the level is low, find the wet spot.",
                            "Dry system, pads explain the level.",
                            "Wet hose, caliper, or master. Repair before you drive.",
                        )
                    ],
                    ["Replace the leaking part. Bleed until the pedal is hard. Replace pads if they are the reason the level dropped."],
                )
            ],
            filters=U,
        ),
        article(
            id="engine-oil-leak",
            title="Oil on the driveway and a wet engine",
            summary="Clean, run, and read the first wet edge. A rocker cover is not a rear main. A turbo feed is not a sump gasket.",
            severity="medium",
            locations=["engine-bay", "under"],
            senses=["look", "leak"],
            systems=["lubrication"],
            symptoms=["Oil spots", "Burning oil smell on the exhaust"],
            safety=COMMON_SAFETY_BAY,
            tools=["Degreaser", "UV dye optional", "Torx / socket set"],
            causes=[
                cause(
                    1,
                    "The highest wet gasket",
                    "common",
                    "Oil runs down. Start at the top.",
                    [
                        test(
                            "Clean and short run",
                            "Degrease. Run 10 minutes. The first wet edge is the leak.",
                            "Stays dry.",
                            "Wet at a cover, a turbo line, a cooler sandwich, or a rear main. Repair that gasket or line.",
                        )
                    ],
                    ["Replace the leaking seal. If it is a rear main, budget the gearbox-out job and replace the clutch while you are there on a manual."],
                )
            ],
            filters=U,
        ),
        article(
            id="starter-solenoid-click",
            title="Single click, no spin",
            summary="This is voltage drop or a starter. It is almost never 'the starter fuse' if the dash is bright and you still only get one click.",
            severity="medium",
            locations=["engine-bay", "electrical"],
            senses=["sound"],
            systems=["body-electrical"],
            symptoms=["Click", "Dash may dip"],
            safety=COMMON_SAFETY_BAY,
            tools=["Multimeter"],
            causes=[
                cause(
                    1,
                    "Voltage drop or a dead starter",
                    "very-common",
                    "Measure during the click.",
                    [
                        test(
                            "Voltage at the starter case versus B+",
                            "If B+ is healthy and the case is not near 0V relative to battery earth, the earth is the job. If both are good, the starter is the job.",
                            "Starter spins.",
                            "Good voltage, still a click: replace the starter. Bad voltage: cables.",
                        )
                    ],
                    ["Repair the path that failed."],
                )
            ],
            related=["engine-no-crank"],
            filters=U,
        ),
        article(
            id="cabin-cluster-dead",
            title="Cluster dark or reset loop",
            summary="A dark cluster is a supply, an earth, or a failed cluster. On late Toyotas, prove ignition feed and earth before you buy a second-hand cluster that needs coding.",
            severity="medium",
            locations=["inside", "electrical"],
            senses=["look"],
            systems=["body-electrical"],
            symptoms=["Dark cluster", "Random reboot"],
            safety=["Disconnect the battery before the cluster comes out."],
            tools=["Multimeter", "Scan tool"],
            causes=[
                cause(
                    1,
                    "Supply or the cluster itself",
                    "common",
                    "A brown-out from a dying 12V also reboots a cluster.",
                    [
                        test(
                            "12V rest, then feeds at the cluster plug",
                            "Load-test the 12V. Then measure the ignition and constant feeds.",
                            "Feeds present and 12V healthy.",
                            "Missing feed: wiring. Feeds present: cluster. Code a replacement to the car.",
                        )
                    ],
                    ["Repair the feed or replace and code the cluster."],
                )
            ],
            related=["electrical-12v-drain"],
            filters=U,
        ),
        article(
            id="cabin-rattle-dash",
            title="Dash or door card rattle",
            summary="Map the rattle with a folded business card and a passenger. Heat-cycle the cabin. A loose airbag cover is a restraint job, not a glue job.",
            severity="low",
            locations=["inside"],
            senses=["sound"],
            systems=["body-electrical"],
            symptoms=["Rattle on coarse chip", "Goes away when you press a panel"],
            safety=["Do not glue an airbag cover."],
            tools=["Trim tools", "Felt tape"],
            causes=[
                cause(
                    1,
                    "Loose clip or a rattling duct",
                    "common",
                    "Press and hold panels while a passenger drives.",
                    [
                        test(
                            "Press-to-kill",
                            "When the rattle dies under your hand, that panel is the source.",
                            "Rattle gone after felt and clips.",
                            "Rattle remains. Keep mapping. Do not foam-fill a defroster duct shut.",
                        )
                    ],
                    ["Refit clips. Add felt at contact points. Replace a broken clip, do not reuse it."],
                )
            ],
            filters=U,
        ),
        article(
            id="under-exhaust-blow",
            title="Exhaust blow under the floor",
            summary="A tick that is louder over a pit than in the cabin is a manifold or a flex. A blow after the DPF can also fake a boost leak.",
            severity="medium",
            locations=["under", "rear"],
            senses=["sound"],
            systems=["exhaust-dpf"],
            symptoms=["Tick on cold start that may stay", "Soot at a joint"],
            safety=COMMON_SAFETY_BAY + ["A leaking manifold is a carbon monoxide risk in a closed shed."],
            tools=["Smoke or soapy water on a cold engine", "Torch"],
            causes=[
                cause(
                    1,
                    "Gasket, flex, or cracked manifold",
                    "common",
                    "Soot is the arrow.",
                    [
                        test(
                            "Soot map",
                            "Look for dry soot at a joint. A paper held near a suspected crack will flutter.",
                            "Joints are clean and dry.",
                            "Sooted joint. Replace the gasket or the flex. A cracked manifold is a manifold.",
                        )
                    ],
                    ["Replace the leaking part. Use new nuts. Do not reuse stretched manifold studs."],
                )
            ],
            filters=U,
        ),
        article(
            id="radiator-cap-fail",
            title="Cooling system will not hold pressure",
            summary="A weak cap boils the system early. Pressure-test the cap and the system as two jobs.",
            severity="medium",
            locations=["engine-bay"],
            senses=["look", "performance"],
            systems=["cooling"],
            symptoms=["Overflow after a run", "Gauge flickers", "Collapsed upper hose when cold"],
            safety=["Cold cap only."],
            tools=["Cap tester", "System pressure tester"],
            causes=[
                cause(
                    1,
                    "Cap or a real leak",
                    "common",
                    "The cap has a stamped pressure.",
                    [
                        test(
                            "Cap then system",
                            "Test the cap on the tester. Then the system with a good cap.",
                            "Cap holds its rating. System holds.",
                            "Cap fails: replace the cap. System fails: find the leak.",
                        )
                    ],
                    ["Replace the cap with the same pressure rating. Then repair any leak the system test found."],
                )
            ],
            related=["engine-overheat"],
            filters=U,
        ),
        article(
            id="front-steering-wander",
            title="Wander and a vague centre",
            summary="Wander is toe, a loose steering box or rack, or tyres with a broken belt. It is not a 'wheel alignment' if the box has a quarter turn of slop.",
            severity="medium",
            locations=["front"],
            senses=["feel"],
            systems=["steering-suspension"],
            symptoms=["Constant corrections", "Play at the wheel"],
            safety=COMMON_SAFETY_BAY,
            tools=["Lever", "Alignment"],
            causes=[
                cause(
                    1,
                    "Play in the steering or toe out of spec",
                    "common on 70 Series and older utes with a box",
                    "Have a helper wiggle the wheel while you watch the drag link.",
                    [
                        test(
                            "Joint play then alignment",
                            "Watch every joint. Then align.",
                            "No play and toe in spec.",
                            "Play: replace that joint or adjust the box to the service method. Toe out: align after the play is gone.",
                        )
                    ],
                    ["Replace the worn joint. Set toe. Do not tighten a worn box past the service stop."],
                )
            ],
            filters=U,
        ),
    ]
