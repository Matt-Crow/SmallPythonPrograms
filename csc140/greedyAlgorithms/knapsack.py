"""
given a set of items, each having a weight and value, maximize total value when
weight cannot exceed a given value

be greedy over value density: value / weight? nope. But this is correct for
"fractional knapsack"
apparently, this problem is not solveable by greedy algorithms
"""

def test():
    items = [
        Item(0, 1),
        Item(9, 10),
        Item(4, 4),
        Item(5, 6),
        Item(1, 1)
    ]
    print(f'All: {", ".join((str(item) for item in items))}')
    choices = chooseItems(items, 10)
    print(f'Best: {", ".join((str(item) for item in choices))}') # should be 9,10 and 1,1

class Item:
    def __init__(self, value, weight):
        self.v = value
        self.w = weight
        self.d = value / weight

    def __repr__(self):
        return f'({self.v}, {self.w}, {self.d})'

def chooseItems(items, maxWeight):
    sortByDensity(items)
    print(f'Sorted: {", ".join((str(item) for item in items))}')
    return chooseItemsImpl(items, 0, maxWeight)

def chooseItemsImpl(items, startIdx, maxWeight):
    bestIdx = startIdx
    while bestIdx < len(items) and items[bestIdx].w > maxWeight:
        bestIdx += 1 # cannot carry current item
    if bestIdx == len(items):
        return [] # can't carry anything else

    # bestIdx now points to item with best density
    choices = chooseItemsImpl(items, bestIdx + 1, maxWeight - items[bestIdx].w)
    choices.append(items[bestIdx])
    return choices



# highest density first
def sortByDensity(items):
    sortByDensityImpl(items, 0, len(items))

def sortByDensityImpl(items, min, max):
    if max - min <= 1:
        return;

    mid = int((min + max) / 2)
    sortByDensityImpl(items, min, mid)
    sortByDensityImpl(items, mid, max)

    merged = []
    i = min
    j = mid
    while i < mid and j < max:
        if items[i].d < items[j].d:
            merged.append(items[j])
            j += 1
        else:
            merged.append(items[i])
            i += 1

    while i < mid:
        merged.append(items[i])
        i += 1

    while j < max:
        merged.append(items[j])
        j += 1

    for k in range(0, max - min):
        items[min + k] = merged[k]

if __name__ == "__main__":
    test()
