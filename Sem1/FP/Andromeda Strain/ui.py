from services import *
from repository import *

class UI:
    def __init__(self, serv):
        self._service = serv

    def read_command(self):
        cmd = input("your command: ")
        idx = cmd.find(" ")
        if idx == -1:
            return (cmd, [])
        command = cmd[:idx]
        param = cmd[idx + 1:]
        return (command, param)

    def start(self):
        d = {"list":self.show_all_people, "simulate":self.simulate_day, "vaccinate":self.vaccinate_person}
        while True:
            cmd = self.read_command()
            command = cmd[0]
            param = cmd[1]
            if command == "exit":
                return
            else:
                d[command](param)


    def show_all_people(self, param):
        for i in self._service.get_people():
            print(i)

    def simulate_day(self, param):
        self._service.simulate_day()

    def vaccinate_person(self, personId):
        personId = int(personId)
        try:
            self._service.vaccinate_person(personId)
        except ValueError as ve:
            print(ve)

repo = textRepository("input.txt")
serv = Service(repo)
ui = UI(serv)
ui.start()