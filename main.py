from src.data.drivers_data import verstappen, norris, leclerc
from src.data.cars_data import rb26, mcl40, sf26
from src.data.circuits_data import circuits

from src.simulation.race import simulate_race
from src.models.entry import Entry

entries = [
    Entry(verstappen, rb26),
    Entry(norris, mcl40),
    Entry(leclerc, sf26)
]

for circuit in circuits:

    wins = {
        "Verstappen": 0,
        "Norris": 0,
        "Leclerc": 0
    }

    for _ in range(10000):

        results = simulate_race(entries, circuit)

        winner = results[0][0].name

        wins[winner] += 1

    print(f"\n=== {circuit.name.upper()} ===\n")

    for driver, victories in wins.items():

        percentage = victories / 10000 * 100

        print(
            f"{driver}: "
            f"{victories} wins "
            f"({percentage:.2f}%)"
        )