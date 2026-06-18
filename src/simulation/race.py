import random

def simulate_race(drivers):
    results = []

    for driver in drivers:
        score = driver.race_pace + random.randint(-5, 5)
        results.append((driver, score))

    results.sort(key=lambda x: x[1], reverse=True)

    return [d[0] for d in results]