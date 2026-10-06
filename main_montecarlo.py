from collections import defaultdict
import multiprocessing as mp
import time

from src.models.entry import Entry

from src.data.drivers_data import *
from src.data.cars_data import *
from src.data.teams_data import *
from src.data.circuits_data import *

from src.simulation.season import simulate_championship


NUM_SIMULATIONS = 25000


_WORKER_ENTRIES = None
_WORKER_CALENDAR = None
_WORKER_CHAMPIONSHIP = None


def _initialize_worker(entries, calendar):
    global _WORKER_ENTRIES, _WORKER_CALENDAR, _WORKER_CHAMPIONSHIP
    _WORKER_ENTRIES = entries
    _WORKER_CALENDAR = calendar
    _WORKER_CHAMPIONSHIP = None


def _summarize_season(championship):
    ranking = championship.driver_seasons
    if not ranking:
        return "", {}

    champion_name = ranking[0].driver.name
    driver_totals = {}

    for driver_season in ranking:
        driver_name = driver_season.driver.name
        driver_totals[driver_name] = [
            driver_season.points,
            driver_season.wins,
            driver_season.podiums,
        ]

    return champion_name, driver_totals


def _plan_batches(num_simulations, workers):
    if num_simulations < 1:
        raise ValueError("num_simulations must be greater than zero")
    if workers < 1:
        raise ValueError("workers must be greater than zero")

    workers = min(workers, num_simulations)
    target_batches = min(num_simulations, max(workers * 4, 4))
    batch_size, remainder = divmod(num_simulations, target_batches)
    return [
        batch_size + (1 if index < remainder else 0)
        for index in range(target_batches)
    ]


def _run_season_batch(num_seasons):
    global _WORKER_CHAMPIONSHIP
    results = []

    for _ in range(num_seasons):
        _WORKER_CHAMPIONSHIP = simulate_championship(
            _WORKER_ENTRIES,
            _WORKER_CALENDAR,
            _WORKER_CHAMPIONSHIP,
            keep_details=False,
        )
        champion_name, driver_totals = _summarize_season(_WORKER_CHAMPIONSHIP)
        results.append((champion_name, driver_totals))

    return results


def run_monte_carlo(entries, calendar, num_simulations=NUM_SIMULATIONS, workers=None):
    if num_simulations < 1:
        raise ValueError("num_simulations must be greater than zero")
    if workers is None:
        workers = max(1, mp.cpu_count() - 1)
    if workers < 1:
        raise ValueError("workers must be greater than zero")
    workers = min(workers, num_simulations)

    titles = defaultdict(int)
    total_points = defaultdict(int)
    total_wins = defaultdict(int)
    total_podiums = defaultdict(int)

    start = time.perf_counter()

    batches = _plan_batches(num_simulations, workers)

    with mp.Pool(
        processes=workers,
        initializer=_initialize_worker,
        initargs=(entries, calendar),
    ) as pool:
        for batch_results in pool.map(_run_season_batch, batches):
            for champion_name, driver_totals in batch_results:
                titles[champion_name] += 1
                for name, (points, wins, podiums) in driver_totals.items():
                    total_points[name] += points
                    total_wins[name] += wins
                    total_podiums[name] += podiums

    elapsed = time.perf_counter() - start
    ranking = sorted(
        total_points.keys(),
        key=lambda name: (
            titles[name],
            total_points[name],
            total_wins[name],
            total_podiums[name],
        ),
        reverse=True,
    )

    print("\n" + "=" * 95)
    print(f"MONTE CARLO SIMULATION ({num_simulations:,} SEASONS)")
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
        title_percentage = titles[driver] / num_simulations * 100
        avg_points = total_points[driver] / num_simulations
        avg_wins = total_wins[driver] / num_simulations
        avg_podiums = total_podiums[driver] / num_simulations
        print(
            f"{driver:<15}"
            f"{titles[driver]:>10}"
            f"{title_percentage:>9.2f}%"
            f"{avg_points:>12.1f}"
            f"{avg_wins:>12.2f}"
            f"{avg_podiums:>14.2f}"
        )

    print("\n" + "=" * 95)
    print(f"Execution time      : {elapsed:.2f} s")
    print(f"Average per season : {elapsed / num_simulations * 1000:.3f} ms")
    print(f"Seasons per second : {num_simulations / elapsed:.1f}")
    print("=" * 95)


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


if __name__ == "__main__":
    run_monte_carlo(entries, calendar, NUM_SIMULATIONS)