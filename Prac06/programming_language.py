"""
Programming languages class
"""


class ProgrammingLanguage:
    """Information about programming languages"""
    def __init__(self, name, typing, reflection, year):
        """Construct details of programming languages."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Returns a programming language information."""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(
            self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        """Check if programming language is dynamic"""
        return self.typing == "Dynamic"
