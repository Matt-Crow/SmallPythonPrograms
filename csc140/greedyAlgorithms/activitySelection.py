"""
given a set of activities with start and end times, find the maximum number of
activities you can perform without overlapping times.

Choose what to be greedy about:
    fewest overlapping times?
    professor says to sort by finishing time:
        start at start t = 0
        find activity with earliest end time
        remove all other events within that time range
        recur with start t = selected activity's end time

not sure if this works
"""



START_TIME = 0
END_TIME = 1


def test():
    activities = [
        [0, 1],
        [0, 5],
        [1, 4],
        [2, 3],
        [3, 5]
    ]
    print(activities)
    best = maxActivities(activities)
    print(best)
    """
    should be [[0, 1], [2, 3], [3, 5]]
    """

def maxActivities(activities):
    order(activities, 0, len(activities))
    print(activities)
    return impl(activities)

def order(a, min, max): # ... by end time
    if max - min <= 1:
        return

    mid = int((min + max) / 2)
    order(a, min, mid)
    order(a, mid, max)

    merged = []
    i = min
    j = mid
    k = 0
    while i < mid and j < max:
        if a[i][END_TIME] < a[j][END_TIME]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(a[j])
            j += 1
        k += 1

    while i < mid:
        merged.append(a[i])
        i += 1
        k += 1

    while j < max:
        merged.append(a[j])
        j += 1
        k += 1

    for m in range(0, k):
        a[min + m] = merged[m]

def impl(activities):
    print(activities)
    if len(activities) <= 1:
        return activities
    best = activities[0]
    bestHasBeenFound = False
    i = 0
    bestIdx = 0
    while i < len(activities) and not bestHasBeenFound:
        if best[0] < activities[i][0]: # done with this start time TODO is this part incorrect???
            bestHasBeenFound = True
        elif best[1] > activities[i][1]: # another task ends sooner
            best = activities[i]
            bestIdx = i
            i += 1
        else:
            i += 1
    # by now, activities[bestIdx] is the best task
    print(f'best is {activities[bestIdx]}')
    subProblem = []
    for i in range(bestIdx + 1, len(activities)):
        if areCompatible(best, activities[i]):
            subProblem.append(activities[i])
    solvedSubProblem = impl(subProblem)
    solvedSubProblem.append(best)
    return solvedSubProblem



# assume a[0] < a[1] and b[0] < b[1]
def areCompatible(a, b):
    aBeforeB = a[1] <= b[0]
    aAfterB = a[0] >= b[1]
    return aBeforeB or aAfterB


if __name__ == "__main__":
    test()
