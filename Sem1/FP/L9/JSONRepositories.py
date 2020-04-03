import json

from memoryRepositories import *
from exceptions import RepositoryException
from domain import *
import datetime


class JSONMovieRepository(MovieRepository):
    def __init__(self, fileName):
        super().__init__([])
        self._fileName = fileName
        self._load_file()

    def _load_file(self):
        f = open(self._fileName, 'r')
        data = json.load(f)
        for i in range(len(data)):
            try:
                newMovie = Movie(data[i]["id"], data[i]["title"], data[i]["description"], data[i]["genre"])
                MovieRepository.store_movie(self, newMovie)
            except KeyError:
                raise RepositoryException("Invalid input format")
        f.close()

    def store_movie(self, movie):
        MovieRepository.store_movie(self, movie)
        self._save_file()

    def update_movie(self, movieId, title, description, genre):
        movie = MovieRepository.update_movie(self, movieId, title, description, genre)
        self._save_file()
        return movie

    def delete_movie(self, movieId):
        movie = MovieRepository.delete_movie(self, movieId)
        self._save_file()
        return movie

    def _save_file(self):
        f = open(self._fileName, 'w')
        data = []
        for m in self.get_list_movies():
            data.append(m.to_dictionary())
        json.dump(data, f)
        f.close()


class JSONClientRepository(ClientRepository):
    def __init__(self, fileName):
        super().__init__([])
        self._fileName = fileName
        self._load_file()

    def _load_file(self):
        f = open(self._fileName, 'r')
        data = json.load(f)
        for i in range(len(data)):
            try:
                newClient = Client(data[i]["id"], data[i]["name"])
                ClientRepository.store_client(self, newClient)
            except KeyError:
                raise RepositoryException("Invalid input format")
        f.close()

    def store_client(self, client):
        ClientRepository.store_client(self, client)
        self._save_file()

    def delete_client(self, clientId):
        client = ClientRepository.delete_client(self, clientId)
        self._save_file()
        return client

    def update_client(self, clientId, name):
        client = ClientRepository.update_client(self, clientId, name)
        self._save_file()
        return client

    def _save_file(self):
        f = open(self._fileName, 'w')
        data = []
        for c in self.get_list_clients():
            data.append(c.to_dictionary())
        json.dump(data, f)
        f.close()


class JSONRentalRepository(RentalRepository):
    def __init__(self, fileName, movieRepo, clientRepo):
        super().__init__([], movieRepo, clientRepo)
        self._fileName = fileName
        self._load_file()

    def _load_file(self):
        f = open(self._fileName, 'r')
        data = json.load(f)
        for i in range(len(data)):
            try:
                formatdate = "%Y-%m-%d"
                if data[i]["returnedDate"] != "None":
                    newRental = Rental(data[i]["id"], data[i]["movieId"], data[i]["clientId"],
                                       datetime.datetime.strptime(data[i]["rentedDate"], formatdate).date(),
                                       datetime.datetime.strptime(data[i]["dueDate"], formatdate).date(),
                                       datetime.datetime.strptime(data[i]["returnedDate"], formatdate).date())
                else:
                    newRental = Rental(data[i]["id"], data[i]["movieId"], data[i]["clientId"],
                                       datetime.datetime.strptime(data[i]["rentedDate"], formatdate).date(),
                                       datetime.datetime.strptime(data[i]["dueDate"], formatdate).date(), None)
                RentalRepository.store_rental(self, newRental)
            except KeyError:
                raise RepositoryException("Invalid input format")
        f.close()

    def store_rental(self, rental):
        RentalRepository.store_rental(self, rental)
        self._save_file()

    def update_rental(self, clientId, movieId, returnedDate):
        RentalRepository.update_rental(self, clientId, movieId, returnedDate)
        self._save_file()

    def delete_rental(self, rentalId):
        rental = RentalRepository.delete_rental(self, rentalId)
        self._save_file()
        return rental

    def _save_file(self):
        f = open(self._fileName, 'w')
        data = []
        for r in self.get_list_rentals():
            data.append(r.to_dictionary())
        json.dump(data, f)
        f.close()
