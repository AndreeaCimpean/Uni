import random
import time


def exercise_4_print_neighbours():
    print("4: Print all neighbours for each vertex")
    graph = hard_coded_graph(DictionaryGraph)
    for x in graph.parseX():
        line = str(x) + " :"
        for y in graph.parseNout(x):
            line = line + " " + str(y)
        print(line)
    print("")


def exercise_5_parse_random_graph():
    print("5. Time needed to parse random graph")
    time_to_parse_random_graphs(DictionaryGraph, 10)
    print("")


def exercise_6_time_random_graphs():
    print("6 Time needed to parse random graphs")
    print("With adjacency matrix: ")
    time_to_parse_random_graphs(MatrixGraph, 1000)
    time_to_parse_random_graphs(MatrixGraph, 10000)
    '''
    time_to_parse_random_graphs(MatrixGraph, 100000)
    time_to_parse_random_graphs(MatrixGraph, 1000000)
    '''
    print("With dictionary: ")
    time_to_parse_random_graphs(DictionaryGraph, 1000)
    time_to_parse_random_graphs(DictionaryGraph, 10000)
    '''
    time_to_parse_random_graphs(DictionaryGraph, 100000)
    time_to_parse_random_graphs(DictionaryGraph, 1000000)
    '''
    print("With two dictionaries: ")
    time_to_parse_random_graphs(DoubleDictionaryGraph, 1000)
    time_to_parse_random_graphs(DoubleDictionaryGraph, 10000)
    time_to_parse_random_graphs(DoubleDictionaryGraph, 100000)
    time_to_parse_random_graphs(DoubleDictionaryGraph, 1000000)


def hard_coded_graph(graph_type):
    graph = graph_type(6)
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(1, 2)
    graph.addEdge(1, 5)
    graph.addEdge(2, 3)
    graph.addEdge(3, 2)
    graph.addEdge(5, 0)
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


def parse_graph(graph):
    for x in graph.parseX():
        for y in graph.parseNin(x):
            pass
        for y in graph.parseNout(x):
            pass


def time_to_parse_random_graphs(graph_type, vertices):
    start_time = time.time()
    graph = random_graph(graph_type, vertices, vertices*10)
    print("For a graph with " + str(vertices) + " vertices it takes " + str(time.time() - start_time) + " seconds to create and ", end="")
    start_time = time.time()
    parse_graph(graph)
    print(str(time.time() - start_time) + " seconds to parse")


def main():
    exercise_4_print_neighbours()
    exercise_5_parse_random_graph()
    exercise_6_time_random_graphs()


class MatrixGraph:
    def __init__(self, n):
        self._matrix = []
        for i in range(n):
            self._matrix.append([])
            for j in range(n):
                self._matrix[i].append(False)

    def parseX(self):
        nrOfVertices = len(self._matrix)
        return range(nrOfVertices)

    def parseNout(self, x):
        list = []
        for i in range(len(self._matrix[x])):
            if self._matrix[x][i]:
                list.append(i)
        return list

    def parseNin(self, x):
        list = []
        for i in range(len(self._matrix)):
            if self._matrix[i][x]:
                list.append(i)
        return list

    def isEdge(self, x, y):
        return self._matrix[x][y]

    def addEdge(self, x, y):
        self._matrix[x][y] = True


class DictionaryGraph:
    def __init__(self, n):
        self._dictionary = {}
        for i in range(n):
            self._dictionary[i] = []

    def parseX(self):
        return self._dictionary.keys()

    def parseNout(self, x):
        return self._dictionary[x]

    def parseNin(self, x):
        list = []
        for i in self._dictionary.keys():
            if x in self._dictionary[i]:
                list.append(i)
        return list

    def isEdge(self, x, y):
        return y in self._dictionary[x]

    def addEdge(self, x, y):
        self._dictionary[x].append(y)


class DoubleDictionaryGraph:
    def __init__(self, n):
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

main()