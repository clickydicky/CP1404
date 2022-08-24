"""
Guitar class
"""
import datetime
CURRENT_YEAR = datetime.date.today().year
VINTAGE_AGE = 50


class Guitar:
    """Information of guitar"""
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return guitar information"""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """check age of guitar based on present day's year"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """check if guitar is considered vintage"""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """sort guitar based on release year"""
        return self.year < other.year
