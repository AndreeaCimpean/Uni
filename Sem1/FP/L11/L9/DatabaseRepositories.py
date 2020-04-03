import mysql.connector
from memoryRepositories import *
import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="AndreeaCimpean",
    passwd="jhdIG77@",
    database="moviesapp"
)

# creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor = mydb.cursor()


class DatabaseMovieRepository(MovieRepository):
    def __init__(self):
        super().__init__([])
        self._load_movies_table()

    def _load_movies_table(self):
        query = "SELECT * FROM movies"
        cursor.execute(query)
        movies = cursor.fetchall()
        for m in movies:
            newMovie = Movie(m[0], m[1], m[2], m[3])
            MovieRepository.store_movie(self, newMovie)

    def store_movie(self, movie):
        MovieRepository.store_movie(self, movie)
        query = "INSERT INTO movies(id, title, description, genre) VALUES (%s, %s, %s, %s)"
        m = (movie.movieId, movie.Title, movie.Description, movie.Genre)
        cursor.execute(query, m)
        mydb.commit()

    def delete_movie(self, movieId):
        movie = MovieRepository.delete_movie(self, movieId)
        query = "DELETE FROM movies WHERE id = %s"
        cursor.execute(query, (movieId,))
        mydb.commit()
        return movie

    def update_movie(self, movieId, title, description, genre):
        movie = MovieRepository.update_movie(self, movieId, title, description, genre)
        query = "UPDATE movies SET title = %s, description = %s, genre = %s WHERE id = %s"
        parameters = (title, description, genre, movieId)
        cursor.execute(query, parameters)
        mydb.commit()
        return movie


class DatabaseClientRepository(ClientRepository):
    def __init__(self):
        super().__init__([])
        self._load_clients_table()

    def _load_clients_table(self):
        query = "SELECT * FROM clients"
        cursor.execute(query)
        clients = cursor.fetchall()
        for c in clients:
            newClient = Client(c[0], c[1])
            ClientRepository.store_client(self, newClient)

    def store_client(self, client):
        ClientRepository.store_client(self, client)
        query = "INSERT INTO clients(id, name) VALUES (%s, %s)"
        c = (client.clientId, client.Name)
        cursor.execute(query, c)
        mydb.commit()

    def delete_client(self, clientId):
        client = ClientRepository.delete_client(self, clientId)
        query = "DELETE FROM clients WHERE id = %s"
        cursor.execute(query, (clientId,))
        mydb.commit()
        return client

    def update_client(self, clientId, name):
        client = ClientRepository.update_client(self, clientId, name)
        query = "UPDATE clients SET name = %s WHERE id = %s"
        parameters = (name, clientId)
        cursor.execute(query, parameters)
        mydb.commit()
        return client


class DatabaseRentalRepository(RentalRepository):
    def __init__(self, movieRepo, clientRepo):
        super().__init__([], movieRepo, clientRepo)
        self._load_rentals_table()

    def _load_rentals_table(self):
        query = "SELECT * FROM rentals"
        cursor.execute(query)
        rentals = cursor.fetchall()
        for r in rentals:
            newRental = Rental(r[0], r[1], r[2], r[3], r[4], r[5])
            RentalRepository.store_rental(self, newRental)

    def store_rental(self, rental):
        RentalRepository.store_rental(self, rental)
        if rental.returnedDate == None:
            query = "INSERT INTO rentals(id, movieId, clientId, rentedDate, dueDate) VALUES (%s, %s, %s, %s, %s)"
            r = (rental.rentalId, rental.movieId, rental.clientId,
                 datetime.datetime.strftime(rental.rentedDate, "%Y-%m-%d"),
                 datetime.datetime.strftime(rental.dueDate, "%Y-%m-%d"))
        else:
            query = "INSERT INTO rentals(id, movieId, clientId, rentedDate, dueDate, returnedDate) VALUES (%s, %s, %s, %s, %s, %s)"
            r = (rental.rentalId, rental.movieId, rental.clientId,
                 datetime.datetime.strftime(rental.rentedDate, "%Y-%m-%d"),
                 datetime.datetime.strftime(rental.dueDate, "%Y-%m-%d"),
                 datetime.datetime.strftime(rental.returnedDate, "%Y-%m-%d"))
        cursor.execute(query, r)
        mydb.commit()

    def delete_rental(self, rentalId):
        rental = RentalRepository.delete_rental(self, rentalId)
        query = "DELETE FROM rentals WHERE id = %s"
        cursor.execute(query, (rentalId,))
        mydb.commit()
        return rental

    def update_rental(self, clientId, movieId, returnedDate):
        rental = RentalRepository.update_rental(self, clientId, movieId, returnedDate)
        if returnedDate != None:
            query = "UPDATE rentals SET returnedDate = %s WHERE clientId = %s AND movieId = %s"
            parameters = (returnedDate, clientId, movieId)
        else:
            query = "UPDATE rentals SET returnedDate = NULL WHERE clientId = %s AND movieId = %s"
            parameters = (clientId, movieId)
        cursor.execute(query, parameters)
        mydb.commit()
        return rental

