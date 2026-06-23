from src.data.drivers_data import verstappen, norris, leclerc
from src.data.cars_data import rb26, mcl40, sf26
from src.data.teams_data import red_bull, mclaren, ferrari
from src.data.circuits_data import monza

from src.models.entry import Entry

from src.simulation.race import simulate_race

entries = [
    Entry(verstappen, rb26, red_bull),
    Entry(norris, mcl40, mclaren),
    Entry(leclerc, sf26, ferrari)
]

wins = {
    "Verstappen": 0,
    "Norris": 0,
    "Leclerc": 0
}

for _ in range(10000):

    results = simulate_race(entries, monza)

    winner = results[0][0].name

    wins[winner] += 1

print("\n=== WIN DISTRIBUTION AFTER 10000 RACES ===\n")

for driver, victories in wins.items():

    percentage = victories / 10000 * 100

    print(
        f"{driver}: "
        f"{victories} wins "
        f"({percentage:.2f}%)"
    )