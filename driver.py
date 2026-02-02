import dice_roller_class

num_of_dice = int(input("How many dice?: "))
dice_roller = dice_roller_class.DiceRoller(num_of_dice)
dice_roller.roll()
dice_roller.print_dice()
print(f"total: {dice_roller.get_total()}")
