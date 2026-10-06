from dataclasses import dataclass, field

from src.models.circuit import Circuit
from src.models.driver_season import DriverSeason
from src.models.team_season import TeamSeason


@dataclass
class Championship:
    calendar: list[Circuit]
    race_weekends: list = field(default_factory=list)

    driver_seasons: list[DriverSeason] = field(default_factory=list)
    team_seasons: list[TeamSeason] = field(default_factory=list)

    current_round: int = 0