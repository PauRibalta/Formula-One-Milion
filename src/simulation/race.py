import random
from collections import namedtuple

RaceResult = namedtuple("RaceResult", ["driver", "score", "team"])


_RANDOM = random.Random()
_DRIVER_SCORE_CACHE = {}
_DRIVER_WEIGHT_KEYS = {}
_CAR_PERFORMANCE_CACHE = {}
_TEAM_PERFORMANCE_CACHE = {}

_PERFORMANCE_CENTER = 90.0
_PERFORMANCE_SPREAD = 0.70


def _compress_package_performance(score):
    return _PERFORMANCE_CENTER + (score - _PERFORMANCE_CENTER) * _PERFORMANCE_SPREAD


# ==========================
# DRIVER WEIGHTS
# ==========================

QUALIFYING_WEIGHTS = {
    "experience": 0.02,
    "qualifying_pace": 0.25,
    "race_pace": 0.02,
    "wet_skill": 0.00,
    "consistency": 0.08,
    "overtaking": 0.00,
    "defending": 0.00,
    "cornering": 0.15,
    "smoothness": 0.02,
    "braking": 0.10,
    "adaptability": 0.04,
    "reaction_time": 0.10,
    "control": 0.10,
    "accuracy": 0.10,
    "aggressiveness": 0.02,
}

RACE_WEIGHTS = {
    "experience": 0.05,
    "qualifying_pace": 0.03,
    "race_pace": 0.24,
    "wet_skill": 0.02,
    "consistency": 0.15,
    "overtaking": 0.08,
    "defending": 0.07,
    "cornering": 0.10,
    "smoothness": 0.08,
    "braking": 0.05,
    "adaptability": 0.05,
    "reaction_time": 0.02,
    "control": 0.04,
    "accuracy": 0.02,
    "aggressiveness": 0.00,
}

WET_WEIGHTS = {
    "experience": 0.10,
    "qualifying_pace": 0.02,
    "race_pace": 0.08,
    "wet_skill": 0.30,
    "consistency": 0.10,
    "overtaking": 0.05,
    "defending": 0.05,
    "cornering": 0.08,
    "smoothness": 0.06,
    "braking": 0.05,
    "adaptability": 0.04,
    "reaction_time": 0.03,
    "control": 0.02,
    "accuracy": 0.02,
    "aggressiveness": 0.00,
}


def calculate_driver_score(driver, weights):
    weight_key = _DRIVER_WEIGHT_KEYS.get(id(weights))
    if weight_key is None:
        weight_key = tuple(weights.items())
        _DRIVER_WEIGHT_KEYS[id(weights)] = weight_key

    key = (id(driver), weight_key)

    if key not in _DRIVER_SCORE_CACHE:
        raw_score = (
            driver.experience * weights["experience"] +
            driver.qualifying_pace * weights["qualifying_pace"] +
            driver.race_pace * weights["race_pace"] +
            driver.wet_skill * weights["wet_skill"] +
            driver.consistency * weights["consistency"] +
            driver.overtaking * weights["overtaking"] +
            driver.defending * weights["defending"] +
            driver.cornering * weights["cornering"] +
            driver.smoothness * weights["smoothness"] +
            driver.braking * weights["braking"] +
            driver.adaptability * weights["adaptability"] +
            driver.reaction_time * weights["reaction_time"] +
            driver.control * weights["control"] +
            driver.accuracy * weights["accuracy"] +
            driver.aggressiveness * weights["aggressiveness"]
        )
        historical_rating = getattr(driver, "historical_rating", None)
        if historical_rating is not None:
            raw_score = raw_score * 0.65 + historical_rating * 0.35
        _DRIVER_SCORE_CACHE[key] = raw_score

    return _DRIVER_SCORE_CACHE[key]


def calculate_driver_qualifying(driver):
    return calculate_driver_score(driver, QUALIFYING_WEIGHTS)


def calculate_driver_race(driver):
    return calculate_driver_score(driver, RACE_WEIGHTS)


def calculate_driver_wet(driver):
    return calculate_driver_score(driver, WET_WEIGHTS)


def calculate_base_car_performance(car):

    raw_score = (
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

    historical_rating = getattr(car, "historical_rating", None)
    if historical_rating is not None:
        return raw_score * 0.25 + historical_rating * 0.75

    return raw_score


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
    key = (id(car), id(circuit))

    if key not in _CAR_PERFORMANCE_CACHE:
        score = (
            calculate_base_car_performance(car) * 0.70 +
            calculate_circuit_bonus(car, circuit) * 0.30
        )
        _CAR_PERFORMANCE_CACHE[key] = _compress_package_performance(score)

    return _CAR_PERFORMANCE_CACHE[key]


def calculate_team_performance(team):
    key = (id(team), getattr(team, "development_progress", 0.0))

    if key not in _TEAM_PERFORMANCE_CACHE:
        development_bonus = getattr(team, "development_progress", 0.0)
        team_score = (
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
        historical_rating = getattr(team, "historical_rating", None)
        if historical_rating is not None:
            team_score = team_score * 0.85 + historical_rating * 0.15
        _TEAM_PERFORMANCE_CACHE[key] = (
            _compress_package_performance(team_score) + development_bonus
        )

    return _TEAM_PERFORMANCE_CACHE[key]


def generate_weather(circuit):
    return "wet" if _RANDOM.random() < circuit.rain_probability else "dry"


def calculate_driver_error_risk(driver, circuit, weather):
    risk = 0.12
    risk += max(0.0, (100 - driver.consistency) / 100.0) * 0.10
    risk += max(0.0, (100 - driver.control) / 100.0) * 0.08
    risk += max(0.0, (100 - driver.accuracy) / 100.0) * 0.08

    if weather == "wet":
        risk += max(0.0, (100 - driver.wet_skill) / 100.0) * 0.10

    risk += circuit.overtaking_difficulty * 0.06
    return min(risk, 0.55)


def apply_driver_errors(entries, circuit, weather):
    penalties = {}

    for entry in entries:
        driver = entry.driver
        risk = calculate_driver_error_risk(driver, circuit, weather)

        if _RANDOM.random() < risk:
            penalties[driver.name] = {
                "time_loss": _RANDOM.uniform(0.5, 2.5),
                "type": _RANDOM.choice([
                    "lock-up",
                    "momentum loss",
                    "braking mistake",
                    "track position error"
                ]),
                "weather": weather,
            }

    if not penalties and entries:
        weakest = min(
            entries,
            key=lambda e: (
                e.driver.consistency + e.driver.control + e.driver.accuracy
            )
        )
        penalties[weakest.driver.name] = {
            "time_loss": 0.8,
            "type": "minor mistake",
            "weather": weather,
        }

    return penalties


def generate_safety_car_state(circuit, incident_level=0.0):
    total_probability = min(0.85, circuit.safety_car_probability + incident_level)
    roll = _RANDOM.random()

    if roll < total_probability * 0.25:
        mode = "safety_car"
        degradation_factor = 0.60 + _RANDOM.random() * 0.10
    elif roll < total_probability * 0.60:
        mode = "virtual_safety_car"
        degradation_factor = 0.78 + _RANDOM.random() * 0.10
    else:
        mode = "none"
        degradation_factor = 1.0

    return {
        "mode": mode,
        "degradation_factor": degradation_factor,
    }


def calculate_retirement_probability(driver, car, team, weather, incident_level):
    chance = 0.02
    chance += max(0.0, (100 - car.reliability) / 100.0) * 0.10
    chance += max(0.0, (100 - team.reliability_management) / 100.0) * 0.06
    chance += max(0.0, (100 - driver.control) / 100.0) * 0.04
    chance += max(0.0, (100 - driver.accuracy) / 100.0) * 0.04

    if weather == "wet":
        chance += 0.02

    chance += incident_level * 0.05
    return min(chance, 0.28)


def apply_retirements(entries, circuit, weather, incident_level=0.0):
    retirements = {}

    for entry in entries:
        driver = entry.driver
        car = entry.car
        team = entry.team

        failure_chance = calculate_retirement_probability(
            driver,
            car,
            team,
            weather,
            incident_level,
        )

        if _RANDOM.random() < failure_chance:
            retirements[driver.name] = {
                "reason": _RANDOM.choice([
                    "mechanical",
                    "driver mistake",
                    "contact",
                    "reliability issue"
                ]),
                "weather": weather,
            }

    return retirements


def _get_form_value(forms, driver):
    if isinstance(forms, dict):
        return forms.get(driver.name, 0.0)
    return forms[driver.simulation_index]


def _build_race_context(weather, safety_car_state, include_context, driver_errors=None, retirements=None):
    if include_context:
        return {
            "weather": weather,
            "safety_car_state": safety_car_state,
            "driver_errors": driver_errors or {},
            "retirements": retirements or {},
        }

    return {
        "weather": weather,
        "safety_car_state": safety_car_state,
        "driver_errors": {},
        "retirements": {},
    }


def calculate_race_base_score(entry, circuit, weather=None):
    return entry.race_base_score(circuit, weather)


def precompute_entries_scores(entries, circuit, weather=None):
    for entry in entries:
        entry.qualifying_base_score(circuit)
        entry.race_base_score(circuit, weather)


def calculate_grid_bonus(position):

    """
    Avantatge segons la posició de sortida.

    Pole = +0.75
    Últim = -0.75
    """

    return 0.75 - ((position - 1) * (3 / 21))


def simulate_race(entries, circuit, forms, weather=None, incident_level=0.0, include_context=True):

    if weather is None:
        weather = generate_weather(circuit)

    precompute_entries_scores(entries, circuit, weather)

    safety_car_state = generate_safety_car_state(
        circuit,
        incident_level=incident_level
    )

    if include_context:
        driver_errors = apply_driver_errors(
            entries,
            circuit,
            weather
        )
        retirements = apply_retirements(
            entries,
            circuit,
            weather,
            incident_level=incident_level
        )
        retired_names = set(retirements)
        error_penalties = {
            driver_name: details.get("time_loss", 0.0)
            for driver_name, details in driver_errors.items()
        }
    else:
        driver_errors = {}
        retirements = {}
        retired_names = set()
        error_penalties = {}

        for entry in entries:
            driver = entry.driver
            risk = calculate_driver_error_risk(driver, circuit, weather)
            error_penalties[driver.name] = (
                _RANDOM.uniform(0.5, 2.5) if _RANDOM.random() < risk else 0.0
            )

            failure_chance = calculate_retirement_probability(
                driver,
                entry.car,
                entry.team,
                weather,
                incident_level,
            )
            if _RANDOM.random() < failure_chance:
                retired_names.add(driver.name)

    expected_results = []
    race_results = []

    for position, entry in enumerate(entries, start=1):

        driver = entry.driver
        team = entry.team

        base_score = calculate_race_base_score(
            entry,
            circuit,
            weather=weather
        )

        expected_results.append(RaceResult(driver, base_score, team))

        error_penalty = error_penalties.get(driver.name, 0.0)
        retired = driver.name in retired_names

        if retired:
            final_score = -9999.0
        else:
            final_score = (
                base_score +
                _get_form_value(forms, driver) +
                calculate_grid_bonus(position) +
                _RANDOM.uniform(-3, 3) -
                error_penalty * 0.8
            )

        if safety_car_state["mode"] != "none":
            final_score *= safety_car_state["degradation_factor"]

        race_results.append(RaceResult(driver, final_score, team))

    expected_results.sort(key=lambda item: item.score, reverse=True)

    race_results = [
        result for result in race_results
        if result.driver.name not in retired_names
    ]
    race_results.sort(key=lambda item: item.score, reverse=True)

    race_context = _build_race_context(
        weather,
        safety_car_state,
        include_context,
        driver_errors,
        retirements,
    )

    return expected_results, race_results, race_context
