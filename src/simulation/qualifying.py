import random
from collections import namedtuple

QualifyingResult = namedtuple("QualifyingResult", ["entry", "score"])
_RANDOM = random.Random()


def calculate_qualifying_base_score(entry, circuit):
    return entry.qualifying_base_score(circuit)


def simulate_session(entries, circuit, forms):

    session = []

    for entry in entries:
        base_score = calculate_qualifying_base_score(entry, circuit)
        form = forms[entry.driver.name] if isinstance(forms, dict) else forms[entry.driver.simulation_index]
        final_score = base_score + form + _RANDOM.uniform(-2, 2)
        session.append(QualifyingResult(entry, final_score))

    session.sort(key=lambda item: item.score, reverse=True)

    return session


def simulate_qualifying(entries, circuit, forms):

    # ==========================
    # Q1
    # ==========================

    q1_session = simulate_session(
        entries,
        circuit,
        forms
    )

    q1_qualified = q1_session[:16]
    q1_eliminated = q1_session[16:]

    # ==========================
    # Q2
    # ==========================

    q2_entries = [result.entry for result in q1_qualified]

    q2_session = simulate_session(
        q2_entries,
        circuit,
        forms
    )

    q2_qualified = q2_session[:10]
    q2_eliminated = q2_session[10:]

    # ==========================
    # Q3
    # ==========================

    q3_entries = [result.entry for result in q2_qualified]

    q3_session = simulate_session(
        q3_entries,
        circuit,
        forms
    )

    # ==========================
    # Graella final
    # ==========================

    starting_grid = []

    # P1-P10
    starting_grid.extend(result.entry for result in q3_session)

    # P11-P16
    starting_grid.extend(result.entry for result in q2_eliminated)

    # P17-P22
    starting_grid.extend(result.entry for result in q1_eliminated)

    return {
        "starting_grid": starting_grid,
        "q1_results": q1_session,
        "q2_results": q2_session,
        "q3_results": q3_session,
        "pole": q3_session[0][0],
        "pole_score": q3_session[0][1]
    }