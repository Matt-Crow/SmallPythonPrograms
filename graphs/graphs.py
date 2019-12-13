class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = dict()
    def hasVertex(self, v):
        #binary search
        min = 0
        max = len(self.vertices)
        found = False
        while not found and min < max and min >= 0 and max < len(self.vertices):
            mid = int((min + max) / 2)
            print(mid)
            if self.vertices[mid] > v:
                max = mid
            elif self.vertices[mid] < v:
                min = mid
            else:
                found = True
        return found
    def hasEdge(self, start, end):
        return start in self.edges and end in self.edges[start]

    def addVertex(self, v):
        if not self.hasVertex(v):
            self.vertices.append(v)
            #insertion sort
            i = len(self.vertices) - 1
            while i > 0 and self.vertices[i] < self.vertices[i - 1]:
                temp = self.vertices[i]
                self.vertices[i] = self.vertices[i - 1]
                self.vertices[i - 1] = temp
                i -= 1

    def getWeight(self, start, end):
        if self.hasEdge(start, end):
            return self.edges[start][end]

    def getAdjEdges(self, v):
        ret = []
        if v in self.edges.keys():
            for v2, weight in self.edges[v].items():
                ret.append([v, v2, weight])

        return ret

    def addEdge(self, start, end, weight):
        if not start in self.edges:
            self.edges[start] = dict()
        if not end in self.edges[start]:
            self.edges[start][end] = weight

    def print(self):
        print("VERTICES:")
        print(self.vertices)
        print("EDGES:")
        for start in self.edges.keys():
            for end in self.edges[start].keys():
                print(str(start) + ", " + str(end) + ": " + str(self.edges[start][end]))

def graphFromFile(vertexFile, edgeFile):
    g = Graph()

    vFile = open(vertexFile)
    for line in vFile:
        g.addVertex(int(line))
        g.print()
    vFile.close()

    eFile = open(edgeFile)
    for line in eFile:
        a = line.strip().split(" ")
        g.addEdge(int(a[0]), int(a[1]), int(a[2]))
        g.print()
    return g

if __name__ == "__main__":
    graphFromFile("vertices.txt", "edges.txt")
