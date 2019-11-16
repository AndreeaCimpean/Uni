from domain import *


class MovieRepository:
    def __init__(self, movies):
        self._movies = movies

    def get_list_movies(self):
        return self._movies.copy()

    def find_by_id(self, movieId):
        '''
        Find a movie in the list of movies by its id
        params:
            movieId - the id of the searched movie
        return:
            the movie if found
            None otherwise
        '''
        for m in self._movies:
            if m.movieId == movieId:
                return m
        return None

    def store_movie(self, movie):
        '''
        Add a movie to the list of movies
        params:
            movie - the movie
        Add the movie to the list of movies if its id is unique
        Raise an error otherwise
        '''
        if self.find_by_id(movie.movieId) != None:
            raise ValueError("Id must be unique")
        self._movies.append(movie)

    def delete_movie(self, movieId):
        '''
        Delete a movie from the list of movies
        params:
            movieId - the id of the movie
        Delete the movie from the list of movies if found
        Raise an error otherwise
        '''
        movie = self.find_by_id(movieId)
        if movie == None:
            raise ValueError("Not such movie")
        self._movies.remove(movie)

    def update_movie(self, movieId, title, description, genre):
        movie = self.find_by_id(movieId)
        if movie == None:
            raise ValueError("Not such movie")
        movie.Title = title
        movie.Description = description
        movie.Genre = genre


class ClientRepository:
    def __init__(self, clients):
        self._clients = clients

    def get_list_clients(self):
        return self._clients.copy()

    def find_by_id(self, clientId):
        '''
        Find a client in the list of clients by its id
        params:
            cleintId - the id of the searched clientId
        return:
            the client if found
            None otherwise
        '''
        for c in self._clients:
            if c.clientId == clientId:
                return c
        return None

    def store_client(self, client):
        '''
        Add a client to the list of clients
        params:
            client - the client
        Add the client to the list of clients if its id is unique
        Raise an error otherwise
        '''
        if self.find_by_id(client.clientId) != None:
            raise ValueError("Id must be unique")
        self._clients.append(client)

    def delete_client(self, clientId):
        '''
        Delete a client from the list of clients
        params:
            clientId - the id of the client
        Delete the client from the list of clients if found
        Raise an error otherwise
        '''
        client = self.find_by_id(clientId)
        if client == None:
            raise ValueError("Not such client")
        self._clients.remove(client)

    def update_client(self, clientId, name):
        client = self.find_by_id(clientId)
        if client == None:
            raise ValueError("Not such client")
        client.Name = name


class RentalRepository:
    def __init__(self, rentals):
        self._rentals = rentals

    def get_list_rentals(self):
        return self._rentals.copy()

    def find_by_id(self, value):
        for r in self._rentals:
            if r.rentalId == value:
                return r
        return None

    def store_rental(self, rental):
        if self.find_by_id(rental.rentalId) != None:
            raise ValueError("Id must be unique")
        self._rentals.append(rental)

    def update_rental(self, rentalId, returnedDate):
        rental = self.find_by_id(rentalId)
        if rental == None:
            raise ValueError("There is no such rental")
        rental.reurnedDate = returnedDate


def test_find_movie_by_id():
    movies = []
    m1 = Movie("123", "A Movie", "Art", "romance")
    m2 = Movie("124", "The Second Movie", "New", "horror")
    movies.append(m1)
    movies.append(m2)
    movieRepo = MovieRepository(movies)
    assert movieRepo.find_by_id("123") != None
    assert movieRepo.find_by_id("1") == None


def test_store_movie():
    movies = []
    movieRepo = MovieRepository(movies)

    m1 = Movie("123", "A Movie", "Art", "romance")
    m2 = Movie("123", "The Second Movie", "New", "horror")

    movieRepo.store_movie(m1)
    assert movieRepo.get_list_movies()[0] == m1
    try:
        movieRepo.store_movie(m2)
        assert False
    except ValueError:
        assert True


def test_delete_movie():
    movies = []
    m1 = Movie("123", "A Movie", "Art", "romance")
    m2 = Movie("124", "The Second Movie", "New", "horror")
    movies.append(m1)
    movies.append(m2)
    movieRepo = MovieRepository(movies)
    movieRepo.delete_movie("123")
    assert movieRepo.get_list_movies()[0] != m1
    try:
        movieRepo.delete_movie("1")
        assert False
    except ValueError:
        assert True


def test_find_client_by_id():
    clients = []
    c1 = Client("123", "Jimmy Park")
    c2 = Client("124", "Anna Park")
    clients.append(c1)
    clients.append(c2)
    clientRepo = ClientRepository(clients)
    assert clientRepo.find_by_id("123") != None
    assert clientRepo.find_by_id("1") == None


def test_store_client():
    clients = []
    clientRepo = ClientRepository(clients)

    c1 = Client("123", "Jimmy Park")
    c2 = Client("123", "Anna Park")

    clientRepo.store_client(c1)
    assert clientRepo.get_list_clients()[0] == c1
    try:
        clientRepo.store_client(c2)
        assert False
    except ValueError:
        assert True


def test_delete_client():
    clients = []
    c1 = Client("123", "Jimmy Park")
    c2 = Client("124", "Anna Park")
    clients.append(c1)
    clients.append(c2)
    clientRepo = ClientRepository(clients)
    clientRepo.delete_client("123")
    assert clientRepo.get_list_clients()[0] != c1
    try:
        clientRepo.delete_client("1")
        assert False
    except ValueError:
        assert True


test_find_movie_by_id()
test_store_movie()
test_find_client_by_id()
test_store_client()
test_delete_movie()
test_delete_client()