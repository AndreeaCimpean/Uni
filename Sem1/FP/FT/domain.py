class Reservation:
    def __init__(self, id, room, name, guests, arrival, departure):
        self._reservationId = id
        self.room = room
        self.name = name
        self.guests = guests
        self.arrival = arrival
        self.departure = departure

    @property
    def reservationId(self):
        return self._reservationId

    @property
    def room(self):
        return self._room

    @room.setter
    def room(self, value):
        self._room = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def guests(self):
        return self._guests

    @guests.setter
    def guests(self, value):
        self._guests = value

    @property
    def arrival(self):
        return self._arrival

    @arrival.setter
    def arrival(self, value):
        self._arrival = value

    @property
    def departure(self):
        return self._departure

    @departure.setter
    def departure(self, value):
        self._departure = value


class Room:
    def __init__(self, number, type):
        self._number = number
        self.type = type

    @property
    def number(self):
        return self._number

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value