"""
Estimate time: 1 hour
Actual time:
"""
class Project:
    def __init__(self, name, date, priority, cost:float, percentage):
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.percentage = percentage


    def __str__(self):
        return f"{self.name}, start: {self.date}, priority: {self.priority}, estimate: ${self.cost:.2f}, completion: {self.percentage}"


