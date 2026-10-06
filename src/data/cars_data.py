from src.models.car import Car
from src.data.standings_data import apply_car_historical_ratings

# TOP TEAMS

# MERCEDES (~96)
w17 = Car(
    "W17",
    97,   # Top Speed
    96,   # Acceleration
    97,   # Low Speed Corners
    97,   # Medium Speed Corners
    98,   # High Speed Corners
    97,   # Dirty Air Tolerance
    96,   # Tyre Management
    97,   # Engine Power
    97,   # Engine Cooling
    98,   # Aerodynamics
    98,   # Downforce
    96,   # Fuel Efficiency
    96,   # Reliability
    95,   # Energy Recovery
    96,   # Battery Capacity
    96,   # Energy Deployment
    95,   # Hybrid Reliability
    96    # Energy Strategy
)

# FERRARI (~96)
sf26 = Car(
    "SF-26",
    98,   # Top Speed
    97,   # Acceleration
    95,   # Low Speed Corners
    95,   # Medium Speed Corners
    96,   # High Speed Corners
    95,   # Dirty Air Tolerance
    95,   # Tyre Management
    98,   # Engine Power
    95,   # Engine Cooling
    95,   # Aerodynamics
    95,   # Downforce
    96,   # Fuel Efficiency
    95,   # Reliability
    95,   # Energy Recovery
    95,   # Battery Capacity
    96,   # Energy Deployment
    95,   # Hybrid Reliability
    96    # Energy Strategy
)

# McLAREN (~96)
mcl40 = Car(
    "MCL40",
    96,   # Top Speed
    97,   # Acceleration
    97,   # Low Speed Corners
    97,   # Medium Speed Corners
    96,   # High Speed Corners
    97,   # Dirty Air Tolerance
    98,   # Tyre Management
    96,   # Engine Power
    96,   # Engine Cooling
    97,   # Aerodynamics
    96,   # Downforce
    97,   # Fuel Efficiency
    96,   # Reliability
    97,   # Energy Recovery
    96,   # Battery Capacity
    96,   # Energy Deployment
    95,   # Hybrid Reliability
    95    # Energy Strategy
)

# RED BULL (~94.5)
rb26 = Car(
    "RB26",
    95,   # Top Speed
    96,   # Acceleration
    95,   # Low Speed Corners
    96,   # Medium Speed Corners
    98,   # High Speed Corners
    95,   # Dirty Air Tolerance
    93,   # Tyre Management
    94,   # Engine Power
    93,   # Engine Cooling
    98,   # Aerodynamics
    97,   # Downforce
    93,   # Fuel Efficiency
    92,   # Reliability
    94,   # Energy Recovery
    93,   # Battery Capacity
    94,   # Energy Deployment
    92,   # Hybrid Reliability
    93    # Energy Strategy
)


# MIDFIELD

# RACING BULLS (~89.5)
vcarb02 = Car(
    "VCARB 02",
    89,   # Top Speed
    90,   # Acceleration
    90,   # Low Speed Corners
    90,   # Medium Speed Corners
    89,   # High Speed Corners
    90,   # Dirty Air Tolerance
    89,   # Tyre Management
    89,   # Engine Power
    90,   # Engine Cooling
    90,   # Aerodynamics
    90,   # Downforce
    89,   # Fuel Efficiency
    89,   # Reliability
    89,   # Energy Recovery
    89,   # Battery Capacity
    89,   # Energy Deployment
    89,   # Hybrid Reliability
    89    # Energy Strategy
)

# ALPINE (~89.5)
a526 = Car(
    "A526",
    91,   # Top Speed
    90,   # Acceleration
    89,   # Low Speed Corners
    90,   # Medium Speed Corners
    91,   # High Speed Corners
    89,   # Dirty Air Tolerance
    90,   # Tyre Management
    90,   # Engine Power
    88,   # Engine Cooling
    89,   # Aerodynamics
    89,   # Downforce
    91,   # Fuel Efficiency
    89,   # Reliability
    88,   # Energy Recovery
    89,   # Battery Capacity
    90,   # Energy Deployment
    89,   # Hybrid Reliability
    89    # Energy Strategy
)


# LOWER MIDFIELD

# HAAS (~88)
vf26 = Car(
    "VF-26",
    89,   # Top Speed
    88,   # Acceleration
    87,   # Low Speed Corners
    87,   # Medium Speed Corners
    87,   # High Speed Corners
    87,   # Dirty Air Tolerance
    87,   # Tyre Management
    89,   # Engine Power
    87,   # Engine Cooling
    87,   # Aerodynamics
    87,   # Downforce
    88,   # Fuel Efficiency
    88,   # Reliability
    87,   # Energy Recovery
    87,   # Battery Capacity
    87,   # Energy Deployment
    88,   # Hybrid Reliability
    87    # Energy Strategy
)

# WILLIAMS (~87.5)
fw48 = Car(
    "FW48",
    89,   # Top Speed
    88,   # Acceleration
    87,   # Low Speed Corners
    87,   # Medium Speed Corners
    87,   # High Speed Corners
    87,   # Dirty Air Tolerance
    87,   # Tyre Management
    89,   # Engine Power
    87,   # Engine Cooling
    87,   # Aerodynamics
    87,   # Downforce
    88,   # Fuel Efficiency
    87,   # Reliability
    87,   # Energy Recovery
    87,   # Battery Capacity
    87,   # Energy Deployment
    87,   # Hybrid Reliability
    87    # Energy Strategy
)

# AUDI (~86.5)
r26 = Car(
    "R26",
    87,   # Top Speed
    87,   # Acceleration
    86,   # Low Speed Corners
    86,   # Medium Speed Corners
    86,   # High Speed Corners
    86,   # Dirty Air Tolerance
    86,   # Tyre Management
    88,   # Engine Power
    86,   # Engine Cooling
    86,   # Aerodynamics
    86,   # Downforce
    87,   # Fuel Efficiency
    86,   # Reliability
    86,   # Energy Recovery
    86,   # Battery Capacity
    86,   # Energy Deployment
    86,   # Hybrid Reliability
    86    # Energy Strategy
)


# BACKMARKERS

# CADILLAC (~84.5)
c01 = Car(
    "C01",
    85,   # Top Speed
    86,   # Acceleration
    84,   # Low Speed Corners
    84,   # Medium Speed Corners
    84,   # High Speed Corners
    84,   # Dirty Air Tolerance
    84,   # Tyre Management
    86,   # Engine Power
    84,   # Engine Cooling
    84,   # Aerodynamics
    84,   # Downforce
    84,   # Fuel Efficiency
    84,   # Reliability
    84,   # Energy Recovery
    84,   # Battery Capacity
    84,   # Energy Deployment
    84,   # Hybrid Reliability
    84    # Energy Strategy
)

# ASTON MARTIN (~83)
amr26 = Car(
    "AMR26",
    80,   # Top Speed
    81,   # Acceleration
    79,   # Low Speed Corners
    80,   # Medium Speed Corners
    79,   # High Speed Corners
    80,   # Dirty Air Tolerance
    81,   # Tyre Management
    82,   # Engine Power
    80,   # Engine Cooling
    80,   # Aerodynamics
    80,   # Downforce
    80,   # Fuel Efficiency
    80,   # Reliability
    80,   # Energy Recovery
    80,   # Battery Capacity
    80,   # Energy Deployment
    80,   # Hybrid Reliability
    80    # Energy Strategy
)


apply_car_historical_ratings(
    globals(),
    {
        "w17": "Mercedes",
        "sf26": "Ferrari",
        "mcl40": "McLaren",
        "rb26": "Red Bull",
        "vcarb02": "Racing Bulls",
        "a526": "Alpine",
        "vf26": "Haas",
        "fw48": "Williams",
        "r26": "Audi",
        "c01": "Cadillac",
        "amr26": "Aston Martin",
    },
)

