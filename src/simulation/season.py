from src.models.championship import Championship
from src.models.driver_season import DriverSeason
from src.models.team_season import TeamSeason

from src.simulation.race import simulate_race


POINTS_SYSTEM = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]


def create_championship(entries, calendar):

    championship = Championship(calendar)

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

    driver_lookup = {
        ds.driver.name: ds
        for ds in championship.driver_seasons
    }

    team_lookup = {
        ts.team.name: ts
        for ts in championship.team_seasons
    }

    for position, (driver, _, team) in enumerate(results, start=1):

        driver_season = driver_lookup[driver.name]

        driver_season.races += 1

        if position == 1:
            driver_season.wins += 1

        if position <= 3:
            driver_season.podiums += 1

        if position <= 10:

            points = POINTS_SYSTEM[position - 1]

            driver_season.points += points

            team_lookup[team.name].points += points


def update_driver_form(expected_results, race_results, championship):

    driver_lookup = {
        ds.driver.name: ds
        for ds in championship.driver_seasons
    }

    expected_position = {
        driver.name: pos
        for pos, (driver, _, _) in enumerate(expected_results, start=1)
    }

    actual_position = {
        driver.name: pos
        for pos, (driver, _, _) in enumerate(race_results, start=1)
    }

    for driver_name, driver_season in driver_lookup.items():

        delta = expected_position[driver_name] - actual_position[driver_name]

        # La forma es va perdent gradualment
        driver_season.form *= 0.90

        # Millor resultat del previst -> puja la forma
        driver_season.form += delta * 0.05

        # Límit de la forma
        driver_season.form = max(-2.0, min(2.0, driver_season.form))


def simulate_championship(entries, calendar):

    championship = create_championship(
        entries,
        calendar
    )

    for circuit in championship.calendar:

        championship.current_round += 1

        forms = {
            ds.driver.name: ds.form
            for ds in championship.driver_seasons
        }

        expected_results, race_results = simulate_race(
            entries,
            circuit,
            forms
        )

        assign_points(
            race_results,
            championship
        )

        update_driver_form(
            expected_results,
            race_results,
            championship
        )

    championship.driver_seasons.sort(
        key=lambda ds: ds.points,
        reverse=True
    )

    championship.team_seasons.sort(
        key=lambda ts: ts.points,
        reverse=True
    )

    return championship