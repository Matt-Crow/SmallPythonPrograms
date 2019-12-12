"""
Calculates the chance of rolling specific numbers or higher
using a set of dice (d4, d6, d20, etc)
"""

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
Computes every possible combination
of terms from set1 and set2
"""
def cartesianProduct(set1, set2):
    pass

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
    dice = [4, 6]
    for die1 in dice:
        for die2 in dice:
            for sum in range(1, die1 + die2 + 1):
                if die1 != die2:
                    formatChance(dice, sum, True)
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
        except:
            print("Invalid input: " + ip)

if __name__ == "__main__":
    menu()
