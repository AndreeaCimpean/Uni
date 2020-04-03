import unittest
from repositories import *
from domain import *
from services import *
from datetime import date, timedelta
from validators import *
from exceptions import *
from undoservice import *
# from main import generate_list_of_movies, generate_list_of_clients


'''class TestMain(unittest.TestCase):
    def test_list_movies(self):
        movies = generate_list_of_movies()
        for i in range(len(movies) - 1):
            for j in range(i+1, len(movies)):
                self.assertNotEqual(movies[i].movieId, movies[j].movieId)
    def test_list_clients(self):
        clients = generate_list_of_clients()
        self.assertEqual(True, True)
'''

class TestMovieDomain(unittest.TestCase):

    def test_create_movie(self):
        m = Movie("123", "A Movie", "Art", "drama")
        self.assertEqual(m.movieId, "123")
        self.assertEqual(m.Title, "A Movie")
        self.assertEqual(m.Description, "Art")
        self.assertEqual(m.Genre, "drama")

    def test_str_movie(self):
        m = Movie("123", "A Movie", "New", "drama")
        self.assertEqual(str(m), "id: 123, title: A Movie, description: New, genre: drama")


class TestMovieValidator(unittest.TestCase):
    def test_movie(self):
        movieValidator = MovieValidator()

        m = Movie("123", "A Movie", "Art", "drama")
        self.assertEqual(movieValidator.validate(m), True)

        m = Movie("", "Art", "Art", "comedy")
        with self.assertRaises(ValidatorException):
            movieValidator.validate(m)

        m = Movie("124", "", "Art", "comedy")
        with self.assertRaises(ValidatorException):
            movieValidator.validate(m)

        m = Movie("125", "Art", "", "comedy")
        with self.assertRaises(ValidatorException):
            movieValidator.validate(m)

        m = Movie("126", "Art", "Art", "")
        with self.assertRaises(ValidatorException):
            movieValidator.validate(m)

        m = Movie("123", "", "", "")
        with self.assertRaises(ValidatorException):
            movieValidator.validate(m)

        c = Client("1", "Anna")
        with self.assertRaises(TypeError):
            movieValidator.validate(c)


class TestMovieServiceRepository(unittest.TestCase):
    def test_find_movie_by_id(self):
        movies = []
        m1 = Movie("123", "A Movie", "Art", "romance")
        m2 = Movie("124", "The Second Movie", "New", "horror")
        movies.append(m1)
        movies.append(m2)
        movieRepo = MovieRepository(movies)
        self.assertNotEqual(movieRepo.find_by_id("123"), None)
        self.assertEqual(movieRepo.find_by_id("1"), None)

    def test_add_movie(self):
        movies = []
        movieRepo = MovieRepository(movies)
        movieValidator = MovieValidator()
        undoService = UndoService()
        rentalRepo = RentalRepository([])
        clientRepo = ClientRepository([])
        rentalValidator = RentalValidator()
        rentalService = RentalService(rentalRepo, movieRepo, clientRepo, rentalValidator, undoService)
        movieServ = MovieService(movieRepo, movieValidator, undoService, rentalService)

        m1 = Movie("123", "A Movie", "Art", "romance")
        m2 = Movie("123", "The Second Movie", "New", "horror")

        movieServ.add_movie(m1.movieId, m1.Title, m1.Description, m1.Genre)
        addedMovie = movieServ.get_movies()[0]
        self.assertEqual(addedMovie.movieId, m1.movieId)
        self.assertEqual(addedMovie.Title, m1.Title)
        self.assertEqual(addedMovie.Description, m1.Description)
        self.assertEqual(addedMovie.Genre, m1.Genre)


        with self.assertRaises(MovieException):
            movieServ.add_movie(m2.movieId, m2.Title, m2.Description, m2.Genre)

    def test_remove_movie(self):
        movies = []
        m1 = Movie("123", "A Movie", "Art", "romance")
        m2 = Movie("124", "The Second Movie", "New", "horror")
        movies.append(m1)
        movies.append(m2)
        movieRepo = MovieRepository(movies)

        movieValidator = MovieValidator()
        undoService = UndoService()
        rentalRepo = RentalRepository([])
        clientRepo = ClientRepository([])
        rentalValidator = RentalValidator()
        rentalService = RentalService(rentalRepo, movieRepo, clientRepo, rentalValidator, undoService)
        movieServ = MovieService(movieRepo, movieValidator, undoService, rentalService)

        movieServ.remove_movie("123")
        self.assertNotEqual(movieRepo.get_list_movies()[0].movieId, m1.movieId)


        with self.assertRaises(MovieException):
            movieServ.remove_movie("1")

    def test_update_movie(self):
        movies = []
        m1 = Movie("123", "A Movie", "Art", "romance")
        m2 = Movie("124", "The Second Movie", "New", "horror")
        movies.append(m1)
        movies.append(m2)
        movieRepo = MovieRepository(movies)

        movieValidator = MovieValidator()
        undoService = UndoService()
        rentalRepo = RentalRepository([])
        clientRepo = ClientRepository([])
        rentalValidator = RentalValidator()
        rentalService = RentalService(rentalRepo, movieRepo, clientRepo, rentalValidator, undoService)
        movieServ = MovieService(movieRepo, movieValidator, undoService, rentalService)

        movieServ.update_movie("123", "Another Movie", "", "")
        self.assertEqual(movieServ.get_movies()[0].movieId, "123")
        self.assertEqual(movieServ.get_movies()[0].Title, "Another Movie")
        self.assertEqual(movieServ.get_movies()[0].Description, "Art")
        self.assertEqual(movieServ.get_movies()[0].Genre, "romance")

        movieServ.update_movie("124", "", "New movie", "thriller")
        self.assertEqual(movieServ.get_movies()[1].movieId, "124")
        self.assertEqual(movieServ.get_movies()[1].Title, "The Second Movie")
        self.assertEqual(movieServ.get_movies()[1].Description, "New movie")
        self.assertEqual(movieServ.get_movies()[1].Genre, "thriller")

        with self.assertRaises(MovieException):
            movieServ.update_movie("1", "Movie", "description", "")

    def test_search_movie_by_id(self):
        movies = []
        m1 = Movie("123", "A Movie", "Art", "romance")
        m2 = Movie("124", "The Second Movie", "New", "horror")
        movies.append(m1)
        movies.append(m2)
        movieRepo = MovieRepository(movies)

        movieValidator = MovieValidator()
        undoService = UndoService()
        rentalRepo = RentalRepository([])
        clientRepo = ClientRepository([])
        rentalValidator = RentalValidator()
        rentalService = RentalService(rentalRepo, movieRepo, clientRepo, rentalValidator, undoService)
        movieServ = MovieService(movieRepo, movieValidator, undoService, rentalService)

        self.assertEqual(movieServ.search_movie_by_id("1"), movies)
        self.assertEqual(movieServ.search_movie_by_id("m"), [])

    def test_search_movie_by_title(self):
        movies = []
        m1 = Movie("123", "A Movie", "Art", "romance")
        m2 = Movie("124", "The Second Movie", "New", "horror")
        movies.append(m1)
        movies.append(m2)
        movieRepo = MovieRepository(movies)

        movieValidator = MovieValidator()
        undoService = UndoService()
        rentalRepo = RentalRepository([])
        clientRepo = ClientRepository([])
        rentalValidator = RentalValidator()
        rentalService = RentalService(rentalRepo, movieRepo, clientRepo, rentalValidator, undoService)
        movieServ = MovieService(movieRepo, movieValidator, undoService, rentalService)

        self.assertEqual(movieServ.search_movie_by_title("ovie"), movies)

        movies.clear()
        movies.append(m2)
        self.assertEqual(movieServ.search_movie_by_title("d"), movies)

    def test_search_movie_by_description(self):
        movies = []
        m1 = Movie("123", "A Movie", "Art", "romance")
        m2 = Movie("124", "The Second Movie", "New", "horror")
        movies.append(m1)
        movies.append(m2)
        movieRepo = MovieRepository(movies)

        movieValidator = MovieValidator()
        undoService = UndoService()
        rentalRepo = RentalRepository([])
        clientRepo = ClientRepository([])
        rentalValidator = RentalValidator()
        rentalService = RentalService(rentalRepo, movieRepo, clientRepo, rentalValidator, undoService)
        movieServ = MovieService(movieRepo, movieValidator, undoService, rentalService)

        self.assertEqual(movieServ.search_movie_by_description("Something"), [])
        movies.clear()
        movies.append(m1)
        self.assertEqual(movieServ.search_movie_by_description("art"), movies)

    def test_search_movie_by_genre(self):
        movies = []
        m1 = Movie("123", "A Movie", "Art", "romance")
        m2 = Movie("124", "The Second Movie", "New", "horror")
        movies.append(m1)
        movies.append(m2)
        movieRepo = MovieRepository(movies)

        movieValidator = MovieValidator()
        undoService = UndoService()
        rentalRepo = RentalRepository([])
        clientRepo = ClientRepository([])
        rentalValidator = RentalValidator()
        rentalService = RentalService(rentalRepo, movieRepo, clientRepo, rentalValidator, undoService)
        movieServ = MovieService(movieRepo, movieValidator, undoService, rentalService)

        self.assertEqual(movieServ.search_movie_by_genre("comedy"),[])
        movies.clear()
        movies.append(m1)
        self.assertEqual(movieServ.search_movie_by_genre("mance"),movies)

class TestClientDomain(unittest.TestCase):
    def test_create_client(self):
        c = Client("123", "Jimmy Park")
        self.assertEqual(c.clientId, "123")
        self.assertEqual(c.Name, "Jimmy Park")

    def test_str_client(self):
        c = Client("123", "Jimmy Park")
        self.assertEqual(str(c), "id: 123, name: Jimmy Park")


class TestClientValidator(unittest.TestCase):
    def test_client(self):
        clientValidator = ClientValidator()

        c = Client("123", "Jimmy Park")
        self.assertEqual(clientValidator.validate(c), True)

        c = Client("", "Anna Park")
        with self.assertRaises(ValidatorException):
            clientValidator.validate(c)

        c = Client("124", "")
        with self.assertRaises(ValidatorException):
            clientValidator.validate(c)


        c = Client("", "")
        try:
            clientValidator.validate(c)
        except ValidatorException as v:
            self.assertEqual(str(v), "Client id can not be empty" + '\n' + "Client must have a name" + '\n')

        m = Movie("1", "Far", "New", "romance")
        with self.assertRaises(TypeError):
            clientValidator.validate(m)


class TestClientServiceRepository(unittest.TestCase):
    def test_find_client_by_id(self):
        clients = []
        c1 = Client("123", "Jimmy Park")
        c2 = Client("124", "Anna Park")
        clients.append(c1)
        clients.append(c2)
        clientRepo = ClientRepository(clients)
        self.assertNotEqual(clientRepo.find_by_id("123"), None)
        self.assertEqual(clientRepo.find_by_id("1"), None)

    def test_add_client(self):
        clients = []
        clientRepo = ClientRepository(clients)
        clientValidator = ClientValidator()
        rentalRepo = RentalRepository([])
        movieRepo = MovieRepository([])
        rentalValidator = RentalValidator()
        undoService = UndoService()
        rentalService = RentalService(rentalRepo, movieRepo, clientRepo, rentalValidator, undoService)
        clientServ = ClientService(clientRepo, clientValidator, rentalService, undoService)

        c1 = Client("123", "Jimmy Park")
        c2 = Client("123", "Anna Park")

        clientServ.add_client(c1.clientId, c1.Name)
        addedClient = clientServ.get_clients()[0]
        self.assertEqual(addedClient.clientId, c1.clientId)
        self.assertEqual(addedClient.Name, c1.Name)


        with self.assertRaises(ClientException):
            clientServ.add_client(c2.clientId, c2.Name)

    def test_delete_client(self):
        clients = []
        c1 = Client("123", "Jimmy Park")
        c2 = Client("124", "Anna Park")
        clients.append(c1)
        clients.append(c2)
        clientRepo = ClientRepository(clients)

        clientValidator = ClientValidator()
        rentalRepo = RentalRepository([])
        movieRepo = MovieRepository([])
        rentalValidator = RentalValidator()
        undoService = UndoService()
        rentalService = RentalService(rentalRepo, movieRepo, clientRepo, rentalValidator, undoService)
        clientServ = ClientService(clientRepo, clientValidator, rentalService, undoService)

        clientServ.remove_client("123")
        self.assertNotEqual(clientRepo.get_list_clients()[0].clientId, c1.clientId)


        with self.assertRaises(ClientException):
            clientServ.remove_client("1")

    def test_update_client(self):
        clients = []
        c1 = Client("123", "Jimmy Park")
        c2 = Client("124", "Anna Park")
        clients.append(c1)
        clients.append(c2)
        clientRepo = ClientRepository(clients)

        clientValidator = ClientValidator()
        rentalRepo = RentalRepository([])
        movieRepo = MovieRepository([])
        rentalValidator = RentalValidator()
        undoService = UndoService()
        rentalService = RentalService(rentalRepo, movieRepo, clientRepo, rentalValidator, undoService)
        clientServ = ClientService(clientRepo, clientValidator, rentalService, undoService)

        clientServ.update_client("123", "Jimmy Phil")
        self.assertEqual(clientServ.get_clients()[0].clientId, "123")
        self.assertEqual(clientServ.get_clients()[0].Name, "Jimmy Phil")

        clientServ.update_client("124", "Danna Park")
        self.assertEqual(clientServ.get_clients()[1].clientId, "124")
        self.assertEqual(clientServ.get_clients()[1].Name, "Danna Park")

        with self.assertRaises(ClientException):
            clientServ.update_client("1", "Mary")

    def test_search_client_by_id(self):
        clients = []
        c1 = Client("123", "Jimmy Park")
        c2 = Client("124", "Anna Park")
        clients.append(c1)
        clients.append(c2)
        clientRepo = ClientRepository(clients)

        clientValidator = ClientValidator()
        rentalRepo = RentalRepository([])
        movieRepo = MovieRepository([])
        rentalValidator = RentalValidator()
        undoService = UndoService()
        rentalService = RentalService(rentalRepo, movieRepo, clientRepo, rentalValidator, undoService)
        clientServ = ClientService(clientRepo, clientValidator, rentalService, undoService)

        self.assertEqual(clientServ.search_client_by_id("1"), clients)
        self.assertEqual(clientServ.search_client_by_id("5"), [])

    def test_search_client_by_name(self):
        clients = []
        c1 = Client("123", "Jimmy Park")
        c2 = Client("124", "Anna Park")
        clients.append(c1)
        clients.append(c2)
        clientRepo = ClientRepository(clients)

        clientValidator = ClientValidator()
        rentalRepo = RentalRepository([])
        movieRepo = MovieRepository([])
        rentalValidator = RentalValidator()
        undoService = UndoService()
        rentalService = RentalService(rentalRepo, movieRepo, clientRepo, rentalValidator, undoService)
        clientServ = ClientService(clientRepo, clientValidator, rentalService, undoService)

        self.assertEqual(clientServ.search_client_by_name("ark"), clients)
        clients.clear()
        clients.append(c1)
        self.assertEqual(clientServ.search_client_by_name("j"), clients)

class TestRentalDomain(unittest.TestCase):
    def test_create_rental(self):
        r = Rental("123", "123", "123", date(2019, 10, 12), date(2019, 11, 15), date(2019, 10, 13))
        self.assertEqual(r.rentalId, "123")
        self.assertEqual(r.movieId, "123")
        self.assertEqual(r.clientId, "123")
        self.assertEqual(r.rentedDate, date(2019, 10, 12))
        self.assertEqual(r.dueDate, date(2019, 11, 15))
        self.assertEqual(r.returnedDate, date(2019, 10, 13))

    def test_str_rental(self):
        r = Rental("123", "123", "123", date(2019, 10, 12), date(2019, 11, 15), date(2019, 10, 13))
        self.assertEqual(str(r), "id: 123, movieId: 123, clientId: 123, rentedDate: 2019-10-12, dueDate: 2019-11-15, returnedDate: 2019-10-13")
        r2 = Rental("124", "123", "123", date(2019, 10, 12), date(2019, 11, 15), None)
        self.assertEqual(str(r2), "id: 124, movieId: 123, clientId: 123, rentedDate: 2019-10-12, dueDate: 2019-11-15, returnedDate: None")

    def test_len_rental(self):
        r = Rental("123", "123", "123", date(2019, 10, 12), date(2019, 11, 15), date(2019, 10, 13))
        self.assertEqual(len(r), 2)
        r2 = Rental("124", "123", "123", date(2019, 11, 20), date(2019, 11, 21), None)
        length = int((date.today() - r2.rentedDate).days) + 1
        self.assertEqual(len(r2), length)

    def test_delay_days(self):
        r = Rental("124", "123", "123", date(2019, 11, 20), date(2019, 11, 21), None)
        delay = int((date.today() - r.dueDate).days)
        self.assertEqual(r.delay_days(), delay)

        r2 = Rental("125", "123", "123", date(2019, 11, 20), date.today() + timedelta(days=14), None)
        self.assertEqual(r2.delay_days(), 0)

        r3 = r = Rental("126", "123", "123", date(2019, 11, 20), date(2019, 11, 24), date(2019, 11, 24))
        self.assertEqual(r3.delay_days(), 0)

    def test_is_late(self):
        r = Rental("124", "123", "123", date(2019, 11, 20), date(2019, 11, 21), None)
        self.assertEqual(r.is_late(), True)

        r2 = Rental("125", "123", "123", date(2019, 11, 20), date.today() + timedelta(days=14), None)
        self.assertEqual(r2.is_late(), False)

        r3 = r = Rental("126", "123", "123", date(2019, 11, 20), date(2019, 11, 24), date(2019, 11, 24))
        self.assertEqual(r3.is_late(), False)


class TestRentalServiceRepo(unittest.TestCase):
    def test_find_by_id(self):
        rentals = []
        r = Rental("123", "123", "123", date(2019, 10, 12), date(2019, 11, 15), date(2019, 10, 13))
        rentals.append(r)
        rentalRepo = RentalRepository(rentals)
        self.assertNotEqual(rentalRepo.find_by_id("123"), None)
        self.assertEqual(rentalRepo.find_by_id("1"), None)

    def test_generate_rental(self):
        clients = []
        movies = []
        rentals = []
        c1 = Client("123", "Jimmy Park")
        c2 = Client("124", "Anna Park")
        m1 = Movie("123", "A Movie", "Art", "drama")
        m2 = Movie("124", "The Second Movie", "New", "comedy")
        m3 = Movie("125", "The Third Movie", "New", "thriller")
        r = Rental("1", "124", "124", date(2019, 11, 28), date(2019, 11, 29), None)
        clients.append(c1)
        clients.append(c2)
        movies.append(m1)
        movies.append(m2)
        movies.append(m3)
        rentals.append(r)

        clientRepo = ClientRepository(clients)
        movieRepo = MovieRepository(movies)
        rentalRepo = RentalRepository(rentals)

        with self.assertRaises(RentalException):
            rentalRepo.store_rental(r)

        rentalValidator = RentalValidator()
        undoService = UndoService()
        rentalServ = RentalService(rentalRepo, movieRepo, clientRepo, rentalValidator, undoService)

        rentalServ.generate_rental("123", "123")
        self.assertEqual(rentalServ.get_rentals()[1].movieId, m1.movieId)
        self.assertEqual(rentalServ.get_rentals()[1].clientId, c1.clientId)

        with self.assertRaises(RentalException):
            rentalServ.generate_rental("123", "123")

        with self.assertRaises(RentalException):
            rentalServ.generate_rental("124", "125")

    def test_delete_rental(self):
        r = Rental("1", "124", "124", date(2019, 11, 28), date(2019, 11, 29), None)
        rentals = []
        rentals.append(r)
        clientRepo = ClientRepository([])
        movieRepo = MovieRepository([])
        rentalRepo = RentalRepository(rentals)
        rentalValidator = RentalValidator()
        undoService = UndoService()
        rentalServ = RentalService(rentalRepo, movieRepo, clientRepo, rentalValidator, undoService)

        rentalServ.delete_rental("1")
        self.assertEqual(rentalServ.get_rentals(), [])

        with self.assertRaises(RentalException):
            rentalServ.delete_rental("1")

    def test_return_movie(self):
        clients = []
        movies = []
        rentals = []
        c1 = Client("123", "Jimmy Park")
        m1 = Movie("123", "A Movie", "Art", "drama")
        r = Rental("1", "123", "123", date(2019, 11, 28), date(2019, 12, 12), None)
        clients.append(c1)
        movies.append(m1)
        rentals.append(r)

        clientRepo = ClientRepository(clients)
        movieRepo = MovieRepository(movies)
        rentalRepo = RentalRepository(rentals)
        rentalValidator = RentalValidator()
        undoService = UndoService()
        rentalServ = RentalService(rentalRepo, movieRepo, clientRepo, rentalValidator, undoService)

        rentalServ.return_movie("123", "123")
        self.assertEqual(rentalServ.get_rentals()[0].returnedDate, date.today())

        with self.assertRaises(RentalException):
            rentalServ.return_movie("124", "124")


class TestRentalValidator(unittest.TestCase):
    def test_rental(self):
        rentalValidator = RentalValidator()

        r = Rental("123", "123", "123", date(2019, 10, 12), date(2019, 11, 15), date(2019, 10, 13))

        self.assertEqual(rentalValidator.validate(r), True)

        r = Rental("", "123", "123", date(2019, 10, 12), date(2019, 11, 15), date(2019, 10, 13))
        with self.assertRaises(ValidatorException):
            rentalValidator.validate(r)

        r = Rental("124", "", "123", date(2019, 10, 12), date(2019, 11, 15), date(2019, 10, 13))
        with self.assertRaises(ValidatorException):
            rentalValidator.validate(r)

        r = Rental("125", "123", "", date(2019, 10, 12), date(2019, 11, 15), date(2019, 10, 13))
        with self.assertRaises(ValidatorException):
            rentalValidator.validate(r)

        r = Rental("126", "123", "123", date(2019, 10, 12), date(2019, 9, 15), date(2019, 10, 13))
        with self.assertRaises(ValidatorException):
            rentalValidator.validate(r)

        r = Rental("127", "123", "123", date(2019, 10, 12), date(2019, 11, 15), date(2019, 9, 13))
        with self.assertRaises(ValidatorException):
            rentalValidator.validate(r)

        c = Client("1", "Anna")
        with self.assertRaises(TypeError):
            rentalValidator.validate(c)


class TestUndoService(unittest.TestCase):
    def test_undo_delete_movie(self):
        clients = []
        movies = []
        rentals = []
        c1 = Client("123", "Jimmy Park")
        m1 = Movie("123", "A Movie", "Art", "drama")
        r = Rental("1", "123", "123", date(2019, 11, 28), date(2019, 12, 12), None)
        clients.append(c1)
        movies.append(m1)
        rentals.append(r)

        clientRepo = ClientRepository(clients)
        movieRepo = MovieRepository(movies)
        rentalRepo = RentalRepository(rentals)
        rentalValidator = RentalValidator()
        movieValidator = MovieValidator()
        undoService = UndoService()
        rentalServ = RentalService(rentalRepo, movieRepo, clientRepo, rentalValidator, undoService)
        movieServ = MovieService(movieRepo, movieValidator, undoService, rentalServ)

        movieServ.remove_movie("123")
        undoService.undo()
        self.assertEqual(movieServ.get_movies()[0].movieId, "123")
        self.assertEqual(rentalServ.get_rentals()[0].rentalId, "1")

        with self.assertRaises(ValueError):
            undoService.undo()

        undoService.redo()
        self.assertEqual(movieServ.get_movies(), [])
        self.assertEqual(rentalServ.get_rentals(), [])

        with self.assertRaises(ValueError):
            undoService.redo()

    def test_undo_delete_client(self):
        clients = []
        movies = []
        rentals = []
        c1 = Client("123", "Jimmy Park")
        m1 = Movie("123", "A Movie", "Art", "drama")
        r = Rental("1", "123", "123", date(2019, 11, 28), date(2019, 12, 12), None)
        clients.append(c1)
        movies.append(m1)
        rentals.append(r)

        clientRepo = ClientRepository(clients)
        movieRepo = MovieRepository(movies)
        rentalRepo = RentalRepository(rentals)
        rentalValidator = RentalValidator()
        clientValidator = ClientValidator()
        undoService = UndoService()
        rentalServ = RentalService(rentalRepo, movieRepo, clientRepo, rentalValidator, undoService)
        clientServ = ClientService(clientRepo, clientValidator, rentalServ, undoService)

        clientServ.remove_client("123")
        undoService.undo()
        self.assertEqual(clientServ.get_clients()[0].clientId, "123")
        self.assertEqual(rentalServ.get_rentals()[0].rentalId, "1")

        undoService.redo()
        self.assertEqual(clientServ.get_clients(), [])
        self.assertEqual(rentalServ.get_rentals(), [])


class TestMostRentedMovies(unittest.TestCase):
    def test(self):
        clients = []
        movies = []
        rentals = []
        c1 = Client("123", "Jimmy Park")
        c2 = Client("124", "Anna Park")
        m1 = Movie("123", "A Movie", "Art", "drama")
        m2 = Movie("124", "The Second Movie", "New", "comedy")
        r = Rental("1", "124", "124", date(2019, 11, 28), date(2019, 11, 29), date(2019, 11, 28))
        clients.append(c1)
        clients.append(c2)
        movies.append(m1)
        movies.append(m2)
        rentals.append(r)

        clientRepo = ClientRepository(clients)
        movieRepo = MovieRepository(movies)
        rentalRepo = RentalRepository(rentals)
        rentalValidator = RentalValidator()
        undoService = UndoService()
        rentalServ = RentalService(rentalRepo, movieRepo, clientRepo, rentalValidator, undoService)

        self.assertEqual(rentalServ.most_rented_movies()[0].Days, 1)
        self.assertEqual(rentalServ.most_rented_movies()[0].Movie.movieId, m2.movieId)
        self.assertEqual(rentalServ.most_rented_movies()[1].Days, 0)
        self.assertEqual(rentalServ.most_rented_movies()[1].Movie.movieId, m1.movieId)


class TestMostActiveClients(unittest.TestCase):
    def test(self):
        clients = []
        movies = []
        rentals = []
        c1 = Client("123", "Jimmy Park")
        c2 = Client("124", "Anna Park")
        m1 = Movie("123", "A Movie", "Art", "drama")
        m2 = Movie("124", "The Second Movie", "New", "comedy")
        r = Rental("1", "124", "124", date(2019, 11, 28), date(2019, 11, 29), date(2019, 11, 28))
        clients.append(c1)
        clients.append(c2)
        movies.append(m1)
        movies.append(m2)
        rentals.append(r)

        clientRepo = ClientRepository(clients)
        movieRepo = MovieRepository(movies)
        rentalRepo = RentalRepository(rentals)
        rentalValidator = RentalValidator()
        undoService = UndoService()
        rentalServ = RentalService(rentalRepo, movieRepo, clientRepo, rentalValidator, undoService)

        self.assertEqual(rentalServ.most_active_clients()[0].Days, 1)
        self.assertEqual(rentalServ.most_active_clients()[0].Client.clientId, c2.clientId)
        self.assertEqual(str(rentalServ.most_active_clients()[1]), "0 days - id: 123, name: Jimmy Park")
        self.assertEqual(rentalServ.most_active_clients()[1].Days, 0)
        self.assertEqual(rentalServ.most_active_clients()[1].Client.clientId, c1.clientId)


class TestLateRentals(unittest.TestCase):
    def test(self):
        clients = []
        movies = []
        rentals = []
        c1 = Client("123", "Jimmy Park")
        c2 = Client("124", "Anna Park")
        m1 = Movie("123", "A Movie", "Art", "drama")
        m2 = Movie("124", "The Second Movie", "New", "comedy")
        r = Rental("1", "123", "123", date(2019, 11, 28), date(2019, 11, 28), None)
        clients.append(c1)
        clients.append(c2)
        movies.append(m1)
        movies.append(m2)
        rentals.append(r)

        clientRepo = ClientRepository(clients)
        movieRepo = MovieRepository(movies)
        rentalRepo = RentalRepository(rentals)
        rentalValidator = RentalValidator()
        undoService = UndoService()
        rentalServ = RentalService(rentalRepo, movieRepo, clientRepo, rentalValidator, undoService)


        latedays = int((date.today() - r.dueDate).days)
        self.assertEqual(str(rentalServ.late_rentals()[0]), str(latedays) + " days - id: 123, title: A Movie, description: Art, genre: drama")
