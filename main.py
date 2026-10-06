from src.models.entry import Entry

from src.data.drivers_data import *
from src.data.cars_data import *
from src.data.teams_data import *
from src.data.circuits_data import *

from src.simulation.season import simulate_championship


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


championship = simulate_championship(
    entries,
    calendar
)


for round_number, weekend in enumerate(championship.race_weekends, start=1):

    print("\n" + "=" * 70)
    print(f"ROUND {round_number} - {weekend.circuit.name.upper()}")
    print("=" * 70)

    print("\nQUALIFYING")

    for position, entry in enumerate(
        weekend.qualifying["starting_grid"],
        start=1
    ):
        print(f"P{position:>2} - {entry.driver.name}")

    print("\nRACE")

    for position, (driver, _, _) in enumerate(
        weekend.race_results,
        start=1
    ):
        print(f"P{position:>2} - {driver.name}")

    print("\nTOP 5 CHAMPIONSHIP")

    for position, driver_season in enumerate(
        championship.driver_seasons[:5],
        start=1
    ):
        print(
            f"P{position} - "
            f"{driver_season.driver.name:<15}"
            f"{driver_season.points} pts"
        )


print("\n" + "=" * 70)
print("FINAL CHAMPIONSHIP")
print("=" * 70)

for position, driver_season in enumerate(
    championship.driver_seasons,
    start=1
):
    print(
        f"P{position:>2} "
        f"{driver_season.driver.name:<15}"
        f"{driver_season.points:>4} pts"
    )


print("\n" + "=" * 70)
print("CONSTRUCTORS")
print("=" * 70)

for position, team_season in enumerate(
    championship.team_seasons,
    start=1
):
    print(
        f"P{position:>2} "
        f"{team_season.team.name:<20}"
        f"{team_season.points:>4} pts"
    )