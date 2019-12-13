from graphs import Graph, graphFromFile

class EdgeMinHeap:
    def __init__(self):
        self.a = []

    def siftUp(self, start, end, weight):
        self.a.append([start, end, weight])
        idx = len(self.a) - 1
        parent = int(idx / 2)
        while idx > 0 and self.a[idx] < self.a[parent]:
            self.print()
            temp = self.a[parent]
            self.a[parent] = self.a[idx]
            self.a[idx] = temp
            idx = parent
            parent = int(idx / 2)
        self.print()

    def print(self):
        depth = 1
        breadth = 0
        s = ""
        print("(start, end, weight)")
        for i in range(1, len(self.a)):
            s += "(" + str(self.a[i][0]) + ", " + str(self.a[i][1]) + ", " + str(self.a[i][2]) + ")"
            breadth += 1
            if breadth == 2 ** depth:
                print(s)
                s = ""
                breadth *= 2
                depth += 1
        print(s)

def prims(graph, start):
    minSpanTree = Graph()
    heap = EdgeMinHeap()

    minSpanTree.addVertex(start)
    for edge in graph.getAdjEdges(start):
        heap.siftUp(edge[0], edge[1], edge[2])

    return minSpanTree

if __name__ == "__main__":
    g = graphFromFile("vertices.txt", "edges.txt")
    prims(g, 1)
