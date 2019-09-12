import math


class Circle:
    """Circle with radius, area, and diameter."""
    def __init__(self, radius=1):
        self.radius = radius
        self.area = math.pi * self.radius ** 2
        self.diameter = self.radius * 2

    def __repr__(self):
        return f"Circle({self.radius})"
