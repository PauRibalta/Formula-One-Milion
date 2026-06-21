from dataclasses import dataclass

@dataclass
class Circuit:
    name: str

    low_speed_importance: float
    medium_speed_importance: float
    high_speed_importance: float

    top_speed_importance: float
    acceleration_importance: float

    tyre_degradation: float

    engine_stress: float
    cooling_requirement: float

    aerodynamics_importance: float

    energy_recovery_potential: float

    overtaking_difficulty: float

    rain_probability: float

    pit_stop_time: float

    qualifying_importance: float
    safety_car_probability: float