"""Summary statistics over a list of measurements."""


def average(values: list[float]) -> float:
    """The arithmetic mean of the values, or 0.0 when there are none."""
    return sum(values) / len(values)


def largest(values: list[float]) -> float:
    """The largest value, or 0.0 when there are none."""
    if not values:
        return 0.0
    return max(values)
