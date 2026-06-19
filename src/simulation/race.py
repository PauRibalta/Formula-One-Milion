import random


def calculate_car_performance(car):
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


def simulate_race(entries):
    results = []

    for driver, car in entries:

        car_performance = calculate_car_performance(car)

        score = (
            driver.race_pace * 0.6 +
            car_performance * 0.4 +
            random.uniform(-5, 5)
        )

        results.append((driver, score))

    results.sort(key=lambda result: result[1], reverse=True)

    return results