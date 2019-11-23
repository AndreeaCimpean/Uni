from repositories import *
from services import *
from Client import *
from Rental import *
from Client import *
from datetime import date

class UI:
    def __init__(self, carService, clientService, rentalService):
        self._carService = carService
        self._clientService = clientService
        self._rentalService = rentalService

    def deleteClient(self):
        '''
        When we delete a client, we delte their rentals
        '''
        try:
            clientId = input("Client id = ")
            self._rentalService.deleteAllRentals(clientId)
        except RepositoryException as re:
            print(re)

    def _mostRentedCars(self):
        result = self._rentalService.mostRentedCars()
        for r in result:
            print(r)
        # car info -> number of days

    def _rentCar(self):
        try:
            # 1. Determine the client(get client id)
            clientId = input("client id = ")
            client = self._clientService.getClient(clientId)

            # 2. Determine the car(get car id)
            carId = input("car id = ")
            car = self._carService.getCar(carId)

            # 3. Validation
            # 4. Create rental

            rent = Rental(100, date(), date(), client, car)
        except RepositoryException as re:
            print(re)

    def start(self):
        '''
        Start program, display menu, read user input, call other methods...
        '''
        pass