import unittest
from repository import *
from service import *


class TestFirst(unittest.TestCase):
    def test_find_driver_by_id(self):
        driverRepo = DriverRepository("drivers.txt")
        self.assertNotEqual(driverRepo.find_by_id(1),None)
        self.assertEqual(driverRepo.find_by_id(9999999),None)

    def test_store_order(self):
        driverRepo = DriverRepository("drivers.txt")
        orderRepo = OrderRepository("orders.txt", driverRepo)
        o = Order(1,9)
        orderRepo.store_order(o)
        self.assertEqual(orderRepo.get_orders()[len(orderRepo.get_orders())-1], o)
        o2 = Order(50000,9)
        with self.assertRaises(ValueError):
            orderRepo.store_order(o2)


    def test_add_order(self):
        driverRepo = DriverRepository("drivers.txt")
        orderRepo = OrderRepository("orders.txt", driverRepo)
        orderServ = OrderService(orderRepo)
        orderServ.add_order(1,9)
        self.assertEqual(orderRepo.get_orders()[len(orderRepo.get_orders())-1].driverId, 1)
        self.assertEqual(orderRepo.get_orders()[len(orderRepo.get_orders())-1].Distance, 9)
        with self.assertRaises(ValueError):
            orderServ.add_order(1,-1)