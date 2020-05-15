import random
import copy


def run():
    graph = hard_coded_dag(DoubleDictionaryGraph)
    print("The graph: ")
    print_graph(graph)
    print("")

    print("Topological sorting using predecessor count")
    sorted = topological_sorting_predecessor(graph)
    print(sorted)

    print("Topological sorting using DFS")
    sorted = topological_sorting_DFS(graph)
    print(sorted)


def topological_sorting_predecessor(graph):
    sorted = []
    queue = []
    count = {}
    for node in graph.parseX():
        count[node] = graph.inDegree(node)
        if count[node] == 0:
            queue.append(node)
    while len(queue) > 0:
        # print(count)
        # print(queue)
        current_node = queue.pop(0)
        sorted.append(current_node)
        for neighbour in graph.parseNout(current_node):
            count[neighbour] -= 1
            if count[neighbour] == 0:
                queue.append(neighbour)
    if len(sorted) != graph.numberVertices:
        return None
    return sorted


def topological_sorting_DFS(graph):
    sorted = []
    fully_processed = set()
    in_process = set()
    for node in graph.parseX():
        if node not in fully_processed:
            ok = DFS_for_topological_sorting(graph, node, sorted, fully_processed, in_process)
            if not ok:
                return None
    return sorted


def DFS_for_topological_sorting(graph, start_vertex, sorted, fully_processed, in_process):
    in_process.add(start_vertex)
    for neighbour in graph.parseNin(start_vertex):
        if neighbour in in_process:
            return False
        elif neighbour not in fully_processed:
            ok = DFS_for_topological_sorting(graph, neighbour, sorted, fully_processed, in_process)
            if not ok:
                return False
    in_process.remove(start_vertex)
    sorted.append(start_vertex)
    fully_processed.add(start_vertex)
    return True


class DoubleDictionaryGraph:
    def __init__(self, n):
        self.numberVertices = n
        self._dictionaryOut = {}
        self._dictionaryIn = {}
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

    def addEdge(self, x, y):
        self._dictionaryOut[x].append(y)
        self._dictionaryIn[y].append(x)

    def inDegree(self, x):
        return len(self._dictionaryIn[x])


def print_graph(graph):
    for i in range(0, graph.numberVertices):
        if len(graph.parseNin(i)) == len(graph.parseNout(i)) == 0:
            print(str(i) + " is an isolated vertex")
        else:
            for j in graph.parseNout(i):
                print(str(i) + " -> " + str(j))


def hard_coded_dag(graph_type):
    graph = graph_type(7)
    graph.addEdge(0, 6)
    graph.addEdge(6, 1)
    graph.addEdge(5, 4)
    graph.addEdge(5, 6)
    graph.addEdge(6, 3)
    graph.addEdge(6, 2)
    graph.addEdge(4, 3)
    graph.addEdge(3, 2)
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


run()
