class ClientService:

    def __init__(self, clientRepo):
        self._clientRepository = clientRepo


class CarService:

    def __init__(self, carRepo):
        self._carService = carRepo


class CarRentalDays:
    def __init__(self, car, days):
        self._car = car
        self._days = days

    def __str__(self):
        return str(self._days) + '-' + str(self._car)


class RentalService:

    def getAllRentals(self):
        '''
        Return all rentals
        '''
        pass

    def deleteAllRentals(self, clientId):
        '''
        Delete all rentals associated with given client
        '''
        i = 0
        while i < len(self._rentalRepository):
            rental = self._rentalRepository[i]
            if clientId == rental._client.Id:
                self._rentalRepository.delete(clientId)
            else:
                i += 1

    def _mostRentedCars(self):
        d = dict()
        for i in range(len(self._rentalRepository)):
            rent = self._rentalRepository[i]
            if rent.Car not in d.keys():
                d[rent.Car] = len(rent)
            else:
                d[rent.Car] += len(rent)

        for i in range(len(self._carRepository)):
            car = self._carRepository[i]

    def __init__(self, rentalRepo, carRepo, clientRepo):
        self._rentalRepository = rentalRepo
        self._carRepository = carRepo
        self._clientRepository = clientRepo