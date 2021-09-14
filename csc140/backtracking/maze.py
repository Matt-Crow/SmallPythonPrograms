"""
Given a 2-d array as a maze, finds a path from the upper-left corner to the
lower right
"""


OPEN = "."
WALL = "#"
EXPLORED = "X"
PATH = "P"

def solveMaze(x, y, maze):
    if x == len(maze[y]) - 1 and y == len(maze) - 1:
        maze[y][x] = PATH
        printMaze(maze)
        return True

    maze[y][x] = PATH
    printMaze(maze)
    foundExit = False

    if y - 1 >= 0 and maze[y - 1][x] is OPEN:
        # don't copy maze: need to pass by reference
        foundExit = solveMaze(x, y - 1, maze)
    if not foundExit and x - 1 >= 0 and maze[y][x - 1] is OPEN:
        foundExit = solveMaze(x - 1, y, maze)
    if not foundExit and y + 1 < len(maze) and maze[y + 1][x] is OPEN:
        foundExit = solveMaze(x, y + 1, maze)
    if not foundExit and x + 1 < len(maze[y]) and maze[y][x + 1] is OPEN:
        foundExit = solveMaze(x + 1, y, maze)

    if not foundExit:
        maze[y][x] = EXPLORED # mark unsuccessfull path

    return foundExit



def printMaze(maze):
    print("MAZE")
    for row in maze:
        print(f'\t{"".join(row)}')

if __name__ == "__main__":
    found = solveMaze(0, 0, [
        [OPEN, OPEN, OPEN],
        [OPEN, WALL, OPEN],
        [WALL, WALL, OPEN]
    ])
    print(found)
