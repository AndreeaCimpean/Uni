from services import *


class UI:
    def __init__(self, movieServ, clientServ, rentalServ):
        self._movieService = movieServ
        self._clientService = clientServ
        self._rentalService = rentalServ

    def _print_menu(self):
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
        print("    12 to search a movie")
        print("    13 to search a client")
        print("    x  to exit")

    def start(self):
        while True:
            self._print_menu()
            command = input("> ")
            if command == "1":
                self._show_all_movies()
            elif command == "2":
                self._show_all_clients()
            elif command == "3":
                self._show_all_rentals()
            elif command == "4":
                self._add_movie_ui()
            elif command == "5":
                self._add_client_ui()
            elif command == "6":
                self._remove_movie_ui()
            elif command == "7":
                self._remove_client_ui()
            elif command == "8":
                self._update_movie_ui()
            elif command == "9":
                self._update_client_ui()
            elif command == "10":
                self._rent_movie_ui()
            elif command == "11":
                self._return_movie_ui()
            elif command == "12":
                self.search_movie_ui()
            elif command == "13":
                self.search_client_ui()
            elif command == "x":
                return
            else:
                print("Not a valid command")

    def _show_all_movies(self):
        print(" ")
        print("MOVIES")
        print(" ")
        for m in self._movieService.get_movies():
            print(m)

    def _show_all_clients(self):
        print(" ")
        print("CLIENTS")
        print(" ")
        for c in self._clientService.get_clients():
            print(c)

    def _show_all_rentals(self):
        print(" ")
        print("RENTALS")
        print(" ")
        for r in self._rentalService.get_rentals():
            print(r)

    def _add_movie_ui(self):
        movieId = input("movie id = ")
        title = input("title = ")
        description = input("description: ")
        genre = input("genre = ")
        try:
            movie = Movie(movieId, title, description, genre)
            self._movieService.add_movie(movie)
        except MovieException as ve:
            print(ve)

    def _add_client_ui(self):
        clientId = input("client id = ")
        name = input("name = ")
        try:
            client = Client(clientId, name)
            self._clientService.add_client(client)
        except ClientException as ve:
            print(ve)

    def _remove_movie_ui(self):
        movieId = input("movie id = ")
        try:
            self._movieService.remove_movie(movieId)
            self._rentalService.delete_all_rentals_movie(movieId)
        except MovieException as ve:
            print(ve)

    def _remove_client_ui(self):
        clientId = input("client id = ")
        try:
            self._clientService.remove_client(clientId)
            self._rentalService.delete_all_rentals_client(clientId)
        except ClientException as ve:
            print(ve)

    def _update_movie_ui(self):
        movieId = input("new movie id = ")
        title = input("new title = ")
        description = input("new description: ")
        genre = input("new genre = ")
        try:
            self._movieService.update_movie(movieId, title, description, genre)
        except MovieException as ve:
            print(ve)

    def _update_client_ui(self):
        clientId = input("client id = ")
        name = input("new name = ")
        try:
            self._clientService.update_client(clientId, name)
        except ClientException as ve:
            print(ve)

    def _rent_movie_ui(self):
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
        except RentalException as ve:
            print(ve)

    def _return_movie_ui(self):
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
        except RentalException as ve:
            print(ve)

    def search_movie_ui(self):
        print("By what do you want to search? (id .../title .../description .../genre ...)")
        command = input("> ")
        idx = command.find(" ")
        field = command[:idx]
        parameter = command[idx+1:]
        parameter = parameter.lower()
        #print(parameter)
        movies = []
        if field == "id":
            movies = self._movieService.search_movie_by_id(parameter)
        elif field == "title":
            movies = self._movieService.search_movie_by_title(parameter)
        elif field == "description":
            movies = self._movieService.search_movie_by_description(parameter)
        elif field == "genre":
            movies = self._movieService.search_movie_by_genre(parameter)
        else:
            print("invalid command")
            return
        if len(movies) > 0:
            for m in movies:
                print(m)
        else:
            print("No movies found")

    def search_client_ui(self):
        print("By what do you want to search? (id .../name ...)")
        command = input("> ")
        idx = command.find(" ")
        field = command[:idx]
        parameter = command[idx + 1:]
        parameter = parameter.lower()
        clients = []
        if field == "id":
            clients = self._clientService.search_client_by_id(parameter)
        elif field == "name":
            clients = self._clientService.search_client_by_name(parameter)
        else:
            print("invalid command")
            return
        if len(clients) > 0:
            for c in clients:
                print(c)
        else:
            print("No clients found")