from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = float(fanciness)
        self.price_per_km = Taxi.price_per_km


    def __str__(self):
        return f"{super().__str__()}, plus flagfall of {self.flagfall:.2f}"


    def calculate_fare(self):
        return self.price_per_km * self.fanciness + self.flagfall