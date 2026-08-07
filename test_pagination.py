import unittest

from pagination import page_count, paginate


class PageCountTest(unittest.TestCase):
    def test_an_exact_fit(self) -> None:
        self.assertEqual(page_count(["a"] * 20, 10), 2)

    def test_a_partial_last_page(self) -> None:
        self.assertEqual(page_count(["a"] * 21, 10), 3)

    def test_no_items_is_no_pages(self) -> None:
        self.assertEqual(page_count([], 10), 0)


class PaginateTest(unittest.TestCase):
    def test_a_page_past_the_end_is_empty(self) -> None:
        self.assertEqual(paginate(["a", "b"], 10, 5), [])


if __name__ == "__main__":
    unittest.main()
