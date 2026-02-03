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
    score = 0
    print(f"{player.name}, your turn!")
    #start loop here
    round_over = False
    while not round_over:
        dice.roll()
        dice.print_dice()
        round_points = dice.determine_ba_farkle_points()
        full_round_points = score+round_points if round_points > 0 else 0
        print(f"Score this roll: {round_points}, for a total score of {full_round_points} this round" +
              f" which would give you a total score of {player.score + full_round_points}")
        if round_points == 0:
            print("You farkled!")
            score = 0
            round_over = True
        else:
            score += round_points
            keep_going = input("Would you like to keep going (y/n): ").lower()
            if keep_going != "y":
                round_over = True
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
        for player in players:
            player.score += play_round(player, dice)
            if player.score >= points_to_play_to:
                found_winner = True
    #determine who won and say it
    

if __name__ == "__main__":
    ask_user()
