from graph import *
from functions import *
import copy


class UI:
    def __init__(self):
        self._graph = self.choose_graph()
        self._copy_graph = copy.deepcopy(self._graph)

    def choose_graph(self):
        fileName = input("give file name: ")
        return read_activities_from_file(fileName)

    def _print_menu(self):
        print(" ")
        print("MENU")
        print("1. Get topological order")
        print("2. Get activities time")
        print("3. Get critical activities")
        print("4. Number of vertices of the graph")
        print("5. Print graph")
        print("6. Parse vertices")
        print("7. Check if an edge exists")
        print("8. Get the in degree of a vertex")
        print("9. Get the out degree of a vertex")
        print("10. Parse outbound edges of a vertex")
        print("11. Parse inbound edges of a vertex")
        print("12. Add edge")
        print("13. Remove edge")
        print("14. Add vertex")
        print("15. Remove vertex")
        print("16. Print original graph")
        print("x to exit")
        print(" ")

    def start(self):
        if topological_sorting_predecessor(self._graph) != None:
            compute_times(self._graph)
        while True:
            self._print_menu()
            command = input("> ")
            if command == "1":
                self._get_topological_order()
            elif command == "2":
                self._get_activities()
            elif command == "3":
                self._get_critical_activities()
            elif command == "4":
                self._display_number_of_vertices()
            elif command == "5":
                self._print_graph(self._graph)
            elif command == "6":
                self._parse_vertices()
            elif command == "7":
                self._check_if_edge_exists()
            elif command == "8":
                self._get_in_degree()
            elif command == "9":
                self._get_out_degree()
            elif command == "10":
                self._parse_outbound_edges()
            elif command == "11":
                self._parse_inbound_edges()
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
            elif command == "x":
                return

    def _get_topological_order(self):
        order = topological_sorting_predecessor(self._graph)
        if order == None:
            print("Graph is not a DAG")
        else:
            print("Graph is a DAG")
            print("A topological order is")
            print(order)

    def _get_activities(self):
        if topological_sorting_predecessor(self._graph) == None:
            print("Not a DAG")
        else:
            print("Total time of the project: " + str(self._graph.earliestBegin[self._graph.NumberOfVertices-1]))
            for node in self._graph.parse_vertices():
                print("Activity: " + str(node) + " earliest start: " + str(self._graph.earliestBegin[node]) + " latest start: "+ str(self._graph.latestBegin[node]))

    def _get_critical_activities(self):
        if topological_sorting_predecessor(self._graph) == None:
            print("Not a DAG")
        else:
            print("Activity, duration, earliest begin, latest begin, earliest end, latest end")
            for node in get_critical_activities(self._graph):
                print(self._graph.to_string_vertex(node))

    def _display_number_of_vertices(self):
        print(self._graph.get_number_of_vertices())

    def _print_graph(self, graph):
        print("Number of vertices: " + str(graph.NumberOfVertices))
        print("Number of edges: " + str(graph.NumberOfEdges))
        print("Activity, duration, earliest begin, latest begin, earliest end, latest end")
        for i in graph.parse_vertices():
            if len(graph.NeighboursIn[i]) == len(graph.NeighboursOut[i]) == 0:
                print(self._graph.to_string_vertex(i))
            else:
                for j in graph.NeighboursOut[i]:
                    print(self._graph.to_string_vertex(i) + " -> " + self._graph.to_string_vertex(j))

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

    def _add_edge(self):
        source = int(input("source vertex: "))
        target = int(input("target vertex: "))
        try:
            self._graph.add_edge(source, target)
            self._graph.compute_times()
        except ValueError as ve:
            print(ve)

    def _remove_edge(self):
        source = int(input("source vertex: "))
        target = int(input("target vertex: "))
        try:
            self._graph.remove_edge(source, target)
            self._graph.compute_times()
        except ValueError as ve:
            print(ve)

    def _add_vertex(self):
        self._graph.add_vertex()
        self._graph.compute_times()

    def _remove_vertex(self):
        vertex = int(input("vertex: "))
        try:
            self._graph.remove_vertex(vertex)
            self._graph.compute_times()
        except ValueError as ve:
            print(ve)


ui = UI()
ui.start()
