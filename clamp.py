"""Bringing a number inside a range."""


def clamp(value: int, low: int, high: int) -> int:
    """`value`, brought inside the inclusive range from `low` to `high`."""
    if low > high:
        raise ValueError(f"low {low} is above high {high}")
    return max(low, min(value, high))
