from memoryRepositories import *
import pickle


class PickleMovieRepository(MovieRepository):
    def __init__(self, fileName):
        self._fileName = fileName
        super().__init__([])
        self._load_file()

    def _load_file(self):
        f = open(self._fileName, "rb")
        movies = pickle.load(f)
        for m in movies:
            MovieRepository.store_movie(self, m)
        f.close()

    def _save_file(self):
        f = open(self._fileName, 'wb')
        pickle.dump(self.get_list_movies(), f)
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


class PickleClientRepository(ClientRepository):
    def __init__(self, fileName):
        self._fileName = fileName
        super().__init__([])
        self._load_file()

    def _load_file(self):
        f = open(self._fileName, "rb")
        clients = pickle.load(f)
        for c in clients:
            ClientRepository.store_client(self, c)
        f.close()

    def _save_file(self):
        f = open(self._fileName, 'wb')
        pickle.dump(self.get_list_clients(), f)
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


class PickleRentalRepository(RentalRepository):
    def __init__(self, fileName, movieRepo, clientRepo):
        self._fileName = fileName
        super().__init__([], movieRepo, clientRepo)
        self._load_file()

    def _load_file(self):
        f = open(self._fileName, "rb")
        rentals = pickle.load(f)
        for r in rentals:
            RentalRepository.store_rental(self, r)
        f.close()

    def _save_file(self):
        f = open(self._fileName, 'wb')
        pickle.dump(self.get_list_rentals(), f)
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

