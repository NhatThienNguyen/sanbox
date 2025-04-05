from prac_09.car import Car
from random import randint

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability


    def __str__(self):
        return f"{super().__str__()}, reliability: {self.reliability}%"


    def drive(self, distance):
        drive_chance = randint(0, 100)
        if drive_chance > self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven