"""Slicing a list of results into pages for display."""


def paginate(items: list[str], per_page: int, page: int) -> list[str]:
    """The items on one page.

    Pages are numbered from one, so `paginate(items, 10, 1)` is the first ten items.
    A page past the end is empty rather than an error.
    """
    start = page * per_page
    return items[start : start + per_page]


def page_count(items: list[str], per_page: int) -> int:
    """How many pages the items fill."""
    return (len(items) + per_page - 1) // per_page
