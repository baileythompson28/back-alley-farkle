def ask_user():
    """asks the user how many players & how many points they are playing to"""
    num_players = int(input("How many players are playing? "))
    points_to_play_to = int(input("How many points are you playing to? "))
    print(f"Starting game with {num_players} players, Playing till {points_to_play_to} points.")

def main():
    """starts the players turn"""
    ask_user()
    players_turn = input("Enter player's name for their turn: ")
    round_points = 0
    print(f"{players_turn}'s turn")
    print(f"Current points for the round: {round_points}")

def dice_roller():
    pass

def determine_points(dice_values):
    pass



if __name__ == "__main__":
    main()