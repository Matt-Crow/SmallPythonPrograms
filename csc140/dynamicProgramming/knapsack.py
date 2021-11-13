"""
given a set of items, each having a weight and value, maximize total value when
weight cannot exceed a given value

be greedy over value density: value / weight? nope. But this is correct for
"fractional knapsack"
apparently, this problem is not solveable by greedy algorithms
BUUUT it's solveable via dynamic programming!

Optimal Substructure:
    given a set of items, I, and a total allowed weight, W, the solution to the
    optimal subset of items is solution = (i + solution(W - i)), where i is the
    optimal choice

recursive solution:
I is sorted by weight
f(I, W),
    if I is empty,
        return {}
    while |I| is not 0 and I[0].w > W,
        remove first element from I
    chooseFirst = {I[0] + f(I[1...], W - I[0].w)}
    notChooseFirst = f(I[1...], W)

    if totalValue(chooseFirst) < totalValue(notChooseFirst),
        return notChooseFirst
    return chooseFirst

"""

def test():
    items = [
        Item(1, 1),
        Item(6, 2),
        Item(18, 5),
        Item(22, 6),
        Item(28, 7)
    ]
    print(f'All: {", ".join((str(item) for item in items))}')
    choices = chooseItems(items, 11)
    print(f'Best: {", ".join((str(item) for item in choices))} (total: {total(choices)})')

class Item:
    def __init__(self, value, weight):
        self.v = value
        self.w = weight

    def __repr__(self):
        return f'({self.v}, {self.w})'

def chooseItems(items, maxWeight):
    items = sorted(items, key=lambda item : item.w)
    print(f'Sorted: {", ".join((str(item) for item in items))}')
    return dynamic(items, maxWeight)

# works
def recurImpl(items, start, maxWeight):
    # find first item that fits
    i = start
    while i < len(items) and items[i].w > maxWeight:
        i += 1

    if i >= len(items):
        return [] # nothing remaining fits

    # compare values for choosing or not choosing items[i]
    choice = items[i]
    isChosen = [choice]
    for otherItem in recurImpl(items, i + 1, maxWeight - choice.w): # choose remaining
        isChosen.append(otherItem)
    isNotChosen = recurImpl(items, i + 1, maxWeight)

    if total(isChosen) < total(isNotChosen):
        return isNotChosen
    return isChosen

def total(items):
    sum = 0
    for item in items:
        sum += item.v
    return sum

# works
def memoized(items, start, maxWeight, cache=None):
    if start >= len(items):
        return []

    if cache is None: # cache[i][w] = best solution for start = i and maxWeight = w
        cache = [[None for i in range(0, maxWeight + 1)] for item in items]
    elif cache[start][maxWeight] is not None:
        return cache[start][maxWeight]

    # find first item that fits
    i = start
    while i < len(items) and items[i].w > maxWeight:
        i += 1

    solution = None
    if i >= len(items):
        solution = [] # nothing remaining fits
    else:
        # compare values for choosing or not choosing items[i]
        choice = items[i]
        isChosen = [choice]
        for otherItem in memoized(items, i + 1, maxWeight - choice.w, cache): # choose remaining
            isChosen.append(otherItem)
        isNotChosen = memoized(items, i + 1, maxWeight, cache)

        if total(isChosen) < total(isNotChosen):
            solution = isNotChosen
        else:
            solution = isChosen
    cache[start][maxWeight] = solution
    #print(cache)
    return solution

# works
def dynamic(items, maxWeight):
    if len(items) == 0 or maxWeight <= 0:
        return []

    """
    index i, j is the ideal solution using items[0...i] and maxWeight = j
    """
    solutions = [[[] for i in range(maxWeight + 1)] for item in items]
    totals = [[None for i in range(maxWeight + 1)] for item in items]

    for i in range(0, len(items)):
        solutions[i][0] = [] # no choices when maxWeight = 0
        totals[i][0] = 0
    for j in range(1, maxWeight + 1):
        if items[0].w <= j: # first item is best when it's the only item
            solutions[0][j] = [items[0]]
            totals[0][j] = items[0].w

    for i in range(1, len(items)):
        for j in range(1, maxWeight + 1):
            if items[i].w > j: # current item cannot fit
                solutions[i][j] = solutions[i - 1][j]
                totals[i][j] = totals[i - 1][j]
            elif totals[i - 1][j] < totals[i - 1][j - items[i].w] + items[i].v: # better to choose this
                solutions[i][j] = solutions[i - 1][j - items[i].w]
                solutions[i][j].append(items[i])
                totals[i][j] = totals[i - 1][j - items[i].w] + items[i].v
            else: # better not to choose this
                solutions[i][j] = solutions[i - 1][j]
                totals[i][j] = totals[i - 1][j]
    for line in totals:
        print(line)
    return solutions[len(items) - 1][maxWeight]



if __name__ == "__main__":
    test()
