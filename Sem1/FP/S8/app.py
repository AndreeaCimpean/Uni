from repositories import *
from services import *
from Client import *
from Rental import *
from Car import *
from datetime import date
from ui import *

clientRepo = Repository()
clientRepo.store((cl1 := Client(1, "Pop Maria", 20)))
clientRepo.store((cl2 := Client(2, "Vlad Maria", 25)))

carRepo = Repository()
carRepo.store( (car1 := Car(1, "CJ01ERT", "Dacia", "Lodgy", "red")) )
carRepo.store( (car2 := Car(1, "CJ01XVT", "Volvo", "XC60", "red")) )

rentalRepo = Repository
rentalRepo.store((r1 := Rental(1,date(2010,11,20), date(2010,11,30), cl1, car1)))
rentalRepo.store((r2 := Rental(2,date(2016,12,25), date(2017,11,20), cl1, car1)))

carService = CarService(carRepo)
clientService = ClientService(clientRepo)
rentalService = RentalService(rentalRepo, carRepo, clientRepo)

ui = UI(carService, clientService, rentalService)
ui.start()