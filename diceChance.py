"""
Calculates the chance of rolling specific numbers or higher
using a set of dice (d4, d6, d20, etc)

This program is currently extreamly inefficient,
but I have theorized a mathematical, significantly faster solution:
The chance to roll exactly X using a set of dice S:
let N = (the number of integer solutions to the plane X = s1 + s2 + s3 + ... + sn
bounded by 1 <= s <= s_max for each s in S)
let D = s1 * s2 * s3 * ... * sn
(the number of integer solutions to an n-dimesional cube, bounded the same as the plane)

chance = N/D.
"""

import itertools

"""
Calculates the probability
that the sum of all dice
rolled will exactly equal x
dice is an array of integers,
where each element of the array represents the number of sides on the die rolled.
For example, [4, 6, 10] means a 4 sided die, 6 sided die, and 10 sided die are being rolled.
"""
def chanceX(dice, x):
    # first, set up base cases
    # account for only one die passed
    # also accounts for recursive base
    if isinstance(dice, tuple):
        dice = list(dice)
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
    I assume the chance corresponds to the surface area of a plane,
    as when the rolls required are graphed in cartesian coordinates,
    the points form a slanted plane.
    """
    chance = 0
    otherDice = dice.copy()
    lockedIn = otherDice.pop() # removes last die

    # vary the value of the die removed
    for i in range(1, lockedIn + 1):
        # compute the probability that the other dice can sum to the x after the locked in value is added
        chanceOthers = chanceX(otherDice, x - i)
        #print("The chance of rolling {} using {}, given {} is {}".format(x, otherDice, i, chanceOthers / lockedIn))
        chance += chanceOthers / lockedIn # || to chances together
        # chance to roll (x -i) times the chance to roll with the other dice, times the chance to roll i with this die

    return chance


"""
Caclulates the probability
that the sum of all dice rolled
will be at least x.
Dice is an array of integers,
where each element of the array represents the number of sides on the die rolled.
For example, [4, 6, 10] means a 4 sided die, 6 sided die, and 10 sided die are being rolled.
"""
def chanceXPlus(dice, x):
    chance = 0
    if isinstance(dice, tuple):
        dice = list(dice)
    if not isinstance(dice, list):
        dice = [dice]

    if x <= len(dice):
        return 1 # since each die is at least 1, we are guaranteed to roll more than x

    """
    Keep increasing the value of x
    until the dice can no longer sum
    up to x
    """
    added = 1
    while added != 0:
        added = chanceX(dice, x)
        chance += added
        x += 1

    return chance

"""
cartesian products the given
set with itself [power] times
"""
def setPower(set, power):
    return itertools.product(set, repeat=power)

"""
Calculates the chance to roll the given value
with the given dice, then prints the result.

TODO: make this return an array so it can be sorted
"""
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

"""
TODO: use cartesianProduct to run all possible combinations,
then sort them by most to least likely.
"""
def testCombos():
    dice = [4, 6, 8, 10, 20]
    for diceCount in range(1, len(dice) + 1):
        for subset in setPower(dice, diceCount):
            print(type(subset[0]))
            sum = 0
            for die in subset:
                print(die)
                sum += die
            for i in range(1, sum + 1):
                formatChance(subset, i, True)

def testMax():
    dice = [4, 6, 8, 10, 20]
    sum = 0
    for die in dice:
        sum += die
    for i in range(1, sum + 1):
        formatChance(dice, i, True)

def menu():
    dice = []
    val = 0
    ip = " "
    text = """
    Select an option
    1. Run standard tests
    2. Add a die to the set
    3. Set the value to calculate the probability of summing to
    4. Compute probabilities for the given set
    5. Compute cartesian product of standard dice set
    -1. Quit
    """

    while ip != -1:
        print("Current set is " + str(dice))
        print("Current sum to calculate probability for is " + str(val))
        print(text)
        ip = input("Enter an option: ")
        try:
            ip = int(ip)
            if ip == 1:
                testAllSingle()
                testCombos()
                testMax()
            elif ip == 2:
                ip = input("Enter the number of sides on the die to add: ")
                ip = int(ip)
                if 1 <= ip:
                    dice.append(ip)
                else:
                    print("Number of sides must be a positive integer")
                ip = 2
            elif ip == 3:
                ip = input("Enter the number to calculate the probability of summing to: ")
                ip = int(ip)
                if 1 <= ip:
                    val = ip
                else:
                    print("Sum must be a positive integer")
                ip = 3
            elif ip == 4:
                formatChance(dice, val, True)
                dice = []
            elif ip == 5:
                std = [4, 6, 20]
                for set in setPower(std, 5):
                    print(set)
        except ValueError as err:
            print("Invalid input: " + str(ip))

if __name__ == "__main__":
    menu()
