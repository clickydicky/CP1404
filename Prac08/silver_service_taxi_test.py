"""
Silver service taxi text
"""

from CP1404.Prac08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print("Total fare: {}" .format(taxi.get_fare()))


main()
