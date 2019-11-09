class Movie:
    def __init__(self,movieId,title,description,genre):
        self._movieId = movieId
        self._title = title
        self._description = description
        self._genre = genre
    def __str__(self):
        return "id: " + str(self._movieId) + ", title: " + self._title + ", description: " + self._description + ", genre: " + self._genre

class Client:
    def __init__(self,clientId,name):
        self._clientId = clientId
        self._name = name

class Rental:
    def __init__(self,rentalId,movieId,clientId,rentedDate,dueDate,returnedDate):
        self._rentalId = rentalId
        self._movieId = movieId
        self._clientId = clientId
        self._rentedDate = rentedDate
        self._dueDate = dueDate
        self._returnedDate = returnedDate