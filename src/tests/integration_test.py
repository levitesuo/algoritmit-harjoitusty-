import unittest
from services.running_service import AppEngine


class IntegrationTest(unittest.TestCase):
    def setUp(self):
        self.engine = AppEngine()
        self.engine.draw_results = False
        self.engine.octaves = (2, 5, 10)
        self.engine.amplitudes = (1, 0.2, 0.05)

    def test_seed_1_cost(self):
        self.engine.random_seed = 1
        self.engine.init_empty_values()
        best_path_length = 153.39893153085478
        results = self.engine.execute()
        costs = [results[run]['cost'] for run in results]
        for cost in costs:
            self.assertEqual(cost, best_path_length)

    def test_seed_2_path(self):
        self.engine.random_seed = 2
        self.engine.init_empty_values()
        best_path_length = 90.40765252767535
        results = self.engine.execute()
        costs = [results[run]['cost'] for run in results]
        for cost in costs:
            self.assertEqual(cost, best_path_length)

    def test_seed_3_path(self):
        self.engine.random_seed = 3
        self.engine.init_empty_values()
        best_path_length = 138.07620668705226
        results = self.engine.execute()
        costs = [results[run]['cost'] for run in results]
        for cost in costs:
            self.assertEqual(cost, best_path_length)
