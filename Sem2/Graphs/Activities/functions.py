from graph import *
from priorityqueue import *
import random


def topological_sorting_predecessor(graph):
    sorted = []
    queue = []
    count = {}
    for node in graph.parse_vertices():
        count[node] = graph.get_in_degree(node)
        if count[node] == 0:
            queue.append(node)
    while len(queue) > 0:
        # print(count)
        # print(queue)
        current_node = queue.pop(0)
        sorted.append(current_node)
        for neighbour in graph.parse_outbound_edges(current_node):
            count[neighbour] -= 1
            if count[neighbour] == 0:
                queue.append(neighbour)
    if len(sorted) != graph.NumberOfVertices:
        return None
    return sorted


def get_critical_activities(graph):
    critical_activities = []
    for node in graph.parse_vertices():
        if graph.earliestBegin[node] == graph.latestBegin[node]:
            critical_activities.append(node)
    return critical_activities


def compute_earliest_times(graph):
    graph.earliestBegin[0] = graph.earliestEnd[0]
    order = topological_sorting_predecessor(graph)
    for i in range(1, graph.NumberOfVertices):
        max_time = -1
        for j in graph.parse_inbound_edges(order[i]):
            max_time = max(max_time, graph.earliestEnd[j])
        graph.earliestBegin[order[i]] = max_time
        graph.earliestEnd[order[i]] = max_time + graph.durations[order[i]]


def compute_latest_times(graph):
    order = topological_sorting_predecessor(graph)
    graph.latestEnd[graph.NumberOfVertices - 1] = graph.latestBegin[graph.NumberOfVertices - 1] = graph.earliestEnd[graph.NumberOfVertices - 1]
    for i in range(graph.NumberOfVertices-2, -1, -1):
        min_time = 999999
        for j in graph.parse_outbound_edges(order[i]):
            min_time = min(min_time, graph.latestBegin[j])
        graph.latestEnd[order[i]] = min_time
        graph.latestBegin[order[i]] = min_time - graph.durations[order[i]]


def compute_times(graph):
    compute_earliest_times(graph)
    compute_latest_times(graph)


def read_activities_from_file(fileName):
    '''
    Read activities from a given file and build the corresponding graph
    :param fileName: the name of the file
    :return: the list of activities, the graph built
    '''
    activities = []
    numberOfVertices = 0
    f = open(fileName, "r")
    line = f.readline()
    while len(line) > 0:
        numberOfVertices += 1
        line = f.readline().strip()
    f.close()
    graph = ActivitiesDirectedGraph(numberOfVertices+2)

    f = open(fileName, "r")
    line = f.readline()
    while len(line) > 0:
        parameters = line.split(",")
        graph.durations[int(parameters[0])] = int(parameters[2])
        activities.append(parameters[1])
        if len(parameters) == 4:
            parameters[3] = parameters[3].split(" ")
            for i in parameters[3]:
                graph.add_edge_without_check(int(i), int(parameters[0]))
        else:
            graph.add_edge_without_check(0, int(parameters[0]))
        line = f.readline().strip()
    f.close()
    for node in range(1, graph.NumberOfVertices - 1):
        if graph.get_out_degree(node) == 0:
            graph.add_edge_without_check(node, graph.NumberOfVertices - 1)
    return graph