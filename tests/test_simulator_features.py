import unittest
from types import SimpleNamespace

from src.data.cars_data import rb26, mcl40
from src.data.circuits_data import australia
from src.data.drivers_data import verstappen, norris
from src.data.teams_data import red_bull, mclaren
from src.models.entry import Entry
from src.simulation.race import (
    apply_driver_errors,
    calculate_race_base_score,
    calculate_team_performance,
    generate_weather,
    generate_safety_car_state,
    precompute_entries_scores,
)
from src.simulation.season import simulate_championship
from src.models.team import Team


class SimulatorFeatureTests(unittest.TestCase):
    def setUp(self):
        self.entry_1 = Entry(verstappen, rb26, red_bull)
        self.entry_2 = Entry(norris, mcl40, mclaren)

    def test_generate_weather_returns_dry_or_wet(self):
        weather = generate_weather(australia)
        self.assertIn(weather, {"dry", "wet"})

    def test_apply_driver_errors_returns_penalties(self):
        penalties = apply_driver_errors([self.entry_1, self.entry_2], australia, "dry")
        self.assertIsInstance(penalties, dict)
        self.assertGreaterEqual(len(penalties), 1)

    def test_team_performance_includes_development_progress(self):
        team = Team(
            "Test Team",
            90, 90, 90,
            95, 90, 90,
            90, 90, 90,
            90
        )
        team.development_progress = 0.15
        performance = calculate_team_performance(team)
        self.assertGreater(performance, 90)

    def test_entry_cache_tracks_team_development(self):
        original_progress = self.entry_1.team.development_progress
        self.entry_1.reset_performance_cache()
        try:
            initial_score = calculate_race_base_score(self.entry_1, australia, "dry")
            self.entry_1.team.development_progress = original_progress + 0.2
            developed_score = calculate_race_base_score(self.entry_1, australia, "dry")
            self.assertAlmostEqual(developed_score - initial_score, 0.02)
        finally:
            self.entry_1.team.development_progress = original_progress
            self.entry_1.reset_performance_cache()

    def test_championship_reuse_resets_season_state(self):
        entries = [self.entry_1, self.entry_2]
        original_progress = [
            (entry.team, entry.team.development_progress)
            for entry in entries
        ]
        try:
            championship = simulate_championship(entries, [australia])
            first_progress = {
                team.team.name: team.team.development_progress
                for team in championship.team_seasons
            }

            reused = simulate_championship(entries, [australia], championship)

            self.assertIs(reused, championship)
            self.assertEqual(reused.current_round, 1)
            self.assertEqual(len(reused.race_weekends), 1)
            self.assertEqual(
                {
                    team.team.name: team.team.development_progress
                    for team in reused.team_seasons
                },
                first_progress,
            )
        finally:
            for team, progress in original_progress:
                team.development_progress = progress
            for entry in entries:
                entry.reset_performance_cache()

    def test_lightweight_championship_mode_skips_weekend_details(self):
        entries = [self.entry_1, self.entry_2]
        championship = simulate_championship(entries, [australia], keep_details=False)
        self.assertEqual(len(championship.race_weekends), 0)
        self.assertGreaterEqual(len(championship.driver_seasons), 2)
        self.assertGreaterEqual(championship.driver_seasons[0].points, 0)

    def test_precompute_entries_scores_populates_entry_cache(self):
        entries = [self.entry_1, self.entry_2]
        for entry in entries:
            entry.reset_performance_cache()

        precompute_entries_scores(entries, australia, "dry")

        self.assertGreater(len(self.entry_1.base_performance_cache), 0)
        self.assertGreater(len(self.entry_2.base_performance_cache), 0)
        self.assertIn(
            ("race", australia.name, "dry", self.entry_1.team.development_progress),
            self.entry_1.base_performance_cache,
        )

    def test_generate_safety_car_state_returns_valid_state(self):
        state = generate_safety_car_state(australia, 0.6)
        self.assertIn(state["mode"], {"none", "safety_car", "virtual_safety_car"})
        self.assertGreaterEqual(state["degradation_factor"], 0.0)

    def test_compact_season_summary_preserves_driver_totals(self):
        from main_montecarlo import _summarize_season

        driver_1 = SimpleNamespace(driver=SimpleNamespace(name="Hamilton"), points=25, wins=1, podiums=1)
        driver_2 = SimpleNamespace(driver=SimpleNamespace(name="Verstappen"), points=18, wins=0, podiums=1)
        championship = SimpleNamespace(driver_seasons=[driver_1, driver_2])

        champion_name, totals = _summarize_season(championship)

        self.assertEqual(champion_name, "Hamilton")
        self.assertEqual(totals["Hamilton"], [25, 1, 1])
        self.assertEqual(totals["Verstappen"], [18, 0, 1])

    def test_batch_planner_keeps_balanced_worker_work(self):
        from main_montecarlo import _plan_batches

        batches = _plan_batches(25000, 7)

        self.assertEqual(sum(batches), 25000)
        self.assertGreaterEqual(len(batches), 8)
        self.assertLessEqual(max(batches) - min(batches), 1)
        self.assertLessEqual(max(batches), 1000)

    def test_fast_path_form_access_and_context_helpers(self):
        from src.simulation.race import _get_form_value, _build_race_context

        self.entry_1.driver.simulation_index = 1
        self.assertAlmostEqual(_get_form_value({self.entry_1.driver.name: 1.5}, self.entry_1.driver), 1.5)
        self.assertAlmostEqual(_get_form_value([0.25, 0.5], self.entry_1.driver), 0.5)

        context = _build_race_context("dry", {"mode": "none"}, include_context=False)
        self.assertEqual(context["weather"], "dry")
        self.assertEqual(context["safety_car_state"]["mode"], "none")
        self.assertEqual(context["driver_errors"], {})
        self.assertEqual(context["retirements"], {})


if __name__ == "__main__":
    unittest.main()
