"""Areas of a few shapes."""


def rectangle(width: float, height: float) -> float:
    return width * height


def triangle(base: float, height: float) -> float:
    return base * height / 2


def circle(radius: float) -> float:
    return 3.14159 * radius * radius
