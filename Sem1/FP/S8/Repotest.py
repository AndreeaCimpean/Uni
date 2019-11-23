from repositories import *
from Client import Client
import unittest


class RepoTest(unittest.TestCase):
    def testRepo(self):
        r = Repository()
        #check length of repo using len()
        self.assertEqual(0, len(r))
        r.store((c := Client(1, "Ana", 19)))
        self.assertEqual(1, len(r))
        #use [] operator to access repo stuff
        self.assertEqual(c, r[0]) # __getitem__
        r.store((c2 := Client(2, "Marius", 20)))
        self.assertEqual(2, len(r))
        self.assertEqual(c, r[0])
        self.assertEqual(c2, r[1])
        #client with id 2 is at index 1
        self.assertEqual(1, r.find(2))
        #trying to add Marius again shoud raise an exception
        with self.assertRaises(RepositoryException):
            r.store(c2)
        #delete clients from repo
        r.delete(1)
        r.delete(2)
        self.assertEqual(0, len(r))