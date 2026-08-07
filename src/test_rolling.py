from rolling import RollingAverage


def test_the_average_of_one_reading_is_that_reading():
    average = RollingAverage(3)
    average.add(10)
    assert average.average() == 10


def test_the_average_of_three_readings():
    average = RollingAverage(3)
    for reading in (10, 20, 30):
        average.add(reading)
    assert average.average() == 20
