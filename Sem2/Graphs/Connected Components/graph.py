import copy


class UndirectedGraph:
    def __init__(self, numberOfVertices):
        self.Neighbours = {}
        self.Costs = {}
        self.NumberOfEdges = 0
        self.NumberOfVertices = numberOfVertices
        for i in range(0, self.NumberOfVertices):
            self.Neighbours[i] = []

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

    def add_edge(self, vertex1, vertex2, cost):
        '''
        Complexity:
            - O(degree(vertex1)) for checking if edge already exists
            - Theta(1) for adding the edge
        Add an edge to a graph
        :param vertex1: a vertex, integer
        :param vertex2: another vertex, integer
        :param cost: the information of the edge
        Add the edge if it doesn't already exist
        Raise an error otherwise
        '''
        if self.is_edge(vertex1, vertex2):
            raise ValueError("Edge already exists")
        self.Neighbours[vertex1].append(vertex2)
        self.Neighbours[vertex2].append(vertex1)
        self.Costs[(vertex1, vertex2)] = cost
        self.Costs[(vertex2, vertex1)] = cost
        self.NumberOfEdges += 1

    def add_edge_without_check(self, vertex1, vertex2, cost):
        '''
        Complexity: Theta(1)
        Add edge without checking if it already exists, for efficient reading, supposing valid input
        :param vertex1: a vertex of the edge, integer
        :param vertex2: the other vertex of the edge, integer
        :param cost: the information of the edge
        Add the edge
        '''
        self.Neighbours[vertex1].append(vertex2)
        self.Neighbours[vertex2].append(vertex1)
        self.Costs[(vertex1, vertex2)] = cost
        self.Costs[(vertex2, vertex1)] = cost
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
        return iter(self.Neighbours.keys())

    def parse_neighbours(self, vertex):
        '''
        Complexity:
            -O(numberVertices) to check if valid vertex
            -O(1) for returning iterator
            -O(degree(vertex)) when iterating
        Parse the neighbours of a vertex
        :param vertex: the given vertex, integer
        :return: an iterator over the set of neighbours of the vertex if the given vertex exists
        Raise an error if vertex does not exist
        '''
        if not self.is_vertex(vertex):
            raise ValueError("Vertex does not exist")
        return iter(self.Neighbours[vertex])

    def is_edge(self, vertex1, vertex2):
        '''
        Complexity:
            - O(numberVertices) for checking if source/target are valid
            - O(degree(source)) to check if there is an edge
        Check if there is an edge between two vertices
        :param vertex1: a vertex of the edge, integer
        :param vertex2: the other vertex of the edge, integer
        :return: True if the edge exists
                 False if the edge does not exist
        Raise an error if the vertices do not exist
        '''
        if not self.is_vertex(vertex1):
            raise ValueError("Source vertex does not exist")
        if not self.is_vertex(vertex2):
            raise ValueError("Target vertex does not exist")
        for i in self.parse_neighbours(vertex1):
            if i == vertex2:
                return True
        return False

    def is_vertex(self, vertex):
        '''
        Complexity: O(numberVertices)
        Check if a vertex exists
        :param vertex: the given vertex, integer
        :return: True if it exists
                 False otherwise
        '''
        if vertex not in self.parse_vertices():
            return False
        return True

    def get_degree(self, vertex):
        '''
        Complexity:
            -O(numberVertices) for checking if valid vertex
            -O(1) for getting the degree
        Get the degree of a vertex
        :param vertex: the given vertex, integer
        :return: the degree if the vertex exists
        Raise an error if the vertex does not exist
        '''
        if not self.is_vertex(vertex):
            raise ValueError("Vertex does not exist")
        return len(self.Neighbours[vertex])

    def get_cost(self, vertex1, vertex2):
        '''
        Complexity:
            -O(degree(vertex1)) for checking if edge exists
            -O(1) to get the cost
        Get the information of an edge
        :param vertex1: a vertex of the edge, integer
        :param vertex2: the other vertex of the edge, integer
        :return: the information of the edge if the edge exists
        Raise an error otherwise
        '''
        if not self.is_edge(vertex1, vertex2):
            raise ValueError("Edge does not exist")
        return self.Costs[(vertex1, vertex2)]

    def set_cost(self, vertex1, vertex2, value):
        '''
        CComplexity:
            -O(degree(vertex1)) for checking if edge exists
            -O(1) to set the cost
        Set the information of an edge
        :param vertex1: a vertex of the edge, integer
        :param vertex2: the other vertex of the edge, integer
        :param value: the information
        Set the information of the edge if the edge exists
        Raise an error otherwise
        '''
        if not self.is_edge(vertex1, vertex2):
            raise ValueError("Edge does not exist")
        self.Costs[(vertex1, vertex2)] = value
        self.Costs[(vertex2, vertex1)] = value

    def remove_edge(self, vertex1, vertex2):
        '''
        Complexity:
            -O(degree(vertex1)) for checking if edge_exists
            -O(degree(vertex1)+degree(vertex2)) to remove
        Remove an edge of the graph
        :param vertex1: the source vertex of the edge, integer
        :param vertex2: the target vertex of the edge, integer
        Remove the edge if it exists
        Raise an error otherwise
        '''
        if not self.is_edge(vertex1, vertex2):
            raise ValueError("Edge does not exist")
        self.Neighbours[vertex1].remove(vertex2)
        self.Neighbours[vertex2].remove(vertex1)
        del self.Costs[(vertex1, vertex2)]
        del self.Costs[(vertex2, vertex1)]
        self.NumberOfEdges -= 1

    def add_vertex(self):
        '''
        Complexity:
            -O(1) to add vertex
        Add a vertex
        '''
        self.Neighbours[self.NumberOfVertices] = []
        self.NumberOfVertices += 1

    def remove_vertex(self, vertex):
        '''
        Complexity: O(degree(vertex)) for removing
                    O(m+n) for renumbering
        Remove a vertex
        :param vertex: the given vertex, integer
        Remove the vertex if it exists
        Raise an error otherwise
        '''
        edges_to_remove = []
        for i in self.parse_neighbours(vertex):
            edges_to_remove.append((i, vertex))
        for i in range(0, len(edges_to_remove)):
            self.remove_edge(edges_to_remove[i][0], edges_to_remove[i][1])
        del self.Neighbours[vertex]

        copy_costs = copy.deepcopy(self.Costs)
        self.Costs = {}
        for edge in copy_costs.keys():
            if edge[0] > vertex and edge[1] > vertex:
                self.Costs[(edge[0] - 1, edge[1] - 1)] = copy_costs[edge]
            elif edge[0] > vertex:
                self.Costs[(edge[0] - 1, edge[1])] = copy_costs[edge]
            elif edge[1] > vertex:
                self.Costs[(edge[0], edge[1] - 1)] = copy_costs[edge]
            else:
                self.Costs[edge] = copy_costs[edge]

        copy_neighbours = copy.deepcopy(self.Neighbours)
        self.Neighbours = {}

        for i in range(0, self.NumberOfVertices - 1):
            self.Neighbours[i] = []

        for i in copy_neighbours.keys():
            for j in copy_neighbours[i]:
                if i > vertex and j > vertex:
                    self.Neighbours[i-1].append(j-1)
                elif i > vertex:
                    self.Neighbours[i-1].append(j)
                elif j > vertex:
                    self.Neighbours[i].append(j-1)
                else:
                    self.Neighbours[i].append(j)

        self.NumberOfVertices -= 1
