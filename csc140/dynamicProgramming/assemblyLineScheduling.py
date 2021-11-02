"""
given two assembly lines, each with n stations
corresponding stations perform the same operation, but may take different
amounts of time
can switch from one line to the other at a time cost

Problem: which pattern of assembly line stations to run through to minimize time

min time to get to station[n] relies on min time to station[n - 1] in either
branch

IT WORKS!!!
FOR CRYING OUT LOUD I'VE FINALLY SOLVED ONE OF THESE THINGS!!!

decoding route wrong
"""



def test():
    line1 =  [1, 2, 3, 9] # 15 time units to build
    line2 =  [4, 7, 1, 3] # 15 time units to build
    switchFrom1 = [0, 1, 10, 1]
    switchFrom2 = [0, 5, 5, 5]
    print(line1)
    print(line2)
    print(switchFrom1)
    print(switchFrom2)
    """
    ideal pattern is
    1 2 3
          1
          3
    total 10, path 1112
    """
    solution = solve(line1, line2, switchFrom1, switchFrom2)
    print(f'fastest time takes {solution["total"]} units of time {solution["route"]}')

def solve(line1, line2, switchFrom1, switchFrom2):
    last = len(line1)
    # cache best times it takes to reach each point in the line
    bestTimes1 = [line1[0]]
    prev1 = []
    bestTimes2 = [line2[0]]
    prev2 = []
    for i in range(1, last):
        stay1 = bestTimes1[i - 1]
        from2To1 = bestTimes2[i - 1] + switchFrom2[i]

        stay2 = bestTimes2[i - 1]
        from1To2 = bestTimes1[i - 1] + switchFrom1[i]

        if stay1 < from2To1:
            prev1.append(1) # came from 1
            bestTimes1.append(stay1 + line1[i])
        else:
            prev1.append(2)
            bestTimes1.append(from2To1 + line1[i])
        if stay2 < from1To2:
            prev2.append(2)
            bestTimes2.append(stay2 + line2[i])
        else:
            prev2.append(1)
            bestTimes2.append(from1To2 + line2[i])
    prev1.append(1)
    prev2.append(2)
    print(bestTimes1, bestTimes2)
    print(prev1, prev2)


    ret = dict()
    ret["route"] = []
    curr = None
    if bestTimes1[last - 1] < bestTimes2[last - 1]:
        curr = 1
        ret["total"] = bestTimes1[last - 1]
    else:
        curr = 2
        ret["total"] = bestTimes2[last - 1]
    for i in range(last - 1, 0, -1):
        ret["route"].insert(0, curr)
        if curr == 1:
            curr = prev1[i]
        else:
            curr = prev2[i]

    return ret

if __name__ == "__main__":
    test()
