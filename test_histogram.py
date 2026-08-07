import unittest

from histogram import bucket_counts, normalize


class BucketCountsTest(unittest.TestCase):
    def test_values_land_in_their_bucket(self) -> None:
        self.assertEqual(bucket_counts([1, 5, 9], [0, 4, 8, 12]), [1, 1, 1])

    def test_a_boundary_value_belongs_to_the_upper_bucket(self) -> None:
        self.assertEqual(bucket_counts([4], [0, 4, 8]), [1, 0])

    def test_out_of_range_values_are_dropped(self) -> None:
        self.assertEqual(bucket_counts([-1, 100], [0, 4, 8]), [0, 0])


class NormalizeTest(unittest.TestCase):
    def test_counts_sum_to_one(self) -> None:
        self.assertEqual(normalize([1, 1, 2]), [0.25, 0.25, 0.5])


if __name__ == "__main__":
    unittest.main()
