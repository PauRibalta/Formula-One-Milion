from src.models.circuit import Circuit

monza = Circuit(
    name="Monza",

    low_speed_importance=0.05,
    medium_speed_importance=0.15,
    high_speed_importance=0.25,

    top_speed_importance=0.35,
    acceleration_importance=0.20,

    tyre_degradation=0.30,

    engine_stress=0.80,
    cooling_requirement=0.40,

    aerodynamics_importance=0.20,

    energy_recovery_potential=0.60,

    overtaking_difficulty=0.20,

    rain_probability=0.10,

    pit_stop_time=24.0,

    qualifying_importance=0.40,
    safety_car_probability=0.15
)

monaco = Circuit(
    name="Monaco",

    low_speed_importance=0.45,
    medium_speed_importance=0.20,
    high_speed_importance=0.05,

    top_speed_importance=0.05,
    acceleration_importance=0.25,

    tyre_degradation=0.40,

    engine_stress=0.30,
    cooling_requirement=0.20,

    aerodynamics_importance=0.50,

    energy_recovery_potential=0.30,

    overtaking_difficulty=1.00,

    rain_probability=0.10,

    pit_stop_time=19.0,

    qualifying_importance=1.00,
    safety_car_probability=0.50
)

silverstone = Circuit(
    name="Silverstone",

    low_speed_importance=0.10,
    medium_speed_importance=0.25,
    high_speed_importance=0.35,

    top_speed_importance=0.10,
    acceleration_importance=0.20,

    tyre_degradation=0.60,

    engine_stress=0.50,
    cooling_requirement=0.50,

    aerodynamics_importance=0.40,

    energy_recovery_potential=0.50,

    overtaking_difficulty=0.50,

    rain_probability=0.30,

    pit_stop_time=22.0,

    qualifying_importance=0.70,
    safety_car_probability=0.25
)

circuits = [
    monza,
    monaco,
    silverstone
]