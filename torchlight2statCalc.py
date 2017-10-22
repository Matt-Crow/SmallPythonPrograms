# Credit, stat calculations: torchlight.wikia.com/wiki/Stats_(T2)
# todo: HP and Mana
# is calcing wrong?

# this works
def perc(num):
    """
    Returns num as a percentage:
    Example:
        perc(0.05) returns
        "5%"
    deletes decimal:
        perc(0.041) returns
        "4%", not "4.1%"
    """
    return str(int(num * 100)) + '%'

def calcWeaponBonus(strength):
    return strength * 0.5

def calcCritMult(strength):
    mult = 1.5
    mult += 0.04 * strength
    if mult > 4.5:
        mult = 4.5
    return mult
#n/d
def calcDodgeChance(dexterity):
    chance = 0 # what base?
    if chance > 0.75:
        chance = 0.75
    return chance

#n/d
def calcCritChance(dexterity):
    chance = 0 #what is base?
    chance += ((0.2002 - 0.0002 * dexterity) * dexterity)
    if chance > 0.5:
        chance = 0.5
    return chance

#n/d    
def calcFumblePen(dexterity):
    return

#n/d
def calcEleBonus(focus):
    return

#n/d. Cap?
def calcExecuteChance(focus):
    # chance to attack with two weapons at the same time
    chance = 0.098
    chance += ((0.2002 - 0.0002 * focus) * focus)
    
    return chance

#n/d
def calcArmorBonus(vitality):
    return

def calcBlockChance(vitality):
    chance = ((0.2002 - 0.0002 * vitality) * vitality)
    if chance > 0.75:
        chance = 0.75
    return chance

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
    print("Block chance: " + perc(calcBlockChance(v)))

def run():
    statNames = ("strength", "dexterity", "focus", "vitality")
    inp = [0, 0, 0, 0]
    
    for i in range(0, 4):
        inp[i] = float(raw_input("Enter " + statNames[i] + ":"))
    
    displayAllStats(inp[0], inp[1], inp[2], inp[3])

run()