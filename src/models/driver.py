from dataclasses import dataclass, field

@dataclass
class Driver:
    name: str

    experience: int
    qualifying_pace: int
    race_pace: int
    wet_skill: int
    consistency: int
    overtaking: int
    defending: int
    cornering: int
    smoothness: int
    braking: int
    adaptability: int
    reaction_time: int
    control: int
    accuracy: int
    aggressiveness: int
    historical_rating: float | None = None
    simulation_index: int = field(default=-1, init=False, repr=False, compare=False)