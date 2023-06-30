import random


class Cube:
    def __init__(self, odds):
        self.roll = None
        self.odds = odds

    def roll_dice(self):
        self.roll = int(random.choice(self.odds))
        return self.roll


