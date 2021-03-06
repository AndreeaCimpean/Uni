from graph import *
from priorityqueue import *
import random


def get_path(graph, start_vertex, target_vertex):
    '''
    Find the minimum cost walk between two vertices in a graph
    :param graph: the given graph
    :param start_vertex: the start vertex, integer
    :param target_vertex: the target vertex, integer
    :return: the cost and the path, if it exists
    Raise an error if there is no path from start to target
    '''
    dijkstra_result = Dijkstra(graph, start_vertex)
    distances = dijkstra_result[0]
    previous = dijkstra_result[1]

    if target_vertex not in distances.keys():
        raise ValueError("There is no path from " + str(start_vertex) + " to " + str(target_vertex))

    minimum_cost = distances[target_vertex]
    path = []
    while target_vertex != start_vertex:        # construct the path backwards
        path.insert(0, target_vertex)
        target_vertex = previous[target_vertex]
    path.insert(0, start_vertex)
    return (minimum_cost, path)


def Dijkstra(graph, start_vertex):
    '''
    Find the minimum cost walk from the start vertex to all its accessible vertices
    :param graph: the given graph
    :param start_vertex: the start vertex
    :return: the minimum costs, the previous node from the path for each vertex
    '''
    previous = {}   # keep track of the previous node before accessing the current
    queue = PriorityQueue()  # priority queue for parsing each accessible vertex in ascending order regarding the cost
    queue.push(start_vertex, 0)
    distances = {start_vertex: 0}  # construct the minimum distance from the start vertex to each accessible vertex
    visited = set()  # keep track of the visited vertices
    visited.add(start_vertex)
    while not queue.empty():
        current_node = queue.pop()
        for neighbour in graph.parse_outbound_edges(current_node):  # for each node parse its neighbours
            # if the neighbour is not visited or
            # if the path, in which the current node is before this neighbour,
            # has a lower cost than the currently cost for reaching this neighbour
            # then change the cost in the distances dictionary
            # add the neighbour to visited if it's not visited
            # add the neighbour to the priority queue/change its priority
            # set the previous of the neighbour to be the current node
            if neighbour not in visited or distances[neighbour] > distances[current_node] + graph.Costs[(current_node, neighbour)]:
                distances[neighbour] = distances[current_node] + graph.Costs[(current_node, neighbour)]
                visited.add(neighbour)
                queue.push(neighbour, distances[neighbour])
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