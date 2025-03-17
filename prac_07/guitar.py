"""
Estimate time: 20 minutes
Actual time:
"""
class Guitar:
    """Represents guitar object"""
    def __init__(self, name:str, year:int, cost:float):
        """Initialise a Guitar with name, year and cost"""
        self.name = name
        self.year = year
        self.cost = cost


    def __str__(self):
        """Print out the object with name, year and cost"""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"


    def __lt__(self, other):
        """Comparing year of two object"""
        return self.year < other.year