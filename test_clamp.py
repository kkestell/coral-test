import unittest

from clamp import clamp


class ClampTest(unittest.TestCase):
    def test_a_value_inside_the_range_is_unchanged(self) -> None:
        self.assertEqual(clamp(5, 1, 10), 5)

    def test_a_value_below_the_range_comes_up_to_low(self) -> None:
        self.assertEqual(clamp(-3, 1, 10), 1)

    def test_a_value_above_the_range_comes_down_to_high(self) -> None:
        self.assertEqual(clamp(99, 1, 10), 10)

    def test_the_bounds_themselves_are_inside(self) -> None:
        self.assertEqual(clamp(1, 1, 10), 1)
        self.assertEqual(clamp(10, 1, 10), 10)

    def test_a_single_point_range(self) -> None:
        self.assertEqual(clamp(7, 4, 4), 4)

    def test_an_inverted_range_is_refused(self) -> None:
        with self.assertRaises(ValueError):
            clamp(5, 10, 1)


if __name__ == "__main__":
    unittest.main()
