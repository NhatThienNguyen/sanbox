"""
Estimate time: 20 minutes
Actual time: 21 minutes
"""
class ProgrammingLanguage:
    """Represent programming language object"""
    def __init__(self, name, typing, reflection, year):
        """Initiate programming language"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year


    def is_dynamic(self):
        """To check if that language is dynamic"""
        return self.typing == 'Dynamic'


    def __str__(self):
        """To print out the object"""
        return f"{self.name}, {self.typing}, Reflection={self.reflection}, First appeared in {self.year}"