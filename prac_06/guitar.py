"""
Estimate time: 20 minutes
Actual time:
"""
class Guitar:
    """Represents guitar object"""
    def __init__(self, name='', year=0, cost=0):
        """Initialise a Guitar with name, year and cost"""
        self.name = name
        self.year = year
        self.cost = cost



    def __str__(self):
        """Print out the object with name, year and cost"""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"


    def get_age(self):
        """It returned how old is the guitar"""
        return 2025 - self.year


    def is_vintage(self):
        """to check if the guitar is vintage"""
        return 2025 - self.year >= 50