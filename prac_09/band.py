class Band:
    """Class band"""
    def __init__(self, name=''):
        """Represent band"""
        self.name = name
        self.musicians = []


    def __str__(self):
        """Return string"""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"


    def add(self,musician):
        """Add musician to musicians list"""
        return self.musicians.append(musician)


    def play(self):
        """return string showing band playing"""
        result = []
        for musician in self.musicians:
            result.append(musician.play())
        return "\n".join(result)