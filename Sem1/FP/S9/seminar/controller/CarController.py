# from controller.UndoController import FunctionCall, Operation, CascadedOperation
from domain.Car import Car
from controller.UndoController import *

class CarController:
    def __init__(self, undoController, rentalController, validator, repository):
        self.__validator = validator
        self.__repository = repository
        self._rentalController = rentalController
        self._undoController = undoController
        
    def create(self, carId, licensePlate, carMake, carModel):
        car = Car(carId, licensePlate, carMake, carModel)
        self.__validator.validate(car)
        self.__repository.store(car)

        redo = FunctionCall(self.create, carId, licensePlate, carMake, carModel)
        undo = FunctionCall(self.delete, carId)
        op = Operation(undo, redo)
        self._undoController.recordOperation(op)

        return car
        
    def delete(self, carId, inUndoRedo=False):
        '''
            1. Delete the car from the repository
        '''
        car = self.__repository.delete(carId)

        undo = FunctionCall(self.create, carId, car.license, car.make, car.model)
        redo = FunctionCall(self.delete, carId, True)
        op = Operation(undo, redo)
        listOp = []
        listOp.append(op)

        '''
            2. Delete its rentals
            NB! This implementation is not transactional, i.e. the two delete operations are performed separately
        '''
        rentals = self._rentalController.filterRentals(None, car)

        for rent in rentals:
            undo = FunctionCall(self._rentalController.createRental, rent.id, rent.client, rent.car, rent.start, rent.end, False)
            redo = FunctionCall(self._rentalController.deleteRental, rent.id, False)
            op = Operation(undo, redo)
            listOp.append(op)

        cascadeOp = CascadedOperation(listOp)
        self._undoController.recordOperation(cascadeOp)

        if inUndoRedo == False:
            for rent in rentals:
                self._rentalController.deleteRental(rent.id, False)
        return car
       
    def update(self, car):
        '''
            NB! Undo/redo is also needed here
        '''
        pass
