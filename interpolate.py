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

def interpolate(inputFilePath, outputFilePath):
    inF = open(inputFilePath, mode="r", encoding="utf-8-sig")
    outF = open(outputFilePath, mode="w")
    containsRGB = True
    error = False
    try:
        firstLine = inF.readline().strip()
        #print(firstLine)
        containsRGB = "r" in firstLine.lower()
    except Exception as e:
        print("Error while reading file: " + str(e))

    if not error:
        # oh wait, I do need to cache lines to compute partial derivatives across multiple axes
        fLines = []
        minX = None
        minY = None
        for line in inF:
            if "x" in line:
                continue # skip first line if it hasn't been read yet
            line = line.strip().replace(",", " ") # FME output doesn't contain commas, so make sure all data stays that way
            if not containsRGB:
                line = line + " 0 0 0"
            line = line.split(" ")
            newline = [];
            # all lines should contain 6 cells now
            x = int(float(line[0]))
            y = int(float(line[1]))
            z = int(float(line[2]))
            if minX == None or minX > x:
                minX = x
            if minY == None or minY > y:
                minY = y
            newline.extend([x, y, z])
            newline.extend(line[3:6])
            fLines.append(newline)
        twoD = []
        for line in fLines:
            newX = line[0] - minX
            newY = line[1] - minY
            # Make sure there is a spot in the twoD array for the new coordinate
            while len(twoD) <= newY:
                newRow = []
                if len(twoD) is not 0:
                    for i in range(0, len(twoD[0])):
                        newRow.append(None)
                twoD.append(newRow)
            while len(twoD[0]) <= newX:
                for row in twoD:
                    row.append(None)
            twoD[newY][newX] = line # need to preserve not only z, but color as well
        printMatrix(twoD)

        # shift everything to (0,0) being the lowest xy coordinate. Use 2D array for O(1) lookup
        # interpolate, write to output file (don't forget "x y z r g b"!) also, shift everything back to old coordinate system
    inF.close()
    outF.close()

if __name__ == "__main__":
    args = getCmdLineArgs()
    sfile = args.sourcefile[0]
    print("Source file is " + sfile)
    readAs2DArray(sfile)
