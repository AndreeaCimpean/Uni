from graph import *
from functions import *
import random
import copy


class UI:
    def __init__(self):
        self._graph = self.choose_graph()
        self._copy_graph = copy.deepcopy(self._graph)

    def choose_graph(self):
        fileName = input("give file name: ")
        return read_graph_from_file(fileName)

    def _print_menu(self):
        print(" ")
        print("MENU")
        print("1. Print Hamiltonian cycle")
        print("2. Print connected components")
        print("3. Number of vertices of the graph")
        print("4. Print graph")
        print("5. Parse vertices")
        print("6. Check if an edge exists")
        print("7. Get the degree of a vertex")
        print("8. Parse neighbours of a vertex")
        print("9. Get edge information")
        print("10. Change edge information")
        print("11. Add edge")
        print("12. Remove edge")
        print("13. Add vertex")
        print("14. Remove vertex")
        print("15. Print original graph")
        print("16. Write the graph in a file")
        print("x to exit")
        print(" ")

    def start(self):
        while True:
            self._print_menu()
            command = input("> ")
            if command == "1":
                self._print_hamiltonian_cycle()
            elif command == "2":
                self._print_connected_components()
            if command == "3":
                self._display_number_of_vertices()
            elif command == "4":
                self._print_graph(self._graph)
            elif command == "5":
                self._parse_vertices()
            elif command == "6":
                self._check_if_edge_exists()
            elif command == "7":
                self._get_degree()
            elif command == "8":
                self._parse_neighbours()
            elif command == "9":
                self._get_edge_information()
            elif command == "10":
                self._change_edge_information()
            elif command == "11":
                self._add_edge()
            elif command == "12":
                self._remove_edge()
            elif command == "13":
                self._add_vertex()
            elif command == "14":
                self._remove_vertex()
            elif command == "15":
                self._print_graph(self._copy_graph)
            elif command == "16":
                self._write_graph_to_file()
            elif command == "x":
                return

    def _print_hamiltonian_cycle(self):
        cycle = get_hamiltonian_cycle(self._graph)
        print("The cycle is:")
        print(cycle[0])
        print("Its cost is: " + str(cycle[1]))

    def _print_connected_components(self):
        components = connected_components(self._graph)
        print("Number of connected components: " + str(len(components)))
        for i in range(0, len(components)):
            print(components[i])

    def _display_number_of_vertices(self):
        print(self._graph.get_number_of_vertices())

    def _print_graph(self, graph):
        print("Number of vertices: " + str(graph.NumberOfVertices))
        print("Number of edges: " + str(graph.NumberOfEdges))
        for i in graph.parse_vertices():
            if len(graph.Neighbours[i]) == 0:
                print(str(i) + " is an isolated vertex")
            else:
                for j in graph.Neighbours[i]:
                    if j > i:
                        print("(" + str(i) + ", " + str(j) + ")" + " having the cost: " + str(graph.Costs[(i, j)]))

    def _parse_vertices(self):
        string_to_print = ""
        for i in self._graph.parse_vertices():
            string_to_print += str(i) + " "
        print(string_to_print)

    def _check_if_edge_exists(self):
        source = int(input("a vertex of the edge: "))
        target = int(input("the other vertex of the edge: "))
        try:
            if self._graph.is_edge(source, target):
                print("There is an edge between " + str(source) + " and " + str(target))
            else:
                print("There isn't an edge between " + str(source) + " and " + str(target))
        except ValueError as ve:
            print(ve)

    def _get_degree(self):
        vertex = int(input("vertex: "))
        try:
            print(self._graph.get_degree(vertex))
        except ValueError as ve:
            print(ve)

    def _parse_neighbours(self):
        vertex = int(input("vertex: "))
        try:
            string_to_print = ""
            for i in self._graph.parse_neighbours(vertex):
                string_to_print += "(" + str(vertex) + ", " + str(i) + ") "
            print(string_to_print)
            if string_to_print == "":
                print("From vertex " + str(vertex) + " there is no edge")
        except ValueError as ve:
            print(ve)

    def _get_edge_information(self):
        source = int(input("a vertex of the edge: "))
        target = int(input("the other vertex of the edge: "))
        try:
            print(self._graph.get_cost(source, target))
        except ValueError as ve:
            print(ve)

    def _change_edge_information(self):
        source = int(input("a vertex of the edge: "))
        target = int(input("the other vertex of the edge: "))
        newInformation = int(input("new information: "))
        try:
            self._graph.set_cost(source, target, newInformation)
        except ValueError as ve:
            print(ve)

    def _add_edge(self):
        source = int(input("a vertex vertex of the edge: "))
        target = int(input("the other vertex of the edge: "))
        information = int(input("information: "))
        try:
            self._graph.add_edge(source, target, information)
        except ValueError as ve:
            print(ve)

    def _remove_edge(self):
        source = int(input("a vertex vertex of the edge: "))
        target = int(input("the other vertex of the edge: "))
        try:
            self._graph.remove_edge(source, target)
        except ValueError as ve:
            print(ve)

    def _add_vertex(self):
        self._graph.add_vertex()

    def _remove_vertex(self):
        vertex = int(input("vertex: "))
        try:
            self._graph.remove_vertex(vertex)
        except ValueError as ve:
            print(ve)

    def _write_graph_to_file(self):
        fileName = input("give file name: ")
        write_graph_to_file(fileName, self._graph)


ui = UI()
ui.start()
