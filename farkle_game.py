def ask_user():
    """asks the user how many players & how many points they are playing to"""
    num_players = int(input("How many players are playing? "))
    points_to_play_to = int(input("How many points are you playing to? "))
    print(f"Starting a game with {num_players} players, Playing to {points_to_play_to} points.")

def main():
    ask_user()
    players_turn = input("Enter player's name for their turn: ")
    round_points = 0
    print(f"{players_turn}'s Turn")
    print(f"Current points for the round: {round_points}")

def roll_dice():
    pass

def determine_points(dice_values):
    pass



if __name__ == "__main__":
    main()