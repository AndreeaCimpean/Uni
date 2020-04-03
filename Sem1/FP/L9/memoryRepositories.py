from domain import *
from exceptions import RepositoryException


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
            raise RepositoryException("Duplicate movie id: " + movie.movieId)
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
            raise RepositoryException("No movie with the id: " + movieId)
        self._movies.remove(movie)
        return movie

    def update_movie(self, movieId, title, description, genre):
        '''
        Update a movie
        params:
            movieId - the id of the movie
            title - the new title
            description - the new description
            genre - the new genre
        Update the movie
        '''
        movie = self.find_by_id(movieId)
        if movie == None:
            raise RepositoryException("No movie with the id: " + movieId)
        if len(title) > 0:
            movie.Title = title
        if len(description) > 0:
            movie.Description = description
        if len(genre) > 0:
            movie.Genre = genre
        return movie


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
            raise RepositoryException("Duplicate client id: " + client.clientId)
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
            raise RepositoryException("No client with the id: " + clientId)
        self._clients.remove(client)
        return client

    def update_client(self, clientId, name):
        '''
        Update a client
        params:
            clientId - the id of the client
            name - the new name
        Update the client
        '''
        client = self.find_by_id(clientId)
        if client == None:
            raise RepositoryException("No client with the id: " + clientId)
        client.Name = name
        return client


class RentalRepository:
    def __init__(self, rentals, movieRepo, clientRepo):
        self._rentals = rentals
        self.movieRepository = movieRepo
        self.clientRepository = clientRepo

    def get_list_rentals(self):
        return self._rentals.copy()

    def find_by_id(self, rentalId):
        for r in self._rentals:
            if r.rentalId == rentalId:
                return r
        return None

    def store_rental(self, rental):
        if self.movieRepository.find_by_id(rental.movieId) == None:
            raise RepositoryException("There is no movie with the id: " + rental.movieId)
        if self.clientRepository.find_by_id(rental.clientId) == None:
            raise RepositoryException("There is no client with the id: " + rental.clientId)
        if not self.is_movie_available(rental.movieId):
            raise RepositoryException("Movie with the id: " + rental.movieId + " is not available")
        if not self.can_rent(rental.clientId):
            raise RepositoryException("Client with the id:" + rental.clientId +
                                      " can not rent because due date for a movie passed, and still not returned")
        if self.find_by_id(rental.rentalId) != None:
            raise RepositoryException("Duplicate rental id: " + rental.rentalId)
        self._rentals.append(rental)

    def update_rental(self, clientId, movieId, returnedDate):
        if self.movieRepository.find_by_id(movieId) == None:
            raise RepositoryException("There is no movie with the id: " + movieId)
        if self.clientRepository.find_by_id(clientId) == None:
            raise RepositoryException("There is no client with the id: " + clientId)
        rental = self.find_rental_by_movie_and_client(clientId, movieId)
        if rental == None:
            raise RepositoryException("There is no such rental")
        rental.returnedDate = returnedDate

    def delete_rental(self, rentalId):
        rental = self.find_by_id(rentalId)
        if rental == None:
            raise RepositoryException("There is no rental with the id: " + rentalId)
        self._rentals.remove(rental)
        return rental

    def find_rental_by_movie_and_client(self, clientId, movieId):
        for r in self.get_list_rentals():
            if r.movieId == movieId and r.clientId == clientId:
                return r
        return None

    def is_movie_available(self, movieId):
        for r in self.get_list_rentals():
            if r.movieId == movieId and r.returnedDate == None:
                return False
        return True

    def can_rent(self, clientId):
        for r in self.get_list_rentals():
            if r.clientId == clientId and r.returnedDate == None and date.today() > r.dueDate:
                return False
        return True


