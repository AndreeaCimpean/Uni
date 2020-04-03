from domain import *
from exceptions import ValidatorException

class ClientValidator:
    def validate(self, client):
        if isinstance(client, Client) == False:
            raise TypeError("Can only validate Client objects!")
        _errors = []
        if len(client.clientId) == 0:
            _errors.append("Client id can not be empty")
        if len(client.Name) == 0:
            _errors.append("Client must have a name")
        if len(_errors) != 0:
            raise ValidatorException(_errors)
        return True


class MovieValidator:
    def validate(self, movie):
        if isinstance(movie, Movie) == False:
            raise TypeError("Can only validate Movie objects!")
        _errors = []
        if len(movie.movieId) == 0:
            _errors.append("Movie id can not be empty")
        if len(movie.Title) == 0:
            _errors.append("Movie must have a name")
        if len(movie.Description) == 0:
            _errors.append("Movie must have a description")
        if len(movie.Genre) == 0:
            _errors.append("Movie must have a genre")
        if len(_errors) != 0:
            raise ValidatorException(_errors)
        return True


class RentalValidator:
    def validate(self, rental):
        if isinstance(rental, Rental) == False:
            raise TypeError("Can only validate Rental objects!")
        _errors = []
        if len(rental.rentalId) == 0:
            _errors.append("Id must not be empty")
        if len(rental.clientId) == 0:
            _errors.append("Client Id must not be empty")
        if len(rental.movieId) == 0:
            _errors.append("Movie Id must not be empty")
        if rental.dueDate < rental.rentedDate:
            _errors.append("Due date must be after rent date")
        if rental.returnedDate != None:
            if rental.returnedDate < rental.rentedDate:
                _errors.append("Returned date must be after rent date")
        if len(_errors) != 0:
            raise ValidatorException(_errors)
        return True
