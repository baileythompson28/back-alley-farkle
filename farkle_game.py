def ask_user():
    """asks the user how many players & how many points they are playing to"""
    num_players = int(input("How many players are playing? "))
    points_to_play_to = int(input("How many points are you playing to? "))
    print(f"Starting game with {num_players} players, Playing till {points_to_play_to} points.")
    main()


def main():
    """starts the players turn"""
    players_turn = input("Enter player's name for their turn: ")
    print(f"{players_turn}'s turn")
    dice_roll()


def dice_roll():
    """rolls 3 dice and displays result"""
    import dice_roller_class
    num_of_dice = 3
    dice_roller = dice_roller_class.DiceRoller(num_of_dice)
    dice_roller.roll()
    dice_roller.print_dice()
    print(f"total: {dice_roller.get_total()}")


def determine_points(roll_values):
    """determines points"""
    points = 0
    counts = {i: roll_values.count(i) for i in range(1, 7)}

    for num, count in counts.items():
        if count >= 3:
            points += 500
            counts[num] -= 3
    points += counts[1] * 100
    points += counts[5] * 50
    if points == 0:
        print("Farkle. You get no points this round.")
        return 0
    print(f"Points scored: {points}")
    return points

def next_turn():
    """next player's turn"""
    next_player = input("Enter next player's name for their turn: ")
    print(f"{next_player}'s turn")
    dice_roll()

def winner():
    """checks for winner"""
    winner = "Player 1"
    print(f"The winner is {winner}!")
    play_again = input("Play again? (yes/no): ")
    if play_again.lower() == 'yes':
        ask_user()
    else:
        print("bye bye")


if __name__ == "__main__":
    ask_user()
