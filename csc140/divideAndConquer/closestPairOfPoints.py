"""
Given a collection of points, find the two that are closest to each other

Doesn't work yet

Idea:
    draw a line through the plane
    find the two points closest to each other on the left side using recursion
    find the two points closest to each other on the right side using recursion
    find the two points, one on each side of the line, closest to each other
    return 1 of these 3 based on which pair has the smallest distance between its points
"""


import random
import math



def test():
    pts = createRandomPoints(1000)
    pts = unduped(pts)
    for p in pts:
        pass
        #print(p)
    closestByBruteForce = solveBruteForce(pts)
    print(f'By brute force, the closest points are {closestByBruteForce[0]} and {closestByBruteForce[1]} ({dist(closestByBruteForce[0], closestByBruteForce[1])})')
    closest = closestPoints(pts);
    print(f'By divide and conquer, the closest points are {closest[0]} and {closest[1]} ({dist(closest[0], closest[1])})')
    return dist(closestByBruteForce[0], closestByBruteForce[1]) - dist(closest[0], closest[1])

def createRandomPoints(n):
    pts = []
    for i in range(n):
        pts.append((random.randint(0, 10), random.randint(0, 10)))
    return pts

def unduped(pts):
    # sorted is a stable sort, so this sorts by y, then by x properly
    # sort first by y-coordinate...
    sortedByY = sorted(pts, key=lambda point: point[1]) # theta(nlogn) probably
    # ... then by x-coordinate ...
    sortedByX = sorted(sortedByY, key=lambda point: point[0]) # theta(nlogn) probably
    # ... then remove duplicates
    unduped = [sortedByX[0]]
    i = 0
    for j in range(1, len(sortedByX)):
        if unduped[i][0] != sortedByX[j][0] or unduped[i][1] != sortedByX[j][1]:
            unduped.append(sortedByX[j])
            i += 1
    #print(f'sorted: {unduped}')
    return unduped

def solveBruteForce(pts):
    a = pts[0]
    b = pts[1]
    d = dist(a, b)
    for p1 in pts:
        for p2 in pts:
            temp = dist(p1, p2)
            if p1 is not p2:
                pass
                #print(f'{p1} -> {p2} = {temp}')
            if temp < d and p1 is not p2:
                a = p1
                b = p2
                d = temp
    return [a, b]

def dist(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return math.sqrt(dx * dx + dy * dy)

def closestPoints(pts):
    if len(pts) < 2:
        return None

    return recur(pts, 0, len(pts))

def recur(pts, minIdx, maxIdx):
    if maxIdx - minIdx < 2:
        return None # need at least 2 points to compare
    if maxIdx - minIdx == 2:
        return (pts[minIdx], pts[maxIdx - 1]) # if only 2 pts, first and last are closest

    midIdx = int((minIdx + maxIdx) / 2)
    closestLeft = recur(pts, minIdx, midIdx)
    closestRight = recur(pts, midIdx, maxIdx)
    # both of these cannot be None, as that would mean each contains only 1 point
    # already checked for only 2 points

    distLeft = math.inf if closestLeft is None else dist(closestLeft[0], closestLeft[1])
    distRight = math.inf if closestRight is None else dist(closestRight[0], closestRight[1])

    delta = min(distLeft, distRight) # this is finite
    lineX = pts[midIdx][0]
    """
    pts[min...mid] are on the left of the line
    pts[mid...max] are on the right
    don't compare every point on the left to every one on the right
    the only way two points, each on one side of the line, can be closer to each
    other than closestLeft and closestRight is if they are within a distance
    delta of the line.

    A..B|...C
    ....|D...
    ....|....
    E...|...F

    closestLeft = (A, E) 2 dist
    closestRight = (C, F) 2 dist
    A, E, C, and F are all 3 dist from the line, so they are at the minimum 3
    away from a point on the other side of the line
    """
    subsetLeft = []
    subsetRight = []
    for i in range(minIdx, midIdx): # theta(n)
        if abs(pts[i][0] - lineX) < delta:
            subsetLeft.append(pts[i])
    for i in range(midIdx, maxIdx): # theta(n)
        if abs(pts[i][0] - lineX) < delta:
            subsetRight.append(pts[i])

    closestSplit = None
    distSplit = math.inf

    for pt1 in subsetLeft: # theta(n^2), but C is small here
        for pt2 in subsetRight:
            # pt1 can = pt2 if duplicate points TODO no dupes
            if dist(pt1, pt2) < distSplit:
                closestSplit = (pt1, pt2)
                distSplit = dist(pt1, pt2)

    bestDist = min(distLeft, distRight, distSplit)
    if bestDist == distLeft:
        return closestLeft
    if bestDist == distRight:
        return closestRight
    return closestSplit

if __name__ == "__main__":
    ret = 0
    i = 1
    while ret == 0 and i <= 100:
        ret = test()
        msg = 'succeeded' if ret is not 0 else 'failed'
        print(f'Test #{i} {msg}')
        i += 1
    #test()
