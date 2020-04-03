from domain import *

class DriverService:
    def __init__(self, repo):
        self._repository = repo


class OrderService:
    def __init__(self, repo):
        self._repository = repo

    def get_orders(self):
        return self._repository.get_orders()

    def add_order(self, driverId, distance):
        '''
        :param driverId: the given driverId
        :param distance: the given distance
        Call repository function if valid order distance
        If not the ui catches the error
        '''
        o = Order(driverId, distance)
        self._repository.store_order(o)

    def income_driver(self, driverId):
        driver = self._repository.get_driver(driverId)
        income = 0
        for i in self.get_orders():
            if i.driverId == driverId:
                income += i.Distance
        income = float(income) * 2.5
        return Income(income, driver)


class Income:
    def __init__(self, inc, driver):
        self._income = inc
        self._driver = driver

    def __str__(self):
        return str(self._income) + " ron " + " - " + str(self._driver)