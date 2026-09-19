"""Articles recovered from the original Unity MechMate diagnostic graphs.

Node names came from Raeion/MechMate DiagnosisManager and the VDH / subgraph
assets. Procedures are original workshop writing, not copied from Unity UI
copy or from workshop manuals.
"""

from catalog_common import COMMON_SAFETY_BAY, article, cause, source, spec, test

U = [{"universal": True}]


def articles():
    return [
        article(
            id="fluid-leak-colour",
            title="Fluid leak: read the colour first",
            summary="The original MechMate opened Fluid Leak as its own path. Colour, smell, and where it lands beat guessing a pump.",
            severity="high",
            locations=["engine-bay", "under", "front"],
            senses=["look", "leak", "smell"],
            systems=["lubrication", "cooling", "brakes"],
            symptoms=["Spot on the driveway", "Drip on the crossmember", "Wet residual after a wash"],
            safety=COMMON_SAFETY_BAY
            + [
                "Do not taste fluid. Brake fluid and coolant are toxic.",
                "Wipe a petrol or diesel leak and keep ignition sources away before you keep testing.",
            ],
            tools=["White paper towel", "UV lamp if you have dye", "Gloves"],
            causes=[
                cause(
                    1,
                    "Engine oil, coolant, or fuel",
                    "very-common",
                    "Brown or black and oily is engine oil. Green, blue, or orange and sweet is coolant. Clear with a diesel or petrol smell is fuel.",
                    [
                        test(
                            "Towel blot and location",
                            "Blot the drip on a clean towel. Note colour, feel, and whether it is under the sump, radiator, or tank.",
                            "You can name the family: oil, coolant, or fuel.",
                            "It smears like oil under the sump, or it is sweet at the radiator, or it smells like fuel at a filter or line.",
                        )
                    ],
                    [
                        "Oil: find the highest wet point. Common are the sump gasket, cam cover, and the turbo feed.",
                        "Coolant: pressure-test the system cold. Replace the leaking hose, radiator, or water pump.",
                        "Fuel: replace the leaking hose or filter bowl. Do not drive with a wet fuel rail.",
                    ],
                ),
                cause(
                    2,
                    "ATF, power steering, or brake fluid",
                    "common",
                    "Pink or red and oily is often ATF. Straw or clear and slick near the rack is power steering. Clear and watery that strips paint is brake fluid.",
                    [
                        test(
                            "Reservoir levels after a clean-up",
                            "Wipe the leak. Mark each reservoir. Drive 10 km and recheck levels.",
                            "Levels hold.",
                            "One reservoir dropped. That circuit is the leak. Brake fluid on paint needs a wash now, then a leak fix.",
                        )
                    ],
                    [
                        "ATF: inspect the cooler lines and the pan gasket. Repair the leak, then set the level hot in park.",
                        "Power steering: repair the hose or pump seal, then bleed the rack until the bottle stays full.",
                        "Brake: replace the leaking hose, caliper, or master. Bleed that circuit and confirm a firm pedal.",
                    ],
                ),
            ],
            specs=[
                spec(
                    "Colour is a clue, not a brand",
                    "Some ATF is amber. Some coolant is pink. Confirm with the bottle cap and the smell.",
                )
            ],
            parts=["Paper towel", "Correct fluid for the circuit you proved"],
            sources=[
                source(
                    "NTC Australia: handling automotive fluids",
                    "https://www.ntc.gov.au/",
                )
            ],
            related=["engine-oil-leak", "brake-fluid-low", "power-steering-assist-loss"],
            filters=U,
        ),
        article(
            id="steering-pull-after-brakes",
            title="Pulls to one side after a brake job",
            summary="Unity MechMate split steering pull into caliper, bleed, drum, flat tyre, alignment, and bearing. After fresh pads, start with a dragging piston or air in one circuit.",
            severity="high",
            locations=["front", "wheels"],
            senses=["feel"],
            systems=["brakes", "steering-suspension"],
            symptoms=["Pulls under the pedal", "One wheel hotter", "Pedal spongy on one side of a split circuit"],
            safety=COMMON_SAFETY_BAY + ["A pulling brake can lock one wheel. Test in a quiet street, not traffic."],
            tools=["Infrared thermometer", "Brake fluid", "Hose clamp or line clamp rated for brake hose"],
            causes=[
                cause(
                    1,
                    "Caliper piston or slide not returning",
                    "very-common",
                    "A tight piston or a seized slide keeps pad drag on one corner. The car pulls that way as soon as you use the pedal.",
                    [
                        test(
                            "Corner temps after 5 km",
                            "Drive gently. Compare rotor or drum temps. Then check slide play and piston retraction.",
                            "Temps within a few degrees. Slides move by hand.",
                            "One corner is much hotter. Service that caliper. Do not keep driving on a locked pad.",
                        )
                    ],
                    ["Rebuild or replace the caliper. Clean and grease the slides with brake-safe grease. Recheck temps."],
                ),
                cause(
                    2,
                    "Air left in one circuit",
                    "common after a pad or hose job",
                    "A circuit that was opened and not bled will grab late. The other side does the work and the car pulls.",
                    [
                        test(
                            "Pedal and a one-circuit bleed",
                            "Hold a firm pedal. If it sinks, there is air or a leak. Bleed the soft corner first, then the rest of that circuit.",
                            "Pedal stays high and the pull is gone.",
                            "Pedal still sinks. Find the leak or finish the bleed until clear fluid comes out with no bubbles.",
                        )
                    ],
                    ["Bleed until the pedal is firm. Replace a hose that weeps at the crimp."],
                ),
                cause(
                    3,
                    "Drum adjustment, flat tyre, or a bearing",
                    "less-common but on the original tree",
                    "A tight drum shoe, a low tyre, or a collapsed bearing will pull even with even rotor temps.",
                    [
                        test(
                            "Pressures, drum drag, hub play",
                            "Set all tyres to the door-sticker pressure. Spin each drum. Lever the hub at 12 and 6.",
                            "Pressures even. Drums free. No hub play.",
                            "Low tyre: inflate and retest. Tight drum: adjust or replace shoes. Play: replace the bearing and the hub if the race is damaged.",
                        )
                    ],
                    ["Fix the tyre or the drum first. Then align if the pull is still there with even temps."],
                ),
            ],
            related=["pull-to-one-side", "grind-brakes", "front-brake-shudder", "wheel-bearing-growl"],
            filters=U,
        ),
        article(
            id="steering-tight-constant",
            title="Steering stays tight all the time",
            summary="The original Tight path split constant tight from a once-per-turn bind. Constant effort is fluid, pump, column, or a seized top bearing.",
            severity="high",
            locations=["front", "engine-bay"],
            senses=["feel"],
            systems=["steering-suspension"],
            symptoms=["Heavy from lock to lock", "Whine that follows steering input", "Worse when the engine is idle"],
            safety=COMMON_SAFETY_BAY + ["Do not force a steering wheel against a lock with the engine off for long. You can damage the pump."],
            tools=["Power steering fluid or a scan of EPAS", "Belt inspection", "12V meter on EPAS cars"],
            causes=[
                cause(
                    1,
                    "Low fluid or a dying hydraulic pump",
                    "common on older racks",
                    "Air in the bottle or a glazed pump belt steals assist at idle, which is when you notice it in a car park.",
                    [
                        test(
                            "Bottle, belt, and idle assist",
                            "Check the reservoir with the engine off. Then start it and turn slowly. Listen at the pump.",
                            "Level holds and assist is even.",
                            "Foamy fluid or a scream from the pump. Repair the leak, fill with the marked fluid, and bleed. Replace a pump that still screams with a full bottle.",
                        )
                    ],
                    ["Repair the leak first. Bleed until the bottle stays clear. Replace the pump if assist is still gone."],
                ),
                cause(
                    2,
                    "Seized strut bearing or column",
                    "common",
                    "A dry strut top makes the wheel heavy and it springs back oddly. A dry column bearing is heavy even with the car in the air.",
                    [
                        test(
                            "On stands versus on the ground",
                            "Raise the front. Turn the wheel. If it is still heavy in the air, the rack or column is the bind. If it frees up, look at strut tops and tyre pressure.",
                            "Free in the air and on the ground.",
                            "Heavy in the air: column or rack. Heavy only on the ground: strut tops or tyres.",
                        )
                    ],
                    ["Replace seized strut tops as a pair. Service the column bearing. Do not keep driving a rack that binds."],
                ),
            ],
            related=["power-steering-assist-loss", "steering-tight-180", "front-steering-wander"],
            filters=U,
        ),
        article(
            id="steering-tight-180",
            title="Steering binds every half turn",
            summary="Unity labelled this Every One Eighty. A tight spot that repeats every 180 degrees of wheel travel is a rotating part, not low fluid.",
            severity="high",
            locations=["front"],
            senses=["feel"],
            systems=["steering-suspension"],
            symptoms=["A notch twice per steering revolution", "Worse at full lock", "May clunk as it passes the tight spot"],
            safety=COMMON_SAFETY_BAY,
            tools=["Helper to turn the wheel", "Inspection light"],
            causes=[
                cause(
                    1,
                    "Intermediate shaft joint or a bent column shaft",
                    "common after a kerb or a column change",
                    "A collapsed universal or a bent shaft binds once per half turn. Fluid level will look normal.",
                    [
                        test(
                            "Watch the shaft while a helper turns",
                            "Wheels on stands. Watch the intermediate shaft and the rack input. Feel for the notch with one hand on the joint.",
                            "Joints turn smoothly with no notch.",
                            "The joint locks or the shaft walks. Replace the intermediate shaft. Check the rack input spline for damage.",
                        )
                    ],
                    ["Replace the intermediate shaft. Torque the pinch bolt to the figure in the service sequence you have. Do not reuse a stretched pinch bolt."],
                ),
                cause(
                    2,
                    "Rack bush or a bent rack bar",
                    "less-common",
                    "A collapsed rack mount lets the housing twist. A bent rack bar from a hit binds in the same clock position every time.",
                    [
                        test(
                            "Housing movement and lock-to-lock feel",
                            "Lever the rack housing. Then turn lock to lock and mark the wheel when it binds.",
                            "Housing is tight and the bind is gone.",
                            "Housing moves, or the bind is always at the same wheel clock. Replace bushes or the rack.",
                        )
                    ],
                    ["Replace rack bushes first if they are soft. If the bar is bent, replace the rack and align."],
                ),
            ],
            related=["steering-tight-constant", "front-steering-wander"],
            filters=U,
        ),
        article(
            id="steering-loose-play",
            title="Loose steering with play on centre",
            summary="The original Loose panel sat next to Pulling and Tight. Play on centre is joints and mounts, not a pump.",
            severity="medium",
            locations=["front", "wheels"],
            senses=["feel"],
            systems=["steering-suspension"],
            symptoms=["Dead spot on centre", "Clunk over small bumps", "Wander that needs constant correction"],
            safety=COMMON_SAFETY_BAY,
            tools=["Lever bar", "Helper to shake the wheel"],
            causes=[
                cause(
                    1,
                    "Tie rod, rack mount, or hub play",
                    "very-common",
                    "Inner and outer joints show as a click when a helper flicks the wheel and you hold the joint.",
                    [
                        test(
                            "Hands-on each joint",
                            "Wheels on the ground. Helper flicks the steering a few degrees. Hold each outer joint, then the inner, then the rack mounts, then the hub.",
                            "No click and no visible movement.",
                            "A joint moves or a mount slaps. Replace that part, then align.",
                        )
                    ],
                    ["Replace the worn joint or mount. Align. Recheck hub bearings if the wheel still rocks at 12 and 6."],
                )
            ],
            related=["front-steering-wander", "wheel-bearing-growl", "tyre-inner-shoulder-wear"],
            filters=U,
        ),
        article(
            id="vibration-stationary",
            title="Vibration when the car is still",
            summary="Unity split vibration into When Stationary, When Braking, and While Driving. Stationary shake is mounts, pulleys, or an auto in gear.",
            severity="medium",
            locations=["engine-bay", "inside"],
            senses=["feel", "sound"],
            systems=["engine-mechanical", "mhev-48v"],
            symptoms=["Shake in the seat at idle", "Steering wheel buzz in drive", "Worse when the 48V belt motor cuts in"],
            safety=COMMON_SAFETY_BAY + ["Keep hands clear of a running belt and a 48V pulley."],
            tools=["Stethoscope or a long screwdriver", "Inspection light"],
            causes=[
                cause(
                    1,
                    "Accessory or 48V pulley, then mounts",
                    "very-common",
                    "A failing idler or a 48V generator pulley knocks at idle. Broken engine mounts let the whole bay shake in drive.",
                    [
                        test(
                            "Neutral versus drive, then a pulley watch",
                            "Note the shake in park. Select drive with the brake on. Then watch each pulley for wobble.",
                            "Smooth in park and drive. Pulleys run true.",
                            "Worse in drive: mounts. One pulley wobbles or chirps: replace that pulley or the belt kit. On 48V, start with the 12V battery before you condemn the belt motor.",
                        )
                    ],
                    [
                        "Replace a wobbling idler or tensioner as a set with the belt.",
                        "Replace torn engine or gearbox mounts.",
                        "On V-Active and EQ Boost, confirm 12V health, then inspect the 48V belt.",
                    ],
                )
            ],
            related=["squeal-cold-belt", "mhev-12v-first", "vibration-at-speed"],
            filters=U,
        ),
        article(
            id="vibration-when-braking",
            title="Vibration only when you brake",
            summary="The original When Braking node sat under Vibration, not under Steering. Thickness variation and a loose hub still come first.",
            severity="medium",
            locations=["front", "wheels"],
            senses=["feel"],
            systems=["brakes"],
            symptoms=["Steer shake under the pedal", "Pedal buzz that fades when you lift", "Worse from 80 km/h down"],
            safety=COMMON_SAFETY_BAY,
            tools=["Micrometer", "Hub runout gauge if you have one"],
            causes=[
                cause(
                    1,
                    "Rotor thickness variation or a dirty hub face",
                    "very-common",
                    "A rotor that is still thick enough can still pulse if rust sits between the hat and the hub.",
                    [
                        test(
                            "Clean the hub and measure the rotor",
                            "Mark the hot spots. Measure thickness in 6 places. Then clean the hub face and torque the wheel in a star.",
                            "Thickness even and the pulse is gone after a clean hub.",
                            "Variation over the service limit, or a hub that is still rusty. Machine only if the rotor stays above minimum. Otherwise replace the pair.",
                        )
                    ],
                    ["Replace or machine within the published minimum. Clean every hub face. Torque wheels in a star when they are cold."],
                )
            ],
            related=["front-brake-shudder", "grind-brakes", "vibration-at-speed"],
            filters=U,
        ),
        article(
            id="glass-windscreen-leak",
            title="Water past the windscreen",
            summary="Glass was a first-class Unity category. A wet A-pillar or a drip on the dash is usually urethane, a clogged cowl, or a cracked screen.",
            severity="medium",
            locations=["glass", "inside", "outside"],
            senses=["look", "leak"],
            systems=["body-electrical", "hvac"],
            symptoms=["Wet passenger footwell after rain", "Drip on the dash at the A-pillar", "Musty smell after a wash"],
            safety=COMMON_SAFETY_BAY + ["Keep water off a live fuse box in the cowl. Disconnect the 12V earth if you are flooding that area."],
            tools=["Hose", "Helper inside", "Trim tools"],
            causes=[
                cause(
                    1,
                    "Cowl drain or a failed urethane bed",
                    "very-common",
                    "Leaves in the cowl overflow into the cabin. A screen that was replaced without a continuous urethane bead leaks at the corners.",
                    [
                        test(
                            "Hose on the cowl, then on the glass edge",
                            "Run a hose on the cowl only. If it stays dry inside, move the hose around the glass edge. A helper watches the A-pillar.",
                            "Cowl drains and the cabin stays dry.",
                            "Cowl overflow: clear the drains. Edge leak: reseal or replace the screen with a continuous bead.",
                        )
                    ],
                    ["Clear the cowl. If the urethane is the leak, remove the screen and reset it. Dry the carpet so it does not keep smelling."],
                )
            ],
            related=["exterior-water-ingress", "cabin-musty-smell", "glass-wiper-chatter"],
            filters=U,
        ),
        article(
            id="glass-wiper-chatter",
            title="Wipers chatter or smear",
            summary="The original Glass path covered more than a cracked screen. Chatter is a worn blade, a bent arm, or glass that was waxed.",
            severity="low",
            locations=["glass", "outside"],
            senses=["sound", "look"],
            systems=["body-electrical"],
            symptoms=["Skip across the glass", "Fan-shaped smear", "Squeal on the first wipe"],
            safety=["Do not reach through a running wiper. Turn the ignition off."],
            tools=["New blades", "Glass cleaner that is wax-free", "Arm tension check"],
            causes=[
                cause(
                    1,
                    "Blade rubber, arm spring, or wax on the glass",
                    "very-common",
                    "A blade that has sat in sun folds over. An arm with a weak spring skips. Wax or rain-repellent that is too thick makes any blade chatter.",
                    [
                        test(
                            "New blade on clean glass",
                            "Clean the screen with a wax-free glass cleaner. Fit a new blade. If it still chatters, lift the arm and feel the spring.",
                            "Quiet wipe and an even wet film.",
                            "Still chatters: the arm is bent or the spring is weak. Replace the arm. Do not keep bending it by hand.",
                        )
                    ],
                    ["Replace blades in pairs. Clean the glass. Replace a weak arm. Recheck park position so the blade does not sit in sun-baked rubber."],
                )
            ],
            related=["glass-windscreen-leak", "exterior-water-ingress"],
            filters=U,
        ),
        article(
            id="smell-fuel-vapour",
            title="Fuel smell in or around the car",
            summary="Smell was its own Unity category. A fuel smell is a leak until you prove it is a charcoal canister or a rich cold start.",
            severity="critical",
            locations=["under", "engine-bay", "inside"],
            senses=["smell"],
            systems=["fuel"],
            symptoms=["Petrol or diesel smell after fill", "Smell in the cabin with recirc off", "Wet around a filter or rail"],
            safety=COMMON_SAFETY_BAY
            + [
                "No smoking, no starter sparks, no work over a running engine if you can see wet fuel.",
                "Wipe standing fuel before you crank.",
            ],
            tools=["Inspection light", "Gloves", "Scan for evaporative codes on petrol"],
            causes=[
                cause(
                    1,
                    "Hose, filter, or a filler neck",
                    "very-common",
                    "Most fuel smells are a wet clamp, a cracked filter bowl, or a filler hose that dried out.",
                    [
                        test(
                            "Wipe and watch after a fill",
                            "Fill the tank. Wipe every joint from the filler to the rail. Wait ten minutes with the engine off.",
                            "Everything stays dry.",
                            "A joint wets again. Replace that hose or bowl. Diesel filter bowls crack. Petrol filler hoses perish at the tank.",
                        )
                    ],
                    ["Replace the wet hose or filter. Clear evap codes after a petrol leak. Recheck after the next fill."],
                ),
                cause(
                    2,
                    "Canister purge or a rich cold start",
                    "common on petrol",
                    "A stuck purge valve dumps vapour into the intake at idle. A leaking injector wets a plug and smells in the bay.",
                    [
                        test(
                            "Purge command and plug smell",
                            "Scan purge duty. Pull the hose at idle if the procedure for that engine allows it. Pull one plug after a cold start if it smells rich.",
                            "Purge only when commanded. Plugs dry.",
                            "Purge flows at idle or a plug is wet. Replace the valve or the leaking injector after a leak-down.",
                        )
                    ],
                    ["Replace a stuck purge valve. Repair a leaking injector. Do not keep driving a wet bay."],
                ),
            ],
            related=["fuel-filter-diesel-clog", "smoke-black-fuel", "engine-crank-no-start"],
            filters=U,
        ),
        article(
            id="smell-coolant-sweet",
            title="Sweet coolant smell from the bay or the vents",
            summary="A sweet smell is coolant. Find whether it is an external hose or a heater core before you keep topping up.",
            severity="high",
            locations=["engine-bay", "inside", "front"],
            senses=["smell", "look", "leak"],
            systems=["cooling", "hvac"],
            symptoms=["Sweet smell after a drive", "Fog on the inside of the glass", "Level drops with no driveway spot"],
            safety=COMMON_SAFETY_BAY + ["Never open a hot cap. Coolant under the car can still be boiling."],
            tools=["Pressure tester", "UV dye if the leak is slow", "Infrared thermometer"],
            causes=[
                cause(
                    1,
                    "Hose, radiator, or heater core",
                    "very-common",
                    "An external leak leaves residue at a clamp. A heater core smells in the cabin and fogs the glass.",
                    [
                        test(
                            "Cold pressure test, then heater smell",
                            "Pressure-test cold. Watch the radiator, pump weep, and hoses. Then run heat inside and smell the vents.",
                            "Holds pressure. Vents smell like air, not coolant.",
                            "External weep: replace that part. Cabin smell with a dry bay: the heater core. Repair it. Do not keep driving a dropping level.",
                        )
                    ],
                    ["Replace the leaking hose, radiator, or heater core. Bleed the system. Confirm the level after two heat cycles."],
                )
            ],
            related=["engine-overheat", "smoke-white-coolant", "cabin-hvac-no-cold"],
            filters=U,
        ),
        article(
            id="smell-electrical-burn",
            title="Electrical burning smell",
            summary="The original Electrical path sat on the home grid for a reason. A burning smell is a load, a poor earth, or a melting loom.",
            severity="critical",
            locations=["electrical", "inside", "engine-bay"],
            senses=["smell", "look"],
            systems=["body-electrical"],
            symptoms=["Hot plastic smell", "One circuit dead after the smell", "Discoloured insulation"],
            safety=[
                "If you see smoke, isolate the 12V earth. On 48V cars, do not pull blue connectors until you have the service sequence and 0V.",
                "Do not keep powering a circuit that already smells.",
            ],
            tools=["Multimeter", "Inspection light", "Circuit load figures if you have them"],
            causes=[
                cause(
                    1,
                    "High resistance joint or a pinched loom",
                    "common",
                    "A dirty earth or a pinched loom heats until the insulation cooks. The fuse may still be intact.",
                    [
                        test(
                            "Voltage drop on the smelling circuit",
                            "Find the circuit that smells. Measure voltage drop on the feed and the earth under load.",
                            "Drop stays low and the smell is gone after you repair the joint.",
                            "Drop is high or the insulation is brown. Remake the joint. Repair the loom. Replace a switch that is burnt inside.",
                        )
                    ],
                    ["Repair the high-resistance joint. Protect the loom. Replace a burnt switch. Recheck the 12V battery if a 48V DC-DC was dumping into a bad earth."],
                )
            ],
            related=["electrical-12v-drain", "charging-system-low", "cabin-cluster-dead"],
            filters=U,
        ),
        article(
            id="body-ext-paint-chip-rust",
            title="Rust starting at a paint chip",
            summary="Body Exterior was a Unity home tile. A chip that already shows brown needs metal work, not another coat of wax.",
            severity="low",
            locations=["outside"],
            senses=["look"],
            systems=["body-electrical"],
            symptoms=["Brown edge on a stone chip", "Blister under paint on a trailing edge", "Surface rust on a tray or sill"],
            safety=["Wear a mask if you grind. Keep sparks off a fuel tank or a 48V pack tray."],
            tools=["Sandpaper", "Rust converter only on the metal you have cleaned", "Primer and colour"],
            causes=[
                cause(
                    1,
                    "Bare steel after a chip or a stone",
                    "very-common on AU utes",
                    "Stone chips on a bonnet or a tray rail go brown in weeks if the metal stays wet.",
                    [
                        test(
                            "Push the blister and check the back",
                            "Press the paint. If it is soft, the rust is under it. Check the other side of the panel.",
                            "Chip is shallow and the metal is bright after a clean.",
                            "Soft blister or rust through. Cut the rust back to bright metal. Treat, prime, and paint. A hole needs a patch.",
                        )
                    ],
                    ["Clean to bright metal. Treat. Prime. Paint. Do not trap rust under filler. Recheck after rain."],
                )
            ],
            related=["exterior-water-ingress", "rear-leaf-sag"],
            filters=U,
        ),
    ]
