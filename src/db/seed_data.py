"""
src/db/seed_data.py - deterministic, hand-authored seed rows for the fleet-ops DB.

Deliberately NOT randomly generated: every benchmark question in sample_queries.md has
exactly one correct answer an intern can check the NL2SQL pipeline's generated SQL
against by reading this file directly. A few facts (e.g. the Scout Chassis's left plasma thruster
being flagged 3 times) are kept consistent with data/documents/chassis_telemetry.txt on
purpose, so a curious intern can cross-check the structured and unstructured stories.
"""

CHASSIS_DATA = [
    {"chassis_class": "Scout Chassis", "status": "needs_maintenance", "energon_core_pct": 84, "last_diagnostic_date": "2024-03-11"},
    {"chassis_class": "Vanguard Chassis", "status": "combat_ready", "energon_core_pct": 97, "last_diagnostic_date": "2024-03-19"},
    {"chassis_class": "Heavy Assault Chassis", "status": "combat_ready", "energon_core_pct": 99, "last_diagnostic_date": "2024-03-20"},
    {"chassis_class": "Aerial Assault Chassis", "status": "combat_ready", "energon_core_pct": 91, "last_diagnostic_date": "2024-03-18"},
    {"chassis_class": "Medical Evac Chassis", "status": "in_storage", "energon_core_pct": 88, "last_diagnostic_date": "2024-02-01"},
    {"chassis_class": "Legacy Combat Chassis", "status": "decommissioned", "energon_core_pct": 0, "last_diagnostic_date": "2012-05-04"},
]

TECHNICIANS = [
    {"name": "Ironhide", "specialty": "Structural", "years_experience": 8},
    {"name": "Optimus Prime", "specialty": "Propulsion", "years_experience": 20},
    {"name": "Ratchet", "specialty": "Avionics", "years_experience": 6},
    {"name": "Wheeljack", "specialty": "Power Systems", "years_experience": 11},
    {"name": "Brawn", "specialty": "Structural", "years_experience": 4},
    {"name": "Teletraan-1 Automated Diagnostics", "specialty": "Software", "years_experience": 0},
]

# chassis / technician below reference CHASSIS_DATA[i]["chassis_class"] / TECHNICIANS[i]["name"] -
# scripts/seed_db.py resolves these to foreign keys by lookup at insert time.
MAINTENANCE_EVENTS = [
    {"chassis": "Scout Chassis", "technician": "Ironhide", "event_date": "2023-12-01", "component": "Left plasma thruster", "issue": "Intermittent fault under cold conditions", "resolution": "Replaced thruster coil and resealed housing", "resolution_hours": 4.5, "cost_usd": 2200},
    {"chassis": "Scout Chassis", "technician": "Ironhide", "event_date": "2024-01-14", "component": "Left plasma thruster", "issue": "Repeat intermittent fault after coil replacement", "resolution": "Escalated to full thruster housing replacement", "resolution_hours": 9, "cost_usd": 6800},
    {"chassis": "Scout Chassis", "technician": "Ironhide", "event_date": "2024-03-02", "component": "Left plasma thruster", "issue": "Fault flagged a third time under sustained cold exposure", "resolution": "Replaced with redesigned cold-rated coil assembly", "resolution_hours": 6, "cost_usd": 4100},
    {"chassis": "Scout Chassis", "technician": "Ratchet", "event_date": "2024-02-10", "component": "HUD display", "issue": "Minor glare artifact in direct sunlight", "resolution": "Recalibrated display polarization filter", "resolution_hours": 1.5, "cost_usd": 300},
    {"chassis": "Scout Chassis", "technician": "Wheeljack", "event_date": "2024-01-22", "component": "Energon core regulator", "issue": "Output dipped 4% below nominal for under a minute", "resolution": "Replaced regulator fuse, retested to spec", "resolution_hours": 2, "cost_usd": 900},
    {"chassis": "Scout Chassis", "technician": "Ironhide", "event_date": "2024-03-11", "component": "Right plasma thruster", "issue": "New fault reported on right side for the first time", "resolution": "Replaced right thruster coil preemptively", "resolution_hours": 4, "cost_usd": 2100},
    {"chassis": "Scout Chassis", "technician": "Ironhide", "event_date": "2024-02-07", "component": "Left gauntlet plating", "issue": "Minor wear from training exercise", "resolution": "Buffed and resealed plating", "resolution_hours": 1, "cost_usd": 150},
    {"chassis": "Scout Chassis", "technician": "Optimus Prime", "event_date": "2024-01-20", "component": "Ion blaster coil", "issue": "Output 3% below spec on diagnostic sweep", "resolution": "Recalibrated ion blaster coil alignment", "resolution_hours": 2, "cost_usd": 500},
    {"chassis": "Vanguard Chassis", "technician": "Optimus Prime", "event_date": "2024-02-03", "component": "Chestplate servo", "issue": "Minor calibration drift after a high-G maneuver", "resolution": "Recalibrated via the diagnostic dock", "resolution_hours": 1, "cost_usd": 150},
    {"chassis": "Vanguard Chassis", "technician": "Optimus Prime", "event_date": "2024-03-19", "component": "Power regulation circuit", "issue": "Output fluctuation of plus or minus 2 percent under sustained load", "resolution": "Replaced the regulation circuit board", "resolution_hours": 3, "cost_usd": 2400},
    {"chassis": "Vanguard Chassis", "technician": "Brawn", "event_date": "2023-12-15", "component": "Left gauntlet plating", "issue": "Hairline stress fracture after impact", "resolution": "Replaced plating section", "resolution_hours": 2.5, "cost_usd": 700},
    {"chassis": "Vanguard Chassis", "technician": "Ironhide", "event_date": "2024-03-05", "component": "Chestplate servo", "issue": "Servo grinding noise reported by pilot", "resolution": "Lubricated and retested servo assembly", "resolution_hours": 1, "cost_usd": 180},
    {"chassis": "Vanguard Chassis", "technician": "Brawn", "event_date": "2024-01-16", "component": "Chestplate integrity", "issue": "Minor scoring from debris impact", "resolution": "Buffed and resealed chestplate coating", "resolution_hours": 1.5, "cost_usd": 300},
    {"chassis": "Vanguard Chassis", "technician": "Wheeljack", "event_date": "2024-03-15", "component": "Energon core regulator", "issue": "Preventive inspection ahead of scheduled mission", "resolution": "No repair needed - logged as passed diagnostic", "resolution_hours": 1, "cost_usd": 0},
    {"chassis": "Heavy Assault Chassis", "technician": "Teletraan-1 Automated Diagnostics", "event_date": "2024-02-20", "component": "Transformation Cog", "issue": "Transformation lag of 0.4 seconds above spec", "resolution": "Applied firmware patch; lag reduced to 0.1 seconds", "resolution_hours": 0.5, "cost_usd": 0},
    {"chassis": "Heavy Assault Chassis", "technician": "Wheeljack", "event_date": "2024-01-05", "component": "Ion blaster coil", "issue": "Thermal throttling triggered below spec threshold", "resolution": "Replaced coolant line, retested under load", "resolution_hours": 3, "cost_usd": 1800},
    {"chassis": "Heavy Assault Chassis", "technician": "Ratchet", "event_date": "2023-12-28", "component": "Targeting HUD", "issue": "Lock time drift of 0.1 seconds above spec", "resolution": "Recalibrated sensor array", "resolution_hours": 1, "cost_usd": 200},
    {"chassis": "Heavy Assault Chassis", "technician": "Brawn", "event_date": "2024-02-14", "component": "Left plasma thruster", "issue": "Minor efficiency loss reported", "resolution": "Cleaned thruster intake, retested to spec", "resolution_hours": 2, "cost_usd": 400},
    {"chassis": "Heavy Assault Chassis", "technician": "Optimus Prime", "event_date": "2024-02-28", "component": "Transformation Cog", "issue": "Routine firmware audit", "resolution": "Updated firmware to latest validated build", "resolution_hours": 1, "cost_usd": 0},
    {"chassis": "Heavy Assault Chassis", "technician": "Ratchet", "event_date": "2024-03-20", "component": "Energon core regulator", "issue": "Routine post-mission inspection", "resolution": "No repair needed - logged as passed diagnostic", "resolution_hours": 0.5, "cost_usd": 0},
    {"chassis": "Aerial Assault Chassis", "technician": "Ironhide", "event_date": "2024-01-30", "component": "Minigun mount", "issue": "Mount vibration exceeding tolerance during sustained fire", "resolution": "Reinforced mount bracket", "resolution_hours": 5, "cost_usd": 3100},
    {"chassis": "Aerial Assault Chassis", "technician": "Brawn", "event_date": "2023-11-18", "component": "Left leg actuator", "issue": "Actuator response delay under heavy load", "resolution": "Replaced actuator servo", "resolution_hours": 4, "cost_usd": 2600},
    {"chassis": "Aerial Assault Chassis", "technician": "Optimus Prime", "event_date": "2024-02-25", "component": "Energon core regulator", "issue": "Output spike during weapons discharge", "resolution": "Installed surge dampener", "resolution_hours": 3.5, "cost_usd": 2900},
    {"chassis": "Aerial Assault Chassis", "technician": "Ratchet", "event_date": "2024-01-27", "component": "Comms array", "issue": "Static interference on priority channel", "resolution": "Replaced comms antenna array", "resolution_hours": 2.5, "cost_usd": 1200},
    {"chassis": "Aerial Assault Chassis", "technician": "Ratchet", "event_date": "2023-11-30", "component": "HUD display", "issue": "Refresh rate below spec under G-load", "resolution": "Replaced HUD driver board", "resolution_hours": 2, "cost_usd": 950},
    {"chassis": "Aerial Assault Chassis", "technician": "Brawn", "event_date": "2023-12-08", "component": "Flight stabilizer", "issue": "Drift during high-speed maneuvering", "resolution": "Recalibrated stabilizer gyroscope", "resolution_hours": 1.5, "cost_usd": 300},
    {"chassis": "Medical Evac Chassis", "technician": "Ratchet", "event_date": "2023-11-05", "component": "Flight stabilizer", "issue": "Minor drift during hover mode", "resolution": "Recalibrated stabilizer gyroscope", "resolution_hours": 1, "cost_usd": 250},
    {"chassis": "Medical Evac Chassis", "technician": "Wheeljack", "event_date": "2024-01-08", "component": "Energon core", "issue": "Routine capacity check, no fault found", "resolution": "No repair needed - logged as passed diagnostic", "resolution_hours": 0.5, "cost_usd": 0},
    {"chassis": "Medical Evac Chassis", "technician": "Wheeljack", "event_date": "2023-12-20", "component": "Energon Core (chest unit, current)", "issue": "Output ceiling test", "resolution": "No repair needed - logged as passed diagnostic", "resolution_hours": 0.5, "cost_usd": 0},
    {"chassis": "Legacy Combat Chassis", "technician": "Optimus Prime", "event_date": "2012-05-04", "component": "Full frame", "issue": "Total structural failure during the Battle of Iacon", "resolution": "Chassis decommissioned, not repaired", "resolution_hours": 0, "cost_usd": 0},
]

CAMPAIGNS = [
    {"chassis": "Scout Chassis", "campaign_date": "2024-01-05", "location": "The Ark Perimeter", "threat_level": 4, "duration_min": 38, "outcome": "success"},
    {"chassis": "Scout Chassis", "campaign_date": "2024-02-18", "location": "Iacon City", "threat_level": 3, "duration_min": 22, "outcome": "success"},
    {"chassis": "Scout Chassis", "campaign_date": "2024-03-01", "location": "Kaon Test Range", "threat_level": 2, "duration_min": 15, "outcome": "success"},
    {"chassis": "Scout Chassis", "campaign_date": "2023-12-12", "location": "Sea of Rust", "threat_level": 2, "duration_min": 14, "outcome": "success"},
    {"chassis": "Vanguard Chassis", "campaign_date": "2024-01-20", "location": "New Iacon", "threat_level": 5, "duration_min": 54, "outcome": "success"},
    {"chassis": "Vanguard Chassis", "campaign_date": "2024-02-05", "location": "Dark Energon Containment Site", "threat_level": 5, "duration_min": 61, "outcome": "partial"},
    {"chassis": "Vanguard Chassis", "campaign_date": "2024-03-10", "location": "Autobot Base Perimeter", "threat_level": 2, "duration_min": 12, "outcome": "success"},
    {"chassis": "Vanguard Chassis", "campaign_date": "2024-02-27", "location": "Coastal Patrol", "threat_level": 3, "duration_min": 19, "outcome": "success"},
    {"chassis": "Heavy Assault Chassis", "campaign_date": "2024-01-12", "location": "Decepticon Border", "threat_level": 5, "duration_min": 47, "outcome": "success"},
    {"chassis": "Heavy Assault Chassis", "campaign_date": "2024-02-22", "location": "Polyhex Airspace", "threat_level": 5, "duration_min": 58, "outcome": "success"},
    {"chassis": "Heavy Assault Chassis", "campaign_date": "2024-03-05", "location": "Tarn Facility", "threat_level": 4, "duration_min": 33, "outcome": "success"},
    {"chassis": "Heavy Assault Chassis", "campaign_date": "2023-12-30", "location": "Test Flight Corridor", "threat_level": 1, "duration_min": 8, "outcome": "success"},
    {"chassis": "Heavy Assault Chassis", "campaign_date": "2024-01-15", "location": "Arctic Research Station", "threat_level": 4, "duration_min": 36, "outcome": "aborted"},
    {"chassis": "Aerial Assault Chassis", "campaign_date": "2024-01-08", "location": "Decepticon Border", "threat_level": 5, "duration_min": 49, "outcome": "success"},
    {"chassis": "Aerial Assault Chassis", "campaign_date": "2024-02-14", "location": "Vos", "threat_level": 4, "duration_min": 30, "outcome": "partial"},
    {"chassis": "Aerial Assault Chassis", "campaign_date": "2024-03-18", "location": "Autobot Joint Exercise", "threat_level": 2, "duration_min": 20, "outcome": "success"},
    {"chassis": "Aerial Assault Chassis", "campaign_date": "2024-03-22", "location": "Orbital Defense Exercise", "threat_level": 3, "duration_min": 28, "outcome": "success"},
    {"chassis": "Medical Evac Chassis", "campaign_date": "2023-11-10", "location": "The Ark Cliffside Recovery", "threat_level": 3, "duration_min": 25, "outcome": "success"},
    {"chassis": "Medical Evac Chassis", "campaign_date": "2024-01-25", "location": "Iacon Expo Backup", "threat_level": 1, "duration_min": 10, "outcome": "success"},
    {"chassis": "Medical Evac Chassis", "campaign_date": "2024-02-01", "location": "Base Command Vault Drill", "threat_level": 1, "duration_min": 9, "outcome": "success"},
]
