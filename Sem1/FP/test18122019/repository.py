from domain import *

class DriverRepository:
    def __init__(self, fileName):
        self._fileName = fileName
        self._drivers = self._load_file()

    def _load_file(self):
        data = []
        f = open(self._fileName, "r")
        line = f.readline().strip()
        while len(line) > 0:
            params = line.split(",")
            d = Driver(int(params[0]), params[1])
            data.append(d)
            line = f.readline().strip()
        f.close()
        return data

    def find_by_id(self, driverId):
        '''
        :param driverId: the given driverId
        :return the driver if found
        None otherwise
        '''
        for i in self._drivers:
            if i.driverId == driverId:
                return i
        return None


class OrderRepository:
    def __init__(self, fileName, driverRepo):
        self._driverRepository = driverRepo
        self._fileName = fileName
        self._orders = self._load_file()

    def _load_file(self):
        data = []
        f = open(self._fileName, "r")
        line = f.readline().strip()
        while len(line) > 0:
            params = line.split(",")
            o = Order(int(params[0]), int(params[1]))
            data.append(o)
            line = f.readline().strip()
        f.close()
        return data

    def get_orders(self):
        return self._orders

    def store_order(self, order):
        '''
        :param order: the given order
        Add the order if it has an existent driverId
        Raise an error otherwise
        '''
        if self._driverRepository.find_by_id(order.driverId) == None:
            raise ValueError("Not a valid driverId")
        self._orders.append(order)

    def get_driver(self, driverId):
        return self._driverRepository.find_by_id(driverId)