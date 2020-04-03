from service import *
from repository import *

class UI:
    def __init__(self, routeServ, busServ):
        self._routeService = routeServ
        self._busService = busServ

    def read_command(self):
        command = input("your command: ")
        idx = command.find(" ")
        if idx != -1:
            cmd = command[:idx]
            params = command[idx+1:].split(" ")
        else:
            cmd = command
            params = []
        return(cmd, params)

    def start(self):
        while True:
            command = self.read_command()
            cmd = command[0]
            params = command[1]
            if cmd == "exit":
                return
            elif cmd == "display" and params[0] != "bus":
                self.display_buses_on_route(int(params[0]))
            elif cmd == "display" and params[0] == "bus" and params[1] == "routes":
                self.display_bus_routes()
            elif cmd == "km":
                self.km_travelled(int(params[0]))
            else:
                print("Invalid command")

    def display_buses_on_route(self, routeId):
        for i in self._busService.buses_on_route(routeId):
            print(i)

    def display_bus_routes(self):
        for i in self._routeService.get_routes():
            print(i)

    def km_travelled(self, busId):
        print(self._busService.length_travelled(busId))



routeRepo = RoutesRepository("routes.txt")
busRepo = BusesRepository("buses.txt")
routeServ = RouteService(routeRepo)
busServ = BusService(busRepo, routeRepo)
ui = UI(routeServ, busServ)
ui.start()