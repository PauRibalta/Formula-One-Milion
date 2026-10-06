from dataclasses import dataclass, field


@dataclass
class Team:
    name: str

    strategy: int
    pit_stops: int
    race_operations: int

    development_rate: int
    technical_staff: int

    reliability_management: int

    facilities: int
    wind_tunnel: int

    budget: int

    winning_culture: int
    development_progress: float = 0.0
    historical_rating: float | None = None
    simulation_index: int = field(default=-1, init=False, repr=False, compare=False)