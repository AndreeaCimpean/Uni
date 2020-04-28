from graph import *
from functions import *
import copy


class UI:
    def __init__(self):
        self._graph = self.choose_graph()
        self._copy_graph = copy.deepcopy(self._graph)

    def choose_graph(self):
        print("1 for graph read from file")
        print("2 for graph generated randomly")
        choice = input("> ")
        if choice == "1":
            fileName = input("give file name: ")
            return read_graph_from_file(fileName)
        else:
            while True:
                try:
                    numberVertices = int(input("number of vertices: "))
                    numberEdges = int(input("number of edges: "))
                    return generate_random_graph(numberVertices, numberEdges)
                except ValueError as ve:
                    print(ve)

    def _print_menu(self):
        print(" ")
        print("MENU")
        print("1. Get the lowest cost walk from a vertex to another")
        print("2. Number of vertices of the graph")
        print("3. Print graph")
        print("4. Parse vertices")
        print("5. Check if an edge exists")
        print("6. Get the in degree of a vertex")
        print("7. Get the out degree of a vertex")
        print("8. Parse outbound edges of a vertex")
        print("9. Parse inbound edges of a vertex")
        print("10. Get edge information")
        print("11. Change edge information")
        print("12. Add edge")
        print("13. Remove edge")
        print("14. Add vertex")
        print("15. Remove vertex")
        print("16. Print original graph")
        print("17. Write the graph in a file")
        print("x to exit")
        print(" ")

    def start(self):
        while True:
            self._print_menu()
            command = input("> ")
            if command == "1":
                self._get_path()
            if command == "2":
                self._display_number_of_vertices()
            elif command == "3":
                self._print_graph(self._graph)
            elif command == "4":
                self._parse_vertices()
            elif command == "5":
                self._check_if_edge_exists()
            elif command == "6":
                self._get_in_degree()
            elif command == "7":
                self._get_out_degree()
            elif command == "8":
                self._parse_outbound_edges()
            elif command == "9":
                self._parse_inbound_edges()
            elif command == "10":
                self._get_edge_information()
            elif command == "11":
                self._change_edge_information()
            elif command == "12":
                self._add_edge()
            elif command == "13":
                self._remove_edge()
            elif command == "14":
                self._add_vertex()
            elif command == "15":
                self._remove_vertex()
            elif command == "16":
                self._print_graph(self._copy_graph)
            elif command == "17":
                self._write_graph_to_file()
            elif command == "x":
                return

    def _get_path(self):
        start = int(input("give the start vertex: "))
        target = int(input("give the target vertex: "))
        try:
            path = get_path(self._graph, start, target)
            print("The cost is: " + str(path[0]))
            print("The path is:",end=" ")
            print(path[1])
        except ValueError as ve:
            print(ve)

    def _display_number_of_vertices(self):
        print(self._graph.get_number_of_vertices())

    def _print_graph(self, graph):
        print("Number of vertices: " + str(graph.NumberOfVertices))
        print("Number of edges: " + str(graph.NumberOfEdges))
        for i in graph.parse_vertices():
            if len(graph.NeighboursIn[i]) == len(graph.NeighboursOut[i]) == 0:
                print(str(i) + " is an isolated vertex")
            else:
                for j in graph.NeighboursOut[i]:
                    print(str(i) + " -> " + str(j) + " having the cost: " + str(graph.Costs[(i, j)]))

    def _parse_vertices(self):
        string_to_print = ""
        for i in self._graph.parse_vertices():
            string_to_print += str(i) + " "
        print(string_to_print)

    def _check_if_edge_exists(self):
        source = int(input("source edge: "))
        target = int(input("target edge: "))
        try:
            if self._graph.is_edge(source, target):
                print("There is an edge between " + str(source) + " and " + str(target))
            else:
                print("There isn't an edge between " + str(source) + " and " + str(target))
        except ValueError as ve:
            print(ve)

    def _get_in_degree(self):
        vertex = int(input("vertex: "))
        try:
            print(self._graph.get_in_degree(vertex))
        except ValueError as ve:
            print(ve)

    def _get_out_degree(self):
        vertex = int(input("vertex: "))
        try:
            print(self._graph.get_out_degree(vertex))
        except ValueError as ve:
            print(ve)

    def _parse_outbound_edges(self):
        vertex = int(input("vertex: "))
        try:
            string_to_print = ""
            for i in self._graph.parse_outbound_edges(vertex):
                string_to_print += "(" + str(vertex) + ", " + str(i) + ") "
            print(string_to_print)
            if string_to_print == "":
                print("From vertex " + str(vertex) + " there is no edge")
        except ValueError as ve:
            print(ve)

    def _parse_inbound_edges(self):
        vertex = int(input("vertex: "))
        try:
            string_to_print = ""
            for i in self._graph.parse_inbound_edges(vertex):
                string_to_print += "(" + str(i) + ", " + str(vertex) + ") "
            print(string_to_print)
            if string_to_print == "":
                print("To vertex " + str(vertex) + " there is no edge")
        except ValueError as ve:
            print(ve)

    def _get_edge_information(self):
        source = int(input("source vertex: "))
        target = int(input("target vertex: "))
        try:
            print(self._graph.get_cost(source, target))
        except ValueError as ve:
            print(ve)

    def _change_edge_information(self):
        source = int(input("source vertex: "))
        target = int(input("target vertex: "))
        newInformation = int(input("new information: "))
        try:
            self._graph.set_cost(source, target, newInformation)
        except ValueError as ve:
            print(ve)

    def _add_edge(self):
        source = int(input("source vertex: "))
        target = int(input("target vertex: "))
        information = int(input("information: "))
        try:
            self._graph.add_edge(source, target, information)
        except ValueError as ve:
            print(ve)

    def _remove_edge(self):
        source = int(input("source vertex: "))
        target = int(input("target vertex: "))
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
