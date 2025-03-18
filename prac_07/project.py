"""
Estimate time: 1 hour
Actual time:
"""
class Project:
    def __init__(self, name, date, priority:int, cost:float, complete:int):
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.complete = complete


    def __str__(self):
        return f"{self.name}, start: {self.date}, priority: {self.priority}, estimate: ${self.cost:.2f}, completion: {self.complete}%"


