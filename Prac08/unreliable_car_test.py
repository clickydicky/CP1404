"""
Unreliable car test
"""

from CP1404.Prac08.unreliable_car import UnreliableCar


def main():
    """Test UnreliableCars"""

    good_car = UnreliableCar("Mostly Good", 100, 90)
    bad_car = UnreliableCar("Dodgy", 100, 5)

    for i in range(1, 7):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:12} drove {:2}km".format(bad_car.name, bad_car.drive(i)))

    print(good_car)
    print(bad_car)


main()
