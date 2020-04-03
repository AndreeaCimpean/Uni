from domain import *
import datetime

class RoomsRepository:
    def __init__(self, filename):
        self._filename = filename
        self._rooms = self._loadFile()

    def _loadFile(self):
        data = []
        f = open(self._filename, "r")
        line = f.readline().strip()
        while len(line) > 0:
            params = line.split(",")
            for i in params:
                i.strip()
            room = Room(int(params[0]), params[1])
            data.append(room)
            line = f.readline().strip()
        f.close()
        return data


class ReservationsRepository:
    def __init__(self, filename):
        self._filename = filename
        self._reservations = self._loadFile()

    def _loadFile(self):
        data = []
        f = open(self._filename, "r")
        line = f.readline().strip()
        while len(line) > 0:
            params = line.split(",")
            for param in params:
                param.strip()
            reservation = Reservation(params[0], int(params[1]), params[2], int(params[3]), )
            data.append(room)
            line = f.readline().strip()
        f.close()
        return data