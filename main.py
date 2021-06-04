import numpy
import random
from statistics import mean
import matplotlib.pyplot as plt


# Flip a coin.
# Coin is fair by default. If you want an unfair coin, specify the chance of getting a heads.
# Returns the outcome.
def flip(weight=0.5):
    cent = random.random()
    if cent < weight:
        return "heads"
    else:
        return "tails"


# Play specified number of rounds with parameters of starting pot size and of heads weight (default 0.5 if unspecified):
def play(pot, maxRounds, weight=0.5):
    for i in range(maxRounds):
        coin = flip(weight)
        if coin == "heads":
            pot *= 2
        elif coin == "tails":
            return pot
        else:
            return "Something goofed!"


if __name__ == '__main__':
    pot = 1
    maxRounds = 100
    trials = 100000
    winnings = []
    weight = 0.5
    for j in range(trials):
        winning = play(pot, maxRounds, weight)
        print(winning)
        if isinstance(winning, str):
            print("Something goofed!")
        if isinstance(winning, int):
            winnings.append(winning)
    print("Average winnings: " + str(mean(winnings)))
    plt.hist(winnings, bins=numpy.arange(0, 100, 1))
    # plt.show()
