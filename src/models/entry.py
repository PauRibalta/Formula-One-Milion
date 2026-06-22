from dataclasses import dataclass

from src.models.driver import Driver
from src.models.car import Car
from src.models.team import Team


@dataclass
class Entry:
    driver: Driver
    car: Car
    team: Team