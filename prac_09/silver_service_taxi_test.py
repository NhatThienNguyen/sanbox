from prac_09.silver_service_taxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi(name='Tesla', fuel=100, fanciness=2)
print(my_taxi)
my_taxi.drive(18)
print(my_taxi.calculate_fare())