from dataclasses import dataclass

from src.models.driver import Driver
from src.models.car import Car


@dataclass
class Entry:
    driver: Driver
    car: Car