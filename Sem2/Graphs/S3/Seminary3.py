import random
import copy


def run():
    graph = hard_coded_graph(DoubleDictionaryGraph)
    print("The graph: ")
    print_graph(graph)
    print("")
    print("Ex 3")
    exercise_3(graph)
    print("")
    print("Ex 4")
    print("Find the path between two vertices")
    source_vertex = int(input("give the source vertex: "))
    destination_vertex = int(input("give the destination vertex: "))
    exercise_4(graph, source_vertex, destination_vertex)


def exercise_3(graph):
    for i in range(0, graph.numberVertices):
        print("The tree with root " + str(i) + ":")
        tree = get_tree(graph, i)[0]
        print_tree(tree, i, "")


def exercise_4(graph, source_vertex, destination_vertex):
    paths = get_tree(graph, source_vertex)[1]
    if destination_vertex not in paths.keys():
        print("There is no path from vertex " + str(source_vertex) + " to vertex " + str(destination_vertex))
    else:
        for i in paths[destination_vertex]:
            print(str(i) + "->", end="")
        print(str(destination_vertex))


def get_tree(graph, root):
    tree = {}
    tree[root] = []
    paths_from_root = {}
    paths_from_root[root] = []
    visited_vertices = set()
    visited_vertices.add(root)
    queue = []
    queue.append(root)
    while len(queue) > 0:
        parent = queue.pop(0)
        for child in graph.parseNout(parent):
            if child not in visited_vertices:
                visited_vertices.add(child)
                queue.append(child)
                tree[child] = []
                tree[parent].append(child)
                paths_from_root[child] = copy.deepcopy(paths_from_root[parent])
                paths_from_root[child].append(parent)
    return tree, paths_from_root


def print_tree(tree, root, tab):
    print(tab + str(root))
    for children in tree[root]:
        print_tree(tree, children, tab + "    ")


def print_graph(graph):
    for i in range(0, graph.numberVertices):
        if len(graph.parseNin(i)) == len(graph.parseNout(i)) == 0:
            print(str(i) + " is an isolated vertex")
        else:
            for j in graph.parseNout(i):
                print(str(i) + " -> " + str(j))


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


class GoatStatus:
    def __init__(self, i):
        self._status = i

    def __str__(self):
        return self.strX(~self._status) + "/" + self.strX(self._status)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return self._status

    def isValid(self):
        return self.isValidBank(self._status) and self.isValidBank(~self._status)

    def parseN(self):
        ret = []
        for i in range(4):
            if (self._status & 1) == ((self._status >> i) & 1):
                ns = self._status ^ ((1 << i) | 1)
                s = GoatStatus(ns)
                if s.isValid():
                    ret.append(s)
        return ret

    def isValidBank(self, i):
        return (i & 4) == 0 or (i & 1) == 1 or ((i & 2) == 0 and (i & 8) == 0)

    def strX(self, i):
        ret = "("
        for j in range(4):
            if (i & (1 << j)) != 0:
                ret = ret + " " + self.names[j]
        return ret + ")"

    names = ("boat", "cabbage", "goat", "wolf")


class GoatGraph:
    def parseX(self):
        ret = []
        for i in range(16):
            s = GoatStatus(i)
            if s.isValid():
                ret.append(s)
        return ret

    def parseNout(self, s):
        return s.parseN()

    def parseNin(self, s):
        return s.parseN()


def hard_coded_graph(graph_type):
    graph = graph_type(5)
    graph.addEdge(0, 1)
    graph.addEdge(1, 0)
    graph.addEdge(1, 1)
    graph.addEdge(1, 2)
    graph.addEdge(4, 0)
    graph.addEdge(4, 2)
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
