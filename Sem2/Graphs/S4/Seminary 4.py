from graph import *


def get_path():
    print("Get the lowest cost path from a vertex to another")
    graph = hard_coded_graph(DoubleDictionaryGraph)
    print("The graph is:")
    print_graph(graph)
    start = int(input("give the start vertex: "))
    target = int(input("give the target vertex: "))

    dijkstra_result = dijkstra(graph, start)
    distances = dijkstra_result[0]
    previous = dijkstra_result[1]

    if target not in distances.keys():
        print("There is no path from " + str(start) + " to " + str(target))
        return

    print("The minimum cost is: " + str(distances[target]))
    print("The path is:")
    path = []
    while target != start:
        path.insert(0, target)
        target = previous[target]
    path.insert(0, start)
    print(path)


class PriorityQueue:
    def __init__(self):
        self.__values = {}

    def isEmpty(self):
        return len(self.__values) == 0

    def pop(self):
        topPriority = None
        topObject = None
        for obj in self.__values:
            objPriority = self.__values[obj]
            if topPriority is None or topPriority > objPriority:
                topPriority = objPriority
                topObject = obj
        del self.__values[topObject]
        return topObject

    def add(self, obj, priority):
        self.__values[obj] = priority

    def contains(self, val):
        return val in self.__values


def dijkstra(graph, start_vertex):
    previous = {}
    queue = PriorityQueue()
    queue.add(start_vertex, 0)
    distances = {}
    distances[start_vertex] = 0
    visited = set()
    visited.add(start_vertex)
    while not queue.isEmpty():
        current_node = queue.pop()
        for neighbour in graph.parseNout(current_node):
            if neighbour not in visited or distances[neighbour] > distances[current_node] + graph.cost[(current_node, neighbour)]:
                distances[neighbour] = distances[current_node] + graph.cost[(current_node, neighbour)]
                visited.add(neighbour)
                queue.add(neighbour, distances[neighbour])
                previous[neighbour] = current_node

    return (distances, previous)


def print_graph(graph):
    for i in range(0, graph.numberVertices):
        if len(graph.parseNin(i)) == len(graph.parseNout(i)) == 0:
            print(str(i) + " is an isolated vertex")
        else:
            for j in graph.parseNout(i):
                print(str(i) + " -> " + str(j))


get_path()
