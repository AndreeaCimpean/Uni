from datetime import date


class Movie:
    def __init__(self, mid, title, description, genre):
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

    def to_dictionary(self):
        return {"id": self.movieId, "title": self.Title, "description": self.Description, "genre": self.Genre}


class Client:
    def __init__(self, cid, name):
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

    def to_dictionary(self):
        return {"id": self.clientId, "name": self.Name}


class Rental:
    def __init__(self, rid, mid, cid, rented, due, returned):
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

    def to_dictionary(self):
        return {"id": self.rentalId, "movieId": self.movieId, "clientId": self.clientId, "rentedDate": str(self.rentedDate), "dueDate": str(self.dueDate), "returnedDate": str(self.returnedDate)}
    
    def __len__(self):
        if self._returnedDate != None:
            return int((self._returnedDate - self._rentedDate).days) + 1
        else:
            return int((date.today() - self.rentedDate).days) + 1

    def delay_days(self):
        if self.is_late():
            return int((date.today() - self.dueDate).days)
        return 0

    def is_late(self):
        return self.returnedDate == None and self.dueDate < date.today()

