from domain import *

class textRepository:
    def __init__(self, fileName):
        self._filename = fileName
        self._people = self._load_file()

    def _load_file(self):
        f = open(self._filename, "r")
        line = f.readline().strip()
        data = []
        while len(line) > 0:
            params = line.split(",")
            if params[2] == "ill":
                p = Person(params[0], params[1], params[2], 1)
            else:
                p = Person(params[0], params[1], params[2], 0)
            data.append(p)
            line = f.readline().strip()
        f.close()
        return data

    def get_people(self):
        return self._people

    def update_person_status(self, personId, status):
        for i in self._people:
            if i.id == personId:
                i.Status = status

    def update_person_ill_days(self, personId, days):
        for i in self._people:
            if i.id == personId:
                i.DaysIll = days

    def update_person_immunization(self, personId, immun):
        for i in self._people:
            if i.id == personId:
                i.Immunization = immun


    def save_file(self):
        f = open(self._filename,"w")
        for i in self._people:
            line = str(i.id) + "," + i.Immunization + ',' + i.Status + '\n'
            f.write(line)
        f.close()

