from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    """Main function with menu and all the option"""
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    print(f"Let's drive!\n{MENU}")
    choice = input(">>> ").lower()
    current_taxi = None
    total_bill = 0.0
    while choice != 'q':
        if choice == 'c':
            i = 0
            for taxi in taxis:
                print(f"{i} - {taxi}")
                i += 1
            try:
                taxi_choice = int(input("Choose taxi: "))
                if 0 <= taxi_choice < len(taxis):
                    current_taxi = taxis[taxi_choice]
                else:
                    print("Invalid taxi choice!")
            except ValueError:
                print("Invalid input!")
        elif choice =='d':
            if current_taxi is None:
                print("You have to choose a taxi before you can drive")
            else:
                distance = float(input("Drive how far? "))
                current_taxi.start_fare()
                current_taxi.drive(distance)
                if isinstance(current_taxi, SilverServiceTaxi):
                    trip_cost = current_taxi.calculate_fare()
                else:
                    trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you: ${trip_cost:.2f}")
                total_bill += trip_cost
        else:
            print("Invalid option!")
        print(f"Bill to date: ${total_bill}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: {total_bill}")
    print("Taxis are now:")
    i = 0
    for taxi in taxis:
        print(f"{i} - {taxi}")


main()