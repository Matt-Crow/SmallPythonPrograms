class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []
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
    def hasVertex(self, v):
        #binary search
        min = 0
        max = len(self.vertices)
        found = False
        while not found and min < max:
            mid = int((min + max) / 2)
            if self.vertices[mid] > v:
                max = mid
            elif self.vertices[mid] < v:
                min = mid
            else:
                found = True
        return found
    def print(self):
        print("VERTICES:")
        print(self.vertices)

g = Graph()
for i in range(1, 10):
    g.addVertex((i - 5) ** 2)
    g.print()
