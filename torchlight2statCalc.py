# Credit, stat calculations: torchlight.wikia.com/wiki/Stats_(T2)
# todo: HP and Mana

def perc(num):
    """
    Returns num as a percentage:
    Example:
        perc(0.05) returns
        "5%"
    """
    return str(num * 100) + '%'

def calcWeaponBonus(strength):
    return strength * 0.005

def calcCritMult(strength):
    mult = 1.5
    mult += 0.004 * strength
    if mult > 4.5:
        mult = 4.5
    return mult

def calcCritChance(dexterity):
    chance = 0
    chance += ((0.002002 - 0.000002 * dexterity) * dexterity)
    if chance > 0.5:
        chance = 0.5
    return chance

# n/d
def calcDodgeChance(dexterity):
    chance = 0
    chance += ((0.002002 - 0.000002 * dexterity) * dexterity) # guess
    if chance > 0.75:
        chance = 0.75
    return chance

#n/d    
def calcFumblePen(dexterity):
    return 0

def calcEleBonus(focus):
    return focus * 0.005

#n/d. Cap?
def calcExecuteChance(focus):
    # chance to attack with two weapons at the same time
    chance = 0.098
    chance += ((0.002002 - 0.000002 * focus) * focus)
    
    return chance

def calcArmorBonus(vitality):
    return vitality * 0.0025

def calcBlockChance(vitality):
    chance = ((0.002002 - 0.000002 * vitality) * vitality)
    if chance > 0.75:
        chance = 0.75
    return chance

statFunctions = {
    "Weapon Bonus": calcWeaponBonus,
    "Critical Hit Multiplier": calcCritMult,
    "Critical Hit Chance": calcCritChance,
    "Dodge Chance": calcDodgeChance,
    "Fumble Penalty": calcFumblePen,
    "Elemental Damage Bonus": calcEleBonus,
    "Execute Chance": calcExecuteChance,
    "Armor Bonus": calcArmorBonus,
    "Block Chance": calcBlockChance
}

def calcForValue(functionName, value):
    """
    Calculates how many stat points
    you would need to invest for
    functionName to equal value
    """
    statPoints = 0
    f = statFunctions[functionName]
    while f(statPoints) < value and statPoints < 1000:
        statPoints += 1
    
    print('\n')
    print("In order to have a " + functionName)
    print("value of " + perc(value))
    print("you would have to invest " + str(statPoints))
    print("into its respective stat.")
    print('\n')
    
    return statPoints

def askStatAndValue():
    statList = []
    for stat in statFunctions.keys():
        statList.append(stat)
    inpStat = -1
    while inpStat < 0 or inpStat >= len(statList):
        for i in range(0, len(statList)):
            print("#" + str(i) + ": " + statList[i])
        inpStat = raw_input("Enter the number next to the stat you want to calculate:")
        try:
            inpStat = int(float(inpStat))
        except:
            inpStat = -1
    
    inpVal = -1
    while inpVal < 0:
        inpVal = raw_input("Enter the desired value for that stat: (for example, use 50 for 50%)")
        try:
            inpVal = int(float(inpVal))
        except:
            inpVal = -1
    
    calcForValue(statList[inpStat], float(inpVal) / 100)

def askAndCalcStats():
    statNames = ("strength", "dexterity", "focus", "vitality")
    inp = [0, 0, 0, 0]
    
    for i in range(0, 4):
        inp[i] = float(raw_input("Enter " + statNames[i] + ":"))
    
    displayAllStats(inp[0], inp[1], inp[2], inp[3])
    
#n/d
def displayAllStats(s, d, f, v):
    print("Given stats:")
    print("Strength: " + str(s))
    print("Dexterity: " + str(d))
    print("Focus: " + str(f))
    print("Vitality: " + str(v))
    print(" ")
    
    print("Weapon damage bonus: " + perc(calcWeaponBonus(s)))
    print("Critical hit multiplier: " + perc(calcCritMult(s)))
    print("Critical hit chance: " + perc(calcCritChance(d)))
    print("Dodge chance: " + perc(calcDodgeChance(d)))
    print("Fumble penalty: " + "TODO")
    print("Magic damage bonus: " + perc(calcEleBonus(f)))
    print("Execute chance: " + perc(calcExecuteChance(f)))
    print("Armor bonus: " + perc(calcArmorBonus(v)))
    print("Block chance: " + perc(calcBlockChance(v)))

def run():
    inp = -2
    while inp != -1:
        print("OPTIONS:")
        print("Enter -1 to quit")
        print("Enter 0 to calculate stats based on attribute values")
        print("Enter 1 to calculate attribute values needed for a stat value")
        inp = raw_input("Type your answer and press enter/return")
        
        if inp == "0":
            askAndCalcStats()
        elif inp == "1":
            askStatAndValue()
        else:
            print("GLEHH!")
            inp = -1

run()