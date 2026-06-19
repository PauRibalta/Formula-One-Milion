from src.models.driver import Driver
from src.models.car import Car
from src.simulation.race import simulate_race


Verstappen = Driver("Verstappen", 98, 99, 100, 95, 97, 96, 94, 93, 92, 91, 95, 98, 97, 96, 98)
Norris = Driver("Norris", 95, 96, 95, 90, 94, 92, 90, 89, 88, 90, 92, 93, 92, 91, 93)
Leclerc = Driver("Leclerc", 94, 95, 94, 92, 93, 91, 89, 90, 91, 90, 91, 92, 91, 92, 91)



RB26 = Car("RB26", 96, 97, 99, 98, 100, 95, 95, 95, 92, 100, 99, 92, 94, 95, 94, 96, 93, 95)
MCL40 = Car("MCL40", 97, 96, 96, 99, 98, 94, 97, 94, 94, 98, 97, 95, 96, 94, 95, 94, 96, 94)
SF26 = Car("SF-26", 100, 98, 95, 96, 95, 90, 92, 99, 91, 94, 94, 91, 93, 93, 94, 95, 92, 93)


entries = [
    (Verstappen, RB26),
    (Norris, MCL40),
    (Leclerc, SF26)
]

results = simulate_race(entries)

print("\n=== RACE RESULTS ===\n")

for position, (driver, score) in enumerate(results, start=1):
    print(f"{position}. {driver.name} - {score:.2f}")