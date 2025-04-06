from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    print(f"Let's drive!\n{MENU}")
    choice = input(">>> ").lower()
    current_taxi = None
    total_bill = 0
    while choice != 'q':
        print(f"Bill to date:")
        if choice == 'c':
            i = 0
            for taxi in taxis:
                i+=1
            print(f"{i} - {taxi}")
            try:
                taxi_choice = int(input("Choose taxi: "))
                if 0 <= taxi_choice < len(taxis):
                    current_taxi = taxis[taxi_choice]
                else:
                    print("Invalid taxi choice!")
            except ValueError:
                print("Invalid input!")