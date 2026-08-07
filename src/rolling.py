"""A rolling average over the most recent readings."""


class RollingAverage:
    def __init__(self, window):
        self.window = window
        self.readings = []

    def add(self, reading):
        self.readings.append(reading)
        if len(self.readings) > self.window:
            self.readings.pop()

    def average(self):
        return sum(self.readings) / len(self.readings)
