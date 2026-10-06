from dataclasses import dataclass


@dataclass
class RaceWeekend:

    circuit: object

    qualifying: dict

    race_results: list

    weather: object | None = None

    fastest_lap: object | None = None

    safety_cars: int = 0

    virtual_safety_cars: int = 0

    red_flags: int = 0