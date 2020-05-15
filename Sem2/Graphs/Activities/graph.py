import copy


class ActivitiesDirectedGraph:
    def __init__(self, numberOfVertices):
        self.NumberOfVertices = numberOfVertices
        self.NumberOfEdges = 0
        self.NeighboursIn = {}
        self.NeighboursOut = {}
        self.durations = {0: 0, self.NumberOfVertices-1: 0}
        self.earliestBegin = {0: 0, self.NumberOfVertices-1: 0}
        self.earliestEnd = {0: 0, self.NumberOfVertices-1: 0}
        self.latestBegin = {0: 0, self.NumberOfVertices-1: 0}
        self.latestEnd = {0: 0, self.NumberOfVertices-1: 0}
        for i in range(0, self.NumberOfVertices):
            self.NeighboursIn[i] = []
            self.NeighboursOut[i] = []
            self.earliestBegin[i] = 0
            self.earliestEnd[i] = 0
            self.latestBegin[i] = 0
            self.latestEnd[i] = 0

    @property
    def NumberOfVertices(self):
        return self._number_of_vertices

    @NumberOfVertices.setter
    def NumberOfVertices(self, value):
        self._number_of_vertices = value

    @property
    def NumberOfEdges(self):
        return self._number_of_edges

    @NumberOfEdges.setter
    def NumberOfEdges(self, value):
        self._number_of_edges = value

    def add_edge(self, source, target):
        '''
        Complexity:
            - O(outdegree(source)) for checking if edge already exists
            - Theta(1) for adding the edge
        Add an edge to a graph
        :param source: the source vertex, integer
        :param target: the target vertex, integer
        Add the edge if it doesn't already exist
        Raise an error otherwise
        '''
        if self.is_edge(source, target):
            raise ValueError("Edge already exists")
        self.NeighboursIn[target].append(source)
        self.NeighboursOut[source].append(target)
        self.NumberOfEdges += 1

    def add_edge_without_check(self, source, target):
        '''
        Complexity: Theta(1)
        Add edge without checking if it already exists, for efficient reading, supposing valid input
        :param source: the source vertex of the edge, integer
        :param target: the target vertex of the edge, integer
        Add the edge
        '''
        self.NeighboursIn[target].append(source)
        self.NeighboursOut[source].append(target)
        self.NumberOfEdges += 1

    def get_number_of_vertices(self):
        '''
        Complexity: Theta(1)
        Get the number of vertices of the graph
        :return: the number pf vertices
        '''
        return self.NumberOfVertices

    def get_number_of_edges(self):
        '''
        Complexity: Theta(1)
        Get the number of edges of the graph
        :return: the number of edges
        '''
        return self.NumberOfEdges

    def parse_vertices(self):
        '''
        Complexity:
            -O(1) fore returning the iterator
            -O(numberVertices) when iterating
        Parse the vertices of a graph
        :return: an iterator over the set of vertices
        '''
        return iter(self.NeighboursIn.keys())

    def parse_inbound_edges(self, vertex):
        '''
        Complexity:
            -O(numberVertices) to check if valid vertex
            -O(1) for returning iterator
            -O(indegree(vertex)) when iterating
        Parse the inbound edges of a vertex
        :param vertex: the given vertex, integer
        :return: an iterator over the set of direct predecessors of the vertex if the given vertex exists
        Raise an error if vertex does not exist
        '''
        if not self.is_vertex(vertex):
            raise ValueError("Vertex does not exist")
        return iter(self.NeighboursIn[vertex])

    def parse_outbound_edges(self, vertex):
        '''
        Complexity:
            -O(numberEdges) to check if valid vertex
            -O(1) for returning iterator
            -O(outdegree(vertex)) when iterating
        Parse outbound edges of a vertex
        :param vertex: the given vertex, integer
        :return: an iterator over the set of direct successors of the vertex if the given vertex exists
        Raise an error if the vertex does not exist
        '''
        if not self.is_vertex(vertex):
            raise ValueError("Vertex does not exist")
        return iter(self.NeighboursOut[vertex])

    def is_edge(self, source, target):
        '''
        Complexity:
            - O(numberVertices) for checking if source/target are valid
            - O(outdegree(source)) to check if there is an edge
        Check if there is an edge between two vertices
        :param source: the source vertex, integer
        :param target: the target vertex, integer
        :return: True if the edge exists
                 False if the edge does not exists
        Raise an error if the vertices do not exist
        '''
        if not self.is_vertex(source):
            raise ValueError("Source vertex does not exist")
        if not self.is_vertex(target):
            raise ValueError("Target vertex does not exist")
        for i in self.parse_outbound_edges(source):
            if i == target:
                return True
        return False

    def is_vertex(self, vertex):
        '''
        Complexity: O(numberVertices)
        Check if a vertex exist
        :param vertex: the given vertex, integer
        :return: True if it exists
                 False otherwise
        '''
        if vertex not in self.parse_vertices():
            return False
        return True

    def get_in_degree(self, vertex):
        '''
        Complexity:
            -O(numberVertices) for checking if valid vertex
            -O(1) for getting the in degree
        Get the in degree of a vertex
        :param vertex: the given vertex, integer
        :return: the in degree if the vertex exists
        Raise an error if the vertex does not exist
        '''
        if not self.is_vertex(vertex):
            raise ValueError("Vertex does not exist")
        return len(self.NeighboursIn[vertex])

    def get_out_degree(self, vertex):
        '''
        Complexity:
            -O(numberVertices) for checking if valid veretex
            -O(1) for getting the out degree
        Get the out degree of a vertex
        :param vertex: the given vertex, integer
        :return: the out degree if the vertex exists
        Raise an error if the vertex does not exist
        '''
        if not self.is_vertex(vertex):
            raise ValueError("Vertex does not exist")
        return len(self.NeighboursOut[vertex])

    def remove_edge(self, source, target):
        '''
        Complexity:
            -O(outdegree(source)) for checking if edge_exists
            -O(outdegree(source)+indegree(target)) to remove
        Remove an edge of the graph
        :param source: the source vertex of the edge, integer
        :param target: the target vertex of the edge, integer
        Remove the edge if it exists
        Raise an error otherwise
        '''
        if not self.is_edge(source, target):
            raise ValueError("Edge does not exist")
        self.NeighboursIn[target].remove(source)
        self.NeighboursOut[source].remove(target)
        self.NumberOfEdges -= 1

    def add_vertex(self, duration, prerequisites):
        '''
        :param: duration - the duration of the activity, integer
        :param: prerequisites - the activities that must be done before
        Complexity:
            -O(1) to add vertex
        Add a vertex
        '''
        self.NeighboursIn[self.NumberOfVertices] = self.NeighboursIn[self.NumberOfVertices - 1]
        self.NeighboursOut[self.NumberOfVertices] = self.NeighboursOut[self.NumberOfVertices - 1]
        self.durations[self.NumberOfVertices] = self.durations[self.NumberOfVertices - 1]
        self.NeighboursIn[self.NumberOfVertices - 1] = []
        self.NeighboursOut[self.NumberOfVertices - 1] = self.NeighboursOut[self.NumberOfVertices - 1]
        self.durations[self.NumberOfVertices - 1] = duration
        for p in prerequisites:
            self.add_edge(p, self.NumberOfVertices - 1)
        self.NumberOfVertices += 1

    def remove_vertex(self, vertex):
        '''
        Complexity: O(indegree(vertex)+outdegree(vertex)) for removing
                    O(m+n) for renumbering
        Remove a vertex
        :param vertex: the given vertex, integer
        Remove the vertex if it exists
        Raise an error otherwise
        '''
        edges_to_remove = []
        for i in self.parse_inbound_edges(vertex):
            edges_to_remove.append((i, vertex))
        for i in range(0, len(edges_to_remove)):
            self.remove_edge(edges_to_remove[i][0], edges_to_remove[i][1])
        edges_to_remove = []
        for i in self.parse_outbound_edges(vertex):
            edges_to_remove.append((vertex, i))
        for i in range(0, len(edges_to_remove)):
            self.remove_edge(edges_to_remove[i][0], edges_to_remove[i][1])
        del self.NeighboursIn[vertex]
        del self.NeighboursOut[vertex]

        for i in range(vertex, self.NumberOfVertices):
            self.durations[i] = self.durations[i + 1]
        del self.durations[self.NumberOfVertices]

        copy_neighbours_in = copy.deepcopy(self.NeighboursIn)
        copy_neighbours_out = copy.deepcopy(self.NeighboursOut)
        self.NeighboursIn = {}
        self.NeighboursOut = {}

        for i in range(0, self.NumberOfVertices - 1):
            self.NeighboursIn[i] = []
            self.NeighboursOut[i] = []

        for i in copy_neighbours_in.keys():
            for j in copy_neighbours_in[i]:
                if i > vertex and j > vertex:
                    self.NeighboursIn[i-1].append(j-1)
                elif i > vertex:
                    self.NeighboursIn[i-1].append(j)
                elif j > vertex:
                    self.NeighboursIn[i].append(j-1)
                else:
                    self.NeighboursIn[i].append(j)

        for i in copy_neighbours_out.keys():
            for j in copy_neighbours_out[i]:
                if i > vertex and j > vertex:
                    self.NeighboursOut[i-1].append(j-1)
                elif i > vertex:
                    self.NeighboursOut[i-1].append(j)
                elif j > vertex:
                    self.NeighboursOut[i].append(j-1)
                else:
                    self.NeighboursOut[i].append(j)

        self.NumberOfVertices -= 1

    def to_string_vertex(self, vertex):
        vertex_string = ""
        vertex_string += "(" + str(vertex) + ", " + str(self.durations[vertex]) + ", " + str(self.earliestBegin[vertex]) + ", "
        vertex_string += str(self.latestBegin[vertex]) + ", " + str(self.earliestEnd[vertex]) + ", " + str(self.latestEnd[vertex])
        vertex_string += ")"
        return vertex_string

