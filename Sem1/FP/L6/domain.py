class MovieException(Exception):

    def __init__(self, message):
        super().__init__(message)


class ClientException(Exception):

    def __init__(self, message):
        super().__init__(message)


class RentalException(Exception):

    def __init__(self, message):
        super().__init__(message)


class Movie:
    def __init__(self, mid, title, description, genre):
        if len(mid) == 0:
            raise MovieException("Id must not be empty")
        if len(title) == 0:
            raise MovieException("Title must not be empty")
        if len(description) == 0:
            raise MovieException("Description must not be empty")
        if len(genre) == 0:
            raise MovieException("Genre must not be empty")
        self._movieId = mid
        self.Title = title
        self.Description = description
        self.Genre = genre

    @property
    def movieId(self):
        return self._movieId

    @property
    def Title(self):
        return self._title

    @Title.setter
    def Title(self, title):
        self._title = title

    @property
    def Description(self):
        return self._description

    @Description.setter
    def Description(self, description):
        self._description = description

    @property
    def Genre(self):
        return self._genre

    @Genre.setter
    def Genre(self, genre):
        self._genre = genre

    def __str__(self):
        return "id: " + self._movieId + \
               ", title: " + self._title + \
               ", description: " + self._description + \
               ", genre: " + self._genre


class Client:
    def __init__(self, cid, name):
        if len(cid) == 0:
            raise ClientException("Id must not be empty")
        if len(name) == 0:
            raise ClientException("Name must not be empty")
        self._clientId = cid
        self.Name = name

    @property
    def clientId(self):
        return self._clientId

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, name):
        self._name = name

    def __str__(self):
        return "id: " + self._clientId + ", name: " + self._name


class Rental:
    def __init__(self, rid, mid, cid, rented, due, returned):
        if len(rid) == 0:
            raise RentalException("Id must not be empty")
        if len(cid) == 0:
            raise RentalException("Client Id must not be empty")
        if len(mid) == 0:
            raise RentalException("Movie Id must not be empty")
        self._rentalId = rid
        self._movieId = mid
        self._clientId = cid
        self._rentedDate = rented
        self._dueDate = due
        self.returnedDate = returned

    @property
    def rentalId(self):
        return self._rentalId

    @property
    def movieId(self):
        return self._movieId

    @property
    def clientId(self):
        return self._clientId

    @property
    def rentedDate(self):
        return self._rentedDate

    @property
    def dueDate(self):
        return self._dueDate

    @property
    def returnedDate(self):
        return self._returnedDate

    @returnedDate.setter
    def returnedDate(self, date):
        self._returnedDate = date

    def __str__(self):
        return "id: " + self._rentalId + \
               ", movieId: " + self._movieId + \
               ", clientId: " + self._clientId + \
               ", rentedDate: " + str(self._rentedDate) + \
               ", dueDate: " + str(self._dueDate) + \
               ", returnedDate: " + str(self.returnedDate)
