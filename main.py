from src.models.entry import Entry

from src.data.drivers_data import *
from src.data.cars_data import *
from src.data.teams_data import *
from src.data.circuits_data import *

from src.simulation.race import (
    calculate_driver_performance,
    calculate_car_performance,
    calculate_team_performance
)


entries = [

    Entry(verstappen, rb26, red_bull),
    Entry(hadjar, rb26, red_bull),

    Entry(norris, mcl40, mclaren),
    Entry(piastri, mcl40, mclaren),

    Entry(leclerc, sf26, ferrari),
    Entry(hamilton, sf26, ferrari),

    Entry(russell, w17, mercedes),
    Entry(antonelli, w17, mercedes),

    Entry(alonso, amr26, aston_martin),
    Entry(stroll, amr26, aston_martin),

    Entry(sainz, fw48, williams),
    Entry(albon, fw48, williams),

    Entry(gasly, a526, alpine),
    Entry(colapinto, a526, alpine),

    Entry(ocon, vf26, haas),
    Entry(bearman, vf26, haas),

    Entry(hulkenberg, r26, audi),
    Entry(bortoleto, r26, audi),

    Entry(lawson, vcarb02, racing_bulls),
    Entry(lindblad, vcarb02, racing_bulls),

    Entry(perez, c01, cadillac),
    Entry(bottas, c01, cadillac),
]


circuit = monza

print(f"\n========== {circuit.name.upper()} ==========\n")

ranking = []

for entry in entries:

    driver_score = calculate_driver_performance(entry.driver)
    car_score = calculate_car_performance(entry.car, circuit)
    team_score = calculate_team_performance(entry.team)

    final_score = (
        driver_score * 0.5 +
        car_score * 0.4 +
        team_score * 0.1
    )

    ranking.append({
        "driver": entry.driver.name,
        "team": entry.team.name,
        "car": driver_score,
        "car_perf": car_score,
        "team_perf": team_score,
        "final": final_score
    })

ranking.sort(
    key=lambda x: x["final"],
    reverse=True
)

print(
    f"{'Driver':<12}"
    f"{'Team':<16}"
    f"{'Driver':>10}"
    f"{'Car':>10}"
    f"{'Team':>10}"
    f"{'Final':>10}"
)

print("-" * 68)

for data in ranking:

    print(
        f"{data['driver']:<12}"
        f"{data['team']:<16}"
        f"{data['car']:>10.2f}"
        f"{data['car_perf']:>10.2f}"
        f"{data['team_perf']:>10.2f}"
        f"{data['final']:>10.2f}"
    )