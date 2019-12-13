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
            parent = int((idx - 1) / 2)
        self.print()

    def siftDown(self):
        if len(self.a) == 0:
            throw Error("Heap is empty, cannot sift down")
        ret = self.a[0]
        self.a[0] = self.a[len(self.a) - 1]
        self.a.pop()

        idx = 0
        l = 1
        r = 2
        while (l < len(self.a) and self.a[l][2] < self.a[idx][2]) or (r < len(self.a) and self.a[r][2] < self.a[idx][2]):
            self.print()
            if self.a[l][2] > self.a[r][2]:
                temp = self.a[r]
                self.a[r] = self.a[idx]
                self.a[idx] = temp
                idx = r
            else:
                temp = self.a[l]
                self.a[l] = self.a[idx]
                self.a[idx] = temp
                idx = l
            l = 2 * idx + 1
            r = 2 * idx + 1

        self.print()

        return ret

    def isEmpty(self):
        return len(self.a) == 0

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
    unvisited = []
    visited = dict()

    minSpanTree.addVertex(start)
    visited[start] = True

    for edge in graph.getAdjEdges(start):
        heap.siftUp(edge[0], edge[1], edge[2])
        unvisited.append(edge[1])

    # not done

    return minSpanTree

if __name__ == "__main__":
    g = graphFromFile("vertices.txt", "edges.txt")
    prims(g, 1)
