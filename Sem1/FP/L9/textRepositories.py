from memoryRepositories import *
from domain import *
import datetime


class TextMovieRepository(MovieRepository):
    def __init__(self, fileName):
        super().__init__([])
        self._fileName = fileName
        self._load_file()

    def _load_file(self):
        f = open(self._fileName, 'r')
        line = f.readline().strip()
        while len(line) > 0:
            params = line.split(",")
            newMovie = Movie(params[0], params[1], params[2], params[3])
            MovieRepository.store_movie(self, newMovie)
            line = f.readline().strip()
        f.close()

    def _save_file(self):
        f = open(self._fileName, 'w')
        for m in self.get_list_movies():
            line = str(m.movieId) + ',' + m.Title + ',' + m.Description + ',' + m.Genre + '\n'
            f.write(line)
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


class TextClientRepository(ClientRepository):
    def __init__(self, fileName):
        super().__init__([])
        self._fileName = fileName
        self._load_file()

    def _load_file(self):
        f = open(self._fileName, 'r')
        line = f.readline().strip()
        while len(line) > 0:
            params = line.split(",")
            newClient = Client(params[0], params[1])
            ClientRepository.store_client(self, newClient)
            line = f.readline().strip()
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
        for c in self.get_list_clients():
            line = str(c.clientId) + ',' + c.Name + '\n'
            f.write(line)
        f.close()


class TextRentalRepository(RentalRepository):
    def __init__(self, fileName, movieRepo, clientRepo):
        super().__init__([], movieRepo, clientRepo)
        self._fileName = fileName
        self._load_file()

    def _load_file(self):
        f = open(self._fileName, 'r')
        line = f.readline().strip()
        while len(line) > 0:
            params = line.split(",")
            formatdate = "%Y-%m-%d"
            if params[5] != "None":
                newRental = Rental(params[0], params[1], params[2],
                                   datetime.datetime.strptime(params[3], formatdate).date(),
                                   datetime.datetime.strptime(params[4], formatdate).date(),
                                   datetime.datetime.strptime(params[5], formatdate).date())
            else:
                newRental = Rental(params[0], params[1], params[2],
                                   datetime.datetime.strptime(params[3], formatdate).date(),
                                   datetime.datetime.strptime(params[4], formatdate).date(),
                                   None)
            RentalRepository.store_rental(self, newRental)
            line = f.readline().strip()
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
        for r in self.get_list_rentals():
            line = r.rentalId + ',' + r.movieId + ',' + r.clientId + ',' + \
                   str(r.rentedDate) + ',' + str(r.dueDate) + ',' + str(r.returnedDate) + '\n'
            f.write(line)
        f.close()