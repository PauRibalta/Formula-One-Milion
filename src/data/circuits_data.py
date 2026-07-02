from src.models.circuit import Circuit

australia = Circuit(
    "Australia",

    0.60,  # Low Speed Importance
    0.80,  # Medium Speed Importance
    0.85,  # High Speed Importance

    0.80,  # Top Speed Importance
    0.80,  # Acceleration Importance

    0.65,  # Tyre Degradation

    0.65,  # Engine Stress
    0.50,  # Cooling Requirement

    0.85,  # Aerodynamics Importance
    0.75,  # Downforce Importance

    0.70,  # Energy Recovery Potential

    0.55,  # Overtaking Difficulty

    0.25,  # Rain Probability

    0.22,  # Pit Stop Time

    0.70,  # Qualifying Importance

    0.45   # Safety Car Probability
)


china = Circuit(
    "China",

    0.55,  # Low Speed Importance
    0.80,  # Medium Speed Importance
    0.85,  # High Speed Importance

    0.95,  # Top Speed Importance
    0.85,  # Acceleration Importance

    0.70,  # Tyre Degradation

    0.80,  # Engine Stress
    0.65,  # Cooling Requirement

    0.90,  # Aerodynamics Importance
    0.80,  # Downforce Importance

    0.90,  # Energy Recovery Potential

    0.45,  # Overtaking Difficulty

    0.30,  # Rain Probability

    0.23,  # Pit Stop Time

    0.65,  # Qualifying Importance

    0.35   # Safety Car Probability
)


japan = Circuit(
    "Japan",

    0.40,  # Low Speed Importance
    0.95,  # Medium Speed Importance
    1.00,  # High Speed Importance

    0.65,  # Top Speed Importance
    0.75,  # Acceleration Importance

    0.75,  # Tyre Degradation

    0.75,  # Engine Stress
    0.60,  # Cooling Requirement

    1.00,  # Aerodynamics Importance
    1.00,  # Downforce Importance

    0.75,  # Energy Recovery Potential

    0.90,  # Overtaking Difficulty

    0.35,  # Rain Probability

    0.22,  # Pit Stop Time

    0.90,  # Qualifying Importance

    0.45   # Safety Car Probability
)


bahrain = Circuit(
    "Bahrain",

    0.75,  # Low Speed Importance
    0.65,  # Medium Speed Importance
    0.55,  # High Speed Importance

    0.90,  # Top Speed Importance
    0.95,  # Acceleration Importance

    0.95,  # Tyre Degradation

    0.90,  # Engine Stress
    0.95,  # Cooling Requirement

    0.70,  # Aerodynamics Importance
    0.65,  # Downforce Importance

    0.90,  # Energy Recovery Potential

    0.35,  # Overtaking Difficulty

    0.05,  # Rain Probability

    0.24,  # Pit Stop Time

    0.50,  # Qualifying Importance

    0.30   # Safety Car Probability
)


saudi_arabia = Circuit(
    "Saudi Arabia",

    0.30,  # Low Speed Importance
    0.85,  # Medium Speed Importance
    1.00,  # High Speed Importance

    0.95,  # Top Speed Importance
    0.85,  # Acceleration Importance

    0.45,  # Tyre Degradation

    0.75,  # Engine Stress
    0.85,  # Cooling Requirement

    0.95,  # Aerodynamics Importance
    0.90,  # Downforce Importance

    0.75,  # Energy Recovery Potential

    0.60,  # Overtaking Difficulty

    0.02,  # Rain Probability

    0.23,  # Pit Stop Time

    0.80,  # Qualifying Importance

    0.75   # Safety Car Probability
)


miami = Circuit(
    "Miami",

    0.60,  # Low Speed Importance
    0.75,  # Medium Speed Importance
    0.75,  # High Speed Importance

    0.90,  # Top Speed Importance
    0.90,  # Acceleration Importance

    0.65,  # Tyre Degradation

    0.75,  # Engine Stress
    0.85,  # Cooling Requirement

    0.80,  # Aerodynamics Importance
    0.75,  # Downforce Importance

    0.80,  # Energy Recovery Potential

    0.45,  # Overtaking Difficulty

    0.40,  # Rain Probability

    0.21,  # Pit Stop Time

    0.65,  # Qualifying Importance

    0.50   # Safety Car Probability
)


imola = Circuit(
    "Imola",

    0.75,  # Low Speed Importance
    0.85,  # Medium Speed Importance
    0.75,  # High Speed Importance

    0.65,  # Top Speed Importance
    0.75,  # Acceleration Importance

    0.80,  # Tyre Degradation

    0.65,  # Engine Stress
    0.55,  # Cooling Requirement

    0.85,  # Aerodynamics Importance
    0.90,  # Downforce Importance

    0.65,  # Energy Recovery Potential

    0.95,  # Overtaking Difficulty

    0.30,  # Rain Probability

    0.28,  # Pit Stop Time

    0.90,  # Qualifying Importance

    0.55   # Safety Car Probability
)


monaco = Circuit(
    "Monaco",

    1.00,  # Low Speed Importance
    0.40,  # Medium Speed Importance
    0.20,  # High Speed Importance

    0.20,  # Top Speed Importance
    0.60,  # Acceleration Importance

    0.80,  # Tyre Degradation

    0.40,  # Engine Stress
    0.30,  # Cooling Requirement

    0.75,  # Aerodynamics Importance
    1.00,  # Downforce Importance

    0.40,  # Energy Recovery Potential

    1.00,  # Overtaking Difficulty

    0.20,  # Rain Probability

    0.18,  # Pit Stop Time

    1.00,  # Qualifying Importance

    0.70   # Safety Car Probability
)


barcelona = Circuit(
    "Barcelona",

    0.55,  # Low Speed Importance
    0.90,  # Medium Speed Importance
    0.95,  # High Speed Importance

    0.75,  # Top Speed Importance
    0.80,  # Acceleration Importance

    0.75,  # Tyre Degradation

    0.70,  # Engine Stress
    0.60,  # Cooling Requirement

    1.00,  # Aerodynamics Importance
    0.95,  # Downforce Importance

    0.70,  # Energy Recovery Potential

    0.80,  # Overtaking Difficulty

    0.20,  # Rain Probability

    0.22,  # Pit Stop Time

    0.85,  # Qualifying Importance

    0.35   # Safety Car Probability
)


canada = Circuit(
    "Canada",

    0.85,  # Low Speed Importance
    0.55,  # Medium Speed Importance
    0.45,  # High Speed Importance

    0.95,  # Top Speed Importance
    1.00,  # Acceleration Importance

    0.70,  # Tyre Degradation

    0.80,  # Engine Stress
    0.60,  # Cooling Requirement

    0.60,  # Aerodynamics Importance
    0.55,  # Downforce Importance

    0.95,  # Energy Recovery Potential

    0.30,  # Overtaking Difficulty

    0.30,  # Rain Probability

    0.19,  # Pit Stop Time

    0.60,  # Qualifying Importance

    0.75   # Safety Car Probability
)


austria = Circuit(
    "Austria",

    0.55,  # Low Speed Importance
    0.80,  # Medium Speed Importance
    0.80,  # High Speed Importance

    0.95,  # Top Speed Importance
    0.95,  # Acceleration Importance

    0.65,  # Tyre Degradation

    0.75,  # Engine Stress
    0.55,  # Cooling Requirement

    0.80,  # Aerodynamics Importance
    0.75,  # Downforce Importance

    0.90,  # Energy Recovery Potential

    0.35,  # Overtaking Difficulty

    0.35,  # Rain Probability

    0.20,  # Pit Stop Time

    0.60,  # Qualifying Importance

    0.45   # Safety Car Probability
)


silverstone = Circuit(
    "Silverstone",

    0.50,  # Low Speed Importance
    0.90,  # Medium Speed Importance
    1.00,  # High Speed Importance

    0.80,  # Top Speed Importance
    0.85,  # Acceleration Importance

    0.70,  # Tyre Degradation

    0.70,  # Engine Stress
    0.60,  # Cooling Requirement

    0.95,  # Aerodynamics Importance
    0.90,  # Downforce Importance

    0.80,  # Energy Recovery Potential

    0.60,  # Overtaking Difficulty

    0.35,  # Rain Probability

    0.22,  # Pit Stop Time

    0.75,  # Qualifying Importance

    0.55   # Safety Car Probability
)


belgium = Circuit(
    "Belgium",

    0.45,  # Low Speed Importance
    0.80,  # Medium Speed Importance
    1.00,  # High Speed Importance

    1.00,  # Top Speed Importance
    0.85,  # Acceleration Importance

    0.75,  # Tyre Degradation

    0.85,  # Engine Stress
    0.65,  # Cooling Requirement

    0.95,  # Aerodynamics Importance
    0.80,  # Downforce Importance

    0.90,  # Energy Recovery Potential

    0.40,  # Overtaking Difficulty

    0.45,  # Rain Probability

    0.24,  # Pit Stop Time

    0.65,  # Qualifying Importance

    0.70   # Safety Car Probability
)


hungary = Circuit(
    "Hungary",

    0.90,  # Low Speed Importance
    0.80,  # Medium Speed Importance
    0.40,  # High Speed Importance

    0.40,  # Top Speed Importance
    0.75,  # Acceleration Importance

    0.85,  # Tyre Degradation

    0.55,  # Engine Stress
    0.50,  # Cooling Requirement

    0.90,  # Aerodynamics Importance
    0.95,  # Downforce Importance

    0.55,  # Energy Recovery Potential

    0.95,  # Overtaking Difficulty

    0.20,  # Rain Probability

    0.20,  # Pit Stop Time

    0.95,  # Qualifying Importance

    0.45   # Safety Car Probability
)


zandvoort = Circuit(
    "Zandvoort",

    0.75,  # Low Speed Importance
    0.90,  # Medium Speed Importance
    0.75,  # High Speed Importance

    0.55,  # Top Speed Importance
    0.75,  # Acceleration Importance

    0.80,  # Tyre Degradation

    0.60,  # Engine Stress
    0.55,  # Cooling Requirement

    0.95,  # Aerodynamics Importance
    1.00,  # Downforce Importance

    0.60,  # Energy Recovery Potential

    0.90,  # Overtaking Difficulty

    0.30,  # Rain Probability

    0.20,  # Pit Stop Time

    0.90,  # Qualifying Importance

    0.45   # Safety Car Probability
)


monza = Circuit(
    "Monza",

    0.40,  # Low Speed Importance
    0.60,  # Medium Speed Importance
    0.80,  # High Speed Importance

    1.00,  # Top Speed Importance
    0.90,  # Acceleration Importance

    0.60,  # Tyre Degradation

    0.80,  # Engine Stress
    0.50,  # Cooling Requirement

    0.70,  # Aerodynamics Importance
    0.40,  # Downforce Importance

    0.70,  # Energy Recovery Potential

    0.40,  # Overtaking Difficulty

    0.15,  # Rain Probability

    0.25,  # Pit Stop Time

    0.85,  # Qualifying Importance

    0.30   # Safety Car Probability
)


madrid = Circuit(
    "Madrid",

    0.80,  # Low Speed Importance
    0.75,  # Medium Speed Importance
    0.70,  # High Speed Importance

    0.80,  # Top Speed Importance
    0.90,  # Acceleration Importance

    0.75,  # Tyre Degradation

    0.75,  # Engine Stress
    0.80,  # Cooling Requirement

    0.85,  # Aerodynamics Importance
    0.80,  # Downforce Importance

    0.75,  # Energy Recovery Potential

    0.65,  # Overtaking Difficulty

    0.10,  # Rain Probability

    0.22,  # Pit Stop Time

    0.85,  # Qualifying Importance

    0.60   # Safety Car Probability
)


azerbaijan = Circuit(
    "Azerbaijan",

    0.70,  # Low Speed Importance
    0.60,  # Medium Speed Importance
    0.60,  # High Speed Importance

    1.00,  # Top Speed Importance
    0.95,  # Acceleration Importance

    0.55,  # Tyre Degradation

    0.80,  # Engine Stress
    0.70,  # Cooling Requirement

    0.65,  # Aerodynamics Importance
    0.60,  # Downforce Importance

    0.95,  # Energy Recovery Potential

    0.45,  # Overtaking Difficulty

    0.10,  # Rain Probability

    0.19,  # Pit Stop Time

    0.80,  # Qualifying Importance

    0.80   # Safety Car Probability
)


singapore = Circuit(
    "Singapore",

    0.95,  # Low Speed Importance
    0.60,  # Medium Speed Importance
    0.25,  # High Speed Importance

    0.30,  # Top Speed Importance
    0.85,  # Acceleration Importance

    0.90,  # Tyre Degradation

    0.95,  # Engine Stress
    1.00,  # Cooling Requirement

    0.85,  # Aerodynamics Importance
    0.95,  # Downforce Importance

    0.65,  # Energy Recovery Potential

    0.95,  # Overtaking Difficulty

    0.45,  # Rain Probability

    0.28,  # Pit Stop Time

    0.95,  # Qualifying Importance

    0.85   # Safety Car Probability
)


usa = Circuit(
    "United States",

    0.65,  # Low Speed Importance
    0.85,  # Medium Speed Importance
    0.90,  # High Speed Importance

    0.85,  # Top Speed Importance
    0.90,  # Acceleration Importance

    0.70,  # Tyre Degradation

    0.75,  # Engine Stress
    0.65,  # Cooling Requirement

    0.90,  # Aerodynamics Importance
    0.85,  # Downforce Importance

    0.80,  # Energy Recovery Potential

    0.50,  # Overtaking Difficulty

    0.25,  # Rain Probability

    0.21,  # Pit Stop Time

    0.75,  # Qualifying Importance

    0.50   # Safety Car Probability
)


mexico = Circuit(
    "Mexico",

    0.70,  # Low Speed Importance
    0.75,  # Medium Speed Importance
    0.80,  # High Speed Importance

    0.90,  # Top Speed Importance
    0.90,  # Acceleration Importance

    0.60,  # Tyre Degradation

    0.95,  # Engine Stress
    1.00,  # Cooling Requirement

    0.75,  # Aerodynamics Importance
    0.65,  # Downforce Importance

    0.85,  # Energy Recovery Potential

    0.45,  # Overtaking Difficulty

    0.10,  # Rain Probability

    0.20,  # Pit Stop Time

    0.70,  # Qualifying Importance

    0.45   # Safety Car Probability
)


brazil = Circuit(
    "Brazil",

    0.65,  # Low Speed Importance
    0.85,  # Medium Speed Importance
    0.85,  # High Speed Importance

    0.75,  # Top Speed Importance
    0.90,  # Acceleration Importance

    0.75,  # Tyre Degradation

    0.80,  # Engine Stress
    0.70,  # Cooling Requirement

    0.90,  # Aerodynamics Importance
    0.85,  # Downforce Importance

    0.85,  # Energy Recovery Potential

    0.45,  # Overtaking Difficulty

    0.60,  # Rain Probability

    0.21,  # Pit Stop Time

    0.70,  # Qualifying Importance

    0.85   # Safety Car Probability
)


las_vegas = Circuit(
    "Las Vegas",

    0.45,  # Low Speed Importance
    0.55,  # Medium Speed Importance
    0.60,  # High Speed Importance

    1.00,  # Top Speed Importance
    0.95,  # Acceleration Importance

    0.45,  # Tyre Degradation

    0.75,  # Engine Stress
    0.20,  # Cooling Requirement

    0.55,  # Aerodynamics Importance
    0.45,  # Downforce Importance

    0.90,  # Energy Recovery Potential

    0.35,  # Overtaking Difficulty

    0.01,  # Rain Probability

    0.20,  # Pit Stop Time

    0.75,  # Qualifying Importance

    0.60   # Safety Car Probability
)


qatar = Circuit(
    "Qatar",

    0.45,  # Low Speed Importance
    0.90,  # Medium Speed Importance
    0.95,  # High Speed Importance

    0.75,  # Top Speed Importance
    0.80,  # Acceleration Importance

    0.90,  # Tyre Degradation

    0.95,  # Engine Stress
    0.95,  # Cooling Requirement

    1.00,  # Aerodynamics Importance
    0.95,  # Downforce Importance

    0.75,  # Energy Recovery Potential

    0.70,  # Overtaking Difficulty

    0.02,  # Rain Probability

    0.22,  # Pit Stop Time

    0.85,  # Qualifying Importance

    0.35   # Safety Car Probability
)


abu_dhabi = Circuit(
    "Abu Dhabi",

    0.65,  # Low Speed Importance
    0.75,  # Medium Speed Importance
    0.70,  # High Speed Importance

    0.80,  # Top Speed Importance
    0.85,  # Acceleration Importance

    0.60,  # Tyre Degradation

    0.70,  # Engine Stress
    0.85,  # Cooling Requirement

    0.80,  # Aerodynamics Importance
    0.75,  # Downforce Importance

    0.80,  # Energy Recovery Potential

    0.50,  # Overtaking Difficulty

    0.01,  # Rain Probability

    0.21,  # Pit Stop Time

    0.75,  # Qualifying Importance

    0.30   # Safety Car Probability
)
