import unittest
from repositories import ClientRepository, MovieRepository
from domain import *
import coverage


class TestMovie(unittest.TestCase):

    def test_find_movie_by_id(self):
        movies = []
        m1 = Movie("123", "A Movie", "Art", "romance")
        m2 = Movie("124", "The Second Movie", "New", "horror")
        movies.append(m1)
        movies.append(m2)
        movieRepo = MovieRepository(movies)
        self.assertNotEqual(movieRepo.find_by_id("123"), None)
        self.assertEqual(movieRepo.find_by_id("1"), None)

    def test_store_movie(self):
        movies = []
        movieRepo = MovieRepository(movies)

        m1 = Movie("123", "A Movie", "Art", "romance")
        m2 = Movie("123", "The Second Movie", "New", "horror")

        movieRepo.store_movie(m1)
        self.assertEqual(movieRepo.get_list_movies()[0], m1)
        with self.assertRaises(MovieException):
            movieRepo.store_movie(m2)

    def test_delete_movie(self):
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

