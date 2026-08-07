import unittest

from slugify import slugify


class SlugifyTest(unittest.TestCase):
    def test_words_become_hyphens(self) -> None:
        self.assertEqual(slugify("Hello There World"), "hello-there-world")

    def test_punctuation_collapses(self) -> None:
        self.assertEqual(slugify("What's new -- in 2026?!"), "what-s-new-in-2026")

    def test_edges_are_trimmed(self) -> None:
        self.assertEqual(slugify("  ...Leading and trailing!  "), "leading-and-trailing")

    def test_nothing_usable_is_empty(self) -> None:
        self.assertEqual(slugify("!!!"), "")
        self.assertEqual(slugify(""), "")


if __name__ == "__main__":
    unittest.main()
