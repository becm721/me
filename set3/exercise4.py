# -*- coding: UTF-8 -*-
"""Set 3, Exercise 4."""


import math
from typing import Sequence

# import time
import math


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    
    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    
    This will be quite hard, especially hard if you don't have a good diagram!
    
    Use the VS Code debugging tools a lot here. It'll make understanding 
    things much easier.
    """
    tries = 0
    guess = 0

    # Taking Inputs
    lower = int(input("Enter Lower bound:- "))
    upper = int(input("Enter Upper bound:- "))

    # generating random number between the lower and upper
    x = math.randint(lower, upper)
    print(
        "\n\tYou've only ",
        round(math.log(upper - lower + 1, 2)),
        " chances to guess the integer!\n",
    )

    # Initializing the number of guesses.
    tries = 0

    # for calculation of minimum number of
    # guesses depends upon range
    while tries < math.log(upper - lower + 1, 2):
        tries += 1

    # taking guessing number as input
    guess = int(input("Guess a number:- "))

    # Condition testing
    if x == guess:
        print("Congratulations you did it in ", tries, " try")
        # Once guessed, loop will break
        breakpoint
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")

    # If Guessing is more than required guesses,shows this output.
    if tries >= math.log(upper - lower + 1, 2):
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next time!")

    return {"guess": guess, "tries": tries}


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))

