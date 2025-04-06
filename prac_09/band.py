from prac_03.exceptions_to_complete import result


class Band:
    def __init__(self, name=''):
        self.name = name
        self.musicians = []


    def __str__(self):
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"