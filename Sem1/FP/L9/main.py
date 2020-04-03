from services import *

import datetime
from validators import *

from ui import *
from domain import *
import random
import names
from undoservice import *
from textRepositories import *
from pickleRepositories import *
import pickle
from exceptions import RepositoryException
from SettingsClass import *
from JSONRepositories import *
import mysql.connector
from DatabaseRepositories import *


def generate_client():
    clientId = "C" + str(random.randint(100, 999))
    name = names.get_full_name()
    return Client(clientId, name)


def generate_movie():
    descriptions = ["Blockbuster for 4 weeks", "A beautiful story", "Think about it", "New"]
    genres = ["horror", "drama", "comedy", "romance"]
    titles = {"first": ["The", "Good", "Gorgeous"],
              "second": ["Last", "Bad", "Final"],
              "third": ["Movie", "Chapter", "Grandma"]}

    movieId = "M" + str(random.randint(100, 999))
    title = titles["first"][random.randint(0, 2)]
    title += " "
    title += titles["second"][random.randint(0, 2)]
    title += " "
    title += titles["third"][random.randint(0, 2)]
    description = descriptions[random.randint(0, 3)]
    genre = genres[random.randint(0, 3)]
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
                rentedDate = datetime.date(2019, random.randint(1, 12), random.randint(1, 31))
                if rentedDate <= datetime.date.today():
                    break
            except ValueError:
                pass
        dueDate = rentedDate + datetime.timedelta(days=14)
        while True:
            try:
                returnedDate = datetime.date(2019, random.randint(1, 12), random.randint(1, 31))
                if returnedDate > rentedDate and returnedDate <= datetime.date.today():
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
                rentedDate = datetime.date(2019, random.randint(1, 12), random.randint(1, 31))
                if rentedDate <= datetime.date.today():
                    break
            except ValueError:
                pass
        dueDate = rentedDate + datetime.timedelta(days=14)
        returnedDate = None
        rental = Rental(rentalId, movieId, clientId, rentedDate, dueDate, returnedDate)
        rentals.append(rental)
    return rentals


def memory_repository_start():
    clients = generate_list_of_clients()
    movies = generate_list_of_movies()
    rentals = generate_list_of_rentals(movies, clients)

    movieRepo = MovieRepository(movies)
    clientRepo = ClientRepository(clients)
    rentalRepo = RentalRepository(rentals, movieRepo, clientRepo)

    return (movieRepo, clientRepo, rentalRepo)


def text_repository_start(moviesFile, clientsFile, rentalsFile):
    try:
        movieRepo = TextMovieRepository(moviesFile)
    except RepositoryException as e:
        print(str(e) + " in " + str(moviesFile))
        return None
    try:
        clientRepo = TextClientRepository(clientsFile)
    except RepositoryException as e:
        print(str(e) + " in " + str(clientsFile))
        return None
    try:
        rentalRepo = TextRentalRepository(rentalsFile, movieRepo, clientRepo)
    except RepositoryException as e:
        print(str(e) + " in " + str(rentalsFile))
        return None

    return (movieRepo, clientRepo, rentalRepo)


def write_in_pickle_files(moviesFile, clientsFile, rentalsFile):
    clients = generate_list_of_clients()
    movies = generate_list_of_movies()
    rentals = generate_list_of_rentals(movies, clients)

    f = open(moviesFile, "wb")
    pickle.dump(movies, f)
    f.close()

    f = open(clientsFile, "wb")
    pickle.dump(clients, f)
    f.close()

    f = open(rentalsFile, "wb")
    pickle.dump(rentals, f)
    f.close()


def pickle_repository_start(moviesFile, clientsFile, rentalsFile):
    # write_in_pickle_files(moviesFile, clientsFile, rentalsFile)
    try:
        movieRepo = PickleMovieRepository(moviesFile)
    except RepositoryException as e:
        print(str(e) + " in " + str(moviesFile))
        return None
    try:
        clientRepo = PickleClientRepository(clientsFile)
    except RepositoryException as e:
        print(str(e) + " in " + str(clientsFile))
        return None
    try:
        rentalRepo = PickleRentalRepository(rentalsFile, movieRepo, clientRepo)
    except RepositoryException as e:
        print(str(e) + " in " + str(rentalsFile))
        return None

    return (movieRepo, clientRepo, rentalRepo)


def json_repository_start(moviesFile, clientsFile, rentalsFile):
    try:
        movieRepo = JSONMovieRepository(moviesFile)
    except RepositoryException as e:
        print(str(e) + " in " + str(moviesFile))
        return None
    try:
        clientRepo = JSONClientRepository(clientsFile)
    except RepositoryException as e:
        print(str(e) + " in " + str(clientsFile))
        return None
    try:
        rentalRepo = JSONRentalRepository(rentalsFile, movieRepo, clientRepo)
    except RepositoryException as e:
        print(str(e) + " in " + str(rentalsFile))
        return None

    return (movieRepo, clientRepo, rentalRepo)


def write_in_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="AndreeaCimpean",
        passwd="jhdIG77@",
        database="moviesapp"
    )
    cursor = mydb.cursor()

    movies = generate_list_of_movies()
    clients = generate_list_of_clients()
    rentals = generate_list_of_rentals(movies, clients)
    rentals_with_return_date = []
    rentals_without_return_date = []
    for i in range(0, len(rentals)):
        r = rentals[i]
        if r.returnedDate != None:
            rentals_with_return_date.append((r.rentalId, r.movieId, r.clientId,
                                            datetime.datetime.strftime(r.rentedDate, "%Y-%m-%d"),
                                            datetime.datetime.strftime(r.dueDate, "%Y-%m-%d"),
                                            datetime.datetime.strftime(r.returnedDate, "%Y-%m-%d")))
        else:
            rentals_without_return_date.append((r.rentalId, r.movieId, r.clientId,
                                                datetime.datetime.strftime(r.rentedDate, "%Y-%m-%d"),
                                                datetime.datetime.strftime(r.dueDate, "%Y-%m-%d")))

    for i in range(0, len(movies)):
        m = movies[i]
        movies[i] = (m.movieId, m.Title, m.Description, m.Genre)
    for i in range(0, len(clients)):
        c = clients[i]
        clients[i] = (c.clientId, c.Name)

    query = "DELETE FROM clients"
    cursor.execute(query)
    query = "DELETE FROM movies"
    cursor.execute(query)
    query = "DELETE FROM rentals"
    cursor.execute(query)

    query_insert_movies = "INSERT INTO movies (id, title, description, genre) VALUES (%s, %s, %s, %s)"
    cursor.executemany(query_insert_movies, movies)
    mydb.commit()

    query_insert_clients = "INSERT INTO clients(id, name) VALUES (%s, %s)"
    cursor.executemany(query_insert_clients, clients)
    mydb.commit()

    query_insert_rentals_with_return_date = "INSERT INTO rentals(id, movieId, clientId, rentedDate, dueDate, returnedDate) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.executemany(query_insert_rentals_with_return_date, rentals_with_return_date)
    mydb.commit()

    query_insert_rentals_without_return_date = "INSERT INTO rentals(id, movieId, clientId, rentedDate, dueDate) VALUES (%s, %s, %s, %s, %s)"
    cursor.executemany(query_insert_rentals_without_return_date, rentals_without_return_date)
    mydb.commit()

def database_repository_start():
    try:
        movieRepo = DatabaseMovieRepository()
    except RepositoryException as e:
        print(str(e) + " in movies table")
        return None
    try:
        clientRepo = DatabaseClientRepository()
    except RepositoryException as e:
        print(str(e) + " in client table")
        return None
    try:
        rentalRepo = DatabaseRentalRepository(movieRepo, clientRepo)
    except RepositoryException as e:
        print(str(e) + " in rental table")
        return None
    
    return (movieRepo, clientRepo, rentalRepo) 

def start_program():

    settings = Settings("settings.properties")

    if settings.RepositoryType == "inmemory":
        repositories = memory_repository_start()
    elif settings.RepositoryType == "textfiles":
        repositories = text_repository_start(settings.MoviesFile, settings.ClientsFile, settings.RentalsFile)
    elif settings.RepositoryType == "binaryfiles":
        repositories = pickle_repository_start(settings.MoviesFile, settings.ClientsFile, settings.RentalsFile)
    elif settings.RepositoryType == "jsonfiles":
        repositories = json_repository_start(settings.MoviesFile, settings.ClientsFile, settings.RentalsFile)
    elif settings.RepositoryType == "database":
        repositories = database_repository_start()
    else:
        print("Invalid repository type")
        return

    if repositories != None:
        movieRepo = repositories[0]
        clientRepo = repositories[1]
        rentalRepo = repositories[2]

        movieValidator = MovieValidator()
        clientValidator = ClientValidator()
        rentalValidator = RentalValidator()

        undoServ = UndoService()

        rentalServ = RentalService(rentalRepo, rentalValidator, undoServ)
        movieServ = MovieService(movieRepo, movieValidator, undoServ, rentalServ)
        clientServ = ClientService(clientRepo, clientValidator, rentalServ, undoServ)

        ui = UI(movieServ, clientServ, rentalServ, undoServ)
        ui.start()


# write_in_database()

start_program()

