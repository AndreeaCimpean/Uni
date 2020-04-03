
from memoryRepositories import *
import datetime
from undoservice import *
import random
from fuzzywuzzy import fuzz


class MovieService:
    def __init__(self, movieRepo, validator, undoService, rentalService):
        self.__validator = validator
        self._movieRepository = movieRepo
        self._rentalService = rentalService
        self._undoService = undoService

    def get_movies(self):
        return self._movieRepository.get_list_movies()

    def get_movies_id(self):
        moviesids = []
        for m in self.get_movies():
            moviesids.append(m.movieId)
        return moviesids

    def add_movie(self, movieId, title, description, genre):
        '''
        Call repository function to add a new movie to the list
        params:
            movie - the movie
        '''
        movie = Movie(movieId, title, description, genre)
        self.__validator.validate(movie)
        self._movieRepository.store_movie(movie)

        redo = FunctionCall(self.add_movie, movieId, title, description, genre)
        undo = FunctionCall(self.remove_movie, movieId)
        op = Operation(undo, redo)
        self._undoService.recordOperation(op)

    def remove_movie(self, movieId, inUndoRedo=False):
        '''
        Call repository function to remove a movie from the list
        params:
            movieId - the id of the movie
        '''

        movie = self._movieRepository.delete_movie(movieId)

        undo = FunctionCall(self.add_movie, movieId, movie.Title, movie.Description, movie.Genre)
        redo = FunctionCall(self.remove_movie, movieId, True)
        op = Operation(undo, redo)
        listOp = []
        listOp.append(op)

        rentals = self._rentalService.find_movie_rentals(movieId)
        for rent in rentals:
            undo = FunctionCall(self._rentalService.create_rental, rent.rentalId, rent.movieId, rent.clientId, rent.rentedDate, rent.dueDate, rent.returnedDate, False)
            redo = FunctionCall(self._rentalService.delete_rental, rent.rentalId, False)
            op = Operation(undo, redo)
            listOp.append(op)

        cascadeOp = CascadeOperation(listOp)
        self._undoService.recordOperation(cascadeOp)

        if inUndoRedo == False:
            for rent in rentals:
                self._rentalService.delete_rental(rent.rentalId, False)

    def update_movie(self, movieId, title, description, genre):
        '''
        Call repository function to update a movie
        params:
            movieId - the id of the movie
            title - the new title
            description - the new description
            genre - the new genre
        '''
        movieBefore = self._movieRepository.find_by_id(movieId)

        if movieBefore != None:
            oldTitle = movieBefore.Title
            oldDescription = movieBefore.Description
            oldGenre = movieBefore.Genre

        movieAfter = self._movieRepository.update_movie(movieId, title, description, genre)

        undo = FunctionCall(self.update_movie, movieId, oldTitle, oldDescription, oldGenre)
        redo = FunctionCall(self.update_movie, movieId, movieAfter.Title, movieAfter.Description, movieAfter.Genre)
        op = Operation(undo, redo)
        self._undoService.recordOperation(op)

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
    def __init__(self, clientRepo, validator, rentalService, undoService):
        self._clientRepository = clientRepo
        self.__validator = validator
        self._rentalService = rentalService
        self._undoService = undoService

    def get_clients(self):
        return self._clientRepository.get_list_clients()

    def get_clients_id(self):
        clientsids = []
        for c in self.get_clients():
            clientsids.append(c.clientId)
        return clientsids

    def add_client(self, clientId, name):
        '''
        Call repository function to add a new client to the list
        params:
            client - the client
        '''
        client = Client(clientId, name)
        self.__validator.validate(client)
        self._clientRepository.store_client(client)

        redo = FunctionCall(self.add_client, clientId, name)
        undo = FunctionCall(self.remove_client, clientId)
        op = Operation(undo, redo)
        self._undoService.recordOperation(op)

    def remove_client(self, clientId, inUndoRedo=False):
        '''
        Call repository function to remove a client from the list
        params:
            clientId - the id of the client
        '''
        client = self._clientRepository.delete_client(clientId)

        undo = FunctionCall(self.add_client, clientId, client.Name)
        redo = FunctionCall(self.remove_client, clientId, True)
        op = Operation(undo, redo)
        listOp = []
        listOp.append(op)

        rentals = self._rentalService.find_client_rentals(clientId)
        for rent in rentals:
            undo = FunctionCall(self._rentalService.create_rental, rent.rentalId, rent.movieId, rent.clientId,
                                rent.rentedDate, rent.dueDate, rent.returnedDate, False)
            redo = FunctionCall(self._rentalService.delete_rental, rent.rentalId, False)
            op = Operation(undo, redo)
            listOp.append(op)

        cascadeOp = CascadeOperation(listOp)
        self._undoService.recordOperation(cascadeOp)

        if inUndoRedo == False:
            for rent in rentals:
                self._rentalService.delete_rental(rent.rentalId, False)

    def update_client(self, clientId, name):
        '''
        Call repository function to update a client
        params:
            clientId - the id of the client
            name - the new name
        '''
        clientBefore = self._clientRepository.find_by_id(clientId)
        if clientBefore != None:
            oldName = clientBefore.Name

        clientAfter = self._clientRepository.update_client(clientId, name)
        undo = FunctionCall(self.update_client, clientId, oldName)
        redo = FunctionCall(self.update_client, clientId, clientAfter.Name)
        op = Operation(undo, redo)
        self._undoService.recordOperation(op)

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
    def __init__(self, rentalRepo, validator, undoService):
        self._rentalRepository = rentalRepo
        self.__validator = validator
        self._undoService = undoService

    def get_rentals(self):
        return self._rentalRepository.get_list_rentals()

    def find_movie_rentals(self, movieId):
        rentals = []
        for r in self.get_rentals():
            if r.movieId == movieId:
                rentals.append(r)
        return rentals

    def find_client_rentals(self, clientId):
        rentals = []
        for r in self.get_rentals():
            if r.clientId == clientId:
                rentals.append(r)
        return rentals

    def create_rental(self, rentalId, movieId, clientId, rented, due, returned, recordUndo=True):
        rental = Rental(rentalId, movieId, clientId, rented, due, returned)
        self.__validator.validate(rental)
        self._rentalRepository.store_rental(rental)

        if recordUndo == True:
            redo = FunctionCall(self.create_rental, rentalId, movieId, clientId, rented, due, returned)
            undo = FunctionCall(self.delete_rental, rentalId)
            op = Operation(undo, redo)
            self._undoService.recordOperation(op)

    def delete_rental(self, rentalId, recordUndo=True):
        rental = self._rentalRepository.delete_rental(rentalId)
        if recordUndo == True:
            redo = FunctionCall(self.delete_rental, rentalId)
            undo = FunctionCall(self.create_rental, rentalId, rental.movieId, rental.clientId, rental.rentedDate, rental.dueDate, rental.returnedDate)
            op = Operation(undo, redo)
            self._undoService.recordOperation(op)

    def generate_rental(self, clientId, movieId):
        rentalId= "R" + str(random.randint(100, 999))
        while self._rentalRepository.find_by_id(rentalId) != None:
            rentalId= "R" + str(random.randint(100, 999))
        rentedDate = datetime.date.today()
        dueDate = rentedDate + datetime.timedelta(days=14)
        returnedDate = None
        self.create_rental(rentalId, movieId, clientId, rentedDate, dueDate, returnedDate)

    def return_movie(self, clientId, movieId, inUndoRedo=False):
        if inUndoRedo == False and self.is_returned(clientId, movieId) == True:
            raise Exception("Already returned")
        self._rentalRepository.update_rental(clientId, movieId, date.today())
        undo = FunctionCall(self._rentalRepository.update_rental, clientId, movieId, None)
        redo = FunctionCall(self.return_movie, clientId, movieId, True)
        op = Operation(undo, redo)
        self._undoService.recordOperation(op)

    def is_returned(self, clientId, movieId):
        for r in self.get_rentals():
            if r.clientId == clientId and r.movieId == movieId and r.returnedDate != None:
                return True
        return False

    def most_rented_movies(self):
        d = dict()
        for i in range(len(self.get_rentals())):
            rent = self.get_rentals()[i]
            if rent.movieId not in d.keys():
                d[rent.movieId] = len(rent)
            else:
                d[rent.movieId] += len(rent)

        result = []
        for i in range(len(self._rentalRepository.movieRepository.get_list_movies())):
            movie = self._rentalRepository.movieRepository.get_list_movies()[i]
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
        for i in range(len(self._rentalRepository.clientRepository.get_list_clients())):
            client = self._rentalRepository.clientRepository.get_list_clients()[i]
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
        for i in range(len(self._rentalRepository.movieRepository.get_list_movies())):
            movie = self._rentalRepository.movieRepository.get_list_movies()[i]
            if movie.movieId in d.keys():
                result.append(MovieDays(movie, d[movie.movieId]))

        result.sort(key=lambda x: x.Days, reverse=True)
        return result