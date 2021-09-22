import random
import math

# works for 3x3 and 9x9

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
    return impl(suduku, 0, 0)

def impl(suduku, x, y):
    solution = None
    if y == SIZE: # past last row
        solution = suduku

    num = 1
    while num <= SIZE and solution is None:
        if canPlace(num, x, y, suduku) or suduku[y][x] == num: # cell already set
            copy = copySuduku(suduku)
            copy[y][x] = num
            print()
            printSuduku(copy)
            if x + 1 == SIZE: # outside of row
                solution = impl(copy, 0, y + 1)
            else:
                solution = impl(copy, x + 1, y)
        num = num + 1


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
    solveable = [
        [5, 3, 0,  0, 7, 0,  0, 0, 0],
        [6, 0, 0,  1, 9, 5,  0, 0, 0],
        [0, 9, 8,  0, 0, 0,  0, 6, 0],

        [8, 0, 0,  0, 6, 0,  0, 0, 3],
        [4, 0, 0,  8, 0, 3,  0, 0, 1],
        [7, 0, 0,  0, 2, 0,  0, 0, 6],

        [0, 6, 0,  0, 0, 0,  2, 8, 0],
        [0, 0, 0,  4, 1, 9,  0, 0, 5],
        [0, 0, 0,  0, 8, 0,  0, 7, 9]
    ]
    unsolveable = [
        [0, 0, 0,  0, 0, 0,  0, 0, 1],
        [0, 0, 0,  0, 0, 0,  0, 0, 1],
        [0, 0, 0,  0, 0, 0,  0, 0, 1],

        [0, 0, 0,  0, 0, 0,  0, 0, 1],
        [0, 0, 0,  0, 0, 0,  0, 0, 1],
        [0, 0, 0,  0, 0, 0,  0, 0, 1],

        [0, 0, 0,  0, 0, 0,  0, 0, 1],
        [0, 0, 0,  0, 0, 0,  0, 0, 1],
        [0, 0, 0,  0, 0, 0,  0, 0, 1]
    ]
    #problem = unsolveable
    printSuduku(problem)
    solution = solveSuduku(problem)
    if solution is not None:
        print("solution:")
        printSuduku(solution)
    else:
        print("No solution :(")
