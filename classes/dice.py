import random


class Dice:
    def __init__(self, odds):
        self.roll = None
        self.odds = odds

    def dice_roll(self):
        self.roll = int(random.choice(self.odds))
        print(self.roll)
        return self.roll


