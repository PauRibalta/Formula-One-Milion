from dataclasses import dataclass, field

from src.models.driver import Driver
from src.models.car import Car
from src.models.team import Team


@dataclass
class Entry:
    driver: Driver
    car: Car
    team: Team

    base_performance_cache: dict = field(default_factory=dict, init=False, repr=False)

    def qualifying_base_score(self, circuit=None):
        cache_key = (
            "qualifying",
            getattr(circuit, "name", "default"),
            getattr(self.team, "development_progress", 0.0),
        )
        if cache_key not in self.base_performance_cache:
            from src.simulation.race import (
                calculate_driver_qualifying,
                calculate_car_performance,
                calculate_team_performance,
            )

            car_score = calculate_car_performance(self.car, circuit) if circuit is not None else 0
            driver_score = calculate_driver_qualifying(self.driver)
            team_score = calculate_team_performance(self.team)

            self.base_performance_cache[cache_key] = (
                driver_score * 0.45 +
                car_score * 0.45 +
                team_score * 0.10
            )

        return self.base_performance_cache[cache_key]

    def race_base_score(self, circuit=None, weather=None):
        cache_key = (
            "race",
            getattr(circuit, "name", "default"),
            weather or "dry",
            getattr(self.team, "development_progress", 0.0),
        )
        if cache_key not in self.base_performance_cache:
            from src.simulation.race import (
                calculate_driver_race,
                calculate_driver_wet,
                calculate_car_performance,
                calculate_team_performance,
            )

            driver_score = (
                calculate_driver_wet(self.driver)
                if weather == "wet"
                else calculate_driver_race(self.driver)
            )
            car_score = calculate_car_performance(self.car, circuit) if circuit is not None else 0
            team_score = calculate_team_performance(self.team)

            score = (
                driver_score * 0.40 +
                car_score * 0.50 +
                team_score * 0.10
            )

            if weather == "wet":
                score *= 0.95

            self.base_performance_cache[cache_key] = score

        return self.base_performance_cache[cache_key]

    def reset_performance_cache(self):
        self.base_performance_cache.clear()