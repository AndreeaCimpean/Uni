from graph import *
from queue import PriorityQueue
import random


def get_path(graph, start_vertex, target_vertex):
    dijkstra_result = Dijkstra(graph, start_vertex)
    distances = dijkstra_result[0]
    previous = dijkstra_result[1]

    if target_vertex not in distances.keys():
        raise ValueError("There is no path from " + str(start) + " to " + str(target))

    minimum_cost = distances[target_vertex]
    path = []
    while target_vertex != start_vertex:
        path.insert(0, target_vertex)
        target_vertex = previous[target_vertex]
    path.insert(0, start_vertex)
    return (minimum_cost, path)


def Dijkstra(graph, start_vertex):
    previous = {}
    queue = PriorityQueue()
    queue.put((0, start_vertex))
    distances = {}
    distances[start_vertex] = 0
    visited = set()
    visited.add(start_vertex)
    while not queue.empty():
        current_node = queue.get()[1]
        for neighbour in graph.parse_outbound_edges(current_node):
            if neighbour not in visited or distances[neighbour] > distances[current_node] + graph.Costs[(current_node, neighbour)]:
                distances[neighbour] = distances[current_node] + graph.Costs[(current_node, neighbour)]
                visited.add(neighbour)
                queue.put((distances[neighbour], neighbour))
                previous[neighbour] = current_node

    return (distances, previous)


def read_graph_from_file(fileName):
    '''
    Read graph from a given file
    :param fileName: the name of the file
    :return: the graph built
    '''
    f = open(fileName, "r")
    line = f.readline()
    parameters = line.split(" ")
    graph = DirectedGraph(int(parameters[0]))
    numberOfEdges = int(parameters[1])
    for i in range(0, numberOfEdges):
        line = f.readline().strip()
        parameters = line.split(" ")
        graph.add_edge_without_check(int(parameters[0]), int(parameters[1]), int(parameters[2]))
    f.close()
    return graph


def write_graph_to_file(fileName, graph):
    '''
    Write graph to a given file
    :param fileName: the name of the file
    :param graph: the graph to be written
    '''
    f = open(fileName, "w")
    line = str(graph.NumberOfVertices) + " " + str(graph.NumberOfEdges) + '\n'
    f.write(line)
    edges = graph.Costs.keys()
    for edge in edges:
        line = str(edge[0]) + " " + str(edge[1]) + " " + str(graph.Costs[edge]) + '\n'
        f.write(line)
    f.close()


def generate_random_graph(numberVertices, numberEdges):
    '''
    Generate randomly a graph
    :param numberVertices: the given number of vertices
    :param numberEdges: the given number of edges
    :return: the graph built
    Raise an error if numberEdges > numberVertices^2
    '''
    if numberEdges > numberVertices*numberVertices:
        raise ValueError("Invalid number of edges!")
    graph = DirectedGraph(numberVertices)
    count = 0
    while count != numberEdges:
        source = random.randint(0, numberVertices-1)
        target = random.randint(0, numberVertices-1)
        cost = random.randint(-100, 100)
        try:
            graph.add_edge(source, target, cost)
            count += 1
        except ValueError:
            continue
    return graph