from repository.CarTextRepository import *
from domain.Car import *

carRepo = CarTextRepository('cars.txt')  # at this point is the same as Repository
'''carRepo.store(Car("100", 'CJ 08 MTR', 'Dacia', 'Duster'))
print(carRepo)'''

clientRepo = ClientTextRepository('clients.txt')
rentalRepo = RentalTextRepository('rentals.txt', carRepo, clientRepo)

'''
When loading a rental from the file:
    read clientId, carId
    client = clientRepo.find(clientId)
    car = carRepo.find(carId)
'''

'''
carRepo = None
clientRepo = None
rentalRepo = None

print('-' * 10 + " Clients " + '-' * 10)
print(clientRepo)
print('-' * 10 + " Cars " + '-' * 10)
print(carRepo)
print('-' * 10 + " Rentals " + '-' * 10)
print(rentalRepo)
'''
