"""
Given a collection of points, find the two that are closest to each other

Doesn't work
"""


import random
import math



def test():
    pts = createRandomPoints(3)
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
    return pts

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
