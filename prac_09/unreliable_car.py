from prac_09.car import Car
from random import randint

class UnreliableCar(Car):
    """Represents an unreliable car."""
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability


    def __str__(self):
        return f"{super().__str__()}, reliability: {self.reliability}%"


    def drive(self, distance):
        """Check if the reliability is lower than drive chance to decide whether it can be driven or not"""
        drive_chance = randint(0, 100)
        if drive_chance > self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven