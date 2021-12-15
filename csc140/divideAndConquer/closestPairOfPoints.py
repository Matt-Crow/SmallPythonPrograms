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
    pts = createRandomPoints(4)
    for p in pts:
        print(p)
    closestByBruteForce = solveBruteForce(pts)
    print(f'By brute force, the closest points are {closestByBruteForce[0]} and {closestByBruteForce[1]} ({dist(closestByBruteForce[0], closestByBruteForce[1])})')
    closest = closestPoints(pts);
    print(f'By divide and conquer, the closest points are {closest[0]} and {closest[1]} ({dist(closest[0], closest[1])})')

def createRandomPoints(n):
    pts = []
    for i in range(n):
        pts.append((random.randint(0, 10), random.randint(0, 10)))
    return pts

def solveBruteForce(pts):
    a = pts[0]
    b = pts[1]
    d = dist(a, b)
    for p1 in pts:
        for p2 in pts:
            temp = dist(p1, p2)
            if p1 is not p2:
                print(f'{p1} -> {p2} = {temp}')
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
    # sort first by y-coordinate...
    sortedByY = sorted(pts, key=lambda point: point[1]) # theta(nlogn) probably
    # ... then by x-coordinate ...
    sortedByX = sorted(sortedByY, key=lambda point: point[0]) # theta(nlogn) probably
    # ... then remove duplicates
    unduped = []
    i = 0
    j = 1
    max = len(sortedByX)
    while j < max:
        # find end of current range of x
        while j < max and sortedByX[i][0] == sortedByX[j][0]:
            j += 1
        # sortedByX[i...j] exclusive of end all have the same x-coord
        dupe = False
        for t1 in range(i, j):
            dupe = False
            for t2 in range(t1 + 1, j):
                if sortedByX[t1][1] == sortedByX[t2][1]:
                    dupe = True
                    t2 = j # break
            if not dupe:
                unduped.append(sortedByX[t1])
        i = j
        j += 1
    print(f'sorted: {unduped}')
    return recur(unduped, 0, len(unduped)) # don't use any other len

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

def impl(pts):
    if len(pts) <= 2:
        return pts
    # divide into 2 regions
    minX = None
    maxX = None
    for pt in pts:
        if minX is None or minX > pt[0]:
            minX = pt[0]
        if maxX is None or maxX < pt[0]:
            maxX = pt[0]
    midX = int((minX + maxX) / 2)
    left = []
    right = []
    for pt in pts:
        if pt[0] <= midx:
            left.append(pt)
        else:
            right.append(pt)

    # find closest points within each region
    closestLeft = impl(left)
    closestRight = impl(right)
    leftD = dist(closestLeft[0], closestLeft[1])
    rightD = dist(closestRight[0], closestRight[0])
    delta = min(leftD, rightD)
    # find closest pair of points where 1 point is in each region
    closestSplit = None
    splitD = None
    """
    only bother checking points that are closer to the line than closestLeft
    and closestRight's pairs are to each other
    """
    closeToLineLeft = []
    for pt1 in left:
        #      dist to line
        if midX - pt1[0] < delta:
            closeToLineLeft.append(pt1)
    closeToLineRight = []
    for pt2 in right:
        if pt2[0] - midX < delta:
            closeToLineRight.append(pt2)

    # todo: sort pt1 and pt2 by y-coordinate
    # only bother comparing pts whose addresses are at most delta appart Theta(n)
    # says to create 2 arrays of pts: one sorted by x, one sorted by y, pass that to function
    # then merge those arrays or something

    m = min(leftD, rightD, splitD)
    if m == leftD:
        return closestLeft
    if m == rightD:
        return closestRight
    return closestSplit


if __name__ == "__main__":
    test()
