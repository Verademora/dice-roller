#!/usr/bin/env python3

import sys
import random

# Dice roller
# 
# Takes an argument of dice to roll and 2 optional (But required together) 
# modifier arguments to add or subtract from the roll 
# 
# Example:  'roll 3d6' - rolls 3 6-sided dice and returns the rolls and sum
#           'roll 2d8 + 12' - rolls 2 8-sided dice and prints rolls and sum then adds 12 and returns a final result


def main():

    # Check for too many or too few arguments
    if len(sys.argv) != 2 and len(sys.argv) != 4:
        print("Error: Invalid syntax")
        err_handle(1)

    # Attempt to parse the dice argument
    dice = sys.argv[1]

    try:
        values = dice.lower().split("d")
        qty = int(values[0])
        sides = int(values[1])
    except:
        print(f"Error: Invalid dice input \'{sys.argv[1]}\'")
        err_handle(1)

    # If only a dice argument is provided roll the dice and print the results
    # Otherwise attempt to 
    if len(sys.argv) == 2:
        rolls = dice_roll(qty, sides)
        results(rolls)
        return None

    else:
        try:
            operator = sys.argv[2]
            modifier = int(sys.argv[3])
        except ValueError:
            print(f"Error: Invalid modifier \'{sys.argv[3]}\'")
            err_handle(1)
        if operator != "+" and operator != "-":
            print(f"Error: Invalid operator \'{sys.argv[2]}\'")
            err_handle(1)
        rolls = dice_roll(qty, sides) 
        total = modify(sum(rolls), operator, modifier)
        results(rolls, operator, modifier, total)
        return None

    return None
    

def dice_roll(qty, sides):
    """Takes an argument for number of dice to roll and number of sides then rolls the dice and returns a list of rolls"""
    rolls = []
    total = 0
    for i in range(qty):
        rolls.append(random.randint(1, sides))

    return rolls

def modify(value, operator, mod):
    if operator == "+":
        return value + mod
    else:
        return value - mod

def err_handle(errno):
    print()
    print(f"Usage: {sys.argv[0]} [dice] [optional: operator] [optional: mod]")
    print("[dice] should be a value provided as xdy where x is the number of dice and y is the number of sides the dice has")
    print()
    print("Examples:\t\"roll 3d6\" - Rolls 3 6-sided dice and returns the rolls and sum")
    print("\t\t\"roll 2d8 + 12\" - Rolls 2 8-sided dice and returns the rolls and sum and then adds the modifier to the sum")
    sys.exit(errno)

def results(rolls, operator=None, modifier=None, total=None):
    print("--------------------------------")
    print("You rolled: ", end="")
    for i, roll in enumerate(rolls):
        if i > 0:
            print(", ", end="")
        print(roll, end="")
    print("\n")
    print(f"For a total of: {sum(rolls)}")
    
    if operator != None and modifier != None and total != None:
        print(f"\n{sum(rolls)} {operator} {modifier} = {total}")

    else:
        total = sum(rolls)

    print("--------------------------------")
    print(f"Final result = {total}\n")
    return None

if __name__ == "__main__":
    main()
