from src.models.championship import Championship
from src.models.driver_season import DriverSeason
from src.models.team_season import TeamSeason
from src.models.race_weekend import RaceWeekend

from src.simulation.qualifying import simulate_qualifying
from src.simulation.race import precompute_entries_scores, simulate_race


POINTS_SYSTEM = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]


def reset_championship(championship, entries):
    championship.driver_seasons.sort(
        key=lambda driver_season: driver_season.driver.simulation_index
    )
    championship.team_seasons.sort(
        key=lambda team_season: team_season.team.simulation_index
    )

    for driver_season in championship.driver_seasons:
        driver_season.points = 0
        driver_season.wins = 0
        driver_season.podiums = 0
        driver_season.poles = 0
        driver_season.fastest_laps = 0
        driver_season.races = 0
        driver_season.form = 0.0

    for team_season in championship.team_seasons:
        team_season.points = 0
        team_season.wins = 0
        team_season.podiums = 0
        team_season.poles = 0
        team_season.fastest_laps = 0
        team_season.races = 0
        team_season.form = 0.0
        team_season.team.development_progress = 0.0

    for entry in entries:
        entry.reset_performance_cache()

    championship.race_weekends.clear()
    championship.current_round = 0
    return championship


def update_team_development(championship):
    for team_season in championship.team_seasons:
        team = team_season.team
        seasonal_progress = (championship.current_round / max(1, len(championship.calendar))) * 0.18
        team.development_progress = min(
            0.45,
            max(-0.20, seasonal_progress + (team.development_rate - 85) / 400.0)
        )


def create_championship(entries, calendar):

    championship = Championship(calendar)
    for index, entry in enumerate(entries):
        entry.driver.simulation_index = index

    team_indices = {}
    for entry in entries:
        team_name = entry.team.name
        if team_name not in team_indices:
            team_indices[team_name] = len(team_indices)
        entry.team.simulation_index = team_indices[team_name]

    championship.driver_seasons = [
        DriverSeason(entry.driver)
        for entry in entries
    ]

    added_teams = set()

    for entry in entries:

        if entry.team.name not in added_teams:

            championship.team_seasons.append(
                TeamSeason(entry.team)
            )

            added_teams.add(entry.team.name)

    return championship


def assign_points(results, championship):
    driver_seasons = championship.driver_seasons
    team_seasons = championship.team_seasons

    for position, result in enumerate(results, start=1):
        driver = result.driver
        team = result.team
        driver_season = driver_seasons[driver.simulation_index]

        driver_season.races += 1

        if position == 1:
            driver_season.wins += 1

        if position <= 3:
            driver_season.podiums += 1

        if position <= 10:
            points = POINTS_SYSTEM[position - 1]
            driver_season.points += points
            team_seasons[team.simulation_index].points += points


def update_driver_form(expected_results, race_results, championship):

    expected_position = [0] * len(championship.driver_seasons)
    actual_position = [len(race_results) + 1] * len(championship.driver_seasons)

    for position, result in enumerate(expected_results, start=1):
        expected_position[result.driver.simulation_index] = position

    for position, result in enumerate(race_results, start=1):
        actual_position[result.driver.simulation_index] = position

    for index, driver_season in enumerate(championship.driver_seasons):
        delta = expected_position[index] - actual_position[index]

        # La forma es va perdent gradualment
        driver_season.form *= 0.90

        # Millor resultat del previst -> puja la forma
        driver_season.form += delta * 0.05

        # Límit de la forma
        driver_season.form = max(-2.0, min(2.0, driver_season.form))


def simulate_championship(entries, calendar, championship=None, keep_details=True):

    if championship is None:
        championship = create_championship(entries, calendar)
    else:
        championship.calendar = calendar
        reset_championship(championship, entries)

    driver_seasons = championship.driver_seasons
    team_seasons = championship.team_seasons
    forms = [0.0] * len(driver_seasons)

    for circuit in championship.calendar:
        championship.current_round += 1

        for index, driver_season in enumerate(driver_seasons):
            forms[index] = driver_season.form

        precompute_entries_scores(entries, circuit)
        qualifying = simulate_qualifying(entries, circuit, forms)
        starting_grid = qualifying["starting_grid"]
        weather = None

        expected_results, race_results, race_context = simulate_race(
            starting_grid,
            circuit,
            forms,
            weather=weather,
            include_context=keep_details,
        )

        assign_points(race_results, championship)
        update_team_development(championship)
        update_driver_form(expected_results, race_results, championship)

        if keep_details:
            weekend = RaceWeekend(
                circuit=circuit,
                qualifying=qualifying,
                race_results=race_results,
                weather=race_context["weather"],
                safety_cars=1 if race_context["safety_car_state"]["mode"] == "safety_car" else 0,
                virtual_safety_cars=1 if race_context["safety_car_state"]["mode"] == "virtual_safety_car" else 0,
                red_flags=len(race_context["retirements"]),
            )
            championship.race_weekends.append(weekend)

    driver_seasons.sort(key=lambda ds: (-ds.points, ds.driver.simulation_index))
    team_seasons.sort(key=lambda ts: (-ts.points, ts.team.simulation_index))

    return championship