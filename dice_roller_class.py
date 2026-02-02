import random

"""a constructor is what is called when we first create and object from our class
    used to initialize any necessary vallues"""
class DiceRoller:
    def __init__(self, num_of_dice):
        self.num_of_dice = num_of_dice
        self.values = [0] * num_of_dice
        self.dice_art = {
            1: ("┌─────────┐",
                "│         │",
                "│    ●    │",
                "│         │",
                "└─────────┘"),
            2: ("┌─────────┐",
                "│  ●      │",
                "│         │",
                "│      ●  │",
                "└─────────┘"),
            3: ("┌─────────┐",
                "│  ●      │",
                "│    ●    │",
                "│      ●  │",
                "└─────────┘"),
            4: ("┌─────────┐",
                "│  ●   ●  │",
                "│         │",
                "│  ●   ●  │",
                "└─────────┘"),
            5: ("┌─────────┐",
                "│  ●   ●  │",
                "│    ●    │",
                "│  ●   ●  │",
                "└─────────┘"),
            6: ("┌─────────┐",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "└─────────┘")
        }

    """when roll is called each value in the values list should be set to a random number from 1 to 6"""
    def roll(self):
        for i in range(self.num_of_dice):
            self.values[i] = random.randint(1, 6)

    """returns the sum of the dice (the sum of the elements in the values list)"""
    def get_total(self):
        return sum(self.values)
    
    """print the dice (horizontally, like at the end of the video)"""
    def print_dice(self):
        for line in range(5):
            for die in self.values:
                print(self.dice_art.get(die)[line], end="")
            print()

    def determine_ba_farkle_points(self):
        if len(set(self.values)) == 1:
            return 500
        score = 0
        for val in self.values:
            if val == 5:
                score += 50
            elif val == 1:
                score += 100
        return score

