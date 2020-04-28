import random


class DoubleDictionaryGraph:
    def __init__(self, n):
        self.numberVertices = n
        self._dictionaryOut = {}
        self._dictionaryIn = {}
        self.cost = {}
        for i in range(n):
            self._dictionaryOut[i] = []
            self._dictionaryIn[i] = []

    def parseX(self):
        return self._dictionaryOut.keys()

    def parseNout(self, x):
        return self._dictionaryOut[x]

    def parseNin(self, x):
        return self._dictionaryIn[x]

    def isEdge(self, x, y):
        return y in self._dictionaryOut[x]

    def addEdge(self, x, y, value):
        self._dictionaryOut[x].append(y)
        self._dictionaryIn[y].append(x)
        self.cost[(x, y)] = value


def accessible(graph, start_vertex):
    accessible_vertices = set()
    accessible_vertices.add(start_vertex)
    queue = [start_vertex]
    while len(queue) > 0:
        current_node = queue.pop(0)
        for neighbour in graph.parseNout(current_node):
            if neighbour not in accessible_vertices:
                accessible_vertices.add(neighbour)
                queue.append(neighbour)
    return accessible_vertices


def hard_coded_graph(graph_type):
    graph = graph_type(7)
    graph.addEdge(0, 1, 7)
    graph.addEdge(0, 2, 6)
    graph.addEdge(0, 3, 2)
    graph.addEdge(1, 4, 2)
    graph.addEdge(2, 1, 1)
    graph.addEdge(2, 4, 4)
    graph.addEdge(3, 2, 3)
    graph.addEdge(3, 6, 1)
    graph.addEdge(5, 1, 7)
    graph.addEdge(5, 4, 1)
    graph.addEdge(6, 4, 7)
    return graph


def random_graph(graph_type, vertices, edges):
    graph = graph_type(vertices)
    count = 0
    while count < edges:
        x = random.randrange(0, vertices)
        y = random.randrange(0, vertices)
        if not graph.isEdge(x, y):
            graph.addEdge(x, y)
            count += 1
    return graph

