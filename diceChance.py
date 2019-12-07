"""
Calculates the chance of rolling specific numbers or higher
using a set of dice (d4, d6, d20, etc)
"""

"""
Calculates the probability
that the sum of all dice
rolled will exactly equal x
"""
def chanceX(dice, x):
    # first, set up base cases
    # account for only one die passed
    if not isinstance(dice, list):
        dice = [dice]
    # each die can be at the minimum 1
    if x < len(dice):
        return 0

    """
    How do I calculate for multiple dice?
    """
    # now, how do I calculate this?
    # let's see if I can determine a formula


    # compute the number of permutations
    # this is the cartesian product of each die
    chance = 0
    denom = 1
    max = 0
    for die in dice:
        denom *= die
        max += die

    if max < x:
        return 0

    if len(dice) == 1:
        return 1 / dice[0] # only one face can equal x

    # use recursion for multiple
    otherDice = dice.copy()
    lockedIn = otherDice.pop() # removes last die
    for i in range(1, lockedIn + 1):
        #vary the value of lockedIn
        chanceOthers = chanceX(otherDice, x - i)
        print("The chance of rolling {} using {}, given {} is {}".format(x, otherDice, i, chanceOthers / lockedIn))
        chance += chanceOthers / lockedIn

    return chance

"""
Caclulates the probability
that the sum of all dice rolled
will be at least x
"""
def chanceXPlus(dice, x):
    chance = 0
    if not isinstance(dice, list):
        dice = [dice]

    added = 1
    while added != 0:
        added = chanceX(dice, x)
        chance += added
        x += 1

    return chance

def testAll():
    dice = [4, 6, 8, 10, 20] #might be up to 2 more
    for die in dice:
        for i in range(1, die + 1):
            print("Chance to roll " + str(i) + " or more using a d" + str(die) + ": " + str(chanceXPlus(die, i)))
    chanceXPlus(dice, 20)

def testCombos():
    dice = [4, 6]
    for die1 in dice:
        for die2 in dice:
            for sum in range(1, die1 + die2 + 1):
                if die1 != die2:
                    print(str(sum) + " : " + str(chanceX([die1, die2], sum)))
    print("rolling a d4, a d6, and a d8, the chance of their sum being a 5 is: ")
    print(chanceX([4, 6, 8], 5))

def testChanceX():
    dice = [4, 6, 8, 10, 20] #might be up to 2 more
    for die1 in dice:
        for die2 in dice:
            for sum in range(1, die1 + die2 + 1):
                if die1 != die2:
                    print(str(sum) + " : " + str(chanceX([die1, die2], sum)))

#testAll()
testCombos()
#testChanceX()
