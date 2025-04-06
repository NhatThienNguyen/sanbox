from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Represent a silver service taxi"""
    flagfall = 4.50
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = float(fanciness)
        self.price_per_km = Taxi.price_per_km


    def __str__(self):
        """Return a string inherit from parent class plus from this class"""
        return f"{super().__str__()}, plus flagfall of {self.flagfall:.2f}"


    def drive(self, distance):
        return super().drive(distance)


    def calculate_fare(self):
        """Calculate the fare of a service based on price, fanciness, distance and flagfall"""
        base_fare = super().get_fare()
        return base_fare * self.fanciness + self.flagfall