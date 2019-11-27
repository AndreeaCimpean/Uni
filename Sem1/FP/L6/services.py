from repositories import *
from datetime import date, timedelta
import random
from fuzzywuzzy import fuzz


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
        '''
        Call repository function to update a movie
        params:
            movieId - the id of the movie
            title - the new title
            description - the new description
            genre - the new genre
        '''
        self._movieRepository.update_movie(movieId, title, description, genre)

    def search_movie_by_id(self, movieId):
        movies = []
        for m in self.get_movies():
            #if fuzz.partial_ratio(movieId, m.movieId.lower()) > 50:
            if movieId in m.movieId.lower():
                movies.append(m)
        return movies

    def search_movie_by_title(self, title):
        movies = []
        for m in self.get_movies():
            #if fuzz.partial_ratio(title, m.Title.lower()) > 50:
            if title in m.Title.lower():
                movies.append(m)
        return movies

    def search_movie_by_description(self, description):
        movies = []
        for m in self.get_movies():
            #if fuzz.partial_ratio(description, m.Description.lower()) > 50:
             if description in m.Description.lower():
                movies.append(m)
        return movies

    def search_movie_by_genre(self, genre):
        movies = []
        for m in self.get_movies():
            #if fuzz.partial_ratio(genre, m.Genre.lower()) > 50:
             if genre in m.Genre.lower():
                movies.append(m)
        return movies


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
        '''
        Call repository function to update a client
        params:
            clientId - the id of the client
            name - the new name
        '''
        self._clientRepository.update_client(clientId, name)

    def search_client_by_id(self, clientId):
        clients = []
        for c in self.get_clients():
            #if fuzz.partial_ratio(clientId, c.clientId.lower()) > 50:
             if clientId in c.clientId.lower():
                clients.append(c)
        return clients

    def search_client_by_name(self, name):
        clients = []
        for c in self.get_clients():
            #if fuzz.partial_ratio(name, c.Name.lower()) > 70:
             if name in c.Name.lower():
                clients.append(c)
        return clients


class MovieDays:
    def __init__(self, movie, days):
        self._movie = movie
        self._days = days

    @property
    def Movie(self):
        return self._movie

    @property
    def Days(self):
        return self._days

    def __str__(self):
        return str(self.Days) + " days - " + str(self.Movie)


class ClientRentalDays:
    def __init__(self, client, days):
        self._client = client
        self._days = days

    @property
    def Client(self):
        return self._client

    @property
    def Days(self):
        return self._days

    def __str__(self):
        return str(self.Days) + " days - " + str(self.Client)


class RentalService:
    def __init__(self, rentalRepo, movieRepo, clientRepo):
        self._rentalRepository = rentalRepo
        self._movieRepository = movieRepo
        self._clientRepository = clientRepo

    def get_rentals(self):
        return self._rentalRepository.get_list_rentals()

    def rent_movie(self, clientId, movieId):
        if not self.is_movie_available(movieId):
            raise RentalException("Movie is not available")
        if not self.can_rent(clientId):
            raise RentalException("Can not rent because due date for a movie passed, and still not returned")
        while True:
            try:
                rental = self.generate_rental(clientId, movieId)
                self._rentalRepository.store_rental(rental)
                break
            except RentalException:
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
        rentalId = self.find_rental_by_movie_and_client(clientId, movieId)
        self._rentalRepository.update_rental(rentalId, date.today())

    def find_rental_by_movie_and_client(self, clientId, movieId):
        for r in self.get_rentals():
            if r.movieId == movieId and r.clientId == clientId and r.returnedDate == None:
                return r.rentalId
        return None

    def delete_all_rentals_client(self, clientId):
        i = 0
        while i < len(self.get_rentals()):
            if self.get_rentals()[i].clientId == clientId:
                self._rentalRepository.delete_rental(self.get_rentals()[i].rentalId)
            else:
                i += 1

    def delete_all_rentals_movie(self, movieId):
        i = 0
        while i < len(self.get_rentals()):
            if self.get_rentals()[i].movieId == movieId:
                self._rentalRepository.delete_rental(self.get_rentals()[i].rentalId)
            else:
                i += 1

    def most_rented_movies(self):
        d = dict()
        for i in range(len(self.get_rentals())):
            rent = self.get_rentals()[i]
            if rent.movieId not in d.keys():
                d[rent.movieId] = len(rent)
            else:
                d[rent.movieId] += len(rent)

        result = []
        for i in range(len(self._movieRepository.get_list_movies())):
            movie = self._movieRepository.get_list_movies()[i]
            try:
                result.append(MovieDays(movie, d[movie.movieId]))
            except KeyError:
                result.append(MovieDays(movie, 0))
        result.sort(key=lambda x: x.Days, reverse=True)
        return result

    def most_active_clients(self):
        d = dict()
        for i in range(len(self.get_rentals())):
            rent = self.get_rentals()[i]
            if rent.clientId not in d.keys():
                d[rent.clientId] = len(rent)
            else:
                d[rent.clientId] += len(rent)

        result = []
        for i in range(len(self._clientRepository.get_list_clients())):
            client = self._clientRepository.get_list_clients()[i]
            try:
                result.append(ClientRentalDays(client, d[client.clientId]))
            except KeyError:
                result.append(ClientRentalDays(client, 0))
        result.sort(key=lambda x: x.Days, reverse=True)
        return result

    def late_rentals(self):
        d = dict()
        for i in range(len(self.get_rentals())):
            rent = self.get_rentals()[i]
            if rent.is_late():
                if rent.movieId not in d.keys():
                    d[rent.movieId] = rent.delay_days()
                else:
                    d[rent.movieId] += rent.delay_days()

        result = []
        for i in range(len(self._movieRepository.get_list_movies())):
            movie = self._movieRepository.get_list_movies()[i]
            if movie.movieId in d.keys():
                result.append(MovieDays(movie, d[movie.movieId]))

        result.sort(key=lambda x: x.Days, reverse=True)
        return result