from dataclasses import dataclass

@dataclass
class Circuit:
    name: str

    low_speed_importance: int
    medium_speed_importance: int
    high_speed_importance: int

    top_speed_importance: int
    acceleration_importance: int

    tyre_degradation: int

    engine_stress: int
    cooling_requirement: int

    aerodynamics_importance: int

    energy_recovery_potential: int

    overtaking_difficulty: int

    rain_probability: int

    pit_stop_time: float

    qualifying_importance: int
    safety_car_probability: int