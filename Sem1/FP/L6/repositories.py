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
            raise MovieException("Id must be unique")
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
            raise MovieException("Not such movie")
        self._movies.remove(movie)

    def update_movie(self, movieId, title, description, genre):
        '''
        Update a movie
        params:
            movieId - the id of the movie
            title - the new title
            description - the new description
            genre - the new genre
        Update the movie if found
        Raise an error otherwise
        '''
        movie = self.find_by_id(movieId)
        if movie == None:
            raise MovieException("Not such movie")
        if len(title) > 0:
            movie.Title = title
        if len(description) > 0:
            movie.Description = description
        if len(genre) > 0:
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
            raise ClientException("Id must be unique")
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
            raise ClientException("Not such client")
        self._clients.remove(client)

    def update_client(self, clientId, name):
        '''
        Update a client
        params:
            clientId - the id of the client
            name - the new name
        Update the client if found
        Raise an error otherwise
        '''
        client = self.find_by_id(clientId)
        if client == None:
            raise ClientException("Not such client")
        client.Name = name


class RentalRepository:
    def __init__(self, rentals):
        self._rentals = rentals

    def get_list_rentals(self):
        return self._rentals.copy()

    def find_by_id(self, rentalId):
        for r in self._rentals:
            if r.rentalId == rentalId:
                return r
        return None

    def store_rental(self, rental):
        if self.find_by_id(rental.rentalId) != None:
            raise RentalException("Id must be unique")
        self._rentals.append(rental)

    def update_rental(self, rentalId, returnedDate):
        rental = self.find_by_id(rentalId)
        if rental == None:
            raise RentalException("There is no such rental")
        rental.returnedDate = returnedDate

    def delete_rental(self, rentalId):
        rental = self.find_by_id(rentalId)
        self._rentals.remove(rental)
