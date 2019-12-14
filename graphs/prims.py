from graphs import Graph, graphFromFile

class EdgeMinHeap:
    def __init__(self):
        self.a = []

    def siftUp(self, start, end, weight):
        self.a.append([start, end, weight])
        idx = len(self.a) - 1
        parent = int(idx / 2)
        while idx > 0 and self.a[idx][2] < self.a[parent][2]:
            #self.print()
            temp = self.a[parent]
            self.a[parent] = self.a[idx]
            self.a[idx] = temp
            idx = parent
            parent = int((idx - 1) / 2)
        #self.print()

    def siftDown(self):
        if len(self.a) == 0:
            raise Exception("Heap is empty, cannot sift down")
        ret = self.a[0]
        self.a[0] = self.a[len(self.a) - 1]
        self.a.pop()

        idx = 0
        l = 1
        r = 2
        while (0 <= l < len(self.a) and self.a[l][2] < self.a[idx][2]) or (0 <= r < len(self.a) and self.a[r][2] < self.a[idx][2]):
            #self.print()
            if r < len(self.a) and self.a[l][2] > self.a[r][2]:
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

        #self.print()

        return ret

    def isEmpty(self):
        return len(self.a) == 0

    def print(self):
        depth = 0
        breadth = 0
        s = ""
        print("HEAP IS")
        print("(start, end, weight)")
        for i in range(0, len(self.a)):
            s += "(" + str(self.a[i][0]) + ", " + str(self.a[i][1]) + ", " + str(self.a[i][2]) + ")"
            breadth += 1
            if breadth == 2 ** depth:
                print(s)
                s = ""
                breadth = 0
                depth += 1
        print(s)
        print("END HEAP")

def prims(graph, start):
    print("Finding minimum spanning tree")
    graph.print()

    minSpanTree = Graph()
    heap = EdgeMinHeap()
    visited = dict()
    for vertex in graph.getVertices():
        visited[vertex] = False

    minSpanTree.addVertex(start)
    visited[start] = True

    print("Adding edges adjacent to initial vertex to potential edges")
    for edge in graph.getAdjEdges(start):
        heap.siftUp(edge[0], edge[1], edge[2])
    heap.print()

    done = heap.isEmpty()
    while not done:
        print("Sifting down to find shortest edge with an unvisited destination")
        heap.print()
        top = heap.siftDown()
        found = not visited[top[1]] # top.to
        done = heap.isEmpty()
        heap.print()
        while not found and not done:
            top = heap.siftDown()
            found = not visited[top[1]]
            heap.print()
            if heap.isEmpty():
                done = True

        if not found:
            break
        print(str(top) + " is a valid edge. Adding to MST")
        visited[top[1]] = True
        minSpanTree.addVertex(top[1])
        minSpanTree.addEdge(top[0], top[1], top[2])
        print("Adding edges adjacent to " + str(top[1]) + " to potential edges")
        for edge in graph.getAdjEdges(top[1]):
            if not visited[edge[1]]:
                heap.siftUp(edge[0], edge[1], edge[2])
        heap.print()

    return minSpanTree

if __name__ == "__main__":
    g = graphFromFile("vertices.txt", "edges.txt", True)
    mst = prims(g, 1)
    print("Original:")
    g.print()
    print("Minimum Spanning Tree:")
    mst.print()
