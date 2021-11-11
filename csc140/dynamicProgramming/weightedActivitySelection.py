"""
Given a set of activites with start time, end time, and weight, find maximum
total weight for compatible activites

Optimal substructure:
    remove an activity, e, from the solution. This is still the solution to the
    problem if e's time frame didn't exist

Need to solve by finding the best activity to fill each block of time, build up
to larger blocks

Recursive solution:
    T(A, end): # professor goes backward
        if end < 0:
            return []

        choice = A[end]
        i = end - 1
        while i >= 0 and A[i] is not compatible with choice:
            i -= 1
        # by now, i is either -1 or points to the next compatible job
        endIsChosen = T(A, i) union choice
        endNotChosen = T(A, end - 1)
        if total(endIsChosen) < total(endNotChosen):
            return endNotChosen
        else:
            return endIsChosen

"""

class Activity:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __str__(self):
        return f'{self.start} to {self.end}: {self.weight}'

def test():
    activites = [
        Activity(0, 1, 3), # 3
        Activity(1, 3, 2), #  22
        Activity(0, 2, 2), # 22
        Activity(2, 3, 4)  #   4
    ]
    sol = maxWeight(activites) # should be (0, 1, 3) and (2, 3, 4)
    print("Best:")
    printActs(sol)

def maxWeight(activites):
    s = sorted(activites, key=lambda act : act.end)
    printActs(s)
    return memoized(s, len(s) - 1)

# works
def recurImpl(acts, lastIdx):
    if lastIdx < 0:
        return []

    choice = acts[lastIdx]
    compIdx = lastIdx - 1
    while compIdx >= 0 and not areCompatible(choice, acts[compIdx]):
        compIdx -= 1

    # ... what if we choose the last?
    lastChosen = recurImpl(acts, compIdx)
    lastChosen.append(choice)
    # ... and what if we don't?
    lastNotChosen = recurImpl(acts, lastIdx - 1)

    if total(lastChosen) < total(lastNotChosen):
        return lastNotChosen
    return lastChosen

# works
def memoized(acts, lastIdx, cache=None):
    if lastIdx < 0:
        return []

    if cache is None:
        cache = [None for a in acts]
    # cache[i] holds the best choices for acts[0:i]
    if cache[lastIdx] is not None:
        print("cached")
        return cache[lastIdx]

    choice = acts[lastIdx]
    compIdx = lastIdx - 1
    while compIdx >= 0 and not areCompatible(choice, acts[compIdx]):
        compIdx -= 1

    # ... what if we choose the last?
    lastChosen = memoized(acts, compIdx, cache)
    lastChosen.append(choice)
    # ... and what if we don't?
    lastNotChosen = memoized(acts, lastIdx - 1)

    if total(lastChosen) < total(lastNotChosen):
        return lastNotChosen
    else:
        cache[lastIdx] = lastChosen
    return cache[lastIdx]

def areCompatible(a1, a2):
    a1BeforeA2 = a1.end <= a2.start
    a2BeforeA1 = a2.end <= a1.start

    return a1BeforeA2 or a2BeforeA1

def total(acts):
    sum = 0
    for a in acts:
        sum += a.weight
    return sum

def printActs(acts):
    print(", ".join(str(a) for a in acts))

if __name__ == "__main__":
    test()
