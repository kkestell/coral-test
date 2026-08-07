def bucket_counts(values: list[float], boundaries: list[float]) -> list[int]:
    """Count how many values fall in each bucket defined by consecutive boundaries.

    `boundaries` has `n` values defining `n - 1` half-open buckets `[boundaries[i], boundaries[i+1])`.
    A value below the first boundary or at or above the last is not counted.
    """
    counts = [0] * (len(boundaries) - 1)
    for value in values:
        for i in range(len(boundaries) - 1):
            if boundaries[i] <= value < boundaries[i + 1]:
                counts[i] += 1
    return counts


def normalize(counts: list[int]) -> list[float]:
    """Scale a list of counts so they sum to 1.0."""
    total = sum(counts)
    return [count / total for count in counts]
