import unittest

from stats import average, largest


class AverageTest(unittest.TestCase):
    def test_the_mean_of_three(self) -> None:
        self.assertEqual(average([1.0, 2.0, 3.0]), 2.0)


class LargestTest(unittest.TestCase):
    def test_the_largest_of_three(self) -> None:
        self.assertEqual(largest([1.0, 5.0, 3.0]), 5.0)

    def test_no_values_is_zero(self) -> None:
        self.assertEqual(largest([]), 0.0)


if __name__ == "__main__":
    unittest.main()
