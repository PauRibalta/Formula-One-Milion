from src.models.driver import Driver
from src.simulation.race import simulate_race

drivers = [
    Driver("Verstappen", 98, 99, 100, 95, 97, 96, 94, 93, 92, 91, 95, 98, 97, 96, 98),
    Driver("Norris", 95, 96, 95, 90, 94, 92, 90, 89, 88, 90, 92, 93, 92, 91, 93),
    Driver("Leclerc", 94, 95, 94, 92, 93, 91, 89, 90, 91, 90, 91, 92, 91, 92, 91),
]

result = simulate_race(drivers)

for i, d in enumerate(result):
    print(f"{i+1}. {d.name}")