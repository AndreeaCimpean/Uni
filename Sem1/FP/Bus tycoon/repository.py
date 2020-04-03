from domain import *

class RoutesRepository:
    def __init__(self, fileName):
        self._fileName = fileName
        self._routes = self._load_file()

    def _load_file(self):
        data = []
        f = open(self._fileName, "r")
        line = f.readline().strip()
        while len(line) > 0:
            params = line.split(",")
            r = Route(int(params[0]),int(params[1]))
            data.append(r)
            line = f.readline().strip()
        f.close()
        return data

    def get_routes(self):
        return self._routes

    def get_route_by_id(self, routeId):
        '''
        :param routeId: the id of the given route
        :return: the route if found
                None otherwise
        '''
        for i in self._routes:
            if i.routeId == routeId:
                return i
        return None


class BusesRepository:
    def __init__(self, fileName):
        self._fileName = fileName
        self._buses = self._load_file()

    def _load_file(self):
        data = []
        f = open(self._fileName, "r")
        line = f.readline().strip()
        while len(line) > 0:
            params = line.split(",")
            b = Bus(int(params[0]),int(params[1]),params[2], int(params[3]))
            data.append(b)
            line = f.readline().strip()
        f.close()
        return data

    def get_buses(self):
        return self._buses

    def get_bus_by_id(self, busId):
        '''
        :param busId: the id of the given bus
        :return: the bus if found
                None otherwise
        '''
        for i in self._buses:
            if i.busId == busId:
                return i
        return None