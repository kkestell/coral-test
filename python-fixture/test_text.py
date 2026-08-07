from text import columns, initials, slugify, truncate, wrap


def test_initials_takes_the_first_letter_of_each_word() -> None:
    assert initials("ada lovelace") == "A.L"


def test_truncate_leaves_short_text_alone() -> None:
    assert truncate("short", 20) == "short"


def test_wrap_breaks_between_words() -> None:
    assert wrap("one two three", 7) == ["one two", "three"]


def test_columns_pads_every_column() -> None:
    assert columns([["a", "bb"], ["ccc", "d"]]) == "a    bb\nccc  d "


def test_slugify_joins_words_with_hyphens() -> None:
    assert slugify("Hello, World!") == "hello-world"
