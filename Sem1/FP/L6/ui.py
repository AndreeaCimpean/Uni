from services import *


class UI:
    def __init__(self, movieServ, clientServ, rentalServ):
        self._movieService = movieServ
        self._clientService = clientServ
        self._rentalService = rentalServ

    def print_menu(self):
        print(" ")
        print("    1  to show all the movies")
        print("    2  to show all the clients")
        print("    3  to show all rentals")
        print("    4  to add a new movie")
        print("    5  to add a new client")
        print("    6  to delete a movie")
        print("    7  to delete a client")
        print("    8  to update a movie")
        print("    9  to update a client")
        print("    10 to rent a movie")
        print("    11 to return a movie")
        print("    x  to exit")

    def start(self):
        while True:
            self.print_menu()
            command = input("> ")
            if command == "1":
                self.show_all_movies()
            elif command == "2":
                self.show_all_clients()
            elif command == "3":
                self.show_all_rentals()
            elif command == "4":
                self.add_movie_ui()
            elif command == "5":
                self.add_client_ui()
            elif command == "6":
                self.remove_movie_ui()
            elif command == "7":
                self.remove_client_ui()
            elif command == "8":
                self.update_movie_ui()
            elif command == "9":
                self.update_client_ui()
            elif command == "10":
                self.rent_movie_ui()
            elif command == "11":
                self.return_movie_ui()
            elif command == "x":
                return
            else:
                print("Not a valid command")

    def show_all_movies(self):
        print(" ")
        print("MOVIES")
        print(" ")
        for m in self._movieService.get_movies():
            print(m)

    def show_all_clients(self):
        print(" ")
        print("CLIENTS")
        print(" ")
        for c in self._clientService.get_clients():
            print(c)

    def show_all_rentals(self):
        print(" ")
        print("RENTALS")
        print(" ")
        for r in self._rentalService.get_rentals():
            print(r)

    def add_movie_ui(self):
        movieId = input("movie id = ")
        title = input("title = ")
        description = input("description: ")
        genre = input("genre = ")
        try:
            movie = Movie(movieId, title, description, genre)
            self._movieService.add_movie(movie)
        except ValueError as ve:
            print(ve)

    def add_client_ui(self):
        clientId = input("client id = ")
        name = input("name = ")
        try:
            client = Client(clientId, name)
            self._clientService.add_client(client)
        except ValueError as ve:
            print(ve)

    def remove_movie_ui(self):
        movieId = input("movie id = ")
        try:
            self._movieService.remove_movie(movieId)
        except ValueError as ve:
            print(ve)

    def remove_client_ui(self):
        clientId = input("client id = ")
        try:
            self._clientService.remove_client(clientId)
        except ValueError as ve:
            print(ve)

    def update_movie_ui(self):
        movieId = input("movie id = ")
        title = input("title = ")
        description = input("description: ")
        genre = input("genre = ")
        try:
            self._movieService.update_movie(movieId, title, description, genre)
        except ValueError as ve:
            print(ve)

    def update_client_ui(self):
        clientId = input("client id = ")
        name = input("name = ")
        try:
            self._clientService.update_client(clientId, name)
        except ValueError as ve:
            print(ve)

    def rent_movie_ui(self):
        clientId = input("client id = ")
        movieId = input("movie id = ")
        if movieId not in self._movieService.get_movies_id():
            print("No such movie")
            return
        if clientId not in self._clientService.get_clients_id():
            print("No such client")
            return
        try:
            self._rentalService.rent_movie(clientId, movieId)
        except ValueError as ve:
            print(ve)

    def return_movie_ui(self):
        clientId = input("client id = ")
        movieId = input("movie id = ")
        if movieId not in self._movieService.get_movies_id():
            print("No such movie")
            return
        if clientId not in self._clientService.get_clients_id():
            print("No such client")
            return
        try:
            self._rentalService.return_movie(clientId, movieId)
        except ValueError as ve:
            print(ve)