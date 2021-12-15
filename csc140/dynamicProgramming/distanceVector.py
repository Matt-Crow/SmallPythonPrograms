"""
isn't finding the correct path, but distance looks like it works



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

Strategy: start with e, fill it in and pass it down. Combine memoization with
          backtracking. May not work, as backtracking finds A SOLUTION not THE
          BEST SOLUTION

I think the solution must be recursive, as I can't iterate over graph powers, as
the shortest path may not necessarilly have the fewest links.
"""



import random



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

    e2 = [[random.randint(0, 10) % 5 for i in range(10)] for i in range(10)]
    for i in range(0, len(e2)):
        e2[i][i] = 0
    e2[0][9] = 0
    printArray(e2)
    p2 = findShortestPath(e2, 0, 9)
    print(p2)

class Path:
    def __init__(self, path, dist):
        self.path = path
        self.dist = dist
    def __str__(self):
        return f'({", ".join((str(n) for n in self.path))}) D: {self.dist}'

def findShortestPathRecur(e, start, end, visited): # visited must contain start
    if e[start][end] != 0:
        return Path([start, end], e[start][end]) # direct edge
    best = None
    curr = None
    for vertex in range(0, len(e)):
        if vertex not in visited: # avoid infinite loops
            curr = None
            if e[start][vertex] != 0:
                newSet = visited.copy()
                newSet.add(vertex)
                curr = findShortestPathRecur(e, vertex, end, newSet)
            if best is None or (curr is not None and curr.dist < best.dist):
                best = curr

    if best is not None:
        temp = [start]
        for n in best.path:
            temp.append(n)
        best = Path(temp, best.dist + e[start][best.path[0]])
    return best

def findShortestPath(e, start, end):
    for row in e:
        print(row)
    print()
    newEdges = copy(e)
    solution = impl(newEdges, start, end, set([start]))
    for row in newEdges:
        print(row)
    return solution

def copy(e):
    return [[n for n in row] for row in e]

# memoized
def impl(e, start, end, visited):
    if e[start][end] != 0:
        return Path([start, end], e[start][end]) # T(1)
    best = None
    curr = None
    for i in range(0, len(e)): # T(|v|)
        curr = None
        if i != start and i not in visited: # don't try and find self-loops
            newSet = visited.copy()
            newSet.add(i)
            curr = impl(e, i, end, newSet)
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

def printArray(arr):
    for a in arr:
        print(a)


if __name__ == "__main__":
    test()
