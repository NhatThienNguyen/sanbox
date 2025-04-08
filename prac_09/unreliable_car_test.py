from prac_09.unreliable_car import UnreliableCar

test_car = UnreliableCar(name="Tesla", fuel=100, reliability=30)
for i in range(10):
    print(f"The car has driven: {test_car.drive(30)} Km")