from collections import defaultdict
import time

from src.models.entry import Entry

from src.data.drivers_data import *
from src.data.cars_data import *
from src.data.teams_data import *
from src.data.circuits_data import *

from src.simulation.season import simulate_championship


NUM_SIMULATIONS = 10000


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


calendar = [
    australia,
    china,
    japan,
    bahrain,
    saudi_arabia,
    miami,
    canada,
    monaco,
    barcelona,
    austria,
    united_kingdom,
    belgium,
    hungary,
    netherlands,
    italy,
    madrid,
    azerbaijan,
    singapore,
    usa,
    mexico,
    brazil,
    las_vegas,
    qatar,
    abu_dhabi
]


titles = defaultdict(int)

total_points = defaultdict(int)
total_wins = defaultdict(int)
total_podiums = defaultdict(int)


start = time.perf_counter()

for _ in range(NUM_SIMULATIONS):

    championship = simulate_championship(
        entries,
        calendar
    )

    champion = championship.driver_seasons[0]

    titles[champion.driver.name] += 1

    for driver in championship.driver_seasons:

        name = driver.driver.name

        total_points[name] += driver.points
        total_wins[name] += driver.wins
        total_podiums[name] += driver.podiums

end = time.perf_counter()


ranking = sorted(
    total_points.keys(),
    key=lambda name: (
        titles[name],
        total_points[name],
        total_wins[name],
        total_podiums[name]
    ),
    reverse=True
)


print("\n" + "=" * 95)
print(f"MONTE CARLO SIMULATION ({NUM_SIMULATIONS:,} SEASONS)")
print("=" * 95)

print(
    f"\n{'Driver':<15}"
    f"{'Titles':>10}"
    f"{'Title %':>10}"
    f"{'Avg Pts':>12}"
    f"{'Avg Wins':>12}"
    f"{'Avg Podiums':>14}"
)

print("-" * 95)


for driver in ranking:

    title_percentage = titles[driver] / NUM_SIMULATIONS * 100

    avg_points = total_points[driver] / NUM_SIMULATIONS
    avg_wins = total_wins[driver] / NUM_SIMULATIONS
    avg_podiums = total_podiums[driver] / NUM_SIMULATIONS

    print(
        f"{driver:<15}"
        f"{titles[driver]:>10}"
        f"{title_percentage:>9.2f}%"
        f"{avg_points:>12.1f}"
        f"{avg_wins:>12.2f}"
        f"{avg_podiums:>14.2f}"
    )


elapsed = end - start

print("\n" + "=" * 95)
print(f"Execution time      : {elapsed:.2f} s")
print(f"Average per season : {elapsed / NUM_SIMULATIONS * 1000:.3f} ms")
print(f"Seasons per second : {NUM_SIMULATIONS / elapsed:.1f}")
print("=" * 95)