"""
Taxi simulator
"""

from CP1404.Prac06.car import Car
from CP1404.Prac08.taxi import Taxi
from CP1404.Prac08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator program, show menu until quit, display all taxis and show total fare after end of every trip"""
    total_fare = 0
    taxis = [Taxi("SMRT", 100), Taxi("Comfort Delgro", 90), SilverServiceTaxi("Lamborghini", 200, 5)]
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif menu_choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance_to_drive = float(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name,
                                                             trip_cost))
                total_fare += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_fare))
        print(MENU)
        menu_choice = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_fare))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display numbered list of taxis."""
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()