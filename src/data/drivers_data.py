from src.models.driver import Driver
from src.data.standings_data import (
    apply_historical_ratings,
    driver_historical_rating,
)

verstappen = Driver(
    "Verstappen",
    92,  # Experience
    95,  # Qualifying Pace
    95,  # Race Pace
    92,  # Wet Skill
    96,  # Consistency
    96,  # Overtaking
    96,  # Defending
    96,  # Cornering
    90,  # Smoothness
    96,  # Braking
    96,  # Adaptability
    96,  # Reaction Time
    96,  # Control
    97,  # Accuracy
    90   # Aggressiveness
)
# Overall ≈ 95


norris = Driver(
    "Norris",
    92,  # Experience
    94,  # Qualifying Pace
    95,  # Race Pace
    91,  # Wet Skill
    94,  # Consistency
    93,  # Overtaking
    92,  # Defending
    92,  # Cornering
    93,  # Smoothness
    93,  # Braking
    94,  # Adaptability
    93,  # Reaction Time
    93,  # Control
    92,  # Accuracy
    89   # Aggressiveness
)
# Overall ≈ 93


leclerc = Driver(
    "Leclerc",
    91,  # Experience
    94,  # Qualifying Pace
    90,  # Race Pace
    88,  # Wet Skill
    87,  # Consistency
    90,  # Overtaking
    89,  # Defending
    91,  # Cornering
    91,  # Smoothness
    91,  # Braking
    91,  # Adaptability
    91,  # Reaction Time
    91,  # Control
    91,  # Accuracy
    90   # Aggressiveness
)
# Overall ≈ 92


piastri = Driver(
    "Piastri",
    88,  # Experience
    92,  # Qualifying Pace
    92,  # Race Pace
    89,  # Wet Skill
    95,  # Consistency
    91,  # Overtaking
    92,  # Defending
    93,  # Cornering
    93,  # Smoothness
    93,  # Braking
    93,  # Adaptability
    91,  # Reaction Time
    93,  # Control
    93,  # Accuracy
    86   # Aggressiveness
)
# Overall ≈ 92


russell = Driver(
    "Russell",
    92,  # Experience
    93,  # Qualifying Pace
    91,  # Race Pace
    91,  # Wet Skill
    92,  # Consistency
    90,  # Overtaking
    92,  # Defending
    91,  # Cornering
    92,  # Smoothness
    91,  # Braking
    92,  # Adaptability
    90,  # Reaction Time
    91,  # Control
    91,  # Accuracy
    90   # Aggressiveness
)
# Overall ≈ 91


hamilton = Driver(
    "Hamilton",
    99,  # Experience
    94,  # Qualifying Pace
    93,  # Race Pace
    95,  # Wet Skill
    96,  # Consistency
    95,  # Overtaking
    95,  # Defending
    94,  # Cornering
    95,  # Smoothness
    93,  # Braking
    96,  # Adaptability
    92,  # Reaction Time
    95,  # Control
    96,  # Accuracy
    90   # Aggressiveness
)
# Overall ≈ 90


alonso = Driver(
    "Alonso",
    99,  # Experience
    84,  # Qualifying Pace
    86,  # Race Pace
    90,  # Wet Skill
    88,  # Consistency
    87,  # Overtaking
    89,  # Defending
    88,  # Cornering
    88,  # Smoothness
    87,  # Braking
    89,  # Adaptability
    82,  # Reaction Time
    87,  # Control
    87,  # Accuracy
    80   # Aggressiveness
)
# Overall ≈ 89

sainz = Driver(
    "Sainz",
    91,  # Experience
    86,  # Qualifying Pace
    87,  # Race Pace
    87,  # Wet Skill
    87,  # Consistency
    86,  # Overtaking
    88,  # Defending
    87,  # Cornering
    90,  # Smoothness
    87,  # Braking
    89,  # Adaptability
    85,  # Reaction Time
    87,  # Control
    87,  # Accuracy
    84   # Aggressiveness
)
# Overall ≈ 87


antonelli = Driver(
    "Antonelli",
    80,  # Experience
    90,  # Qualifying Pace
    90,  # Race Pace
    88,  # Wet Skill
    88,  # Consistency
    90,  # Overtaking
    90,  # Defending
    88,  # Cornering
    87,  # Smoothness
    88,  # Braking
    88,  # Adaptability
    90,  # Reaction Time
    88,  # Control
    89,  # Accuracy
    89   # Aggressiveness
)
# Overall ≈ 86


albon = Driver(
    "Albon",
    90,  # Experience
    87,  # Qualifying Pace
    87,  # Race Pace
    87,  # Wet Skill
    88,  # Consistency
    87,  # Overtaking
    88,  # Defending
    87,  # Cornering
    90,  # Smoothness
    88,  # Braking
    89,  # Adaptability
    87,  # Reaction Time
    88,  # Control
    88,  # Accuracy
    86   # Aggressiveness
)
# Overall ≈ 86


gasly = Driver(
    "Gasly",
    88,  # Experience
    84,  # Qualifying Pace
    87,  # Race Pace
    86,  # Wet Skill
    86,  # Consistency
    87,  # Overtaking
    86,  # Defending
    86,  # Cornering
    87,  # Smoothness
    86,  # Braking
    86,  # Adaptability
    87,  # Reaction Time
    85,  # Control
    85,  # Accuracy
    84   # Aggressiveness
)
# Overall ≈ 85


ocon = Driver(
    "Ocon",
    90,  # Experience
    86,  # Qualifying Pace
    87,  # Race Pace
    85,  # Wet Skill
    88,  # Consistency
    84,  # Overtaking
    85,  # Defending
    86,  # Cornering
    84,  # Smoothness
    85,  # Braking
    86,  # Adaptability
    83,  # Reaction Time
    87,  # Control
    87,  # Accuracy
    86   # Aggressiveness
)
# Overall ≈ 84


hulkenberg = Driver(
    "Hulkenberg",
    95,  # Experience
    82,  # Qualifying Pace
    85,  # Race Pace
    85,  # Wet Skill
    85,  # Consistency
    84,  # Overtaking
    88,  # Defending
    85,  # Cornering
    88,  # Smoothness
    85,  # Braking
    87,  # Adaptability
    82,  # Reaction Time
    84,  # Control
    85,  # Accuracy
    81   # Aggressiveness
)
# Overall ≈ 85

lawson = Driver(
    "Lawson",
    84,  # Experience
    86,  # Qualifying Pace
    85,  # Race Pace
    83,  # Wet Skill
    83,  # Consistency
    85,  # Overtaking
    85,  # Defending
    85,  # Cornering
    84,  # Smoothness
    84,  # Braking
    85,  # Adaptability
    87,  # Reaction Time
    85,  # Control
    86,  # Accuracy
    90   # Aggressiveness
)
# Overall ≈ 84


hadjar = Driver(
    "Hadjar",
    80,  # Experience
    88,  # Qualifying Pace
    88,  # Race Pace
    86,  # Wet Skill
    86,  # Consistency
    88,  # Overtaking
    85,  # Defending
    88,  # Cornering
    86,  # Smoothness
    86,  # Braking
    88,  # Adaptability
    88,  # Reaction Time
    87,  # Control
    87,  # Accuracy
    92   # Aggressiveness
)
# Overall ≈ 84


bearman = Driver(
    "Bearman",
    80,  # Experience
    88,  # Qualifying Pace
    87,  # Race Pace
    83,  # Wet Skill
    83,  # Consistency
    85,  # Overtaking
    83,  # Defending
    87,  # Cornering
    84,  # Smoothness
    85,  # Braking
    83,  # Adaptability
    88,  # Reaction Time
    87,  # Control
    86,  # Accuracy
    91   # Aggressiveness
)
# Overall ≈ 83


perez = Driver(
    "Perez",
    94,  # Experience
    77,  # Qualifying Pace
    80,  # Race Pace
    86,  # Wet Skill
    82,  # Consistency
    81,  # Overtaking
    85,  # Defending
    81,  # Cornering
    88,  # Smoothness
    82,  # Braking
    88,  # Adaptability
    79,  # Reaction Time
    84,  # Control
    87,  # Accuracy
    80   # Aggressiveness
)
# Overall ≈ 82


bottas = Driver(
    "Bottas",
    95,  # Experience
    81,  # Qualifying Pace
    80,  # Race Pace
    81,  # Wet Skill
    82,  # Consistency
    79,  # Overtaking
    82,  # Defending
    81,  # Cornering
    84,  # Smoothness
    82,  # Braking
    83,  # Adaptability
    78,  # Reaction Time
    82,  # Control
    82,  # Accuracy
    79   # Aggressiveness
)
# Overall ≈ 81


colapinto = Driver(
    "Colapinto",
    77,  # Experience
    81,  # Qualifying Pace
    81,  # Race Pace
    80,  # Wet Skill
    78,  # Consistency
    81,  # Overtaking
    79,  # Defending
    81,  # Cornering
    80,  # Smoothness
    80,  # Braking
    80,  # Adaptability
    84,  # Reaction Time
    81,  # Control
    80,  # Accuracy
    85   # Aggressiveness
)
# Overall ≈ 80


bortoleto = Driver(
    "Bortoleto",
    76,  # Experience
    80,  # Qualifying Pace
    82,  # Race Pace
    81,  # Wet Skill
    80,  # Consistency
    81,  # Overtaking
    79,  # Defending
    82,  # Cornering
    83,  # Smoothness
    82,  # Braking
    82,  # Adaptability
    85,  # Reaction Time
    82,  # Control
    83,  # Accuracy
    83   # Aggressiveness
)
# Overall ≈ 81


stroll = Driver(
    "Stroll",
    84,  # Experience
    77,  # Qualifying Pace
    79,  # Race Pace
    80,  # Wet Skill
    78,  # Consistency
    79,  # Overtaking
    77,  # Defending
    78,  # Cornering
    80,  # Smoothness
    80,  # Braking
    78,  # Adaptability
    80,  # Reaction Time
    80,  # Control
    80,  # Accuracy
    85   # Aggressiveness
)
# Overall ≈ 80


lindblad = Driver(
    "Lindblad",
    72,  # Experience
    79,  # Qualifying Pace
    79,  # Race Pace
    78,  # Wet Skill
    75,  # Consistency
    81,  # Overtaking
    76,  # Defending
    80,  # Cornering
    78,  # Smoothness
    80,  # Braking
    82,  # Adaptability
    89,  # Reaction Time
    79,  # Control
    78,  # Accuracy
    93   # Aggressiveness
)
# Overall ≈ 77


apply_historical_ratings(globals(), driver_historical_rating)

