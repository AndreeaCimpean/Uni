class BusService:
    def __init__(self, busRepo, routeRepo):
        self._busRepository = busRepo
        self._routeRepository = routeRepo

    def get_buses(self):
        return self._busRepository.get_buses()

    def buses_on_route(self, routeId):
        buses = []
        for i in self.get_buses():
            if i.routeCode == routeId:
                buses.append(i)
        return buses

    def length_travelled(self, busId):
        '''
        :param busId: the id of the given bus
        :return: an LengthTravelled object, having the attributes the bus and the length travelled
        '''
        bus = self._busRepository.get_bus_by_id(busId)
        route = self._routeRepository.get_route_by_id(bus.routeCode)
        return LengthTravelled(bus, route.Length*bus.Times)

class LengthTravelled:
    def __init__(self, bus, km):
        self._bus = bus
        self._km = km

    def __str__(self):
        return str(self._bus) + 'travelled: ' + str(self._km) + ' km'


class RouteService:
    def __init__(self, repo):
        self._repository = repo

    def get_routes(self):
        return self._repository.get_routes()