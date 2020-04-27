import unittest
from maximum_loot import maximum_loot_value


class TestMaximumLoot(unittest.TestCase):
    def test(self):
        for (capacity, weights, prices, answer) in [
            (1000, [30], [500], 500),
            (50, [20, 50, 30], [60, 100, 120], 180.0),
            (10, [30], [500], 500/3),
            (20, [5, 15], [10, 20], 30.0),
            (1000, [30], [500], 500)
        ]:
            self.assertAlmostEqual(
                maximum_loot_value(capacity, weights, prices),
                answer,
                delta=1e-03
            )


if __name__ == '__main__':
    unittest.main()
