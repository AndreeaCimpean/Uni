from service import *
from repository import *
import unittest


class TestThird(unittest.TestCase):

    def test_get_bus_by_id(self):
        busRepo = BusesRepository("buses.txt")
        b1 = busRepo.get_buses()[0]
        self.assertEqual(busRepo.get_bus_by_id(b1.busId),b1)
        self.assertEqual(busRepo.get_bus_by_id(10000),None)

    def test_get_route_by_id(self):
        routeRepo = RoutesRepository("routes.txt")
        r = routeRepo.get_routes()[0]
        self.assertEqual(routeRepo.get_route_by_id(r.routeId),r)
        self.assertEqual(routeRepo.get_route_by_id(10000), None)

    def test_length_travelled(self):
        busRepo = BusesRepository("buses.txt")
        routeRepo = RoutesRepository("routes.txt")
        busServ = BusService(busRepo, routeRepo)
        self.assertEqual(busServ.length_travelled(3)._km,91)