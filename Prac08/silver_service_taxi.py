"""
Silver service taxi class
"""

from CP1404.Prac08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flag_fall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return complete string with flag fall pricing."""
        return "{} plus flag fall of ${:.2f}".format(super().__str__(),self.flag_fall)

    def get_fare(self):
        """Get the current fare."""
        return self.flag_fall + super().get_fare()