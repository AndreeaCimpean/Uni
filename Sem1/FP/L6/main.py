from services import *
from datetime import date, timedelta

from ui import *
from domain import *
import random
import names


def generate_client():
    clientId = "C" + str(random.randint(100,999))
    name = names.get_full_name()
    return Client(clientId, name)


def generate_movie():
    descriptions = ["Blockbuster for 4 weeks", "A beautiful story", "Think about it"]
    genres = ["horror", "drama", "comedy", "romance"]
    titles = {"first": ["The", "Good", "Gorgeous"], "second": ["Last", "Bad", "Final"], "third": ["Movie", "Chapter", "Grandma"]}

    movieId = "M" + str(random.randint(100, 999))
    title = titles["first"][random.randint(0, 2)]
    title += " "
    title += titles["second"][random.randint(0, 2)]
    title += " "
    title += titles["third"][random.randint(0, 2)]
    description = descriptions[random.randint(0,2)]
    genre = genres[random.randint(0,3)]
    return Movie(movieId, title, description, genre)


def find_client_in_list(clients, clientId):
    for c in clients:
        if c.clientId == clientId:
            return True
    return False


def generate_list_of_clients():
    clients = []
    client = generate_client()
    clients.append(client)
    i = 1
    while i < 10:
        client = generate_client()
        while find_client_in_list(clients, client.clientId):
            client = generate_client()
        clients.append(client)
        i += 1
    return clients


def find_movie_in_list(movies, movieId):
    for m in movies:
        if m.movieId == movieId:
            return True
    return False


def generate_list_of_movies():
    movies = []
    movie = generate_movie()
    movies.append(movie)
    i = 1
    while i < 10:
        movie = generate_movie()
        while find_movie_in_list(movies, movie.movieId):
            movie = generate_movie()
        movies.append(movie)
        i += 1
    return movies


def find_rental_in_list(rentals, rentalId):
    for r in rentals:
        if r.rentalId == rentalId:
            return True
    return False


def generate_list_of_rentals(movies, clients):
    rentals = []
    for i in range(0, 5):
        movieId = movies[i].movieId
        clientId = clients[i].clientId
        rentalId = "R" + str(random.randint(100, 999))
        while find_rental_in_list(rentals, rentalId):
            rentalId = "R" + str(random.randint(100, 999))

        while True:
            try:
                rentedDate = date(2019, random.randint(1, 12), random.randint(1, 31))
                if rentedDate <= date.today():
                    break
            except ValueError:
                pass
        dueDate = rentedDate + timedelta(days=14)
        while True:
            try:
                returnedDate = date(2019, random.randint(1, 12), random.randint(1, 31))
                if returnedDate > rentedDate and returnedDate <= date.today():
                    break
            except ValueError:
                pass
        rental = Rental(rentalId, movieId, clientId, rentedDate, dueDate, returnedDate)
        rentals.append(rental)

    for i in range(5, len(movies)):
        movieId = movies[i].movieId
        clientId = clients[i].clientId
        rentalId = "R" + str(random.randint(100, 999))
        while find_rental_in_list(rentals, rentalId):
            rentalId = "R" + str(random.randint(100, 999))

        while True:
            try:
                rentedDate = date(2019, random.randint(1, 12), random.randint(1, 31))
                if rentedDate <= date.today():
                    break
            except ValueError:
                pass
        dueDate = rentedDate + timedelta(days=14)
        returnedDate = None
        rental = Rental(rentalId, movieId, clientId, rentedDate, dueDate, returnedDate)
        rentals.append(rental)
    return rentals


clients = generate_list_of_clients()
movies = generate_list_of_movies()
rentals = generate_list_of_rentals(movies, clients)

movieRepo = MovieRepository(movies)
movieServ = MovieService(movieRepo)
clientRepo = ClientRepository(clients)
clientServ = ClientService(clientRepo)
rentalRepo = RentalRepository(rentals)
rentalServ = RentalService(rentalRepo)
ui = UI(movieServ, clientServ, rentalServ)
ui.start()