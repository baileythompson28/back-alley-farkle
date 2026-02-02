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


def dice_roll():
    """rolls 3 dice and displays result"""
    from dice_roller_class import DiceRoller
    dice_roller = DiceRoller(3)
    dice_roller.roll()
    dice_roller.print_dice()
    return dice_roller.values


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
        print("Farkle.")
        return 0
    print(f"Points scored: {points}")
    return points



if __name__ == "__main__":
    main()
