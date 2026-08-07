from text import initials


def test_initials_takes_the_first_letter_of_each_word() -> None:
    assert initials("ada lovelace") == "A.L"
