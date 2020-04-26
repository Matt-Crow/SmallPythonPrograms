import argparse
import os

"""
Verifies that the given
path points to a csv file,
throwing an exception otherwise.
Returns the absolute path to the
file if path is valid.
"""
def verifyCsv(path):
    path = os.path.abspath(path)
    if not os.path.isfile(path):
        raise ValueError("Argument must be a path to a file.")
    ext = os.path.splitext(path)[1]
    if not ".csv" == ext:
        raise ValueError("Argument must be a path to a csv file.")
    return path

"""
Reads a csv file containing X, Y, and Z coordinates,
and puts them in a 2-D array for O(1) lookup.
"""
def readAs2DArray(inPath):
    verifyCsv(inPath)

    # First, find the maximum and minimum x and y coordinates,
    # and cache the points.
    minX = None
    minY = None
    points = []
    x = 0
    y = 0
    z = 0
    #                            ignore byte order mark
    with open(inPath, mode="rt", encoding="utf-8-sig") as inFile:
        headers = inFile.readline() # pop headers off, maybe verify later
        for line in inFile:
            line = line.strip().split(",")
            if len(line) < 3:
                continue # skip lines with not enough coordinates (such as the last line)
            x = int(float(line[0])) # int method doesn't accept strings
            y = int(float(line[1]))
            z = int(float(line[2]))
            if minX is None or minX > x:
                minX = x
            if minY is None or minY > y:
                minY = y
            points.append((x, y, z))
    # construct the matrix
    matrix = []
    for point in points:
        x = point[0] - minX
        y = point[1] - minY
        # make sure there's room for the new point
        while len(matrix) <= y:
            matrix.append([])
        for row in matrix:
            while len(row) <= x:
                row.append(None)
        # keep the highest point
        if matrix[y][x] is None or matrix[y][x][2] < point[2]:
            matrix[y][x] = point
    return matrix

def getCmdLineArgs():
    desc = """
        Interpolates z coordinates in a csv file.
        This takes a series of 3-D points from a CSV file,
        and converts those points to use integer coordinates.
        It then fills any holes in the resulting point cloud,
        creating a 3-D surface with exactly one point at each
        (x, y) coordinate.
    """
    parser = argparse.ArgumentParser(description=desc, usage="%(prog)s [sourcefile]")
    parser.add_argument("sourcefile", metavar="sourcefile", type=verifyCsv, nargs=1, help="the csv file to interpolate")
    args = parser.parse_args()
    return args

def printMatrix(twoD):
    for line in twoD:
        for column in line:
            if column is None:
                print("  ", end="")
            else:
                print(" " + str(column[2]), end="") #print z-coord
        print("")

"""
approximate
the partial derivative dz/dx
at the point (x, y)
"""
def computeDzDx(matrix, x, y):
    diffInfo = {}

    maxX = len(matrix[0])
    left = x - 1
    right = x + 1
    while left >= 0 and matrix[y][left] is None:
        left -= 1
    if left == -1:
        left = None # no value to the left, so what do I do? Maybe try to find two points to the right of x?

    while right < maxX and matrix[y][right] is None:
        right += 1
    if right == maxX:
        right = None # no value to the right

    if left is not None and right is not None:
        diffInfo["left"] = left
        diffInfo["right"] = right
        dx = right - left
        zLeft = matrix[y][left][2]
        zRight = matrix[y][right][2]
        dz = zRight - zLeft
        diffInfo["dx"] = dx
        diffInfo["dz"] = dz
        diffInfo["dz/dx"] = float(dz) / dx

    return diffInfo

"""
approximate
the partial derivative dz/dy
at the point (x, y)
"""
def computeDzDy(matrix, x, y):
    diffInfo = {}

    maxY = len(matrix)
    top = y - 1
    bottom = y + 1
    while top >= 0 and matrix[top][x] is None:
        top -= 1
    if top == -1:
        top = None

    while bottom < maxY and matrix[bottom][x] is None:
        bottom += 1
    if bottom == maxY:
        bottom = None

    if top is not None and bottom is not None:
        diffInfo["top"] = top
        diffInfo["bottom"] = bottom
        dy = bottom - top
        zTop = matrix[top][x][2]
        zBottom = matrix[bottom][x][2]
        dz = zBottom - zTop
        diffInfo["dy"] = dy
        diffInfo["dz"] = dz
        diffInfo["dz/dy"] = float(dz) / dy

    return diffInfo

"""
https://en.wikipedia.org/wiki/Linear_approximation

Inserts a plane at the point (a, b, z),
with slopes of dz/dx in the x direction,
and dz/dy in the y direction,
and returns the z coordinate of the point on the plane above (x, y)
"""
def tangentPlaneApprox(x, y, a, b, z, dzdx, dzdy):
    xTerm = dzdx * (x - a)
    yTerm = dzdy * (y - b)
    approx = int(z + xTerm + yTerm)
    print("Approx is " + str(approx))
    return approx

"""
interpolate z coordinates into inMatrix
"""
def interpolate(inMatrix):
    rows = len(inMatrix)
    cols = 0 if rows == 0 else len(inMatrix[0])
    for rowNum in range(0, rows):
        for colNum in range(0, cols):
            if inMatrix[rowNum][colNum] is None:
                # perform tangent plane approximation
                print("Dz/Dx " + str(colNum) + ", " + str(rowNum))
                print(computeDzDx(inMatrix, colNum, rowNum))
                print("Dz/Dy " + str(colNum) + ", " + str(rowNum))
                print(computeDzDy(inMatrix, colNum, rowNum))

if __name__ == "__main__":
    args = getCmdLineArgs()
    sfile = args.sourcefile[0]
    matrix = readAs2DArray(sfile)
    print("Input matrix")
    printMatrix(matrix)
    interpolate(matrix)
    print("Output matrix")
    printMatrix(matrix)
