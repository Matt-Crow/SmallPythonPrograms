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
    """
    How do I calculate for multiple dice?
    """
    # first, compute the number of permutations
    # this is the cartesian product of each die
    denom = 1
    for die in dice:
        denom *= die
    print(dice)
    print("Has " + str(denom) + " permutations")

    num = 0
    # first, how would I calculate it for 2 dice?
    if len(dice) == 2:
        num = dice[0] + dice[1] - x + 1
        chance = num / denom

    # now, what would be the formula for an arbitrary number of dice?

    return chance

def testAll():
    dice = [4, 6, 8, 10, 20] #might be up to 2 more
    for die in dice:
        for i in range(1, die + 1):
            print("Chance to roll " + str(i) + " or more using a d" + str(die) + ": " + str(chanceXPlus(die, i)))
    chanceXPlus(dice, 20)

def testCombos():
    dice = [4, 6, 8, 10, 20] #might be up to 2 more
    for die1 in dice:
        for die2 in dice:
            for sum in range(1, die1 + die2 + 1):
                if die1 != die2:
                    print(str(sum) + " : " + str(chanceXPlus([die1, die2], sum)))

#testAll()
testCombos()
