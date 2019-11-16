from repositories import *
from datetime import date, timedelta
import random


class MovieService:
    def __init__(self, movieRepo):
        self._movieRepository = movieRepo

    def get_movies(self):
        return self._movieRepository.get_list_movies()

    def get_movies_id(self):
        moviesids = []
        for m in self.get_movies():
            moviesids.append(m.movieId)
        return moviesids

    def add_movie(self, movie):
        '''
        Call repository function to add a new movie to the list
        params:
            movie - the movie
        '''
        self._movieRepository.store_movie(movie)

    def remove_movie(self, movieId):
        '''
        Call repository function to remove a movie from the list
        params:
            movieId - the id of the movie
        '''
        self._movieRepository.delete_movie(movieId)

    def update_movie(self, movieId, title, description, genre):
        self._movieRepository.update_movie(movieId, title, description, genre)


class ClientService:
    def __init__(self, clientRepo):
        self._clientRepository = clientRepo

    def get_clients(self):
        return self._clientRepository.get_list_clients()

    def get_clients_id(self):
        clientsids = []
        for c in self.get_clients():
            clientsids.append(c.clientId)
        return clientsids

    def add_client(self, client):
        '''
        Call repository function to add a new client to the list
        params:
            client - the client
        '''
        self._clientRepository.store_client(client)

    def remove_client(self, clientId):
        '''
        Call repository function to remove a client from the list
        params:
            clientId - the id of the client
        '''
        self._clientRepository.delete_client(clientId)

    def update_client(self, clientId, name):
        self._clientRepository.update_client(clientId, name)


class RentalService:
    def __init__(self, rentalRepo):
        self._rentalRepository = rentalRepo

    def get_rentals(self):
        return self._rentalRepository.get_list_rentals()

    def rent_movie(self, clientId, movieId):
        if not self.is_movie_available(movieId):
            raise ValueError("Movie is not availabale")
        if not self.can_rent(clientId):
            raise ValueError("Can not rent because due date for a movie passed, and still not returned")
        while True:
            try:
                rental = self.generate_rental(clientId, movieId)
                self._rentalRepository.store_rental(rental)
                break
            except ValueError:
                pass

    def generate_rental(self, clientId, movieId):
        rentalId = "R" + str(random.randint(100, 999))
        rentedDate = date.today()
        dueDate = rentedDate + timedelta(days=14)
        returnedDate = None
        return Rental(rentalId, movieId, clientId, rentedDate, dueDate, returnedDate)

    def is_movie_available(self, movieId):
        for r in self.get_rentals():
            if r.movieId == movieId and r.returnedDate == None:
                return False
        return True

    def can_rent(self, clientId):
        for r in self.get_rentals():
            if r.clientId == clientId and r.returnedDate == None and date.today() > r.dueDate:
                return False
        return True

    def return_movie(self, clientId, movieId):
        rentalId = self.find_rental_by_movia_and_client(movieId, clientId)
        self._rentalRepository.update_rental(rentalId, date.today())

    def find_rental_by_movia_and_client(self, clientId, movieId):
        for r in self.get_rentals():
            if r.movieId == movieId and r.clientId == clientId:
                return r.rentalId
