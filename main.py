from src.data.drivers_data import verstappen, norris, leclerc
from src.data.cars_data import rb26, mcl40, sf26

from src.simulation.race import simulate_race

entries = [
    (verstappen, rb26),
    (norris, mcl40),
    (leclerc, sf26)
]

wins = {
    "Verstappen": 0,
    "Norris": 0,
    "Leclerc": 0
}

for _ in range(10000):
    results = simulate_race(entries)

    winner = results[0][0].name

    wins[winner] += 1

print("\n=== WIN DISTRIBUTION AFTER 10000 RACES ===\n")

for driver, victories in wins.items():
    percentage = victories / 10000 * 100
    print(f"{driver}: {victories} wins ({percentage:.2f}%)")