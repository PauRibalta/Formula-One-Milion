from dataclasses import dataclass

@dataclass
class Car:
    name: str

    top_speed: int
    acceleration: int

    low_speed_corners: int
    medium_speed_corners: int
    high_speed_corners: int

    dirty_air_tolerance: int
    tyre_management: int

    engine_power: int
    engine_cooling: int

    aerodynamics: int
    downforce: int

    fuel_efficiency: int
    reliability: int

    energy_recovery: int
    battery_capacity: int
    energy_deployment: int

    hybrid_reliability: int
    energy_strategy: int