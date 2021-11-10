"""
Given a graph, the Distance Vector algorithm finds the shortest path between two
vertices using the following recurrence relation:

T(x, y) = {
    d(x, y) if x => y is an edge
    min({d(x, z) + T(z, y) for each z adjacent to x}) otherwise
}

Find a dynamic programming solution.

each call to T(x, y) relies on call to T(z, y) for each z adj to x. This does
not have any set growing direction, so the typical growth-oriented solution
won't work. Instead, I'll try memoization.

Strategy: start with e, fill it in and pass it down Combine memoization with
          backtracking. May not work, as backtracking finds A SOLUTION not THE
          BEST SOLUTION
"""

def test():
    """
    (0)-5->(1)
     |      |
     2      1
     |      |
     V      V
    (2)-6->(3)
    """
    v = [0, 1, 2, 3]
    e = [
        [0, 5, 2, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 6],
        [0, 0, 0, 0]
    ]
    path = findShortestPath(e, 0, 3)
    print(path) # should be (0, 1, 3) 6

class Path:
    def __init__(self, path, dist):
        self.path = path
        self.dist = dist
    def __str__(self):
        return f'({", ".join((str(n) for n in self.path))}) D: {self.dist}'

def findShortestPathRecur(e, start, end):
    if e[start][end] != 0:
        return Path([start, end], e[start][end]) # direct edge
    best = None
    curr = None
    for a in range(0, len(e)):
        curr = None
        if e[start][a] != 0:
            curr = findShortestPathRecur(e, a, end)
        if best is None:
            best = curr
        elif curr is not None and curr.dist < best.dist:
            best = curr

    if best is not None:
        temp = [start]
        for n in best.path:
            temp.append(n)
        best = Path(temp, best.dist + e[start][best.path[0]])
    return best

# currently has infinite recursion issues
def findShortestPath(e, start, end):
    solution = impl(copy(e), start, end)
    for row in e:
        print(row)
    return solution

def copy(e):
    return [[n for n in row] for row in e]

def impl(e, start, end):
    if e[start][end] != 0:
        return Path([start, end], e[start][end]) # T(1)
    best = None
    curr = None
    for i in range(0, len(e)): # T(|v|)
        curr = None
        if i != start: # don't try and find self-loops
            curr = impl(e, i, end)
            if best is None:
                best = curr
            elif curr is not None and curr.dist < best.dist:
                best = curr
    if best is not None:
        temp = [start]
        for n in best.path:
            temp.append(n)
        best = Path(temp, best.dist + e[start][best.path[0]])
        e[start][end] = best.dist # memoize
    return best

if __name__ == "__main__":
    test()
