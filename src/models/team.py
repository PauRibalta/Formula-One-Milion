from dataclasses import dataclass

@dataclass
class Team:
    name: str

    strategy: int
    pit_stops: int

    development_rate: int

    reliability_management: int

    facilities: int