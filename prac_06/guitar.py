"""
Estimate time: 20 minutes
Actual time:
"""
class Guitar:
    """Represents guitar object"""
    def __init__(self, name='', year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost


    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"