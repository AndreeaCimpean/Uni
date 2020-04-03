class DirectedGraph:
    def __init__(self, numberOfVertices):
        self.NeighboursIn = {}
        self.NeighboursOut = {}
        self.Costs = {}
        self.NumberOfEdges = 0
        self.NumberOfVertices = numberOfVertices
        for i in range(0, self.NumberOfVertices):
            self.NeighboursIn[i] = []
            self.NeighboursOut[i] = []

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

    def add_edge(self, source, target, cost):
        '''
        Complexity:
            - O(outdegree(source)) for checking if edge already exists
            - Theta(1) for adding the edge
        Add an edge to a graph
        :param source: the source vertex, integer
        :param target: the target vertex, integer
        :param cost: the information of the edge
        Add the edge if it doesn't already exist
        Raise an error otherwise
        '''
        if self.is_edge(source, target):
            raise ValueError("Edge already exists")
        self.NeighboursIn[target].append(source)
        self.NeighboursOut[source].append(target)
        self.Costs[(source, target)] = cost
        self.NumberOfEdges += 1

    def add_edge_without_check(self, source, target, cost):
        '''
        Complexity: Theta(1)
        Add edge without checking if it already exists, for efficient reading, supposing valid input
        :param source: the source vertex of the edge, integer
        :param target: the target vertex of the edge, integer
        :param cost: the information of the edge
        Add the edge
        '''
        self.NeighboursIn[target].append(source)
        self.NeighboursOut[source].append(target)
        self.Costs[(source, target)] = cost
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

    def get_cost(self, source, target):
        '''
        Complexity:
            -O(outdegree(source)) for checking if edge_exists
            -O(1) to get the cost
        Get the information of an edge
        :param source: the source vertex of the edge, integer
        :param target: the target vertex of the edge, integer
        :return: the information of the edge if the edge exists
        Raise an error otherwise
        '''
        if not self.is_edge(source, target):
            raise ValueError("Edge does not exist")
        return self.Costs[(source, target)]

    def set_cost(self, source, target, value):
        '''
        CComplexity:
            -O(outdegree(source)) for checking if edge_exists
            -O(1) to set the cost
        Set the information of an edge
        :param source: the source vertex of the edge, integer
        :param target: the target vertex of the edge, integer
        :param value: the information
        Set the information of the edge if the edge exists
        Raise an error otherwise
        '''
        if not self.is_edge(source, target):
            raise ValueError("Edge does not exist")
        self.Costs[(source, target)] = value

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
        del self.Costs[(source, target)]
        self.NumberOfEdges -= 1

    def add_vertex(self, vertex):
        '''
        Complexity:
            -O(numberVertices) to check if valid vertex
            -O(1) to add vertex
        Add a vertex
        :param vertex: the vertex, integer
        Add the vertex if it doesn't already exist
        Raise an error otherwise
        '''
        if self.is_vertex(vertex):
            raise ValueError("Vertex already exist")
        self.NeighboursIn[vertex] = []
        self.NeighboursOut[vertex] = []
        self.NumberOfVertices += 1

    def remove_vertex(self, vertex):
        '''
        Complexity: O(indegree(vertex)+outdegree(vertex))
        Remove a vertes
        :param vertex: the given vertex, integer
        Remove the vertex if it exists
        Raise an error otherwise
        '''
        for i in self.parse_inbound_edges(vertex):
            self.remove_edge(i, vertex)
        for i in self.parse_outbound_edges(vertex):
            self.remove_edge(vertex, i)
        del self.NeighboursIn[vertex]
        del self.NeighboursOut[vertex]
        self.NumberOfVertices -= 1






