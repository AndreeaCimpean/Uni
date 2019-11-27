import unittest
from repositories import *
from domain import *
from services import *
from datetime import date, timedelta
import coverage


class TestMovieDomain(unittest.TestCase):

    def test_create_movie(self):
        m = Movie("123", "A Movie", "Art", "drama")
        self.assertEqual(m.movieId, "123")
        self.assertEqual(m.Title, "A Movie")
        self.assertEqual(m.Description, "Art")
        self.assertEqual(m.Genre, "drama")
        with self.assertRaises(MovieException):
            m2 = Movie("", "Art", "Art", "comedy")
        with self.assertRaises(MovieException):
            m2 = Movie("124", "", "Art", "comedy")
        with self.assertRaises(MovieException):
            m2 = Movie("125", "Art", "", "comedy")
        with self.assertRaises(MovieException):
            m2 = Movie("126", "Art", "Art", "")

    def test_str_movie(self):
        m = Movie("123", "A Movie", "New", "drama")
        self.assertEqual(str(m), "id: 123, title: A Movie, description: New, genre: drama")


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
        movieServ = MovieService(movieRepo)

        m1 = Movie("123", "A Movie", "Art", "romance")
        m2 = Movie("123", "The Second Movie", "New", "horror")

        movieServ.add_movie(m1)
        self.assertEqual(movieServ.get_movies()[0], m1)
        with self.assertRaises(MovieException):
            movieServ.add_movie(m2)

    def test_remove_movie(self):
        movies = []
        m1 = Movie("123", "A Movie", "Art", "romance")
        m2 = Movie("124", "The Second Movie", "New", "horror")
        movies.append(m1)
        movies.append(m2)
        movieRepo = MovieRepository(movies)
        movieRepo.delete_movie("123")
        self.assertNotEqual(movieRepo.get_list_movies()[0], m1)
        with self.assertRaises(MovieException):
            movieRepo.delete_movie("1")

    def test_update_movie(self):
        movies = []
        m1 = Movie("123", "A Movie", "Art", "romance")
        m2 = Movie("124", "The Second Movie", "New", "horror")
        movies.append(m1)
        movies.append(m2)
        movieRepo = MovieRepository(movies)
        movieRepo.update_movie("123", "Another Movie", "", "")
        self.assertEqual(movieRepo.get_list_movies()[0].movieId, "123")
        self.assertEqual(movieRepo.get_list_movies()[0].Title, "Another Movie")
        self.assertEqual(movieRepo.get_list_movies()[0].Description, "Art")
        self.assertEqual(movieRepo.get_list_movies()[0].Genre, "romance")

        movieRepo.update_movie("124", "", "New movie", "thriller")
        self.assertEqual(movieRepo.get_list_movies()[1].movieId, "124")
        self.assertEqual(movieRepo.get_list_movies()[1].Title, "The Second Movie")
        self.assertEqual(movieRepo.get_list_movies()[1].Description, "New movie")
        self.assertEqual(movieRepo.get_list_movies()[1].Genre, "thriller")

        with self.assertRaises(MovieException):
            movieRepo.update_movie("1", "Movie", "description", "")


class TestClient(unittest.TestCase):
    def test_create_client(self):
        c = Client("123", "Jimmy Park")
        self.assertEqual(c.clientId, "123")
        self.assertEqual(c.Name, "Jimmy Park")
        with self.assertRaises(ClientException):
            c2 = Client("", "Anna Park")
        with self.assertRaises(ClientException):
            c2 = Client("124", "")

    def test_str_client(self):
        c = Client("123", "Jimmy Park")
        self.assertEqual(str(c), "id: 123, name: Jimmy Park")

    def test_find_client_by_id(self):
        clients = []
        c1 = Client("123", "Jimmy Park")
        c2 = Client("124", "Anna Park")
        clients.append(c1)
        clients.append(c2)
        clientRepo = ClientRepository(clients)
        self.assertNotEqual(clientRepo.find_by_id("123"), None)
        self.assertEqual(clientRepo.find_by_id("1"), None)

    def test_store_client(self):
        clients = []
        clientRepo = ClientRepository(clients)

        c1 = Client("123", "Jimmy Park")
        c2 = Client("123", "Anna Park")

        clientRepo.store_client(c1)
        self.assertEqual(clientRepo.get_list_clients()[0], c1)
        with self.assertRaises(ClientException):
            clientRepo.store_client(c2)

    def test_delete_client(self):
        clients = []
        c1 = Client("123", "Jimmy Park")
        c2 = Client("124", "Anna Park")
        clients.append(c1)
        clients.append(c2)
        clientRepo = ClientRepository(clients)
        clientRepo.delete_client("123")
        self.assertNotEqual(clientRepo.get_list_clients()[0], c1)
        with self.assertRaises(ClientException):
            clientRepo.delete_client("1")

    def test_update_client(self):
        clients = []
        c1 = Client("123", "Jimmy Park")
        c2 = Client("124", "Anna Park")
        clients.append(c1)
        clients.append(c2)
        clientRepo = ClientRepository(clients)
        clientRepo.update_client("123", "Jimmy Phil")
        self.assertEqual(clientRepo.get_list_clients()[0].clientId, "123")
        self.assertEqual(clientRepo.get_list_clients()[0].Name, "Jimmy Phil")

        clientRepo.update_client("124", "Danna Park")
        self.assertEqual(clientRepo.get_list_clients()[1].clientId, "124")
        self.assertEqual(clientRepo.get_list_clients()[1].Name, "Danna Park")

        with self.assertRaises(ClientException):
            clientRepo.update_client("1", "Mary")


class TestRental(unittest.TestCase):
    def test_create_rental(self):
        r = Rental("123", "123", "123", date(2019, 10, 12), date(2019, 11, 15), date(2019, 10, 13))
        self.assertEqual(r.rentalId, "123")
        self.assertEqual(r.movieId, "123")
        self.assertEqual(r.clientId, "123")
        self.assertEqual(r.rentedDate, date(2019, 10, 12))
        self.assertEqual(r.dueDate, date(2019, 11, 15))
        self.assertEqual(r.returnedDate, date(2019, 10, 13))

        with self.assertRaises(RentalException):
            r2 = Rental("", "123", "123", date(2019, 10, 12), date(2019, 11, 15), date(2019, 10, 13))
        with self.assertRaises(RentalException):
            r2 = Rental("124", "", "123", date(2019, 10, 12), date(2019, 11, 15), date(2019, 10, 13))
        with self.assertRaises(RentalException):
            r2 = Rental("125", "123", "", date(2019, 10, 12), date(2019, 11, 15), date(2019, 10, 13))
        with self.assertRaises(RentalException):
            r2 = Rental("126", "123", "123", date(2019, 10, 12), date(2019, 9, 15), date(2019, 10, 13))
        with self.assertRaises(RentalException):
            r2 = Rental("127", "123", "123", date(2019, 10, 12), date(2019, 11, 15), date(2019, 9, 13))

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