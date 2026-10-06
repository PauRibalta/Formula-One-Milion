from src.models.team import Team
from src.data.standings_data import (
    apply_historical_ratings,
    team_historical_rating,
)

# MERCEDES (~98.0)
mercedes = Team(
    "Mercedes",
    98,  # Strategy
    98,  # Pit Stops
    98,  # Race Operations
    99,  # Development Rate
    98,  # Technical Staff
    98,  # Reliability Management
    98,  # Facilities
    98,  # Wind Tunnel
    97,  # Budget
    98   # Winning Culture
)

# McLAREN (~95.5)
mclaren = Team(
    "McLaren",
    96,  # Strategy
    96,  # Pit Stops
    95,  # Race Operations
    95,  # Development Rate
    95,  # Technical Staff
    95,  # Reliability Management
    95,  # Facilities
    96,  # Wind Tunnel
    96,  # Budget
    96   # Winning Culture
)

# RED BULL (~94.0)
red_bull = Team(
    "Red Bull",
    97,  # Strategy
    98,  # Pit Stops
    96,  # Race Operations
    93,  # Development Rate
    94,  # Technical Staff
    94,  # Reliability Management
    93,  # Facilities
    93,  # Wind Tunnel
    91,  # Budget
    91   # Winning Culture
)

# FERRARI (~96.5)
ferrari = Team(
    "Ferrari",
    92,  # Strategy
    95,  # Pit Stops
    94,  # Race Operations
    97,  # Development Rate
    97,  # Technical Staff
    96,  # Reliability Management
    99,  # Facilities
    99,  # Wind Tunnel
    99,  # Budget
    97   # Winning Culture
)

# ASTON MARTIN (~84.5)
aston_martin = Team(
    "Aston Martin",
    81,  # Strategy
    80,  # Pit Stops
    82,  # Race Operations
    81,  # Development Rate
    84,  # Technical Staff
    80,  # Reliability Management
    82,  # Facilities
    83,  # Wind Tunnel
    85,  # Budget
    80   # Winning Culture
)

# ALPINE (~92.5)
alpine = Team(
    "Alpine",
    93,  # Strategy
    92,  # Pit Stops
    92,  # Race Operations
    94,  # Development Rate
    93,  # Technical Staff
    94,  # Reliability Management
    93,  # Facilities
    93,  # Wind Tunnel
    93,  # Budget
    95   # Winning Culture
)

# RACING BULLS (~93.5)
racing_bulls = Team(
    "Racing Bulls",
    95,  # Strategy
    96,  # Pit Stops
    94,  # Race Operations
    94,  # Development Rate
    93,  # Technical Staff
    93,  # Reliability Management
    93,  # Facilities
    93,  # Wind Tunnel
    93,  # Budget
    91   # Winning Culture
)

# AUDI (~88.0)
audi = Team(
    "Audi",
    87,  # Strategy
    87,  # Pit Stops
    87,  # Race Operations
    89,  # Development Rate
    88,  # Technical Staff
    87,  # Reliability Management
    90,  # Facilities
    88,  # Wind Tunnel
    91,  # Budget
    86   # Winning Culture
)

# WILLIAMS (~91.5)
williams = Team(
    "Williams",
    92,  # Strategy
    92,  # Pit Stops
    92,  # Race Operations
    94,  # Development Rate
    92,  # Technical Staff
    91,  # Reliability Management
    93,  # Facilities
    92,  # Wind Tunnel
    89,  # Budget
    90   # Winning Culture
)

# HAAS (~89.0)
haas = Team(
    "Haas",
    90,  # Strategy
    91,  # Pit Stops
    90,  # Race Operations
    89,  # Development Rate
    88,  # Technical Staff
    89,  # Reliability Management
    89,  # Facilities
    88,  # Wind Tunnel
    90,  # Budget
    86   # Winning Culture
)

# CADILLAC (~82.0)
cadillac = Team(
    "Cadillac",
    81,  # Strategy
    82,  # Pit Stops
    81,  # Race Operations
    83,  # Development Rate
    82,  # Technical Staff
    81,  # Reliability Management
    82,  # Facilities
    80,  # Wind Tunnel
    82,  # Budget
    80   # Winning Culture
)


apply_historical_ratings(globals(), team_historical_rating)