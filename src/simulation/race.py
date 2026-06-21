import random


def calculate_driver_performance(driver):
    return (
        driver.experience +
        driver.qualifying_pace +
        driver.race_pace +
        driver.wet_skill +
        driver.consistency +
        driver.overtaking +
        driver.defending +
        driver.cornering +
        driver.smoothness +
        driver.braking +
        driver.adaptability +
        driver.reaction_time +
        driver.control +
        driver.accuracy +
        driver.aggressiveness
    ) / 15


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
        circuit.aerodynamics_importance +
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
        car.downforce * circuit.aerodynamics_importance +
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


def simulate_race(entries, circuit):

    results = []

    for entry in entries:

        driver = entry.driver
        car = entry.car

        driver_performance = calculate_driver_performance(driver)

        car_performance = calculate_car_performance(
            car,
            circuit
        )

        score = (
            driver_performance * 0.6 +
            car_performance * 0.4 +
            random.uniform(-5, 5)
        )

        results.append((driver, score))

    results.sort(
        key=lambda result: result[1],
        reverse=True
    )

    return results