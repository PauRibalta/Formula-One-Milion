from dataclasses import dataclass

from src.models.driver import Driver


@dataclass
class DriverSeason:
    driver: Driver

    points: int = 0

    wins: int = 0
    podiums: int = 0
    poles: int = 0
    fastest_laps: int = 0

    races: int = 0

    form: float = 0.0