symbols = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z"
]

word = input("Enter phrase to decipher: ")
broken = [char.upper() for char in word];
print(broken)

for i in range(1, len(symbols)):
    newStr = ""
    for char in broken:
        if char in symbols:
            newStr += symbols[(symbols.index(char) + i) % len(symbols)]
        else:
            newStr += "_"
    print(newStr)

