from text import initials, truncate


def test_initials_takes_the_first_letter_of_each_word() -> None:
    assert initials("ada lovelace") == "A.L"


def test_truncate_leaves_short_text_alone() -> None:
    assert truncate("ada", 10) == "ada"
