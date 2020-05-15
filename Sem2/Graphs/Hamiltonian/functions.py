import random
from graph import *
from priorityqueue import *


def get_hamiltonian_cycle(graph):
    tree = minimum_spanning_tree_prim(graph, 0)
    cycle = traverse_tree(tree, 0)
    cycle.append(0)
    cost = 0
    for i in range(0, len(cycle) - 1):
        cost += graph.Costs[(cycle[i], cycle[i + 1])]
    return cycle, cost


def minimum_spanning_tree_prim(graph, root):
    '''
    Complexity: O(m+nlogn)
    :param graph:
    :return:
    '''
    queue = PriorityQueue()
    previous = {}
    distance = {}
    edges = set()
    chosen_vertices = [root]
    for node in graph.parse_neighbours(root):
        distance[node] = graph.Costs[node, root]
        previous[node] = root
        queue.push(node, distance[node])
    while not queue.empty():
        node = queue.pop()
        if node not in chosen_vertices:
            edges.add((node, previous[node]))
            chosen_vertices.append(node)
            for neighbour in graph.parse_neighbours(node):
                if neighbour not in distance.keys() or graph.Costs[(node, neighbour)] < distance[neighbour]:
                    distance[neighbour] = graph.Costs[(node, neighbour)]
                    queue.push(neighbour, distance[neighbour])
                    previous[neighbour] = node
    tree = {root:[]}
    for edge in edges:
        if edge[1] not in tree.keys():
            tree[edge[1]] = []
        tree[edge[1]].append(edge[0])
    return tree


def traverse_tree(tree, root):
    order = []
    nodes_stack = []
    nodes_stack.append(root)
    while len(nodes_stack):
        parent = nodes_stack.pop(0)
        order.append(parent)
        if parent in tree.keys():
            for child in tree[parent]:
                nodes_stack.insert(0, child)
    return order


def connected_components(graph):
    '''
    Complexity: O(n+m)
    Get the connected components of a graph
    :param graph: the graph
    :return: The components
    '''
    components = []
    visited_vertices = {}  # keep track of the visited vertices : true for visited/false for unvisited
    for vertex in graph.parse_vertices():  # initially, all vertices are unvisited
        visited_vertices[vertex] = False
    for vertex in graph.parse_vertices():
        if not visited_vertices[vertex]:             # for every unvisited vertex call BFS, which returns
            components.append(BFS(graph, vertex))    # the accessible vertices from the vertex -> a new component
            for i in components[len(components)-1]:  # mark the vertices of the new component as visited
                visited_vertices[i] = True
    return components


def BFS(graph, start_vertex):
    '''
    Breadth first traversal of the graph
    :param graph: the graph
    :param start_vertex: the starting vertex
    return: the accessible vertices from the given start vertex
    '''
    accessible = [start_vertex]
    queue = [start_vertex]  # keep track of the vertices to be checked
    while len(queue) > 0:   # loop until there is no vertex to be checked
        current_node = queue.pop(0)
        for neighbour in graph.Neighbours[current_node]:  # loop the neighbours of the current vertex
            if neighbour not in accessible:               # if the neighbour is not in the accessible vertices
                queue.append(neighbour)                   # add it to the vertices to be checked
                accessible.append(neighbour)              # and add it to the accessible set
    return accessible


def read_graph_from_file(fileName):
    '''
    Read graph from a given file
    :param fileName: the name of the file
    :return: the graph built
    '''
    f = open(fileName, "r")
    line = f.readline()
    parameters = line.split(" ")
    graph = UndirectedGraph(int(parameters[0]))
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
        if edge[0] < edge[1]:
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
    if numberEdges > (numberVertices*(numberVertices-1))//2:
        raise ValueError("Invalid number of edges!")
    graph = UndirectedGraph(numberVertices)
    count = 0
    while count != numberEdges:
        vertex1 = random.randint(0, numberVertices-1)
        vertex2 = random.randint(0, numberVertices-1)
        if vertex1 == vertex2:
            continue
        cost = random.randint(-100, 100)
        try:
            graph.add_edge(vertex1, vertex2, cost)
            count += 1
        except ValueError:
            continue
    return graph