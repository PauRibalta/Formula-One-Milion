"""Historical championship results used to calibrate simulation ratings."""

SEASON_WEIGHTS = {
    2026: 1.0,
}

DRIVER_SEASON_WEIGHTS = {
    2026: 1.0,
}

CAR_SEASON_WEIGHTS = {
    2026: 1.0,
}

DRIVER_STANDINGS = {
    2026: {
        "Antonelli": 302, "Russell": 236, "Hamilton": 199,
        "Norris": 186, "Leclerc": 179, "Verstappen": 163,
        "Piastri": 120, "Hadjar": 86, "Lawson": 59, "Gasly": 41,
        "Lindblad": 37, "Colapinto": 27, "Bearman": 20,
        "Bortoleto": 10, "Hulkenberg": 7, "Ocon": 7, "Sainz": 7,
        "Albon": 5, "Alonso": 3, "Tsunoda": 1, "Stroll": 0,
        "Bottas": 0, "Perez": 0,
    },
    2025: {
        "Norris": 423, "Verstappen": 421, "Piastri": 410,
        "Russell": 319, "Leclerc": 242, "Hamilton": 156,
        "Antonelli": 150, "Albon": 73, "Sainz": 64,
        "Alonso": 56, "Hulkenberg": 51, "Hadjar": 51,
        "Bearman": 41, "Ocon": 38, "Lawson": 38, "Stroll": 33,
        "Tsunoda": 33, "Gasly": 22, "Bortoleto": 19,
        "Colapinto": 0, "Doohan": 0,
    },
    2024: {
        "Verstappen": 437, "Norris": 374, "Leclerc": 356,
        "Piastri": 292, "Sainz": 290, "Russell": 245,
        "Hamilton": 223, "Perez": 152, "Alonso": 70,
        "Gasly": 42, "Hulkenberg": 41, "Tsunoda": 30,
        "Stroll": 24, "Ocon": 23, "Magnussen": 16,
        "Albon": 12, "Ricciardo": 12, "Bearman": 7,
        "Colapinto": 5, "Zhou": 4, "Lawson": 4, "Bottas": 0,
        "Sargeant": 0, "Doohan": 0,
    },
}

TEAM_STANDINGS = {
    2026: {
        "Mercedes": 538, "Ferrari": 378, "McLaren": 306,
        "Red Bull": 263, "Racing Bulls": 83, "Alpine": 68,
        "Haas": 27, "Audi": 17, "Williams": 12,
        "Aston Martin": 3, "Cadillac": 0,
    },
    2025: {
        "McLaren": 833, "Mercedes": 469, "Red Bull": 451,
        "Ferrari": 398, "Williams": 137, "Racing Bulls": 92,
        "Aston Martin": 89, "Haas": 79, "Kick Sauber": 70,
        "Alpine": 22,
    },
    2024: {
        "McLaren": 666, "Ferrari": 652, "Red Bull": 589,
        "Mercedes": 468, "Aston Martin": 94, "Alpine": 65,
        "Haas": 58, "RB": 46, "Williams": 17,
        "Stake Sauber": 4,
    },
}


def _normalised_points(standings, name, missing_score=0.35):
    season_points = standings.get(name)
    if season_points is None:
        return missing_score

    maximum = max(standings.values())
    return season_points / maximum if maximum else missing_score


def weighted_rating(name, standings, minimum, maximum, season_weights):
    weighted_score = sum(
        season_weights[season] * _normalised_points(
            standings[season],
            name,
        )
        for season in season_weights
    )
    return round(minimum + (maximum - minimum) * weighted_score, 2)


def driver_historical_rating(name):
    return weighted_rating(
        name,
        DRIVER_STANDINGS,
        76.0,
        97.0,
        DRIVER_SEASON_WEIGHTS,
    )


def team_historical_rating(name):
    return weighted_rating(
        name,
        TEAM_STANDINGS,
        80.0,
        97.0,
        SEASON_WEIGHTS,
    )


def car_historical_rating(team_name):
    return weighted_rating(
        team_name,
        TEAM_STANDINGS,
        80.0,
        97.0,
        CAR_SEASON_WEIGHTS,
    )


def apply_historical_ratings(namespace, rating_function):
    for value in namespace.values():
        if value.__class__.__name__ in {"Driver", "Team"}:
            value.historical_rating = rating_function(value.name)


def apply_car_historical_ratings(namespace, car_team_names):
    for car_name, team_name in car_team_names.items():
        car = namespace[car_name]
        car.historical_rating = car_historical_rating(team_name)