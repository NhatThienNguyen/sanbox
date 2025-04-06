from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = float(fanciness)
        self.price_per_km = Taxi.price_per_km


    def __str__(self):
        return f"{super().__str__()}, fanciness: {self.fanciness}"