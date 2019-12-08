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
    # also accounts for recursive base
    if not isinstance(dice, list):
        dice = [dice]

    # each die can be at the minimum 1, so the sum cannot be less than the number of dice
    if x < len(dice):
        return 0

    # is it possible for the dice to sum up to x?
    max = 0
    for die in dice:
        max += die

    if max < x:
        return 0

    if len(dice) == 1:
        if dice[0] < x:
            return 0 # cannot roll x, as dice has no side for it
        else:
            return 1 / dice[0] # one side has x
    """
    For multiple dice,
    compute the chance recursively.
    There may be a way to do this
    iteratively, or with a basic formula,
    but I'm not sure how I would do that.
    """
    chance = 0
    otherDice = dice.copy()
    lockedIn = otherDice.pop() # removes last die
    for i in range(1, lockedIn + 1):
        # varry the value of lockedIn
        chanceOthers = chanceX(otherDice, x - i)
        #print("The chance of rolling {} using {}, given {} is {}".format(x, otherDice, i, chanceOthers / lockedIn))
        chance += chanceOthers / lockedIn # || to chances together
        # chance to roll (x -i) times the chance to roll with the other dice, times the chance to roll i with this die

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

def formatChance(dice, rollX, orMore=False):
    rollStr = str(rollX)
    f = chanceX

    if orMore:
        rollStr += " or higher"
        f = chanceXPlus

    print("The chance of rolling a {} using the dice {} is {}".format(rollStr, dice, str(int(f(dice, rollX) * 100)) + "%"))

def testAllSingle():
    dice = [4, 6, 8, 10, 20] #might be up to 2 more
    for die in dice:
        for i in range(1, die + 1):
            formatChance([die], i, False)
            #print("Chance to roll " + str(i) + " or more using a d" + str(die) + ": " + str(chanceXPlus(die, i)))

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

if __name__ == "__main__":
    testAllSingle()
    #testCombos()
    #testChanceX()
