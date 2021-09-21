import random
import math

# works for 3x3, but not 9x9 yet
# keeps trying the same solutions over and over


SIZE = 9

def createSuduku():
    board = []
    for i in range(0, SIZE):
        row = []
        for j in range(0, SIZE):
            row.append(0)
        board.append(row)

    # populate
    for num in range(0, SIZE):
        row = random.randint(0, SIZE) % SIZE
        col = random.randint(0, SIZE) % SIZE
        board[row][col] = num + 1

    return board

def printSuduku(suduku):
    for row in suduku:
        print(row, sep=" ")

def copySuduku(suduku):
    return [[col for col in row] for row in suduku]

def solveSuduku(suduku):
    return impl(suduku, 1)

def impl(suduku, num):
    solution = None

    if isFilled(suduku):
        solution = suduku
    elif count(suduku, num) == SIZE:
        print(num)
        printSuduku(suduku)
        #input()
        solution = impl(suduku, num + 1)

    # find all places for num
    row = 0
    while row < SIZE and solution is None:
        if num not in suduku[row]:
            col = 0
            while col < SIZE and solution is None:
                if canPlace(num, col, row, suduku):
                    copy = copySuduku(suduku)
                    copy[row][col] = num
                    solution = impl(copy, num)
                col = col + 1
        row = row + 1

    return solution

def canPlace(num, i, j, suduku):
    isOccupied = suduku[j][i] is not 0
    inRow = num in suduku[j]

    inCol = False
    for row in suduku:
        if row[i] == num:
            inCol = True

    inGroup = False
    groupSize = math.floor(math.sqrt(SIZE))
    groupX = int(i / groupSize)
    groupY = int(j / groupSize)
    for dx in range(0, groupSize):
        for dy in range(0, groupSize):
            if suduku[groupY * groupSize + dy][groupX * groupSize + dx] == num:
                inGroup = True

    return not (isOccupied or inRow or inCol or inGroup)

def isFilled(suduku):
    b = True
    i = 0
    j = 0
    while i < SIZE and b:
        j = 0
        while j < SIZE and b:
            if suduku[i][j] == 0:
                b = False
            j = j + 1
        i = i + 1
    return b

def count(suduku, num):
    total = 0
    for row in suduku:
        if num in row:
            total = total + 1
    return total

if __name__ == "__main__":
    problem = createSuduku()
    printSuduku(problem)
    solution = solveSuduku(problem)
    if solution is not None:
        print("solution:")
        printSuduku(solution)
    else:
        print("No solution :(")
