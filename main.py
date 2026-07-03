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


print("\n" + "=" * 60)
print("DRIVERS' CHAMPIONSHIP")
print("=" * 60)

print(f"\n{'Pos':<4}{'Driver':<15}{'Points':>8}{'Wins':>8}{'Podiums':>10}")

for position, driver in enumerate(championship.driver_seasons, start=1):

    print(
        f"{position:<4}"
        f"{driver.driver.name:<15}"
        f"{driver.points:>8}"
        f"{driver.wins:>8}"
        f"{driver.podiums:>10}"
    )


print("\n" + "=" * 60)
print("CONSTRUCTORS' CHAMPIONSHIP")
print("=" * 60)

print(f"\n{'Pos':<4}{'Team':<18}{'Points':>8}")

for position, team in enumerate(championship.team_seasons, start=1):

    print(
        f"{position:<4}"
        f"{team.team.name:<18}"
        f"{team.points:>8}"
    )