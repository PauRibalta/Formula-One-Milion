import random

# ==========================
# DRIVER WEIGHTS
# ==========================

DRIVER_WEIGHTS = {
    "experience": 0.03,
    "qualifying_pace": 0.10,
    "race_pace": 0.20,
    "wet_skill": 0.04,
    "consistency": 0.13,
    "overtaking": 0.05,
    "defending": 0.04,
    "cornering": 0.10,
    "smoothness": 0.06,
    "braking": 0.05,
    "adaptability": 0.05,
    "reaction_time": 0.03,
    "control": 0.07,
    "accuracy": 0.03,
    "aggressiveness": 0.02,
}


def calculate_driver_performance(driver):

    return (
        driver.experience * DRIVER_WEIGHTS["experience"] +
        driver.qualifying_pace * DRIVER_WEIGHTS["qualifying_pace"] +
        driver.race_pace * DRIVER_WEIGHTS["race_pace"] +
        driver.wet_skill * DRIVER_WEIGHTS["wet_skill"] +
        driver.consistency * DRIVER_WEIGHTS["consistency"] +
        driver.overtaking * DRIVER_WEIGHTS["overtaking"] +
        driver.defending * DRIVER_WEIGHTS["defending"] +
        driver.cornering * DRIVER_WEIGHTS["cornering"] +
        driver.smoothness * DRIVER_WEIGHTS["smoothness"] +
        driver.braking * DRIVER_WEIGHTS["braking"] +
        driver.adaptability * DRIVER_WEIGHTS["adaptability"] +
        driver.reaction_time * DRIVER_WEIGHTS["reaction_time"] +
        driver.control * DRIVER_WEIGHTS["control"] +
        driver.accuracy * DRIVER_WEIGHTS["accuracy"] +
        driver.aggressiveness * DRIVER_WEIGHTS["aggressiveness"]
    )


def calculate_base_car_performance(car):

    return (
        car.top_speed +
        car.acceleration +
        car.low_speed_corners +
        car.medium_speed_corners +
        car.high_speed_corners +
        car.dirty_air_tolerance +
        car.tyre_management +
        car.engine_power +
        car.engine_cooling +
        car.aerodynamics +
        car.downforce +
        car.fuel_efficiency +
        car.reliability +
        car.energy_recovery +
        car.battery_capacity +
        car.energy_deployment +
        car.hybrid_reliability +
        car.energy_strategy
    ) / 18


def calculate_circuit_bonus(car, circuit):

    total_weight = (
        circuit.low_speed_importance +
        circuit.medium_speed_importance +
        circuit.high_speed_importance +
        circuit.top_speed_importance +
        circuit.acceleration_importance +
        circuit.aerodynamics_importance +
        circuit.downforce_importance +
        circuit.cooling_requirement +
        circuit.energy_recovery_potential
    )

    return (
        car.low_speed_corners * circuit.low_speed_importance +
        car.medium_speed_corners * circuit.medium_speed_importance +
        car.high_speed_corners * circuit.high_speed_importance +
        car.top_speed * circuit.top_speed_importance +
        car.acceleration * circuit.acceleration_importance +
        car.aerodynamics * circuit.aerodynamics_importance +
        car.downforce * circuit.downforce_importance +
        car.engine_cooling * circuit.cooling_requirement +
        car.energy_recovery * circuit.energy_recovery_potential
    ) / total_weight


def calculate_car_performance(car, circuit):

    base_performance = calculate_base_car_performance(car)

    circuit_bonus = calculate_circuit_bonus(car, circuit)

    return (
        base_performance * 0.7 +
        circuit_bonus * 0.3
    )


def calculate_team_performance(team):

    return (
        team.strategy +
        team.pit_stops +
        team.race_operations +
        team.development_rate +
        team.technical_staff +
        team.reliability_management +
        team.facilities +
        team.wind_tunnel +
        team.budget +
        team.winning_culture
    ) / 10


def simulate_race(entries, circuit):

    results = []

    for entry in entries:

        driver = entry.driver
        car = entry.car
        team = entry.team

        driver_performance = calculate_driver_performance(driver)
        car_performance = calculate_car_performance(car, circuit)
        team_performance = calculate_team_performance(team)

        score = (
            driver_performance * 0.40 +
            car_performance * 0.50 +
            team_performance * 0.10 +
            random.uniform(-5, 5)
        )

        results.append((driver, score))

    results.sort(
        key=lambda result: result[1],
        reverse=True
    )

    return results