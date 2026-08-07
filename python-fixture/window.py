def moving_average(values: list[float], window: int) -> list[float]:
    """The mean of each `window`-long run of `values`, in order.

    A list of n values has n - window + 1 runs of that length.
    """
    averages = []
    for start in range(len(values) - window):
        run = values[start : start + window]
        averages.append(sum(run) / window)
    return averages
