import unittest
from domain import Client

class TestClient(unittest.TestCase):

    def test_client(self):
        c = Client(1,"Pop Andreea",19)
        self.assertEqual(c.clientId,1)
        self.assertEqual(c.Name,"Pop Andreea")
        self.assertEqual(c.Age,19)


        data = [1,2,3]
        # Assign len(data) to n and retutn n
        # if (n := len(data)) == 3:
        # print(n)


    def test_client_again(self):
        c = Client(1,"Pop Andreea",19)

        with self.assertRaises(ValueError):
            c.Age = 16

        '''try:
            c.Age = 17
            assert False        # Should have raised an exception
        except ValueError:
            assert True         # We are ei okay
        except Exception:
            assert False        # A different exception was raised
        '''