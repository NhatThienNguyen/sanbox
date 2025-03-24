"""
Estimate time: 1 hour
Actual time: 2 days and 3 hours
"""
class Project:
    """Project class"""
    def __init__(self, name, date, priority:int, cost:float, complete:int):
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.complete = complete


    def __str__(self):
        """Default print"""
        return f"{self.name}, start: {self.date}, priority: {self.priority}, estimate: ${self.cost:.2f}, completion: {self.complete}%"


    def __lt__(self, other):
        """Comparing lower than"""
        return self.priority < other.priority