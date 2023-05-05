class alreadyBorrowed(Exception):
    def __init__(self):
        self.message = "copy is already borrowed"
        
        super().__init__(self.message)


class InvalidYearCupError(Exception):
    def __init__(self):
        self.message = "there was no world cup this year"
        super().__init__(self.message)


class ImpossibleTitlesError(Exception):
    def __init__(self):
        self.message = "impossible to have more titles than disputed cups"
        super().__init__(self.message)
