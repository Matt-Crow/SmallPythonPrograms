import random


def test(n):
    a = createArray(n)
    #print(a)
    dupe = checkForDupes(a)
    if dupe is None:
        print("no duplicates")
    else:
        print(f'Duplicate: {dupe}')

def createArray(n):
    a = []
    for i in range(n):
        a.append(random.randint(-255, 256))
    return a

# theta(n)
def checkForDupes(a):
    s = set()
    dupe = None
    i = 0
    while dupe is None and i < len(a):
        n = a[i]
        if n in s:
            dupe = n
        s.add(n)
        i += 1
    return dupe

if __name__ == "__main__":
    test(1000)
