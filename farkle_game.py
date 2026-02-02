import dice_roller_class

class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

def ask_user():
    """asks the user how many players & how many points they are playing to"""
    num_players = int(input("How many players are playing? "))
    points_to_play_to = int(input("How many points are you playing to? "))
    print(f"\nStarting game with {num_players} players, Playing till {points_to_play_to} points.")
    main(num_players, points_to_play_to)

def play_round(player, dice):
    #has the player roll until they choose to stop or farkle
    score = 0
    print(f"{player.name}, your turn!")
    #start loop here
    dice.roll()
    dice.print_dice()
    print(f"Score this roll: {dice.determine_ba_farkle_points()}")
    input()
    #there's more to happen here
    #check for farkle, if farkle, score = 0 exit loop
    #if not farkle, ask if user wants to roll again to add to score
    # if not, stop, send back total score. 
    return score
    

def main(num_players=2, points_to_play_to=1000):
    dice = dice_roller_class.DiceRoller(3)
    """starts the players turn"""
    players = []
    for i in range(num_players):
        name = input(f"Enter player {i+1}'s name for their turn: ")
        players.append(Player(name))
    found_winner = False

    while not found_winner:
        #player a round:
        for player in players:
            player.score += play_round(player, dice)
            if player.score >= points_to_play_to:
                found_winner = True
    #determine who won and say it


if __name__ == "__main__":
    ask_user()
