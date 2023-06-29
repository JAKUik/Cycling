import random

class Cube:
    def __init__(self, odds):
        last_value = None
        self.odds = odds

    def roll(self):
        return random.choice(self.odds)

