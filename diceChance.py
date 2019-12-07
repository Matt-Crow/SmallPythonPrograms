"""
Calculates the chance of rolling specific numbers or higher
using a set of dice (d4, d6, d20, etc)
"""

"""
Caclulates the probability
that the sum of all dice rolled
will be at least x
"""
def chanceXPlus(dice, x):
    chance = 0
    if not isinstance(dice, list):
        dice = [dice]
    for die in dice:
        if die < x:
            chance += 0
        else:
            chance += (die - x + 1) / die
    return chance

def testAll():
    dice = [4, 6, 8, 10, 20] #might be up to 2 more
    for die in dice:
        for i in range(1, die + 1):
            print("Chance to roll " + str(i) + " or more using a d" + str(die) + ": " + str(chanceXPlus(die, i)))
    chanceXPlus(dice, 20)

testAll()
