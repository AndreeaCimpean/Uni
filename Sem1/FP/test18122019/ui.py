from service import *
from repository import *

class UI:
    def __init__(self, driverServ, orderServ):
        self._driverService = driverServ
        self._orderService = orderServ

    def read_command(self):
        command = input("your command: ")
        idx = command.find(" ")
        if idx == -1:
            return (command,[])
        else:
            cmd = command[:idx]
            params = command[idx+1:].split(",")
        return (cmd, params)

    def start(self):
        while True:
            command = self.read_command()
            cmd = command[0]
            params = command[1]
            if cmd == "exit":
                return
            elif cmd == "add":
                self.add_order(params)
            elif cmd == "display":
                self.display_orders()
            elif cmd == "income":
                self.income_driver(params)

    def display_orders(self):
        for i in self._orderService.get_orders():
            print(i)

    def add_order(self, params):
        try:
            self._orderService.add_order(int(params[0]), int(params[1]))
        except ValueError as ve:
            print(ve)

    def income_driver(self, params):
        print(self._orderService.income_driver(int(params[0])))


driverRepo = DriverRepository("drivers.txt")
orderRepo = OrderRepository("orders.txt", driverRepo)
driverServ = DriverService(driverRepo)
orderServ = OrderService(orderRepo)
ui = UI(driverServ, orderServ)
ui.start()